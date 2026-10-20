# Security boundaries.

The default workflow stages text files. Models have no shell, browser or
filesystem tools through this framework. They receive the supplied goal,
explicitly selected context and, for review, proposed artifacts.

`--apply` is an explicit request to write reviewed files. Existing files must be
selected context and unchanged since the run began. Sensitive configuration
paths, traversal, symlink targets and nonportable names are refused. This is
defence in depth for an assistant workflow, not a sandbox for hostile local users.

`--check-file` is an explicit request to execute the argument arrays in a file
you authored. These commands run with your operating-system account. They are
not sandboxed by this Python toolkit. Inspect both commands and generated code
before enabling checks for untrusted projects. No shell-string evaluation is
performed by the wrapper.

Codex and Claude model-generation stages disable their tools and customisations
for the invocation. Their authentication and managed organisation policy still
apply. The toolkit never reads credential stores or automatically starts login.
No permission bypass flags are used.

Private run state contains prompts, model output and backups. Keep it private,
review retention, and exclude it from repositories. The default state location
is outside the clone. Windows relies on inherited user-directory ACLs.

The local Ollama endpoint must be loopback HTTP. Cloud models require explicit
opt-in and send data to their provider. Using a loopback endpoint alone does not
prove that inference is local. Common API-key environment overrides are removed
for the subscription CLI adapters; they do not support API billing in v0.1.

Provider request errors are reported without echoing authentication output.
No toolkit telemetry is sent. Existing vendor clients have their own telemetry
and service policies.

Report vulnerabilities through GitHub's private vulnerability reporting feature
if enabled. Otherwise open an issue containing only a minimal, sanitised
description and request a private contact path. Never post keys, private run
directories or customer content in a public issue.
