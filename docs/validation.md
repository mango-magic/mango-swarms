# Validation status.

This file distinguishes deterministic integration coverage from real model use.
Provider account availability and model outputs vary.

## Automated checks.

All 23 unit/integration tests passed on macOS/Python 3.9 in 4.806 seconds
from an isolated copy of the same source. Earlier runs in the original working
directory encountered a CLI fixture startup timeout; the isolated run completed
without increasing timeouts. Coverage includes:

- All four actual provider-routing combinations.
- Plan/work/review/stage/apply/check lifecycle.
- Existing-file preservation, backups, changed-file guards and path validation.
- Cross-process lock release and shared Ollama request serialization.
- Real subprocess contracts for Codex and Claude using offline fixtures.
- A real loopback HTTP fixture through the installed-style launcher.
- Installer output for all four names, including a path containing spaces.
- Timeout cleanup, cloud opt-in, context budgets and API environment removal.

GitHub Actions runs the suite on Windows, macOS and Linux with Python 3.9 and
3.13. CI uses synthetic fixtures and does not require provider credentials.
The workflow badge links to the actual current run; a configured matrix is not
itself evidence of successful Windows execution.

The [initial published CI run](https://github.com/mango-magic/mango-swarms/actions/runs/39414347905)
passed all six OS/Python combinations, including Windows `.cmd` launchers and
the shared lock tests. A fresh public clone on the test Mac also completed
`bash install.sh`, ran all four installed commands with `--dry-run`, and passed
the public-source audit. CI additionally exercises the documented shell,
PowerShell and CMD setup entrypoints.

## Live checks.

On 2026-10-20, all four modes completed the supplied `hello-python` example on
macOS 26.5, Apple M4 Pro, 24 GB unified memory. Each planned one task, wrote
`greeting.py`, received a fresh model review, applied it, and passed the
predefined four-case verifier. Each verifier was also rerun independently.

| Mode | Result | Sum of model-stage wall times |
| --- | --- | ---: |
| `swarm-ollama` | Four cases passed | 16.725 s |
| `swarm-ollama-claude` | Four cases passed | 15.536 s |
| `swarm-ollama-gpt` | Four cases passed | 17.490 s |
| `swarm-gpt` | Four cases passed | 17.660 s |

These are single small-task observations, not comparative provider benchmarks.
The two GPT workflows overlapped. Times exclude startup diagnostics and the
final verifier; they include each model call's queue/load delay. The pure
Ollama plan included a 7.163 s cold model load.

Local model: Qwen3 8.2B, `qwen3:8b`, GGUF `Q4_K_M`,
digest `500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41`.
Ollama 0.40.6; context 8192; output limit 2048; temperature 0.2; thinking off;
one shared local inference slot. A subsequent `/api/ps` snapshot reported
5,801,708,093 bytes loaded, all in GPU placement, at 8192 context. That snapshot
is not peak process memory or total system usage; peak memory and swap were
not measured.

Cloud adapters used existing subscription logins and each CLI's default model
rather than a pinned model ID: Codex `0.163.0-alpha.10.2`, Claude Code `2.1.304`.
Provider-default models can change. Initial GPT plan attempts exposed a
task-ID compatibility bug; underscore IDs are now supported and regression
checked before the successful reruns.

The local synthetic `--benchmark 3` command also passed all exact-answer checks:
warm request times 0.435, 0.333 and 0.334 seconds, mean 0.367 seconds. Each answer
contained 14 output tokens; reported generation rates were approximately
44.8-45.6 tokens/second, excluding prompt processing and load time.

The initial release is not a benchmark of ten simultaneous workflows, sustained
load, larger coding tasks or human staffing equivalence. Native Windows provider
inference is not tested by the offline CI matrix. Private run reports, local
paths, credentials and account data are excluded from this repository.
