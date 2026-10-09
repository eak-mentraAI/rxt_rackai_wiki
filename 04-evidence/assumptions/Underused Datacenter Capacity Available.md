---
id: asm-dc-capacity-available
type: assumption
status: draft
owner: infrastructure
domain: capacity
aliases: [underused datacenter capacity, underutilized dc space, underused dc space, available datacenter space, spare dc capacity, powered space available]
related: [hub-why-now, idx-fleet-inventory, ent-gpu-amd-instinct, ent-region, hub-minimum-operable-estate, wiki-roadmap-narratives, idx-gpu-capacity-demand-rationale, idx-assumption-register]
source_docs: ["product owner statement (2026-10-09)"]
confidence: assumed
last_reviewed: 2026-10-09
parent: hub-evidence
summary: "Belief that Rackspace has underused, powered DC space that can host more AI capacity sooner than buyers can find it."
---

# Underused Datacenter Capacity Available

## Statement

> Rackspace has underused datacenter space, with power and cooling available, that can host additional AI capacity (more MI350P, or a customer's operated estate) sooner than a buyer could source equivalent powered capacity elsewhere.

Stated by the product owner on 2026-10-09 as one leg of the [[Why Now]] argument. **No figure exists in the corpus**: no site list, no available megawatts, no lead times. Until those are recorded, this is a belief, and the deck and any external material may only say that we *believe* we have capacity to bring online, not how much.

## Why It Matters

The [[Why Now]] argument rests on a scarcity: in the external evidence, AI compute is constrained more by powered datacenter space than by chips. If Rackspace already holds powered, underused space, that is an asset a new entrant can't buy quickly. It also bears on two gates:

- **MOE-1:** where the first operated estate physically runs, if the customer's boundary is a Rackspace facility.
- **MOE-3:** which jurisdictions we can offer residency in depends on where the space is ([[Region]]).

## What This Is Not

- **Not the Houston facility.** The Houston GB300 buildout in intake material is a partner-owned facility (DataJourney) with a committed anchor tenant. It is evidence that Rackspace operates inside other people's computer rooms, not evidence of Rackspace-owned spare space.
- **Not GPU idle capacity.** The SPOT environment resells otherwise-idle *GPUs* ([[Fleet Inventory]]). This assumption is about *space and power*.

## Exit Criterion

Validated when infrastructure records, per site: location and jurisdiction; available IT power (MW) and the basis (IT vs total facility load); cooling type (air vs liquid; what rack densities it supports); time to energize; and what is already committed. That fills the datacenter/geography and power-envelope attributes [[Fleet Inventory]] Milestone 0.1 already lists as TBD.

Weakened or falsified if the space needs material capital or more than a few quarters to bring online for AI densities, or if it sits in jurisdictions no target buyer needs.

## Impacts

| Note | What changes if validated / falsified |
|------|---------------------------------------|
| [[Why Now]] | The "we can meet the moment" leg becomes measured, or drops to MI350P alone |
| [[Fleet Inventory]] | Site and power attributes populated |
| [[GPU Capacity Demand Rationale]] | Expansion beyond the current fleet becomes a placement question, not a facilities one |
| [[Roadmap Narratives]] | MOE-3 jurisdictions get a concrete starting set |

## Status

`assumed`. Owner: infrastructure. Raised 2026-10-09; no evidence yet.

## See Also

- [[Why Now]]
- [[Fleet Inventory]]
- [[Assumption Register]]
