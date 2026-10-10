---
id: prd-sovereign-isolation-assurance
type: prd
status: draft
owner: rackai-product
domain: governance
aliases: [sovereign isolation prd, isolation and assurance prd, prd e, sovereignty level 1 prd, dedicated pool prd, boundary rules prd, customer isolation prd]
related: [pol-sovereignty-levels, ent-authority-context, evd-gpu-co-tenancy-risk, ent-organization, ent-capacity-pool, ent-accelerator-class, ent-workload-declaration, prd-workload-declaration-placement, spec-workload-declaration-placement, spec-sovereign-isolation-assurance, prd-governed-execution-authority, prd-customer-observability-evidence, prd-model-lifecycle, pol-verification-status, pol-failure-taxonomy, pol-release-readiness, hub-minimum-operable-estate, hub-battlegrounds, hub-ai-governance-assurance, wf-perimeter-info-flow, src-metering-spec, src-identity-access-spec, wiki-prd-coverage-plan]
source_docs: ["00-hub/Sovereignty Levels.md", "04-evidence/GPU Co-Tenancy Risk.md", "00-hub/Minimum Operable Estate.md", "05-wiki/PRD Coverage Plan.md", "05-wiki/Workload Declaration & Placement Tech Spec.md", "Product-owner review disposition 2026-10-10", "RSS-Engineering/rackai@79ca4de (read-only)", "RSS-Engineering/rackai-docs@ccb52a3 (read-only)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-product
summary: "PRD E: what Sovereignty Level 1 means at node and network level, the boundary rules C enforces, and proof they held."
---

# Sovereign Isolation & Assurance — PRD

| Field | Value |
|:--|:--|
| Version | v0.2 |
| Status | Draft |
| Owner | rackai-product |
| Reviewers | Product owner; Platform engineering (control plane, dataplane); Security; Legal; Compliance workstream; C, A, D and F owners |
| Product review | **Product-owner review disposition, 2026-10-10: conditional acceptance; not formal artifact approval.** PD-1 conditionally approved (shared control-plane boundary and residual risks must be explicit); PD-3 and PD-5 to PD-11 approved in principle; PD-2 and PD-4 revised in v0.2 (Organization as isolation principal per X-1; severity-based containment); baseline enforcement stated per release; failure handling, ACs and readiness aligned to the shared policies |
| Product approval | not yet approved — recorded by the product owner only (who, date, version); passing checks is not approval |
| Date | 2026-10-10 |
| Roadmap items | Customer isolation + private inference; First applicable assurance attestation |
| Tech spec(s) | [[Sovereign Isolation & Assurance Tech Spec]] (v0.2 draft, drafted alongside per product-owner instruction 2026-10-10; not yet approved) |

> **Artifact type: Product Requirements Document.** The canonical concept is [[Sovereignty Levels]]; this PRD projects Levels 0 and 1 from it into product rules and must not redefine the levels. The risk evidence is [[GPU Co-Tenancy Risk]]. Status words follow [[Verification Status Vocabulary]] (`boundary` status), [[Failure Mode Taxonomy]] and [[Release Readiness States]]. If they disagree, the canonical notes win and this PRD is stale.
>
> **Status banner.** *Draft PRD for a proposed initiative.* Nothing here is built: there are no dedicated pools, taints, sovereignty fields or boundary evidence today (§2). Requirements are intent, not commitments. Every product decision (§20) is *proposed*; the product owner's review of 2026-10-10 is a conditional acceptance, not approval.
>
> **Scope line (read first).** This PRD owns **where execution happens, what may cross the customer's boundary, and how we show the boundary controls operated**: the rules that make a pool Sovereignty Level 1, the Level 0 baseline, the boundary evidence, and the product controls a first attestation will rely on. It owns the **isolation principal** (the Organization). It does **not** own: *who* may act or authorise an exception, the customer's **authority principal**, and how actions are enforced (**C**, [[Governed Execution & Delegated Authority PRD]]); the placement mechanism and its containment execution (**A**, [[Workload Declaration & Placement PRD]]); model intake and staging (**F**, [[Model Lifecycle PRD]]); the customer evidence report (**D**, [[Customer Observability & Evidence Report PRD]]); residency, jurisdiction and multi-region, which are Level 2 (**K**, later horizon); the attestation programme itself (auditor, framework, audit scope), which is a compliance workstream.

## 1. Summary / Vision

Every RackAI tenant is isolated, but today that isolation is a namespace on one shared GPU cluster, and we can't show a customer how it is enforced. This PRD makes isolation a **stated, checkable product**: a short set of **boundary rules** per [[Sovereignty Levels|sovereignty level]], with Level 1 (Dedicated) meaning *whole nodes that are the customer's alone, fenced on the network, with nothing shared above them, inside a shared, RackAI-operated control plane*. Each rule is checked continuously and leaves evidence that its control was operating, period by period. We say plainly what each rule does and does not prove, and which rules each release actually enforces.

Why now: customer isolation and the first assurance attestation are MOE-1 Musts ([[Minimum Operable Estate]]). Level 1 is the floor for proprietary alpha and regulated data, and attestation lead times are long. A, C and D are all waiting on E's rules (A's open Q-4).

## 2. Problem Statement

**What is true today** (read-only code survey, `RSS-Engineering/rackai@79ca4de`, `rackai-docs@ccb52a3`; `derived`):

- **Isolation is a namespace on a shared cluster.** Each Organization gets one namespace on the control plane and one on the single AI workload cluster (`rackai@79ca4de:internal/controller/namespace.go`, `reconcileNamespace`, `ensureNamespaceExistsInAICluster`). The user guide promises resources "are not visible to other organizations" and bans cross-namespace references (`rackai-docs@ccb52a3:docs/user/guides/rackai-user-guide.md`, *Isolation*). It says nothing about the hardware or the network.
- **The network is mostly open between tenants.** The only per-tenant NetworkPolicy on the AI cluster fences the fine-tuning trainer's metrics port. It is ingress-only and selects trainer pods only; the code deliberately leaves inference pods and all egress unfenced (`rackai@79ca4de:internal/controller/namespace.go`, `reconcileAIClusterNetworkPolicy`; tests in `internal/controller/namespace_networkpolicy_test.go`). The chart notes that an unenforcing CNI makes the policy silently inert (`charts/rackai-manager/values.yaml`, `trainerMetricsNetworkPolicy`).
- **No dedicated hardware concept.** `AcceleratorClass` selects nodes with `nodeSelectorTerms` only; there are no taints, tolerations, dedicated pools or sovereignty fields, and it is cluster-scoped, so any tenant can reference any class (`rackai@79ca4de:api/v1alpha1/acceleratorclass_types.go`). Tolerations are designed in A's spec but not built.
- **"Sovereign" is an install mode, not a product level.** A sovereign install is a single-CustomerOrg deployment: the webhook refuses a second CustomerOrg unless `rbac.multiOrg.enabled`, and the one seeded CustomerOrg bills through `cmsAccountId` (`rackai@79ca4de:internal/webhook/v1alpha1/customerorg_webhook.go`). Nothing records which isolation a workload actually had.
- **Billing can't tell levels apart.** `executionType` (`shared` | `tenant-specific`) describes whether a *model instance* is shared, and defaults to `tenant-specific` because every instance is per-namespace. It says nothing about whether the GPUs or nodes were dedicated (`rackai@79ca4de:pkg/metering/event.go`; `internal/meteringextproc/config.go`).
- **A cross-tenant cache exists as an example.** The opt-in shared LMCache KV-cache recipe uses one unnamespaced Redis; its own comments name a cross-tenant membership side channel and note that no mitigation is built (`rackai@79ca4de:hack/cli/examples/lmcache-shared-kv-modelclass.yaml`).
- **No boundary evidence.** The audit categories are a closed set (`quota|config|dataset`; `pkg/audit/outbox.go`). No event or record says that an isolation control was checked or operating.

**Why it matters.** [[Sovereignty Levels]] sells Level 1 at MOE-1, and [[GPU Co-Tenancy Risk]] shows what it must remove: the silicon class (leftover memory, side channels, Rowhammer), including leakage between whole GPUs that share one multi-GPU node. It also shows that most real breaches are in software (container escapes, misconfiguration, shared caches), which apply at every level. **Hypothesis** (no customer evidence yet): an MOE-1 customer with proprietary or regulated data will accept dedicated nodes in a shared, RackAI-operated cluster as Level 1, provided the shared control-plane boundary and residual risks are explicit, the rules are explicit, and the evidence shows their controls operated.

## 3. Product Principles

1. **The boundary is declared, never implied.** A workload's level is a hard constraint in its [[Workload Declaration]]. E says what the level requires; A places to it.
2. **Dedicated means the whole node, not the whole cluster.** Whole GPUs on a shared node still leak to each other ([[GPU Co-Tenancy Risk]], "Spy in the GPU-box"), so the unit of Level 1 is the node. The control plane stays shared, and we say so: dedicated nodes are never described as a dedicated cluster.
3. **Deny by default at the boundary.** Every crossing is a named rule. Anything else is denied unless C authorises a time-bound exception.
4. **Software controls are the intended baseline at every level.** Dedicated hardware fixes none of the common breach paths. Each release states which baseline rules it enforces and which it only monitors (§6).
5. **Say what you can verify, and no more.** A rule's `boundary` status is `held` only with evidence for the period. `held` means the control was configured and operating; it is not proof that no forbidden flow occurred, unless the rule states an observed-flow basis ([[Verification Status Vocabulary]]). A check that couldn't run is `unverified`, never `held`.
6. **Contain by severity, protect the innocent.** A confirmed failure stops new placements at once. What happens to a running workload depends on severity: we remove the cause when it is safe to, and stop or move the customer's workload only when isolation can't otherwise be restored.
7. **E defines, C authorises, A places and contains, D reports.** Each boundary rule is defined once, here. Mechanisms in other teams' areas are written as requested interface changes.
8. **Controls before certificates.** E builds product controls and their evidence; the certificate is the compliance workstream's job.

## 4. Scope: Goals & Non-Goals

**Goals**
- Level 1 (Dedicated) is a precise, testable set of rules that A can place to and C can enforce against, presented with its residual risks.
- Every tenant, at every level, has a stated baseline, with what each release actually enforces shown honestly.
- For every workload and period, we can show which boundary controls were checked and their `boundary` status.
- A confirmed failure is contained in proportion to its severity, with defined recovery.
- The product controls and evidence that a first attestation needs exist before the attestation is scoped.

**Non-Goals / Out of Scope**
- Who may approve an exception, act on a workload, or administer policy, and the customer's authority principal: **C** ([[Authority Context]]). E names which rules may be excepted; C authorises.
- The placement mechanism, feasibility and the execution of containment: **A**. E supplies rules, checks and severity; A's guard executes stop or relocation.
- Model intake, staging and provenance records: **F**. E requires them as a Level 1 prerequisite (FR-23).
- The customer evidence report: **D**. E contributes `boundary-held`, `boundary-exception` and `coverage` records in the D-0 shape.
- **Level 2** (data, models, logs and backups pinned to a jurisdiction) and multi-region: **K** (Residency & Multi-Region, MOE-3). **Level 3** (customer hardware): MOE-4. Both are named later phases only (§14).
- The attestation programme: framework choice, auditor, audit scope and timeline (compliance workstream; D-2).
- Context-assembly information-flow control for agents ([[Perimeter Information-Flow Control]]): later research.
- Observing individual network flows (flow logging): not in Phase 1; network statuses are control-operating claims (principle 5).
- GPU-side confidential computing: not in this horizon ([[GPU Co-Tenancy Risk]] §3).
- Pricing of levels: **B** and Metering (D-6).

## 5. Users & Personas

| Persona | Side | Needs from E |
|---|---|---|
| **Customer security / risk officer** | Customer | Know exactly what Level 0 and Level 1 guarantee, what they don't, and see each period whether the controls operated |
| **Customer application owner** | Customer | Declare a level and get it, with no hidden sharing and no needless outage when someone else causes a fault |
| **RackAI platform operator** | RackAI | Build and retire dedicated node sets safely; be told at once when a boundary check fails, with a severity and a runbook |
| **RackAI security and compliance** | RackAI | A control catalogue with evidence to scope the attestation against; the severity policy to review |
| **Sales** | RackAI | A defensible, plain statement of what each level includes in the current release ([[Sovereignty Levels]], *Selling Ahead of Delivery*) |
| **Downstream PRDs** (A, C, D, I, F) | Platform | One boundary rule set to place to, enforce against, gate on and report on |

## 6. Core Entities

| Entity | Role here |
|---|---|
| [[Sovereignty Levels]] | The canonical levels. E projects Levels 0 and 1 into rules |
| [[GPU Co-Tenancy Risk]] | The evidence behind each rule |
| [[Organization]] | The **isolation principal**: the unit of dedication (PD-2, X-1) |
| [[Authority Context]] (C) | The customer's **authority principal**, resolved by C; E does not infer customer ownership from the Organization or CustomerOrg |
| [[Accelerator Class]] / [[Capacity Pool]] | The pool A places onto; a Level 1 pool is one class bound to one dedicated node set |
| [[Workload Declaration]] | Carries the declared level as a hard constraint (A) |

**Defined here, not yet canonical** (C and A consume them; promotion to a canonical note is D-9):

- **Boundary rule.** One checkable statement about where execution may happen or what may cross the boundary. Each has an ID, the levels it applies to, what it constrains, its default (deny or allow), how it is verified (and whether its basis is *control operating* or *observed flow*), whether it may be excepted, and the evidence it produces. Rules are versioned as a set.
- **Dedicated node set.** The nodes that make up one Level 1 pool: all serving one Organization, with nothing else scheduled on them.
- **Boundary exception.** A C authorisation of an exceptable E rule, bound to a rule, a scope and a time window. Never standing.
- **Product control.** A named control (e.g. *dedicated compute*, *network isolation*) mapped to the rules that implement it and the evidence that shows it operated.
- **Severity.** The class of a confirmed boundary failure (S1 to S4, §12) that sets the containment response.

**The rule set: intended contract and what Phase 1 actually enforces.** "Enforced" means the platform prevents or contains the failure; "monitored" means it detects, records `not-held` and alerts, but does not prevent; "off by default" means the control exists but is not active unless enabled. Customer-facing statements must use this column, not the intent (FR-22).

| Rule | Levels | Intended: what must be true | Basis | Phase 1 (MOE-1) at Level 0 | Phase 1 at Level 1 | Exceptable |
|---|---|---|---|---|---|---|
| **B-1** Namespace boundary | 0, 1 | Tenant resources live in the Organization's namespace and reference nothing outside it | control | **Enforced** (built today) | Enforced | No |
| **B-2** No shared serving cache | 0, 1 | No KV, prefix or other serving cache is shared with another Organization | control | **Monitored** (detected and reported; not rejected) | Enforced (rejected at admission) | No |
| **B-3** Tenant network fence | 0, 1 | No pod of another tenant can open a connection into the Organization's namespace | control | **Off by default** (flag); where off, reported `not-held` | Enforced (via L1-6) | No |
| **B-4** Patched runtime stack | 0, 1 | Nodes run a container runtime and GPU toolkit at or above the security baseline | control | **Monitored** | Monitored | No |
| **B-5** No content in exported telemetry | 0, 1 | Prompts, completions and training data never leave the boundary in logs, metrics or traces | control (configuration plus operator record) | **Monitored** | Monitored | Yes (C) |
| **L1-1** Dedicated node set | 1 | Every node of the pool belongs to one dedicated node set for one Organization | control | — | Enforced (pool quarantined) | No |
| **L1-2** Taint and exact toleration | 1 | Every node carries the dedication taint; only that Organization's workloads tolerate it; no tenant workload tolerates every taint | control | — | Enforced | No |
| **L1-3** Reference restriction | 1 | Only the dedicated Organization's workloads can use the Level 1 pool | control | — | Enforced (rejected at admission) | No |
| **L1-4** Whole-node exclusivity | 1 | No pod of any other Organization runs on any node of the set. Named platform system pods are allowed | observed state | — | Enforced (contained by severity) | No |
| **L1-5** Whole GPUs only | 1 | No GPU in the set is time-sliced, shared by MPS, or partitioned | observed state | — | Enforced (contained by severity) | No |
| **L1-6** Network deny by default | 1 | The namespace denies all ingress and egress except gateway ingress, monitoring scrape, DNS and the platform object store | control | — | Enforced | Egress only (C) |
| **L1-7** Clean node lifecycle | 1 | A node joins a set only from a recorded clean state, and leaves only after a recorded scrub (GPU reset, local storage wiped) | operator record | — | Enforced as a precondition (record required); the scrub itself is an operator procedure | No |

Rules that define a level (L1-1 to L1-5, L1-7) are never excepted: a customer who doesn't need them declares Level 0 instead (PD-3).

**Level 1 residual risk, stated to customers** (PD-1): the RackAI control plane and the AI cluster's Kubernetes control plane are shared; the inference gateway is shared; operators can access nodes under C's authority; node clean-state between reset and wipe rests on an operator record in Phase 1; network statuses show the fence was operating, not that no flow occurred.

## 7. User Journeys / Scenarios

**Worked example: building and using a Level 1 pool.** A regulated customer (Organization `acme-risk`) buys Level 1 for an interactive model.
1. A RackAI operator follows the join runbook for four nodes: each is reset and recorded clean (L1-7), then labelled and tainted for `acme-risk`. The operator binds them to a Level 1 accelerator class.
2. RackAI checks every rule for the set. Only when all are `held` does the class become a Level 1 pool that A may offer, and only to `acme-risk` (L1-3).
3. The customer's model artefacts are staged into the platform object store with a provenance record and digests (FR-23). The declaration says *Level 1*. A places onto the pool, carrying the exact toleration (A spec §4.4).
4. RackAI applies the network fence to `acme-risk`'s namespace: gateway in, monitoring scrape in, DNS and object store out. Nothing else (L1-6).
5. Each period, RackAI records each rule's `boundary` status for the workload, with what was checked. D's report shows the customer that the controls operated, and states what that does and does not prove.

**Worked example: a co-residency fault (severity S2).** Another tenant's pod carrying a catch-all toleration lands on an `acme-risk` node.
1. The whole-node check (L1-4) sees a pod from another Organization on a dedicated node. A second, uncached read confirms it.
2. **New placements stop at once:** the pool is quarantined and A stops offering it.
3. The foreign pod is removed as soon as it is safe to (its own workload is rescheduled elsewhere). `acme-risk`'s workload keeps running; the customer is told, and L1-4 is `not-held` for the window.
4. If the foreign pod can't be removed within the S2 deadline, the fault escalates to S1: A stops or relocates `acme-risk`'s workload to a compliant Level 1 pool.
5. Once every rule is `held` for a full confirmation cycle and the operator records the recovery, the quarantine lifts. Evidence records the window, the response and the recovery.

**Worked example: an egress exception.** `acme-risk` needs its deployment to call an external vector store for one week.
1. The customer's admin requests an exception to L1-6 for that destination and window.
2. **C** decides whether it is authorised and by whom. Until C's model exists, the answer is *absent*, and the exception is not applied (fail closed).
3. With C's authorisation bound to the rule, the destination and the window, RackAI opens exactly that egress, closes it at the end of the window, and records a `boundary-exception` record. The period's evidence shows the rule *held, with exception X*.

## 8. Functional Requirements

**Rules and levels**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-1 | RackAI publishes a versioned **boundary rule set** listing, for each rule, its ID, the levels it applies to, the requirement, the default, its verification basis (control operating, observed state, or operator record), whether it is exceptable, the evidence it produces, and its enforcement state per level in the current release (§6 table) | MUST | The single definition C, A and I consume |
| FR-2 | A pool is **Level 1** only while every Level 1 rule (L1-1 to L1-7) and every baseline rule enforced at Level 1 is `held` for every node in its dedicated node set. A pool that is not is quarantined: never offered for new Level 1 placement | MUST | Answers A's Q-4 |
| FR-3 | A Level 1 pool can be used only by workloads of the Organization it is dedicated to. Any other Organization's reference to it is rejected | MUST | L1-3; today any tenant can reference any class |
| FR-4 | No tenant workload may tolerate the dedication taint except through its own Organization's Level 1 pool, and no tenant workload may tolerate every taint | MUST | L1-2 |
| FR-5 | No GPU in a dedicated node set is time-sliced, shared by MPS or partitioned | MUST | L1-5 |
| FR-6 | An Organization with a Level 1 pool has its namespace fenced: deny all ingress and egress except the allowed crossings in L1-6 | MUST | |
| FR-7 | Every Organization, at every level, and every platform-owned shared-endpoint namespace, can have an ingress fence against other tenants' pods (B-3). Where it is off, B-3 is reported `not-held` | SHOULD (Phase 1, off by default); MUST (Phase 2, on by default) | Staged to avoid breaking serving (D-7) |
| FR-8 | No serving cache is shared between Organizations at any level. This includes a runtime's own prefix cache on a deployment that serves several Organizations (a shared endpoint). A deployment configured to use a cross-Organization cache is rejected at Level 1 and reported `not-held` for B-2 at Level 0. Every deployment carries a checkable B-2 result that other PRDs can gate on (I) | MUST | Phase 2: rejected at Level 0 too |
| FR-9 | Nodes join a dedicated node set only from a recorded clean state, and leave only after a recorded scrub, before any other use. Each record names the human operator who made it | MUST | Operator runbook in Phase 1 (PD-10) |

**Checking and evidence**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-10 | Every rule is checked when anything it depends on changes (node, pod, policy, configuration) and on a regular resync. Each result is a `boundary` status: `held`, `not-held` or `unverified` | MUST | [[Verification Status Vocabulary]] |
| FR-11 | A confirmed failure on a Level 1 pool **stops new placements immediately** (pool quarantine) and starts containment by **severity** (§12): remove the cause when safe; stop or relocate the protected workload only when isolation can't otherwise be restored, or at once where continuing would break a hard sovereignty guarantee (S1). Stop and relocation are executed by A's guard; E runs no second stop path | MUST | PD-4; requested interface change to A (containment policy, A4-6) |
| FR-12 | For each workload and each Level 1 node set, RackAI emits a `boundary-held` evidence record per rule per period in the D-0 shape, naming what was checked, its basis and any gaps. A period with a gap is `unverified` for that rule. A daily `coverage` record reconciles emitted records against the expected population | MUST | Feeds D |
| FR-13 | Every check failure, severity assignment, containment step, recovery, node join and node scrub emits an audit event | MUST | |
| FR-14 | The customer can see, for their own workloads and node sets only, the declared level, each rule's `boundary` status, its basis, its enforcement state, and the time it was last checked. Control-operating statuses are labelled as such, never as proof of absence | MUST (API); SHOULD (console in Phase 1) | |
| FR-15 | Operators are alerted on any `not-held` or `unverified` Level 1 rule, with its severity | MUST | |
| FR-24 | A quarantined pool returns to service only after recovery: every rule `held` for a full confirmation cycle, plus an operator recovery record for S1 and S2 and a security sign-off for S1 | MUST | §12 recovery |

**Exceptions**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-16 | Only exceptable rules (B-5, L1-6 egress) may be excepted. An exception is applied only with a C authorisation bound to exactly that rule, scope, window and rule-set version; it is removed when the window ends | MUST | C owns authorisation |
| FR-17 | Without C's authorisation (including before C's model exists), an exception is not applied | MUST | Fail closed |
| FR-18 | Every applied, expired or rejected exception emits a `boundary-exception` record and an audit event | MUST | |

**Product controls, statements and prerequisites**

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-19 | RackAI maintains a **control catalogue**: each product control, the rules that implement it, and how its evidence is retrieved for a period | MUST | Row 41, product controls only |
| FR-20 | For any control and period, an authorised RackAI compliance user can retrieve the evidence records behind it | MUST | Retrieval through D's evidence store; no separate report |
| FR-21 | Usage records can be attributed to the sovereignty level the work actually ran at | SHOULD | D-6 with B and Metering; `executionType` is not reused (PD-8) |
| FR-22 | Every customer-facing statement of a level (docs, console, sales material) is generated from the rule catalogue for the current release: it states per rule whether it is enforced, monitored or off, and states Level 1's shared control-plane boundary and residual risks (§6). Level 1 is never described as a dedicated cluster | MUST | PD-1 condition; baseline correction |
| FR-23 | **Level 1 prerequisite:** model artefacts are pre-staged in the platform object store with a provenance record (source, revision, who staged it) and per-file integrity digests. A Level 1 workload loads only staged artefacts whose digests match; direct pulls from public hubs need a C-authorised exception | MUST | DV-2 approved; staging and provenance are a consumer requirement on F (requested interface change to [[Model Lifecycle PRD]] intake) |

## 9. Non-Functional Requirements

- **Integrity.** No Level 1 workload runs on a pool with a confirmed failure without that failure being quarantined, assigned a severity and contained per §12. Detection, removal and containment times are target postures for the spec to set and measure; there is no baseline.
- **Fail closed for new work.** If a rule can't be checked, it is `unverified`, and the pool is not offered for new Level 1 placement. Exceptions fail closed (FR-17).
- **Honest evidence.** Evidence states its basis per D-0: `measured` only with a probe or telemetry reference; `derived` for what the system infers from platform state, configuration or audit records; `asserted` only for a record made by a named human operator. Phase-1 node join and scrub records are the operator's own (`asserted`, actor = that operator); the system's boundary evidence that relies on them is `derived` (PD-10).
- **Honest claims.** A `held` network or configuration status means the control was operating; it is never presented as proof that no forbidden flow occurred (principle 5).
- **Tenancy.** No boundary view, record or alert reveals another tenant's identity, workloads or nodes to a customer.
- **No regression.** Existing Level 0 serving keeps working; the Level 0 network fence (FR-7) ships behind a flag until it is shown not to break serving.
- **Security and legal validation.** The rule set and the severity policy are reviewed by security and legal before Level 1 is sold as available (D-1, D-12).

## 10. Platform Integration

| System | Needs from it | Provides to it |
|---|---|---|
| Identity & access (IAC) | Permissions for platform admins (node sets), tenant admins (request exceptions, read boundary status) and compliance users (read control evidence); C's authorisation for exceptions; C's authority principal | New permission set |
| Tenancy & isolation | Organization namespaces on both clusters (built) | The rule set and the isolation principal: dedicated node sets, network fences, cache rule |
| Metering, quotas & billing | A sovereignty-level attribute on usage (D-6) | The level each workload actually ran at |
| Audit | Audit pipeline; a new boundary category | Events for checks, severities, containment, node lifecycle and exceptions |
| Monitoring & observability | Node, pod and policy signals from the AI cluster | Boundary metrics and alerts; tenant-visible boundary status |

## 11. Loop Role & Cross-PRD Interfaces

**Loop role:** *Stay inside your boundaries*, the "where execution happens" half. It serves the **sovereign** promise: the customer's isolation level is enforced and its controls shown to operate, not asserted.

| Interface | Direction | Other PRD | Defined where |
|---|---|---|---|
| Boundary rule set (rules, levels, basis, enforcement state, exceptable flag, evidence) | provides | C, A, D, I | This PRD (§6, FR-1) |
| What makes a pool Level 1 (pool labels, tolerations, compliance state) | provides | A | This PRD (FR-2 to FR-5); mechanism in the spec. Answers A Q-4 |
| Boundary check result and severity for a running placement | provides | A (containment policy) | This PRD (FR-11, §12); requested interface change to A (A4-6) |
| Isolation principal (Organization) | provides | A, D | This PRD (PD-2) |
| Authority principal (Authority Context) | consumes | C | [[Authority Context]] |
| B-2 cache result per deployment | provides | I | This PRD (FR-8); signal in the spec |
| Workload declaration (declared level as a hard constraint) | consumes | A | [[Workload Declaration]] |
| Authorisation of a boundary exception | consumes | C | [[Governed Execution & Delegated Authority PRD]] |
| Enforcement of actions against boundary rules | consumes | C | [[Governed Execution & Delegated Authority PRD]] |
| Staged artefacts with provenance and digests | consumes (consumer requirement) | F | [[Model Lifecycle PRD]] (requested interface change) |
| Evidence envelope (D-0) | consumes | D | [[Customer Observability & Evidence Report PRD]] |
| `boundary-held`, `boundary-exception`, `coverage` records | provides | D | This PRD (FR-12, FR-18), in D's envelope |
| Sovereignty level on usage | provides | B | This PRD (FR-21); pricing is B's |

## 12. Failure Handling

Classes and responses follow [[Failure Mode Taxonomy]].

| Failure | Class | Response | Continues | Stops / degrades | Notified | Exposure limit |
|---|---|---|---|---|---|---|
| A Level 1 rule can't be checked (engine or AI-cluster reads down) | Evidence | **Quarantine** the pool for new placement; status `unverified` | Running workloads | New Level 1 placement stops | Operator (alert); customer (status `unverified`) | Escalates to an operator page after the maximum check age |
| Confirmed boundary failure on a Level 1 pool | Execution | **Quarantine** at once; **contain** by severity (table below) | Per severity | New placement stops | Customer and operator | Per severity |
| Network fence can't be applied | Admission (for the Organization's reconcile) | **Fail closed**: the reconcile fails visibly; never reports success with the fence missing | Existing pods | Level 1 pool not offered; B-3 / L1-6 `not-held` | Operator | — |
| Network policy not enforced by the CNI | Execution | **Contain** as S1 for Level 1 namespaces | — | Level 1 workloads stopped or relocated via A | Customer and operator (page) | None |
| C unavailable or no model yet | Authority | **Fail closed**: exceptions not applied; containment still completes | Applied exceptions until their window or a failed re-check | New exceptions | Requester (status) | — |
| Audit or evidence store unavailable | Evidence | Checks and containment **proceed**; records back-filled and flagged | Everything | Evidence periods wait | Operator | Back-fill before the period's report |
| Containment step itself fails (foreign pod won't leave, stop doesn't complete) | Containment | **Escalate**: page, runbook; never delete the customer's workload or relax a rule | — | — | Operator (page); customer | — |

**Severity and containment (proposed; subject to security review, D-12).**

| Severity | Confirmed condition (examples) | Response | Protected workload | Exposure limit | Recovery |
|---|---|---|---|---|---|
| **S1 Critical**: a hard sovereignty guarantee can't hold while the workload runs | GPU sharing active on a node running the protected workload (L1-5); network policy not enforced for a Level 1 namespace; a shared cache connected to a running Level 1 workload (B-2); an S2 not resolved within its deadline | Quarantine; **fail closed**: A stops or relocates the workload to a compliant Level 1 pool (never a non-compliant one) | Stopped or relocated | None: act at confirmation | All rules `held` for a full cycle, operator recovery record and security sign-off; a stopped workload resumes through a new A proposal |
| **S2 High**: co-residency that can be removed | Another Organization's pod on a dedicated node (L1-4); a taint missing with a foreign pod present | Quarantine; **remove the foreign pod** when safe (its workload is rescheduled elsewhere) | Keeps running; customer told; L1-4 `not-held` for the window | Removal deadline (value set by Security, D-12); then **S1** | Foreign pod gone, rules `held` for a full cycle, operator recovery record |
| **S3 Medium**: control drift with no co-residency | A label or taint missing with no foreign pod; toleration mismatch; policy drift with the probe passing; an extra node matching the pool | Quarantine; restore the configuration | Keeps running; customer told | Restore deadline (D-12); a foreign pod appearing raises it to S2 | Rules `held` for a full cycle |
| **S4 Low**: unverified, no fault seen | A check couldn't run | Quarantine for new placement; operator ticket | Keeps running; status `unverified` | Page after the maximum check age | The check passes |

**Guaranteed never to happen:** a Level 1 pool offered for new placement while a Level 1 rule is `not-held` or `unverified`; a level-defining rule excepted; a status reported `held` for a period nobody checked; a protected workload moved to a non-compliant pool; a customer's workload deleted by the platform.

## 13. Data Retention & Compliance

E holds rule-set versions, node set records, check results, severities, containment and recovery records, exceptions and evidence records. None contains customer content. Evidence and audit records are retained per the platform audit retention setting, which must cover the attestation's observation period (D-2). Node scrub records are kept for the life of the node plus that period. This PRD supplies the evidence a first attestation relies on; it makes no compliance claim itself.

## 14. Scope & Phasing

| Phase | Gate | Delivers | Roadmap items |
|---|---|---|---|
| **1** | MOE-0 → MOE-1 | Rule set v1 with per-release enforcement states (FR-1, FR-22); Level 1 pools: dedicated node sets, taint and toleration, reference restriction, whole-node and whole-GPU checks, network deny-by-default, clean node lifecycle, pre-staged artefacts (FR-2 to FR-6, FR-9, FR-23); cache rule (FR-8); checks, severity-based containment, recovery, evidence and alerts (FR-10 to FR-15, FR-24); exceptions through C, fail-closed until C exists (FR-16 to FR-18); control catalogue (FR-19, FR-20). Level 0: B-1 enforced, B-2/B-4/B-5 monitored, B-3 behind a flag (FR-7 SHOULD) | Customer isolation + private inference; First applicable assurance attestation (product controls and evidence only) |
| **2** | MOE-1 → MOE-2 | Level 0 network fence on by default (FR-7 MUST); cache rule enforced at Level 0; automated node join and scrub; usage attributed by level (FR-21); dedication across several Organizations of one authority principal if D-3 allows | — |
| **Later** | MOE-3 | **Level 2**: jurisdiction-pinned data, models, logs and backups, residency-aware failover and per-jurisdiction evidence | K: Residency & Multi-Region (rows *Data-residency controls*, *Residency-aware placement and failover*, *Per-jurisdiction compliance evidence*) |
| **Later** | MOE-4 | **Level 3**: RackAI operated on the customer's own hardware | Named only |

**Prototype first:** build one dedicated node set on the MOE-0 rehearsal estate by hand, check every rule against it, and only then automate the checks (operate before automate).

## 15. Acceptance Criteria & Success Metrics

**Acceptance criteria** (Phase 1; each pass/fail; proposed). Gates follow [[Release Readiness States]]: the spec milestone named must reach *acceptance proven*; MOE-1 means *customer available* at MOE-1.

| # | Criterion (observable, pass/fail; expected result) | Verifies | Evidence source | Gate |
|---|---|---|---|---|
| AC-1 | A pool whose nodes all satisfy L1-1 to L1-7 becomes Level 1 and is offered to A. Removing the label or the taint from any one node, or binding a node without a clean-state record, quarantines the pool within the check bound, and A no longer offers it | FR-2, FR-9, FR-10 | Integration test results; `boundary` audit events | Spec M1; MOE-1 |
| AC-2 | A workload in another Organization that references a Level 1 pool is rejected, naming the rule, and no pod is created, with webhooks on and off | FR-3 | API test results; `reference_rejected` audit event | M1 |
| AC-3 | A tenant workload that tolerates the dedication taint outside its own Level 1 pool, or tolerates every taint, is rejected; a non-tolerating pod is never scheduled on, or stays on, a dedicated node | FR-4 | Scheduling test results | M1 |
| AC-4 | A dedicated node advertising time-slicing, MPS or a GPU partition makes L1-5 `not-held` and quarantines the pool; with the protected workload on that node, it is handled as S1 | FR-5, FR-11 | Integration test; audit and evidence records | M1 (detection); M3 (S1 handling) |
| AC-5 | From a Level 1 namespace, egress to an undeclared destination fails and egress to each allowed crossing succeeds; ingress from another tenant's namespace fails; gateway ingress and monitoring scrape succeed | FR-6 | E2E connectivity results on an enforcing CNI; CNI probe results | M2; MOE-1 |
| AC-6 | With the Level 0 fence flag on, a pod in tenant X cannot connect to a serving pod in tenant Y or in a platform shared-endpoint namespace, and serving through the gateway still works. With the flag off, B-3 shows `not-held` | FR-7 | E2E results; `boundary-held` records for B-3 | M2 |
| AC-7 | A Level 1 deployment configured with a serving cache shared with another Organization is rejected; the same configuration at Level 0 produces a B-2 `not-held` record, a failing B-2 result on the deployment and an operator alert. A shared endpoint with its prefix cache enabled shows B-2 `not-held` | FR-8 | API test; deployment condition; evidence records; alert | M3 |
| AC-8 | (a) A foreign Organization's pod injected onto a dedicated node is confirmed as L1-4 `not-held`; new placement onto the pool stops at once; the foreign pod is removed; the protected workload keeps running; customer and operator are told. (b) If removal is blocked past the S2 deadline, A stops or relocates the protected workload (S1). (c) After recovery, the pool returns to service only once every rule is `held` for a full cycle and the recovery record exists | FR-10, FR-11, FR-15, FR-24 | Fault-injection test; audit events for severity, containment and recovery; evidence records | M3; MOE-1 |
| AC-9 | For a test period, every Level 1 workload and node set has one `boundary-held` record per rule that validates against D-0, carries the right basis, and a `coverage` record reconciles them against the expected population. A rule whose check could not run for part of the period is `unverified`, never `held` | FR-12 | Evidence schema validation; gap-injection test; coverage record | M4; MOE-1 |
| AC-10 | An egress exception with no C authorisation is not applied. With an authorisation bound to the rule, destination, window and rule-set version, exactly that egress opens, closes at window end, and `boundary-exception` records are produced. A request to except a level-defining rule is rejected | FR-16, FR-17, FR-18 | API test; NetworkPolicy state; evidence records | M4 |
| AC-11 | A customer sees their own workloads' level, each rule's status, basis, enforcement state and last-checked time, with control-operating statuses labelled as such, and nothing about other tenants or node names | FR-14 | API test (console check if shipped) | M4; MOE-1 |
| AC-12 | For every control in the catalogue, a compliance user retrieves the evidence records for a test period, and each record names the rules and checks behind it | FR-19, FR-20 | API test against the evidence store | M4 |
| AC-13 | With the check engine stopped, Level 1 rules become `unverified`, no new Level 1 placement is offered, and an operator alert fires | §12, NFR fail closed | Fault-injection test; alert | M1 |
| AC-14 | The generated level guide and console state, per rule, *enforced*, *monitored* or *off* for the current release, and state Level 1's shared control plane and residual risks; nothing describes Level 1 as a dedicated cluster | FR-22 | Docs build output; console check against the catalogue | M4; MOE-1 |
| AC-15 | A Level 1 deployment whose artefacts aren't staged, lack a provenance record, or whose digests don't match is not started (reason given); a staged, matching artefact loads | FR-23 | Integration test; deployment conditions; staging records | M2; MOE-1 |

**Success metrics** (ladder; baselines are "none today"; targets are postures to instrument):

1. **Level 1 delivered:** MOE-1 customers running on a compliant Level 1 pool. Baseline 0.
2. **Controls operating:** share of workload-rule-periods `held` (vs `not-held` or `unverified`). Posture: `not-held` at zero; `unverified` shrinking.
3. **Detection and response:** time from a fault to confirmation, quarantine and recovery, by severity. No baseline; instrument in Phase 1.
4. **Innocent-workload protection:** S2 faults resolved without stopping the protected workload. Baseline none.
5. **Exception discipline:** exceptions applied without a valid C authorisation (invariant: zero), and exceptions open past their window (zero).
6. **Attestation readiness:** share of controls in the catalogue with retrievable evidence for a full period. Baseline 0.

## 16. Dependencies

- **Row 47** ([[Minimum Operable Estate]] acceptance definition): gates E; it ratifies which controls MOE-1 requires.
- **A:** the declared level, pool labels and `AcceleratorClass.spec.tolerations` (A spec §3.3, §4.4), and the guard that executes stop or relocation under a severity-based containment policy (requested interface change, A4-6).
- **C:** authorisation of exceptions, enforcement of actions against E's rules, and the authority principal (Authority Context).
- **D:** the D-0 evidence envelope and store.
- **F:** staged artefacts with provenance and digests (FR-23; requested interface change).
- **B and Metering:** a sovereignty-level attribute on usage (D-6).
- **Dataplane:** an enforcing CNI on the AI cluster; GPU device-plugin configuration per node set; platform system pods that tolerate the dedication taint.
- **Security and legal:** validation of the rule set and severity policy (D-1, D-12). **Compliance workstream:** the attestation choice (D-2).
- **Depended on by:** A (Level 1 offers), C (rules to enforce), D (boundary evidence), I (B-2 signal), K (Level 2 builds on these rules).

## 17. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Customers or regulators require a dedicated cluster or install, not dedicated nodes | Residual risk stated up front (FR-22); kill criterion (§18); the sovereign install mode exists as a fallback topology, held to the same rules (PD-9) |
| Level 0 baseline sold as guarantees before it is enforced | Enforcement state per rule per release, generated from the catalogue (FR-22, AC-14) |
| Control-operating evidence read as proof that nothing leaked | Basis and "control operating" labels on every status (principle 5, FR-14) |
| An innocent customer's workload stopped because of someone else's pod | Severity-based containment: remove the cause first (S2), stop only at S1 (PD-4) |
| S2 leaves a protected workload co-resident for a while | Bounded removal deadline set by Security, then S1; customer told; window shown `not-held` (D-12) |
| A default-deny network fence breaks serving or fine-tuning | Level 1 first, where the allowed crossings are explicit; Level 0 behind a flag (FR-7); connectivity tests (AC-5, AC-6) |
| Platform DaemonSets don't tolerate the taint and GPU nodes lose drivers or monitoring | Named allowlist of system pods; join runbook verifies them before a node counts (L1-7) |
| Network policy silently inert on an unenforcing CNI | Enforcement probed live, not assumed; failure is S1 for Level 1 |
| Over-selling Level 1 to workloads that fit Level 0 | [[Sovereignty Levels]] fit table used in qualification |

## 18. Kill / Falsification Criterion

The bet is that **dedicated nodes in a shared, RackAI-operated cluster, with explicit rules, stated residual risk and evidence that the controls operated, are enough** for MOE-1 customers with proprietary or regulated data.

**Falsified if** either holds:
1. Security or legal review (D-1), or most MOE-1 prospects who need Level 1, reject dedicated nodes in a shared cluster as insufficient and require a dedicated cluster, a dedicated install or their own hardware, **and** that position persists after they have reviewed the rule set, residual risks and evidence; or
2. The attestation the MOE-1 segment requires (D-2) cannot be supported by these product controls without a dedicated install.

**Evidence:** D-1's review outcome, MOE-1 prospect and customer reviews, the reasons recorded when a Level 1 deal is lost, and the attestation scoping result.

**If falsified:** stop building shared-cluster Level 1; offer Level 1 as a dedicated install (the existing sovereign install topology) checked against the same rule set, and revisit [[Sovereignty Levels]] with the product owner. If prospects instead show they don't value Level 1 over Level 0, stop at the Level 0 baseline. The threshold ("most") is PD-11.

## 19. Open Decisions

| # | Decision | Owner | Blocks |
|---|----------|-------|--------|
| D-1 | Security and legal validation of the rule set and of dedicated-nodes-in-a-shared-cluster as Level 1 | Security; Legal | Selling Level 1 as available |
| D-2 | Which attestation the MOE-1 segment requires (type, framework, scope); retention needed for its observation period | Compliance workstream, with product owner | Control catalogue mapping (FR-19); retention (§13) |
| D-3 | May one dedicated node set serve several Organizations that share one **authority principal** (as resolved by C's Authority Context)? The isolation principal stays the Organization (PD-2) | Product owner, with C | Phase 2 sharing |
| D-4 | Do fine-tuning jobs of a Level 1 Organization have to run on Level 1 nodes? (A D-8, PD-8; with J) | Product owner, with J | Level 1 coverage of training data |
| D-5 | Which RackAI paths count as "customer runs code" and need a VM boundary (custom images, models that execute repository code, training scripts) | Security | Baseline rule set v2 |
| D-6 | Sovereignty level as a usage attribute, and how levels are priced | B owner, with Metering | FR-21 |
| D-7 | When the Level 0 network fence becomes default-on, and the allowed crossings for shared serving | Platform engineering, with product owner | FR-7 Phase 2 |
| D-8 | Is RXT-owned dedicated capacity in a partner facility eligible for Level 1? ([[Sovereignty Levels]] open question) | Product owner | Which nodes may join a set |
| D-9 | Promote *boundary rule* (and *boundary exception*) to a canonical note, since C and A consume them | Knowledge-graph steward | One-concept rule once C lands |
| D-10 | Row 47: ratify the MOE acceptance definition and which controls MOE-1 requires | Product owner | Phase 1 scope confirmation |
| D-11 | ~~Is a CustomerOrg always one customer? (conflict with C's D-9 / Q-14)~~ **Closed 2026-10-10 by the product owner's ruling X-1**: the Organization is the isolation principal (E); customer ownership is the authority principal, resolved by C. E no longer depends on the answer | — | — |
| D-12 | Security review of the severity classes, their examples and the S2 removal and S3 restore deadlines; in particular whether co-residency (S2) may continue for a bounded window or must be S1 | Security, with product owner | FR-11 values; MOE-1 |

## 20. Proposed Product Decisions

None is final until the product owner approves it.

| # | Decision | Alternatives considered | Why this one | Status |
|---|---|---|---|---|
| PD-1 | **Level 1 is a dedicated node set inside the shared AI cluster**: whole nodes, dedication taint, network fence, no co-tenancy. A dedicated cluster or install is not required. The shared control-plane boundary and residual risks are stated with every Level 1 offer (FR-22), and dedicated nodes are never equated with a dedicated cluster | Dedicated GPUs on shared nodes; a dedicated cluster; a dedicated install per customer | Whole GPUs on a shared node still leak ([[GPU Co-Tenancy Risk]]), so GPU-level dedication is too weak; a cluster or install per customer is costly and not what the evidence requires outside defence regimes. Residual risk (shared control plane) is the one [[Sovereignty Levels]] already states | proposed — conditionally approved in principle 2026-10-10 (PO review): condition (explicit shared control-plane boundary and residual risks) applied in v0.2 |
| PD-2 | **The Organization is the isolation principal**: a dedicated node set serves exactly one Organization. Customer ownership is resolved separately, by C's authority principal (Authority Context); E never infers it from an Organization, a CustomerOrg or the installation. Sharing a node set across Organizations of one authority principal is D-3 | Dedicate to the CustomerOrg; treat the installation as the customer | X-1: no customer can gain authority over another customer's workload through a shared parent; the isolation and authority principals are kept apart | proposed — revise (PO review 2026-10-10): Organization as isolation unit per X-1, ownership from C's authority principal; revised v0.2, pending approval |
| PD-3 | **Deny by default; exceptions are C authorisations of exceptable rules only**, bound to rule, scope, window and rule-set version, never standing. Level-defining rules are never excepted | Standing allowlists per customer; any rule exceptable | Keeps the C/E split clean, and keeps a level meaning the same thing for everyone | proposed — approved in principle 2026-10-10 (PO review) |
| PD-4 | **A confirmed failure stops new placements immediately and starts severity-based containment** (§12): quarantine the pool; remove the offending foreign pod when safe; stop or relocate the protected workload only when isolation can't otherwise be restored; fail closed (S1) where continuing would break a hard sovereignty guarantee. Recovery requires every rule `held` for a full cycle, plus recovery records and, for S1, security sign-off. Fed to A's containment policy as a requested interface change (A4-6) | Always stop the protected workload (v0.1); leave it running and alert only | An innocent customer's workload is not stopped because of another tenant's pod when the cause can be removed; a guarantee that can't hold is still never claimed | proposed — revise (PO review 2026-10-10): severity-based, security-reviewed containment with defined recovery; revised v0.2, pending approval |
| PD-5 | **Software-layer rules (B-1 to B-5) are the intended baseline at every level**; each release states which are enforced and which only monitored (§6) | Apply them at Level 1 only | The common breach paths are software ([[GPU Co-Tenancy Risk]]); [[Sovereignty Levels]] already conditions Level 0 on them | proposed — approved in principle 2026-10-10 (PO review); wording corrected in v0.2 to separate intent from enforcement |
| PD-6 | **A boundary status is `held` only with evidence for the period**; `unverified` is a separate status shown to customers; `held` means the control operated, not that no forbidden flow occurred | Report held unless a violation was seen | Principle 5; the evidence report must not over-claim | proposed — approved in principle 2026-10-10 (PO review) |
| PD-7 | **E delivers product controls and evidence, not the attestation.** Framework, auditor and scope belong to the compliance workstream | Pick SOC 2 Type I now and build to it | The roadmap row says the MOE-1 segment sets the attestation; controls are needed whichever is chosen | proposed — approved in principle 2026-10-10 (PO review) |
| PD-8 | **`executionType` keeps its meaning** (whether a model instance is shared). The sovereignty level is a separate usage attribute | Map Level 1 to `tenant-specific` | Every instance is already `tenant-specific`, so reusing it would label all Level 0 usage as dedicated | proposed — approved in principle 2026-10-10 (PO review) |
| PD-9 | **The sovereign install mode is a deployment topology, not a level.** It is checked against the same rules and earns no level on its own | Treat a sovereign install as Level 1 automatically | A level is a guarantee with evidence; a topology is not | proposed — approved in principle 2026-10-10 (PO review) |
| PD-10 | **Node join and scrub are human-operated in Phase 1**. Each join or scrub record names the human operator as its actor and is `asserted`; the system's evidence that cites it is `derived`, never `asserted`. Automation follows in Phase 2 | Automate from day one | Operate before automate; the basis is stated honestly | proposed — approved in principle 2026-10-10 (PO review) |
| PD-11 | **Falsification threshold "most"** for prospect rejection (§18), with no fixed percentage | A fixed percentage now | No baseline exists to set a number honestly | proposed — approved in principle 2026-10-10 (PO review) |

## See Also

- [[Sovereignty Levels]] — the canonical levels this PRD projects
- [[GPU Co-Tenancy Risk]] — the evidence behind the rules
- [[Verification Status Vocabulary]] · [[Failure Mode Taxonomy]] · [[Release Readiness States]] — shared status, failure and readiness terms
- [[Sovereign Isolation & Assurance Tech Spec]] — the engineering design
- [[Workload Declaration & Placement PRD]] · [[Workload Declaration & Placement Tech Spec]] — placement and containment to these rules
- [[Governed Execution & Delegated Authority PRD]] — authorisation, enforcement and the authority principal
- [[Customer Observability & Evidence Report PRD]] — the report the evidence feeds
- [[Model Lifecycle PRD]] — intake and staging that Level 1 requires
- [[Minimum Operable Estate]] · [[PRD Coverage Plan]] · [[AI Governance and Assurance]]
