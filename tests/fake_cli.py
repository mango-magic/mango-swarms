"""Offline CLI contract fixture. Never contacts a model provider."""
import json
import os
from pathlib import Path
import sys

arguments = sys.argv[1:]
if arguments == ["login", "status"]:
    print("Logged in using ChatGPT")
elif arguments == ["auth", "status", "--json"]:
    print(json.dumps({"loggedIn": True, "authMethod": "claude.ai"}))
elif arguments == ["exec", "--help"]:
    print("--ignore-user-config --output-schema --ephemeral")
elif arguments == ["--help"]:
    print("--safe-mode --json-schema --tools")
else:
    sys.stdin.read()
    output = {"answer": "fixture"}
    if "--output-last-message" in arguments:
        Path(arguments[arguments.index("--output-last-message") + 1]).write_text(json.dumps(output))
    else:
        print(json.dumps({"structured_output": output, "is_error": False}))
