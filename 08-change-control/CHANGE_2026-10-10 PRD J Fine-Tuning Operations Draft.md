---
id: chg-2026-10-10-prd-j-fine-tuning-operations
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd j draft, fine-tuning operations prd draft, fine-tuning operations tech spec draft]
related: [prd-fine-tuning-operations, spec-fine-tuning-operations, ent-fine-tuning-job, ent-lora-adapter, ent-dataset, wf-fine-tuning, src-metering-spec, prd-workload-declaration-placement, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["Product-owner instruction 2026-10-10: draft every remaining PRD and its tech spec to the review stop", "RSS-Engineering/rackai@79ca4de, rackai@cfbfd8d (unmerged RACKAI-515 branch), rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD J (fine-tuning boundary) and its largely as-built tech spec; both v0.1, awaiting review."
---

# CHANGE 2026-10-10 — PRD J Fine-Tuning Operations Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted to the point where product and engineering review are needed. J is wave 1 and boundary-only in Phase 1 (P-001, D4). The Mode 2 precondition (an approved PRD) was waived for this batch by the product owner.

## What Changed

- **New PRD:** [[Fine-Tuning Operations PRD]] (`prd-fine-tuning-operations`, v0.1 draft, `confidence: assumed`). It covers:
  - the responsibility matrix (RackAI, delivery partner, customer);
  - the adapter intake contract;
  - complete fine-tuning metering and cost data for B;
  - audit, and D-0 records (`fine-tuning-job`, adapter `lifecycle`).

  It has 19 FRs, 17 ACs, 11 proposed decisions (PD-1 to PD-11) and 9 open decisions. PD-10 answers PRD A's D-8.
- **New spec:** [[Fine-Tuning Operations Tech Spec]] (`spec-fine-tuning-operations`, v0.1 draft). It is largely as built (AS BUILT markers at `rackai@79ca4de`), and marks the RACKAI-515 metering as **IN BRANCH, NOT MERGED** (`rackai@cfbfd8d`). It designs the gaps:
  - evaluation-stage metering and accelerator attribution;
  - parked-usage promotion;
  - adapter origin, producer and required integrity;
  - admission rejection of `RLHF` and `"auto"`;
  - a single method table;
  - audit category `finetuning`;
  - D-0 records and the B cost join.

  It has six milestones, M0 to M5 (M0 is existing RACKAI-515 work), and three divergences: DV-1 and DV-3 are material, DV-2 is non-material.
- **Grounding findings** (read-only):
  - DPO on NVIDIA merged on 2026-10-07 (`rackai@6c4aedb`), but the console and the canonical notes still say "Coming Soon".
  - RLHF is in the enum with no trainer path.
  - Fine-tuning metering is not on main.
  - On the branch, the evaluation stage is unmetered and the GPU type is empty without a named class.
  - There are no fine-tuning audit events.
  - Inference never sets `adapter_id`.

## Not Changed

Per the batch brief, no other file was edited: not the roadmap CSV, the coverage plan, PRD A, canonical or source notes. Proposed edits are returned to the orchestrator. No code repo was written to.

## Contradictions Raised (for central fix)

1. [[Multi-Tenancy and Metering Spec]] and [[Open Questions]] record fine-tuning sidecar metering as built and writing. It exists only on unmerged branches (`rackai@cfbfd8d`) and has never run against a real database or cluster.
2. [[Fine-Tuning Job]] and [[Fine-Tuning]] say DPO is "Coming Soon". The backend and CLI ship DPO on NVIDIA (`rackai@6c4aedb`).

## Reconciliation

- Reconciliation pass 2026-10-10:
  - **D-0 kinds.** The adapter record kind is renamed from `lifecycle` (F's) to J-owned `adapter-intake` (PRD FR-16, AC-16, §11; spec §4.5.2).
  - **D-0 envelope rules adopted** (spec §4.5): `claimVersion`, `sourceId`, `audience`, the `recordId` formula, corrections as `supersedes` records with `#rN`, the daily `coverage` record and `pkg/evidence.EnqueueTx`. `fine-tuning-job` uses a half-open `period`, and adapter integrity basis is now `derived`.
  - **B split made explicit.** J's usage rows are the billable charge view, B's ledger is the internal cost view, and B reconciles the two (PRD PD-9, FR-12, AC-13; spec §4.5.3, §7). The evaluation-stage metering gap is stated in PD-6 and in records (`Unmetered`).
  - **PRD D-8.** Marked "proposed answer in C": the partner acts under its own identity through a customer `AuthorityGrant` (spec Q-6, §7).
  - **PD-10.** Labelled as a proposed answer to the approved PRD A's D-8; annotating PRD A is left to the orchestrator.
- Reconciliation pass 2026-10-10 (B fix): spec §4.5.3 now says J's usage rows drive only the billable `charge` quantity. Internal cost comes from B's ledger, and B reconciles the two (B FR-9, alert `EconomicsBillableVariance`).

## PO review disposition 2026-10-10

This is the product owner's review, recorded as given: **conditional acceptance; not formal artifact approval.** Rulings applied in PRD v0.2 and spec v0.2:

**Decisions**
- PD-1 to PD-11 are approved in principle; PD-2, PD-5, PD-8 and PD-10 explicitly so.
- PD-5 is revised for scope (S-7). It applies to the managed fine-tuning service, not to every GPU workload. FR-4, principle 2 and the §4 matrix are reworded to match. Status: revised v0.2, pending approval.

**Divergences**
- **DV-1, approved with migration.** Attached legacy adapters keep serving temporarily, but get no new attachments and must be remediated by the deadline set in new PRD D-10. Added: FR-2 text, AC-18, and the spec §4.2.1 migration design.
- **DV-3, revised.** It now follows C's attribution contract: `attributed`, `system`, `principal-not-captured`, `unknown-authority-source`. The last two are audit coverage gaps, never actors. AC-15 now fails visibly on any gap, and spec §4.4 was rewritten.
- **DV-2:** no ruling.

**Shared contracts**
- The internal cost (B ledger) vs billable quantity (J usage) split is kept.
- Every AC now names an evidence source and a gate.
- PRD §12 and spec §9 are restated in [[Failure Mode Taxonomy]] terms.
- Spec milestones carry [[Release Readiness States]] and named release blockers (C M2, D M1, B M3, RACKAI-588, RACKAI-589).
- Mechanisms in other teams' areas (attribution capture and inference adapter attribution) are labelled as requested interface changes (S-5).

**D-0 addendum**
- `scope.authorityPrincipal` comes from C's [[Authority Context]].
- `coverage` carries `sourceOfRecord` and `watermark` (S-3).
- J's kinds carry no verification status.

Product approval: not yet approved.

- 2026-10-10 addendum: for system-produced records, `scope.authorityPrincipal` comes from C's `authority.PrincipalFor`. An error holds the record; the principal is never guessed (spec §4.5).

## Open Items

- PRD D-1 to D-9; spec Q-1 to Q-9; DV-1 and DV-3 need product review.
- Product approval and engineering approval are not yet given.
