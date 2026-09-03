---
id: ent-model-deployment
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [model deployment, deployment, serving deployment]
related: [ent-model, ent-model-deployment-spec, ent-serving-runtime, ent-capacity-pool, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: a concrete running instance of a Model on a runtime, capacity pool, and hardware."
---

# Model Deployment

## Definition

A **Model Deployment** is a concrete, running instance of a [[Model]] — a specific set of weights served through a specific [[Serving Runtime]] configuration, drawing from a specific [[Capacity Pool]], on specific hardware and [[Topology]]. It is the operational unit that produces tokens, emits telemetry, and is scaled, canaried, and rolled back. One Model may have several Model Deployments; each Model Deployment serves exactly one Model.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → Model Deployment → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Deployment ID | Stable identifier for the running instance | string | validated |
| Model + version | The Model and weight version served | ref | validated |
| Runtime config | Engine, version, and serving flags | ref | measured |
| Quantization | Active precision (BF16/FP8/FP4/INT8) | enum | measured |
| Parallelism | TP / PP / EP / DP configuration | struct | measured |
| GPU requirement | GPU type and count | struct | measured |
| Context served | Maximum context this deployment supports | int | measured |
| Capability flags | Enabled API capabilities | set | measured |
| Routing policy | How OpenRouter/internal routing targets it | ref | derived |
| Scaling policy | Autoscaling rules | ref | derived |
| Health checks | Liveness/readiness definition | ref | derived |
| Benchmark profile | Reference benchmark run for this config | ref | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Provisioning | Weights loading, workers starting | Placement decided | Workers healthy |
| Internal | Serving internal/synthetic traffic only | Health checks pass | Promoted to canary |
| Canary | Serving limited external traffic under watch | Passes internal validation | Passes canary gate |
| Production | Serving full OpenRouter traffic | Canary gate passed | Draining begins |
| Draining | No new requests, finishing in-flight | Rollback or scale-down triggered | In-flight complete |
| Retired | Torn down, capacity released | Draining complete | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| SERVES | [[Model]] | → | Exactly one Model (invariant) |
| DECLARES | [[Model Deployment Specification]] | → | Exactly one spec (invariant) |
| RUNS_ON | [[Serving Runtime]] | → | Exactly one runtime config (invariant) |
| DRAWS_FROM | [[Capacity Pool]] | → | Exactly one pool (invariant) |
| PLACED_ON | [[GPU Node]] | → | One or more nodes within a cluster |
| CONSTRAINED_BY | [[Topology]] | → | Placement respects topology requirements |
| VALIDATED_BY | [[Benchmark Run]] | → | Performance evidence |
| ROUTED_TO_BY | [[OpenRouter Provider Integration]] | ← | Receives traffic via the provider layer |

## Graph Invariants

- Serves exactly one Model.
- Declares exactly one Model Deployment Specification.
- Runs on exactly one Serving Runtime configuration.
- Draws from exactly one Capacity Pool.

## Evidence

- Source: roadmap Phase 1 (standard deployment contract, scheduling) and Phase 2 (production launch).
- Confidence rationale: entity structure `validated` by the roadmap's standard deployment contract; per-deployment attribute values are `measured` from benchmark/telemetry once a deployment exists.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment Specification]]
- [[Standard Model Deployment]]
