---
id: evt-demand-forecast-published
type: event
status: draft
owner: finops
domain: capacity
aliases: [demand forecast published, forecast published]
related: [wf-demand-forecasting, wf-autoscaling, wf-gpu-reallocation, hub-operations]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Domain event: a demand forecast has been produced for a Model × cluster × time window."
---

# Demand Forecast Published

## Definition

Signals that [[Demand Forecasting]] has produced a new forecast for a Model × cluster × time window. It is the hand-off point from forecasting to the capacity-management workflows that act on it.

## Payload

| Field | Type | Description |
|-------|------|-------------|
| model | ref | The [[Model]] the forecast is for |
| cluster | ref | The [[GPU Cluster]] scope |
| window | timerange | The forecast time window |
| forecast | struct | Predicted demand (requests/tokens) over the window |
| confidence | enum | Forecast confidence state |

## Emitted By

| Source | Workflow | Condition |
|--------|----------|-----------|
| Forecast engine | [[Demand Forecasting]] | A forecast is produced for a window |

## Consumed By

| Consumer | Action Taken |
|----------|--------------|
| [[Autoscaling]] | Adjusts serving replicas ahead of predicted load |
| [[GPU Reallocation]] | Rebalances capacity pools toward predicted demand |

## See Also

- [[Operations Hub]]
- [[Demand Forecasting]]
