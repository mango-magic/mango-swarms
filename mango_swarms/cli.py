"""Command-line interface shared by four distinct provider combinations."""

import argparse
import json
import os
from pathlib import Path
import statistics
import subprocess
import sys
import time

from . import __version__
from .providers import Claude, Codex, Ollama
from .runtime import SwarmError, state_home, timestamp, write_json
from .workflow import MODES, TEXT, execute, obj


def bounded_int(low, high):
    def parse(value):
        try:
            number = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError("Expected an integer.")
        if not low <= number <= high:
            raise argparse.ArgumentTypeError("Expected " + str(low) + "-" + str(high) + ".")
        return number
    return parse


def parser():
    result = argparse.ArgumentParser(
        description="MangoMagic Swarms. Plan, build, review and verify with explicit provider roles.")
    result.add_argument("mode", choices=list(MODES))
    result.add_argument("folder", nargs="?", help="workspace; only --context files are read")
    goals = result.add_mutually_exclusive_group()
    goals.add_argument("-g", "--goal")
    goals.add_argument("--continue", dest="continue_goal", action="store_true")
    result.add_argument("-n", "--workers", type=bounded_int(1, 8), default=2)
    result.add_argument("--max-tasks", type=bounded_int(1, 8), default=3)
    result.add_argument("--ollama-model", default=os.environ.get("MANGO_OLLAMA_MODEL", "qwen3:8b"))
    result.add_argument("--gpt-model", default=os.environ.get("MANGO_GPT_MODEL"))
    result.add_argument("--claude-model", default=os.environ.get("MANGO_CLAUDE_MODEL"))
    result.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    result.add_argument("--allow-ollama-cloud", action="store_true",
                        help="explicitly permit cloud-tagged Ollama models and their usage limits/costs")
    result.add_argument("--context", action="append", default=[], metavar="RELATIVE_FILE",
                        help="explicit UTF-8 context file; repeat for multiple files")
    result.add_argument("--context-chars", type=bounded_int(1000, 100000), default=6000)
    result.add_argument("--review-chars", type=bounded_int(2000, 200000), default=12000)
    result.add_argument("--num-ctx", type=bounded_int(2048, 131072), default=8192)
    result.add_argument("--output-tokens", type=bounded_int(128, 16384), default=2048)
    result.add_argument("--timeout", type=bounded_int(10, 3600), default=300)
    result.add_argument("--apply", action="store_true",
                        help="apply approved text artifacts; existing files must be selected context")
    result.add_argument("--check-file", help="user-authored relative JSON file containing argv arrays")
    result.add_argument("--doctor", action="store_true", help="dependency/auth diagnostics; no generation")
    result.add_argument("--dry-run", action="store_true", help="show provider routing without model calls")
    result.add_argument("--benchmark", type=bounded_int(1, 10), metavar="REQUESTS",
                        help="measure this mode's worker provider with a synthetic prompt")
    result.add_argument("--version", action="version", version="MangoMagic Swarms " + __version__)
    return result


def make_providers(args, home):
    constructors = {
        "ollama": lambda: Ollama(args.ollama_model, home, args.ollama_url, args.num_ctx,
                                args.output_tokens, args.timeout, args.allow_ollama_cloud),
        "codex": lambda: Codex(args.gpt_model, args.timeout),
        "claude": lambda: Claude(args.claude_model, args.timeout),
    }
    return {name: constructors[name]() for name in dict.fromkeys(MODES[args.mode])}


def benchmark(provider, count, home):
    run = home / "benchmarks" / (str(time.time_ns()))
    run.mkdir(parents=True)
    schema = obj({"answer": TEXT})
    elapsed = []
    for index in range(count):
        start = time.monotonic()
        value = provider.generate(
            'Return JSON with answer exactly "MangoMagic benchmark OK". No tools.',
            schema, run, "sample-" + str(index))
        if value.get("answer") != "MangoMagic benchmark OK":
            raise SwarmError("Benchmark correctness check failed; timing alone is not success.")
        elapsed.append(time.monotonic() - start)
    report = {"type": "measured_synthetic", "timestamp": timestamp(), "provider": provider.name,
              "requests": count, "request_concurrency": 1,
              "seconds": [round(x, 3) for x in elapsed],
              "mean_seconds": round(statistics.mean(elapsed), 3),
              "note": "Includes queue/load time. Not a productivity, staffing or capacity benchmark."}
    write_json(run / "benchmark.json", report)
    print(json.dumps(report, indent=2) + "\nReport: " + str(run / "benchmark.json"))
    return 0


def main(argv=None):
    os.umask(0o077)
    args = parser().parse_args(argv)
    home = state_home()
    if args.dry_run:
        print(json.dumps({"brand": "MangoMagic", "mode": args.mode,
                          "stages": dict(zip(("planner", "worker", "reviewer"), MODES[args.mode])),
                          "worker_slots": args.workers, "shared_ollama_requests": 1,
                          "num_ctx": args.num_ctx, "apply": args.apply,
                          "state_home": str(home), "model_requests": 0}, indent=2))
        return 0
    providers = make_providers(args, home)
    diagnostics = [provider.doctor() for provider in providers.values()]
    if args.doctor:
        print(json.dumps({"brand": "MangoMagic", "version": __version__,
                          "providers": diagnostics, "generation_requests": 0}, indent=2))
        return 0
    if args.benchmark:
        return benchmark(providers[MODES[args.mode][1]], args.benchmark, home)
    if not args.folder:
        if not sys.stdin.isatty():
            raise SwarmError("Supply a folder and -g goal.")
        args.folder = input("Folder?\n> ").strip().strip('"').strip("'")
    if not args.goal and not args.continue_goal:
        if not sys.stdin.isatty():
            raise SwarmError("Supply -g goal or --continue.")
        args.goal = input("Goal?\n> ").strip()
    code, _ = execute(args, providers, home, emit=lambda message: print(message, flush=True))
    return code


def entry():
    try:
        return main()
    except KeyboardInterrupt:
        print("\nMangoMagic: cancelled. Inspect the private run report before continuing.", file=sys.stderr)
        return 130
    except subprocess.TimeoutExpired:
        print("MangoMagic: a provider diagnostic or request timed out. "
              "Check the provider CLI and retry; no fallback was used.", file=sys.stderr)
        return 1
    except (SwarmError, OSError) as error:
        print("MangoMagic: " + str(error), file=sys.stderr)
        return 1
