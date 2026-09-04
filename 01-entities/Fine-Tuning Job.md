---
id: ent-fine-tuning-job
type: entity
status: draft
owner: model-enablement
domain: platform
aliases: [fine-tuning job, finetuning job, training job, sft job]
related: [ent-dataset, ent-lora-adapter, ent-organization, ent-model, wf-fine-tuning, hub-entities]
source_docs: [rackai_console_docs, rackai_ui_architecture]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: a training run that consumes a Dataset and produces a LoRA Adapter."
---

# Fine-Tuning Job

## Definition

A **Fine-Tuning Job** is a training run that adapts a base [[Model]] to a [[Dataset]]. The shipped method is `supervised` (SFT); `reinforcement` and `dpo` methods are surfaced as "Coming Soon". Jobs expose SFT and QLoRA hyperparameters and support an optional evaluation split (default 90:10 train:eval). On AMD hardware, the platform auto-configures an AMD recipe. A job progresses through `Running`, `Completed`, and `Failed` statuses. Each Fine-Tuning Job consumes exactly one Dataset and produces a [[LoRA Adapter]], and belongs to exactly one [[Organization]].

## Layer

L1 — Entity Ontology. The job is the transform step of the fine-tuning pipeline:

**[[Dataset]] → Fine-Tuning Job → [[LoRA Adapter]] → [[Model Deployment]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Job ID | Stable identifier | string | measured |
| Method | `supervised` (shipped); `reinforcement`, `dpo` ("Coming Soon") | enum | measured (SFT), assumed (RL/DPO) |
| Base model ref | The Model being fine-tuned | ref | measured |
| Dataset ref | The consumed Dataset | ref | measured |
| Hyperparameters | SFT + QLoRA tuning parameters | struct | measured |
| Eval split | Optional; default 90:10 train:eval | ratio | measured |
| AMD recipe | Auto-configured on AMD hardware | bool | measured |
| Status | `Running`, `Completed`, `Failed` | enum | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Running | Training in progress | Job submitted and scheduled | Training finishes or errors |
| Completed | Training finished successfully | Training converges/completes | — (adapter produced) |
| Failed | Training errored | Runtime or data error | Re-submitted |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSUMES | [[Dataset]] | → | Exactly one dataset |
| PRODUCES | [[LoRA Adapter]] | → | Produces an adapter on success |
| BELONGS_TO | [[Organization]] | → | Runs in the org namespace |
| USES | [[Model]] | → | Fine-tunes a base model |

## Evidence

- Source: `rackai_console_docs`, `rackai_ui_architecture`.
- Confidence rationale: SFT/QLoRA path, eval split default, AMD recipe auto-config, and job statuses are `measured` (shipped). `reinforcement` and `dpo` are `assumed` — surfaced as "Coming Soon" only.
- **Conflict / open question:** the method enum advertises `reinforcement` and `dpo`, but only `supervised` is shipped. Treat RL/DPO as planned (`assumed`) until a release confirms them; the gap is an open question. Shipped beats planned.

## See Also

- [[Entity Ontology Hub]]
- [[Dataset]]
- [[LoRA Adapter]]
- [[Fine-Tuning]]
