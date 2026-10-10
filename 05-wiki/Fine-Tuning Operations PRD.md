---
id: prd-fine-tuning-operations
type: prd
status: draft
owner: rackai-product
domain: product
aliases: [fine-tuning operations prd, prd j, fine-tuning boundary prd, fine-tuning partner boundary prd, ft operations prd]
related: [spec-fine-tuning-operations, ent-fine-tuning-job, ent-dataset, ent-lora-adapter, wf-fine-tuning, ent-model-deployment, ent-accelerator-class, ent-workload-declaration, prd-workload-declaration-placement, wf-metering, coeff-cost-per-gpu-hour, idx-unit-economics, ent-billing-payment, hub-model-services, hub-load-bearing-bets, hub-roadmap, idx-uniphore-recovery-plan, wiki-prd-coverage-plan, src-metering-spec, src-monitoring-audit-spec, src-identity-access-spec]
source_docs: ["00-hub/RackAI Roadmap.md (P-001, D4, K3)", "05-wiki/PRD Coverage Plan.md", "05-wiki/Uniphore Recovery Plan — RackAI Input.md", "06-sources/rackai-platform/Multi-Tenancy and Metering Spec.md", "RSS-Engineering/rackai@79ca4de (read-only)", "RSS-Engineering/rackai@cfbfd8d (read-only; unmerged RACKAI-515 branch)", "RSS-Engineering/rackai-ui@89bddb4 (read-only)", "RSS-Engineering/rackai-docs@ccb52a3 (read-only)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-product
summary: "PRD J: the fine-tuning boundary. RackAI serves, meters and evidences the artifact; a partner builds the tuning."
---

# Fine-Tuning Operations — PRD

| Field | Value |
|:--|:--|
| Version | v0.2 |
| Status | Draft |
| Owner | rackai-product |
| Reviewers | Product owner; Platform engineering (fine-tuning, metering); Commercial (partner scope); B and D owners |
| Product review | **Product-owner review disposition, 2026-10-10: conditional acceptance; not formal artifact approval.** PD-1 to PD-11 approved in principle (PD-2, PD-5, PD-8, PD-10 explicitly). Revised in v0.2: PD-5 and FR-4 scoped to the managed fine-tuning service (S-7); legacy-adapter migration (spec DV-1, approved with migration); actor attribution per C's contract, with gaps failing AC-15 visibly (spec DV-3); ACs carry an evidence source and gate |
| Product approval | not yet approved. Recorded by the product owner only (who, date, version); passing checks is not approval |
| Date | 2026-10-10 |
| Roadmap items | Uniphore: SFT/LoRA; Fine-tuning domain-model experiment; DPO fine tuning |
| Tech spec(s) | [[Fine-Tuning Operations Tech Spec]] (v0.2 draft, drafted alongside this PRD per product-owner instruction 2026-10-10; largely as-built) |

> **Artifact type: Product Requirements Document.** The canonical concepts are [[Fine-Tuning Job]], [[Dataset]], [[LoRA Adapter]] and the [[Fine-Tuning]] workflow. This PRD projects from them and must not redefine them. If they disagree, the canonical notes win and this PRD is stale (two disagreements are raised in §2).
>
> **Status banner.** *Draft PRD, retroactive for what is built.* A first-party fine-tuning pipeline already exists (RACKAI-385). This PRD does not re-specify it. It sets the **product boundary** around it, which nobody has written down: what RackAI serves, what a delivery partner builds, and how fine-tuning is metered, costed and evidenced. The implementation schedule doesn't change. Proposal **P-001**, decision **D4** ([[RackAI Roadmap]]). Requirements are intent, not commitments.
>
> **Scope line (read first).** This PRD owns **the fine-tuning boundary**: what RackAI serves and operates (adapter intake, the adapter's serving lifecycle, fine-tuning jobs as metered GPU workloads), what a delivery partner is responsible for, and fine-tuning metering, cost data and evidence. It does **not** own: choosing the partner or its commercial terms (product and commercial, downstream of P-001); training-toolchain features such as checkpointing and resume (row 75, out of scope); the placement mechanism (**A**; PRD A's D-8 is answered here as PD-10); the cost model and pricing (**B**, [[Billing & Payment]]); the evidence report (**D**); isolation guarantees (**E**); who may act (**C**); base-model onboarding (**F**).

## 1. Summary / Vision

RackAI's job in fine-tuning is to **host and operate the result**: take a fine-tuned adapter, whoever built it, and serve it reliably, metered and evidenced, on the fleet. Building the training service, assembling the data and inventing new methods is delivery work that P-001 says to evaluate partners for. This PRD draws that line and makes it testable. It covers the adapter a partner hands over, what the partner must do, and how every GPU-second spent on fine-tuning is measured, costed and proven.

Why now: the build is moving faster than the boundary. A preference-tuning method (DPO) shipped on the backend on 2026-10-07. Fine-tuning metering is being built on branches. A partner (Uniphore leading) is in discussion. If product doesn't set the boundary now, engineering and the partner will set it by default.

## 2. Problem Statement

**What is true today** (read-only survey, `RSS-Engineering/rackai@79ca4de`, the unmerged RACKAI-515 branch `rackai@cfbfd8d`, `rackai-ui@89bddb4`, `rackai-docs@ccb52a3`; `derived`):

- **A first-party toolchain is growing without a boundary.** The `FineTuningJob` pipeline runs validation, optional preprocessing, training, optional evaluation and adapter upload. It produces a `LoRAAdapter` (`rackai@79ca4de:api/v1alpha1/finetuningjob_types.go`, `internal/controller/finetuningjob_controller.go`). SFT with LoRA/QLoRA runs on NVIDIA, and AMD jobs use a recipe. **DPO on NVIDIA merged on 2026-10-07** (RACKAI-365 to 368, `rackai@6c4aedb`), with guards and tests (`internal/controller/finetuningjob_dpo_*_test.go`) and a CLI flag (`hack/cli/cmd/finetuningjob.go`, `--job-type SFT|DPO`). Method R&D is the delivery work P-001 says to partner.
- **Method availability disagrees across surfaces.** The API enum is `SFT | RLHF | DPO`, but RLHF has no trainer path, and the CLI says so. The user guide still lists `SFT | RLHF | DPO` (`rackai-docs@ccb52a3:docs/user/guides/rackai-user-guide.md`). The console marks DPO "Coming Soon" (`rackai-ui@89bddb4:src/app/pages/fine-tuning/ChooseJobMethodDialog.tsx`). The canonical [[Fine-Tuning Job]] note also says DPO is "Coming Soon", which no longer matches the backend.
- **A partner-built adapter can already be served, but nothing defines the handoff.** Anyone with model permissions can create a `LoRAAdapter` and upload files (`rackaictl loraadapter create|upload`, the console's upload dialog). The base model must exist (`internal/webhook/v1alpha1/loraadapter_webhook.go`). Integrity hashes are optional. The producer and the dataset are "informational only" (`api/v1alpha1/loraadapter_types.go`). Nothing records that an adapter was partner-built, and inference metering doesn't attribute usage to an adapter: `adapter_id` exists on usage records but the inference ext-proc never sets it (`internal/meteringextproc/processor.go`).
- **Fine-tuning is not metered on main.** On `79ca4de` the fine-tuning usage columns are NULL (`docs/metering_m2.md`). Sidecar metering is implemented on the RACKAI-515 branches (PRs #391 to #396, none merged), and its own design says it has **never run against a real database or GPU cluster** (`rackai@cfbfd8d:docs/finetuning-metering-design.md`). The wiki's [[Multi-Tenancy and Metering Spec]] records it as *AS BUILT 2026-10-08*. That overstates it (§2, last bullet). Even on the branch:
  - only the training Job is metered; the evaluation Job requests the same GPUs and carries no sidecar;
  - the GPU type is recorded only when the job names an `AcceleratorClass`, and the console defaults to "any accelerator";
  - failures are billed;
  - a lost completion is parked after 48 hours and billed zero until a person promotes it;
  - there is no live quota enforcement mid-job.
- **No audit trail.** Fine-tuning jobs emit no audit events. Cancelling a job is a `DELETE` with no record of who did it (the planned attribution fields are not built; [[Multi-Tenancy and Metering Spec]]). A `dataset` audit table exists, but nothing writes to it (`rackai@79ca4de:pkg/audit/drain.go`).
- **Placement is a hardware pin or nothing.** `spec.acceleratorClass` is a class name, unset (default scheduler), or `"auto"`. `"auto"` fails the job *after* submission with `AutoSchedulerPending` (`pkg/scope/finetuningjob_resolve.go`). Fine-tuning is outside A's declaration (PRD A's PD-8; PRD A's D-8 is open).
- **The partner's scope is unconfirmed.** It is not known whether Uniphore is a contracted delivery partner or a production tenant running its own applications (P-001's open question). The SFT/LoRA production status reported to Uniphore is also in conflict ([[Uniphore Recovery Plan — RackAI Input]]).

**Why it matters.** Without a boundary, every new trainer feature looks like product scope, and every partner conversation reopens it. Without complete metering, the GPU-hours fine-tuning consumes can't be costed, so B can't tell whether fine-tuning pays (row 27 is a commitment-critical Must). **Hypothesis** (no partner or customer evidence yet): a partner can deliver fine-tuning while RackAI keeps the operator role, and the operating data, by serving, metering and evidencing the artifact.

## 3. Product Principles

1. **Host the artifact, not the toolchain.** RackAI owns the point where a fine-tuned artifact becomes a served, operated, metered deployment (P-001).
2. **Nothing in the managed fine-tuning service runs on our GPUs unmetered**, whoever built the job and whatever its outcome.
3. **One serving path.** A partner-delivered adapter and a first-party adapter are served, metered and evidenced the same way.
4. **Know what you serve.** An adapter is served only when we know its base model, that its files are what was delivered, and where it came from.
5. **What is built stays; new toolchain work stops** unless product decides otherwise. The first-party pipeline is kept for customers who use it and for the experiment.
6. **Keep the experiment alive.** One instrumented domain-model proof point stays ours (K3).

## 4. Scope: Goals & Non-Goals

**Goals**
- A written, testable boundary between RackAI, the delivery partner and the customer for fine-tuning (the responsibility matrix below).
- Any adapter that meets the intake contract can be served, whoever produced it.
- Every GPU-second of fine-tuning is metered and attributable, and B can turn it into cost per job.
- Fine-tuning decisions and outcomes leave audit events and D-0 evidence records.
- The built pipeline keeps working, and the method surfaces tell the truth.

**Responsibility matrix (Phase 1)** (PD-1):

| Responsibility | RackAI | Delivery partner | Customer |
|---|---|---|---|
| Customer-facing tuning service, data and context assembly, method choice and R&D | — | **owns** | engages the partner |
| Training execution on RackAI GPUs (managed fine-tuning service) | runs it as a `FineTuningJob`, meters it (PD-5) | submits it through the job API only | or submits it directly |
| Training off RackAI | — | owns; only the adapter crosses to RackAI | — |
| Adapter quality and fitness for purpose | not guaranteed | **owns** (partner-built) | owns acceptance |
| Rights to the training data | — | warrants for partner-assembled data | owns its data |
| Adapter intake (integrity, base model, origin) | **owns** the check (FR-2) | delivers hashes and origin | — |
| Serving, scaling, hot-load, metering of inference | **owns** | — | — |
| Fine-tuning metering, cost data, evidence | **owns** | — | sees own usage |
| Incidents | serving and platform | training and adapter content | — |
| First-party pipeline (as built) | maintains; no new methods without product decision (PD-2) | may use it as a tenant | may use it |

**Non-Goals / Out of Scope**
- Choosing the partner or setting commercial terms: product and commercial (D-1).
- Checkpointing and resume, experiment tracking, and other training-toolchain features: out of scope (row 75; P-001).
- New fine-tuning methods (RLHF, tool-calling or VLM tuning): partner scope.
- The placement mechanism: **A** (PD-10 answers PRD A's D-8).
- Pricing, rating and invoicing: **B** and [[Billing & Payment]]. J provides the metered (billable) quantities only; B owns cost and reconciliation (PD-9).
- Live, mid-job quota enforcement: Metering M3/M4.
- Artifacts other than LoRA adapters (full or merged weights): D-5, with **F**.

## 5. Users & Personas

| Persona | Side | Needs from J |
|---|---|---|
| **Customer ML engineer** | Customer | Serve an adapter (own, partner-built or first-party); see what each job used |
| **Delivery partner** | Partner | A clear handoff: how to deliver an adapter, or run training on RackAI, and what it is responsible for |
| **RackAI operator** | RackAI | Every fine-tuning GPU-second is visible and attributed; lost usage surfaces instead of vanishing |
| **RackAI finance / B** | RackAI | Per-job metered quantity, accelerator type and period, to cost fine-tuning |
| **RackAI product** | RackAI | A boundary that holds as partner talks proceed; the K3 experiment |
| **D (evidence)** | Platform | `fine-tuning-job` and `adapter-intake` records in the D-0 shape |

## 6. Core Entities

| Entity | Role here |
|---|---|
| [[Fine-Tuning Job]] | A metered GPU workload; its outcome is evidenced. The pipeline is as built |
| [[Dataset]] | Customer- or partner-supplied training input; stays in the tenant's storage |
| [[LoRA Adapter]] | **The artifact at the boundary** (PD-3): what crosses from builder to RackAI |
| [[Model]] | The base model an adapter targets; onboarding is F's |
| [[Model Deployment]] | Where an adapter is hot-loaded and served |
| [[Organization]] | Tenant scope for jobs, adapters, usage and evidence |
| [[Accelerator Class]] | Today's placement pin for jobs (PD-10) |
| [[Workload Declaration]] | Not used by jobs in Phase 1; its hard-constraint subset applies in Phase 2 (PD-10) |
| [[Metering]], [[Cost per GPU-Hour]] | How usage is captured; the coefficient B applies to it |

**Defined here, not yet canonical** (only J uses them):
- **Delivery partner:** an organisation that builds fine-tuned adapters for RackAI customers, on or off RackAI. It is distinct from the consumption-surface bet in [[Load-Bearing Bets]].
- **Adapter origin:** where an adapter came from. *First-party job* (produced by a RackAI `FineTuningJob`), *partner-delivered* or *customer-uploaded*.
- **Adapter intake:** the checks an adapter passes before it may be loaded (FR-2).
- **Fine-tuning usage:** the metered GPU-seconds of one GPU-holding stage of one job, with its attribution.

## 7. User Journeys / Scenarios

**Partner-delivered adapter (training off RackAI).** A partner tunes an adapter for a customer's support assistant elsewhere.
1. In the customer's organisation, an authorised identity creates a `LoRAAdapter` naming the base model, origin *partner-delivered*, the partner, and integrity hashes for every file.
2. Files are uploaded. RackAI verifies them against the hashes and the base model, and the adapter becomes Ready. A mismatch leaves it not Ready, with the reason shown.
3. The customer attaches it to a running deployment of that base model. It is hot-loaded, and inference through it is metered like any other.
4. Intake and attach leave audit events and an evidence record. The adapter's origin is visible in the API and console.

**Training on RackAI GPUs** (first-party pipeline, used by the customer or by a partner acting in the customer's organisation).
1. A job is submitted. The trainer does not start until metering can record it.
2. Training, then evaluation, run. Each GPU stage is metered in GPU-seconds with the accelerator actually used.
3. The job ends, in success, early stop, failure or cancellation. A final usage record is written for each metered stage, with the outcome. If a final record is lost, operators are told.
4. The adapter is produced. A `fine-tuning-job` evidence record joins the job, its usage, its accelerator and its outcome. B turns the usage into cost.

**Domain-model experiment (Phase 2).** One adapter is trained on representative customer data. It is served through the same path and compared with a frontier baseline on quality and cost, using thresholds fixed before the run. The result is evidence for K3.

## 8. Functional Requirements

**Boundary and intake**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-1 | RackAI serves any LoRA adapter that passes intake, whether a RackAI job, a delivery partner or the customer produced it. Serving, inference metering and evidence are identical whatever the origin | MUST | PD-1, PD-3; the path is largely built |
| FR-2 | **Intake:** an adapter is loadable only if (a) its base model is a Model in the same organisation; (b) for adapters not produced by a RackAI job, every file matches the integrity hashes supplied with it; (c) its origin (first-party job / partner-delivered / customer-uploaded) and, for partner-delivered, the partner are recorded. An adapter that fails intake is never loaded, and the reason is shown. **Legacy adapters** (created before intake is enforced, without hashes) that are already attached keep serving temporarily with a visible warning, but **no new attachment** of an unremediated adapter is allowed. Each must be remediated (hashes supplied, or replaced) by the deadline or trigger set in D-10, after which it is not loadable | MUST | PD-4; spec DV-1 (approved with migration) |
| FR-3 | The responsibility matrix (§4) is published in the product documentation and is the reference for partner agreements | MUST | Product artefact |
| FR-4 | Within the **managed fine-tuning service**, training on RackAI GPUs, by a customer or a partner, is supported only as a `FineTuningJob` in an organisation the submitter is authorised for. RackAI offers partners no other training path | MUST | PD-5; who may act for a customer is C's (D-8) |
| FR-5 | The built pipeline keeps working unchanged: SFT with LoRA/QLoRA on NVIDIA, AMD recipe jobs, DPO on NVIDIA, evaluation and adapter upload | MUST | Retroactive; PD-2 |
| FR-6 | Method availability is stated once and matches across API, CLI, console and docs. A method with no trainer path (RLHF today) is not offered and is rejected at submission with a clear reason | MUST | PD-11; console DPO exposure: D-3 |

**Metering and cost**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-7 | Every GPU-holding stage of a job (training and evaluation) is metered in GPU-seconds, attributed to organisation, project, job, stage and the accelerator type actually used, including when no `AcceleratorClass` was named | MUST | PD-6; evaluation and GPU type are gaps today |
| FR-8 | A job does not start GPU work unless metering can record it (fail closed). Disabling this is an operator-only setting, and doing so is audited | MUST | PD-8 |
| FR-9 | Every outcome (success, early stop, failure including OOM, cancellation) produces a final usage record per metered stage, carrying the outcome, so pricing can decide what is charged | MUST | PD-7; charging policy for platform-caused failures: D-2 |
| FR-10 | A stage whose final usage is lost is surfaced to operators within a bounded, configured time and is never billed zero without an attributed operator decision | MUST | Promotion owner and period: D-4 |
| FR-11 | A tenant can read per-job usage after the job ends, scoped to the projects it may see. In-flight usage is visible | MUST (after end); SHOULD (in flight) | Per-record read exists |
| FR-12 | Each job's usage records are the **billable quantity** (charge view) and carry what B needs to reconcile them with its ledger without asking engineering: metered quantity per stage, accelerator type, period and scope, in B's join keys | MUST | PD-9; cost (internal view) is B's ledger |
| FR-13 | Tokens processed and trainable are recorded where the trainer reports them, and marked informational. No charge is derived from them in Phase 1 | SHOULD | PD-6; D-6 |
| FR-14 | Inference served through an adapter is attributable to that adapter | SHOULD | `adapter_id` is never set today |

**Audit and evidence**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-15 | Job submission, cancellation, terminal outcome, adapter intake (accepted or rejected), adapter attach and detach, metering-gate changes and promotion of lost usage each emit an audit event carrying C's [[Authority Context]] attribution: `attributed` (the acting principal) or `system` (a known controller). An action whose principal was not captured, or whose authority source is unknown, is recorded as an **audit coverage gap**, never as an actor | MUST | C's attribution contract; spec DV-3 |
| FR-16 | Each terminal job emits a `fine-tuning-job` evidence record, and each adapter intake, attach and detach emits an `adapter-intake` record, in the D-0 shape (`lifecycle` is F's kind) | MUST | §11 |

**Placement (answers A's D-8)**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-17 | Phase 1: jobs keep today's placement (a named `AcceleratorClass`, or unset). `"auto"` is rejected at submission with a reason instead of failing later. The accelerator actually used is recorded on the job | MUST | PD-10 |
| FR-18 | Phase 2: a job is checked against its organisation's inherited **hard** constraints (vendor allow-list, sovereignty minimum, location) through A's feasibility check, and is rejected, with the reason, if it would violate one. No full declaration is required | SHOULD (Phase 2) | PD-10; needs A Phase 1 and E |

**Experiment (Phase 2)**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-19 | One instrumented domain-model run on representative data, served through the FR-1 path, compared with a frontier baseline on quality and cost using thresholds fixed before the run | SHOULD (Phase 2) | K3; D-9 |

## 9. Non-Functional Requirements

- **Tenancy.** Jobs, datasets, adapters, usage and evidence are scoped to one organisation and project. No adapter, dataset or usage figure is visible across tenants. A holder of the metering write credential must not be able to forge or pre-empt another tenant's usage (open: D-7).
- **Data stays put.** Training data and adapters stay in the tenant's storage. When a partner trains off RackAI, only the adapter crosses. Whether partner training data may enter RackAI is E's rule.
- **Integrity.** No adapter is loaded whose files can't be matched to what was delivered (FR-2).
- **Fail closed on metering** (FR-8). The availability cost is accepted: while the metering store is down, new fine-tuning jobs wait.
- **Completeness.** In the managed fine-tuning service, GPU-seconds with neither a usage record nor a recorded gap are zero by design, and loss is detected (FR-10). This is an invariant, not a target. The evaluation-stage gap is recorded until spec M1.
- **Compatibility.** Existing jobs keep working. Legacy adapters without hashes keep serving where attached until remediated, but can't be newly attached (FR-2, D-10).

## 10. Platform Integration

| System | Needs from it | Provides to it |
|---|---|---|
| Identity & access (IAC) | Who may submit, cancel and upload adapters in an organisation, including partner identities (C, D-8) | Actor on every audit event |
| Tenancy & isolation | Organisation and project scope; E's rules on what training data may cross | Jobs and adapters scoped per organisation and project |
| Metering, quotas & billing | The metering outbox and usage records ([[Multi-Tenancy and Metering Spec]]); pre-execution concurrency check | GPU-seconds per job stage with accelerator type; informational tokens; adapter attribution of inference |
| Audit | The audit outbox and read API ([[Monitoring and Auditability Spec]]) | Fine-tuning and adapter audit events (FR-15) |
| Monitoring & observability | Existing training telemetry and job-status metrics | Metering gate, lost-usage and parked-usage signals for operators |

## 11. Loop Role & Cross-PRD Interfaces

**Loop role:** *Deliver the how* for fine-tuning, on the **operator** side: serve and operate the artifact. It also contributes to *prove it* through D-0 records and B's cost data.

| Interface | Direction | Other PRD | Defined where |
|---|---|---|---|
| Adapter intake contract (what a delivered adapter must carry) | provides | partner and customer; F (D-5) | This PRD (FR-2) |
| Fine-tuning usage (GPU-seconds per job stage, attribution) | provides | B | This PRD (semantics); [[Multi-Tenancy and Metering Spec]] (transport) |
| `fine-tuning-job` and `adapter-intake` evidence records (both J-owned) | provides | D | D-0 envelope ([[Customer Observability & Evidence Report PRD]]) |
| Cost model (cost per GPU-hour by accelerator) | consumes | B | [[Operator Economics & KPI Instrumentation PRD]], [[Cost per GPU-Hour]] |
| Inherited hard constraints and the feasibility check (Phase 2) | consumes | A | [[Workload Declaration]], [[Workload Declaration & Placement PRD]] |
| Authority to act in an organisation (partner identities, operator promotion of usage) | consumes | C | [[Governed Execution & Delegated Authority PRD]] |
| Boundary rules for training data and adapters | consumes | E | [[Sovereign Isolation & Assurance PRD]] |
| Base-model availability | consumes | F | [[Model Lifecycle PRD]] |

**D-0 contribution** (envelope per D; J names its kinds and claims):
- `kind: fine-tuning-job`. Subjects: the job, its base model and its output adapter. The claim: job type, outcome, stage outcomes, requested and observed accelerator, GPU count, metered GPU-seconds per stage and the usage-record references, the metering state (metered, parked, skipped, gate disabled), evaluation result, period. Basis: GPU-seconds `measured` (metering), accelerator `derived` (node labels).
- `kind: adapter-intake` (J-owned): intake accepted or rejected, attached, detached. The claim: origin, producer, integrity result, deployment. Basis: integrity `derived` (storage check); origin and producer `asserted` only when a human created the adapter, otherwise `derived`.
- Every record carries `claimVersion`, `sourceId`, `audience` and `scope.authorityPrincipal`, taken from C's [[Authority Context]], never reconstructed. Integrity is an intake check, not a [[Verification Status Vocabulary]] status. `recordId = UUIDv5(NS(contributor), kind+"|"+sourceId)`. A correction is a new record with `supersedes` and a `sourceId` ending `#rN`. J also emits a daily `coverage` record, counted from its own audit rows (`sourceOfRecord`), complete up to a stated `watermark`, so D can reconcile it against an independent expected population.
- `kind: cost` is **B's**, in two views: the *charge* view (`audience: customer`) is priced from J's usage rows; the *internal* view (`audience: operator`) comes from B's ledger. B reconciles the two (PD-9).

## 12. Failure Handling

Stated in [[Failure Mode Taxonomy]] classes and terms. The spec's §9 gives the full table.

| Failure | Class | Response | Continues / stops / degrades | Who is told |
|---|---|---|---|---|
| Metering store unreachable at job start | Metering | **Fail closed** (FR-8) | New GPU stages wait; running stages continue | Customer (job status), operator (alert) |
| Final usage lost (hard kill, node loss) | Metering | **Quarantine** the stage's usage: it is held and billed only by an attributed operator decision (FR-10). Exposure limit: the sweep window (D-4) | Other jobs unaffected | Operator (alert, job status) |
| A GPU stage runs with no sidecar (evaluation, until spec M1) | Metering | **Fail open** with a stated gap: recorded as `Unmetered`. Exposure limit: evaluation GPU time until M1, visible in B's reconciliation | Job continues | Operator (B reconciliation, evidence record) |
| Adapter fails intake | Admission | **Fail closed**: not loadable | The deployment's other adapters continue | Customer (adapter status), audit and evidence |
| Legacy adapter without hashes | Admission | **Quarantine**: kept where attached, no new attachment, remediation by D-10 | Existing serving continues | Customer and operator (warning condition, alert) |
| Attach to an incompatible deployment | Admission | **Fail closed** | Deployment unchanged | Customer (reason) |
| Authority source unavailable for submit or cancel | Authority | **Fail closed** for the new action | Running jobs continue | Caller (error) |
| Audit or evidence store down | Evidence | Jobs already admitted **proceed**; records are back-filled and flagged; gaps are detected through `coverage` | Jobs continue | Operator (alert) |

**Guaranteed never to happen:** a metered-by-design GPU stage of the managed fine-tuning service running with no usage record and no recorded gap; an adapter served whose integrity check failed; another tenant's adapter, data or usage visible; an unknown actor written as an actor.

## 13. Data Retention & Compliance

- Datasets and adapters are the customer's. They are deletable by the customer, except that an adapter can't be deleted while a deployment uses it (built).
- Usage records follow metering retention (`retentionDays`, default 365) and are not erasable within the window.
- Audit events follow audit retention (`complianceRetentionDays`).
- Evidence records follow D.
- Training data rights for partner-assembled data are the partner's warranty (§4). RackAI stores no prompt or training content in usage, audit or evidence records.

## 14. Scope & Phasing

| Phase | Delivers | Roadmap items |
|---|---|---|
| **1 (boundary; retroactive for what is built)** | Responsibility matrix and intake contract (FR-1 to FR-4); built pipeline retained and method surfaces made consistent (FR-5, FR-6); complete fine-tuning metering and cost data (FR-7 to FR-13); audit and evidence (FR-15, FR-16); placement as today, with `"auto"` rejected early (FR-17). Adapter attribution of inference (FR-14) if Phase 1 capacity allows | Uniphore: SFT/LoRA |
| **2** | Inherited hard constraints for jobs through A (FR-18); the instrumented domain-model experiment (FR-19) | Fine-tuning domain-model experiment |
| **Technique note** | DPO is a technique, not a customer outcome. It stays as built on NVIDIA under FR-5. Its availability follows FR-6, and console exposure is D-3. No further method work without a product decision (PD-11) | DPO fine tuning |
| **Out** | Checkpointing and resume | Fine-Tuning: Checkpointing + resume (no PRD) |

The schedule for RACKAI-385 and RACKAI-515 doesn't change. Phase 1 adds acceptance criteria and closes the gaps in §2. The spec plans those gaps as additive milestones for engineering to schedule.

## 15. Acceptance Criteria & Success Metrics

**Acceptance criteria** (Phase 1; each pass/fail; proposed, not approved):

Each criterion names its evidence source and its milestone gate (spec §13; [[Release Readiness States]]). The release gate for all of them is the Phase 1 release of *Uniphore: SFT/LoRA* (customer available).

| # | Criterion (observable, pass/fail) | Verifies | How tested | Evidence source | Gate |
|---|---|---|---|---|---|
| AC-1 | An adapter created without a RackAI job, with origin *partner-delivered* and correct hashes, becomes Ready, attaches to a running deployment of its base model, and serves inference metered exactly like a first-party adapter | FR-1, FR-2 | Integration test, both origins side by side | Integration run report; the two adapters' usage rows | M2 |
| AC-2 | An adapter not produced by a RackAI job, with missing or mismatched hashes or a base model not in the organisation, never becomes Ready and cannot be attached; the reason is visible in API and console | FR-2 | Negative tests per case | CI test report; `adapter-intake` rejected records | M2 |
| AC-3 | Every adapter's origin (and partner, if any) is retrievable through the API and shown in the console | FR-2 | API test plus console check | CI test report; console component test | M2 (API), M4 (console) |
| AC-4 | The responsibility matrix is published in the product docs and matches §4 | FR-3 | Review check | Docs review record | M4 |
| AC-5 | A job submitted by a partner identity, acting under its own identity through a customer `AuthorityGrant`, is metered, audited and evidenced identically to the customer's own job, and the partner integration guide documents no other training path in the managed fine-tuning service | FR-4 | Integration test plus docs review | Integration run report; audit rows; evidence records | M3 |
| AC-6 | The existing pipeline suite (SFT NVIDIA, AMD recipe, DPO NVIDIA, evaluation, upload) passes unchanged after Phase-1 changes | FR-5 | CI regression | CI test report | every milestone |
| AC-7 | RLHF is offered by none of console, CLI and docs, and an API submission is rejected at admission with a reason; the method list is identical across the four surfaces | FR-6 | API test plus surface check | CI test report; surface diff | M2 (API, CLI), M4 (console, docs) |
| AC-8 | For a job whose training and evaluation both hold GPUs, usage records cover both stages and name organisation, project, job, stage and the accelerator actually used, including when no `AcceleratorClass` was named | FR-7 | Integration test on a GPU cluster | `usage_records` rows; `fine-tuning-job` record | M1 |
| AC-9 | With the metering store unreachable, a new job does no GPU work and shows why; turning the gate off is possible only through an operator setting and produces an audit event | FR-8, FR-15 | Fault injection | Fault-injection run report; audit row | M0 (gate), M3 (audit) |
| AC-10 | Success, early stop, failure (including OOM) and cancellation each produce exactly one final usage record per metered stage, carrying the outcome | FR-9 | Test matrix | `usage_records` rows per case | M1 |
| AC-11 | A stage whose completion is lost is flagged to operators within the configured window and stays unbilled until an attributed operator decision, which is audited | FR-10, FR-15 | Kill-the-pod test | Alert record; dead-letter row; `usage_promoted` audit row | M1 |
| AC-12 | After a job ends, a tenant reads its per-job usage; a caller confined to one project sees only that project's jobs | FR-11 | API test | CI test report | M0 |
| AC-13 | From the records alone, B prices the charge view for every terminal job (quantity × accelerator type × period × scope), and reconciles it with its ledger, with no unattributed rows; evaluation-stage GPU time appears in both | FR-12 | Join and reconciliation test over a test estate | B's reconciliation output; `usage_records`; evidence records | M3 (blocked by B ledger) |
| AC-14 | Token counts appear where available, are labelled informational, and no charge uses them | FR-13 | Record check | `usage_records` rows; B charge records | M0 |
| AC-15 | Submission, cancellation, terminal outcome, intake, attach and detach each produce an audit event whose attribution is `attributed` or `system`. Any `principal-not-captured` or `unknown-authority-source` event in the test window is reported as an audit coverage gap and **fails this criterion visibly** | FR-15 | Audit query test, including a direct delete on the inner apiserver | Audit rows; J's daily `coverage` record with its gap count | M3 (blocked by C attribution contract) |
| AC-16 | Each terminal job produces one `fine-tuning-job` record, and each intake, attach and detach one `adapter-intake` record, validating against D-0; re-emission creates no duplicate, and a correction is a superseding record | FR-16 | Schema plus idempotency test | Evidence store query; `coverage` reconciliation | M3 (blocked by D `pkg/evidence`) |
| AC-17 | `acceleratorClass: auto` is rejected at submission with a reason; named and unset classes behave as today; the accelerator used is on the job's status | FR-17 | API test | CI test report | M1 (status), M2 (admission) |
| AC-18 | After intake is enforced, a legacy adapter without hashes that is already attached keeps serving with a visible warning; a new attachment of it is refused; it is listed for remediation with its D-10 deadline; after the deadline it is not loadable | FR-2 | Upgrade test on a copy of a real estate | Upgrade run report; adapter conditions; audit rows | M2 |

FR-14 (SHOULD) gets its criterion when scheduled. Phase-2 criteria (FR-18, FR-19) are written with Phase 2.

**Success metrics** (ladder; baselines "none today" unless stated; targets are postures):
1. **Metering coverage:** share of fine-tuning GPU-seconds with a usage record. Baseline: none on main. Posture: all of it.
2. **Lost usage:** stages parked or promoted per month. Posture: rare, and never unattended.
3. **Cost visibility:** share of terminal jobs with a computed cost in B. Baseline: none.
4. **Boundary in use:** partner-delivered adapters served, and their inference volume. Baseline: none recorded.
5. **Provenance:** share of served adapters with a complete intake record. Baseline: unknown (no origin field).
6. **Outcome (Phase 2):** K3 result of the domain-model experiment.

## 16. Dependencies

- **Engineering:** merge and enable RACKAI-515 (the sidecar), with RACKAI-588 (credential security sign-off) and RACKAI-589 (cluster connectivity). FR-7 to FR-12 rest on it.
- **Commercial / product:** the partner's contracted scope (D-1).
- **B:** the cost model, and the cost join (FR-12).
- **D:** the D-0 envelope and store (FR-16).
- **C:** partner identities and operator authority (D-8).
- **E:** what training data may cross the boundary.
- **A (Phase 2):** the feasibility interface and inherited constraints (FR-18).
- **F:** base-model availability, and any non-LoRA artifact (D-5).
- **Depended on by:** B (fine-tuning cost), D (evidence), the K3 experiment.

## 17. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| The partner never commits, leaving fine-tuning without a deliverer | The built pipeline stays usable (PD-2); kill criterion §18 |
| First-party method work keeps growing (DPO shipped; RLHF reserved) | PD-2, PD-11: new methods need a product decision |
| Fail-closed metering blocks jobs when the metering store is down | Accepted (PD-8); operator-only override, audited |
| Customers dispute charges for failed jobs | Outcome on every record (FR-9); policy is D-2 |
| Shared metering credential lets a tenant forge usage | Production gated on RACKAI-588 (D-7) |
| Partner adapters with unknown content | Intake (FR-2), with origin visible; quality is the partner's (§4) |

## 18. Kill / Falsification Criterion

The bet is that **fine-tuning delivery can be partnered while RackAI keeps the serving and operating role.** It is falsified if either holds after the partner evaluation (D-1) has run its course:
- **No deliverer:** no partner commits to deliver, and customers who need fine-tuning can't be served by partner-delivered adapters. P-001's "hoped-for partner" case. Then the build-vs-partner decision returns to the product owner.
- **Wrong artifact:** what customers need from partners can't be served through the adapter intake path, for example because they need full or merged weights, or training tightly coupled to serving. The boundary is then drawn at the wrong artifact and must be redrawn with F (D-5).

**Evidence:** the D-1 outcome, partner-delivered adapter counts and inference volume (metric 4), and intake rejections by reason. The domain-model experiment tests K3, the central bet, separately. J reports it but doesn't own that falsification.

**If falsified:** keep the serving, metering and evidence half (it stands on its own), and return the delivery half to the product owner as a funded-build or exit decision.

## 19. Open Decisions

| # | Decision | Owner | Blocks |
|---|----------|-------|--------|
| D-1 | Partner scope: is Uniphore (or another partner) a contracted delivery partner, or only a production tenant? (P-001's open question) | Product owner, with commercial | Partner responsibilities going live; §18 |
| D-2 | Platform-caused failures (node loss, eviction): bill, credit, or bill the part before the failure | Product owner, with B and finance | Pricing of FR-9 records |
| D-3 | DPO in the console: expose it as built (NVIDIA only), or keep it API and CLI only | Product owner | FR-6 console behaviour |
| D-4 | Lost usage: who promotes a parked stage, within what time, and into which billing period; and how a job spanning a month end is attributed | Product owner, with B, finance and operations | FR-10 |
| D-5 | Artifacts beyond LoRA adapters (full or merged weights): J's intake, or F's model onboarding? | Product owner, with F | Intake scope; §18 |
| D-6 | Tokens as a billing unit (with or without padding) after Phase 1 | Product owner, with B | FR-13 |
| D-7 | Metering write credential: one shared credential in tenant namespaces, or per tenant (RACKAI-588) | Security, with E | Production enablement of FR-7, FR-8 |
| D-8 | How a partner acts in a customer's organisation. **Proposed answer in C** ([[Governed Execution & Delegated Authority PRD]] FR-9): the partner acts under its own identity through a customer `AuthorityGrant`, never with customer-issued credentials | Product owner, with C | FR-4, FR-15 actor attribution |
| D-9 | Domain-model experiment: workload, data, frontier baseline and pass thresholds, fixed before the run | Product owner | FR-19 (Phase 2) |
| D-10 | Remediation deadline or trigger for legacy adapters without hashes (FR-2, AC-18): a fixed date, or a trigger such as the organisation's first partner-delivered adapter or the Phase 1 release | Product owner | FR-2 legacy migration |

## 20. Proposed Product Decisions

Product-owner review 2026-10-10: all approved in principle (conditional acceptance; not formal artifact approval). PD-5 is revised in v0.2 for scope (S-7).

| # | Decision | Alternatives considered | Why this one | Status |
|---|---|---|---|---|
| PD-1 | **The boundary is the §4 matrix.** RackAI owns intake, serving, metering, cost data and evidence. The partner owns the tuning service, data assembly, methods, its toolchain and adapter quality | RackAI builds full fine-tuning-as-a-service; the partner also owns serving | P-001's three-way split; serving is the operator job and feeds the [[Empirical Map]] | proposed — approved in principle 2026-10-10 (PO review) |
| PD-2 | **The built pipeline is retained as is**: SFT, LoRA/QLoRA, AMD recipe, DPO on NVIDIA. New training-toolchain features need a product decision | Retire it once a partner is signed; keep investing | Existing users and the K3 experiment need it; P-001 keeps "enough first-party capability to learn" | proposed — approved in principle 2026-10-10 (PO review) |
| PD-3 | **The artifact at the boundary is a LoRA adapter on a RackAI-served base model** in Phase 1 | Accept any model artifact | That path exists and is safe to hot-load; other artifacts are D-5 | proposed — approved in principle 2026-10-10 (PO review) |
| PD-4 | **Adapters not produced by a RackAI job need integrity hashes and a recorded origin before serving** | Optional hashes (today); signed artifacts | Cheapest control that makes "know what you serve" true; signing can follow | proposed — approved in principle 2026-10-10 (PO review) |
| PD-5 | **One meter for all training in the managed fine-tuning service:** partner or customer training offered as the RackAI fine-tuning service runs only as a `FineTuningJob`. Other GPU workloads in the broader RackAI portfolio (e.g. a future general-purpose GPU compute product) are outside this decision and are metered under their own products | Give partners raw GPU namespaces metered by node time | Keeps one metering, audit and evidence path; no unmetered side door | proposed — revise (PO review 2026-10-10): scope to the managed fine-tuning service, not every GPU workload (S-7); revised v0.2, pending approval (approved in principle) |
| PD-6 | **GPU-seconds are the billable quantity** (GPU limit × time from metering start to stage exit), across every GPU stage, **including evaluation, which the branch sidecar does not meter today**. Tokens are informational | Tokens; trainer wall time only | Matches what the GPUs were held for (as implemented on the unmerged branch); token counts include padding and are approximate | proposed — approved in principle 2026-10-10 (PO review) |
| PD-7 | **Meter every outcome**; what is charged is pricing's call (D-2) | Meter only successful jobs | GPUs were held either way; metering and charging stay separate | proposed — approved in principle 2026-10-10 (PO review) |
| PD-8 | **Fail closed: no metering, no job** (the startup gate is on by default) | Fail open and reconcile later | Principle 2. Cost: jobs wait while the metering store is down | proposed — approved in principle 2026-10-10 (PO review) |
| PD-9 | **J's usage rows are the billable quantity (charge view); cost (internal view) is B's ledger; B reconciles the two** and emits both `cost` records | J computes cost per job; billing priced from the ledger | One cost model in one place ([[Cost per GPU-Hour]]); billing follows what was metered, and the ledger cross-checks it (B FR-9) | proposed — approved in principle 2026-10-10 (PO review) |
| PD-10 | **Proposed answer to PRD A's D-8** (PRD A is approved; annotating it is the orchestrator's). Phase 1: jobs don't use the [[Workload Declaration]]; placement stays a named `AcceleratorClass` or unset, and `"auto"` is rejected at submission. Phase 2: jobs are checked against the organisation's inherited **hard** constraints through A's feasibility interface, with no full declaration, and never through a second placement mechanism | Full declarations for jobs now; jobs never constrained | Declaration attributes (profile, SLO, load) are serving-shaped and a job has no service level. But hard constraints protect the sovereign promise, and training touches customer data, so they must hold for jobs too, through A's one mechanism | proposed — approved in principle 2026-10-10 (PO review) |
| PD-11 | **Method surfaces tell the truth:** RLHF is not offered until a trainer path exists. DPO is a technique kept as built (row 26), with no further method work without a product decision | Keep advertising RLHF; expand DPO to AMD | Customers shouldn't see a method that fails; method R&D is partner scope | proposed — approved in principle 2026-10-10 (PO review) |

## See Also

- [[Fine-Tuning Job]], [[Dataset]], [[LoRA Adapter]], [[Fine-Tuning]] — the canonical concepts this PRD builds on
- [[Fine-Tuning Operations Tech Spec]] — the engineering design (largely as-built)
- [[RackAI Roadmap]] — P-001, D4 and K3
- [[PRD Coverage Plan]] — J's place in wave 1
- [[Workload Declaration & Placement PRD]] — PD-8 and D-8, answered by PD-10 here
- [[Multi-Tenancy and Metering Spec]] — fine-tuning metering transport
- [[Uniphore Recovery Plan — RackAI Input]] — partner context and the status conflict
- [[Load-Bearing Bets]] — the partner portfolio
