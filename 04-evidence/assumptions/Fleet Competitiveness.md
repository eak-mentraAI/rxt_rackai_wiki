---
id: asm-fleet-competitiveness
type: assumption
status: draft
owner: performance-eng
domain: capacity
aliases: [fleet competitiveness, interconnect constraint, pcie scaling wall, topology ceiling]
related: [hub-evidence, asm-h200-sufficient, fml-gpus-per-replica, idx-fleet-inventory, ent-gpu-amd-instinct, ent-topology, idx-model-portfolio, ent-openrouter-integration]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Binding constraint is interconnect topology (PCIe vs SXM/UBB8), not GPU count — caps model size near ~27B."
---

# Fleet Competitiveness

## Statement

Rack AI's competitive ceiling on OpenRouter is set by **interconnect topology, not GPU count**. The fleet's H100s are the **NVL PCIe** variant — NVLink bridges GPUs only in pairs (2 interconnected, 4 per node, no intra-host clustering). That means a workload **cannot scale horizontally** across a large, tightly-coupled GPU group, which caps the size of model we can serve competitively at roughly the **~27B class**. This is a genuine constraint the source strategy does not confront; it is surfaced here rather than smoothed over.

## The Real Constraint: Topology

Large models need many GPUs acting as one tightly-coupled unit (tensor/expert parallelism over a fast fabric). On PCIe pair-bridged GPUs that fast fabric doesn't exist beyond a pair, so cross-GPU parallelism spills onto slow links and collapses. More GPUs don't help — you can own many and still not assemble a big-enough coupled group.

| Platform | Coupling | Horizontal scale | Servable model band |
|----------|----------|------------------|---------------------|
| [[NVIDIA H100]] NVL PCIe (fleet) | NVLink pairs (2), 4/node, no clustering | Very limited | ~27B class |
| H200 SXM (competitor) | NVSwitch, 8-GPU coupled node | Strong | Frontier |
| B300 / UBB8 (competitor) | Full fabric domain | Strongest | Frontier+ |

Consequence: we are **not likely to be on the leaderboard for frontier-class models**, and cannot support them at all on current topology. Realistic play is smaller, high-demand models we can serve well within a pair/node.

## Quantity Is Secondary

Usable production capacity is **16× H100** in SPOT (4 of 20 are contracted to a single customer). Quantity limits how much concurrent traffic we can absorb and how many models we can run at once (see [[Model Portfolio Capacity]]), but it is **not** the binding limit — even with more of the same PCIe GPUs, the topology ceiling on model size does not move.

> **Note:** SPOT uptime is *not* treated as a material risk here — availability within SPOT is manageable. Earlier drafts overstated this; the claim has been removed.

## The Other Near-Term Risk: API Conformance

Independent of hardware, the **OpenRouter API/provider requirements** are likely to **down-rank us initially** until we fully meet the capability and conformance surface (streaming, tool calling, structured output, usage reporting, error handling, etc. — [[OpenRouter Provider Integration]]). This is a solvable engineering ramp, but it means early rank will lag real performance. Plan for it rather than being surprised.

## The AMD Step-Up — Real, But Still PCIe

The incoming **8-way [[AMD Instinct]] MI350P** pool (~Oct 2026) adds genuine capacity and lets us serve more concurrent demand. But MI350P is a **PCIe accelerator**, so it hits the **same horizontal-scaling wall** as the H100 NVL. It raises *how much* we can serve, not the ceiling on model size. It does not, by itself, put frontier models or top-10 in reach.

## Path to Top-Tier

Top-10 OpenRouter placement and frontier-class model support require **SXM clusters or UBB8** platforms that provide a large, tightly-coupled fabric domain. Until we deliver that, we will likely never be top-10 overall — and that is a hardware-topology conversation, not a "buy more PCIe GPUs" one.

## Rationale

The NVL-PCIe pair topology, the fabric requirements of large-model parallelism, and OpenRouter's performance-weighted routing together imply topology is the binding ceiling. This is an architectural/analytical expectation, not a measured competitive result.

## Exit Criterion

(a) A measured H100 benchmark of a fitting (~27B-class) model vs. the competitive frontier ([[Validate DeepSeek H100 FP8]] and equivalents); (b) confirmed MI350P specs + a measured benchmark; (c) a decision/plan on delivering SXM or UBB8 capacity. Until then this remains `assumed`.

## Impacts

| Impacted | Type |
|----------|------|
| [[Available Hardware Sufficient for Priority Models]] | SUPPORTS |
| [[Model Portfolio Capacity]] | CONSTRAINS |
| [[Topology]] | SUPPORTS |
| [[AMD Instinct]] | CONSTRAINS |
| [[GPUs per Replica]] | SUPPORTS |

## Status

- Confidence: assumed
- Owner: performance-eng / infrastructure
- Target resolution date: TBD (H100 benchmark now; MI350P after ~Oct 2026; SXM/UBB8 = strategic decision)

## See Also

- [[Evidence Hub]]
- [[Model Portfolio Capacity]]
- [[Topology]]
- [[Fleet Inventory]]
