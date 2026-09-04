---
id: hub-entities
type: hub
status: draft
owner: platform-eng
domain: platform
aliases: [entity hub, L1 hub, entities hub]
related: [hub-root, hub-operations]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Layer 1 navigation hub for canonical inference-platform entities."
---

# Entity Ontology Hub

Layer 1 — the semantic backbone. Canonical business and domain objects of the RackAI platform. Every other layer references entities defined here.

## Serving Chain Entities

| Entity | ID | Status |
|--------|----|--------|
| [[Model]] | ent-model | created |
| [[Model Class]] | ent-model-class | created |
| [[Model Deployment]] | ent-model-deployment | created |
| [[Model Deployment Specification]] | ent-model-deployment-spec | created |
| [[Serving Runtime]] | ent-serving-runtime | created |
| [[Accelerator Class]] | ent-accelerator-class | created |
| [[Capacity Pool]] | ent-capacity-pool | created |
| [[GPU Fleet]] | ent-gpu-fleet | created |
| [[GPU Node]] | ent-gpu-node | created |
| [[GPU Cluster]] | ent-gpu-cluster | created |
| [[Region]] | ent-region | created |
| [[Topology]] | ent-topology | created |
| [[Benchmark Run]] | ent-benchmark-run | created |
| [[Traffic Class]] | ent-traffic-class | created |

## Platform & Tenancy Entities

| Entity | ID | Status |
|--------|----|--------|
| [[Organization]] | ent-organization | created |
| [[RackAI Control Plane]] | ent-rackai-control-plane | created |
| [[Environment]] | ent-environment | created |
| [[API Key]] | ent-api-key | created |
| [[Registry Credential]] | ent-registry-credential | created |

## Fine-Tuning Entities

| Entity | ID | Status |
|--------|----|--------|
| [[Dataset]] | ent-dataset | created |
| [[Fine-Tuning Job]] | ent-fine-tuning-job | created |
| [[LoRA Adapter]] | ent-lora-adapter | created |

## OpenRouter Initiative Entities

| Entity | ID | Status |
|--------|----|--------|
| [[OpenRouter Provider Integration]] | ent-openrouter-integration | created |
| [[OpenRouter Private Model Integration]] | ent-openrouter-private-model | created |
| [[Model Catalog Endpoint]] | ent-model-catalog-endpoint | created |

## Priority Model Instances

| Model | ID | Role |
|-------|----|------|
| [[DeepSeek V4 Flash]] | ent-deepseek-v4-flash | Win now — benchmark |
| [[GLM 5.3 Flash]] | ent-glm-5-3-flash | Win now — growth |
| [[Nemotron 3 Ultra]] | ent-nemotron-3-ultra | Bet ahead |

## GPU Types (fleet ground truth)

| GPU Type | ID | Fleet presence |
|----------|----|----------------|
| [[NVIDIA H100]] | ent-gpu-h100 | SPOT ×20, staging ×4 — current flagship |
| [[NVIDIA A30]] | ent-gpu-a30 | SPOT ×40, dev ×TBD |
| [[NVIDIA L40S]] | ent-gpu-l40s | staging ×6 |
| [[AMD Instinct]] | ent-gpu-amd-instinct | incoming ~Oct 2026 (ROCm) |

Ground truth: [[Fleet Inventory]]. Engine/precision support: [[GPU Type Compatibility Matrix]]. **No H200s in the fleet.**

See the [[Entity Index]] for the full listing. Create new entities using `templates/entity.md`.

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[Operations Hub]]
