#!/usr/bin/env python3
"""Fail on obvious private paths, credentials and runtime files in tracked source.

This supplements human review; it is not a comprehensive secret scanner.
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN_PARTS = {".venv", "runtime", "benchmarks", "test-output", "__pycache__",
                   ".mango-swarms", ".ssh", ".aws"}
PATTERNS = {
    "private home path": re.compile(r"/Users/[A-Za-z][A-Za-z0-9_.-]+/|[A-Z]:\\Users\\[A-Za-z][^\\\s]+\\"),
    "OpenAI-style key": re.compile(r"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}"),
    "GitHub token": re.compile(r"\b(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def audit():
    listing = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True)
    if listing.returncode:
        raise SystemExit("Audit requires a Git checkout with an explicitly staged/tracked file set.")
    files = [Path(name) for name in listing.stdout.decode().split("\0") if name]
    if not files:
        raise SystemExit("No staged/tracked files to audit.")
    problems = []
    for relative in files:
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            problems.append(str(relative) + ": runtime/private directory")
        if relative.name.startswith(".env") or relative.name in ("auth.json", "credentials.json"):
            problems.append(str(relative) + ": credential/config file")
        path = ROOT / relative
        if path.is_symlink():
            problems.append(str(relative) + ": unexpected symlink")
            continue
        raw = path.read_bytes()
        if len(raw) > 1024 * 1024:
            problems.append(str(relative) + ": unexpected large file")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(str(relative) + ": unexpected binary file")
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                problems.append(str(relative) + ": " + label)
    if problems:
        raise SystemExit("Public source audit failed:\n" + "\n".join(problems))
    print("PASS: " + str(len(files)) + " tracked text files; no flagged paths, tokens or runtime files.")


if __name__ == "__main__":
    audit()
