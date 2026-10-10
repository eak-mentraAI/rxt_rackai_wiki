---
id: chg-2026-10-10-prd-f-model-lifecycle
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd f model lifecycle draft, model lifecycle prd draft, model lifecycle tech spec draft]
related: [prd-model-lifecycle, spec-model-lifecycle, hub-model-services, wf-model-launch-factory, wf-canary-rollback, met-model-launch-lag, prd-workload-declaration-placement, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["Product-owner instruction 2026-10-10: draft every remaining PRD and tech spec to the review stop", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD F (Model Lifecycle) v0.1 and its tech spec v0.1 from a read-only code survey; nothing approved."
---

# CHANGE 2026-10-10 — PRD F Model Lifecycle Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted to the point where product and engineering approval are needed, for one batch review. PRD F covers coverage-plan group F: rows 59 (*M2: Request new model support*, committed, RACKAI-354), 61 (*Model version upgrade (canary rollout)*), 60 (*M2: Sunsetting a model*) and 32 (*Multi-model operation*). The Mode 2 precondition (an approved PRD) was waived for this batch by the product owner.

## What Changed

- **New PRD:** [[Model Lifecycle PRD]] (`prd-model-lifecycle`, v0.1 draft, `confidence: assumed`, product approval: not yet approved). 29 FRs; 17 ACs; 10 proposed product decisions (PD-1 to PD-10, all *proposed*); 10 open decisions (D-1 to D-10). Phase 1 = rows 59 and 61 (MOE-1); Phase 2 = rows 60 and 32 (MOE-2).
- **New tech spec:** [[Model Lifecycle Tech Spec]] (`spec-model-lifecycle`, v0.1 draft; engineering and product approval: not yet approved). New CRDs `ModelRequest`, `ModelOffering`, `ModelRollout` and (Phase 2) `ModelRetirement`; authorisations through C's `ActionAuthorization`, an audit category `model`, `lifecycle` evidence records in the D-0 envelope, five milestones (M1–M5). All 29 FRs traced; FR-28 partial until D-0.
- **Divergences declared (spec §1.4):** DV-1 (no traffic canary for declaration-managed workloads until A supports candidate realisation; material), DV-2 (benchmark gate attaches rather than runs benchmarks; non-material), DV-3 (Phase-1 rollback signals exclude live correctness; material), DV-4 (usage during canary attributed to the alias; non-material). None approved.
- **Grounding findings** (read-only, pinned SHAs; spec §3):
  - No commit references RACKAI-354 in any repo; no engineering design found. The CSV and the delivery-plan source disagree on owner and status.
  - The catalog is compiled in (`//go:embed`): 11 Models, 30 ModelClasses. Backend docs still say "59-entry"; the user guide mentions DeepSeek, which is not seeded.
  - Known-broken catalog entries (`gemma-4-12b-aim`; twelve `optimized-nim-vllm` classes not deployable as seeded; the FP8 `aim` class unverified) are recorded only in README prose and shown in the console like any other.
  - `Model` has no version field; upgrades today are in-place repoints with no canary or rollback; the only rollback machinery is the serving-path dual-run.
  - Model and ModelClass emit no audit events; the audit category set is closed.
- **Links:** none added to other files. The PRD's *Tech spec(s)* row and the spec's *Based on PRD(s)* row link each other. Roadmap CSV links, coverage-plan status and canonical back-links are left to the orchestrator (proposed in the batch report).

## Propagation (proposed, not applied)

- Roadmap CSV rows 59, 60, 61, 32: *PRD* column → `prd-model-lifecycle`; *Tech spec* column → `spec-model-lifecycle`.
- Coverage plan §F: status line for the draft PRD and spec.
- Back-links from [[Model Services]], [[Model Launch Factory]], [[Canary & Rollback]] and [[Model Launch Lag]].
- Corrections: [[Model Services]] lists RACKAI-354 under "What Is Shipped Today"; [[Model Class]] lists `nim` in the runtime enum, which the code removed.

## Open Items

- Product review of PD-1 to PD-10, AC-1 to AC-17, and the material divergences DV-1 and DV-3.
- D-2 / Q-15: reconcile row 59 with engineering's RACKAI-354 design before approval.
- Interfaces for other PRDs: A (candidate realisation, Q-2; availability as a feasibility input), C (permissions and the early-stop authorisation, Q-4, Q-5), G (the "verified" rule over F's benchmark records), D (the `lifecycle` claim schema, Q-9), E (where sovereign models are qualified, Q-7), B (launch-lag timestamps; per-version attribution, Q-6).

## Reconciliation

- Reconciliation pass 2026-10-10: aligned with C, D-0, G and A. C's action classes adopted (request routine; gates and promotion consequential, platform, separation of duties; in-use retirement disruptive with customer authority): PRD FR-9, FR-17, FR-24, AC-5, AC-13, D-3, PD-8, §11; spec §4.4 now uses C's `ActionAuthorization` and `authority.Decide` (F's `ModelLifecycleApproval` retained for the record), §4.8 adds a per-organisation `ModelRetirement` subject, §5, §7. D-0: `recordId = UUIDv5(NS(contributor), "lifecycle|"+sourceId)`, `claimVersion`, `sourceId`, `audience`, daily `coverage`, corrections via `supersedes` (spec §4.9); adapters are J's (`adapter-intake`), FR-25 clarified. A §4.6.1 and §4.7 restored and cited; Q-11 resolved. G: benchmark and qualification records carry G's `EvidenceArtifact` header and `scid` inputs (artifact digest, VCP, accelerator type, GPUs per replica, serving path, engine version, operating points, metrics, B4 `thresholdsRef` and acceptor) and are registered as `EvidenceArtifact`s, not into A's Phase-1 source (spec §4.3, PRD FR-7). Open conflict: F `ConfigurationDigest` vs G `scid` (spec Q-16, G spec Q-16). DV-1 kept as a requested change to A's spec.

## PO review disposition 2026-10-10

Product-owner review disposition: conditional acceptance; not formal artifact approval. PRD and spec moved to v0.2; status stays `draft`; product approval: not yet approved. Rulings applied:
- PD-1 to PD-5, PD-7, PD-9, PD-10 approved in principle. PD-4 approved in principle with transition controls: PRD §14.1 and spec §4.7 transition plan (label, don't hide; never advertise unqualified; no disruption; qualify in order of use).
- PD-6 revised (v0.2, pending approval): *routine patch* under operator authority with notice vs *contract-affecting* upgrade needing customer consent or contractual authorisation (PRD §6, FR-20, AC-11; spec §4.5 `changeClass`, `consents[]`, Q-17).
- PD-8 approved in principle: retirement removes eligibility, never authorises a stop; separate security withdrawal via C's `model.security-withdraw` (PRD FR-30, AC-18; spec §4.10).
- X-2: F's `ConfigurationDigest` withdrawn; G's `scid` computed through G's library at qualification; records registered as `EvidenceArtifact`s; Q-16 resolved.
- X-3: C's catalogue adopted (`model.retire` disruptive, never emergency-eligible; `model.security-withdraw`; `model.rollout.own`); D-3, Q-4, Q-5 closed.
- DV-1 conditional: canary requirement retained; A spec Q-18 is a release blocker for declared-workload canaries (D-5, spec M3). DV-3 conditional: correctness limitation shown explicitly; validation path PRD D-11.
- Document correction: artifact identity, `qualification` status ([[Verification Status Vocabulary]]) and offering state separated (PRD §6, spec §4.2).
- Shared contracts: failure handling restated in the [[Failure Mode Taxonomy]] (PRD §12, spec §9); milestones carry [[Release Readiness States]] and named blockers (spec §13); each AC has an evidence source and gate (PRD §15, new AC-18, AC-19).
- Addenda: D-0 `scope.authorityPrincipal` from [[Authority Context]], coverage `watermark` and `sourceOfRecord`, `verification.type: qualification` (spec §4.9). E's staging manifest produced by intake as a consumer requirement from E, release blocker for Level 1 offers (PRD FR-31, AC-19; spec §4.1, M2).

## Checks

Frontmatter lint and broken-link check pass on the three files. `lint-prd-spec.py` reports only the expected L2 roadmap link-back errors until the CSV links are added. P-checks and T-checks done by hand; results are in the batch report.
