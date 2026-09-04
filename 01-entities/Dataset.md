---
id: ent-dataset
type: entity
status: draft
owner: model-enablement
domain: platform
aliases: [dataset, training dataset, training data]
related: [ent-fine-tuning-job, ent-organization, wf-fine-tuning, hub-entities]
source_docs: [rackai_console_docs, rackai_ui_architecture]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: uploaded training data consumed by fine-tuning jobs."
---

# Dataset

## Definition

A **Dataset** is uploaded training data used to fine-tune a base [[Model]] on RackAI. Datasets are uploaded as `.jsonl` files in one of two formats — `messages` (chat-style turns) or `files` — with a maximum size of 1GB. Each Dataset carries a reconciliation status (for example, `Ready`) that reflects whether the platform has validated and prepared it for training. A Dataset is consumed by a [[Fine-Tuning Job]] and belongs to exactly one [[Organization]].

## Layer

L1 — Entity Ontology. A Dataset is an input to the fine-tuning pipeline:

**[[Dataset]] → [[Fine-Tuning Job]] → [[LoRA Adapter]] → [[Model Deployment]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Dataset ID | Stable identifier | string | measured |
| Format | `messages` or `files` | enum | measured |
| File type | `.jsonl` | enum | measured |
| Max size | 1GB upload limit | int | measured |
| Reconciliation status | Preparation state (e.g., `Ready`) | enum | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Uploading | File transfer in progress | Upload initiated | Transfer complete |
| Reconciling | Platform validating/preparing data | Upload complete | Validation resolves |
| Ready | Validated and available for training | Reconciliation succeeds | Deleted |
| Failed | Validation or preparation failed | Reconciliation error | Re-uploaded or deleted |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSUMED_BY | [[Fine-Tuning Job]] | ← | A job consumes one dataset |
| BELONGS_TO | [[Organization]] | → | Org-scoped, in the org namespace |

## Evidence

- Source: `rackai_console_docs`, `rackai_ui_architecture`.
- Confidence rationale: `measured` — `.jsonl` format, `messages`/`files` options, the 1GB limit, and reconciliation status are shipped and documented.

## See Also

- [[Entity Ontology Hub]]
- [[Fine-Tuning Job]]
- [[Fine-Tuning]]
