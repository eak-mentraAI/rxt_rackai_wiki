---
id: chg-2026-10-10-prd-d-customer-observability-evidence
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd d draft, customer observability prd draft, evidence report prd draft, d-0 evidence contract draft]
related: [prd-customer-observability-evidence, spec-customer-observability-evidence, ent-customer-observability, ent-evidence-report, prd-workload-declaration-placement, spec-workload-declaration-placement, wiki-prd-coverage-plan, hub-minimum-operable-estate, hub-roadmap]
source_docs: ["Product-owner instruction 2026-10-10: draft every remaining PRD and tech spec to the point of product and engineering review", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD D and its tech spec (v0.1), formalised the D-0 evidence contract, and added two canonical notes."
---

# CHANGE 2026-10-10 — PRD D Customer Observability & Evidence Report Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted up to the point where product and engineering approval are needed, for review as one batch. PRD D owns the evidence contract (D-0) that every other PRD contributes to, so D-0 is section one of the PRD and the data model of the spec. Mode 1 and then Mode 2 of the PRD → spec workflow were followed. The Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Customer Observability & Evidence Report PRD]] (`prd-customer-observability-evidence`, v0.1 draft, `confidence: assumed`). Roadmap items: *Customer observability (product surface)*; *MOE-1 evidence report*.
  - §1.2 defines the D-0 evidence contract: the shared envelope from the batch brief, unchanged, plus five additive fields (`claimVersion`, `sourceId`, `audience`, `supersedes`, `actor.onBehalfOf`). It also sets eight rules and the kinds per contributor (A, B, C, E, F, G, H, I, J, D), and maps A's interim record onto the envelope (answers A spec Q-5).
  - 28 FRs, 20 ACs, 12 proposed decisions (PD-1 to PD-12), 9 open decisions (D-1 to D-9). Nothing approved.
- **New spec:** [[Customer Observability & Evidence Report Tech Spec]] (`spec-customer-observability-evidence`, v0.1 draft). It covers:
  - `pkg/evidence` (envelope, registry, UUIDv5 IDs, validation, outbox) and an `evidence` schema in the audit database (append-only, RLS, audit retention window);
  - a new `rackai-evidence` service (drainer, query, completeness, materialisers, reports);
  - coverage-based loss detection;
  - re-sourced tenant recording rules with project and model labels, and data states on the metrics API;
  - digest-bound report issuance;
  - four milestones, M1 to M4.
  - Divergences DV-1 to DV-3 are material and pending product review: per-runtime metric coverage, server-side latency, and histogram-based attainment. DV-4 and DV-5 are non-material.
- **New canonical notes** (shared across PRDs): [[Customer Observability]] (`ent-customer-observability`) and [[Evidence Report]] (`ent-evidence-report`).
- **Grounding findings** (read-only, pinned SHAs):
  - The tenant metrics API is wired but has no data source. A tenant recording-rule template has existed since 2026-09-25 (RACKAI-475), but it is off by default, reads `rackai_gateway_*` series nothing emits, and drops `project_id`.
  - TTFT, ITL and throughput are not in the API.
  - Usage is real, but its inference latency and compute fields are zero by omission, and there is no quota or price.
  - No console page or user doc covers usage, metrics or audit.
  - The audit category set is closed, and Prometheus local retention defaults to 7 days.

## Reconciliation

Reconciliation pass 2026-10-10:
- Added the J-owned kind `adapter-intake` (PRD §1.2.3, spec §4.3), replacing J's proposed adapter `lifecycle`.
- Adopted G's kind names: `placement-recommendation`, `decision-outcome`, `characterization`. These replace `recommendation`.
- Aligned `fine-tuning-job` (period) and `boundary-held` (per rule, with `outcome`) with J's and E's specs, and made the boundary-held report rule per rule (spec §4.11.3).
- Justified the new `rackai-evidence` service and documented a no-new-service fallback (spec §2.1, Q-2).

## PO review disposition 2026-10-10

The product owner's disposition is *conditional acceptance; not formal artifact approval*. Applied in PRD v0.2 and spec v0.2. Product approval is still not given.
- **PD-1 to PD-12:** approved in principle, on condition that canonical joint SLO attainment is kept and completeness is strengthened. PD-6 issuance is now one interface, replaceable by policy-governed automation.
- **PD-8 revised (X-1):** the report is scoped to the authority principal from C's [[Authority Context]]. Evidence carries `scope.authorityPrincipal`. Storage and RLS are keyed on authority principal plus Organization, never on CustomerOrg alone. AC-11 and AC-18 now cover a shared CustomerOrg.
- **PD-9 revised (S-3):** coverage is now two-level. *Collection* is stated vs received. *Observation* is reconciled to an independent source: decision journals or audit rows, state transitions, expected realised-workload windows and scrape coverage, with watermarks. Reports separate the two. AC-7 now tests both levels.
- **D-0 as a versioned platform contract:** PRD §1.2.5, FR-29, AC-21; spec §4.8 (compatibility classes, support window, change control, conformance suite).
- **DV-1 approved:** unsupported runtimes are visibly unavailable. **DV-2 approved:** latency is labelled server-side. **DV-3 revised:** `jointAttainment.status: not_measured`, an optional labelled lower bound, and per-threshold estimates; never `met` without measured joint attainment. New PRD D-10 records per-request capture as a requested interface change to Platform Monitoring and I.
- **Shared policies adopted:** each kind is bound to one status type from the [[Verification Status Vocabulary]] (spec §4.3.1, with a new A kind `containment-qualification`); failure handling is restated per the [[Failure Mode Taxonomy]] (PRD §12, spec §9); readiness states and named release blockers per the [[Release Readiness States]] (spec §13.1).
- Every AC now names its evidence source and gate.
- Follow-up: `authorityPrincipal` for system-produced records comes from C's `authority.PrincipalFor` (C spec §4.13). Spec Q-15 is closed by `CustomerOrg.spec.authorityPrincipal`.

## Not Changed

- The roadmap CSV, coverage plan, PRD A and its spec, and every existing canonical, hub and source note. Proposed edits are returned to the orchestrator.
- No code repo was written to.

## Open Items

- Product review of PD-1 to PD-12 and AC-1 to AC-20; product review of material divergences DV-1 to DV-3; engineering review of the spec.
- Gating decisions: row 11 (D-1), row 47 (D-2), the report's accountable owner (D-3), the permission mapping with C (D-6).
- Each contributor confirms its kinds (spec Q-10).
- Roadmap PRD and Tech spec link columns for both rows; coverage-plan status for D; back-links from [[Minimum Operable Estate]], [[SLO Attainment]], [[Monitoring & Observability]] and the PRD A spec.
- Correction to [[Monitoring and Auditability Spec]]: it says no `PrometheusRule` exists, but seven templates now ship.
