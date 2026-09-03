---
id: bench-deepseek-h200-fp8
type: evidence
status: draft
owner: performance-eng
domain: performance
aliases: [deepseek h100 fp8, deepseek fp8 benchmark, deepseek v4 flash h100 benchmark, deepseek h200 fp8]
related: [hub-evidence, idx-benchmark-library, asm-h200-sufficient, asm-fp8-quality-neutral, val-deepseek-h200-fp8, ent-gpu-h100]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Planned benchmark definition for DeepSeek V4 Flash at FP8 on H100 — no results recorded yet."
---

# DeepSeek H100 FP8 Benchmark

> **This note defines a planned benchmark; no results recorded yet.** Confidence is `assumed` because it describes intended measurement, not an executed run. It upgrades to `measured` only once the harness runs and data lands in the Results table below.
>
> **Stable-ID note:** the frontmatter ID (`bench-deepseek-h200-fp8`) retains the historical slug from the knowledge-base architecture doc's ID conventions. The target hardware is **H100** — the fleet has no H200s (see [[Fleet Inventory]]). "deepseek h200 fp8" is preserved as an alias.

## What Was Measured

Nothing yet. This note scopes a run of [[DeepSeek V4 Flash]] served at FP8 quantization on [[NVIDIA H100]] hardware (the fleet's current flagship), using the benchmark harness (roadmap Milestone 0.4) and the Performance Lab (Phase 3). Serving-engine selection is still open — see [[Open Questions]].

## Setup

| Parameter | Value |
|-----------|-------|
| Model | [[DeepSeek V4 Flash]] |
| Serving Runtime | Candidates: vLLM / SGLang / TensorRT-LLM (TBD) |
| Quantization | FP8 |
| GPU type / count | [[NVIDIA H100]] (80GB HBM3 @ ~3.35 TB/s); count TBD (SPOT has 20) |
| Topology | TBD (NVLink / NVSwitch — hardware-fit pending) |
| Parallelism | Tensor + expert parallelism (MoE); profile TBD |
| Batch config | TBD (tuned in Performance Lab) |
| Workload profile | Production-shaped: short chat, long context, coding, tool calls, structured output |

> A companion [[AMD Instinct]] FP8 run (vLLM/SGLang only — no TensorRT-LLM on ROCm) should be added once that capacity lands (~Oct 2026).

## Results

No measurements exist. All cells are pending until the run executes.

| Metric | Value | Unit |
|--------|-------|------|
| TTFT P50 / P95 | pending | ms |
| Output tokens/sec | pending | tokens/s |
| Tokens/sec/GPU | pending | tokens/s/GPU |
| Concurrency | pending | requests |
| Cost / 1M tokens | pending | USD |

## Validates

Once executed with recorded results, this run will upgrade the following from `assumed` to `measured`:

| Claim / Coefficient | ID | Confidence After |
|---------------------|----|------------------|
| [[FP8 Throughput Factor]] | coeff-fp8-throughput | measured |
| [[Tokens per GPU-Second]] | met-tokens-per-gpu-second | measured |
| [[Available Hardware Sufficient for Priority Models]] | asm-h200-sufficient | partially |

## See Also

- [[Evidence Hub]]
- [[Benchmark Library]]
- [[Validate DeepSeek H100 FP8]]
- [[Fleet Inventory]]
