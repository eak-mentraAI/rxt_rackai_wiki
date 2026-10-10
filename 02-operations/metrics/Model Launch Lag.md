---
id: met-model-launch-lag
type: metric
status: draft
owner: model-enablement
domain: model-enablement
aliases: [model launch lag, launch lag, time to production]
related: [wf-model-launch-factory, evt-new-model-detected, evt-deployment-canary-passed, ent-model, ent-openrouter-integration, wf-model-radar, val-launch-lag-24h, evd-kpi-telemetry-targets]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-09
parent: hub-operations
summary: "Elapsed time from publicly usable weights to a production Rack AI endpoint; target <24h median / <72h P90."
---

# Model Launch Lag

> **Roadmap status (2026-10-09).** Not yet measured. The roadmap row *Model Launch Lag instrumentation* (Should, MOE-1) measures it from the first onboarding, so a baseline exists before the <24h / <72h target is committed.

## Definition

Measures how quickly Rackspace turns new model availability into production inference: the elapsed time from publicly usable weights to a production Rack AI endpoint on OpenRouter. It answers whether we can capture demand while a new model is still accelerating, and it is the primary KPI of the [[Model Launch Factory]].

## KPI Job

Serves internal operating decisions (velocity target for the launch factory) and strategic positioning (demand capture while a model is still accelerating) — jobs 1 and 4 per [[KPI Telemetry Target List]]. Different in kind from the serving metrics: it needs the launch pipeline to stamp lifecycle-event timestamps, not a metrics scrape.

## Unit

hours (reported as median and P90).

## Source or Formula

- Measured from: pipeline timestamps — clock starts at usable-weights availability ([[New Model Detected]]) and stops at production publication ([[Deployment Canary Passed]] → publish via [[OpenRouter Provider Integration]]).
- Not a formula — a measured duration.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↓ | <24h median / <72h P90 (roadmap target) | Day-zero readiness where pre-release prep is possible |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model]] | MEASURES → |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Model]] | → | Per model launch |
| MEASURES | [[Model Launch Factory]] | → | Headline KPI of the factory |
| MEASURES | [[Model Radar]] | → | Radar's primary KPI |
| DEPENDS_ON | [[New Model Detected]] | → | Clock start |
| DEPENDS_ON | [[Deployment Canary Passed]] | → | Clock stop (then publication) |
| VALIDATES | [[Validate Launch Lag Under 24h]] | ← | Open validation of the <24h median target |

## Evidence

- Confidence rationale: `assumed` — the <24h/<72h figures are roadmap targets (KPI #4), not measured Rack AI values. They become `measured` once launches complete through the factory.

## See Also

- [[Operations Hub]]
