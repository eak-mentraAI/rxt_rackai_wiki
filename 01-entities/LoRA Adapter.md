---
id: ent-lora-adapter
type: entity
status: draft
owner: model-enablement
domain: platform
aliases: [lora adapter, lora, adapter, fine-tuned adapter]
related: [ent-fine-tuning-job, ent-model, ent-model-deployment, ent-organization, wf-fine-tuning, hub-entities]
source_docs: [rackai_console_docs, rackai_ui_architecture]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: a parameter-efficient adapter produced by a fine-tuning job and hot-loadable onto a deployment."
---

# LoRA Adapter

## Definition

A **LoRA Adapter** is a parameter-efficient fine-tuning artifact. It is produced by a [[Fine-Tuning Job]] (or uploaded directly) and targets exactly one base [[Model]]. An adapter can be hot-loaded onto a running [[Model Deployment]] without re-serving full weights. Adapters carry statuses `Ready`, `Processing`, and `Failed`, plus an `In Use` flag indicating whether the adapter is currently attached to a deployment. Each adapter belongs to exactly one [[Organization]].

## Layer

L1 — Entity Ontology. The adapter is the output of the fine-tuning pipeline and an input to serving:

**[[Dataset]] → [[Fine-Tuning Job]] → LoRA Adapter → [[Model Deployment]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Adapter ID | Stable identifier | string | measured |
| Base model ref | The single base Model the adapter targets | ref | measured |
| Source | Produced by a job, or uploaded | enum | measured |
| Status | `Ready`, `Processing`, `Failed` | enum | measured |
| In Use | Whether currently attached to a deployment | bool | measured |
| Hot-loadable | Can be loaded onto a live deployment | bool | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Processing | Adapter being produced or ingested | Job produces it or upload starts | Processing resolves |
| Ready | Available to attach to a deployment | Processing succeeds | Deleted |
| Failed | Production or ingestion failed | Processing error | Re-created or deleted |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| PRODUCED_BY | [[Fine-Tuning Job]] | ← | Produced by a job (or uploaded) |
| TARGETS | [[Model]] | → | Exactly one base model (invariant) |
| APPLIED_TO | [[Model Deployment]] | → | Hot-loaded onto a deployment |
| BELONGS_TO | [[Organization]] | → | Org-scoped |

## Evidence

- Source: `rackai_console_docs`, `rackai_ui_architecture`.
- Confidence rationale: `measured` — adapter statuses, `In Use` flag, single-base-model targeting, and hot-load behavior are shipped and documented.

## See Also

- [[Entity Ontology Hub]]
- [[Fine-Tuning Job]]
- [[Model Deployment]]
- [[Fine-Tuning]]
