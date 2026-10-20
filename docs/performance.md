# Practical limits. Measure before scaling.

There is no credible conversion from a count of AI agents to a count of
full-time staff. This project does not claim "150+ staff equivalent".
Useful output depends on task quality, model capability, review, tool access,
failure rate and human judgement.

Ten open workflows are also not proof that a 24 GB Mac can perform ten local
generations concurrently. This toolkit permits workflows in separate folders
to queue through a shared **one-request Ollama gate**. It does not multiply
available model memory or guarantee throughput. Long queues can time out.

## A conservative 24 GB starting profile.

The following are **untuned starting suggestions, not measured maximums or
hardware guarantees**. Actual model size, quantisation, architecture, context
and other open applications matter more than parameter count alone.

| Selected model/path | Initial active workflows | Local requests at once | Starting context |
| --- | ---: | ---: | ---: |
| Local 3B-4B Q4 model | 1 initially | 1 shared | 4K for tiny tasks; test 8K |
| Local 7B-8B Q4 model | 1 initially | 1 shared | 4K for tiny tasks; 8K tested here |
| Local 12B-14B Q4 model | 1 experimental | 1 shared | 4K-8K; verify memory first |
| Local 30B-32B Q4 model | 0 until fit is verified | At most 1 in this toolkit | Not a default with normal apps open |
| Ollama workers + Claude/GPT planner | 1-2 | 1 shared | 8K local |
| Claude-only or GPT-only | 1-2 | 0 | Provider-managed |

For 4K context, reduce `--output-tokens` and selected context accordingly.
The wrapper default is 8K because planning and review need room for instructions,
schemas and short artifacts. Larger deliverables may need a larger context,
more memory, or a smaller goal.

Allow roughly 6-8 GB for the OS and other applications as an engineering
starting allowance, then measure actual pressure and swap. This is not a measured
constant. Outside this toolkit, experimenting with two simultaneous generations
on a 3B-8B Q4 model requires short context and observed memory headroom; this
release deliberately retains its single local request gate.

Examples from the [official Qwen3 tags](https://ollama.com/library/qwen3/tags),
checked 2026-10-20:

| Exact tag | Approximate download size |
| --- | ---: |
| `qwen3:4b-q4_K_M` | 2.6 GB |
| `qwen3:8b-q4_K_M` | 5.2 GB |
| `qwen3:14b-q4_K_M` | 9.3 GB |
| `qwen3:32b-q4_K_M` | 20 GB |

These are download sizes, not total runtime RAM. Tags can change; record the
installed digest. A 20 GB model download leaves little room on a 24 GB machine
for context, runtime buffers and normal applications.

The toolkit supports `-n 1` through `-n 8` worker slots per run. That is a
software configuration range, **not a measured capacity rating**. For cloud-only modes,
start at two workers; account quotas and provider latency usually govern scaling
before model-weight RAM does. For mixed modes, start at two workers and one or
two workflows; the Ollama gate still allows one local request at a time.

## Why memory grows.

One Ollama model can serve multiple requests without storing a separate full
weight copy for each logical worker. Concurrent requests still need their own
context/KV-cache and work buffers. Different loaded models need additional
weight allocations. Apple unified memory is shared with the OS and applications.

A useful conceptual estimate is:

```text
memory ≈ OS/apps + loaded model weights
       + concurrent contexts × context/KV-cache requirement
       + runtime/work buffers
```

This is not a capacity calculator. Quantisation and model architecture change
the terms. Ollama documents that increasing parallel requests increases context
memory requirements; model loading and parallel request counts are different
controls. Use `ollama ps` and the operating system's memory-pressure tools.
Do not infer available runtime memory from a model download size alone.

Sources: [Ollama concurrency and memory FAQ](https://docs.ollama.com/faq) and
[context length](https://docs.ollama.com/context-length).

For a manually started, dedicated local server, conservative settings are
`OLLAMA_MAX_LOADED_MODELS=1` and `OLLAMA_NUM_PARALLEL=1`. The toolkit does not
change server settings. Its gate covers only runs sharing the same
`MANGO_SWARMS_HOME`; other Ollama clients and other state homes bypass it.

Ollama recommends at least 64K context for large-context agent/coding-tool
workloads. That uses substantially more memory. Our 4K-8K suggestions apply to
small, explicitly scoped artifact tasks, not repository-wide agent sessions.
The model itself must support any context you request.

## Local versus cloud.

`swarm-ollama` can keep inference local when the chosen model is local. A model
with a cloud-backed tag may execute remotely even though its API endpoint is
`localhost`. The toolkit detects cloud tags/remote metadata and requires
`--allow-ollama-cloud`.

Mixed modes send selected context to their Claude/GPT planner and reviewer.
Claude-only and GPT-only use remote inference for every stage. Their model weights do not sit
in your Mac's RAM; network reliability, provider quotas and existing account
usage settings still apply. Cloud inference and paid extra usage are not free
because the wrapper is MIT-licensed.

The one-to-two workflow suggestions are application starting settings, not
provider entitlements. ChatGPT/Codex subscription allowance and separately billed
OpenAI API usage are distinct; this release accepts the subscription CLI path.
Provider quotas still constrain every cloud stage.

## Run your own baseline.

```sh
./bin/swarm-ollama --ollama-model qwen3:8b --benchmark 3
./bin/swarm-ollama --ollama-model qwen3:8b --num-ctx 16384 --benchmark 3
```

Benchmarks make sequential requests with one exact-answer correctness check.
The private report records wall time including queue/load delay. Ollama metrics
include token counts and timing when the server supplies them. Derive output
tokens/second from `eval_count / (eval_duration / 1e9)`.

For a useful application benchmark, use your own small representative goal and
verifier. Record model digest/quantisation, context/output limits, memory pressure,
cold versus warm load, job count, elapsed time, correct outputs and failures.
Repeat before increasing load. A synthetic latency number is not evidence of
ten simultaneous swarms or a staffing multiplier.

Current measured validation is recorded separately in [validation.md](validation.md).
