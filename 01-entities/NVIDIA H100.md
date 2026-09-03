---
id: ent-gpu-h100
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [h100, nvidia h100, h100 sxm, hopper]
related: [ent-gpu-node, ent-gpu-fleet, ent-serving-runtime, idx-fleet-inventory, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: measured
last_reviewed: 2026-09-03
parent: hub-entities
summary: "GPU type: NVIDIA H100 (Hopper) — the flagship GPU of Rack AI's current fleet."
---

# NVIDIA H100

## Definition

The **NVIDIA H100 NVL (PCIe)** is the flagship GPU type in Rack AI's current fleet and the primary hardware target for the priority models until AMD Instinct capacity arrives. It is present in the SPOT environment (20 GPUs, of which **16 are usable** — 4 are contracted to a single customer) and RackAI staging (4 GPUs) per the [[Fleet Inventory]]. Critically, these are the **NVL PCIe** variant: NVLink bridges GPUs only in pairs (2 interconnected, 4 per node, no intra-host clustering), so it cannot assemble the large tightly-coupled GPU group that big models need. That topology — not the count — is the fleet's binding competitive constraint (see [[Fleet Competitiveness]]).

## Layer

L1 — Entity Ontology. A GPU type realized by [[GPU Node]]s within the [[GPU Fleet]].

## Attributes

| Attribute | Value | Confidence |
|-----------|-------|:----------:|
| Architecture | Hopper | measured |
| GPU memory | 80 GB HBM3 (SXM) | measured |
| Memory bandwidth | ~3.35 TB/s (SXM) | measured |
| Precision support | BF16, FP16, FP8 (Transformer Engine), INT8 | measured |
| Interconnect | NVLink / NVSwitch (multi-GPU), PCIe Gen5 | measured |
| Fleet presence | SPOT ×20, RackAI staging ×4 | measured |

> Memory/bandwidth figures are NVIDIA H100 SXM published specs; the exact H100 form factor per node (SXM vs PCIe) is TBD in the [[Fleet Inventory]].

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| REALIZED_BY | [[GPU Node]] | ← | Nodes of H100 type |
| PART_OF | [[GPU Fleet]] | → | Current fleet flagship |
| SUPPORTS | [[Serving Runtime]] | → | vLLM, SGLang, TensorRT-LLM, Dynamo all run on H100 |
| INVENTORIED_IN | [[Fleet Inventory]] | → | SPOT + staging |

## Evidence

- Fleet presence: operator-reported inventory 2026-09-03 (see [[Fleet Inventory]]).
- Specs: NVIDIA H100 published specifications. Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Fleet Inventory]]
- [[GPU Type Compatibility Matrix]]
- [[Entity Ontology Hub]]
