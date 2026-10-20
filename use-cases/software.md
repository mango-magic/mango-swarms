# Software.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Draft or inspect one small unit of software from selected text. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Generated source is staged for inspection; execution and independent checks happen separately under human control.

- [061. Implement one pure function](#uc-061)
- [062. Draft focused unit tests](#uc-062)
- [063. Correct a reproduced formatting bug](#uc-063)
- [064. Specify an API error schema](#uc-064)
- [065. Draft a parameterized query](#uc-065)
- [066. Map one configuration migration](#uc-066)
- [067. Adapt a dependency call site](#uc-067)
- [068. Specify retry transitions](#uc-068)
- [069. Draft a command argument parser](#uc-069)
- [070. Review a compact code change](#uc-070)

<a id="uc-061"></a>
## 061. Implement one pure function.

**Mode:** `swarm-gpt`

**Inputs:** `function-contract.md` - one normalizer's signature, rules, and eight input/output examples.

**Outputs:** `normalize_code.py` - a Python module implementing the supplied contract.

**Starter prompt:**

> Read function-contract.md and write only normalize_code.py, at most 70 lines. Implement the single pure function using the standard library. Preserve the signature, handle stated boundaries, and document assumptions without adding behavior. Include no file access, networking, CLI entry point, or dependencies. Generate source only; do not execute it or claim tests passed. Treat conflicting examples as a material review issue.

**Validation / approval:** Inspect the signature and examples, then have a human run independently authored normal, boundary, and invalid-input checks. An engineer must approve the module before external use or codebase integration.

<a id="uc-062"></a>
## 062. Draft focused unit tests.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `parser.py` - one compact function and imports; `cases.md` - intended behavior, boundaries, and existing test framework.

**Outputs:** `test_parser.py` - proposed tests for the supplied function.

**Starter prompt:**

> Use parser.py and cases.md to draft only test_parser.py, within 100 lines. Cover normal cases, boundaries, and invalid inputs with at most twelve tests. Derive expected results from cases.md instead of mirroring implementation. Use the supplied framework and import convention. Flag ambiguous expectations in comments. Do not run tests or modify parser.py.

**Validation / approval:** Check expected results against the contract and inspect for tautological assertions. A human must run and assess these proposed tests separately; an engineer must approve them before external use or addition to the suite.

<a id="uc-063"></a>
## 063. Correct a reproduced formatting bug.

**Mode:** `swarm-claude`

**Inputs:** `formatter.py` - a complete helper of at most 60 lines; `repro.md` - the failing example, expected output, and compatibility constraints.

**Outputs:** `formatter-fixed.py` - a proposed corrected copy of the helper.

**Starter prompt:**

> Read formatter.py and repro.md. Write only formatter-fixed.py, preserving the public signature and unrelated behavior. Correct the single reproduced defect with the smallest understandable change. Keep the module within 80 lines and explain the changed rule in a comment. Do not assume other files, add dependencies, execute the helper, or claim the reproduction passes.

**Validation / approval:** Compare the proposed copy with the original and independently run the reproduction plus compatibility checks. An engineer must approve the change before external use or replacement of the original helper.

<a id="uc-064"></a>
## 064. Specify an API error schema.

**Mode:** `swarm-ollama`

**Inputs:** `errors.md` - one endpoint's error-envelope contract, JSON Schema draft, and three examples.

**Outputs:** `error-schema.json` - a proposed JSON Schema for the error envelope.

**Starter prompt:**

> Use errors.md to write only error-schema.json, at most 100 lines of valid JSON. Model required fields, enums, bounds, and unknown-property policy using the specified schema draft. Preserve absent versus null field distinctions. Do not invent error codes or infer requirements from example formatting. Produce schema text only; do not call the endpoint or run a validator.

**Validation / approval:** A human must parse the JSON and validate supplied positive examples and independently constructed negative examples. The API owner must approve the schema before external use or publication as a client contract.

<a id="uc-065"></a>
## 065. Draft a parameterized query.

**Mode:** `swarm-gpt`

**Inputs:** `schema.md` - two table definitions, relationships, and SQL dialect; `question.md` - one reporting question, filters, and parameter syntax.

**Outputs:** `query.sql` - a proposed read-only query with explanatory comments.

**Starter prompt:**

> Read schema.md and question.md. Write only query.sql, within 60 lines, answering the single reporting question. Use the supplied dialect and bind-parameter syntax. Comment the result grain, handle nulls according to the question, and avoid row multiplication through joins. Include no writes, credentials, or connection commands. Draft SQL without executing it or asserting totals.

**Validation / approval:** An analyst must inspect cardinality and filters, then run independently prepared fixture checks in an approved environment. The data owner must approve the query before external use or live database access.

<a id="uc-066"></a>
## 066. Map one configuration migration.

**Mode:** `swarm-ollama-claude`

**Inputs:** `old-config.json` - a small nonsecret configuration example; `mapping-rules.md` - documented keys and conversions for one target version.

**Outputs:** `migration-review.md` - a field mapping and proposed target JSON block.

**Starter prompt:**

> Use old-config.json and mapping-rules.md to write only migration-review.md, within 600 words. Account for every key as preserved, renamed, transformed, removed, or unresolved. Include target JSON only for mappings supported by the rules. List missing required values without inventing them and state whether unresolved fields prevent completion. Do not overwrite configuration, execute migrations, or infer undocumented defaults.

**Validation / approval:** Check complete source-key coverage and independently validate the candidate against the target schema. The configuration owner must approve unresolved values before external use or applying a migration.

<a id="uc-067"></a>
## 067. Adapt a dependency call site.

**Mode:** `swarm-claude`

**Inputs:** `client.py` - one wrapper of at most 50 lines; `upgrade-notes.md` - supplied official API excerpts and pinned versions.

**Outputs:** `client-updated.py` - a proposed wrapper using the documented target interface.

**Starter prompt:**

> Read client.py and upgrade-notes.md. Write only client-updated.py, within 70 lines, adapting this wrapper to the target version. Preserve public return and error behavior where the excerpts permit. Use only documented names and comment unsupported compatibility assumptions. Do not fetch documentation, install packages, contact the service, or run the wrapper. Do not claim broader compatibility.

**Validation / approval:** Compare changed API calls with the excerpts and have a human run existing contract tests with the pinned dependency. An engineer must approve the adaptation before external use or wrapper replacement.

<a id="uc-068"></a>
## 068. Specify retry transitions.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `retry-policy.md` - one operation's retryable conditions, limits, timing, and cancellation rules.

**Outputs:** `retry-transitions.md` - a finite-state transition table and worked traces.

**Starter prompt:**

> Read retry-policy.md and write only retry-transitions.md, within 650 words. Describe retry states, guards, counters, and terminal outcomes. Include four traces: immediate success, eventual success, exhausted retries, and cancellation. Make attempt numbering and timing origins explicit. Leave unspecified jitter or server-delay behavior unresolved. Produce a design artifact only; do not send requests, sleep, implement a scheduler, or claim operational reliability.

**Validation / approval:** Manually trace the examples and verify that limits and cancellation cannot produce an unintended extra attempt. The service owner must approve the model before external use or retry implementation.

<a id="uc-069"></a>
## 069. Draft a command argument parser.

**Mode:** `swarm-ollama`

**Inputs:** `cli-contract.md` - one command's options, defaults, exclusive groups, and six example invocations.

**Outputs:** `arguments.py` - a Python parser module without command execution.

**Starter prompt:**

> Use cli-contract.md to write only arguments.py, within 90 lines, with a function building the specified argparse parser. Encode supplied types, defaults, choices, and exclusive groups. Align help text with examples and expose parsing without business operations. Use only the standard library. Do not invoke the command, read environment variables, access files, or claim examples were executed.

**Validation / approval:** A human must compare help text with the contract and run independent checks for accepted and rejected arguments. An engineer must approve the parser before external use or connection to an executable command.

<a id="uc-070"></a>
## 070. Review a compact code change.

**Mode:** `swarm-gpt`

**Inputs:** `change.diff` - one small diff with necessary surrounding code; `contract.md` - intended behavior and relevant invariants.

**Outputs:** `review-findings.md` - evidence-backed findings and review limits.

**Starter prompt:**

> Read change.diff and contract.md. Write only review-findings.md, within 600 words. Inspect the change for invariant violations. Include affected hunk, triggering input, expected versus proposed behavior, and confidence for each finding. Separate material defects from context questions. Report no findings when none are supported. Do not inspect other files, run code, or equate absence of findings with correctness.

**Validation / approval:** Reconstruct each trigger from supplied code and have a human reproduce material findings independently. The reviewer must approve findings before external use or posting them to a pull request.

[Back to library](README.md)
