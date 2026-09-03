---
id: val-deepseek-h200-fp8
type: validation
status: draft
owner: performance-eng
domain: performance
aliases: [validate deepseek h100 fp8, deepseek fp8 validation, validate deepseek h200 fp8]
related: [hub-evidence, idx-validation-register, bench-deepseek-h200-fp8, asm-fp8-quality-neutral, asm-h200-sufficient, ent-gpu-h100]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Verify DeepSeek V4 Flash TTFT and tokens/sec/GPU at FP8 on H100 meet competitive thresholds — status open."
---

# Validate DeepSeek H100 FP8

> **Stable-ID note:** the frontmatter ID (`val-deepseek-h200-fp8`) retains its original slug from the architecture doc's ID conventions. Target hardware is **H100** (the fleet has no H200s — see [[Fleet Inventory]]).

## What Is Being Validated

That [[DeepSeek V4 Flash]] TTFT and tokens/sec/GPU at FP8 on [[NVIDIA H100]] meet competitive thresholds against leading OpenRouter providers serving the same model — some of whom may run H200- or Blackwell-class hardware.

## Method

Run the benchmark harness (roadmap Milestone 0.4) against the planned run defined in [[DeepSeek H100 FP8 Benchmark]], then feed results through the competitive comparison pipeline (Milestone 3.11) to measure the gap to the competitive frontier. Repeat on [[AMD Instinct]] once that capacity lands.

## Documents This Can Change

| Document | Field / Value | Potential Change |
|----------|---------------|------------------|
| [[FP8 Throughput Factor]] | coefficient value | assumed → measured |
| [[Tokens per GPU-Second]] | metric baseline | assumed → measured |
| [[Available Hardware Sufficient for Priority Models]] | assumption | assumed → measured/refuted |
| [[DeepSeek V4 Flash]] | scorecard rows (TTFT, tokens/sec/GPU) | populated from run |

## Status

| Status | Result | Date |
|--------|--------|------|
| open | pending — no run yet | — |

## See Also

- [[Evidence Hub]]
- [[Validation Register]]
- [[Benchmark Library]]
