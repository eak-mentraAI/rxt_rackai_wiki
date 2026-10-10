---
id: prd-solution-marketplace
type: prd
status: draft
owner: rackai-product
domain: product
aliases: [solution marketplace prd, marketplace prd, packaged solution prd]
related: [ent-solution-marketplace, ent-packaged-solution, ev-sovereign-private-assistant, hub-eac-product-model, hub-ai-operations-product, hub-roadmap, wiki-milestone-release-map, idx-eight-layer-stack, hub-openrouter, hub-ai-governance-assurance, hub-load-bearing-bets]
source_docs: ["01-entities/Solution Marketplace.md", "01-entities/Packaged Solution.md", "00-hub/Enterprise AI Cloud Product Model.md", "00-hub/RackAI Roadmap.md", "PM/leadership marketplace discussion 2026-10-06", "PM/FDE-perspective PRD review 2026-10-09"]
confidence: assumed
last_reviewed: 2026-10-09
parent: hub-product
summary: "PRD for the Solution Marketplace: RackAI-owned rails where FDE-authored Packaged Solutions are published and consumed."
---

# Solution Marketplace — PRD

| Field | Value |
|:--|:--|
| Version | v3 |
| Status | Draft |
| Owner | rackai-product |
| Date | 2026-10-09 |
| Roadmap items | Marketplace: reference implementation / learning prototype; Marketplace: extract the Solution Standard; Marketplace: two-layer trust gate; Marketplace: certification bar for sovereign tenants; Marketplace: lifecycle + second reference solution; Marketplace: surface + catalog; Marketplace: commercial model; Marketplace: third-party / partner / customer authoring |
| Tech spec(s) | not yet written |

> **Artifact type: Product Requirements Document.** This is an authored product spec, not a knowledge-graph definition. The canonical concept lives in [[Solution Marketplace]] (and [[Packaged Solution]]); this PRD *projects* from them and must not re-define them. If they disagree, the canonical notes win and this PRD is stale.
>
> **Status: DRAFT PRD for a PROPOSED initiative.** Nothing in it is built. The marketplace, SDK, certification gate, isolation model, and metering/attribution are all `assumed` ([[Capability Gap Register]]). Requirements here express **intent, not commitments**; unresolved items are carried as **Open Decisions**, not invented specs. This document exists to make the initiative reviewable and to force the decisions that would let it be scoped and funded.

> **Scope line (read first).** This PRD specs the **rails** — the RackAI-owned platform and distribution machinery. It does **not** spec the solutions themselves; those are business logic authored by FDEs/partners/customers ([[Packaged Solution]]). Per the evolved [[Enterprise AI Cloud Product Model]] boundary, *RackAI owns the factory and the marketplace, not everything produced by the factory.*

> **Design stance toward FDEs (v3).** *We are not asking FDEs to change how they invent solutions. We are removing the repetitive work needed to turn a successful solution into something we can deliver safely, repeatedly, and economically across customers.* The rails must feel like an **accelerator**, not a framework FDEs have to conform to. Experimenting should be easy. Production trust boundaries are never optional (§5 operating modes).

## 1. Summary

The Solution Marketplace is a RackAI-owned **consumption surface** on which **Packaged Solutions** — agents, apps, and harnesses that serve a specific outcome — are published, certified, instantiated across customer estates, and metered. Its users are two-sided: **solution authors** (FDEs first, then partners and customers) who build to a RackAI standard, and **RackAI customers** who discover and instantiate those solutions. Its purpose is to **drive consumption of the platform**: a solution authored once can be instantiated across many estates, so demand grows without engineering effort growing linearly with it. It is the **second consumption channel** after the [[OpenRouter Initiative|OpenRouter channel]].

> **The proposition, stated precisely:** *package once, **certify the reusable artifact** once, and **validate each instantiation** against the target estate's policy and compatibility.* "Certified once, run anywhere" is too strong — because each instantiation binds a customer's own models and data (per their [[#Binding policy|binding policy]]), so a two-layer trust model is required: **package certification** (the artifact is trusted) + **instantiation validation** (this solution + these bindings + this estate is valid). See FR-8/FR-8a.

## 2. Problem / Opportunity

**Today.** Every customer-specific solution Rackspace delivers is a bespoke engagement. FDE work does not compound: an assistant or agent built for customer A is not readily reusable for customer B, so delivery cost scales roughly linearly with customers. There is no standard way to package, certify, distribute, or meter a solution built on RackAI — so the operator business has no demand-side flywheel, only a supply-side labor model.

**The opportunity.** If FDE output can be **packaged to a standard, certified as a reusable artifact, and safely validated and instantiated across many estates**, three things happen: (1) consumption of the RackAI platform is pulled through by ready-made outcomes rather than requiring every customer to build from scratch; (2) FDE leverage rises — the **workloads-per-operations-FTE** north-star ([[AI Operations Product]]) improves; (3) each instantiation becomes a [[Empirical Map|harness×model workload]] that feeds the moat. The marketplace is the mechanism that turns bespoke delivery into a compounding product.

**Hypothesis (not yet evidenced).** Enough solution shapes are **common across customers** (e.g. a private assistant over a corpus — [[Sovereign Private Assistant]]) that re-instantiation beats re-building. If almost every solution turns out to be fully bespoke, the marketplace's leverage is weak — see Risks.

## 3. Goals & Non-Goals

**Goals**
- Make an FDE-authored solution **re-instantiable across estates** without re-engineering per customer.
- **Drive platform consumption** via ready-made outcomes (demand side of Proof 4 — *Operate at Scale*).
- Let a **third-party-authored** solution run **safely inside a (sovereign) tenant** — the trust/isolation bar is the thing that makes the marketplace credible for regulated buyers.
- Raise **workloads/operations-FTE** by making delivery compound.
- Feed the [[Empirical Map]] with cross-workload telemetry from solution runs.
- **Make FDE delivery faster, not slower.** Deployment, identity, model access, customer isolation, observability, and reuse should be easier on the rails than without them. If not, FDEs will route around the rails.

**Non-Goals**
- **Productizing every engagement.** Experiments and one-off customer deployments do not have to be packaged or certified. A solution is packaged only once its reuse is justified (§5 operating modes).
- **Dictating the authoring framework.** FDEs keep their preferred frameworks, libraries, and tools. The SDK sets only the minimum integration points (FR-5a).
- **A full application-development platform.** The rails cover deploy, govern, operate, and scale. They are not an IDE, an agent framework, or a build system.
- **Authoring the solutions.** The solutions are business logic owned by FDE/partners/customers. RackAI builds the rails, not the catalog contents.
- **A public app store.** This is inward to RackAI customers, not arbitrary public traffic (that is OpenRouter's job).
- **Replacing Palantir/Uniphore-class application platforms.** Partner solutions are welcome *on* the rails; the rails are not an application platform ([[Three Battlegrounds]] refuse-to-compete line).
- **Billing/payment implementation.** Metering/attribution is in scope; the charge/payment mechanism is a known platform gap ([[Billing & Payment]]) and a dependency, not a deliverable of this PRD.
- **GPU-level exposure.** Solutions route via Model endpoints; the marketplace never exposes GPUs (initiative invariant).

## 4. Users & Personas

| Persona | Side | What they need |
|---------|------|----------------|
| **FDE author** (canonical first supplier) | Supply | Freedom to build with their own tools. A real dev/test/debug loop in a customer-like sandbox. A low-ceremony path from experiment to customer deployment to package. A manifest that is generated for them, not hand-written. A clear handoff to operations once they move to another engagement. Confidence that the solution will be isolated and attributable in a customer tenant |
| **Partner author** (later) | Supply | The same, plus commercial terms (rev-share) and a trust bar they can meet |
| **Customer author** (later) | Supply | Self-service authoring within their own estate, to the same standard |
| **Consuming customer** (RackAI tenant admin) | Demand | Discover certified solutions; instantiate into their estate with their own models/data; see consumption + cost |
| **Consuming end user** | Demand | Use the resulting experience (e.g. the private assistant) without touching the machinery |
| **RackAI product/governance owner** | Platform | Own the standard, the certification bar, the isolation model, and the metering — and keep "RackAI" from leaking into the solutions |

## 5. User Journeys / Scenarios

### Operating modes

The same rails support three ways of working. They are **not** three products or forced release stages. A solution moves to the next mode only when there is a reason to.

| Mode | Purpose | What the rails require | Marketplace certification? |
|------|---------|------------------------|:--------------------------:|
| **Experiment** | Find out whether something works | Minimal friction. Runs in a controlled sandbox with no customer production data unless approved | No |
| **Customer deployment** | Deliver a real outcome for one customer | Production security, scoped identity, isolation, default-deny inside the estate, and observability. Operational controls apply | No (estate-level validation only, FR-9a) |
| **Reusable Packaged Solution** | Distribute across estates | The full packaging contract: manifest, package certification, versioning, lifecycle (FR-1–24) | Yes |

### FDE developer workflow

The SDK (FR-4–6b) is accountable for this **whole** workflow, not just the packaging step:

1. **Build** with the FDE's preferred framework, libraries, models, and integrations (FR-5a).
2. **Test** in a customer-like sandbox with real identity, data access, model endpoints, logs, and traces (FR-6a).
3. **Package** once reuse is proven: generate the manifest from the solution's dependencies and config, review it, and validate it (FR-1a, FR-6b).
4. **Deploy** into another estate: bind customer-specific dependencies and parameters, validate, launch (FR-8a, FR-11, FR-13a).
5. **Operate and improve**: diagnose failures, ship new versions, and hand off operations (FR-14–21, FR-18b).

**Author journey (FDE, reusable path):** experiment → customer deployment → reuse is justified → package (generated manifest) → submit → pass package certification → published → maintained/versioned under a named maintaining owner (FR-18b).

**Consume journey (customer):** browse the catalog → pick a certified solution (e.g. [[Sovereign Private Assistant]]) → instantiate into the estate, binding *their* corpus (private storage) and *their* sovereign models → the solution runs under a scoped identity, isolated, metered → the admin sees consumption and cost.

**Worked example — Sovereign Private Assistant.** An FDE packages a RackAI-aware private ChatGPT over a corpus in private Rackspace storage, using the customer's sovereign models (answering alpha-leakage concerns). It is certified for sovereign-tenant isolation, published, and instantiated by multiple regulated customers — each binding their own corpus and models. One authored solution, many estates. Full example: [[Sovereign Private Assistant]].

## 6. Functional Requirements

Grouped by rail. **MUST / SHOULD / MAY.** Unresolved items point to Open Decisions (§13).

> **The central primitive: the Capability/Permission Manifest.** Before the groups below, note the one artifact they all hinge on. A Packaged Solution MUST ship a **manifest** declaring everything it needs and does. The manifest is the **contract that connects SDK → certification → customer approval → runtime enforcement → audit** — authored against the SDK, checked at certification, surfaced for customer approval at instantiation, enforced at runtime, and recorded for audit. It is likely the single most important thing to get right. What a manifest declares:
>
> | Facet | Declares |
> |-------|----------|
> | **Models** | Which model endpoints/classes it calls, and the **binding policy** per dependency (fixed / constrained / bindable — see below) |
> | **Data** | Which storage/data classes it reads/writes; corpus binding policy |
> | **Network** | Outbound destinations, if any (default none) |
> | **Tools / actions** | APIs/actions it invokes |
> | **Secrets** | Credentials/scopes it requires |
> | **Resources** | Compute/runtime requirements |
> | **Identity** | The scopes it needs to run under |
> | **Telemetry** | What it emits (feeds the two observability surfaces + the Map) |
>
> **Default-deny invariant (a defining principle of the marketplace).** *A Packaged Solution receives no access to models, data, tools, secrets, network destinations, or actions unless explicitly declared in its manifest and approved for the target estate.* Anything undeclared is denied. This gives the whole marketplace one coherent security model — **declare → certify → approve → enforce → audit** — and makes the manifest the single surface a customer reviews before trusting a solution in their estate.

**Capability / permission manifest (the primitive)**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-1 | Every [[Packaged Solution]] MUST ship a **capability/permission manifest** declaring models, data, network, tools/actions, secrets, resources, identity scopes, and telemetry (the facets above). | MUST | The contract linking SDK→cert→approval→enforcement→audit |
| FR-2 | The manifest MUST declare, per model and per data/corpus dependency, a **binding policy**: **fixed** (must use this exact model/source), **constrained** (any model/source satisfying a declared capability/class), or **customer-bindable** (customer chooses from approved options). | MUST | Replaces the old "always bind your own" assumption; see Binding policy |
| FR-1a | The manifest SHOULD be **mostly generated** from the solution's code, dependencies, and config. The author reviews it and fills in only what can't be discovered automatically. A validation tool SHOULD flag access the solution uses but has not declared before submission. | SHOULD | Design objective: keep security compliance from turning into a paperwork exercise. Default-deny still holds whether the manifest is generated or hand-written |
| FR-3 | The runtime MUST enforce the manifest — a solution MUST NOT exceed the models/data/network/tools/secrets/identity it declared. | MUST | Enforcement side of the contract |
| FR-3a | When a solution needs something the rails don't natively support (an external API, a partner platform, an unsupported tool), there MUST be an **extension path**: declare it as an external integration in the manifest (network, secrets, tools facets) and have it approved for the estate. Anything beyond that goes through a defined **exception process** with a named owner. | MUST | Prevents "unsupported" from meaning "blocked". Exception process owner and scope = D-9 |

**Solution SDK & packaging standard**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-4 | The SDK MUST define an admissible [[Packaged Solution]] = harness pattern + skills/tools + model/data bindings (per policy) + the manifest + packaging metadata (author identity, version, instantiation parameters). | MUST | The unit from [[Packaged Solution]]; exact minimum contract = Open Decision **D-0** |
| FR-5 | The SDK SHOULD make a solution "RackAI-aware" (discovers endpoints, identity, metering hooks) without the author wiring platform internals. | SHOULD | |
| FR-5a | The SDK MUST be **framework-agnostic**. It defines the **minimum integration points** (identity, model-endpoint access, telemetry, manifest) and MUST NOT require a specific agent framework, language, or library. | MUST | FDEs keep their tools; the rails plug in at the edges |
| FR-6 | The SDK MAY extend the existing P2 product surface (API/SDK/console) rather than being a separate kit. | MAY | Open Decision D-3 |
| FR-6a | Authors MUST have a **dev/test loop** against a customer-like sandbox: scoped identity, representative data access, real model endpoints, logs, traces, and debugging. This loop MUST be available before any packaging. | MUST | The Experiment-mode substrate (§5) |
| FR-6b | A solution MUST be able to move **experiment → customer deployment → Packaged Solution** without a rewrite. Each step adds controls (estate validation, then the full packaging contract); none requires re-platforming. | MUST | Packaging is a promotion, not a port |

**Two-layer trust: package certification + instantiation validation**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-7 | The marketplace MUST provide a submission workflow taking an authored solution through review to a published catalog listing. | MUST | Lifecycle below |
| FR-8 | **Package certification** — the solution *artifact* MUST pass a certification bar (signed, policy-compliant, declares its manifest correctly, does not violate platform boundaries) before listing. | MUST | Bar contents = D-2 |
| FR-8a | **Instantiation validation** — each *instantiation* (this solution + these model/data bindings + this estate config) MUST be validated against the **target estate's policy and compatibility** before it runs. | MUST | The thing "certified once" misses; per-estate |
| FR-9 | Both certification and instantiation validation MUST produce attestable records (what was checked, against what, by whom, when). | MUST | Feeds compliance evidence |
| FR-9a | **Package certification (FR-8) gates only reusable publication.** Experiments and single-customer deployments MUST NOT wait on marketplace certification. Customer deployments MUST still pass estate-level validation (identity, isolation, default-deny, observability) before they run in production. | MUST | Keeps certification off the customer-delivery critical path without making trust boundaries optional |

**Catalog, discovery & instantiation**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-10 | Customers MUST be able to discover certified solutions and see each solution's **manifest** (what it requires and will do) before instantiating. | MUST | Informed consent via the manifest |
| FR-11 | Instantiation MUST honor each dependency's **binding policy**: let the customer bind their own models/corpus where the policy is *customer-bindable*, select within declared constraints where *constrained*, and use the author's pinned choice where *fixed*. | MUST | Loosens the old FR-10; preserves sovereignty where it applies |
| FR-12 | An instantiated solution MUST run under a **scoped, attributable identity** and route into the serving chain via Model endpoints only. | MUST | [[Agent Identity]]; invariant |
| FR-13 | A Packaged Solution MUST support **repeatable instantiation across compatible estates** using declared per-estate parameters, **without modification to the packaged artifact**. | MUST | *The* leverage mechanism — if it isn't repeatably instantiable without editing the package, it doesn't satisfy the marketplace thesis |
| FR-13a | **Customization without forking.** Per-customer differences MUST be expressed through (a) declared configuration parameters, (b) declared **extension points**, or (c) customer-specific logic kept in an **estate-scoped extension layer** outside the shared artifact. Changing the shared artifact itself creates a **fork**: a new solution lineage with its own version history and maintaining owner (FR-18b). | MUST | Lets FR-13 hold as customers diverge. Extension-point contract = part of D-0 |

**Solution lifecycle & maintenance**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-14 | Every Packaged Solution MUST be **versioned independently of its instantiated instances**. | MUST | Publication ≠ mutating running instances |
| FR-15 | The marketplace MUST track **which solution version each estate is running**. | MUST | |
| FR-16 | The platform MUST validate **solution-version ↔ platform/RackAI-version compatibility** before upgrade or instantiation. | MUST | |
| FR-17 | An author MUST be able to publish a replacement version **without automatically mutating existing instances**. | MUST | Author-controlled publish, not forced upgrade |
| FR-18 | **Platform security revocation** — RackAI MUST be able to **immediately prevent execution** of a solution/version (including **running instances**) when its certification/security integrity is invalidated. | MUST | The emergency stop; authority sits with RackAI platform/security |
| FR-18a | **Operational withdrawal / deprecation** — removing a solution for non-security reasons (author bug, EOL, customer-initiated) MUST follow a defined **notification + change-management policy**, not an immediate kill. | MUST | Distinct authority + process from FR-18; owned by the [[AI Operations Product]] responsibility model (who may stop a customer's production workload, and how) — ties to D-6 |
| FR-18b | **Operating contract and handoff.** Every published solution MUST name a **maintaining owner** that survives the original FDE moving to another engagement. Each solution MUST also carry a responsibility split for: application defects, platform defects, dependency failures (for example, a breaking change in an external API), security incidents, and version maintenance / upgrade coordination across estates. | MUST | FDEs need this settled before they agree to produce reusable solutions. Proposed default split below; final matrix = D-7 |
| FR-19 | A customer/admin SHOULD be able to **upgrade or roll back** an instantiated solution within supported compatibility bounds. | SHOULD | Upgrade behavior = Open Decision D-6 (auto / admin-approved / author-controlled) |
| FR-20 | The marketplace MUST define a **deprecation / EOL** state and surface it to affected tenants. | MUST | |
| FR-21 | The platform MUST define behavior when a solution's **required model is retired** (block instantiation, warn running instances, suggest a substitute per binding policy). | MUST | Ties to model [[#10. Dependencies|lifecycle]] |

**Metering & attribution**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-22 | Every solution's consumption MUST be metered and attributable to (solution, version, author, consuming tenant). | MUST | Feeds [[Metering]] + commercial model |
| FR-23 | Metering output MUST feed the [[Empirical Map]] as harness×model workload telemetry. | MUST | The moat linkage |
| FR-24 | The system SHOULD support an author-attribution record sufficient for a future rev-share model. | SHOULD | Commercial model = Open Decision D-1 |

### Operating contract — proposed default split (FR-18b)

*Hypothesis for D-7, not a commitment.* **Worked case:** a solution runs in 12 estates and an external API it depends on changes, breaking it. Who diagnoses, fixes, approves, and rolls out the fix?

| Failure / duty | Diagnoses | Fixes | Approves new version | Coordinates rollout |
|----------------|-----------|-------|----------------------|---------------------|
| Application defect (solution logic) | AI Operations (first line) → maintaining owner | Maintaining owner | Package certification (FR-8) | AI Operations per FR-18a / D-6 |
| Platform defect (rails, runtime, identity) | AI Operations | RackAI platform | n/a (platform change) | RackAI platform |
| Dependency failure (external API, model retirement) | AI Operations | Maintaining owner (FR-21 for models) | Package certification | AI Operations |
| Security incident | RackAI platform/security | Maintaining owner + security | Security (FR-18 revocation if needed) | Security → AI Operations |
| Ongoing maintenance / upgrades | Maintaining owner | Maintaining owner | Package certification | AI Operations with tenant admins (D-6) |

The maintaining owner may be the authoring FDE team, a designated solution-maintenance function, or (later) a partner. Choosing which = D-7.

### Binding policy

A dependency (model or corpus/storage) is one of:

- **Fixed** — the solution requires a specific model/adapter/embedding or data source to function correctly; the customer cannot swap it.
- **Constrained** — any model/source satisfying a declared capability or [[Model Class|class]] is acceptable; the customer (or RackAI placement) chooses within that constraint.
- **Customer-bindable** — the customer binds their own (e.g. a sovereign model, their private corpus) — the [[Sovereign Private Assistant]] case.

This replaces the earlier "every instantiation binds the customer's own models and corpus" assumption, which over-constrained the product: some solutions need a specific fine-tuned model or embedding to work. The manifest (FR-2) carries the policy per dependency, so sovereignty is preserved where it matters without forcing it where it breaks the solution.

## 7. Non-Functional Requirements

- **Isolation (load-bearing):** a third-party-authored solution MUST NOT be able to cross the tenant boundary — read, exfiltrate, or affect data/models outside the estate it is instantiated in. This is the single most important NFR; it is what lets the marketplace be credible for sovereign/regulated buyers. Ties to [[Multi-Cluster Governance Brief (Partner)]] and [[AI Governance and Assurance]].
- **Sovereignty:** instantiation MUST keep the customer's corpus and models within their control boundary (no egress to author or to RackAI beyond what metering requires).
- **Provenance/audit:** certification records and solution-version provenance MUST be auditable.
- **Compatibility:** the platform MUST validate a solution's declared manifest + version against the estate before running it (FR-8a, FR-16).
- **Observability:** solution runs MUST surface the customer-observability metrics the consuming admin expects (requests, latency, cost) and the operator-intelligence that feeds the Map — the two surfaces from the roadmap's observability split.

## 8. Scope & Phasing

> **Prototype before standard (operate-before-automate).** The phasing is deliberately re-sequenced so we **build one genuinely reusable solution first, learn what makes it reusable, and only then extract the SDK/standard from those lessons** — rather than designing an elegant generic marketplace contract before we know what a reusable solution actually needs. This mirrors the corpus-wide ladder (bespoke → instrumented → repeatable → productized → automated) and the roadmap's "do not automate before we operate." It adds a new **MK.S0** ahead of the standard, and the exact package contract (**D-0**) is something S0/S1 *discovers*, not something assumed up front.

Phased per the [[Milestone Release Map]] capability stages. All stages are `assumed`/proposed; sequencing is mostly Proof 4, with S0–S1 able to start earlier as a proving ground.

| Stage | Scope | FRs |
|-------|-------|-----|
| **MK.S0 — Reference implementation / learning prototype** | FDE builds [[Sovereign Private Assistant]] with the *smallest possible* packaging convention, **using a realistic FDE workflow** (their own tools, a real customer-like environment), not a purpose-built demo. Record FDE hours and friction at each workflow step (§5). Instrument what is common vs. bespoke. **No generic SDK yet.** | discovers D-0; proves the manifest + binding shapes in the small; baselines FDE delivery effort |
| **MK.S1 — Extract the Solution Standard** | Turn S0's lessons into the SDK + manifest contract + binding-policy model, plus the dev/test loop, manifest generation, and the experiment → deployment → package promotion path | FR-1–6b |
| **MK.S2 — Two-layer trust gate** | Package certification + instantiation validation; isolation bar; a third-party solution can run safely in a tenant | FR-7–9a, NFR isolation |
| **MK.S3 — Lifecycle & second reference solution** | Versioning, upgrade/rollback, revocation, EOL, operating contract/handoff; prove re-instantiation on a *second* estate/solution | FR-14–21 (incl. FR-18b); tests re-instantiation + FDE delivery leverage |
| **MK.S4 — Marketplace surface + catalog** | Discovery, instantiation, customization without forking, metering/attribution | FR-10–13a, FR-22–24 |
| **MK.S5 — Third-party / partner / customer authoring** | Open the standard beyond FDE once the trust bar + lifecycle are proven | all + D-1 |

> **Note:** this renumbers the release-map stages (previously MK.S1 = SDK). The [[Milestone Release Map]] has been updated to match (S0 prototype-first). The old "SDK → certification → reference solution" order is explicitly reversed.

## 9. Success Metrics

Baselines are **zero/none today** (nothing built). Targets are the *posture* to instrument, not asserted values. A single ratio is Goodhart-fragile (one solution instantiated 100 times but barely used would look great), so use a **ladder** — authoring leverage, adoption, real consumption, and the delivery-cost test that actually proves the §2 hypothesis.

| Rung | Metric | Baseline | What good looks like |
|------|--------|:--------:|----------------------|
| **Marketplace leverage** | **production** solution instances ÷ distinct solutions authored | n/a | >1 and rising — authored-once / used-many, counting only instances actually in production |
| **Marketplace adoption** | % of eligible estates running ≥1 marketplace solution | 0% | rising — the surface is actually reached for |
| **Marketplace consumption** | inference/token/workload consumption attributable to marketplace solutions | 0 | material and growing — instances are *used*, not shelf-ware |
| **FDE delivery leverage** ⭐ | median FDE engineering hours to deploy an existing Packaged Solution into an *additional* estate vs. the first deployment, **including integration and customization work** (not just the instantiation step) | n/a | second estate materially cheaper/faster than the first — **this is the direct test of the §2 hypothesis** |
| **Authoring overhead** | FDE hours spent on packaging, manifest, and certification ÷ hours spent building the solution | none today (baselined at MK.S0) | low and falling — the rails must not become a process tax that FDEs route around |
| **Operating leverage** | **workloads per operations FTE** ([[AI Operations Product]]) | per AIOps | rising downstream — the operating-scale effect, distinct from delivery effort |
| **Moat instrumentation** | % of solution instantiations feeding the [[Empirical Map]] | 0% | →100% |
| **Trust bar** | sovereign-tenant certification + instantiation-validation pass | none | a repeatable bar regulated buyers accept |

> **Why FDE delivery leverage is the headline.** The §2 thesis is not "we instantiated it twice" — it is "**the second customer was materially cheaper/faster to deliver than the first.**" The causal chain the ladder encodes: *author once → less FDE effort per additional deployment (delivery leverage) → more deployments (leverage/adoption) → more real usage (consumption) → more workloads → automation reduces Ops effort (operating leverage).* The old "workloads/FTE rises because solutions replace bespoke builds" conflated **delivery** effort (FDE build) with **operating** effort (Ops run); these are separated here.

## 10. Dependencies

- **RackAI core** — models, inference, runtime interfaces the solutions consume ([[Enterprise AI Cloud Product Model]] core).
- **Tenant isolation + governance** — the certification bar depends on [[AI Governance and Assurance]] and the multi-cluster isolation work ([[Multi-Cluster Governance Brief (Partner)]]).
- **Metering** — [[Metering]] must capture per-solution usage; **billing/payment** ([[Billing & Payment]]) is a separate, currently-missing capability that a rev-share model would need.
- **FDE motion** — FDE supplies the first authors and reference solutions; [[AI Operations Product]] defines the operating/handoff model for instantiated solutions (incl. the FR-18a withdrawal authority and the FR-18b operating contract). The marketplace is the leverage mechanism for the FDE motion, not its owner. **FDE leadership review** of the developer workflow and operating modes (§5) is a precondition for MK.S0 scoping.
- **Partner platforms** — Palantir/Uniphore-class platforms appear on the rails as declared external integrations (FR-3a) unless D-8 decides otherwise ([[Load-Bearing Bets]], [[Three Battlegrounds]]).
- **Agent identity** — [[Agent Identity]] for scoped, attributable solution identities.
- **Object/file storage** — the corpus binding depends on the CODB Object Store decision ([[RackAI Roadmap]]).

## 11. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Solutions are mostly bespoke** → low re-instantiation, weak leverage | Prototype-first (MK.S0) then prove re-instantiation on a second solution/estate (MK.S3); measure **FDE delivery leverage** (§9) before investing in the full surface. Extract the SDK only after a solution proves reusable |
| **A third-party solution breaches tenant isolation** → sovereign credibility destroyed | Isolation is a MUST NFR and a certification gate; do not open third-party authoring (MK.S5) until the bar is proven on FDE solutions |
| **"RackAI" leaks into owning the solutions** → collides with Palantir/partners, blurs the boundary | Hold the boundary: rails = RackAI, solution logic = author's ([[Enterprise AI Cloud Product Model]], [[Three Battlegrounds]]) |
| **No commercial model** → authors have no incentive; consumption not monetized | Resolve D-1 before MK.S5; metering/attribution (FR-22–24) is built to support whatever model is chosen |
| **Marketplace becomes its own product strategy** → distracts from the operator identity | Keep it subordinate, like OpenRouter — it is a consumption *channel* feeding the loop, not the destination ([[RackAI Roadmap]]) |
| **Rails become a process tax** → FDEs route around them and leverage never materializes | Operating modes (§5): certification only for reusable publication (FR-9a). Framework-agnostic SDK (FR-5a), generated manifest (FR-1a), and the **authoring overhead** metric (§9) |
| **Orphaned solutions** → the authoring FDE rotates off and nobody owns failures across estates | Named maintaining owner + responsibility split (FR-18b, D-7) required before publication |
| **Customization sprawl** → every customer edits the package, turning one solution into N bespoke forks | FR-13a: config / extension points / estate-scoped extensions; editing the artifact is an explicit fork |

## 12. Kill / Falsification Criterion

After 1–2 reference solutions, the leverage thesis is wrong and the marketplace should not receive disproportionate investment if **either** test fails. This has the same shape as the Empirical Map's K2 test.

1. **Technical portability:** the re-instantiation ratio stays ~1, meaning every customer needs a bespoke build anyway.
2. **Effort saved:** the solution technically instantiates on a second estate, but **FDE delivery leverage** (§9, counting integration and customization work) shows no material reduction in hours versus the first deployment.

Portability without effort saved does not count as leverage.

## 13. Open Decisions

| # | Decision | Owner | Blocks |
|---|----------|-------|--------|
| **D-0** ⭐ | **What is the minimum reusable unit that qualifies as a Packaged Solution?** Code + config? Harness + tools + model requirements? A complete deployable workload? A template materialized into a customer-specific deployment? FR-4's definition is the current *hypothesis*; the real contract is what **MK.S0/S1 must discover**, not assume. Everything else depends on this. | RackAI Product | D-0 gates the SDK, certification, and the whole contract |
| **D-1** | Commercial model: author rev-share (FDE/partner/customer) vs. bundled into Outcome as a Service? | Product + Commercial | MK.S5; monetization |
| **D-2** | What exactly is the certification/trust bar (package certification *and* instantiation validation) for a third-party solution to run inside a sovereign tenant? | [[AI Governance and Assurance]] | MK.S2; all third-party authoring |
| **D-3** | Does the Solution SDK extend the existing P2 product surface (API/SDK/console) or is it a separate authoring kit? | RackAI Product | MK.S1 scope |
| **D-4** | Is the corpus binding a thin pointer to [[Dataset]] + Object Store, or its own packaging primitive? | RackAI Product | FR-11; MK.S1 |
| **D-5** | Sequencing: how early does MK.S0/S1 start as a proving ground vs. the full surface at Proof 4? | Product + Roadmap | phasing |
| **D-6** | Upgrade behavior for instantiated solutions: automatic, admin-approved, or author-controlled? | RackAI Product + [[AI Governance and Assurance]] | FR-19; lifecycle |
| **D-7** | **Operating contract:** who is the maintaining owner once the authoring FDE moves on (the FDE team, a solution-maintenance function, or a partner)? What is the final responsibility matrix (§6 proposed default)? | [[AI Operations Product]] + FDE leadership | FR-18b; publication of any reusable solution |
| **D-8** | **Partner-framework scope:** does the marketplace package agents/harnesses only (with Palantir/Uniphore-class apps as declared integrations), or can it also package integrations or external applications? | RackAI Product + Partnerships | FR-3a, FR-4; partner authoring (MK.S5) |
| **D-9** | **Exception process:** who approves capabilities the rails don't natively support, how fast, and when does a recurring exception become a supported integration? | RackAI Product + [[AI Governance and Assurance]] | FR-3a |

**Discovery input for D-0 (ask FDE leadership before MK.S0 is scoped):** *"If you built a successful customer solution today and needed to deploy it for five more customers, what work would you most want RackAI to take off your plate?"* The answer should shape MK.S0 and the SDK contract.

## 14. FDE Review Map

The questions FDEs are expected to ask, and where this PRD answers them (added v3, 2026-10-09):

| # | FDE question | Answered in |
|---|--------------|-------------|
| 1 | Why use this instead of my existing tools? | §3 goal "faster, not slower"; §5 workflow; FR-5, FR-6a |
| 2 | Do I have to build to your standard from day one? | §5 operating modes; FR-6b, FR-9a |
| 3 | How do I develop, test, and debug? | §5 workflow; FR-6a |
| 4 | What if I need something RackAI doesn't support? | FR-3a; D-9 |
| 5 | Does certification slow down customer delivery? | FR-9a; §5 operating modes |
| 6 | Who maintains my solution after I leave the engagement? | FR-18b + operating-contract table; D-7 |
| 7 | How do I customize a packaged solution for a new customer? | FR-13a |
| 8 | How does this work with Palantir, Uniphore, and other frameworks? | FR-5a, FR-3a; §10 partner platforms; D-8 |

## See Also

- [[Solution Marketplace]] — the canonical concept this PRD builds on
- [[Packaged Solution]] — the unit being specced around
- [[Sovereign Private Assistant]] — the worked reference solution
- [[Enterprise AI Cloud Product Model]] — the RackAI boundary (core + rails) this sits inside
- [[AI Operations Product]] — the FDE motion + workloads/FTE lever
- [[RackAI Roadmap]] · [[Milestone Release Map]] — where the stages (MK.S1–S5) live
- [[Product Hub]]
