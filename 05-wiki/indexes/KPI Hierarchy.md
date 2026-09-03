---
id: idx-kpi-hierarchy
type: index
status: draft
owner: knowledge-graph-steward
domain: strategy
aliases: [kpi hierarchy, headline kpis, kpi tree]
related: [hub-wiki, idx-metrics, src-engineering-roadmap, src-strategic-vision]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "The four headline engineering KPIs, their supporting guardrails, and the executive milestone sequence M1-M10."
---

# KPI Hierarchy

## Purpose

Lists the KPI hierarchy that governs the roadmap: four headline engineering KPIs plus the supporting guardrails, each linked to its canonical metric note. Also records the executive milestone sequence M1–M10. This is a navigation index over canonical metric notes; it does not redefine the metrics.

## Outcome vs. Target

Top-five OpenRouter rank is treated as an **outcome**, not a directly optimized target. It is the external validation that the operating metrics below are moving in the right direction. Engineers optimize the headline KPIs and respect the guardrails; the rank follows as a consequence.

## Headline KPIs

| KPI | Canonical Note | ID | Confidence |
|-----|----------------|----|:----------:|
| Productive GPU Utilization | [[Productive GPU Utilization]] | met-gpu-utilization | assumed |
| Tokens per GPU-Second | [[Tokens per GPU-Second]] | met-tokens-per-gpu-second | assumed |
| TTFT (P50 / P95) | [[TTFT]] | met-ttft | assumed |
| Model Launch Lag | [[Model Launch Lag]] | met-model-launch-lag | assumed |

- **Productive GPU Utilization** — productive inference GPU-hours / available GPU-hours. Answers: are we monetizing the fleet?
- **Tokens per GPU-Second** — infrastructure efficiency. Answers: are we getting better at producing inference from hardware we own?
- **TTFT** — responsiveness. Answers: can we compete for latency-sensitive traffic?
- **Model Launch Lag** — usable model release → Rackspace production. Answers: can we capture demand while a model is still accelerating?

## Supporting Guardrails

| Guardrail | Canonical Note | Direction / Target |
|-----------|----------------|--------------------|
| Availability | [[Availability]] | ↑ (>99.9% for priority models) |
| Error rate | — | ↓ |
| Queueing delay | — | ↓ |
| Capability coverage | — | ↑ |
| Cost / 1M tokens | [[Cost per 1M Tokens]] | ↓ |
| Revenue / GPU-hour | [[Revenue per GPU-Hour]] | ↑ |
| Gross margin / model | — | ↑ |

## Executive Milestone Sequence (M1–M10)

| Milestone | Outcome |
|-----------|---------|
| M1 — Know the Fleet | Inventory, telemetry, cost model, and benchmark harness complete. |
| M2 — Serve One Model Correctly | DeepSeek running through the standard Rack AI inference stack. |
| M3 — Become an OpenRouter Provider | Production DeepSeek traffic flowing and competitive measurements visible. |
| M4 — Prove Repeatability | GLM deployed through the same platform without rebuilding the stack. |
| M5 — Build Performance Advantage | Model-specific optimization closes the gap against leading OpenRouter providers. |
| M6 — Prove Model Velocity | Nemotron or another priority model moves through the new model factory in <72 hours. |
| M7 — Reach <24-Hour Launches | Known architectures become effectively automated model deployments. |
| M8 — Optimize Fleet Utilization | Capacity dynamically moves between models based on real demand. |
| M9 — Optimize Economics | Scheduler incorporates tokens/GPU-second, utilization, and revenue/GPU-hour. |
| M10 — Close the Loop | Performance and capacity optimization become continuous automated processes. |

## See Also

- [[Wiki Hub]]
- [[Metric Index]]
