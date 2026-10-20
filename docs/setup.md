# Setup and authentication.

The installer builds all four command names inside this clone's `bin/` directory.
It creates `.venv/` using the selected Python interpreter without pip or external
packages. It does not edit PATH, shell profiles, login settings or other programs.
Keep the clone: the launchers use its code. Moving a clone on the same OS retains
relative launcher paths, but a virtual environment should be recreated after
changing Python or operating systems.

## macOS.

Install Git and Python 3.9+ if absent. Run `bash install.sh` from the clone.
The bundled Codex CLI inside ChatGPT/Codex is recognised as a fallback when
`codex` is not on PATH. Ollama must already be running.

[Ollama's macOS requirements](https://docs.ollama.com/macos) specify macOS 14+
and Apple M-series CPU/GPU support; Intel Macs use CPU inference. Prefer the
native app for Apple GPU acceleration.

Optional, current terminal session only:

```sh
export PATH="$PWD/bin:$PATH"
swarm-gpt --doctor
```

If you already have a command named `swarm-gpt`, prefer `./bin/swarm-gpt` to make
the version explicit. The installer never replaces a user-level command.

## Windows.

Install Python 3.9+ and Git. Run `.\install.ps1`, `.\install.cmd`, or
`py -3 scripts/install.py`. No administrator account or execution-policy change
is needed. PowerShell 5.1+ is sufficient for the setup script.

The generated `.cmd` entrypoints support paths with spaces. Provider executables
are invoked with argument arrays. Known official npm shims resolve to their
JavaScript entrypoint through Node, avoiding an extra command-shell layer.

Optional, current PowerShell session only:

```powershell
$env:PATH="$PWD\bin;$env:PATH"
swarm-gpt --doctor
```

Use native Windows Ollama/Codex/Claude installations with the Windows toolkit.
For WSL, clone and install inside WSL with its own Python/provider tools; do not
reuse the Windows `.venv`.

[Ollama's Windows requirements](https://docs.ollama.com/windows) specify Windows
10 22H2+; GPU support depends on the hardware and driver.
[Codex supports a native Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox);
WSL is an option, not a requirement.

## Provider preparation.

| Provider | Required action by you | Cost boundary |
| --- | --- | --- |
| Ollama local | Install/start Ollama; choose an installed local model | Hardware, memory, power |
| Ollama cloud | Existing Ollama sign-in and explicit `--allow-ollama-cloud` | Cloud plan/limits and current provider terms |
| Codex | Install official CLI or desktop app; run `codex login`, choose ChatGPT | Existing ChatGPT/Codex allowance and account settings |
| Claude Code | Install official CLI; run `claude`, sign in with your subscription | Existing Claude allowance and account settings |

For example, you may explicitly choose to download a model:

```sh
ollama pull qwen3:8b
ollama list
```

Review its download size and licence first. The toolkit never runs `pull` or
changes Ollama server settings. It connects only to a loopback HTTP endpoint.
Cloud-tagged/remotely-backed models are refused unless explicitly allowed.

The GPT and Claude adapters strip common API-key and endpoint overrides from
their child environment and require subscription login. They do not read
credential files. Provider account settings can still allow paid extra usage;
manage those in the provider account. This toolkit does not buy credits or
guarantee future provider prices.

## Useful options.

```text
--doctor                 Check needed tools, model metadata and login; no generation
--dry-run                Print the selected stage routing; no model requests
-g, --goal TEXT          A bounded goal
--continue               Reuse the folder's saved goal in a new run
--context FILE           Send this UTF-8 relative file as context; repeat as needed
-n, --workers N          Worker slot cap, 1-8 (default 2)
--max-tasks N            Planner task cap, 1-8 (default 3)
--ollama-model NAME      Installed model (default qwen3:8b)
--gpt-model NAME         Optional Codex model override
--claude-model NAME      Optional Claude model override
--num-ctx N              Ollama context setting (default 8192)
--output-tokens N        Ollama output budget (default 2048)
--timeout SECONDS        Request/check/queue timeout (default 300)
--apply                  Apply reviewed artifacts with overwrite guards
--check-file FILE        Run user-authored argv checks after application
--benchmark N            Synthetic sequential worker-provider benchmark, 1-10 requests
```

Environment options: `MANGO_SWARMS_HOME`, `MANGO_OLLAMA_MODEL`,
`MANGO_GPT_MODEL`, `MANGO_CLAUDE_MODEL`, `MANGO_CODEX_BIN`, and `MANGO_CLAUDE_BIN`.
Use one state home across local workflows to share the Ollama gate.

`--continue` reuses the saved goal; it creates a new plan and run. It does not
resume an interrupted model session or automatically resend old context.
Repeat the intended `--context` options.

## Troubleshooting.

- **Ollama unavailable:** open the Ollama app or start `ollama serve`; check
  `ollama list` and the selected model.
- **Context budget exceeded:** use smaller selected files/deliverables or
  explicitly increase `--num-ctx` if memory allows. The byte-based guard is
  conservative and is not an exact tokenizer.
- **Authentication required:** sign in through the official CLI yourself.
  Diagnostics do not start login flows or create keys.
- **Existing file not selected:** inspect staged output, then rerun with that
  file explicitly included as context if you intend to modify it.
- **Busy lock:** another workflow owns the folder or inference gate. Wait or
  stop the owning process. OS locks release after process exit; do not delete
  lock files while processes are running.
- **Rate limit or provider failure:** the run stops with a private report.
  There is no automatic provider switch or spending fallback.

Official references:
[Ollama](https://docs.ollama.com/quickstart),
[Codex](https://developers.openai.com/codex/cli),
[Codex authentication](https://developers.openai.com/codex/auth),
[Claude setup](https://code.claude.com/docs/en/setup), and
[Claude authentication](https://code.claude.com/docs/en/authentication).
