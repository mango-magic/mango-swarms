# From prompt to useful files.

[Back to Swarms](../../README.md) · [Browse the use-case library](../../use-cases/README.md)

The library contains starter recipes, not promises that every model will pass
every task. Choose one small deliverable, use representative inputs and judge the
result against an acceptance checklist you write first.

## 1. Prepare a small text brief.

Create a working folder outside this toolkit. Save the files listed under
**Inputs** in your chosen recipe as UTF-8 text. Markdown, plain text, JSON and
small CSV extracts work. A file extension does not make a PDF, image, spreadsheet
workbook or slide deck readable: export a relevant text extract yourself first.
The toolkit does not fetch links or open apps mentioned in a brief.

The default file reader caps each input at **6,000 UTF-8 bytes** and combined
selected file contents at **6,000 characters**.
These are file-loading limits, not a promise that a model request will fit.
Non-ASCII text can use several bytes per character.

Ollama has a separate conservative full-prompt byte guard. At the defaults
(`--num-ctx 8192`, `--output-tokens 2048`) that guard is **5,632 bytes**. The goal,
context, stage instructions and plan all take space; review also includes the
generated artifacts. Start an Ollama recipe with about **1,000 combined input
characters**, one task (`--max-tasks 1`) and an output of **150-200 words**. This
is a small trial, not a fit guarantee. Reduce higher recipe output caps for the
first trial, especially for non-ASCII text. A few rows beat an entire archive.

On a budget error, shorten inputs, goal or output scope. If your installed model
and hardware support it, explicitly increasing `--num-ctx` is another option;
see [memory and performance](performance.md). Increasing it does not raise the
separate file-loading limits. Larger inputs need an explicit `--context-chars`
change too, and should still be minimised. Split larger work into separate runs
that a person reviews between steps. Workers do not receive one another's drafts.

Remove secrets and use synthetic or appropriately authorised, minimised data.
Cloud planners and reviewers also see selected context and generated artifacts
in hybrid modes. For local inference, verify the installed model is local and
use `swarm-ollama` without enabling Ollama cloud.

## 2. Choose a mode and supply every input.

Run these commands from `toolkit/` after installation. This concrete
example uses a folder called `launch-draft` next to the repository clone, containing a short
`brief.md` with audience, approved product facts and open questions.

**macOS / Linux**

```sh
./bin/swarm-claude --doctor
./bin/swarm-claude ../../launch-draft --context brief.md --max-tasks 1 \
  -g "Use brief.md to draft launch-faq.md: six concise questions and answers. Use only supplied facts. Mark missing answers for review."
```

**Windows PowerShell**

```powershell
.\bin\swarm-claude.cmd --doctor
.\bin\swarm-claude.cmd ..\..\launch-draft --context brief.md --max-tasks 1 -g "Use brief.md to draft launch-faq.md: six concise questions and answers. Use only supplied facts. Mark missing answers for review."
```

Replace the mode, folder, input filenames and goal with your chosen recipe.
Copy the whole starter prompt into `-g`, inside quotes appropriate for your shell.
For an input containing quotes, edit or escape them before pasting the command.
Repeat `--context` once per input. For example, a two-file goal uses
`--context brief.md --context voice.md --max-tasks 1`. Naming a file in the goal alone does not
send its contents.

The toolkit creates a bounded plan, drafts text artifacts and asks a fresh
reviewer to assess them. Each mode uses the providers listed in the
[chooser](../../README.md#choose-a-swarm). An example's mode is a suitable starting
point, not a comparative quality benchmark. Use `--dry-run` to inspect routing
without model calls; use `--doctor` for the selected dependencies.

## 3. Inspect the staged result.

Terminal prints the private run directory. Its `artifacts/` folder contains the
proposed files; `review.json` records the model review and `report.json` records
the outcome. A successful staged run has not written those files into your
working folder or run tests. A rejected review leaves the workspace unchanged.
Inspect even a result the model approved.

Check the recipe's **Validation / approval** criteria yourself. Verify source
facts, calculations, names and omitted information. Review generated code before
executing it, and run independently written tests with representative fixtures.
A generated checker can share the generator's mistakes.

For publishing, email, CRM updates, bookings, payments, deployment or another
external action, transfer the approved result through a separately authorised
tool or do it yourself. Swarms does not include those integrations.

## 4. Apply and verify deliberately.

Copy selected staged files yourself, or rerun with `--apply` to authorise writing
reviewer-approved artifacts into the working folder. **Rerunning generates a new
result**; it does not apply the previous staged run. Inspect that result too.
Existing files can be replaced only if selected with `--context` and unchanged
since the run began. Original bytes are backed up in private run state.

For a runnable example with checks already supplied by the project, follow
[hello-python](../examples/README.md). Its tiny requirements and independent
verifier make the outcome inspectable.

A user-authored `checks.json` can contain argument arrays:

```json
[
  ["{python}", "-m", "unittest", "discover", "-s", "tests", "-v"]
]
```

`--apply --check-file checks.json` authorises those commands to run on your
machine after applying the files. Only use checks you understand and keep them
outside the model's editing task. The toolkit does not sandbox arbitrary check
commands. No checks means no claim of tested correctness.

## Boundaries that matter.

- Default: at most three planned tasks and two worker slots. Keep each recipe
  narrow; a long list of outputs is not a better goal.
- Ollama requests share one local inference gate per state home. Worker slots do
  not change server parallelism. Other Ollama clients are outside that gate.
- One workflow owns a target folder at a time. Avoid simultaneous editing during
  application. Use separate folders for independent jobs.
- Calls and queue waits time out. There is no unattended 24-hour work loop or
  automatic paid fallback.
- `--continue` starts a new run with the saved goal. Repeat the context options;
  it does not resume an interrupted model conversation.

[Setup and options](setup.md) · [State and result meanings](architecture.md) · [Measure accepted work](measuring-results.md)
