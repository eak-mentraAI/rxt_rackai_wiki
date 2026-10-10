---
id: pol-sovereignty-levels
type: policy
status: draft
owner: product
domain: governance
aliases: [sovereignty levels, levels of sovereignty, sovereignty ladder, sovereign tiers, data sensitivity fit, which consumption model, dedicated vs shared gpu, time-sliced vs dedicated, sovereign enough]
related: [hub-battlegrounds, hub-why-now, hub-minimum-operable-estate, wiki-roadmap-narratives, hub-eac-product-model, evd-gpu-co-tenancy-risk, ev-sovereign-private-assistant, hub-ai-governance-assurance, ent-organization]
source_docs: ["product owner direction (2026-10-09)", "00-hub/Three Battlegrounds.md", "05-wiki/Roadmap Narratives.md"]
confidence: assumed
last_reviewed: 2026-10-09
parent: hub-battlegrounds
summary: "Four levels of sovereignty and which data each fits, so customers pick a consumption model and we know what to sell."
---

# Sovereignty Levels

How the **sovereign provider** centre of [[Three Battlegrounds]] is offered. Every level is sovereign: the customer gets tenant isolation, private endpoints and an audit trail at all of them. What changes from level to level is the **residual risk** the customer accepts, and so **which data each level is right for**. Matching the two tells a customer which consumption model fits them, and tells us what to sell.

> **Confidence `assumed`.** Product owner direction, 2026-10-09. The levels, data classes and fit calls are pending validation with security and legal; until then they are guidance, not compliance advice. The co-tenancy risk behind Level 0 is sourced in [[GPU Co-Tenancy Risk]].

## The Four Levels

Rackspace owns the hardware and operates it at Levels 0–2. Running RackAI on the customer's own hardware (Level 3) is an end-state objective, reached only once the platform is proven on ours.

| Level | What the customer gets | Hardware | Residual risk the customer accepts | Unlocked by | Status today |
|---|---|---|---|---|---|
| **0 · Shared** | Tenant isolation, private endpoints, audit trail | RXT-owned; GPUs shared with other tenants (time-sliced or MIG) | Hardware co-tenancy: time-slicing gives no memory isolation; MIG leaks activity patterns; leftover-memory and side-channel classes apply ([[GPU Co-Tenancy Risk]]); noisy neighbours; shared blast radius | Today | Sold today (shared endpoints). Identity, RBAC and audit foundation shipped; extended audit in progress |
| **1 · Dedicated** | Level 0, plus GPUs that are the customer's alone: no time slicing, no MIG; evidence the boundary held | RXT-owned, dedicated to one customer | The provider's control plane and software stack; GPUs sharing a multi-GPU node can still leak to each other; only the regions we offer | MOE-1 | Dedication is operationally possible (e.g. Uniphore's dedicated environment); the proof is not built: customer isolation and the first assurance attestation are MOE-1 Musts, not started |
| **2 · Dedicated in a jurisdiction** | Level 1, plus data, models, logs and backups kept in a declared jurisdiction, with failover only inside it | RXT-owned, dedicated, in a declared region | The provider's control plane | MOE-3 (proposed) | Not started; single region today |
| **3 · Your own hardware** | RackAI operated inside the customer's own perimeter | Customer-owned | Whatever the customer's own estate carries | MOE-4 (proposed; end state) | Not started |

Time-sliced endpoints remain a deliberate Level 0 offer for customers whose data fits it. Selling Level 1 to a workload that fits Level 0 is over-selling.

## What the Evidence Says

From [[GPU Co-Tenancy Risk]]:

- **Most demonstrated cross-tenant breaches are in software, not silicon:** container escapes, platform misconfiguration and caches shared between tenants. These apply at **every** level, so Level 0 is only legitimately sovereign with serving-layer controls in place: no KV or prefix cache shared across tenants, a VM boundary where customers run code, and a patched container stack. Dedicated GPUs don't fix any of these.
- **Dedicated GPUs (Level 1) remove the silicon class:** leftover memory, side channels and Rowhammer between tenants. That is what makes them the right floor for proprietary alpha and regulated data.
- **Regulation is mostly risk-based,** not a dedicated-hardware mandate, outside defence (DoD IL5) and some sovereign-cloud regimes such as SecNumCloud. The ⚠️ cells below are judgement calls, not legal requirements.

## Which Level Fits Which Data

| Data the workload touches | 0 Shared | 1 Dedicated | 2 Jurisdiction | 3 Own hardware |
|---|:-:|:-:|:-:|:-:|
| Public or low-sensitivity (published documents, marketing) | ✅ | ✅ | ✅ | ✅ |
| Internal confidential (internal knowledge, code) | ✅ | ✅ | ✅ | ✅ |
| **Proprietary alpha** (trading signals, research, M&A, pricing strategy) | ⚠️ the customer's risk call | ✅ | ✅ | ✅ |
| Regulated personal or financial data | ⚠️ depends on the regulator or contract | ✅ with attestation | ✅ | ✅ |
| Data legally bound to a jurisdiction | ❌ beyond our current region | ⚠️ only if our region matches | ✅ | ✅ |
| Must stay inside the customer's perimeter | ❌ | ❌ | ❌ | ✅ |

✅ fits · ⚠️ fits only if the stated condition holds · ❌ doesn't fit. All cells `assumed` pending security and legal review. **Proprietary alpha** is the case the [[Sovereign Private Assistant]] describes: the value lies in no one else seeing it, even indirectly, which is why hardware co-tenancy matters for it.

## How Customers Choose, and What We Sell

Three questions place a workload:

1. **What data will the workload touch?** The most sensitive class sets the floor.
2. **Does a regulator or contract require residency?** If so, Level 2 or higher.
3. **Must it stay inside your own perimeter?** If so, Level 3.

The answer is a level, and the level is the consumption model: shared endpoints (0), dedicated (1), regional dedicated (2), or your own hardware (3). For sales the same questions are qualification: which level to lead with, and which level would be over-selling.

## Selling Ahead of Delivery

We sell into the vision and make it real before deployment. A level that isn't deliverable yet may be sold as a **dated commitment**, provided:

- the delivery date is no earlier than the roadmap date of the gate that unlocks the level ([[Roadmap Narratives]]); sales owns timing commitments to those dates;
- it is presented as a commitment, never as a production capability. A production claim still needs the gate to pass (the readiness labels in [[Roadmap Narratives]]).

## Relationship to the Roadmap

Each MOE gate unlocks the next level, so "which market opens" also reads as "which data we can take":

- **MOE-1** → Level 1: proprietary alpha and regulated data on dedicated hardware.
- **MOE-3** → Level 2: jurisdiction-bound data.
- **MOE-4** → Level 3: the customer's own perimeter.

## Open Questions

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Security and legal validation of the levels, data classes and fit calls | this note | High |
| Confirm the serving-layer controls Level 0 needs are in place: per-tenant KV / prefix cache, VM boundary where customers run code, patched NVIDIA Container Toolkit | [[GPU Co-Tenancy Risk]] | High |
| Scope the shared KV cache in *M2: Inference routing* (RACKAI-311, in progress) and *Shared KV cache (improvement)* as per-tenant; cross-tenant sharing leaks prompts | [[RackAI Roadmap]] | High |
| Does Level 1 require a dedicated cluster or node, or are dedicated GPUs in a shared cluster (namespace-per-organisation isolation) enough? | [[Organization]], [[Minimum Operable Estate]] | High |
| Is RXT-owned, dedicated capacity in a partner facility (e.g. Houston) eligible for Levels 1–2? | [[Why Now]] | Medium |
| Does Level 0 carry a jurisdiction claim for our current single region? | this note | Medium |

## See Also

- [[Three Battlegrounds]]: the sovereign provider centre these levels express
- [[GPU Co-Tenancy Risk]]: the evidence behind Level 0's residual risk
- [[Minimum Operable Estate]] · [[Roadmap Narratives]] · [[Why Now]]
