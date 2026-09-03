---
id: idx-fleet-inventory
type: index
status: draft
owner: infrastructure
domain: infrastructure
aliases: [fleet inventory, gpu inventory, ground truth inventory, phase 0 inventory]
related: [hub-evidence, ent-gpu-fleet, ent-gpu-node, ent-gpu-cluster, idx-open-questions]
source_docs: [openrouter_engineering_roadmap.md]
confidence: measured
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Phase-0 ground-truth GPU fleet inventory across the SPOT, RackAI staging, and RackAI dev environments."
---

# Fleet Inventory

## Purpose

The machine-readable ground-truth inventory of the GPU fleet that the roadmap's **Phase 0 — Establish Ground Truth** (Milestone 0.1) requires before any model-placement decision. It records what hardware Rack AI actually has, in which environment, and what is on order. It backs the [[GPU Fleet]] entity and the environment [[GPU Cluster]]s. Machine-readable companion: `fleet-inventory.csv` (same folder).

> **Confidence:** `measured` — this reflects an operator-reported fleet snapshot as of 2026-09-03, not a projection. Some per-node host/power attributes (roadmap Milestone 0.1) and the AMD order details remain TBD and are tracked in [[Open Questions]].

## Environments

Each environment maps to a canonical [[GPU Cluster]]. Production-eligible capacity lives in **SPOT** (OpenStack Flex); **RackAI staging** and **RackAI dev** are pre-production.

| Environment | Cluster role | GPUs | Production-eligible |
|-------------|--------------|------|:-------------------:|
| SPOT (OpenStack Flex) | Distribution channel for otherwise-idle capacity | 20× H100 (**16 usable**, 4 contracted to a single customer), 40× A30 | Yes (spot) |
| RackAI — staging | Pre-production validation / canary | 4× H100, 6× L40S | Canary only |
| RackAI — dev | Development / experimentation | some A30 (count TBD) | No |

**Usable production H100 count is 16**, not 20 — four are contracted to a single customer and unavailable to the inference pool.

## Interconnect Topology (the binding constraint)

The SPOT H100s are the **NVL PCIe** variant, not SXM. This is the single most important fact about the fleet's competitive position:

- NVLink bridges GPUs **in pairs** → **2 GPUs NVLink-interconnected**, **4 GPUs per node**, and **no intra-host clustering** beyond that.
- There is no NVSwitch fabric tying 8 GPUs into one tightly-coupled domain (as an HGX/SXM node would).
- Consequence: a workload **cannot scale horizontally** across a large interconnected GPU group. This caps servable model size regardless of how many GPUs we own. See [[Fleet Competitiveness]] and [[GPUs per Replica]].

## GPU Type Summary

| GPU Type | Usable count | Environments | Interconnect | Canonical Note |
|----------|:------------:|--------------|--------------|----------------|
| NVIDIA H100 NVL (PCIe) | 16 usable (+4 contracted) SPOT, 4 staging | SPOT, staging | NVLink pairs, 4/node, no clustering | [[NVIDIA H100]] |
| NVIDIA A30 | 40 SPOT, dev TBD | SPOT, dev | PCIe / NVLink | [[NVIDIA A30]] |
| NVIDIA L40S | 6 | staging | PCIe, no NVLink | [[NVIDIA L40S]] |
| AMD Instinct MI350P | on order | incoming ~Oct 2026 | 8-way pool (PCIe accelerator) | [[AMD Instinct]] |

**No H200s are in the fleet.** Earlier notes used H200 as an illustrative example; the fleet flagship is the **H100 NVL PCIe**. See the [[GPU Type Compatibility Matrix]] for serving-engine and precision support per type.

## Incoming Capacity

- **AMD Instinct MI350P** — a large order, ETA approximately **October 2026**. We can position an **8-way MI350P** inference pool, a real step up in capacity. But it is a **PCIe accelerator**, so it carries the *same* horizontal-scaling limitation as the H100 NVL: it will not scale a workload across a large interconnected group the way an SXM part (H200) or UBB8 platform (B300) does. It also introduces the ROCm serving path (vLLM/SGLang only) — see [[GPU Type Compatibility Matrix]].

## Path to Top-Tier

Top-10 OpenRouter placement and frontier-class model support are **not reachable on PCIe topology**. They require delivering **SXM clusters or UBB8** platforms that provide a large, tightly-coupled NVLink/fabric domain. Until then the realistic competitive band is smaller models (~27B class). See [[Fleet Competitiveness]].

## Milestone 0.1 Attributes (to complete)

The roadmap requires each node to record: GPU type/generation, count, memory, host CPU/RAM, NVLink/NVSwitch topology, network fabric, storage, datacenter/geography, power envelope, cluster ownership, committed vs available capacity, and maintenance state. This inventory currently captures type, count, and environment; the remaining per-node attributes are TBD and should be populated as Phase 0 telemetry (Milestone 0.2) comes online.

## See Also

- [[GPU Fleet]]
- [[GPU Type Compatibility Matrix]]
- [[Evidence Hub]]
