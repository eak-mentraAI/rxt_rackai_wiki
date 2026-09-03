---
id: evt-new-model-detected
type: event
status: draft
owner: model-enablement
domain: model-enablement
aliases: [new model detected, model radar signal, launch candidate detected]
related: [wf-model-launch-factory, met-model-launch-lag, ent-model]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
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

## See Also

- [[Operations Hub]]
