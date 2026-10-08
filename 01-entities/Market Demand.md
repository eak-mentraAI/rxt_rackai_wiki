---
id: ent-market-demand
type: entity
status: draft
owner: finops
domain: commercial
aliases: [market demand, demand signal, model demand, openrouter demand, inference demand, demand node]
related: [ent-traffic-class, ent-model, ent-deepseek-v4-flash, ent-glm-5-3-flash, ent-openrouter-integration, ent-organization, wf-demand-forecasting, wf-model-radar, wf-request-routing, evt-demand-forecast-published, asm-openrouter-initial-share, asm-traffic-peak-multiplier, asm-traffic-follows-performance, idx-gpu-capacity-demand-rationale, bench-openrouter-leaderboard-2026-09, idx-moc-serving-platform, hub-entities]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md, "reference/RackAI - GPU Capacity.xlsx", 04-evidence/benchmarks/OpenRouter Leaderboard Snapshot.md]
confidence: derived
last_reviewed: 2026-10-08
parent: hub-entities
summary: "Canonical head of the serving chain: inference demand per Model and Traffic Class, from OpenRouter and direct tenants."
---

# Market Demand

## Definition

**Market Demand** is the inference demand (tokens and requests over time) for a [[Model]], broken down by [[Traffic Class]] and by channel. There are two channels: the **OpenRouter** provider pool (all providers serving that model, of which RackAI wins a share) and **direct RackAI tenants** ([[Organization]]s calling deployment endpoints). It is the head of the serving chain. Demand is expressed against Model endpoints, never against GPUs.

This note is the single canonical home for "demand". The other demand notes link here. [[Demand Forecasting]] forecasts it. [[Demand Forecast Published]] carries the forecast. [[Model Radar]] reads it as a launch signal. [[GPU Capacity Demand Rationale]] turns it into GPU counts.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

Market Demand is the first hop. Its shape (per [[Traffic Class]]) constrains deployment configuration further down the chain. Its volume drives [[Autoscaling]], [[GPU Reallocation]] and the [[Procurement Trigger]] through the forecast.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Model | The [[Model]] the demand is for | ref | validated |
| Traffic Class | Workload shape, e.g. long-context, coding, short chat ([[Traffic Class]]) | ref | derived |
| Channel | OpenRouter provider pool, or direct tenant | enum | validated |
| Pool volume | Tokens per period across **all** OpenRouter providers for the model | float | measured (2026-09-03 snapshot only) |
| RackAI share | Fraction of pool volume routed to RackAI | ratio | assumed |
| Peak-to-average | Peak multiplier used for sizing | ratio | assumed |
| Trend | Growth rate of pool volume | float | measured (snapshot) |
| Direct-tenant demand | Committed or agreed enterprise demand | float | assumed |

## Current Demand Evidence (priority models)

| Model | OpenRouter pool volume (all providers) | Trend | RackAI share | Source |
|-------|------------------------------------------|-------|--------------|--------|
| [[DeepSeek V4 Flash]] (0731) | 47.8T tokens/month; 11.4T/week | month ↑>999%; week ↓8% | none (not live) | [[OpenRouter Leaderboard Snapshot]] (measured, 2026-09-03) |
| [[GLM 5.3 Flash]] | 11.8T tokens/month; 11.4T/week | ↑>999% (breakout) | <1% at launch; 15–25% base case (assumed) | [[OpenRouter Leaderboard Snapshot]], [[OpenRouter Initial Market Share]] |

The pool volumes are a **measured market** figure for one date. RackAI's own share, the per-Traffic-Class split (for example, how much of the volume is long-context coding) and the peak multiplier are all `assumed`. No RackAI telemetry exists yet. No canonical demand *metric* note exists yet. Pool volume and share are attributes here until telemetry defines one.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Observed | Market volume seen in OpenRouter rankings or tenant requests | Leaderboard snapshot or a tenant request | Forecast produced |
| Forecast | Projected per Model × cluster × window | [[Demand Forecast Published]] | Served or re-forecast |
| Served | Routed to RackAI deployments | Live traffic through [[Request Routing]] | Demand shifts or model retired |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| ROUTES_TO | [[Model]] | → | Demand is expressed against Model endpoints (spine hop 1). Consumers never see GPUs |
| ROUTES_TO | [[DeepSeek V4 Flash]] | → | 47.8T tokens/month pool volume (measured snapshot) |
| ROUTES_TO | [[GLM 5.3 Flash]] | → | 11.4T tokens/week pool volume, breakout mover (measured snapshot) |
| USES | [[Traffic Class]] | → | Demand is segmented by Traffic Class (long-context, coding, ...) |
| ROUTES_TO | [[OpenRouter Provider Integration]] | → | The OpenRouter channel enters through the provider endpoint |
| ROUTES_TO | [[Request Routing]] | → | Live requests are classified and placed on deployments |
| GENERATES | [[Organization]] | ← | Direct-tenant demand comes from tenant Organizations |
| FORECASTS | [[Demand Forecasting]] | ← | Forecast per Model × cluster × window |
| FORECASTS | [[Demand Forecast Published]] | ← | The event carries the published forecast |
| CONSUMES | [[Model Radar]] | ← | OpenRouter demand is one of the Radar's sources |
| CONSUMES | [[GPU Capacity Demand Rationale]] | ← | Converts demand into GPU counts for the prod proposal |
| MEASURES | [[OpenRouter Leaderboard Snapshot]] | ← | Measured pool volume for one date (2026-09-03) |
| CONSTRAINS | [[OpenRouter Initial Market Share]] | ← | RackAI share assumption (<1% at launch) |
| CONSTRAINS | [[Traffic Peak Multiplier]] | ← | 3× peak-to-average assumption |
| SUPPORTS | [[OpenRouter Traffic Follows Performance]] | ← | Routed share is expected to follow measured performance |

## Evidence

- Source: strategy narrative (demand-led model bets); roadmap (demand forecasting, Phase 5); [[OpenRouter Leaderboard Snapshot]] (measured market volumes, 2026-09-03); [[GPU Capacity Demand Rationale]] (the two demand sources and the share scenarios).
- Confidence rationale: `derived`. The concept and the two channels are stated in the sources. Market pool volumes are `measured` for one snapshot date. RackAI share, the Traffic Class split and the peak multiplier are `assumed` until Phase 1 and Phase 3 telemetry exist. Downstream notes must not treat demand for RackAI as measured.

## See Also

- [[Entity Ontology Hub]]
- [[Serving Platform MOC]]
- [[Traffic Class]]
- [[Demand Forecasting]]
