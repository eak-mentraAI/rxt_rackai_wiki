---
id: ent-model
type: entity
status: draft
owner: model-enablement
domain: model-enablement
aliases: [model, foundation model, open-weight model, llm]
related: [ent-model-deployment, ent-model-deployment-spec, ent-openrouter-integration, hub-entities]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: an open-weight model Rack AI serves as an inference product on OpenRouter."
---

# Model

## Definition

A **Model** is an open-weight language (or multimodal) model that Rack AI serves as an inference product. It is the unit OpenRouter consumers request by name and the unit around which every optimization program, scorecard, and capacity pool is organized. A Model is distinct from any single deployment of it — the same Model can have multiple [[Model Deployment]]s across hardware and regions.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → Model → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A Model is the highest platform-owned entity in the chain. Above it sits only market demand.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Identity | Canonical name and version (e.g., DeepSeek V4 Flash) | string | validated |
| Weight source | Origin of the weights (Hugging Face, model lab, NVIDIA) | string | validated |
| Architecture | Dense, MoE, MLA, multimodal, reasoning, hybrid attention | enum | measured |
| Parameter count | Total parameters | int | measured |
| Active parameter count | Parameters activated per token (MoE) | int | measured |
| Context length | Maximum supported context window | int | measured |
| Tokenizer | Tokenizer identity/version | string | measured |
| Native precision | Precision the weights ship in (BF16, FP8, etc.) | enum | measured |
| Capability surface | Tool calling, structured output, reasoning controls, multimodal, prompt caching, streaming | set | measured |
| Strategic role | Win-now benchmark, growth, or forward bet | enum | validated |
| License | Distribution license (e.g., MIT, Apache-2.0) | string | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Watch | Tracked on the [[Model Radar]] but not being prepared | Identified as strategically relevant | Promoted to Prepare |
| Prepare | Pre-release readiness work underway | Architecture likely supported and demand probable | Weights become usable |
| Launch Candidate | Weights available, moving through the [[Model Launch Factory]] | Usable weights + passing intake | Passes production gate |
| Production | Serving live OpenRouter traffic | Canary passed, published | Retired or deprecated |
| Deprecated | Withdrawn from active serving | Superseded or demand collapsed | Archived |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| SERVED_BY | [[Model Deployment]] | → | One Model, one or more deployments |
| DECLARES | [[Model Deployment Specification]] | → | Deployment intent declared per deployment |
| PUBLISHED_VIA | [[OpenRouter Provider Integration]] | → | Exposed to consumers as an endpoint |
| MEASURED_BY | [[Model Scorecard]] | ← | Operating metrics tracked per Model |
| TRACKED_ON | [[Model Radar]] | ← | Discovery and readiness pipeline |
| CHARACTERIZED_BY | [[Traffic Class]] | → | Real workload shape per Model |
| BELONGS_TO | [[Organization]] | → | On the platform, a Model is registered within a tenant org |
| USES | [[Registry Credential]] | → | Weights fetched via a registry credential (e.g. HF token) |
| TARGETED_BY | [[LoRA Adapter]] | ← | Adapters target a specific base Model |
| CONFIGURED_BY | [[Model Class]] | → | A Model Class binds the Model to a runtime + engine config |

## RackAI Platform Reality

On the RackAI platform, a Model is a Kubernetes custom resource (`Model` CRD) registered within an [[Organization]] and reconciled by the [[RackAI Control Plane]]. Beyond the OpenRouter-facing view above, the shipped product model adds:

- **Source type** — weights come from a URI (e.g. `hf://…`) or direct upload.
- **Reconciliation phase** — `Pending → Processing → Ready → Failed` (plus cache states), surfaced via CRD `status`.
- **Registration** — via console (Resources → Models), CLI (`rackaictl`), or the resource API; gated weights use a [[Registry Credential]].

This platform view (`measured`, from the 1.0.0 docs and API reference) and the OpenRouter product view above describe the same canonical Model from two angles: what tenants register versus what OpenRouter demand consumes.

## Priority Models

| Model | Role | Canonical Note |
|-------|------|----------------|
| DeepSeek V4 Flash | Win now — benchmark | [[DeepSeek V4 Flash]] |
| GLM 5.3 Flash | Win now — growth | [[GLM 5.3 Flash]] |
| Nemotron 3 Ultra | Bet ahead | [[Nemotron 3 Ultra]] |

The third slot is intentionally rotatable — Rack AI always maintains one emerging-model bet.

## Evidence

- Source: strategy narrative (model bets, capability completeness) and roadmap (model intake, architecture compatibility).
- Confidence rationale: the entity definition and its role in the abstraction chain are `validated` by both source documents; specific per-model attributes carry their own confidence on each model note.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment]]
- [[Model Radar]]
