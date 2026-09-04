---
id: idx-entities
type: index
status: draft
owner: knowledge-graph-steward
domain: platform
aliases: [entity index, L1 entity listing, entities index]
related: [hub-wiki, hub-entities, idx-moc-serving-platform]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Index of the canonical Layer-1 entities of the RackAI platform plus priority model instances."
---

# Entity Index

## Purpose

Lists the canonical Layer-1 (L1) entities that form the semantic backbone of the RackAI platform, plus the three priority model instances. Entities are defined once in their canonical notes; this index only points to those homes and records their graph status. Kept current as entity notes are created.

## Serving Chain Entities

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[Model]] | ent-model | entity | draft | validated |
| [[Model Class]] | ent-model-class | entity | draft | measured |
| [[Model Deployment]] | ent-model-deployment | entity | draft | validated |
| [[Model Deployment Specification]] | ent-model-deployment-spec | entity | draft | assumed |
| [[Serving Runtime]] | ent-serving-runtime | entity | draft | validated |
| [[Accelerator Class]] | ent-accelerator-class | entity | draft | measured |
| [[Capacity Pool]] | ent-capacity-pool | entity | draft | assumed |
| [[GPU Fleet]] | ent-gpu-fleet | entity | draft | validated |
| [[GPU Node]] | ent-gpu-node | entity | draft | assumed |
| [[GPU Cluster]] | ent-gpu-cluster | entity | draft | assumed |
| [[Region]] | ent-region | entity | draft | assumed |
| [[Topology]] | ent-topology | entity | draft | assumed |
| [[Benchmark Run]] | ent-benchmark-run | entity | draft | assumed |
| [[Traffic Class]] | ent-traffic-class | entity | draft | assumed |

## Platform & Tenancy Entities

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[Organization]] | ent-organization | entity | draft | measured |
| [[RackAI Control Plane]] | ent-rackai-control-plane | entity | draft | measured |
| [[Environment]] | ent-environment | entity | draft | measured |
| [[API Key]] | ent-api-key | entity | draft | assumed |
| [[Registry Credential]] | ent-registry-credential | entity | draft | measured |

## Fine-Tuning Entities

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[Dataset]] | ent-dataset | entity | draft | measured |
| [[Fine-Tuning Job]] | ent-fine-tuning-job | entity | draft | measured |
| [[LoRA Adapter]] | ent-lora-adapter | entity | draft | measured |

## OpenRouter Initiative Entities

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[OpenRouter Provider Integration]] | ent-openrouter-integration | entity | draft | assumed |
| [[OpenRouter Private Model Integration]] | ent-openrouter-private-model | entity | draft | derived |
| [[Model Catalog Endpoint]] | ent-model-catalog-endpoint | entity | draft | assumed |
| [[Billing & Payment]] | ent-billing-payment | entity | draft | assumed |

## Priority Model Instances

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[DeepSeek V4 Flash]] | ent-deepseek-v4-flash | entity | draft | assumed |
| [[GLM 5.3 Flash]] | ent-glm-5-3-flash | entity | draft | assumed |
| [[Nemotron 3 Ultra]] | ent-nemotron-3-ultra | entity | draft | assumed |

## GPU Types (fleet ground truth)

See the [[Fleet Inventory]] for counts per environment.

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[NVIDIA H100]] | ent-gpu-h100 | entity | draft | measured |
| [[NVIDIA A30]] | ent-gpu-a30 | entity | draft | measured |
| [[NVIDIA L40S]] | ent-gpu-l40s | entity | draft | measured |
| [[AMD Instinct]] | ent-gpu-amd-instinct | entity | draft | assumed |

## See Also

- [[Wiki Hub]]
- [[Entity Ontology Hub]]
- [[Serving Platform MOC]]
