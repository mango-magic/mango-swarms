# Measure useful work.

[Back to Swarms](../../README.md) · [Use-case library](../../use-cases/README.md) · [Existing validation](validation.md)

The library offers 200 candidate workflows. It does not establish how much time
they save, whether one model is better, or how many people a terminal replaces.
The repository has no benchmark supporting 1,000 human-hours per terminal per
day, staff-equivalence claims or a general 24-hour throughput guarantee.

## Start with a fair comparison.

1. Choose a specific recipe and a representative set of small, authorised input
   briefs. Include easy, ordinary and difficult cases.
2. Before running anything, write acceptance criteria: factual accuracy,
   completeness, format, source traceability and any executable checks.
3. Have a qualified person complete comparable tasks without Swarms. Measure
   active time and quality; do not substitute a guess for a human baseline.
4. Run Swarms on matched or counterbalanced tasks. Record the exact mode, model,
   model settings, hardware, input size and toolkit commit. Respect provider
   limits and the same disclosure boundaries used in normal work.
5. Have an appropriate reviewer assess both sets against the same rubric. Where
   practical, hide how each artifact was produced. Count rejections and failures.
6. Count all human effort around the assisted work: preparing inputs, reading,
   testing, correcting, re-running and approving it. Record provider usage and
   costs, queue time and unattended wall time separately.

Do not have someone redo an identical task from memory and call that a fair
baseline. Randomise order or use comparable task pairs, and report the design.
For important work, use independent review rather than the same model's verdict.

## Keep a simple evidence log.

One row per attempt is enough to start:

```csv
case_id,attempt,mode,model,accepted,human_minutes,wall_seconds,provider_usage,rework_notes
sample-001,1,swarm-claude,record-actual-model,false,12,35,record-from-provider,missing-source-fact
sample-001,2,swarm-claude,record-actual-model,true,8,31,record-from-provider,approved-after-correction
```

These rows are an **illustrative format, not measured results**. Keep real logs
private when they contain input content, identities or account information. The
example omits baseline rows for brevity; collect them as part of your study.

For matched accepted tasks, report:

- Acceptance rate and sample count, including failed attempts.
- Total human minutes for the manual baseline and the assisted workflow,
  including the assisted workflow's failed attempts and rework.
- Difference in human minutes, with the distribution across tasks, not only the
  best run. Negative savings are a valid finding.
- Wall time, provider usage and hardware constraints separately from human time.

For example, measured human time saved is the comparable manual total minus the
assisted human total. Model latency is not human time saved. Do not multiply one
fast sample by 24 hours or by the number of open terminals: queues, failures,
review capacity, usage caps and task variation change throughput.

## What the built-in benchmark answers.

```sh
./bin/swarm-ollama --benchmark 3
```

This runs three sequential, synthetic worker-provider requests and checks a
fixed answer. It measures request latency, including queue/load time, for that
small prompt. It does not measure business productivity or parallel capacity.
Cloud benchmarks consume provider allowance. See [performance](performance.md)
for configuration guidance and [validation](validation.md) for the actual
platform and smoke-test evidence.

Publish claims only with the task definition, input selection, sample size,
quality rubric, failures, all human effort and measurement limitations beside
the result. A narrow, reproducible result is more useful than a staffing analogy.
