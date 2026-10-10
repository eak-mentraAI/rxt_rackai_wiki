---
id: chg-2026-10-10-prd-a-tech-spec
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd a tech spec draft, workload declaration tech spec draft]
related: [spec-workload-declaration-placement, prd-workload-declaration-placement, ent-workload-declaration, ent-accelerator-class, wiki-prd-coverage-plan, hub-roadmap, chg-2026-10-10-prd-a-workload-declaration]
source_docs: ["PM direction 2026-10-10: take PRD A through Stage 2 (tech spec)", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey, mirrors refreshed 2026-10-10)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted the PRD A tech spec (v0.1 to v0.3) from a read-only code survey; linked from the PRD and roadmap."
---

# CHANGE 2026-10-10 — PRD A Tech Spec Draft

## Trigger

PRD A ([[Workload Declaration & Placement PRD]] v1.0) was approved, and the product owner asked for Stage 2: the tech spec, written with Mode 2 of the PRD → spec workflow. Work stops before commit for engineering and product review.

## What Changed

- **New spec:** [[Workload Declaration & Placement Tech Spec]] (`spec-workload-declaration-placement`, v0.1 draft, `confidence: assumed`). It is a new spec that extends the [[Accelerator Selection Spec]] additively rather than revising it.
  - **Design:** five new CRDs (`WorkloadDeclaration`, `WorkloadDeclarationRevision`, `SupplyTarget`, `PlacementProposal`, `PlacementApproval`) and an interim `PlacementPolicy`. A `pkg/placement` package holds the feasibility engine and the supply, inherited and evidence interfaces. Two supply implementations: owned fleet, and a test-only fake. A placement guard handles runtime violations. Adds an audit category `placement`. Five milestones, M1–M5.
  - **Traceability:** all 22 FRs. Phase-1 FRs are covered; FR-21 is partial until D-0; FR-12, FR-18, FR-19 and FR-22 are deferred to Phase 2. All 14 ACs are mapped to designs and tests.
  - **Divergence:** none material. One narrowing is declared: Phase-1 containment is *stop* only, because "move back" is re-placement (FR-19). Product confirmation is requested.
- **Grounding findings** (read-only, pinned SHAs; recorded in spec §3):
  - `AcceleratorClass` tolerations are designed but not built.
  - Webhooks and RBAC enforcement are off by default, so integrity checks are placed in the controller.
  - `ModelDeployment` emits no audit events.
  - The audit category set is closed.
  - The UI fetches deployment conditions but never renders them.
  - API docs are vendored by hand from `openapi-external.yaml`.
- **Links:**
  - The PRD's *Tech spec(s)* row and `related` field now point to the spec.
  - The roadmap CSV's **Tech spec** column links the spec for *Supply-abstraction interface*, *Workload declaration (intent + constraints)*, *Supply abstraction v1 - second impl (AMD/partner)* and *Heterogeneous supply*. The two later rows get the interface only; their implementations are a later spec revision. No other cell changed (verified by a column diff).
- **Propagation:** back-links from [[Workload Declaration]] (`related`, See Also) and [[Accelerator Class]] (See Also).

## v0.2 — Product-Owner Refinement Pass (same day)

The product owner directionally approved the architecture and the A/G/C/E boundaries and asked for four corrections and four refinements. The scope stays the same: no new roadmap items, the same five milestones, traceability and test structure.

**Corrections:**
1. **Containment (§4.9):** suspected and confirmed violations are separate states. Confirmation takes two uncached reads, and a constraint that cannot be verified counts as violated. Containment is a deterministic, idempotent whole-deployment stop (zero replicas). If the stop fails, the outcome is `ContainmentFailed`, a page and a runbook. Automatic deletion is removed. Resuming needs a new proposal and approval.
2. **Schedulability (§4.4):** `supply.Fit` checks, deterministically and per node, the exact pod shape from the runtime adapter's pure `Build`. It covers taints, cordons, CPU, memory, shared memory, one node per replica, the runtime gate and in-flight commitments. It is not an optimiser, and the Kubernetes scheduler stays authoritative. Aggregate GPU counts are a pre-filter only.
3. **Approval binding (§4.7):** proposals are immutable and carry a digest. Approvals are immutable and single-use, bound to the proposal digest, the revision, a policy digest and an expiry (TTL owned by C). The behaviour for stale, expired and replayed approvals is defined, and so are inherited-policy changes (§4.5).
4. **Audit consistency (§4.11):** Kubernetes and PostgreSQL are two stores with no shared transaction. Every decision has a deterministic ID, used as the idempotency key in both, and moves through staged decision records (Intended → Audited → Revalidated/Abandoned → Applied → Recorded). Each declaration has one in-flight claim. Recovery works from any stage, and an in-process gap sweep checks for missing audit rows. Placement actions are gated on audit; safety actions (stop) are not.

**Refinements:**
- **Evidence (§4.6.1):** provenance, exact configuration match, workload and load coverage, and a freshness bound before *verified*. Evidence of known infeasibility must meet the same bar.
- **Adoption (§4.8):** adopted declarations are *system-inferred*. They carry no operator approval, are labelled as such, and are converted when the customer submits a revision.
- **Justification (§4.2, §4.7):** why revisions and approvals are separate CRDs (immutability, route-level authorisation, no aggregated API server), and why neither is independently managed.
- **MOE-0 / MOE-1 boundaries (§13.0):** the gating milestones, environments, users, acceptance criteria and decisions for each gate. Audit moved into M3 because the commit path needs it.

**Divergences (§1.4):**
- DV-1: stop-only containment, non-material, kept.
- DV-2: only stop-capable runtimes are offered. Candidate material.
- DV-3: inherited-policy tightening against realised workloads. Candidate material; with C.
- DV-4: adopted deployments are system-inferred and not initial realizations for AC-7. Candidate material.
- DV-5: *verified* can lapse. Non-material.
- DV-6: suspected violations are visible to operators only. Non-material.

The PRD has not been edited for these; they are returned for product review.

**New open questions:** Q-14 (approval TTL), Q-15 (guard timings), Q-16 (policy tightening), Q-17 (interconnect topology). Q-7 and Q-13 are widened.

## v0.3 — Product-Owner Divergence Decisions (same day)

Decisions as given by the product owner on 2026-10-10:
- **DV-2, approved with clarification:** declaration-managed placement is limited to runtimes with demonstrated, reliable containment. Qualification must verify that execution stops, confirm the resulting state, and produce evidence. A runtime that fails is not offered for declaration-managed placement, which does not remove it from other RackAI services.
- **DV-3, revision required:** naming affected workloads is necessary but not sufficient. A disruptive policy change needs authorisation under C's delegated-authority model, with the affected workloads and consequences presented before approval. A enforces the change, contains the affected workloads and records evidence; unauthorised changes are rejected. C defines the emergency security-policy path. This stays within the C/A boundaries and **remains open pending C's authority-model decision**.
- **DV-4, approved with clarification:** legacy adoption is not a new initial realization and needs no retroactive approval under AC-7. Adopted declarations are system-inferred, with no fabricated approval or customer authorisation. Later material changes follow normal approval.

**Spec changes:**
- §4.9.1 adds containment qualification: three checks (execution stops, the stopped state is confirmed, evidence is produced), bound to the adapter version and image digest, re-run in CI, with an allowlist that must cite qualification records.
- §4.5 is rewritten: effective versus pending policy generations, impact presentation, an `authority.ForPolicyChange` interface to C, bound single-use authorisation, enforcement with evidence, rejection, and an emergency path defined by C. Until C decides, disruptive changes are rejected (fail closed).
- §4.8: adoption creates no approval object, uses `decision: Adopted`, keeps `CustomerAuthorised=False`, and later material changes follow normal approval.
- §1.3, the §12 tests, the M4 breakdown, §13.0, Q-7, Q-16, event kinds and Appendix A are updated to match.
- v0.2's acknowledgment-only design is retained for the record.

No Phase-1 scope or initiative was added. The PRD's requirements are unchanged; only its Tech spec(s) row now names v0.3.

## Product Approval (same day)

The product owner wrote, on 2026-10-10: **"MOE-0 manual check is fine; approve spec with DV-3 interim."** Recorded as:
- the spec v0.3 is product-approved, with DV-3's fail-closed interim (disruptive policy changes rejected until C's authority model exists);
- DV-3 stays open pending C (Q-16);
- the MOE-0 manual runtime check (§13.0) is approved.

Engineering approval has not been given and is not recorded. The spec's `status` stays `draft` until engineering approves.

## Correction: Sections Restored (same day, after `e1ae63f`)

The v0.3 edit removed spec §4.6 (feasibility engine), §4.6.1 (performance evidence) and §4.7 (decision interface) because a text replacement covered too wide a range. That broken text was committed and pushed in `e1ae63f`. The PRD G drafting agent found the gap during the batch drafting. The three sections are restored verbatim from v0.2, with the v0.3 wording change *stop-capable* → *containment-qualified*. A diff against an independently recovered copy matches. No design change; product approval is unaffected. The fix ships in the next push.

## v0.4 — Product-Owner Review Rulings (same day)

The product owner reviewed the batch B–J requests to PRD A's spec ("Product-owner review disposition, 2026-10-10"). Their rulings:
- **Approved:** A4-1, A4-3 to A4-9, A4-11 to A4-13.
- **Revised:** A4-2, per X-1. Customer authority follows the actual customer security principal; a CustomerOrg owns policy only when explicitly validated as single-customer. Invariant: no customer can gain authority over another customer's workload through a shared parent.
- **Kept as a requirement, design deferred:** A4-10.

Applied in spec v0.4 (§0.1 lists each change and its section):
- C's final `ForPolicyChange` signature.
- The authority principal per X-1.
- The `placement-operator` role.
- Permissions renamed to `declaration:write` / `declaration:read`.
- Level 1 labels owned by E's boundary controller.
- Foreign-pod handling through E's severity-based containment.
- The D-0 envelope.
- G's verification rules, with the four option states.
- Attribution labels as Must have.
- New Q-18 (candidate revision).
- The PrometheusRule correction.

PRD A's D-8 is annotated with J's proposed answer. Section headings were checked against the committed version: only §0.1 and the restored §4.6–§4.7 differ. Formal re-approval of v0.4, and engineering approval, are separate recorded actions.

## A4-14 and Confirmations (same day)

The product owner wrote: **"approve A4-14, confirm the rest, then commit."**
- A4-14 is applied: Level 1 staging reasons `ModelSourceNotStaged` and `ArtefactIntegrityFailed` (§4.6 step 7, Appendix A).
- Non-material divergences DV-5 and DV-6 are confirmed.
- Formal re-approval of v0.4, and engineering approval, remain separate actions.

## Not Changed

- PRD requirements, acceptance criteria and decisions are untouched.
- No code repo was written to.
- The coverage plan status for A is updated at Stage 3, after approval.

## Open Items

- Spec Q-1 to Q-13. Q-1 (D-1 profile set), Q-2/Q-3 (C: policy source, approvers), Q-4 (E: Level 1 pool rules), Q-5 (D-0 shape) and Q-8 (unpinned legacy adoption) gate milestones.
- Product approval given 2026-10-10 (v0.3, with the DV-3 interim). Engineering approval not yet given.
