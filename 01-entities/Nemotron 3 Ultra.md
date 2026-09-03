---
id: ent-nemotron-3-ultra
type: entity
status: draft
owner: model-enablement
domain: model-enablement
aliases: [nemotron 3 ultra, nemotron 3, nemotron ultra]
related: [ent-model, ent-model-deployment, ent-serving-runtime, ent-capacity-pool, ent-benchmark-run, hub-entities]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Priority Model instance: Nemotron 3 Ultra, the bet-ahead, NVIDIA-aligned enterprise/agentic model."
---

# Nemotron 3 Ultra

## Definition

**Nemotron 3 Ultra** is a priority [[Model]] instance — Rack AI's "bet ahead" model. It is NVIDIA-aligned and positioned for enterprise and agentic workloads, representing the forward-looking slot in the model portfolio. It is an instance of the [[Model]] entity and inherits that note's canonical definition.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

Nemotron 3 Ultra is a specific Model; its deployments follow the standard chain below it.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Strategic role | Bet ahead | enum | validated |
| Ecosystem alignment | NVIDIA-aligned | enum | validated |
| Target workloads | Enterprise and agentic | set | validated |
| Architecture | Specific architecture not yet confirmed here | enum | assumed |
| Total parameters | Not yet confirmed here | int | assumed |
| Active parameters | Not yet confirmed here | int | assumed |
| Context length | Not yet confirmed here | int | assumed |

> **Open question:** Nemotron 3 Ultra architecture specifics, parameter counts, and context length are not yet confirmed and are marked `assumed`. Confirm against primary NVIDIA release notes before promoting confidence.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Watch | Tracked as the forward bet | Emerging strategic relevance | Promoted to Prepare |
| Prepare | Readiness work for the model bet | Strategically prioritized | Weights usable |
| Launch Candidate | Moving through the launch factory | Usable weights + intake pass | Production gate passed |
| Production | Serving live OpenRouter traffic | Canary passed | Retired or superseded |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| INSTANCE_OF | [[Model]] | → | Priority Model instance |
| SERVED_BY | [[Model Deployment]] | → | One or more deployments |
| RUNS_ON | [[Serving Runtime]] | → | NVIDIA-aligned; may favor NVIDIA-only engines for peak throughput |
| ASSIGNED_TO | [[Capacity Pool]] | → | Dedicated per-model Nemotron pool |
| VALIDATED_BY | [[Benchmark Run]] | → | Performance evidence per config |

## Evidence

- Source: strategy narrative (bet-ahead slot; NVIDIA alignment; enterprise/agentic) and roadmap (priority model enablement).
- Confidence rationale: the strategic role, NVIDIA alignment, and target workloads are `validated` by the source docs; specific architecture, parameter counts, and context length are `assumed` pending confirmation.

## See Also

- [[Entity Ontology Hub]]
- [[Model]]
- [[Serving Runtime]]
