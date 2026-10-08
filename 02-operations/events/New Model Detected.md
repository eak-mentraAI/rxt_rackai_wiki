---
id: evt-new-model-detected
type: event
status: draft
owner: model-enablement
domain: model-enablement
aliases: [new model detected, model radar signal, launch candidate detected]
related: [wf-model-launch-factory, met-model-launch-lag, ent-model, wf-model-radar]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Signals that Model Radar has found a strategically relevant model worth moving toward launch."
---

# New Model Detected

## Definition

Signals that Model Radar has identified a strategically relevant [[Model]] — from model labs, Hugging Face, GitHub, NVIDIA, OpenRouter demand, research announcements, or ecosystem partners — that should enter the launch pipeline. Emitted by the Model Radar step of the [[Model Launch Factory]]. (Roadmap Milestone 4.1.)

## Payload

| Field | Type | Description |
|-------|------|-------------|
| model_name | string | Detected model identity |
| source | enum | Where it was detected (huggingface / github / nvidia / model-lab / openrouter / research / partner) |
| architecture_hint | string | Preliminary architecture guess (dense / MoE / multimodal / MLA / hybrid / reasoning) |
| strategic_stage | enum | watch / prepare / launch-candidate |
| detected_at | timestamp | When Radar flagged the model |

## Emitted By

| Source | Workflow | Condition |
|--------|----------|-----------|
| Model Radar | [[Model Launch Factory]] | A strategically relevant model appears |

## Consumed By

| Consumer | Action Taken |
|----------|--------------|
| [[Model Launch Factory]] | Starts automated intake for the candidate |
| [[Model Launch Lag]] | Starts the launch-lag clock at usable-weights availability |
| Model-enablement backlog | Records the candidate in the Watch/Prepare/Launch pipeline |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| GENERATES | [[Model Radar]] | ← | Radar emits when a relevant model appears |
| GENERATES | [[Model Launch Factory]] | ← | Via its Radar step |
| CONSUMES | [[Model Launch Factory]] | ← | Starts automated intake |
| DEPENDS_ON | [[Model Launch Lag]] | ← | Starts the launch-lag clock |
| SUPPORTS | [[Model]] | → | Candidate enters the Prepare → Launch Candidate lifecycle |

## See Also

- [[Operations Hub]]
