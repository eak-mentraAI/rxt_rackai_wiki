---
id: prd-solution-marketplace
type: prd
status: draft
owner: rackai-product
domain: product
aliases: [solution marketplace prd, marketplace prd, packaged solution prd]
related: [ent-solution-marketplace, ent-packaged-solution, ev-sovereign-private-assistant, hub-eac-product-model, hub-ai-operations-product, hub-roadmap, wiki-milestone-release-map, idx-eight-layer-stack, hub-openrouter, hub-ai-governance-assurance]
source_docs: ["01-entities/Solution Marketplace.md", "01-entities/Packaged Solution.md", "00-hub/Enterprise AI Cloud Product Model.md", "00-hub/RackAI Roadmap.md", "PM/leadership marketplace discussion 2026-10-06"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-product
summary: "PRD for the Solution Marketplace: RackAI-owned rails where FDE-authored Packaged Solutions are published and consumed."
---

# Solution Marketplace — PRD

> **Artifact type: Product Requirements Document.** This is an authored product spec, not a knowledge-graph definition. The canonical concept lives in [[Solution Marketplace]] (and [[Packaged Solution]]); this PRD *projects* from them and must not re-define them. If they disagree, the canonical notes win and this PRD is stale.
>
> **Status: DRAFT PRD for a PROPOSED initiative.** Nothing in it is built. The marketplace, SDK, certification gate, isolation model, and metering/attribution are all `assumed` ([[Capability Gap Register]]). Requirements here express **intent, not commitments**; unresolved items are carried as **Open Decisions**, not invented specs. This document exists to make the initiative reviewable and to force the decisions that would let it be scoped and funded.

> **Scope line (read first).** This PRD specs the **rails** — the RackAI-owned platform and distribution machinery. It does **not** spec the solutions themselves; those are business logic authored by FDEs/partners/customers ([[Packaged Solution]]). Per the evolved [[Enterprise AI Cloud Product Model]] boundary, *RackAI owns the factory and the marketplace, not everything produced by the factory.*

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

**Non-Goals**
- **Authoring the solutions.** The solutions are business logic owned by FDE/partners/customers. RackAI builds the rails, not the catalog contents.
- **A public app store.** This is inward to RackAI customers, not arbitrary public traffic (that is OpenRouter's job).
- **Replacing Palantir/Uniphore-class application platforms.** Partner solutions are welcome *on* the rails; the rails are not an application platform ([[Three Battlegrounds]] refuse-to-compete line).
- **Billing/payment implementation.** Metering/attribution is in scope; the charge/payment mechanism is a known platform gap ([[Billing & Payment]]) and a dependency, not a deliverable of this PRD.
- **GPU-level exposure.** Solutions route via Model endpoints; the marketplace never exposes GPUs (initiative invariant).

## 4. Users & Personas

| Persona | Side | What they need |
|---------|------|----------------|
| **FDE author** (canonical first supplier) | Supply | A clear packaging standard + SDK; a predictable submission/certification path; confidence their solution will be isolated and attributable when it runs in a customer tenant |
| **Partner author** (later) | Supply | The same, plus commercial terms (rev-share) and a trust bar they can meet |
| **Customer author** (later) | Supply | Self-service authoring within their own estate, to the same standard |
| **Consuming customer** (RackAI tenant admin) | Demand | Discover certified solutions; instantiate into their estate with their own models/data; see consumption + cost |
| **Consuming end user** | Demand | Use the resulting experience (e.g. the private assistant) without touching the machinery |
| **RackAI product/governance owner** | Platform | Own the standard, the certification bar, the isolation model, and the metering — and keep "RackAI" from leaking into the solutions |

## 5. User Journeys / Scenarios

**Author journey (FDE):** build a solution to the Solution SDK standard → submit to the marketplace → pass the certification/isolation gate → published to the catalog → maintained/versioned.

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
| FR-3 | The runtime MUST enforce the manifest — a solution MUST NOT exceed the models/data/network/tools/secrets/identity it declared. | MUST | Enforcement side of the contract |

**Solution SDK & packaging standard**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-4 | The SDK MUST define an admissible [[Packaged Solution]] = harness pattern + skills/tools + model/data bindings (per policy) + the manifest + packaging metadata (author identity, version, instantiation parameters). | MUST | The unit from [[Packaged Solution]]; exact minimum contract = Open Decision **D-0** |
| FR-5 | The SDK SHOULD make a solution "RackAI-aware" (discovers endpoints, identity, metering hooks) without the author wiring platform internals. | SHOULD | |
| FR-6 | The SDK MAY extend the existing P2 product surface (API/SDK/console) rather than being a separate kit. | MAY | Open Decision D-3 |

**Two-layer trust: package certification + instantiation validation**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-7 | The marketplace MUST provide a submission workflow taking an authored solution through review to a published catalog listing. | MUST | Lifecycle below |
| FR-8 | **Package certification** — the solution *artifact* MUST pass a certification bar (signed, policy-compliant, declares its manifest correctly, does not violate platform boundaries) before listing. | MUST | Bar contents = D-2 |
| FR-8a | **Instantiation validation** — each *instantiation* (this solution + these model/data bindings + this estate config) MUST be validated against the **target estate's policy and compatibility** before it runs. | MUST | The thing "certified once" misses; per-estate |
| FR-9 | Both certification and instantiation validation MUST produce attestable records (what was checked, against what, by whom, when). | MUST | Feeds compliance evidence |

**Catalog, discovery & instantiation**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-10 | Customers MUST be able to discover certified solutions and see each solution's **manifest** (what it requires and will do) before instantiating. | MUST | Informed consent via the manifest |
| FR-11 | Instantiation MUST honor each dependency's **binding policy**: let the customer bind their own models/corpus where the policy is *customer-bindable*, select within declared constraints where *constrained*, and use the author's pinned choice where *fixed*. | MUST | Loosens the old FR-10; preserves sovereignty where it applies |
| FR-12 | An instantiated solution MUST run under a **scoped, attributable identity** and route into the serving chain via Model endpoints only. | MUST | [[Agent Identity]]; invariant |
| FR-13 | A Packaged Solution MUST support **repeatable instantiation across compatible estates** using declared per-estate parameters, **without modification to the packaged artifact**. | MUST | *The* leverage mechanism — if it isn't repeatably instantiable without editing the package, it doesn't satisfy the marketplace thesis |

**Solution lifecycle & maintenance**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-14 | Every Packaged Solution MUST be **versioned independently of its instantiated instances**. | MUST | Publication ≠ mutating running instances |
| FR-15 | The marketplace MUST track **which solution version each estate is running**. | MUST | |
| FR-16 | The platform MUST validate **solution-version ↔ platform/RackAI-version compatibility** before upgrade or instantiation. | MUST | |
| FR-17 | An author MUST be able to publish a replacement version **without automatically mutating existing instances**. | MUST | Author-controlled publish, not forced upgrade |
| FR-18 | **Platform security revocation** — RackAI MUST be able to **immediately prevent execution** of a solution/version (including **running instances**) when its certification/security integrity is invalidated. | MUST | The emergency stop; authority sits with RackAI platform/security |
| FR-18a | **Operational withdrawal / deprecation** — removing a solution for non-security reasons (author bug, EOL, customer-initiated) MUST follow a defined **notification + change-management policy**, not an immediate kill. | MUST | Distinct authority + process from FR-18; owned by the [[AI Operations Product]] responsibility model (who may stop a customer's production workload, and how) — ties to D-6 |
| FR-19 | A customer/admin SHOULD be able to **upgrade or roll back** an instantiated solution within supported compatibility bounds. | SHOULD | Upgrade behavior = Open Decision D-6 (auto / admin-approved / author-controlled) |
| FR-20 | The marketplace MUST define a **deprecation / EOL** state and surface it to affected tenants. | MUST | |
| FR-21 | The platform MUST define behavior when a solution's **required model is retired** (block instantiation, warn running instances, suggest a substitute per binding policy). | MUST | Ties to model [[#10. Dependencies|lifecycle]] |

**Metering & attribution**
| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-22 | Every solution's consumption MUST be metered and attributable to (solution, version, author, consuming tenant). | MUST | Feeds [[Metering]] + commercial model |
| FR-23 | Metering output MUST feed the [[Empirical Map]] as harness×model workload telemetry. | MUST | The moat linkage |
| FR-24 | The system SHOULD support an author-attribution record sufficient for a future rev-share model. | SHOULD | Commercial model = Open Decision D-1 |

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
| **MK.S0 — Reference implementation / learning prototype** | FDE builds [[Sovereign Private Assistant]] with the *smallest possible* packaging convention; instrument what is common vs. bespoke. **No generic SDK yet.** | discovers D-0; proves the manifest + binding shapes in the small |
| **MK.S1 — Extract the Solution Standard** | Turn S0's lessons into the SDK + manifest contract + binding-policy model | FR-1–6 |
| **MK.S2 — Two-layer trust gate** | Package certification + instantiation validation; isolation bar; a third-party solution can run safely in a tenant | FR-7–9, NFR isolation |
| **MK.S3 — Lifecycle & second reference solution** | Versioning, upgrade/rollback, revocation, EOL; prove re-instantiation on a *second* estate/solution | FR-14–21; tests re-instantiation + FDE delivery leverage |
| **MK.S4 — Marketplace surface + catalog** | Discovery, instantiation, metering/attribution | FR-10–13, FR-22–24 |
| **MK.S5 — Third-party / partner / customer authoring** | Open the standard beyond FDE once the trust bar + lifecycle are proven | all + D-1 |

> **Note:** this renumbers the release-map stages (previously MK.S1 = SDK). The [[Milestone Release Map]] has been updated to match (S0 prototype-first). The old "SDK → certification → reference solution" order is explicitly reversed.

## 9. Success Metrics

Baselines are **zero/none today** (nothing built). Targets are the *posture* to instrument, not asserted values. A single ratio is Goodhart-fragile (one solution instantiated 100 times but barely used would look great), so use a **ladder** — authoring leverage, adoption, real consumption, and the delivery-cost test that actually proves the §2 hypothesis.

| Rung | Metric | Baseline | What good looks like |
|------|--------|:--------:|----------------------|
| **Marketplace leverage** | **production** solution instances ÷ distinct solutions authored | n/a | >1 and rising — authored-once / used-many, counting only instances actually in production |
| **Marketplace adoption** | % of eligible estates running ≥1 marketplace solution | 0% | rising — the surface is actually reached for |
| **Marketplace consumption** | inference/token/workload consumption attributable to marketplace solutions | 0 | material and growing — instances are *used*, not shelf-ware |
| **FDE delivery leverage** ⭐ | median FDE engineering hours to deploy an existing Packaged Solution into an *additional* estate vs. the first deployment | n/a | second estate materially cheaper/faster than the first — **this is the direct test of the §2 hypothesis** |
| **Operating leverage** | **workloads per operations FTE** ([[AI Operations Product]]) | per AIOps | rising downstream — the operating-scale effect, distinct from delivery effort |
| **Moat instrumentation** | % of solution instantiations feeding the [[Empirical Map]] | 0% | →100% |
| **Trust bar** | sovereign-tenant certification + instantiation-validation pass | none | a repeatable bar regulated buyers accept |

> **Why FDE delivery leverage is the headline.** The §2 thesis is not "we instantiated it twice" — it is "**the second customer was materially cheaper/faster to deliver than the first.**" The causal chain the ladder encodes: *author once → less FDE effort per additional deployment (delivery leverage) → more deployments (leverage/adoption) → more real usage (consumption) → more workloads → automation reduces Ops effort (operating leverage).* The old "workloads/FTE rises because solutions replace bespoke builds" conflated **delivery** effort (FDE build) with **operating** effort (Ops run); these are separated here.

## 10. Dependencies

- **RackAI core** — models, inference, runtime interfaces the solutions consume ([[Enterprise AI Cloud Product Model]] core).
- **Tenant isolation + governance** — the certification bar depends on [[AI Governance and Assurance]] and the multi-cluster isolation work ([[Multi-Cluster Governance Brief (Partner)]]).
- **Metering** — [[Metering]] must capture per-solution usage; **billing/payment** ([[Billing & Payment]]) is a separate, currently-missing capability that a rev-share model would need.
- **FDE motion** — FDE supplies the first authors and reference solutions; [[AI Operations Product]] defines the operating/handoff model for instantiated solutions (incl. the FR-18a withdrawal authority). The marketplace is the leverage mechanism for the FDE motion, not its owner.
- **Agent identity** — [[Agent Identity]] for scoped, attributable solution identities.
- **Object/file storage** — the corpus binding depends on the CODB Object Store decision ([[RackAI Roadmap]]).

## 11. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Solutions are mostly bespoke** → low re-instantiation, weak leverage | Prototype-first (MK.S0) then prove re-instantiation on a second solution/estate (MK.S3); measure **FDE delivery leverage** (§9) before investing in the full surface. Extract the SDK only after a solution proves reusable |
| **A third-party solution breaches tenant isolation** → sovereign credibility destroyed | Isolation is a MUST NFR and a certification gate; do not open third-party authoring (MK.S5) until the bar is proven on FDE solutions |
| **"RackAI" leaks into owning the solutions** → collides with Palantir/partners, blurs the boundary | Hold the boundary: rails = RackAI, solution logic = author's ([[Enterprise AI Cloud Product Model]], [[Three Battlegrounds]]) |
| **No commercial model** → authors have no incentive; consumption not monetized | Resolve D-1 before MK.S5; metering/attribution (FR-13–15) is built to support whatever model is chosen |
| **Marketplace becomes its own product strategy** → distracts from the operator identity | Keep it subordinate, like OpenRouter — it is a consumption *channel* feeding the loop, not the destination ([[RackAI Roadmap]]) |

## 12. Kill / Falsification Criterion

If, after 1–2 reference solutions, the re-instantiation ratio stays ~1 (every customer needs a bespoke build anyway), the marketplace's leverage thesis is wrong and it should not receive disproportionate investment — the same shape as the Empirical Map's K2 test.

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

## See Also

- [[Solution Marketplace]] — the canonical concept this PRD builds on
- [[Packaged Solution]] — the unit being specced around
- [[Sovereign Private Assistant]] — the worked reference solution
- [[Enterprise AI Cloud Product Model]] — the RackAI boundary (core + rails) this sits inside
- [[AI Operations Product]] — the FDE motion + workloads/FTE lever
- [[RackAI Roadmap]] · [[Milestone Release Map]] — where the stages (MK.S1–S5) live
- [[Product Hub]]
