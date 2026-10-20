"""Cross-platform state, locking, subprocesses and safe artifact handling."""

from contextlib import contextmanager
from datetime import datetime, timezone
import errno
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import signal
import subprocess
import sys
import time
import uuid


class SwarmError(Exception):
    """An actionable failure that is safe to show without a traceback."""


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def state_home():
    configured = os.environ.get("MANGO_SWARMS_HOME")
    if configured:
        return Path(configured).expanduser().resolve()
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local")))
    elif sys.platform == "darwin":
        base = Path.home() / "Library/Application Support"
    else:
        base = Path(os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local/state")))
    return base / "MangoMagic" / "swarms"


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with temporary.open("x", encoding="utf-8", newline="") as stream:
            stream.write(text)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def write_json(path, value):
    atomic_write(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


class FileLock:
    """OS-released lock; no PID guessing and no stale lock-file deletion."""

    def __init__(self, path, timeout=0):
        self.path = Path(path)
        self.timeout = timeout
        self.stream = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.stream = self.path.open("a+b")
        self.stream.seek(0, 2)
        if self.stream.tell() == 0:
            self.stream.write(b"\0")
            self.stream.flush()
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    self.stream.seek(0)
                    msvcrt.locking(self.stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except OSError as error:
                if error.errno not in (errno.EACCES, errno.EAGAIN, errno.EDEADLK):
                    self.stream.close()
                    raise
                if time.monotonic() >= deadline:
                    self.stream.close()
                    raise SwarmError("Busy: another workflow owns this lock. Retry after it finishes.")
                time.sleep(0.1)

    def __exit__(self, *_):
        try:
            if os.name == "nt":
                import msvcrt
                self.stream.seek(0)
                msvcrt.locking(self.stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.stream, fcntl.LOCK_UN)
        finally:
            self.stream.close()


def process(command, prompt="", cwd=None, env=None, timeout=300):
    """Run argv without a shell; terminate this child's process tree on cancellation."""
    settings = {"start_new_session": True} if os.name != "nt" else {
        "creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
    child = subprocess.Popen(
        command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, encoding="utf-8", errors="replace", cwd=cwd, env=env, **settings)
    try:
        out, err = child.communicate(prompt, timeout=timeout)
        return child.returncode, out, err
    except (subprocess.TimeoutExpired, KeyboardInterrupt):
        if child.poll() is None:
            if os.name == "nt":
                subprocess.run(["taskkill", "/PID", str(child.pid), "/T", "/F"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                try:
                    os.killpg(child.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
        try:
            child.communicate(timeout=3)
        except subprocess.TimeoutExpired:
            if os.name != "nt":
                try:
                    os.killpg(child.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            else:
                child.kill()
            child.communicate()
        raise


def relative_path(name):
    """Use portable forward-slash paths and reject sensitive/control locations."""
    if not isinstance(name, str) or not name or "\\" in name or ":" in name or "\0" in name:
        raise SwarmError("Artifact paths must be portable relative paths.")
    path = PurePosixPath(name)
    if path.is_absolute() or name != path.as_posix() or any(p in ("", ".", "..") for p in name.split("/")):
        raise SwarmError("Artifact path escapes or ambiguously addresses the workspace.")
    protected = {".git", ".codex", ".agents", ".aws", ".ssh", ".mango-swarms", ".venv",
                 "node_modules", "__pycache__"}
    reserved = {"CON", "PRN", "AUX", "NUL"} | {
        prefix + str(i) for prefix in ("COM", "LPT") for i in range(1, 10)}
    for part in path.parts:
        if part.lower() in protected or part.lower().startswith(".env"):
            raise SwarmError("Protected configuration or secret path is not an artifact target.")
        if part.rstrip(" .") != part or part.split(".")[0].upper() in reserved:
            raise SwarmError("Artifact path is not portable to Windows.")
        if any(c in part for c in '<>"|?*') or any(ord(c) < 32 for c in part):
            raise SwarmError("Artifact path contains unsupported characters.")
    return path.as_posix()


def safe_target(root, name):
    name = relative_path(name)
    target = root
    for part in PurePosixPath(name).parts:
        target = target / part
        if target.is_symlink():
            raise SwarmError("Refusing to follow a symlink in an artifact/context path.")
    if not target.resolve().is_relative_to(root.resolve()):
        raise SwarmError("Path is outside the selected workspace.")
    return target


def digest(content):
    return hashlib.sha256(content).hexdigest()


def read_context(workspace, names, limit=24000):
    """Read only files explicitly selected by the human; never crawl a project."""
    context, original = {}, {}
    for name in names:
        name = relative_path(name)
        path = safe_target(workspace, name)
        if not path.is_file():
            raise SwarmError("Context file not found: " + name)
        if path.stat().st_size > limit:
            raise SwarmError("Context is too large; choose a smaller excerpt.")
        data = path.read_bytes()
        try:
            context[name] = data.decode("utf-8")
        except UnicodeDecodeError:
            raise SwarmError("Context files must be UTF-8 text.")
        original[name] = digest(data)
    if sum(len(text) for text in context.values()) > limit:
        raise SwarmError("Combined context exceeds the configured character limit.")
    return context, original


def apply_artifacts(workspace, files, original, backup):
    """Preflight the entire batch, then write; preserve existing unselected/user-edited files."""
    targets = []
    for name, content in files.items():
        target = safe_target(workspace, name)
        if target.exists():
            if not target.is_file() or name not in original:
                raise SwarmError("Existing file was not selected as context: " + name)
            data = target.read_bytes()
            if digest(data) != original[name]:
                raise SwarmError("File changed after the workflow started; refusing overwrite: " + name)
        else:
            data = None
            if name in original:
                raise SwarmError("Context file was removed during the workflow: " + name)
        targets.append((name, target, content, data))
    # Backups only contain explicitly selected context; private runtime state.
    for name, target, content, previous in targets:
        if previous is not None:
            previous_path = backup / name
            previous_path.parent.mkdir(parents=True, exist_ok=True)
            previous_path.write_bytes(previous)
        # Recheck directly before writing to reduce accidental concurrent-edit races.
        safe_target(workspace, name)
        if previous is None:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("x", encoding="utf-8", newline="") as stream:
                stream.write(content)
        else:
            if digest(target.read_bytes()) != original[name]:
                raise SwarmError("File changed during application: " + name)
            atomic_write(target, content)


def check_commands(workspace, filename):
    path = safe_target(workspace, relative_path(filename))
    try:
        commands = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        raise SwarmError("Checks file must contain a JSON array of argument arrays.")
    if not isinstance(commands, list) or not 1 <= len(commands) <= 20:
        raise SwarmError("Supply 1-20 verification commands.")
    if not all(isinstance(c, list) and c and all(isinstance(a, str) and a for a in c)
               for c in commands):
        raise SwarmError("Each verification command must be a nonempty string argument array.")
    return commands
