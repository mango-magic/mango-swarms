# The Swarms toolkit.

[Product overview](../README.md) · [200 use cases](../use-cases/README.md)

Everything needed to install, run, test and understand the five swarm modes lives
in this folder. The use-case catalogue is a separate sibling.

## Install here.

From the repository root, enter `toolkit/`. On macOS/Linux, run `bash install.sh`.
On Windows, run `.\install.cmd` or `.\install.ps1`. The installer creates the
local `.venv/` and `bin/` here. It does not modify your global commands or login.

```sh
cd toolkit
bash install.sh
./bin/swarm-gpt --dry-run
```

Windows PowerShell, from the repository root:

```powershell
cd toolkit
.\install.cmd
.\bin\swarm-gpt.cmd --dry-run
```

Use `swarm-ollama`, `swarm-ollama-claude`, `swarm-ollama-gpt`, `swarm-gpt` or
`swarm-claude` as the command name. Use `--doctor` to check the selected providers.
[Prepare the providers and sign in](docs/setup.md).

## Find your way around.

| Folder | Contents |
| --- | --- |
| `mango_swarms/` | Orchestration, provider adapters and command-line interface |
| `scripts/` | Installer, documentation checks and public-source audit |
| `tests/` | Offline tests and provider-contract fixtures |
| `examples/` | A small Python task with independent checks |
| `docs/` | Setup, architecture, performance, validation and run guides |
| `assets/` | MangoMagic brand vectors and responsive README hero |
| `bin/` and `.venv/` | Local generated files, excluded from Git |

## Updating an older clone.

Enter `toolkit/` and run its installer after updating the source. Use the new
`toolkit/bin/` launchers. An older root-level `bin/` is no longer the launch
location. Do not delete or overwrite personal wrappers or unrelated environments;
keep any you customised until you have reviewed them.

The private state location and all `MANGO_*` environment variable names are
unchanged. Goals, run reports, backups, provider login and selected models are
not migrated or reset by this layout change. If you exported the old `bin/`
path in a terminal session, use the new path in that session or invoke the
launcher by its explicit path. No shell profile is edited.

[Run a use case](docs/running-a-use-case.md) · [Architecture](docs/architecture.md) · [Performance](docs/performance.md) · [Validation](docs/validation.md) · [Security](../.github/SECURITY.md) · [Contributing](../.github/CONTRIBUTING.md)
