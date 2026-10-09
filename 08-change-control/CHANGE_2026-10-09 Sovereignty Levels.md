---
id: chg-2026-10-09-sovereignty-levels
type: change
status: draft
owner: product
domain: governance
aliases: [sovereignty levels change, sovereignty levels 2026-10-09]
related: [pol-sovereignty-levels, evd-gpu-co-tenancy-risk, hub-battlegrounds, wiki-roadmap-narratives, hub-minimum-operable-estate, wiki-eac-marketing-site-projection, hub-evidence]
source_docs: ["product owner direction (2026-10-09)", "web research 2026-10-09"]
confidence: derived
last_reviewed: 2026-10-09
parent: hub-wiki
summary: "Defined four sovereignty levels and their data fit; RackAI runs on RXT-owned gear, customer hardware only at MOE-4."
---

# 2026-10-09 — Sovereignty Levels

## Trigger

Product owner correction and direction. Rackspace does not run RackAI on customer hardware today: the customer buys from us, we own the gear and operate it for them. What makes it sovereign is that, unlike token endpoints and APIs, GPUs can be dedicated, with no time slicing or MIG; time-sliced endpoints are sold too. Running on the customer's own hardware is an end-state objective at MOE-4, once the platform is strong on ours. Sovereignty comes in levels: Level 0 is sovereign (tenant isolation, auditability, private endpoints), and what matters is which level fits which data, so customers know which consumption model is for them and we know what to sell. Security and legal will validate later; until then everything is `assumed`. Selling ahead of delivery is allowed, with sales timing commitments to roadmap dates.

## Objects Changed

- **Added:** [[Sovereignty Levels]] (`pol-sovereignty-levels`, policy, `assumed`, parent [[Three Battlegrounds]]). Four levels (0 Shared, 1 Dedicated, 2 Dedicated in a jurisdiction, 3 Your own hardware), a data-fit matrix, three qualifying questions, the selling-ahead-of-delivery rule, the gate each level is unlocked by, and open questions.
- **Added:** [[GPU Co-Tenancy Risk]] (`evd-gpu-co-tenancy-risk`, evidence, `derived`). Sourced isolation properties of each GPU sharing mode, demonstrated leakage in silicon and in the serving stack, mitigations and their limits, and regulatory guidance.
- **Changed:** [[Three Battlegrounds]]. "What private means" no longer says private need not be physically dedicated, nor lists customer infrastructure as a present option; it points to the levels. The supply line is sequenced (RXT-owned today, customer-owned at MOE-4, partner and hyperscaler an open question). The sovereign-provider row adds "at the level its data needs".
- **Changed:** [[Roadmap Narratives]] and [[Minimum Operable Estate]]: MOE-4 is labelled the end state, reached once the platform is proven on RXT-owned hardware; Narratives maps each gate to the level it unlocks.
- **Changed:** [[Enterprise AI Cloud Marketing Site Projection]]: a correction where it calls RackAI in a "customer environment" shipped and sellable today. Its infrastructure lines (colocation, customer-owned GPU infrastructure) describe Rackspace infrastructure offers, not RackAI, and are unchanged.
- **Changed:** [[Evidence Hub]]: link and `related`.

## What the Evidence Changed

The research found that most demonstrated cross-tenant breaches are in software (container escapes, misconfiguration, caches shared between tenants), not in GPU silicon. So Level 0's sovereignty depends on serving-layer controls, and the roadmap's shared KV cache work (RACKAI-311, in progress) must be scoped per tenant. Both are open questions in [[Sovereignty Levels]], not claims about current configuration.

## Edges

- **Added:** pol-sovereignty-levels → hub-battlegrounds (parent), evd-gpu-co-tenancy-risk, wiki-roadmap-narratives, hub-minimum-operable-estate; reverse links from Three Battlegrounds, Roadmap Narratives, Minimum Operable Estate, the marketing projection and Evidence Hub.
- **Removed:** none.

## Confidence Changes

None upgraded. The levels and fit calls are `assumed` pending security and legal review.

## Open Questions

Listed in [[Sovereignty Levels]]: security and legal validation; serving-layer controls for Level 0; per-tenant scope of the shared KV cache; whether Level 1 needs a dedicated node or cluster; partner-facility eligibility; whether Level 0 carries a claim for our current region.
