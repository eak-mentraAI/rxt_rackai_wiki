---
id: chg-2026-10-10-prd-b-operator-economics
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd b draft, operator economics prd draft, operator economics tech spec draft]
related: [prd-operator-economics, spec-operator-economics, coeff-cost-per-gpu-hour, idx-unit-economics, met-model-launch-lag, src-metering-spec, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["Product-owner instruction 2026-10-10: draft every remaining PRD and tech spec to the review point", "RSS-Engineering/rackai@79ca4de, rackai@cfbfd8d (RACKAI-515 branch), rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD B (operator economics, KPIs) and its tech spec from a read-only code survey; nothing approved."
---

# CHANGE 2026-10-10 — PRD B Operator Economics Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted to the point where product and engineering approval are needed, for review as one batch. PRD B (proposal P-003, decision D2) is wave 1 in the [[PRD Coverage Plan]], because cost history can't be backfilled. The Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Operator Economics & KPI Instrumentation PRD]] (`prd-operator-economics`, v0.1 draft, `confidence: assumed`, *not yet approved*).
  - Two separate halves. **Financial:** capacity ledger, cost rates, cost per GPU-hour and per workload (Phase 1), then cost per token, revenue inputs, margin, reconciliation and `cost` evidence records (Phase 2). **Operational:** KPI scorecard and Model Launch Lag records (Phase 2), and workloads per FTE (later).
  - 24 FRs, 14 ACs, 11 proposed decisions (PD-1 to PD-11), 8 open decisions (D-1 to D-8). The kill criterion has one falsifier per half.
  - Roadmap items: Cost model (internal cost/GPU-hour); Unit economics & margin; Operator KPI instrumentation; Model Launch Lag instrumentation; Operational leverage (workloads/FTE).
- **New spec:** [[Operator Economics & KPI Instrumentation Tech Spec]] (`spec-operator-economics`, v0.1 draft; engineering and product approval *not yet approved*).
  - A ledger sampler in the manager reuses the `AcceleratorClass` device accounting. New tables in the metering database. Rollups run in `rackai-metering`; platform-scoped routes are added to `rackai-usage`. There is no new service.
  - All 24 FRs are traced; FR-21 is deferred. Two non-material divergences (DV-1, DV-2). Eleven open questions (Q-1 to Q-11). Milestones M1–M5 plus M4a.
- **Grounding findings** (recorded in PRD §2 and spec §3):
  - No price, rate or cost field exists anywhere in the code.
  - Inference `*_secs` are zero on every row.
  - Nothing produces `model-deployment` usage rows, so deployed GPU time is not metered.
  - RACKAI-515 fine-tuning metering is on unmerged branches, not on main at `79ca4de`.
  - `AcceleratorClass.status` is a snapshot. Prometheus retention is 7 days (Mimir 30).
  - The usage and observability APIs are tenant-only.
  - There is no economics UI or docs page.

## Propagation

None applied by this change, because other files are edited centrally for the batch. Proposed edits returned to the orchestrator:
- Roadmap PRD and Tech spec links for the five rows.
- Coverage-plan status.
- Back-links on [[Cost per GPU-Hour]], [[Unit Economics Model]] and [[Model Launch Lag]].
- A correction to the RACKAI-515 "built" wording in [[Multi-Tenancy and Metering Spec]] and [[KPI Telemetry Target List]].
- Q-3 to A's spec owners (declaration labels from *nice to have* to *must have*).

## Open Items

- Product review of PD-1 to PD-11 and AC-1 to AC-14. The most contestable are PD-3, PD-4 and PD-11.
- Engineering review of the spec, Q-1 to Q-11, and DV-1 and DV-2 for confirmation.
- Finance inputs: D-2, D-3, D-4. Ownership: D-1.

## Reconciliation

Reconciliation pass 2026-10-10:
- **D-0.** Spec §4.8 is rewritten to D's final envelope.
  - Separate `cost` records per view: `internal` (`audience: operator`) and `charge` (`audience: customer`, only once a price input exists). `claim.internal` is dropped.
  - D's `recordId`/`sourceId` formula, `claimVersion`, typed `evidenceRefs`, `supersedes` corrections and `pkg/evidence.EnqueueTx`.
  - A daily `coverage` record per organization, counted from `capacity_daily` and `usage_records`.
  - Basis rules: `derived`, never `asserted`.
  - Spec Q-5 is resolved. PRD FR-14, AC-11 and §11 are updated.
- **J.** DV-1 and PRD FR-9 now say that the billable quantity (`charge`) comes from J's GPU-seconds usage rows, internal cost comes from B's ledger, and reconciling the two is B's check. J spec §4.5.3 should be aligned.
- **Evaluation stage.** The ledger samples every device pod, including evaluation pods (holder resolution now uses the `finetuningjob` and `finetuningjob-job-type` labels). Unmetered evaluation stages are reported as *unmetered stage*.
- **A.** Q-3 is reworded as a requested change to A's spec, for product review.

## PO review disposition 2026-10-10

Product-owner review disposition, 2026-10-10: *conditional acceptance; not formal artifact approval*. Applied in PRD v0.2 and spec v0.2. Both stay `draft`, and *Product approval* stays not yet approved.

**Decision rulings**
- PD-1 to PD-10: approved in principle.
- PD-3: as written.
- PD-4: clarified. FR-10 and spec §4.6 now state:
  - the denominator: output tokens in the same period;
  - the allocation basis: `allocated-device-seconds` or the `token-share` of a shared deployment;
  - for workloads with no traffic: idle-allocated cost, and *no traffic* for cost per token.
- PD-11: revised v0.2, pending approval. PRD §18 now has a reusable kill-threshold framework (§18.1) with metric, window, minimum data coverage, confidence requirement, owner-set threshold, and an action that is always an explicit product review, never an automatic stop. B's thresholds are in §18.2. New AC-15.

**Other rulings**
- FR-16 renamed to *allocation utilisation*. It is kept separate from physical GPU activity and useful throughput. Productive GPU Utilization stays *not defined* until D-8 decides. Spec §4.9 and AC-12 are updated.

**Shared contracts**
- PRD §12 and spec §9 are restated in [[Failure Mode Taxonomy]] terms.
- Every AC names an evidence source and a gate.
- Every spec milestone carries [[Release Readiness States]] and named `blocked-by` blockers.
- To avoid a clash with D's `coverage` status ([[Verification Status Vocabulary]]), "ledger coverage" is renamed *capture completeness*, reconciled against an independent population (S-3).
- `scope.authorityPrincipal` from C's [[Authority Context]] is added to the `cost` and `coverage` records. New Q-12 to C as a consumer requirement.
- The requests to A and C are labelled as consumer requirements (S-5).
- DV-1 and DV-2: no ruling; they remain for confirmation.
- Q-12 is resolved: C provides `authority.PrincipalFor` in `pkg/authority` (C spec §4.13, C M2). `blocked-by: C M2` is added to M3 and to AC-11 in both the PRD and the spec.
