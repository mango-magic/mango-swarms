# Small goals. Clear checks.

Run commands from `toolkit/`. Start in a new folder so generated artifacts cannot collide with existing work.
Copy the `hello-python` example to a working directory outside the toolkit:

```sh
cp -R examples/hello-python ../../hello-python-demo
./bin/swarm-ollama ../../hello-python-demo \
  --context requirements.md \
  -g "Implement only greeting.py according to requirements.md" \
  --max-tasks 1 --apply --check-file checks.json
```

Windows PowerShell:

```powershell
Copy-Item -Recurse .\examples\hello-python ..\..\hello-python-demo
.\bin\swarm-ollama.cmd ..\..\hello-python-demo `
  --context requirements.md `
  -g "Implement only greeting.py according to requirements.md" `
  --max-tasks 1 --apply --check-file checks.json
```

Substitute any of the five commands to compare the provider combinations.
For a Claude-only run with no Ollama dependency:

```sh
./bin/swarm-claude ../../hello-python-demo \
  --context requirements.md \
  -g "Implement only greeting.py according to requirements.md" \
  --max-tasks 1 --apply --check-file checks.json
```

On Windows, use `.\bin\swarm-claude.cmd` with the same arguments.
The example verifier is provided with the toolkit and excluded from the model's task.
It checks empty, ordinary and whitespace-padded names.

Other useful bounded goals:

- Draft `launch-checklist.md` from an explicitly selected brief.
- Produce a small CSV validation utility and its usage instructions.
- Rewrite one selected document for a defined audience.

Do not supply secrets or private customer data to cloud modes unless you have
the right to share it with those providers. The sample content here is generic.
