---
id: chg-2026-10-06-roadmap-review-proof3-rename
type: change
status: draft
owner: product
domain: strategy
aliases: [proof 3 rename change, assume responsibility rename, release map stage rename, roadmap review 2026-10-06 part 2]
related: [hub-roadmap, wiki-milestone-release-map, hub-minimum-operable-estate, hub-model-services, hub-ai-governance-assurance, hub-ai-operations-product, hub-ai-harness, hub-inference-serving, hub-inference-optimization]
source_docs: ["PM/leadership roadmap review 2026-10-06", "00-hub/RackAI Roadmap.md", "05-wiki/Milestone Release Map.md", "05-wiki/RackaI Roadmap 10062026.csv"]
confidence: derived
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Roadmap review: renamed Proof 3 Control -> Assume Responsibility, added per-proof pass/fail tests, resolved the Proof-1/Proof-3 evidence circularity, adopted the placement principle, ruled GPU-node access out of scope, split technique from capability, and reworked the release CSV + map (Release -> Capability Stage)."
---

# 2026-10-06 — Roadmap Review: Proof-3 Rename, Proof Pass/Fail Tests, Release CSV + Map Rework

## Trigger

PM/leadership review of the [[Milestone Release Map]] + the `RackaI Roadmap 10062026.csv` projection. The review endorsed the structure (five functional tracks, proof-vs-backlog separation, exposed gaps) and requested a set of structural and framing changes. Twelve points were raised; all were incorporated. The authoritative changes land on the canonical [[RackAI Roadmap]]; the CSV and [[Milestone Release Map]] are projections updated to match.

## Objects Changed

### Canonical — [[RackAI Roadmap]] (`hub-roadmap`)
- **Proof 3 renamed `Control` → `Assume Responsibility`** (review pt 3). Control is reframed as *one capability that helps pass the proof*, not the proof itself. Updated: section header + exit block, executive-summary status table, commercial-gate table, operating-loop stage table, line-of-sight mermaid node, how-to-read bullet, one-liner, frontmatter `summary`, and a new alias `observe decide assume-responsibility operate` (old alias retained for discoverability).
- **Per-proof pass/fail tests added** (pts 3, 5, 11):
  - **Proof 1** — pass test = *representative workload evidence, NOT a paid enterprise customer*; names [[GLM 5.3 Flash]] + OpenRouter Path A as the evidence source. **Resolves the Proof-1/Proof-3 circularity** the review flagged.
  - **Proof 3** — pass test = MOE-1 passes its operational-acceptance gate (external, regulated, delegated, paid). MOE-1 framed as the **integration test for the whole strategy**; capabilities form the ladder *into* the gate (Capabilities → MOE-0 → MOE-1 → PASSED); the [[Minimum Operable Estate]] spec is the **acceptance definition**, not another capability (pt 4).
  - **Proof 4** — quantitative pass test = *onboard/operate more workloads without labor or cost scaling linearly*; acceptance measures: workloads/operator, time-to-onboard, change-failure rate, placement-automation rate, gross margin, capacity utilization, SLO attainment (pt 11).
- **Supply-abstraction placement principle adopted** (pt 9): *RackAI chooses by default; customers constrain when necessary.* Resolves the Workload Placement Policy open question's *direction* (intent+constraints in, RackAI picks hardware; explicit hardware = a constraint). Quota-model rework remains the open implementation item.
- **GPU-node access ruled Out of Scope** (pt 10): Proof-4 milestone row struck through + PM-note rewritten as a decision — direct GPU-node access is GPU IaaS, belongs to the GPUaaS/IaaS boundary.
- **Accelerator selection split** (pt 7): the shipped RACKAI-336 item renamed *Accelerator inventory & consumption telemetry* (telemetry prerequisite, `Complete`); a new `gap → P-005` row *Accelerator selection (evidence-informed)* carries the actual selection capability.
- Frontmatter `last_reviewed` → 2026-10-06; added "PM/leadership roadmap review 2026-10-06" to `source_docs`.

### Projection — `05-wiki/RackaI Roadmap 10062026.csv`
- Rebuilt (14 columns, 58 rows). **`Release` → `Capability Stage`** (`T#.S#`) so stages are not read as committed releases (pt 2). Added **`Type`** (Product capability / Technique — pt 6) and **`Disposition`** (Committed / Experiment / Decision Required / Gap / Backlog / Out of Scope / Done — pt 12); **`Status`** is now strictly execution (Not started / In progress / Done). Added **`Release date (post-eng meeting)`** seeded from `Due`.
- Techniques (7) tagged: speculative decoding, Refrag, shared-KV-cache improvement, DPO, semantic router, AMD AIM, checkpointing. GPU-node access + checkpointing = Out of Scope. Added customer-observability vs operator-intelligence as two rows (pt 8). Corpus items folded in (GLM/OpenRouter Path A, workload characterization, multi-model, domain-model experiment, unit economics, MOE spec, Proof-4 operator-business rows, etc.).

### Projection — [[Milestone Release Map]] (`wiki-milestone-release-map`)
- Terminology **Release → Capability Stage** (`T#.S#`); all 56 stage IDs + line-of-sight shorthand normalized; the only genuine *releases* are the MOE-0/MOE-1 gates. Proof-3 rename applied (incl. the deep-link anchor). Added a **Product-Boundary Decisions (2026-10-06)** section (placement principle, GPU-node-access out-of-scope, observability-is-two-products) + a technique-vs-capability note pointing at the CSV columns. T1.S2 theme rewritten to the placement principle; T1.S4 marks GPU-node access out of scope.

### Dependent notes (rename propagation — Semantic Drift Rule)
- Proof-name `Control` → `Assume Responsibility` propagated to: [[Model Services]], [[AI Governance and Assurance]], [[AI Operations Product]], [[AI Harness]], [[Inference and Serving Services]], [[Inference Optimization]], [[Minimum Operable Estate]] (incl. its mermaid node + summary), [[Rack AI Knowledge Base]], and the [[Source-to-Concept Crosswalk]] roadmap row. Capability-word uses of "control" (control plane / boundary / envelope — 17 in the roadmap) were **deliberately preserved**.

## Edges

- **Added:** [[Milestone Release Map]] → `RackaI Roadmap 10062026.csv` (technique/capability note). No new canonical concepts; placement principle, GPU-node boundary, observability split all reference existing homes ([[Capacity Pool]], [[Empirical Map]], [[Monitoring & Observability]]).
- **Removed:** GPU-node access as an in-charter Proof-4/T1.S4 item (moved to out-of-scope, not deleted from history).

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| hub-roadmap | derived | derived | Framing/structure + two product-boundary *decisions*; no capability upgraded to shipped. The accelerator split **lowers** an overclaim (selection was implicitly "Complete"; now only telemetry is Complete, selection is `gap`). |
| wiki-milestone-release-map | derived | derived | Projection kept in sync; no new assertions. |

No performance numbers introduced. The Proof-4 acceptance measures are named as *targets to instrument*, not current values. Proof-1 note now states margin/pricing stay `assumed` until representative-workload usage exists.

## Open Questions

- **Created:** Quota model must be re-expressed in intent+constraint terms to fit the placement principle (ties [[Capacity Pool]], P-004).
- **Resolved (direction):** "RackAI selects everything vs customer keeps GPU control" — resolved to *RackAI chooses by default; customer constrains* (implementation/quota rework still open). "Is GPU-node access in charter?" — resolved **No** (out of scope). "Is Observability M1 for end users or Rackers?" — resolved **both, as two distinct products**.

## Downstream Propagation Check

- Dependent notes updated for the Proof-3 rename (9 notes + crosswalk). Canonical IDs/aliases preserved (old alias kept; new alias added). No formula/coefficient/scorecard references the proof *name*, so none required edits. Source-to-Concept Crosswalk row updated in place (no new source concept — the review is logged via `source_docs` + this packet).

## Fitness / Consistency Result

- Structural: **Pass** — CSV parses (14 cols × 58 rows, 0 malformed); release-map stage IDs all `T#.S#` (0 stray `T#.R#`); deep-link anchor updated to the renamed Proof-3 header.
- Consistency: **Pass** — proof name reconciled corpus-wide; capability-word "control" preserved; CSV ↔ map ↔ roadmap agree on Proof-3 name, placement principle, GPU-node out-of-scope, accelerator telemetry-vs-selection split, and technique/capability tagging.
- Confidence propagation: **Pass** — nothing upgraded; one overclaim corrected downward (accelerator selection).
- Regressions: none.

## See Also

- [[RackAI Roadmap]] · [[Milestone Release Map]] · [[Minimum Operable Estate]]
- [[Wiki Hub]] · [[CHANGE_PACKET]]
