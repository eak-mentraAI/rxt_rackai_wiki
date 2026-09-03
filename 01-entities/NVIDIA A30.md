---
id: ent-gpu-a30
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [a30, nvidia a30, ampere a30]
related: [ent-gpu-node, ent-gpu-fleet, ent-serving-runtime, idx-fleet-inventory, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: measured
last_reviewed: 2026-09-03
parent: hub-entities
summary: "GPU type: NVIDIA A30 (Ampere) — high-count lower-power inference GPU in SPOT and dev."
---

# NVIDIA A30

## Definition

The **NVIDIA A30** (Ampere architecture) is a mainstream, low-power inference GPU present in large numbers in Rack AI's fleet: 40 in the SPOT environment plus some in RackAI dev (count TBD) per the [[Fleet Inventory]]. Its modest 24 GB memory and lack of FP8 support make it best suited to smaller models, quantized workloads, or as MIG-partitioned capacity rather than to large MoE priority models on their own.

## Layer

L1 — Entity Ontology. A GPU type realized by [[GPU Node]]s within the [[GPU Fleet]].

## Attributes

| Attribute | Value | Confidence |
|-----------|-------|:----------:|
| Architecture | Ampere | measured |
| GPU memory | 24 GB HBM2 | measured |
| Memory bandwidth | ~933 GB/s | measured |
| Power envelope | ~165 W (low-power) | measured |
| Precision support | FP64…TF32, FP16, INT8, INT4 (no FP8) | measured |
| Partitioning | Up to 4 MIG instances per GPU | measured |
| Interconnect | PCIe Gen4; third-gen NVLink (~200 GB/s) | measured |
| Fleet presence | SPOT ×40, RackAI dev ×TBD | measured |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| REALIZED_BY | [[GPU Node]] | ← | Nodes of A30 type |
| PART_OF | [[GPU Fleet]] | → | High-count capacity |
| SUPPORTS | [[Serving Runtime]] | → | vLLM/SGLang/TensorRT-LLM run; no FP8 path |
| INVENTORIED_IN | [[Fleet Inventory]] | → | SPOT + dev |

## Suitability Note

The A30's 24 GB memory and no-FP8 constraint mean the large MoE priority models ([[DeepSeek V4 Flash]], [[Nemotron 3 Ultra]]) are unlikely to fit or perform competitively on A30 alone. A30 is more relevant for smaller models, heavily quantized (INT8/INT4) serving, MIG-partitioned multi-tenant capacity, or dev/experimentation. This is a hardware-fit consideration, not yet a measured result — see [[Open Questions]].

## Evidence

- Fleet presence: operator-reported inventory 2026-09-03 (see [[Fleet Inventory]]).
- Specs: [NVIDIA A30 product page / datasheet](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) (24 GB HBM2, 933 GB/s, ~165 W, MIG, third-gen NVLink). Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Fleet Inventory]]
- [[GPU Type Compatibility Matrix]]
- [[Entity Ontology Hub]]
