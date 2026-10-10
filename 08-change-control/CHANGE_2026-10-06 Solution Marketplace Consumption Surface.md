---
id: chg-2026-10-06-solution-marketplace
type: change
status: draft
owner: product
domain: strategy
aliases: [solution marketplace change, marketplace consumption surface change, packaged solution change]
related: [ent-solution-marketplace, ent-packaged-solution, ev-sovereign-private-assistant, hub-roadmap, wiki-milestone-release-map, hub-eac-product-model, idx-eight-layer-stack, hub-ai-operations-product, hub-openrouter, hub-entities]
source_docs: ["PM/leadership marketplace discussion 2026-10-06", "00-hub/Enterprise AI Cloud Product Model.md", "05-wiki/Eight-Layer Stack.md", "00-hub/Three Battlegrounds.md"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Modeled the Solution Marketplace: a RackAI-governed Consumption channel for FDE-authored Packaged Solutions."
---

# 2026-10-06 — Solution Marketplace (Consumption Driver via FDE-Authored Solutions)

## Trigger

PM/leadership discussion: should driving consumption via a **marketplace of agents/apps/harnesses** — authored by FDEs, distributed to RackAI customers — be a dedicated track or part of an existing one, and where is the boundary between the RackAI product org (marketplace + governance + SDK) and the FDEs (who author the solutions)? Example given: a RackAI-aware private ChatGPT over a customer's own corpus and sovereign models, answering alpha-leakage concerns.

**Decision reflected:** it is **not a sixth track** — it is a **cross-cutting Consumption-layer surface** (the second channel after OpenRouter) that pulls demand through the five existing tracks. Modeled as proposed strategy (`assumed`), not shipped capability.

## Objects Changed

- **Added — canonical entities:**
  - `01-entities/Solution Marketplace.md` (`ent-solution-marketplace`, `assumed`) — the Consumption-layer distribution surface. Core content: the two-sided boundary (RackAI builds rails = marketplace + Solution SDK + certification + isolation; FDE/partners/customers author solutions), second-channel framing alongside OpenRouter, why it is not a "RackAI platform product" (consumes RackAI; resolves into Outcome as a Service), and why it strengthens strategy (feeds the Empirical Map, bends workloads/FTE, makes sovereignty distributable).
  - `01-entities/Packaged Solution.md` (`ent-packaged-solution`, `assumed`) — the distributable unit = harness + skills/tools + target (incl. sovereign) models + corpus/storage binding. Explicitly contains **exactly one** [[Governed Harness]] (One-Concept preserved — does not redefine it); business logic is author-owned, harness is RackAI machinery.
- **Added — evidence/worked example:**
  - `04-evidence/Sovereign Private Assistant.md` (`ev-sovereign-private-assistant`, `assumed`) — the canonical worked example of a Packaged Solution; ties private Rackspace object/file storage + customer sovereign models + harness + a ChatGPT-like interface to the alpha-leakage concern.
- **Changed — [[RackAI Roadmap]]:** new *Cross-Cutting Surfaces → Solution Marketplace* subsection (table of SDK/gate/surface/reference-solution/third-party stages); Proof-4 *Consumption at scale* line under Multi-estate Operations; the **marketplace-rails-vs-FDE-authoring boundary decision (2026-10-06)**; intro line now names "two external consumption channels"; See Also + frontmatter `related` extended.
- **Changed — [[Milestone Release Map]]:** new *Cross-Cutting Consumption Surfaces* section (OpenRouter + Solution Marketplace as the two channels) with marketplace capability stages **MK.S1–MK.S5**; See Also.
- **Changed — link wiring (bidirectional):** [[Eight-Layer Stack]] (Consumption-layer row + See Also), [[Enterprise AI Cloud Product Model]] (See Also — resolves into Outcome as a Service), [[AI Operations Product]] (See Also — FDE output becomes distributable), [[OpenRouter Initiative]] (See Also — sibling second channel), [[Entity Ontology Hub]] (new *Consumption / Distribution Entities* section), [[Source-to-Concept Crosswalk]] (new source row).
- **Deprecated:** none.

## Edges

- **Added:** Solution Marketplace ↔ Packaged Solution (PUBLISHES/GOVERNS ↔ BELONGS_TO); Packaged Solution → Governed Harness (USES), → Model/Model Deployment (CONSUMES), → Dataset (corpus binding), → Empirical Map (MEASURED_BY), → Agent Identity (USES); Solution Marketplace → Empirical Map (PRODUCES, telemetry), → AI Governance and Assurance (GOVERNED_BY); Sovereign Private Assistant → Packaged Solution / Governed Harness / Three Battlegrounds. Hub/See-Also edges from the six notes above. All verified to resolve (0 missing).
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| ent-solution-marketplace | — | assumed | Proposed strategy direction; no SDK/gate/surface exists. |
| ent-packaged-solution | — | assumed | Packaging standard + artifact do not exist. |
| ev-sovereign-private-assistant | — | assumed | Illustrative design, not benchmarked or shipped. |
| hub-roadmap, wiki-milestone-release-map | derived | derived | Added a proposed cross-cutting surface + a boundary decision; no capability upgraded to shipped (all marketplace items marked ⚠ proposed / 🔴). |

No performance numbers introduced. Cost-per-outcome on a Packaged Solution is explicitly `measured`-only-from-a-real-instantiation; nothing asserted now.

## Open Questions Created

| Question | Affected Docs |
|----------|---------------|
| Commercial model: author rev-share (FDE/partner/customer) vs. bundled into Outcome as a Service? | [[Solution Marketplace]], [[Enterprise AI Cloud Product Model]], [[Commercial & Capacity Hub]] |
| Trust/certification bar for a third-party-authored solution to run inside a sovereign tenant? | [[Solution Marketplace]], [[AI Governance and Assurance]], [[Multi-Cluster Governance Brief (Partner)]] |
| Does the Solution SDK extend the existing P2 product surface (API/SDK/console), or is it a separate authoring kit? | [[Solution Marketplace]], [[RackAI Organizational Design]] |
| Is the corpus binding a thin pointer to [[Dataset]] + Object Store, or its own packaging primitive? | [[Packaged Solution]], [[RackAI Roadmap]] (CODB Object Store) |
| Sequencing: how early can the SDK + first FDE reference solution start as a proving ground vs. full marketplace at Proof 4? | [[RackAI Roadmap]] |

## Downstream Propagation Check

- **Dependent notes updated?** Yes — the Consumption-layer homes (Eight-Layer Stack, Product Model, OpenRouter Initiative), the FDE-motion home (AI Operations Product), the roadmap + release map, the entity hub, and the crosswalk all now reference the new concepts. No existing canonical *definition* was altered (Governed Harness, Model, Dataset, Empirical Map unchanged — the new entities link to them, don't redefine them).
- **Canonical IDs/aliases preserved?** Yes — all new IDs are fresh (`ent-solution-marketplace`, `ent-packaged-solution`, `ev-sovereign-private-assistant`); no existing ID/alias changed.
- **Formulas/metrics/coefficients/scorecards affected?** None directly. The marketplace references **workloads-per-ops-FTE** (north-star, [[AI Operations Product]]) and [[Cost per Outcome]] as *consumers* of those metrics, not redefinitions.
- **Source-to-Concept Crosswalk?** Updated — new row for the 2026-10-06 marketplace discussion → the three new notes.
- **One-Concept Rule?** Held — Packaged Solution contains, but does not redefine, [[Governed Harness]]; marketplace is a channel, not a new platform layer.
- **Layer purity?** Held — entities at L1 (Consumption), worked example at L4, projections (roadmap/release map) link down; the RackAI-vs-portfolio ownership convention from [[Enterprise AI Cloud Product Model]] is explicitly honored so "RackAI" does not leak upward.

## Fitness / Consistency Result

- Structural: **Pass** — all wikilinks in the three new notes verified to resolve (script sweep, 0 missing); new entities registered in [[Entity Ontology Hub]].
- Consistency: **Pass** — boundary convention stated identically across Solution Marketplace, roadmap, and release map; mirrors the [[Three Battlegrounds]] harness boundary and [[Pillar Working Model]] producer/consumer discipline without contradiction; second-channel framing consistent with [[OpenRouter Initiative]].
- Confidence propagation: **Pass** — all new objects `assumed`; nothing downstream upgraded; no numbers asserted.
- Regressions: none.

## See Also

- [[Solution Marketplace]] · [[Packaged Solution]] · [[Sovereign Private Assistant]]
- [[RackAI Roadmap]] · [[Milestone Release Map]]
- [[Wiki Hub]] · [[CHANGE_PACKET]]
