---
id: chg-2026-10-10-prd-i-inference-access-distribution
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd i draft, inference access prd draft, inference access tech spec draft]
related: [prd-inference-access-distribution, spec-inference-access-distribution, pol-sovereignty-levels, idx-openrouter-integration-plan, idx-phase1-execution-glm, ent-billing-payment, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["PM direction 2026-10-10: draft every remaining PRD and its tech spec to the review stop point", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD I (Inference Access & Distribution) and its tech spec, v0.1, from a read-only code survey; not approved."
---

# CHANGE 2026-10-10 — PRD I Inference Access Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted to the point where product and engineering approval are needed, for review as one batch. PRD I is wave 3 in the [[PRD Coverage Plan]]. Mode 1, then Mode 2, of the PRD → spec workflow; the Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Inference Access & Distribution PRD]] (`prd-inference-access-distribution`, v0.1 draft, `confidence: assumed`). Roadmap items: *GLM 5.3 Flash deployment + OpenRouter Path A*; *OpenRouter: Inference aaS in OpenRouter*; *OpenRouter: BYOM in OpenRouter*; *Inference as a Service (direct)*.
  - One access contract for Level 0 inference across the direct API, OpenRouter (private and public) and BYOM. Private and shared endpoint shapes. Public listing gated on billing, which I does not build.
  - 21 FRs, 14 ACs, 10 proposed decisions (PD-1 to PD-10), 8 open decisions (D-1 to D-8). Row 78 is framed as D-1 and not answered.
- **New spec:** [[Inference Access & Distribution Tech Spec]] (`spec-inference-access-distribution`, v0.1 draft). Roadmap items: rows 15 and 77 only. Row 76 needs no access-layer code beyond the private path, and row 78 is conditional on D-1; both are deferred in its §1.3.
  - Design: a shared-endpoint route in the front proxy and authservice, an `APIKey` channel label, `MeteringEvent.Channel`, `executionType: shared` from the route, an error and 429 contract, `/v1/models`, and two CRDs (`InferenceListing`, `ConformanceRecord`). Four milestones, M0–M3.
  - Divergences: DV-1 (per-replica rate limits, non-material), DV-2 (cross-tenant cache control enforced by operator attestation, **material**), DV-3 (direct surface refused until D-1, non-material).
- **Grounding findings** (read-only, pinned SHAs; recorded in the spec §3):
  - The per-deployment OpenAI-compatible endpoint and API keys (HMAC, hosted mint) are built.
  - Inference metering is built. It stamps every event `tenant-specific` and skips any request whose path namespace differs from the caller's tenant, so a shared endpoint would be refused by authorisation and unmetered today.
  - There is no `/v1/models` route, no rate limiting or 429 on inference, no OpenAI-style error mapping, no console API-key page and no billing.

## Propagation

None applied by this change. Proposed edits to the roadmap CSV (PRD and Tech spec columns), the coverage plan status for I, and back-links on canonical notes are returned to the orchestrator, which applies them centrally.

## Not Changed

- No other note was edited.
- No code repo was written to.
- Nothing is approved. The PRD's *Product approval* and the spec's *Engineering approval* and *Product approval* rows read "not yet approved".

## Reconciliation

Reconciliation pass 2026-10-10:
- **E:** remote caches are now checked with E's B-2 detector (E spec §4.6, M3). DV-2 is narrowed to the in-process prefix cache, which is still attested. New PRD D-9 and spec Q-7 are open with E. New spec Q-10: E's tenant ingress fence does not cover the shared namespace.
- **F:** FR-7, FR-17, FR-18 and PD-5 are aligned to F's per-configuration availability and its *customer-managed, not RackAI-qualified* label. The listing admission uses F's offering labels; spec Q-5 is resolved.
- **D-0:** spec §4.8 now uses the final recordId formula, `claimVersion`, `sourceId`, `#rN` corrections, `benchmark-run` refs, platform-CustomerOrg scope with `audience: operator` for shared-endpoint records, and a daily `coverage` record.

Reconciliation round 3, 2026-10-10: FR-12 is gated on E's `BoundaryCacheIsolated=True` (E spec §4.6, M3), with `False` or `Unknown` treated as not proven. The operator attestation is kept as a fallback before E's M3 only. DV-2 is material until E's M3, then closed. PRD D-9 and spec Q-7 are closed, because E owns the rule. Q-10 is closed: the chart labels the shared namespace `rackai.rackspace.com/shared-endpoint=true`, and E renders the fence (E spec §4.5, M2).

## PO review disposition 2026-10-10

The product owner's conditional acceptance (not formal artifact approval) is recorded as given. The PRD and spec move to v0.2. Both stay draft, with *Product approval: not yet approved*.
- **Approved in principle:** PD-1 to PD-7 and PD-9; PD-6 kept conditional.
- **PD-8, revised:** maximum unreconciled exposure per paid surface with automatic suspension of new paid admission (PRD FR-22, AC-15, D-10; spec §4.9), using the Failure Mode Taxonomy's metering class.
- **PD-10, revised:** an economic decision framework (observation window, baseline, confidence, commercial owner, decision outcome) in §18, to be aligned with B's revised PD-11 (D-11).
- **DV-2, rejected:** the attestation fallback is removed (retained for the record). Listings are gated only on E's `BoundaryCacheIsolated=True`, and E's M3 is a release blocker for the shared endpoint. FR-12 and AC-9 are revised.
- **Document correction:** commercial account, execution principal and attribution scope are kept apart, using C's Authority Context (PRD §6, PD-3 wording, spec §4.4).
- **Shared contracts:**
  - failure handling restated in taxonomy classes (PRD §12, spec §9);
  - milestones carry readiness states and named release blockers (spec §13);
  - every AC names an evidence source and a gate;
  - attribute "verification" is renamed to review records, to avoid the typed statuses;
  - cross-team proposals are labelled as requested interface changes (S-5).
- **D-0 addendum:**
  - `scope.authorityPrincipal` from the Authority Context;
  - `coverage` with `sourceOfRecord` and `watermark`, reconciled to an independent source (S-3);
  - D's D-10 (per-request latency capture) acknowledged as spec Q-11.

- **Follow-up (same day):** §18 and PD-10 now reuse B's kill-threshold framework (B PRD §18.1); a breach leads to product review, never an automatic stop. D-11 is closed.

## Open Items

- PRD D-1 (row 78 direct IaaS), D-2 (billing ownership and funding), D-4 (row 15 Path A versus public provider scope) are the gating product decisions.
- Spec DV-2 needs product review; spec Q-1 to Q-9 are open.
