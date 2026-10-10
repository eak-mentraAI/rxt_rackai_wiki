---
id: chg-2026-10-10-prd-batch-b-j
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd batch b-j, prd reconciliation pass, wave 1-3 prd drafts]
related: [wiki-prd-coverage-plan, hub-roadmap, prd-workload-declaration-placement, spec-workload-declaration-placement, prd-operator-economics, prd-governed-execution-authority, prd-customer-observability-evidence, prd-sovereign-isolation-assurance, prd-model-lifecycle, prd-empirical-map-routing, prd-concierge-engineer, prd-inference-access-distribution, prd-fine-tuning-operations, ent-customer-observability, ent-evidence-report, chg-2026-10-10-prd-a-tech-spec]
source_docs: ["PM direction 2026-10-10: draft all remaining PRDs and tech specs through to product and engineering review; run concurrently, then reconcile in dependency order", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "PRDs and specs B–J drafted, reconciled, revised to v0.2 per the PO review; shared contracts and roadmap links added."
---

# CHANGE 2026-10-10 — PRD Batch B–J and Reconciliation

## Trigger

After PRD A's tech spec was product-approved and pushed (`e1ae63f`), the product owner asked for every remaining PRD in the [[PRD Coverage Plan]] to be taken through the PRD → tech spec → roadmap workflow, up to the point where product and engineering approval are needed. The whole batch is then reviewed at once. The product owner chose to draft concurrently and then run an ordered reconciliation pass. K (residency and multi-region) stays in the later horizon, as the plan says.

## What Changed

**Drafted (all v0.1, not approved).** Nine PRDs, each with its tech spec and its own change record:

| | PRD | Tech spec |
|---|---|---|
| B | [[Operator Economics & KPI Instrumentation PRD]] | [[Operator Economics & KPI Instrumentation Tech Spec]] |
| C | [[Governed Execution & Delegated Authority PRD]] | [[Governed Execution & Delegated Authority Tech Spec]] |
| D | [[Customer Observability & Evidence Report PRD]] (§1.2 = D-0 evidence contract) | [[Customer Observability & Evidence Report Tech Spec]] |
| E | [[Sovereign Isolation & Assurance PRD]] | [[Sovereign Isolation & Assurance Tech Spec]] |
| F | [[Model Lifecycle PRD]] | [[Model Lifecycle Tech Spec]] |
| G | [[Empirical Map & Evidence-Informed Routing PRD]] | [[Empirical Map & Evidence-Informed Routing Tech Spec]] |
| H | [[Concierge Engineer PRD]] | [[Concierge Engineer Tech Spec]] |
| I | [[Inference Access & Distribution PRD]] | [[Inference Access & Distribution Tech Spec]] |
| J | [[Fine-Tuning Operations PRD]] | [[Fine-Tuning Operations Tech Spec]] |

The skill's Mode 2 precondition (an approved PRD) was waived by the product owner for this batch; each spec says so in its document control table. Every spec has a read-only Codebase Grounding section pinned to the SHAs above. New canonical notes, written by D because the concepts are shared: [[Customer Observability]], [[Evidence Report]].

**Reconciliation pass (dependency order).** The drafts were written in parallel, so the pass went producers first:
1. **D-0 (D):** the evidence envelope was finalised. It gains `claimVersion`, `sourceId`, `audience`, `supersedes` and `actor.onBehalfOf`. Each record kind has one owner, every contributor emits a daily `coverage` record, and `recordId = UUIDv5(NS(contributor), kind|sourceId)`.
2. **C:** the authority interfaces were finalised: `ForPolicyChange(policyUID, generation, impactDigest)` and `ForBoundaryException(exceptionUID, specDigest)`, each returning `authorised{ref, authoriser, emergency} | denied | absent`.
3. **E, G, B, F:** E's `BoundaryException` was aligned to C. E defined the `BoundaryCacheIsolated` condition for I and the fence for the shared namespace. G adopted C's proposer rule. F's benchmark records now carry G's provenance fields. B's `cost` records were split by audience, with an agreed split against J.
4. **J, H, I:** J moved its adapter records to the kind `adapter-intake`. H adopted C's Phase-2 delegated identity and confirmation. I consumes E's cache condition and fence label.
5. **PRD A** comes last. The changes the other PRDs request are listed below for product review; they are **not applied**.

**Roadmap CSV.** The PRD and Tech spec link columns were filled for 33 rows, 60 cells in total. A diff confirmed that no other column changed. `scripts/lint-prd-spec.py` passes in both directions for all ten PRDs.

**Coverage plan.** The plan has status lines for B–J and D-0. Its header no longer says that no PRD exists. Two corrections to the plan's facts:
- Fine-tuning sidecar metering is written but not merged.
- Org-level role bindings are built and work when RBAC enforcement is on.

**Back-links** (`related` and See Also) were added on 30 canonical and hub notes.

**Corpus claims corrected after a read-only code check at `rackai@79ca4de`.** Each change below was verified by the orchestrator. Where a source note records what an engineering document claimed, a dated code-check note was added instead of rewriting the claim.

| Note | Correction |
|---|---|
| [[Multi-Tenancy and Metering Spec]], [[KPI Telemetry Target List]] | The fine-tuning metering sidecar (RACKAI-515) is on an unmerged branch (`cfbfd8d`), not on main |
| [[Monitoring and Auditability Spec]] | Seven `PrometheusRule` templates ship (RACKAI-475); the tenant one is off by default |
| [[Fine-Tuning Job]], [[Fine-Tuning]], [[Open Questions]] | DPO is merged for NVIDIA (`6c4aedb`); RLHF has no trainer; the console still says "Coming Soon" |
| [[Model Services]] | RACKAI-354 has no commits; it is not "in progress" |
| [[Model Class]] | The runtime enum is `vllm`, `optimized-nim-vllm`, `aim`; `nim` was removed |
| [[Organization]] | Isolation is per namespace on shared clusters, not "at the cluster level" |
| [[API Key]] | Keys are scoped to a tenant, optionally to a project; a hosted mint exists; there is no console page |
| [[OpenRouter Integration Plan]], [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]] | The G1 API-key condition is met. Row 15 is Path A (private), while the plan's success criterion is public, so the scope is open as I D-4 |
| [[RackAI Roadmap]] | IAC M4 "Won't Do" now notes that org-level bindings are built (C D-1). P-008 now notes that the audit read is admin-only |
| [[Traffic Class]] | Per-class profiles are `assumed`, not `measured`: no characterization exists |
| [[Empirical Map]], [[Request Routing]] | The map's cell key gains the serving configuration and accelerator. Routing stays inside the declaration's envelope (A/G rule) |
| [[Agent Identity]], [[GPU Co-Tenancy Risk]], [[Sovereignty Levels]], [[AI Governance and Assurance]] | Code-check notes added, with the proposed answers from E and C, marked pending approval |

**PRD A spec correction.** The v0.3 edit had deleted §4.6, §4.6.1 and §4.7 in `e1ae63f`. They are restored verbatim from v0.2 (see [[Workload Declaration & Placement Tech Spec]] §0 and its change record). The fix is not yet pushed.

## v0.2 — Product-Owner Review Disposition (same day)

The product owner reviewed the batch. Their own review was extended by another agent at their request. They recorded a disposition of **"Conditional acceptance; not formal artifact approval."** It is applied in this pass. Every batch PRD and spec is at **v0.2**, still `draft`, with *Product approval: not yet approved*. Each has a *Product review* row quoting the disposition. Every PD status reads *approved in principle*, *revise* (then revised and pending approval) or *held*; none reads simply "approved".

**Cross-PRD rulings applied**
- **X-1:** customer authority follows the actual customer security principal. A CustomerOrg owns policy only when it carries C's validated `spec.authorityPrincipal` marker, set by a two-party attestation; otherwise the Organization does. Invariant: no customer gains authority over another customer's workload through a shared parent.
  - C: `authority.PrincipalFor`.
  - E: the Organization is the isolation principal.
  - D: row-level security is keyed on authority principal plus Organization.
  - A: consumes both principals.
- **X-2:** G owns `scid` ([[Serving Configuration Identity]]), with frozen schema versions and explicit compatibility. F produces it; A matches on it.
- **X-3:** expressing customer intent is separated from execution authority. `model.retire` is disruptive and never emergency-eligible. A separate, tightly scoped `model.security-withdraw` is emergency-eligible.

**New shared contracts (canonical, draft)**
- [[Verification Status Vocabulary]]: typed statuses, with feasibility as a separate axis.
- [[Failure Mode Taxonomy]].
- [[Release Readiness States]]: four states plus named `blocked-by` blockers.
- [[Authority Context]], written by C.
- [[Serving Configuration Identity]], written by G.

**Divergence rulings applied**
- **Approved:** D DV-1, D DV-2, E DV-2.
- **Revised:**
  - D DV-3: joint attainment is `not_measured`; the lower bound is labelled an estimate.
  - E DV-3: `held` means the control is operating, not that no forbidden flow occurred.
  - H DV-3: the quota output is a non-executable draft.
  - J DV-3: attribution gaps fail visibly, never stand as an actor.
- **Conditional:** F DV-1 and F DV-3.
- **Approved with migration:** J DV-1.
- **Rejected:** I DV-2. No shared endpoint is offered without E's technical cache check.

**Decision revisions**
- B PD-11: a reusable kill-threshold framework that I also adopts.
- C PD-6 and PD-8.
- E PD-2 and PD-4: severity-based containment, pending security review.
- F PD-6.
- I PD-8 and PD-10.
- J PD-5, narrowed to scope (S-7).
- C PD-1 held for Erik.

Document-level corrections:
- H keeps usage, estimated charges and actual charges separate.
- E distinguishes intended from enforced Level 0 controls.
- F separates identity, qualification and offering.
- I separates the commercial account, the execution principal and the attribution scope.
- G's Phase-1 flow is operator-mediated.

**PRD A v0.4.** The rulings A4-1 to A4-13 were applied: A4-2 revised per X-1, and A4-10 kept as a requirement (Q-18). A4-14 is logged **pending ruling**. Release blockers were added (§13.0.1). PRD A's D-8 is annotated.

**Back-links** were added for the new shared notes, on Governance Hub, Empirical Map and Agent Identity.

## Confirmations and Commit (same day)

The product owner wrote: **"approve A4-14, confirm the rest, then commit."**
- PRD A A4-14 is approved and applied.
- Every non-material spec divergence that had no ruling is marked *confirmed by the product owner, 2026-10-10*: B DV-1/2, C DV-1/2, D DV-4/5, E DV-1/4, F DV-2/4, G DV-1/3, H DV-1/2, I DV-1/3, J DV-2, A DV-5/6.
- The batch is committed locally. The push is held until the Knowledge Platform session lifts its TEI hold.
- Formal product approval of the PRDs (decisions and acceptance criteria) and engineering approval of the specs are not given.

## Not Changed

- PRD A and its spec are unchanged beyond the restore above. The PRD A v0.4 changes the batch requests are listed for review only.
- Every PRD and spec in the batch is unapproved. No code repository was written to.
- Nothing was pushed: the Knowledge Platform session asked for wiki pushes to be held during the TEI restart.

## Open Items

- Product review of every batch PRD's proposed decisions and acceptance criteria, and of each spec's material divergences.
- Cross-PRD conflicts left open for decision:
  - C D-9 versus E PD-2: CustomerOrg-level policy against per-Organization dedication.
  - F Q-16 versus G Q-16: one function for configuration identity.
  - F Q-4 and Q-5 with C: whether promoting a rollout needs a platform authoriser, and whether `model.retire` can use the emergency path.
- PRD A v0.4 requested changes (product review).
- Engineering approval of every spec, including PRD A's.
