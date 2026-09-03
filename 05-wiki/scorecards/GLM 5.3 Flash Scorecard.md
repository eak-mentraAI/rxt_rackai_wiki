---
id: idx-scorecard-glm
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [glm scorecard, glm 5.3 flash scorecard]
related: [hub-wiki, ent-model, met-tokens-per-gpu-second, met-ttft]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Operating scorecard for GLM 5.3 Flash — win-now growth-curve model."
---

# GLM 5.3 Flash Scorecard

Model: [[GLM 5.3 Flash]]

**Role:** Win now / growth. GLM is growing rapidly in coding and agentic workloads; the objective is to deploy quickly, optimize aggressively, and scale capacity with demand.

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

## See Also

- [[Wiki Hub]]
- [[Metric Index]]
