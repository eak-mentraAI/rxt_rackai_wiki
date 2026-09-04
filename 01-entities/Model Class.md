---
id: ent-model-class
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [model class, model template, serving template]
related: [ent-serving-runtime, ent-model, ent-model-deployment, hub-entities]
source_docs: [rackai_ui_architecture, rackai_release_1_0_0]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: a reusable template binding a base Model to a Serving Runtime and engine configuration."
---

# Model Class

## Definition

A **Model Class** is a reusable template that binds a base [[Model]] to a [[Serving Runtime]] and its engine configuration (for example, `vllmConfig`). It captures the "how to serve this model" decision — which runtime family, which engine flags — so that a [[Model Deployment]] can instantiate it consistently. The supported runtime enum is `vllm`, `nim`, `optimized-nim-vllm`, and `aim`. A Model Deployment instantiates exactly one Model Class.

## Layer

L1 — Entity Ontology. The Model Class sits between the Model and its runtime configuration in the serving chain:

**[[Model]] → Model Class → [[Serving Runtime]] → [[Model Deployment]] → [[Accelerator Class]] → [[GPU Fleet]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Class ID | Stable identifier for the template | string | measured |
| Base model ref | The Model this class configures | ref | measured |
| Runtime | Serving runtime family: `vllm`, `nim`, `optimized-nim-vllm`, `aim` | enum | measured |
| Engine config | Engine tuning block (e.g., `vllmConfig`) | struct | measured |

## Lifecycle States

Not a stateful entity. (A Model Class is a declarative template; runtime state lives on the [[Model Deployment]] that instantiates it.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| USES | [[Serving Runtime]] | → | Selects the runtime family and engine config |
| DECLARES | [[Model]] | → | Declares serving config for a base model |
| INSTANTIATED_BY | [[Model Deployment]] | ← | A deployment instantiates one Model Class |

## Evidence

- Source: `rackai_ui_architecture`, `rackai_release_1_0_0`.
- Confidence rationale: `measured` — the runtime enum (`vllm`, `nim`, `optimized-nim-vllm`, `aim`) and the Model Class → Deployment relationship are shipped in 1.0.0 and reflected in the UI architecture.

## See Also

- [[Entity Ontology Hub]]
- [[Serving Runtime]]
- [[Model Deployment]]
