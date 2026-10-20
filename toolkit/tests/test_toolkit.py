from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from mango_swarms import cli, providers, workflow
from mango_swarms.runtime import (FileLock, SwarmError, apply_artifacts, digest, process,
                                  read_context, relative_path, safe_target)


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROUTES = {
    "swarm-ollama": ("ollama", "ollama", "ollama"),
    "swarm-ollama-claude": ("claude", "ollama", "claude"),
    "swarm-ollama-gpt": ("codex", "ollama", "codex"),
    "swarm-gpt": ("codex", "codex", "codex"),
    "swarm-claude": ("claude", "claude", "claude"),
}


def response_for(schema, prompt=""):
    fields = schema["properties"]
    if "tasks" in fields:
        return {"tasks": [
            {"id": "alpha", "title": "Alpha", "instructions": "Write alpha.txt containing alpha newline"},
            {"id": "beta", "title": "Beta", "instructions": "Write beta.txt containing beta newline"},
        ]}
    if "files" in fields:
        data = json.loads(prompt.split("\n\n")[-1])
        name = data["task"]["id"]
        return {"summary": "Built " + name,
                "files": [{"path": name + ".txt", "content": name + "\n"}]}
    if "approved" in fields:
        return {"approved": True, "summary": "Artifacts satisfy the fixture goal.", "findings": []}
    return {"answer": "MangoMagic benchmark OK"}


class FixtureProvider:
    def __init__(self, name):
        self.name, self.calls = name, []

    def doctor(self):
        return {"provider": self.name, "fixture": True}

    def generate(self, prompt, schema, run, label):
        self.calls.append(label)
        return response_for(schema, prompt)


class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="mango-swarms-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.workspace = self.root / "project with spaces"
        self.workspace.mkdir()
        self.home = self.root / "private-state"

    def args(self, mode="swarm-ollama", *extra):
        return cli.parser().parse_args([mode, str(self.workspace), "-g", "Create alpha and beta", *extra])

    def fake_providers(self):
        return {name: FixtureProvider(name) for name in ("ollama", "codex", "claude")}

    def test_all_five_routes_use_expected_planner_worker_reviewer_providers(self):
        self.assertEqual(set(workflow.MODES), set(EXPECTED_ROUTES))
        for mode, route in EXPECTED_ROUTES.items():
            with self.subTest(mode=mode):
                adapters = self.fake_providers()
                code, run = workflow.execute(self.args(mode), adapters, self.home, emit=lambda _: None)
                self.assertEqual(code, 0)
                self.assertEqual((run / "artifacts/alpha.txt").read_text(), "alpha\n")
                self.assertEqual((run / "artifacts/beta.txt").read_text(), "beta\n")
                self.assertIn("plan", adapters[route[0]].calls)
                self.assertIn("worker-alpha", adapters[route[1]].calls)
                self.assertIn("worker-beta", adapters[route[1]].calls)
                self.assertIn("review", adapters[route[2]].calls)
                self.assertEqual(sum(len(p.calls) for p in adapters.values()), 4)
                self.assertEqual(json.loads((run / "report.json").read_text())["status"], "staged")
                self.assertFalse((self.workspace / "alpha.txt").exists())

    def test_claude_only_doctor_requires_no_ollama_or_codex(self):
        output = io.StringIO()
        with patch("mango_swarms.cli.Claude", return_value=FixtureProvider("claude")) as claude, \
                patch("mango_swarms.cli.Ollama", side_effect=AssertionError("Ollama must not initialize")), \
                patch("mango_swarms.cli.Codex", side_effect=AssertionError("Codex must not initialize")), \
                patch.dict(os.environ, {"MANGO_CLAUDE_MODEL": "selected-claude-model"}), \
                redirect_stdout(output):
            self.assertEqual(cli.main(["swarm-claude", "--doctor"]), 0)
        claude.assert_called_once_with("selected-claude-model", 300)
        report = json.loads(output.getvalue())
        self.assertEqual(report["providers"], [{"provider": "claude", "fixture": True}])
        self.assertEqual(report["generation_requests"], 0)

    def test_dry_run_reports_local_capacity_only_for_ollama_routes(self):
        for mode, route in EXPECTED_ROUTES.items():
            output = io.StringIO()
            with self.subTest(mode=mode), redirect_stdout(output), \
                    patch("mango_swarms.cli.make_providers", side_effect=AssertionError("No provider calls")):
                self.assertEqual(cli.main([mode, "--dry-run"]), 0)
            report = json.loads(output.getvalue())
            self.assertEqual(tuple(report["stages"].values()), route)
            self.assertEqual(report["shared_ollama_requests"], int("ollama" in route))
            self.assertEqual(report["num_ctx"], 8192 if "ollama" in route else None)
            self.assertEqual(report["model_requests"], 0)

    def test_apply_and_user_authored_check_run_end_to_end(self):
        (self.workspace / "checks.json").write_text(json.dumps([
            ["{python}", "-c",
             "from pathlib import Path; assert Path('alpha.txt').read_bytes()==b'alpha\\n'; "
             "assert Path('beta.txt').read_bytes()==b'beta\\n'; print('PASS')"]]))
        args = self.args("swarm-ollama-gpt", "--apply", "--check-file", "checks.json")
        code, run = workflow.execute(args, self.fake_providers(), self.home, emit=lambda _: None)
        self.assertEqual(code, 0)
        report = json.loads((run / "report.json").read_text())
        self.assertEqual(report["status"], "verified")
        self.assertEqual(report["checks"][0]["exit_code"], 0)
        self.assertEqual(report["checks"][0]["stdout"].strip(), "PASS")

    def test_rejected_review_never_applies(self):
        adapters = self.fake_providers()
        original = adapters["codex"].generate
        def reject(prompt, schema, run, label):
            if label == "review":
                return {"approved": False, "summary": "Missing requirement", "findings": ["Fix it"]}
            return original(prompt, schema, run, label)
        adapters["codex"].generate = reject
        code, run = workflow.execute(self.args("swarm-gpt", "--apply"), adapters,
                                     self.home, emit=lambda _: None)
        self.assertEqual(code, 3)
        self.assertFalse((self.workspace / "alpha.txt").exists())
        self.assertEqual(json.loads((run / "report.json").read_text())["status"], "needs_review")

    def test_existing_unselected_file_preserved_and_batch_preflight(self):
        (self.workspace / "beta.txt").write_text("user work\n")
        with self.assertRaisesRegex(SwarmError, "not selected"):
            workflow.execute(self.args("swarm-gpt", "--apply"), self.fake_providers(),
                             self.home, emit=lambda _: None)
        self.assertEqual((self.workspace / "beta.txt").read_text(), "user work\n")
        self.assertFalse((self.workspace / "alpha.txt").exists())

    def test_changed_selected_file_preserved(self):
        path = self.workspace / "file.txt"
        path.write_text("before")
        context, original = read_context(self.workspace, ["file.txt"])
        path.write_text("human edit")
        with self.assertRaisesRegex(SwarmError, "changed"):
            apply_artifacts(self.workspace, {"file.txt": "model"}, original, self.root / "backup")
        self.assertEqual(path.read_text(), "human edit")

    def test_selected_file_backup_and_application(self):
        path = self.workspace / "file.txt"
        path.write_text("before")
        _, original = read_context(self.workspace, ["file.txt"])
        apply_artifacts(self.workspace, {"file.txt": "after\n"}, original, self.root / "backup")
        self.assertEqual(path.read_bytes(), b"after\n")
        self.assertEqual((self.root / "backup/file.txt").read_bytes(), b"before")

    def test_protected_nonportable_and_traversal_paths_refused(self):
        for name in ("../escape", "/escape", "C:/escape", "a\\b", "a/../b", ".env",
                     ".env.local", ".git/config", ".codex/config.toml", "CON", "x/NUL.txt",
                     "hello.", "a//b", "./file", "a:b", "a?b", "a\x00b"):
            with self.subTest(name=name), self.assertRaises(SwarmError):
                relative_path(name)
        self.assertEqual(relative_path("src/main.py"), "src/main.py")

    def test_symlink_is_not_followed(self):
        outside = self.root / "outside"
        outside.mkdir()
        try:
            (self.workspace / "linked").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable to this Windows account.")
        with self.assertRaisesRegex(SwarmError, "symlink"):
            safe_target(self.workspace, "linked/file.txt")

    def test_plan_and_artifact_validation(self):
        for task_id in ("implement_greeting", "implement-greeting", "task1"):
            plan = {"tasks": [{"id": task_id, "title": "Greeting", "instructions": "Write greeting.py"}]}
            self.assertEqual(workflow.validate_plan(plan, 1)[0]["id"], task_id)
        with self.assertRaises(SwarmError):
            workflow.validate_plan({"tasks": []}, 2)
        with self.assertRaises(SwarmError):
            workflow.validate_plan({"tasks": [
                {"id": "../bad", "title": "bad", "instructions": "bad"}]}, 2)
        with self.assertRaises(SwarmError):
            workflow.validate_artifacts({"summary": "bad", "files": [
                {"path": "A.txt", "content": "A"}, {"path": "a.txt", "content": "a"}]})
        with self.assertRaises(SwarmError):
            workflow.validate_review({"approved": "true", "summary": "bad", "findings": []})

    def test_check_failure_is_recorded_and_not_success(self):
        (self.workspace / "checks.json").write_text(json.dumps([["{python}", "-c", "raise SystemExit(7)"]]))
        code, run = workflow.execute(self.args("swarm-gpt", "--apply", "--check-file", "checks.json"),
                                     self.fake_providers(), self.home, emit=lambda _: None)
        self.assertEqual(code, 3)
        report = json.loads((run / "report.json").read_text())
        self.assertEqual(report["status"], "check_failed")
        self.assertEqual(report["checks"][0]["exit_code"], 7)

    def test_goal_continuation_and_history(self):
        first = workflow.execute(self.args(), self.fake_providers(), self.home, emit=lambda _: None)[1]
        args = cli.parser().parse_args(["swarm-ollama", str(self.workspace), "--continue"])
        second = workflow.execute(args, self.fake_providers(), self.home, emit=lambda _: None)[1]
        self.assertNotEqual(first, second)
        self.assertEqual((first / "GOAL.md").read_bytes(), (second / "GOAL.md").read_bytes())

    def test_cross_process_lock_released_on_exit(self):
        lock = self.root / "lock"
        script = ("from pathlib import Path; from mango_swarms.runtime import FileLock; "
                  "import sys; "
                  "lock=FileLock(Path(sys.argv[1])); lock.__enter__(); print('locked',flush=True); "
                  "sys.stdin.readline()")
        child = subprocess.Popen([sys.executable, "-c", script, str(lock)], cwd=ROOT,
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        try:
            self.assertEqual(child.stdout.readline().strip(), "locked")
            with self.assertRaises(SwarmError):
                with FileLock(lock):
                    pass
        finally:
            child.communicate("\n", timeout=10)
        with FileLock(lock):
            pass

    def test_cli_providers_use_real_subprocess_contract_without_network(self):
        fixture = [sys.executable, str(ROOT / "tests/fake_cli.py")]
        with patch("mango_swarms.providers.find_cli", return_value=fixture):
            for kind in (providers.Codex, providers.Claude):
                provider = kind()
                self.assertEqual(provider.doctor()["location"], "cloud")
                self.root.mkdir(exist_ok=True)
                result = provider.generate("fixture", workflow.obj({"answer": workflow.TEXT}),
                                           self.root, provider.name)
                self.assertEqual(result, {"answer": "fixture"})
        codex = provider = None

    def test_secret_env_overrides_are_removed(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "fixture", "CODEX_API_KEY": "fixture",
                                     "ANTHROPIC_API_KEY": "fixture",
                                     "ANTHROPIC_BASE_URL": "https://example.invalid"}):
            environment = providers.clean_environment()
        for key in ("OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL"):
            self.assertNotIn(key, environment)

    def test_timeout_terminates_child(self):
        with self.assertRaises(subprocess.TimeoutExpired):
            process([sys.executable, "-c", "import time; time.sleep(30)"], timeout=0.1)

    def test_diagnostic_timeout_has_no_traceback_or_command_echo(self):
        import io
        from contextlib import redirect_stderr
        output = io.StringIO()
        with patch("mango_swarms.cli.main", side_effect=subprocess.TimeoutExpired(
                ["private-command-argument"], 20)), redirect_stderr(output):
            self.assertEqual(cli.entry(), 1)
        self.assertIn("timed out", output.getvalue())
        self.assertNotIn("private-command-argument", output.getvalue())

    def test_windows_npm_shim_resolved_without_command_shell(self):
        shim = self.root / "codex.cmd"
        shim.write_text("@echo off\n")
        entry = self.root / "node_modules/@openai/codex/bin/codex.js"
        entry.parent.mkdir(parents=True)
        entry.write_text("// fixture")
        with patch.dict(os.environ, {"MANGO_CODEX_BIN": str(shim)}), \
                patch("mango_swarms.providers.shutil.which", return_value="node.exe"):
            self.assertEqual(providers.find_cli("codex"), ["node.exe", str(entry.resolve())])

    def test_installer_builds_all_five_commands_and_preserves_unrelated_files(self):
        clone = self.root / "clone with spaces"
        shutil.copytree(ROOT / "mango_swarms", clone / "mango_swarms",
                        ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy(ROOT / "launch.py", clone / "launch.py")
        (clone / "scripts").mkdir()
        shutil.copy(ROOT / "scripts/install.py", clone / "scripts/install.py")
        setup = subprocess.run([sys.executable, str(clone / "scripts/install.py")],
                               capture_output=True, text=True, timeout=30)
        self.assertEqual(setup.returncode, 0, setup.stderr)
        for name in EXPECTED_ROUTES:
            command = clone / "bin" / (name + (".cmd" if os.name == "nt" else ""))
            argv = ["cmd.exe", "/d", "/c", str(command), "--dry-run"] if os.name == "nt" else [
                str(command), "--dry-run"]
            result = subprocess.run(argv, capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["mode"], name)
        command.write_text("user work")
        second = subprocess.run([sys.executable, str(clone / "scripts/install.py")],
                                capture_output=True, text=True, timeout=15)
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(command.read_text(), "user work")


    def test_nested_toolkit_relocation_and_reinstall_preserve_state_and_user_files(self):
        repository = self.root / "repository with spaces"
        toolkit = repository / "toolkit"
        shutil.copytree(ROOT / "mango_swarms", toolkit / "mango_swarms",
                        ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy(ROOT / "launch.py", toolkit / "launch.py")
        (toolkit / "scripts").mkdir()
        shutil.copy(ROOT / "scripts/install.py", toolkit / "scripts/install.py")
        (repository / "README.md").write_text("repository overview")
        self.home.mkdir()
        sentinel = self.home / "existing-user-state.txt"
        sentinel.write_text("keep saved state")
        environment = dict(os.environ, MANGO_SWARMS_HOME=str(self.home),
                           MANGO_CLAUDE_MODEL="user-selection")
        subprocess.run([sys.executable, str(toolkit / "scripts/install.py")],
                       env=environment, check=True, capture_output=True, timeout=30)
        notes = toolkit / "bin" / "personal-notes.txt"
        notes.write_text("unrelated user file")
        relocated = self.root / "relocated repository with spaces"
        shutil.move(str(repository), relocated)
        toolkit = relocated / "toolkit"
        subprocess.run([sys.executable, str(toolkit / "scripts/install.py")],
                       env=environment, check=True, capture_output=True, timeout=30)
        for name, route in EXPECTED_ROUTES.items():
            command = toolkit / "bin" / (name + (".cmd" if os.name == "nt" else ""))
            argv = ["cmd.exe", "/d", "/c", str(command), "--dry-run"] if os.name == "nt" else [
                str(command), "--dry-run"]
            result = subprocess.run(argv, env=environment, cwd=relocated,
                                    capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(tuple(report["stages"].values()), route)
            self.assertEqual(Path(report["state_home"]), self.home.resolve())
            self.assertEqual(report["model_requests"], 0)
        self.assertEqual(sentinel.read_text(), "keep saved state")
        self.assertEqual((toolkit / "bin/personal-notes.txt").read_text(), "unrelated user file")
        self.assertEqual((relocated / "README.md").read_text(), "repository overview")


class HTTPIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="mango-http-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.active = 0
        self.maximum = 0
        self.counter_lock = threading.Lock()
        owner = self
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *_):
                pass
            def do_GET(self):
                self.respond({"version": "test"} if self.path.endswith("version") else {
                    "models": [{"name": "fixture:latest", "size": 1}]})
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                if self.path.endswith("show"):
                    self.respond({"model_info": {}, "remote_model": getattr(owner, "remote", None)})
                    return
                with owner.counter_lock:
                    owner.active += 1
                    owner.maximum = max(owner.maximum, owner.active)
                time.sleep(0.02)
                schema = body["format"]
                result = response_for(schema, body["messages"][0]["content"])
                with owner.counter_lock:
                    owner.active -= 1
                self.respond({"message": {"content": json.dumps(result)}, "eval_count": 10,
                              "eval_duration": 100000000, "done": True})
            def respond(self, data):
                payload = json.dumps(data).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.url = "http://127.0.0.1:" + str(self.server.server_port)

    def test_real_launcher_http_adapter_and_artifacts(self):
        workspace = self.root / "workspace"
        workspace.mkdir()
        result = subprocess.run(
            [sys.executable, str(ROOT / "launch.py"), "swarm-ollama", str(workspace),
             "-g", "Create the fixture files", "--ollama-model", "fixture",
             "--ollama-url", self.url, "--num-ctx", "32768", "--apply"],
            env=dict(os.environ, MANGO_SWARMS_HOME=str(self.root / "state")),
            capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((workspace / "alpha.txt").read_bytes(), b"alpha\n")
        self.assertEqual((workspace / "beta.txt").read_bytes(), b"beta\n")
        self.assertEqual(self.maximum, 1)

    def test_remote_model_requires_explicit_opt_in(self):
        self.remote = "provider-model"
        provider = providers.Ollama("fixture", self.root, self.url)
        with self.assertRaisesRegex(SwarmError, "cloud"):
            provider.doctor()
        provider.allow_cloud = True
        self.assertEqual(provider.doctor()["location"], "cloud")

    def test_unsafe_endpoints_rejected(self):
        for endpoint in ("https://example.com", "http://0.0.0.0:11434",
                         "http://user:pass@localhost:11434", self.url + "/other"):
            with self.assertRaises(SwarmError):
                providers.Ollama("fixture", self.root, endpoint)

    def test_shared_gate_serializes_concurrent_calls(self):
        provider = providers.Ollama("fixture", self.root, self.url)
        schema = workflow.obj({"answer": workflow.TEXT})
        with ThreadPoolExecutor(max_workers=3) as pool:
            values = list(pool.map(lambda n: provider.generate("fixture", schema, self.root,
                                                               "sample-" + str(n)), range(3)))
        self.assertEqual(len(values), 3)
        self.assertEqual(self.maximum, 1)

    def test_context_budget_guard(self):
        provider = providers.Ollama("fixture", self.root, self.url, context=2048, output_tokens=1024)
        with self.assertRaisesRegex(SwarmError, "context budget"):
            provider.generate("x" * 2000, workflow.obj({"answer": workflow.TEXT}), self.root, "too-big")


if __name__ == "__main__":
    unittest.main()
