---
id: ent-gpu-l40s
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [l40s, nvidia l40s, ada lovelace l40s, i40, i40s]
related: [ent-gpu-node, ent-gpu-fleet, ent-serving-runtime, idx-fleet-inventory, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: measured
last_reviewed: 2026-09-03
parent: hub-entities
summary: "GPU type: NVIDIA L40S (Ada Lovelace) — FP8-capable GDDR6 inference GPU in RackAI staging."
---

# NVIDIA L40S

## Definition

The **NVIDIA L40S** (Ada Lovelace architecture) is an FP8-capable inference GPU present in RackAI staging (6 GPUs) per the [[Fleet Inventory]]. It has 48 GB of GDDR6 (larger capacity than the A30, but lower bandwidth than HBM parts) and 4th-generation Tensor Cores with a Transformer Engine that supports FP8. It has **no NVLink**, so multi-GPU serving falls back to PCIe — a constraint for tensor/expert parallelism on large MoE models.

> Recorded here as the canonical identity for the "i40's" in staging (aliased). Confirm the exact part (L40S vs L40) against hardware records.

## Layer

L1 — Entity Ontology. A GPU type realized by [[GPU Node]]s within the [[GPU Fleet]].

## Attributes

| Attribute | Value | Confidence |
|-----------|-------|:----------:|
| Architecture | Ada Lovelace | measured |
| GPU memory | 48 GB GDDR6 (ECC) | measured |
| Memory bandwidth | ~864 GB/s | measured |
| Power envelope | ~350 W | measured |
| Precision support | FP16, FP8 (4th-gen Tensor Cores / Transformer Engine), INT8 | measured |
| Interconnect | PCIe Gen4; **no NVLink** | measured |
| Fleet presence | RackAI staging ×6 | measured |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| REALIZED_BY | [[GPU Node]] | ← | Nodes of L40S type |
| PART_OF | [[GPU Fleet]] | → | Staging capacity |
| SUPPORTS | [[Serving Runtime]] | → | vLLM/SGLang/TensorRT-LLM; FP8 via Transformer Engine |
| INVENTORIED_IN | [[Fleet Inventory]] | → | RackAI staging |

## Suitability Note

FP8 support makes the L40S useful for FP8-quantized serving and staging/canary validation, but the lack of NVLink and GDDR6 (vs HBM) bandwidth limits its competitiveness for large multi-GPU MoE serving. Best used for staging, canary, smaller models, or FP8 single-GPU workloads. Hardware-fit is unmeasured — see [[Open Questions]].

## Evidence

- Fleet presence: operator-reported inventory 2026-09-03 (see [[Fleet Inventory]]).
- Specs: NVIDIA L40S published specs (48 GB GDDR6, ~864 GB/s, 350 W, 4th-gen Tensor Cores with FP8, PCIe, no NVLink). Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Fleet Inventory]]
- [[GPU Type Compatibility Matrix]]
- [[Entity Ontology Hub]]
