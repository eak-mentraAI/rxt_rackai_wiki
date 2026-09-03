---
id: met-model-launch-lag
type: metric
status: draft
owner: model-enablement
domain: model-enablement
aliases: [model launch lag, launch lag, time to production]
related: [wf-model-launch-factory, evt-new-model-detected, evt-deployment-canary-passed, ent-model, ent-openrouter-provider-integration]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Elapsed time from publicly usable weights to a production Rack AI endpoint; target <24h median / <72h P90."
---

# Model Launch Lag

## Definition

Measures how quickly Rackspace turns new model availability into production inference: the elapsed time from publicly usable weights to a production Rack AI endpoint on OpenRouter. It answers whether we can capture demand while a new model is still accelerating, and it is the primary KPI of the [[Model Launch Factory]].

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

## Evidence

- Confidence rationale: `assumed` — the <24h/<72h figures are roadmap targets (KPI #4), not measured Rack AI values. They become `measured` once launches complete through the factory.

## See Also

- [[Operations Hub]]
