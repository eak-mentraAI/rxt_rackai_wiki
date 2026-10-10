---
id: chg-2026-10-10-prd-e-sovereign-isolation-assurance
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd e draft, sovereign isolation prd draft, sovereign isolation tech spec draft]
related: [prd-sovereign-isolation-assurance, spec-sovereign-isolation-assurance, pol-sovereignty-levels, evd-gpu-co-tenancy-risk, prd-workload-declaration-placement, spec-workload-declaration-placement, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["Product-owner instruction 2026-10-10: draft every remaining PRD and tech spec to the review point", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD E (Sovereign Isolation & Assurance) v0.1 and its tech spec v0.1 from a read-only code survey."
---

# CHANGE 2026-10-10 — PRD E Sovereign Isolation & Assurance Draft

## Trigger

The product owner asked for every remaining PRD and tech spec to be drafted to the point where product and engineering review are needed, and reviewed as one batch. PRD E is the wave-2 PRD for *where execution happens, what may cross the boundary, and how we prove it held*. The Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Sovereign Isolation & Assurance PRD]] (`prd-sovereign-isolation-assurance`, v0.1 draft, `confidence: assumed`). Roadmap items: *Customer isolation + private inference*; *First applicable assurance attestation* (product controls and evidence only).
  - Projects Levels 0 and 1 from [[Sovereignty Levels]] into a 12-rule set (B-1 to B-5 for every level; L1-1 to L1-7 for Level 1), grounded in [[GPU Co-Tenancy Risk]].
  - 21 FRs, 13 ACs, 11 proposed decisions (PD-1 to PD-11), 10 open decisions (D-1 to D-10). Level 2 and Level 3 are named later phases (K, MOE-4).
  - Answers PRD A's Q-4 (what makes a pool Level 1) as proposed decisions PD-1 and PD-2 plus FR-2 to FR-6.
- **New spec:** [[Sovereign Isolation & Assurance Tech Spec]] (`spec-sovereign-isolation-assurance`, v0.1 draft). Design: compiled-in rule and control catalogue, `DedicatedNodeSet` (cluster-scoped), `BoundaryException` (namespaced, C-authorised, fail closed), tenant network fences on the AI cluster, a CNI enforcement probe, reference restriction in `pkg/scope`, shared-cache detection, integration with A's placement guard (no second containment path), audit category `boundary`, and `boundary-held` / `boundary-exception` records in the D-0 envelope. Four milestones, M1–M4.
  - Divergences: DV-1 label ownership (non-material to E; an exception to A's spec contract), DV-2 Level 1 model artefacts must be pre-staged (candidate material), DV-3 network "held" semantics (candidate material), DV-4 B-5 verified by configuration only (non-material).
- **Grounding findings** (read-only, `RSS-Engineering/rackai@79ca4de`):
  - Isolation is namespace-per-Organization on one shared AI cluster. The only tenant NetworkPolicy fences the trainer metrics port (ingress-only); inference pods and egress are unfenced.
  - No taints, tolerations, dedicated pools or sovereignty fields; `AcceleratorClass` is cluster-scoped, so any tenant can reference any class.
  - "Sovereign" exists only as the single-CustomerOrg install mode.
  - `executionType` describes model-instance sharing and always defaults to `tenant-specific`; it can't distinguish levels.
  - The opt-in shared LMCache KV-cache example is unnamespaced across Organizations and documents a membership side channel.
  - The manager's AI-cluster grant is read-only on nodes, so the node-set controller is verify-only.

## Not Changed

- No other wiki file was edited (parallel batch). Proposed edits to the roadmap CSV (PRD and Tech spec columns for both rows), the coverage plan status line, and back-links on [[Sovereignty Levels]] and [[GPU Co-Tenancy Risk]] are returned to the orchestrator.
- No code repo was written to.
- Nothing was approved. Product approval and engineering approval are not recorded.

## Open Items

- PRD D-1 (security and legal validation) and D-2 (attestation choice) gate selling Level 1 and mapping controls.
- Spec Q-3 (DV-2 staging) and DV-3 need product review; Q-9 needs A's engineering agreement to the §1.6 exceptions; Q-7 needs C.
- `scripts/lint-prd-spec.py` reports L2 link-back errors for both notes until the roadmap CSV links are added.

## Reconciliation Pass

Reconciliation pass 2026-10-10: aligned with C's and D's final interfaces. No decision re-opened; everything stays v0.1 draft and unapproved.
- **Spec §4.8:** C's final `ForBoundaryException(exceptionUID, specDigest)` signature (emergency always false; `Consume` on apply). `status.requestedBy` is stamped at admission; `ruleSetVersion` sits in status and in `specDigest`. The fields C reads are listed.
- **Spec §4.9:** D-0 recordId formula, `sourceId`, `claimVersion`, `audience`, per-rule `outcome`, and a daily `coverage` record. Basis rules: `measured` only with probe or telemetry refs; system records are never `asserted`. Operator join and scrub records name the human operator. PRD NFR and PD-10 updated to match.
- **Spec §4.6, PRD FR-8, AC-7:** a checkable B-2 signal for I: condition `BoundaryCacheIsolated` on every `ModelDeployment`, a metric and per-period records, from M3. It covers the in-instance prefix cache on multi-tenant deployments.
- **Spec DV-1, §1.6, Q-9:** written as requested changes to A's spec that need A's product review.
- **Open conflict:** PRD D-11 and spec Q-11 record C's D-9 / Q-14 against E's PD-2 without choosing a winner.
- Round 3 (2026-10-10): spec §4.5, §12 and M2 now say the boundary controller renders the Level 0 ingress fence for platform-owned shared-endpoint namespaces, keyed on the label `rackai.rackspace.com/shared-endpoint=true`, which I's chart sets. Added an e2e test for it.

## PO Review Disposition 2026-10-10

Recorded as the product owner gave it: "Conditional acceptance; not formal artifact approval." The PRD and spec move to v0.2, both `draft`, with *Product approval: not yet approved*. A *Product review* row is added to both document control tables. Rulings applied:
- **PD-1 conditionally approved:** the shared control-plane boundary and residual risks are now explicit (PRD §6, FR-22, AC-14). Dedicated nodes are never called a dedicated cluster.
- **PD-3 and PD-5 to PD-11:** approved in principle. PD-5's wording now separates the intended baseline from what is enforced.
- **PD-2 revised (X-1):** the Organization is the isolation principal; customer ownership is C's authority principal (Authority Context). D-11 / Q-11 closed, D-3 reworded. Status *revised v0.2, pending approval*.
- **PD-4 revised:** a confirmed failure stops new placements at once (pool quarantine). Containment is by severity (S1–S4, PRD §12; spec §4.7): remove the foreign pod when safe; stop or relocate the protected workload only at S1. Recovery semantics are defined (FR-24). New security review D-12 / Q-12. This is sent to A's containment policy as a requested interface change (A4-6).
- **DV-2 approved:** pre-staging is a Level 1 prerequisite, with a staging manifest (provenance and SHA-256 digests) checked at resolution and at load (PRD FR-23, AC-15). Staging is a consumer requirement on F's intake.
- **DV-3 revised:** network `held` means the control was operating, per [[Verification Status Vocabulary]] (`basisKind: control-operating`). It is never proof of absence. The outcome value `violated` is renamed `not-held` throughout.
- **Document correction (High):** PRD §6 now has a column for each rule's Phase-1 enforcement state at Levels 0 and 1 (enforced, monitored, off). Docs and console text are generated from it.
- Failure handling is restated in [[Failure Mode Taxonomy]] terms (PRD §12, spec §9). Every AC now names an expected result, an evidence source and a gate. Spec milestones carry [[Release Readiness States]] and named blockers.
- DV-1 is phrased as a requested change to A's spec and stays pending A's product review.
- **Round A addendum (D and C envelope):** evidence scope now carries `authorityPrincipal` from [[Authority Context]]. Records carry a typed `verification.type: boundary` (coverage records carry `type: coverage`), and coverage records carry a `watermark` and `sourceOfRecord`. `violated` is mapped to `not-held` throughout. Actors follow C's attribution contract; there is no `system:unknown`. `status.requestedBy` is now the requester's Authority Context, and that context is passed to `ForBoundaryException`.
- §4.9 check (coordinator request): `boundary-exception` records now also carry `verification.type: boundary`. `scope.authorityPrincipal`, the coverage `watermark` and `sourceOfRecord`, and the Authority Context passed to `ForBoundaryException` were already in place.
- Consistency fix: §4.8 now uses C's exact signature `ForBoundaryException(ctx, AuthorityContext, exceptionUID, specDigest) → authorised{ref, authoriser, emergency, context} | denied | absent`.
- §4.9: `scope.authorityPrincipal` on system-produced records comes from C's `authority.PrincipalFor`. If that call errors, the record is not emitted and the gap is counted in coverage.
