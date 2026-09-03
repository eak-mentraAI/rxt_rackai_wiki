---
id: idx-capacity-pools
type: index
status: draft
owner: finops
domain: capacity
aliases: [capacity pool model, pool taxonomy, pool classes, capacity allocation model]
related: [hub-commercial, ent-capacity-pool, wf-demand-forecasting, idx-fleet-yield]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-commercial
summary: "L3 index of the capacity pool taxonomy and software-controlled allocation; links to the canonical Capacity Pool entity."
---

# Capacity Pool Model

## Purpose

This index describes the pool taxonomy Rack AI uses to allocate GPU capacity and how allocation is controlled in software. The canonical definition of the entity lives in Layer 1 at [[Capacity Pool]] — this note references it and does not redefine it (One Concept Rule / Layer Purity: L3 references L1, never redefines it).

Capacity allocation is software-controlled (roadmap Milestone 5.1): pools are logical groupings mapped onto the GPU fleet, and a [[Model Deployment]] draws its capacity from exactly one pool rather than from individual GPUs. Commercial and capacity objects reference [[Model]]s and pools, never individual GPU nodes.

## Pool Taxonomy

- Per-model pools — dedicated capacity for a priority [[Model]]: DeepSeek, GLM, Nemotron.
- Launch / canary — capacity that isolates new launches and canary traffic.
- Reserve — held-back capacity for burst and failover, not routinely allocated.
- Warm — pre-warmed capacity for fast scale-up, reducing cold-start latency.
- Unallocated / spot — idle or spot-eligible capacity, reclaimable at lowest priority.

Pools expand and contract under software control as demand shifts, which is what makes dynamic reallocation between models possible without rebuilding infrastructure.

## Entries

| Item | ID | Type | Confidence |
|------|----|------|:----------:|
| [[Capacity Pool]] | ent-capacity-pool | entity | validated |
| Per-model pool (DeepSeek / GLM / Nemotron) | ent-capacity-pool | pool class | validated |
| Launch / canary pool | ent-capacity-pool | pool class | validated |
| Reserve pool | ent-capacity-pool | pool class | validated |
| Warm pool | ent-capacity-pool | pool class | validated |
| Unallocated / spot pool | ent-capacity-pool | pool class | validated |

## See Also

- [[Capacity Pool]]
- [[Commercial & Capacity Hub]]
