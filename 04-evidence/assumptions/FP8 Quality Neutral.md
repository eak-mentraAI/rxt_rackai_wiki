---
id: asm-fp8-quality-neutral
type: assumption
status: draft
owner: performance-eng
domain: performance
aliases: [fp8 quality neutral, fp8 lossless assumption]
related: [hub-evidence, bench-deepseek-h200-fp8, asm-h200-sufficient, coeff-fp8-throughput, wf-quantization-program, fml-cost-per-1m-tokens, val-deepseek-h200-fp8]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-evidence
summary: "Belief that serving priority models at FP8 does not materially degrade output quality — awaiting Rack AI benchmark."
---

# FP8 Quality Neutral

## Statement

Serving the priority models at FP8 does not materially degrade output quality relative to BF16.

## Rationale

An independent quantization study reports FP8 (W8A8) as effectively lossless across model scales, based on over 500,000 evaluations across academic and real-world tasks — see [Give Me BF16 or Give Me Death (arXiv 2411.02355), Red Hat AI](https://arxiv.org/abs/2411.02355). This supports FP8 as a default serving precision that trades little or no quality for throughput and memory headroom. It is a general-purpose finding, however, not a measurement on Rack AI's specific priority models. Content was rephrased for compliance with licensing restrictions.

## Exit Criterion

A Rack AI quality benchmark comparing the priority models at FP8 vs BF16 (academic benchmarks plus production-shaped tasks) showing no material quality delta. Until then this remains `assumed`.

## Impacts

| Impacted | Type |
|----------|------|
| [[FP8 Throughput Factor]] | SUPPORTS |
| [[Quantization Program]] | SUPPORTS |
| [[Cost per 1M Tokens]] | SUPPORTS |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| SUPPORTS | [[FP8 Throughput Factor]] | → | Quality-safe precision lever |
| SUPPORTS | [[Quantization Program]] | → | FP8 as default candidate |
| SUPPORTS | [[Cost per 1M Tokens]] | → | Lower cost without quality loss |
| VALIDATES | [[Quantization Program]] | ← | Program's quality benchmark is the exit criterion |

## Status

- Confidence: assumed
- Owner: performance-eng
- Target resolution date: TBD (Phase 3 — Quantization Program, Milestone 3.6)

## See Also

- [[Evidence Hub]]
- [[Assumption Register]]
- [[DeepSeek H100 FP8 Benchmark]]
