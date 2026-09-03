---
id: ent-model-deployment-spec
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [model deployment specification, deployment spec, deployment contract, standard deployment contract]
related: [ent-model, ent-model-deployment, ent-serving-runtime, ent-capacity-pool, ent-benchmark-run, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: the declared contract every Model Deployment must satisfy."
---

# Model Deployment Specification

## Definition

A **Model Deployment Specification** is the declared, versioned contract that every [[Model Deployment]] must satisfy before it can serve traffic. It states, up front, what a deployment of a given [[Model]] is supposed to be — its identity and version, weight source, runtime, quantization, supported context, GPU requirement, parallelism, API capabilities, routing and scaling policy, health checks, and reference benchmark profile. The spec is the intent; the deployment is the realization. Each Model Deployment declares exactly one specification.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

The specification is the declared contract that sits alongside a Model Deployment — it constrains the deployment without being a runtime object itself.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Model identity + version | The Model and weight version the spec targets | ref | validated |
| Weight source | Origin and pinning of the weights (Hugging Face, model lab, NVIDIA) | ref | validated |
| Runtime | Declared [[Serving Runtime]] engine and version | ref | validated |
| Quantization | Required active precision (BF16/FP8/FP4/INT8) | enum | validated |
| Supported context | Maximum context window the deployment must serve | int | validated |
| GPU requirement | GPU type, generation, and count | struct | validated |
| Parallelism config | TP / PP / EP / DP configuration | struct | validated |
| API capabilities | Required capability surface (tools, structured output, streaming, prompt caching) | set | validated |
| Routing policy | Declared routing behavior for the deployment | ref | derived |
| Scaling policy | Declared autoscaling rules and bounds | ref | derived |
| Health checks | Required liveness/readiness definitions | ref | derived |
| Benchmark profile | Reference [[Benchmark Run]] the deployment is measured against | ref | validated |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Draft | Spec being authored, not yet approved | Model selected for deployment | Passes review |
| Approved | Reviewed and ready to instantiate | Review and invariants pass | Deployment created against it |
| Active | One or more deployments currently declare it | Deployment instantiated | Superseded by a new version |
| Superseded | Replaced by a newer spec version | Newer version approved | Archived |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| DECLARED_BY | [[Model Deployment]] | ← | Each deployment declares exactly one spec (invariant) |
| SPECIFIES | [[Model]] | → | Identity and version the spec targets |
| REQUIRES | [[Serving Runtime]] | → | Declares the runtime engine and version |
| CONSTRAINS | [[GPU Node]] | → | GPU type and count requirement |
| VALIDATED_BY | [[Benchmark Run]] | → | Reference benchmark profile |

## Graph Invariants

- Each Model Deployment declares exactly one Model Deployment Specification.
- The spec references a Model and its version, never individual GPU hardware beyond a GPU type/count requirement.

## Evidence

- Source: roadmap Milestone 1.2 (standard deployment contract every deployment must satisfy).
- Confidence rationale: the contract's field set and its role as the declared deployment intent are `validated` by the roadmap; concrete values populated per deployment carry their own confidence.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment]]
- [[Model]]
