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
summary: "Index of the canonical Layer-1 entities of the Rack AI inference platform plus priority model instances."
---

# Entity Index

## Purpose

Lists the canonical Layer-1 (L1) entities that form the semantic backbone of the Rack AI inference platform, plus the three priority model instances. Entities are defined once in their canonical notes; this index only points to those homes and records their graph status. Kept current as entity notes are created.

## Canonical Entities

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[Model]] | ent-model | entity | draft | assumed |
| [[Model Deployment]] | ent-model-deployment | entity | draft | assumed |
| [[Model Deployment Specification]] | ent-model-deployment-spec | entity | draft | assumed |
| [[Serving Runtime]] | ent-serving-runtime | entity | draft | assumed |
| [[GPU Node]] | ent-gpu-node | entity | draft | assumed |
| [[GPU Cluster]] | ent-gpu-cluster | entity | draft | assumed |
| [[Capacity Pool]] | ent-capacity-pool | entity | draft | assumed |
| [[GPU Fleet]] | ent-gpu-fleet | entity | draft | validated |
| [[Region]] | ent-region | entity | draft | assumed |
| [[Topology]] | ent-topology | entity | draft | assumed |
| [[OpenRouter Provider Integration]] | ent-openrouter-integration | entity | draft | assumed |
| [[Benchmark Run]] | ent-benchmark-run | entity | draft | assumed |
| [[Traffic Class]] | ent-traffic-class | entity | draft | assumed |

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
