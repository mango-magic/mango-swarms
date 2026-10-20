# Validation status.

This file distinguishes deterministic integration coverage from real model use.
Provider account availability and model outputs vary.

## Automated checks.

All 26 unit/integration tests passed on macOS/Python 3.9 in 6.165 seconds
from an isolated copy after the `toolkit/` and `use-cases/` folder migration.
Coverage includes:

- All five actual provider-routing combinations.
- Claude-only diagnostics and model configuration with Ollama/Codex initialization forbidden.
- Dry-run capacity reporting with zero local inference slots for cloud-only modes.
- Plan/work/review/stage/apply/check lifecycle.
- Existing-file preservation, backups, changed-file guards and path validation.
- Cross-process lock release and shared Ollama request serialization.
- Real subprocess contracts for Codex and Claude using offline fixtures.
- A real loopback HTTP fixture through the installed-style launcher.
- Installer output for all five names, including a path containing spaces.
- Moving and reinstalling a nested toolkit while preserving private state and unrelated files.
- Timeout cleanup, cloud opt-in, context budgets and API environment removal.

GitHub Actions runs the suite on Windows, macOS and Linux with Python 3.9 and
3.13. CI uses synthetic fixtures and does not require provider credentials.
Check the [Actions history](https://github.com/mango-magic/mango-swarms/actions/workflows/ci.yml)
for the specific commit; a configured matrix is not evidence of successful
Windows execution. The [reorganisation CI run](https://github.com/mango-magic/mango-swarms/actions/runs/39508750771)
passed all six OS/Python combinations at commit `cf9914d`, including the 26-test
suite, documentation/source audits and installation of all five commands.
Both Windows setup entrypoints passed their native runner checks.

The [initial published CI run](https://github.com/mango-magic/mango-swarms/actions/runs/39414347905)
passed all six OS/Python combinations, including Windows `.cmd` launchers and
the shared lock tests. A fresh public clone on the test Mac also completed
`bash install.sh`, ran all four installed commands with `--dry-run`, and passed
the public-source audit. CI additionally exercises the documented shell,
PowerShell and CMD setup entrypoints.

The reorganised toolkit was also installed in the existing Mac checkout and
all five generated commands passed `--dry-run`, with zero model requests. The
provider/runtime modules and all three platform install entrypoints are
byte-identical to the previous release apart from their location. The state
location, configuration variables and provider login handling are unchanged.

Documentation checks cover 35 Markdown files, 354 local file/anchor links,
200 unique catalogue IDs/titles/prompts, all required recipe fields and all
five modes. All 200 recipe argument sets and 17 documented launcher commands
were parsed against the real CLI. These are structural checks, not evidence
that all 200 tasks have succeeded with models. The reviewed source audit
passed for 59 text files. A fresh public clone of `cf9914d` installed and
ran all five commands with zero model requests, then passed both audits.
Visual review covered light/dark desktop and 390/320-pixel mobile layouts
locally. The published GitHub page also loaded the desktop and 390-pixel
mobile heroes correctly; the catalogue and recipe anchors were verified live.

## Live checks.

On 2026-10-20, the original four modes completed the supplied `hello-python` example on
macOS 26.5, Apple M4 Pro, 24 GB unified memory. Each planned one task, wrote
`greeting.py`, received a fresh model review, applied it, and passed the
predefined four-case verifier. Each verifier was also rerun independently.

| Mode | Result | Sum of model-stage wall times |
| --- | --- | ---: |
| `swarm-ollama` | Four cases passed | 16.725 s |
| `swarm-ollama-claude` | Four cases passed | 15.536 s |
| `swarm-ollama-gpt` | Four cases passed | 17.490 s |
| `swarm-gpt` | Four cases passed | 17.660 s |
| `swarm-claude` | Four cases passed | 20.088 s |

The subsequent Claude-only check used Claude Code 2.1.305 with its existing
subscription login and default model. Its planner, worker and reviewer all used
Claude in separate requests, followed by the four-case verifier and an
independent verifier rerun. `--doctor` reported Claude as its only dependency.
The four existing local launcher files remained byte-for-byte unchanged.

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
rather than a pinned model ID: Codex `0.163.0-alpha.10.2`, Claude Code `2.1.304`
for the original hybrid check and `2.1.305` for the later Claude-only check.
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
