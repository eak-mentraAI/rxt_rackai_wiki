---
id: chg-2026-10-06-rackai-boundary-operating-platform
type: change
status: draft
owner: product
domain: strategy
aliases: [rackai operating platform boundary change, core and rails boundary, rackai boundary evolution 2026-10-06]
related: [hub-eac-product-model, hub-rackai-platform, hub-battlegrounds, hub-ai-operations-product, ent-solution-marketplace, ent-packaged-solution]
source_docs: ["PM/leadership marketplace discussion 2026-10-06", "00-hub/Enterprise AI Cloud Product Model.md", "01-entities/Solution Marketplace.md"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Evolved RackAI boundary to 'private AI operating platform = core + rails'; reconciled and propagated; FDE kept separate."
---

# 2026-10-06 — RackAI Boundary: Private AI Operating Platform (Core + Rails)

## Trigger

PM follow-up to the [[Solution Marketplace]] work: because RackAI now owns the **platform rails** through which higher-level solutions are packaged, governed, distributed, instantiated, and consumed, the earlier boundary — *"RackAI is the inference and fine-tuning platform"* — is **too narrow**. Direction given: evolve RackAI to the **private AI operating platform = core + rails**; *"RackAI owns the factory and the marketplace, not everything produced by the factory."* Keep **FDE separate** (RackAI creates leverage for FDE; FDE does not become RackAI). Sharpen the identity: RackAI is the operating *platform* that makes the operator model scalable; Managed Operations exercises responsibility *through* it; FDE/partners/customers build on it.

## Objects Changed

- **[[Enterprise AI Cloud Product Model]]** (the canonical home for the boundary) — primary edit:
  - Rewrote the **boundary convention**: RackAI = *private AI operating platform (core + rails)*; now named in **three** places (Inference & Orchestration = core, Fine-Tuning & Distillation, and **Platform Rails** = SDK/marketplace/packaging/certification/metering). Replaced the old "named in exactly two places" convention.
  - Added a **layered-ownership table** (infra → RackAI core → RackAI rails → solutions → Managed Operations → outcome).
  - Added the **"factory + marketplace, not everything produced"** framing and the explicit **FDE-leverage-not-identity** note.
  - Added a **two-senses reconciliation** callout (shipped = inference + fine-tuning; strategic = operating platform; rails `assumed`).
  - Updated the relationship-verb table (Experiences & Agents → "built on rails"; new **Platform rails = is RackAI** row; new **Solutions/outcomes = not RackAI** row), the one-sentence ownership picture, the harness note (runtime interface = rails; logic = not RackAI), the governing-principle line (added "build-on"), the RackAI-offer gloss, and **both** downstream tables (Capability→Offer Map and Traceability each gain a Platform Rails row).
  - Frontmatter: `summary`, `last_reviewed` → 2026-10-06, `source_docs` += marketplace discussion + Solution Marketplace.
- **[[RackAI Platform]]** (shipped-product hub) — added a **two-senses reconciliation** pointer; **left the shipped definition unchanged** (inference + fine-tuning is what exists today). No capability upgraded.
- **[[Three Battlegrounds]]** — "We own" row extended to include the **platform rails**; the harness-boundary callout extended: rails are owned by the *same* horizontal-machinery argument; added the sharpened identity line (operating platform makes the operator model scalable; Managed Ops exercises responsibility through it).
- **[[AI Operations Product]]** — added the **three-way fit** (Marketplace scales *what* is operated · AIOps defines *how* · Empirical Map makes RackAI *better* at it) and the "operator is a company claim exercised *through* the platform" clarification.
- **[[Solution Marketplace]]** — refined the "not a RackAI product" callout to **"the marketplace (rails) IS RackAI; the solutions on it are not."**
- **[[Packaged Solution]]** — refined the boundary note to **"built *on* RackAI, not *is* RackAI"** (harness runtime interface = rails; solution logic = author's).

## Edges

- **Added:** Product Model ↔ [[Solution Marketplace]] / [[Packaged Solution]] (layered-ownership + rails rows); RackAI Platform → Enterprise AI Cloud Product Model + Capability Gap Register (reconciliation); Three Battlegrounds → Solution Marketplace + AI Operations Product; AI Operations Product → Solution Marketplace + Empirical Map + Three Battlegrounds. All verified to resolve.
- **Removed:** the "named in exactly two places" convention (superseded; 0 occurrences remain).

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| hub-eac-product-model | validated | validated | The **ratified three-offer structure** is unchanged (still `validated`). The **boundary widening** is a 2026-10-06 proposal layered on top and labelled as such; the **rails** are explicitly `assumed`/not-built. No offer tier or capability upgraded. |
| hub-rackai-platform | (shipped) | (shipped) | Definition unchanged — only a reconciliation pointer added. |
| ent-solution-marketplace, ent-packaged-solution | assumed | assumed | Framing refinement; still proposed. |

No performance numbers introduced. The rails (SDK, marketplace, certification, metering) remain `assumed`/not-built per the [[Capability Gap Register]]; widening the *boundary* did not change any capability's *build status*.

## Open Questions

No new open questions beyond those already logged with the [[Solution Marketplace]] (commercial model / rev-share; sovereign-tenant certification bar; SDK vs existing P2 product surface). This change is a boundary/definition evolution, not a new build.

## Downstream Propagation Check

- **Dependent notes updated?** Yes — the boundary's canonical home (Product Model) plus the four strategic notes that assert or depend on the boundary (RackAI Platform, Three Battlegrounds, AI Operations Product, and the two marketplace entities).
- **Deliberately NOT changed:** the **shipped-reality / naming-canonical** statements in [[RackAI Platform]] body, the Glossary, the user guide (`reference/`), and the operating-standards steering file. Those describe *what is built today* (inference + fine-tuning) and the canonical product name — rewriting them to "operating platform" would overclaim unbuilt capability (confidence violation). The reconciliation callouts make the two senses coexist without contradiction.
- **Canonical IDs/aliases preserved?** Yes — no IDs changed; no new concept introduced (core/rails are a boundary framing over existing concepts).
- **Formulas/metrics/coefficients/scorecards affected?** None.
- **Source-to-Concept Crosswalk?** The 2026-10-06 marketplace discussion is already registered (prior packet); this is a boundary evolution of the same source, logged here. No new crosswalk row required.
- **One-Concept / Layer purity?** Held — the boundary lives in one canonical home (Product Model); other notes point to it. No duplicate definition.

## Fitness / Consistency Result

- Structural: **Pass** — all wikilinks in the six edited notes resolve (0 missing, escaped-pipe aliases accounted for).
- Consistency: **Pass** — "exactly two places" convention fully removed (0 occurrences); shipped vs strategic senses reconciled explicitly in three places (Product Model, RackAI Platform, and implicitly via Capability Gap Register references); FDE kept separate across all touchpoints; no capability upgraded.
- Confidence propagation: **Pass** — rails `assumed`; offer tiers still `validated`; shipped definition untouched.
- Regressions: none.

## See Also

- [[Enterprise AI Cloud Product Model]] — the canonical home for the evolved boundary
- [[Solution Marketplace]] · [[Packaged Solution]]
- [[RackAI Platform]] — shipped-product definition (reconciled)
- [[Three Battlegrounds]] · [[AI Operations Product]]
- [[Wiki Hub]] · [[CHANGE_PACKET]]
