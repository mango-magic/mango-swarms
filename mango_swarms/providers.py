"""Documented provider interfaces. No credential files, automatic downloads or fallbacks."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

from .runtime import FileLock, SwarmError, process, write_json


def parse_json(text):
    text = text.strip()
    if text.startswith("```json\n") and text.endswith("\n```"):
        text = text[8:-4]
    elif text.startswith("```\n") and text.endswith("\n```"):
        text = text[4:-4]
    try:
        value = json.loads(text)
    except (ValueError, TypeError):
        raise SwarmError("Provider returned invalid JSON; inspect the private run report.")
    if not isinstance(value, dict):
        raise SwarmError("Provider result must be a JSON object.")
    return value


def find_cli(name):
    configured = os.environ.get("MANGO_" + name.upper() + "_BIN")
    candidate = configured or (shutil.which(name + ".exe") if os.name == "nt" else None) or shutil.which(name)
    if candidate and Path(candidate).is_file():
        candidate = Path(candidate).resolve()
        if candidate.suffix.lower() in (".cmd", ".bat"):
            # Avoid cmd.exe parsing/injection for Windows npm shims. Invoke the
            # package's JavaScript entry through node.exe with an argv vector.
            package = {"codex": "@openai/codex/bin/codex.js",
                       "claude": "@anthropic-ai/claude-code/cli.js"}[name]
            entry = candidate.parent / "node_modules" / package
            node = shutil.which("node")
            if entry.is_file() and node:
                return [node, str(entry)]
            raise SwarmError("Cannot safely resolve the Windows " + name +
                             " npm shim. Install the official native CLI, or set MANGO_" +
                             name.upper() + "_BIN to its executable.")
        return [str(candidate)]
    if name == "codex":
        for candidate in (
            "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex",
            "/Applications/Codex.app/Contents/Resources/codex",
        ):
            if Path(candidate).is_file():
                return [candidate]
    raise SwarmError(name + " is not installed/on PATH. See docs/setup.md; nothing was installed.")


def clean_environment():
    blocked = {
        "OPENAI_API_KEY", "CODEX_API_KEY", "OPENAI_BASE_URL", "OPENAI_API_BASE",
        "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL",
        "CLAUDE_CODE_OAUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX",
        "CLAUDE_CODE_USE_FOUNDRY",
    }
    environment = {key: value for key, value in os.environ.items()
                   if key not in blocked and not key.startswith("CODEX_INTERNAL_")}
    environment["RUST_LOG"] = "warn"
    return environment


class Ollama:
    name = "ollama"

    def __init__(self, model, home, endpoint="http://127.0.0.1:11434",
                 context=4096, output_tokens=2048, timeout=300, allow_cloud=False):
        url = urllib.parse.urlsplit(endpoint)
        if (url.scheme != "http" or url.hostname not in ("127.0.0.1", "localhost", "::1")
                or url.username or url.password or url.path not in ("", "/")
                or url.query or url.fragment):
            raise SwarmError("Ollama endpoint must be a plain loopback HTTP URL.")
        if not model:
            raise SwarmError("Choose an installed Ollama model with --ollama-model NAME.")
        self.model, self.home, self.endpoint = model, home, endpoint.rstrip("/")
        self.context, self.output_tokens = context, output_tokens
        self.timeout, self.allow_cloud = timeout, allow_cloud
        self._opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def request(self, method, body=None, timeout=None):
        request = urllib.request.Request(
            self.endpoint + "/api/" + method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={"Content-Type": "application/json"})
        try:
            with self._opener.open(request, timeout=timeout or self.timeout) as response:
                raw = response.read(4 * 1024 * 1024 + 1)
            if len(raw) > 4 * 1024 * 1024:
                raise SwarmError("Ollama response exceeds the 4 MiB safety limit.")
            value = json.loads(raw)
            if not isinstance(value, dict):
                raise SwarmError("Ollama returned an unexpected response shape.")
            return value
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            raise SwarmError("Ollama request failed (" + type(error).__name__ +
                             "). Start Ollama, check --doctor, and retry; no fallback was used.")

    def doctor(self):
        version = self.request("version", timeout=5).get("version", "unknown")
        models = self.request("tags", timeout=5).get("models", [])
        matching = [item for item in models if item.get("name") in
                    (self.model, self.model + ":latest")]
        if not matching:
            raise SwarmError("Selected model is not installed in Ollama. Use ollama list; "
                             "choose or explicitly download a model yourself.")
        details = self.request("show", {"model": self.model}, timeout=10)
        remote = ("cloud" in self.model.lower() or bool(details.get("remote_model"))
                  or bool(details.get("remote_host")) or bool(matching[0].get("remote_model"))
                  or bool(matching[0].get("remote_host")))
        if remote and not self.allow_cloud:
            raise SwarmError("This Ollama model routes to cloud. --allow-ollama-cloud is "
                             "required; prompts leave the machine and provider costs/limits apply.")
        return {"provider": self.name, "version": version, "model": self.model,
                "location": "cloud" if remote else "local", "local_inference_slots": 1}

    def generate(self, prompt, schema, run, label):
        # Conservative guard, not a tokenizer. Reserve output and template space.
        if len(prompt.encode("utf-8")) > self.context - self.output_tokens - 512:
            raise SwarmError("Prompt exceeds the conservative local context budget. "
                             "Reduce context/artifact size or explicitly increase --num-ctx.")
        start = time.monotonic()
        # Every process using this state home shares one local request slot.
        with FileLock(self.home / "locks/ollama-inference.lock", timeout=self.timeout):
            response = self.request("chat", {
                "model": self.model, "messages": [{"role": "user", "content": prompt}],
                "format": schema, "stream": False, "think": False,
                "options": {"num_ctx": self.context, "num_predict": self.output_tokens,
                            "temperature": 0.2},
                "keep_alive": "5m",
            })
        content = response.get("message", {}).get("content", "")
        result = parse_json(content)
        metrics = {key: response.get(key) for key in (
            "total_duration", "load_duration", "prompt_eval_count", "prompt_eval_duration",
            "eval_count", "eval_duration") if response.get(key) is not None}
        metrics.update(provider=self.name, model=self.model,
                       wall_seconds=round(time.monotonic() - start, 3))
        write_json(run / (label + "-metrics.json"), metrics)
        return result


class Codex:
    name = "codex"

    def __init__(self, model=None, timeout=300):
        self.model, self.timeout = model, timeout
        self.binary = find_cli("codex")
        self.environment = clean_environment()

    def doctor(self):
        code, out, err = process(self.binary + ["login", "status"],
                                 env=self.environment, timeout=20)
        if code or "Logged in using ChatGPT" not in out + err:
            raise SwarmError("Codex ChatGPT login required. Run codex login yourself and "
                             "choose ChatGPT. API-key billing is not accepted.")
        code, help_text, _ = process(self.binary + ["exec", "--help"],
                                      env=self.environment, timeout=20)
        required = ("--ignore-user-config", "--output-schema", "--ephemeral")
        if code or any(flag not in help_text for flag in required):
            raise SwarmError("Update the official Codex CLI: this build lacks required batch options.")
        return {"provider": self.name, "authentication": "ChatGPT",
                "model": self.model or "CLI default", "location": "cloud"}

    def command(self, schema_path, output_path):
        command = self.binary + ["--no-daemon", "-a", "never", "-s", "read-only",
                   "-c", 'model_provider="openai"', "-c", 'forced_login_method="chatgpt"',
                   "-c", 'web_search="disabled"']
        for feature in ("shell_tool", "apps", "plugins", "multi_agent", "hooks", "computer_use"):
            command.extend(["--disable", feature])
        if self.model:
            command.extend(["-m", self.model])
        command.extend(["exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
                        "--color", "never", "--output-schema", str(schema_path),
                        "--output-last-message", str(output_path), "-"])
        return command

    def generate(self, prompt, schema, run, label):
        schema_path, output_path = run / (label + "-schema.json"), run / (label + "-output.json")
        write_json(schema_path, schema)
        start = time.monotonic()
        code, _, _ = process(self.command(schema_path, output_path), prompt, run,
                             self.environment, self.timeout)
        if code:
            raise SwarmError("Codex exited " + str(code) +
                             "; run --doctor and check plan availability. No fallback was used.")
        if not output_path.is_file():
            raise SwarmError("Codex did not produce its structured result.")
        result = parse_json(output_path.read_text(encoding="utf-8"))
        write_json(run / (label + "-metrics.json"), {
            "provider": self.name, "model": self.model or "CLI default",
            "wall_seconds": round(time.monotonic() - start, 3)})
        return result


class Claude:
    name = "claude"

    def __init__(self, model=None, timeout=300):
        self.model, self.timeout = model, timeout
        self.binary = find_cli("claude")
        self.environment = clean_environment()

    def doctor(self):
        code, out, _ = process(self.binary + ["auth", "status", "--json"],
                               env=self.environment, timeout=20)
        try:
            auth = json.loads(out)
        except ValueError:
            auth = {}
        if code or not auth.get("loggedIn") or auth.get("authMethod") not in (
                "claude.ai", "oauth"):
            raise SwarmError("Claude Code subscription login required. Run claude and sign in "
                             "yourself. API-key/provider fallbacks are not accepted.")
        code, help_text, _ = process(self.binary + ["--help"],
                                      env=self.environment, timeout=20)
        if code or any(flag not in help_text for flag in ("--safe-mode", "--json-schema", "--tools")):
            raise SwarmError("Update official Claude Code: required tool-free batch options are missing.")
        return {"provider": self.name, "authentication": "Claude subscription",
                "model": self.model or "CLI default", "location": "cloud"}

    def command(self, schema):
        command = self.binary + ["-p", "--safe-mode", "--tools", "",
                   "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                   "--permission-mode", "dontAsk", "--no-session-persistence",
                   "--output-format", "json", "--json-schema", json.dumps(schema)]
        if self.model:
            command.extend(["--model", self.model])
        return command

    def generate(self, prompt, schema, run, label):
        start = time.monotonic()
        code, out, _ = process(self.command(schema), prompt, run,
                               self.environment, self.timeout)
        if code:
            raise SwarmError("Claude Code exited " + str(code) +
                             "; run --doctor and check subscription availability.")
        envelope = parse_json(out)
        if envelope.get("is_error"):
            raise SwarmError("Claude Code reported an error; no fallback was used.")
        result = envelope.get("structured_output")
        if not isinstance(result, dict):
            result = parse_json(envelope.get("result", ""))
        write_json(run / (label + "-metrics.json"), {
            "provider": self.name, "model": self.model or "CLI default",
            "wall_seconds": round(time.monotonic() - start, 3)})
        return result
