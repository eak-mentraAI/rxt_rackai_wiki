---
id: idx-scorecard-deepseek
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [deepseek scorecard, deepseek v4 flash scorecard]
related: [hub-wiki, ent-model, met-tokens-per-gpu-second, met-ttft, ent-deepseek-v4-flash, fml-cost-per-1m-tokens, fml-revenue-per-gpu-hour, val-deepseek-h200-fp8]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-wiki
summary: "Operating scorecard for DeepSeek V4 Flash — win-now flagship benchmark model."
---

# DeepSeek V4 Flash Scorecard

Model: [[DeepSeek V4 Flash]]

**Role:** Win now / benchmark. DeepSeek is the flagship benchmark used to prove Rack AI can operate at elite inference performance and efficiency.

This scorecard **summarizes** the operating metrics defined canonically at L2; it does not redefine them. Each metric links to its canonical note. Every "Current" value is pending because no benchmark run or production telemetry exists yet.

## Operating Scorecard

| Metric | Target Direction | Current | Confidence | Source |
|--------|:----------------:|---------|:----------:|--------|
| [[Productive GPU Utilization]] (GPU utilization) | ↑ | no run yet | assumed | no run yet |
| [[Tokens per GPU-Second]] (Tokens/sec/GPU) | ↑ | no run yet | assumed | no run yet |
| [[Output Throughput]] | ↑ | no run yet | assumed | no run yet |
| [[TTFT]] (P50 / P95) | ↓ | no run yet | assumed | no run yet |
| Queueing delay | ↓ | no run yet | assumed | no run yet |
| [[Availability]] (>99.9%) | ↑ | no run yet | assumed | no run yet |
| Error rate | ↓ | no run yet | assumed | no run yet |
| [[Model Launch Lag]] (<24h median) | ↓ | no run yet | assumed | no run yet |
| Capability coverage | ↑ | no run yet | assumed | no run yet |
| [[Cost per 1M Tokens]] | ↓ | no run yet | assumed | no run yet |
| [[Revenue per GPU-Hour]] | ↑ | no run yet | assumed | no run yet |

## Notes

- **Confidence:** all rows are `assumed` — nothing has been measured. Each row will move to `derived`/`measured`/`validated` only when it cites a specific [[Benchmark Run]] or production telemetry source.
- **OpenRouter rank is an outcome, not a target.** Top-five OpenRouter performance is the external validation that these metrics are moving in the right direction, not a value engineers optimize directly.

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note).

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[DeepSeek V4 Flash]] | → | Operating scorecard for this model (rows assumed until a Benchmark Run is cited) |
| DEPENDS_ON | [[Tokens per GPU-Second]] | → |  |
| DEPENDS_ON | [[TTFT]] | → |  |
| DEPENDS_ON | [[Cost per 1M Tokens]] | → |  |
| DEPENDS_ON | [[Revenue per GPU-Hour]] | → |  |
| VALIDATES | [[Validate DeepSeek H100 FP8]] | ← | Would populate TTFT and tokens/GPU-s rows |

## See Also

- [[Wiki Hub]]
- [[Metric Index]]
