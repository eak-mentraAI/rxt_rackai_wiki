---
id: chg-2026-10-10-prd-g-empirical-map-routing
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd g draft, empirical map prd draft, empirical map tech spec draft]
related: [prd-empirical-map-routing, spec-empirical-map-routing, ent-empirical-map, ent-traffic-class, wf-request-routing, prd-workload-declaration-placement, spec-workload-declaration-placement, pol-benchmark-evidence-chain, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["Product-owner instruction 2026-10-10: draft every remaining PRD and tech spec to the review stop point", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD G (Empirical Map & routing) and its tech spec, v0.1, from a read-only code survey; nothing approved."
---

# CHANGE 2026-10-10 — PRD G Empirical Map & Routing Draft

## Trigger

The product owner asked for every remaining PRD and tech spec to be drafted to the point where product and engineering review are needed, and reviewed as one batch. PRD G covers proposal **P-005**. It was drafted with Mode 1, then Mode 2, of the PRD → spec workflow. The Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Empirical Map & Evidence-Informed Routing PRD]] (`prd-empirical-map-routing`, v0.1 draft, `confidence: assumed`, not approved).
  - **Roadmap items:** Empirical Map v1 + transferable/isolated split; Workload characterization; Evidence-informed routing (routing reads the map); Accelerator selection (evidence-informed); Day-zero model factory, closed-loop optimization.
  - **Content:** 22 FRs, 14 ACs, 11 proposed product decisions (PD-1 to PD-11), 10 open decisions (D-1 to D-10), a two-bet kill criterion (evidence improves decisions; K2 transfer). Prototype-first phasing.
  - **Answers A's Q-13** as proposed decisions: provenance (PD-3), configuration match (PD-4), load coverage (PD-5), freshness (PD-6) and who curates (PD-7). G's source replaces A's Phase-1 operator-curated `evidence.Source`.
- **New spec:** [[Empirical Map & Evidence-Informed Routing Tech Spec]] (`spec-empirical-map-routing`, v0.1 draft, not approved by engineering or product).
  - **Design:** `EvidenceArtifact` registry, PostgreSQL `empirical_map` schema split into transferable and isolated tables, an evidence evaluator behind A's seam, a deterministic recommender writing an immutable `PlacementRecommendation` and proposing through A's `PlacementProposal`, decision records, an `EvaluationPlan` for the pre-registered baseline. Audit category `empirical_map`; four D-0 kinds.
  - **Milestones:** M1 prototype, M2 characterization and telemetry inputs, M3 Map v1, M4 transfer (K2), M5 routing (later revision).
  - **Divergences:** DV-1 (two later rows not designed), DV-2 (operator proposes from the recommendation in the prototype), DV-3 (routing interface-only). All non-material, for confirmation.
  - **Cross-spec exceptions:** two optional `PlacementProposal` fields and two evidence reasons in A's spec; metering timing fields; monitoring scrape default and recording rules.
- **Grounding findings** (read-only, pinned SHAs):
  - Routing is per deployment: each llmisvc has its own InferencePool and EPP with preset scheduler config, so nothing chooses between deployments.
  - Metering leaves latency at zero and records no deployment or accelerator per request.
  - The llmisvc engine scrape and tenant recording rules are off by default. No rule reads TTFT or inter-token latency.
  - No benchmark harness or model-analysis package exists in the backend.
  - **Defect found in A's spec:** the committed A tech spec (`e1ae63f`) cites §4.6, §4.6.1 and §4.7, but those section bodies are missing from the file. The v0.3 edit replaced the text from §4.5's last bullet up to §4.8 and dropped them. G's spec relies on the v0.2 text and raises Q-2. A's file was not edited.

## Propagation

None applied by this change: other files are edited centrally by the orchestrator. Proposed edits (roadmap PRD and Tech spec links, coverage-plan status, back-links on [[Empirical Map]], [[Traffic Class]] and [[Request Routing]], the Request Routing and Traffic Class corrections, and restoring A's missing sections) are listed in the batch report.

## Reconciliation

- Reconciliation pass 2026-10-10: spec now cites the restored A §4.6, §4.6.1, §4.7 (scratchpad copy no longer relied on); `evidence.Source` signature labelled a requested addition to A (Q-2 narrowed); `scid` adds the model artifact digest. C's answer adopted (C PD-5): Phase 1 operator proposes, Phase 2 G's identity may propose at platform scope (PRD D-7, FR-11; spec DV-2, Q-3, §4.6, §7, M3). D-0 records aligned with D spec §4 (four kinds, recordId formula, `claimVersion`, `sourceId`, `audience`, `verification`, daily `coverage`; no-evidence performance is `derived` + `unverified, NoEvidence`). B cost inputs mapped (PRD D-8, spec Q-6). New spec Q-16: one configuration identity with F, and F's benchmark record fields.

## PO review disposition 2026-10-10

Product-owner review disposition, 2026-10-10: conditional acceptance; not formal artifact approval. Rulings applied in v0.2 (PRD and spec):
- PD-1 to PD-11 approved in principle (PD-2, PD-3, PD-11 explicitly). Product approval stays *not yet approved*; status stays draft.
- **X-2:** G owns `scid`. New canonical note [[Serving Configuration Identity]] (`ent-serving-configuration-identity`) with schema, digest, schema versioning (frozen versions; match at the evidence's version; declared equivalence for added fields; mismatch is visible `IdentityVersionMismatch`, never silent), compatibility and verification semantics. Spec Q-16 closed.
- Ranking evidence separated from `performance: verified` (PRD principle 3, §6, FR-7, FR-9, AC-3, AC-7; spec §4.4 `rankingRefs[]`), using [[Verification Status Vocabulary]].
- Document correction: Phase-1 operator-mediated proposal flow in the spec overview, components, dependency map and data flows; recommender proposes only in Phase 2 (C PD-5); AC-6 strengthened.
- S-5: `evidence.Source` signature, `PlacementProposal` fields and new reasons labelled as requested interface changes to A; a requested change to F recorded.
- Failure handling restated per [[Failure Mode Taxonomy]] (PRD §12, spec §9). ACs carry evidence source and gate; milestones carry readiness states and named release blockers per [[Release Readiness States]].

- D envelope addendum 2026-10-10 (spec §4.12): `scope.authorityPrincipal` from C's Authority Context; `coverage` records carry `watermark` and `sourceOfRecord`; `performance` records carry `verification.type: performance`.

## Open Items

- Product review of PD-1 to PD-11 and AC-1 to AC-14. Most contestable: PD-3, PD-11, PD-2.
- Engineering review of the spec, and confirmation of DV-1 to DV-3.
- Open decisions D-1 to D-10 (PRD) and Q-1 to Q-15 (spec). Row 11 (D-1, Q-1) gates *verified* claims.
- Roadmap link-back (P-09, T-10) pending the central CSV update.
