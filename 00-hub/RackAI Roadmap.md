---
id: hub-roadmap
type: hub
status: draft
owner: product
domain: strategy
aliases: [rackai roadmap, canonical roadmap, living roadmap, roadmap hub, operator roadmap, engineering roadmap canonical, four proofs, observe decide control operate, proof roadmap]
related: [hub-root, hub-product, hub-battlegrounds, hub-load-bearing-bets, hub-minimum-operable-estate, hub-ai-operations-product, hub-enterprise-ai, hub-commercial, hub-governance, hub-evidence, src-engineering-roadmap, src-rackai-dev-plan, idx-openrouter-integration-plan, idx-capability-gap-register, ent-empirical-map, ent-governed-harness]
source_docs: ["06-sources/Rack AI OpenRouter Engineering Roadmap.md", "06-sources/RackAI Enterprise AI Development Plan.md", "05-wiki/OpenRouter Integration Plan.md", "04-evidence/Capability Gap Register.md", "00-hub/Three Battlegrounds.md"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-root
summary: "Canonical living roadmap: four proofs of the operator identity (Observe, Decide, Control, Operate)."
---

# RackAI Roadmap

The **single canonical, living roadmap** for RackAI. Unlike the two source narratives it draws from — the [[Rack AI OpenRouter Engineering Roadmap]] (`validated`, read-only) and the [[RackAI Enterprise AI Development Plan]] (`assumed`, raw projection) — **this note is editable and is where planning actually lives.** Those two remain sources; when a proposed change is accepted, it lands here first, and the sources are left intact per the truth hierarchy.

> **Confidence.** `derived` — this roadmap synthesizes two existing planning spines under the [[Three Battlegrounds|Private Enterprise AI Operator]] identity. Individual items carry the confidence of their source (phase/program/gap). Nothing here upgrades a capability to shipped; the live shipped-vs-planned state is the [[Capability Gap Register]].

## How to Read This Roadmap

- **North star** is the operator identity, not leaderboard rank. We are building *the best operator of heterogeneous enterprise AI estates*; OpenRouter competitiveness is a **learning vehicle inside** the operator roadmap, not its critical path ([[Three Battlegrounds]]).
- **The roadmap is organized around four progressive proofs**, not around inherited technical phases: **Observe → Decide → Control → Operate.** Each proof has an exit condition phrased as a claim about *operating an estate*. The two source spines — the [[Rack AI OpenRouter Engineering Roadmap]] (Phases 0–6) and the [[RackAI Enterprise AI Development Plan]] (Programs 1–5, P1–P9) — supply *items that map into these proofs*, but the proofs are the organizing logic.
- **Every item passes one test:** *does this make us materially better at operating a customer's AI estate?* ([[Three Battlegrounds]] strategic choice.)
- **The MVP is the [[Minimum Operable Estate]]**, not the full platform. We earn the word "Operator" by operating one estate, then ten, then automating what hurts.
- **Maturity principle:** every capability walks the ladder **human-operated → instrumented → assisted → automated** (see below). We do not automate before we operate.
- **Proofs are gates, not waterfall phases** (see the callout below the metrics). Later-proof work starts early where lead times or architecture require; we simply cannot *claim* a proof until its exit condition is met.
- **Change workflow:** propose in the "Proposed Changes" section → review → on acceptance, edit the proof/workstream tables and log a change packet in `08-change-control`.

## The Acid Test

> **Strategy:** Become the Private Enterprise AI Operator.
> **Roadmap:** Observe → Decide → Control → Operate.
> **Flywheel:** Every estate operated makes the next estate cheaper and better to operate.
> **Proof:** Start with one [[Minimum Operable Estate]] and progressively automate what we learn.

## North Star & Governing Metrics

The north star is **paired** to avoid Goodhart's law: workload count alone could be maximized by onboarding many trivial workloads into one friendly environment while proving nothing about enterprises delegating real responsibility. The strategy is to *operate estates*, not accumulate endpoints — so the count is anchored by estates and by economics.

| Role | Metric | Why |
|------|--------|-----|
| **Leading** | Production workloads under management | The count that turns identity into a number |
| **Strategic** | Production customer **estates** under management | Guards against "200 trivial workloads in one internal env" — estates prove delegation |
| **Scale** | **Workloads operated per operations FTE** | The signal this is software economics, not a labor business |
| **Economic** | Contribution margin per estate | Proves the operator business is attractive, not just functional |

Supporting families:

| Metric family | Metrics | Note |
|---------------|---------|------|
| **Economics** | Contribution margin / workload + / estate, cost / 1M tokens, GPU utilization, revenue / GPU-hour | Owned economics over abstracted supply |
| **Operational quality** | Availability, incident rate, MTTR, deployment time, model-launch time | The Engineering Roadmap efficiency KPIs live here |
| **Operator leverage** | Workloads per ops FTE, % of decisions automated/assisted | Bends the labor curve |
| **Flywheel** | % of workloads contributing transferable telemetry; **% of operating decisions informed by cross-workload empirical evidence** | The killer metric — this *is* the strategy; measures whether the moat is compounding across customers, not within one |
| **Control** | % of workload execution covered by policy / audit / governance controls | Measures whether we can operate inside an enterprise boundary |

**The dashboard we're building toward.** When the identity is real, it reads as numbers, not marketing — e.g. *42 customer estates · 317 production workloads · 8.4 workloads/Ops FTE · 71% of placement decisions Empirical-Map-informed · 43% lower inference cost vs. initial baseline · 99.95% availability · 47% contribution margin.* (Illustrative target, not current state.)

> **Confidence note.** These metrics are the *target* instrumentation; almost none are measurable today (no [[Benchmark Run]] or telemetry yet — [[Capability Gap Register]]). They are `assumed`/aspirational until Proof 1 lands the measurement primitives. The dashboard figures above are illustrative, not measured.

## Governing Principle — Human-Operated → Automated

Operating knowledge is *created by operating*, so every capability walks this ladder rather than starting automated. This both builds the [[Empirical Map]] and reduces speculative platform engineering.

| Capability | Human-operated | Instrumented | Assisted | Automated |
|-----------|----------------|--------------|----------|-----------|
| Placement | Human chooses model/hardware | Capture decision + result | Empirical Map recommends | Automated placement |
| Routing | Static routes | Instrument traffic | Rules + recommendation | Dynamic routing |
| Capacity | Manual assignment | Utilization visibility | Forecasting | Automated capacity mgmt |
| Governance | Manual policy approval | Encoded policy | Assisted review | Automated enforcement |

## The Four Proofs

Each proof is a horizon *and* a claim we can stand behind. Items trace to their source phase/program; the proof is what makes the item strategy-derived rather than inherited.

> **Proofs define progressive evidence, not sequential development phases.** Work on later proofs begins early where lead times or architectural dependencies require it — compliance, MOE design, identity/tenancy/isolation architecture, the operational-acceptance model, harness v1 design, and first design-partner selection all start during Proof 1. **We simply cannot *claim* a later proof until its exit condition is met.** Reading this as "finish Proof 1, then start Proof 2" would recreate the exact "operator-in-LATER" problem this structure was built to fix.

Each proof carries a **commercial gate** alongside its technical exit — because the strategy contains an economic claim (customers will pay Rackspace to assume operational responsibility) that no technical proof establishes on its own. Technical delegation and willingness to pay must be proven **together**.

| Proof | Commercial question it must also answer |
|-------|-----------------------------------------|
| 1 Observe | Can we quantify the economics? (cost model + pricing hypothesis) |
| 2 Decide | Can we quantify the customer improvement? ("this decision saved X / improved Y") |
| 3 Control | Will a customer delegate responsibility **and pay us**? (first paid MOE / design partner) |
| 4 Operate | Can we repeat it **profitably**? (multiple estates, repeatable SKU/boundary, positive contribution margin, workloads/FTE improving) |

### Proof 1 — Observe: *We can measure and operate AI*

> **Technical exit:** For a production model, Rackspace can **accurately measure** its cost, performance, utilization, reliability, and operational history **on the infrastructure we operate.** (Note: *where/how a workload runs best* is comparative intelligence — that is Proof 2, not Proof 1.)
> **Commercial gate:** we have a defensible cost model and a pricing hypothesis for operated workloads.

| Item | Traces to | Confidence |
|------|-----------|:----------:|
| Cost model (internal cost/GPU-hour) | Eng. 0.3; dev-plan Prog 5 | missing |
| Fleet telemetry instrumentation | Eng. 0.2 | missing |
| Initial benchmark harness | Eng. 0.4 | missing |
| Metering | Gap Register; dev-plan Prog 5.2 | planned |
| Basic reliability / observability | Eng. 2.2 / E | planned |
| GLM 5.3 Flash deployment + OpenRouter Path A (real workloads to exercise the system) | [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]]; [[OpenRouter Integration Plan]] Phase 1 | derived / planned |
| **Supply abstraction — the *interface*, not multi-provider scheduling** (`SupplyTarget / AcceleratorPool / ExecutionLocation`; owned H100 = impl #1) | Strategy-derived architectural requirement ([[Load-Bearing Bets]]) | assumed |
| Compliance envelope kickoff (SOC 2 scoping) | dev-plan **P1** ("start first") | missing |

*Why supply abstraction is here, not later: the abstraction is cheap now and expensive later. Building the control plane against `SupplyTarget` from day one prevents baking owned-fleet assumptions into everything. We do not need multi-provider scheduling yet — only the interface.*

### Proof 2 — Decide: *Our accumulated knowledge improves how we operate*

> **Technical exit (must beat a baseline):** Rackspace can demonstrate at least one placement, routing, model-selection, or configuration decision **informed by accumulated operating evidence** that materially improves an agreed workload KPI **versus a static/default baseline.** This prevents "we built an Empirical Map" from being mistaken for "the flywheel works."
> **Commercial gate:** we can quantify the customer improvement from that decision ("this saved X / improved Y").

| Item | Traces to | Confidence |
|------|-----------|:----------:|
| Empirical Map v1 + **transferable-vs-isolated telemetry model** | dev-plan 1.5; Eng. 3.11 + 6.6 | assumed |
| Placement intelligence (instrumented → assisted) | Eng. 1.5 → 5; ladder | planned |
| Smart-routing gateway (static → rules → recommendation) | Gap Register §4; Eng. 6.4 | planned |
| Performance engineering system | Eng. 3 | planned |
| Multi-model operation | Eng. 2.5 | planned |
| Fine-tuning **operations** (placement, cost-per-job, adapter lifecycle) | dev-plan 4.2; [[LoRA Adapter]] | measured (SFT) |
| Fine-tuning **experiment** — one instrumented domain-model proof point (central-bet test) | [[Three Battlegrounds]] central bet | measured (SFT) |

### Proof 3 — Control: *We can operate inside an enterprise boundary*

> **Technical exit:** Rackspace can take a real enterprise workload and operate it across an approved execution boundary while maintaining customer control, governance, and auditability. **This is the first actual proof of the company identity.**
> **Commercial gate:** a customer will delegate operational responsibility **and pay for it** — the first paid MOE / design partner.

**Two distinct milestones — do not conflate them:**

- **MOE-0 — Operator rehearsal (friendly/internal).** Build the operating model, runbooks, SLOs, incident process, telemetry, and operational-acceptance criteria on a friendly/internal estate. **Does not validate the market thesis** and must never be cited as "we've proven the operator model."
- **MOE-1 — Identity proof (external, regulated).** An external enterprise with a genuine private/control requirement that exercises the control boundary, customer delegation, *and* the commercial proposition. **MOE-1 is what actually satisfies Proof 3.** We have not proven the identity until a customer delegates responsibility and pays.

| Item | Traces to | Milestone | Confidence |
|------|-----------|-----------|:----------:|
| **[[Minimum Operable Estate]]** — the MVP operator target | Strategy-derived (this roadmap) | MOE-0 → MOE-1 | assumed |
| Governed execution harness **v1** (not the full runtime) | dev-plan Program 1 | MOE-0 | assumed |
| Identity / access | dev-plan 2.5; [[Agent Identity]] | MOE-0 | planned |
| Policy enforcement | dev-plan Program 2 | MOE-0 | assumed |
| Auditability | dev-plan P8/P9 | MOE-0 | planned |
| Customer isolation + private inference | [[Multi-Cluster Governance Brief (Partner)]] | MOE-1 | planned |
| Compliance controls (first attestation) | dev-plan P1 | MOE-1 | missing |
| Supply abstraction v1 (second impl: AMD or partner) | [[Load-Bearing Bets]] | MOE-1 | assumed |
| First **paid** private enterprise workload (delegation + willingness to pay) | Strategy-derived; [[AI Operations Product]] | MOE-1 | assumed |

### Proof 4 — Operate the Estate: *Customers can delegate the estate to us*

> **Technical exit:** A customer can give Rackspace operational responsibility for a heterogeneous production AI estate.
> **Commercial gate:** we can repeat it **profitably** — multiple estates, a repeatable SKU / service boundary, positive contribution margin per estate, and workloads/FTE improving.

| Item | Traces to | Confidence |
|------|-----------|:----------:|
| Multi-cluster governance / global front door | [[Multi-Cluster Governance Brief (Partner)]] | assumed |
| Heterogeneous supply (owned/partner/customer/hyperscaler) | [[Load-Bearing Bets]] capacity bet | assumed |
| Day-zero model factory | Eng. 4 | planned |
| Dynamic fleet & capacity mgmt | Eng. 5 | planned |
| Closed-loop optimization (automate what hurts) | Eng. 6 | planned |
| Governed harness (full runtime) | dev-plan Program 1 | assumed |
| Govern & assure inside the perimeter | dev-plan Program 2 | assumed |
| Managed operations + FDE motion | AI Operations Product workstream | not modeled |
| Operational leverage (workloads/FTE up and to the right) | North-star metric family | assumed |

## Workstream View

Cross-cutting owners run *vertically through all four proofs*. Mapped from the Engineering Roadmap's workstreams A–F plus the dev-plan programs — with **AI Operations Product** elevated to first-class, because if the identity is Operator, the operating model is part of the product, not an afterthought.

| Workstream | Owns | Source |
|-----------|------|--------|
| **[[AI Operations Product]]** | Operating model, service boundaries, SLOs, incident model, customer handoffs, FDE escalation, runbooks, lifecycle responsibility, change management, estate onboarding + operational acceptance criteria | **New — elevated from dev-plan P5/P6 + Product Operations JD** |
| Platform / Control Plane | Deployment orchestration, registry, capacity, routing, API, lifecycle, **supply-abstraction interface** | Eng. A |
| Inference Performance Eng | Runtime, kernels, quantization, caching, parallelism, topology | Eng. B |
| Model Enablement | Radar, intake, compatibility, functional testing, launches | Eng. C |
| GPU / Infra Eng | Clusters, networking, storage, topology, firmware, health | Eng. D |
| SRE / Reliability | Availability, observability, incident response, canary, rollback | Eng. E |
| FinOps / Economics | Cost/token, GPU-hour economics, revenue/GPU-hour, contribution margin | Eng. F; dev-plan Prog 5 |
| Harness & Orchestration | Execution harness, routing, context/tool controls, memory, runtime | dev-plan Program 1 |
| Governance & Assurance | Verification, perimeter info-flow, agent identity, **compliance envelope (P1)** | dev-plan Program 2 + P1 |
| Measurement & Self-Improvement | Empirical Map, eval-as-CI, loop planning, self-improvement | dev-plan Program 3 |

Vertically through all four proofs: **AI Operations Product + Compliance + Economics + Telemetry.**

## Open Roadmap Gaps

Seams where the strategy is still ahead of the plan, tracked for the "Proposed Changes" pipeline. Several earlier gaps are now placed by the four-proofs restructure (harness → Proof 3; supply-abstraction interface → Proof 1; transferable-vs-isolated telemetry → Proof 2; compliance → all proofs; operator KPIs → North Star; managed-ops/FDE → AI Operations Product workstream). Remaining open items:

1. **Minimum Operable Estate spec** — needs its own canonical note defining the smallest environment where "we operate your AI" is legitimately true (candidate: 1 customer, 1 private env, 2 models, 1 harness, 1 supply source, basic routing, metering, observability, identity/policy, audit, model lifecycle, human-operated placement).
2. **Operator KPI instrumentation** — the North-Star families are defined but unmeasured; Proof 1 must land them.
3. ~~**AI Operations Product** — elevated here, but has no canonical workstream/owner note yet.~~ **Closed** — canonical note created: [[AI Operations Product]] (staffing/ownership still open).
4. **Supply-abstraction interface spec** (`SupplyTarget / AcceleratorPool / ExecutionLocation`) — an architectural requirement without a design note.

## Proposed Changes (intake → review → adopt)

This is the working queue. Proposals are drafted, discussed, and — once accepted — folded into the horizon/workstream tables above with a change packet recorded. **Nothing here is adopted until moved up.**

| # | Proposed change | Affects | Status | Rationale |
|---|-----------------|---------|--------|-----------|
| **P-001** | Shift fine-tuning *delivery* to a partner (preferred: Uniphore); front-load operator-KPI enablers; protect a thin fine-tuning experiment | Proof 1/2; [[Load-Bearing Bets]]; Inference workstream | **Proposed** | Free the thin Inference pod to focus on what moves operator KPIs, without deferring the wedge experiment. See detail below. |
| **P-002** | Commit to a first [[Minimum Operable Estate]] as the concrete Proof 3 target, and name its first customer | Proof 3; [[Minimum Operable Estate]]; [[AI Operations Product]]; [[Load-Bearing Bets]] | **Proposed** | Turns "operator" from a claim into a dated deliverable; forces the operational-acceptance and boundary decisions early. See detail below. |

### P-001 — Fine-tuning: partner the delivery, keep the operations, protect the experiment

**Proposed by:** CEO/product discussion, 2026-09-21. **Status: Proposed — not adopted.**

**Problem.** "Should we push fine-tuning milestones to Uniphore and focus early effort on operator-KPI work?" The corpus shows the org already *intends* this — [[RackAI Organizational Design]]: "Fine-Tuning — No REQs required currently — will partner with Uniphore," and the Inference pod's fine-tuning line is `[0/1]` staffed. But "fine-tuning" is two things on opposite sides of the [[Three Battlegrounds|harness boundary]], so a blanket defer is wrong.

**The three-way split.**

| Bucket | Disposition | Rationale |
|--------|-------------|-----------|
| Fine-tuning *delivery* — customer-facing tuning service, data/context assembly, advanced methods (RL/DPO, still "Coming Soon" + unstaffed) | **Partner** (preferred partner: Uniphore, pending validation) | Business-logic-adjacent; "what customers build." Frees the `[2/8]` Inference pod. **Strategic decision is vendor-independent**; Uniphore is the implementation choice, not the strategy. |
| Fine-tuning *operations* — running tuning jobs efficiently: placement, utilization, cost-per-job, [[LoRA Adapter]] lifecycle on the fleet | **Keep — ours** | Squarely "what we operate"; feeds the [[Empirical Map]] as transferable operating knowledge. |
| Fine-tuning *as strategic experiment* — one domain-model proof point on customer/representative data | **Keep thin — do not zero** | This is the wedge and the **first test of the central strategic bet** ([[Three Battlegrounds]]). Deferring all fine-tuning would defer the proof the operator thesis is viable. |

**What front-loads instead (the operator-KPI enablers already in NOW/NEXT):** cost model (Eng. 0.3), telemetry (0.2), benchmark harness (0.4), metering, compliance-envelope kickoff (dev-plan P1). These move workloads-operated, cost-per-outcome, and compliance-coverage.

**Honest trade-off to weigh before adopting.** SFT is the one capability here that is **shipped and `measured`**; most operator-KPI enablers are `missing`/`planned`. So this proposal trades a working capability's roadmap weight for net-new build — the near-term plan gets *heavier*, not lighter. That can be right, but it should be a conscious choice.

**Dependency / open question (blocks adoption):** the corpus shows the *intent* to partner fine-tuning with Uniphore but not the **commercial/contractual scope** — whether Uniphore is signed to deliver customer fine-tuning as a service, or is only a production tenant (`uniphore.rackai.rax.io`) running its own apps. This determines whether P-001 is "defer to a committed partner" or "defer to a hoped-for partner." **Confirm before adopting.**

**Strategic decision (vendor-independent):** *partner fine-tuning delivery; retain fine-tuning operations and experimental capability.* The implementation decision — *preferred delivery partner: Uniphore, pending commercial/technical validation* — is separable, so the strategy does not depend on one vendor negotiation.

**On acceptance:** (1) move the operator-KPI enablers' priority up explicitly in Proof 1; (2) add "fine-tuning delivery" as a partner scope in [[Load-Bearing Bets]] (preferred: Uniphore, pending validation) with its own exit criterion; (3) keep one instrumented fine-tuning proof point in Proof 2 tied to the central-bet falsification test; (4) log a change packet.

### P-002 — Commit to a first Minimum Operable Estate

**Proposed by:** CEO/product discussion, 2026-09-21. **Status: Proposed — not adopted.**

**Problem.** Proof 3 (Control) is where "operator" stops being a claim and becomes a demonstrated fact, but the roadmap currently describes the [[Minimum Operable Estate]] only as a target shape. Without a *named first customer* and a *date*, Proof 3 stays abstract and the operator identity stays unproven. This proposal commits to one concrete MOE.

**What we'd commit to.** The v1 scope in [[Minimum Operable Estate]] (1 customer, 1 private environment, 2 models, 1 harness v1, 1 owned supply source behind the abstraction interface, basic routing, metering, observability, identity/policy, audit, human-operated placement) — operated to a defined SLO with a defined operational-acceptance gate ([[AI Operations Product]]).

**The first-customer choice (the key decision).** Two candidate paths, with a real trade-off:

| Path | Candidate | Pro | Con |
|------|-----------|-----|-----|
| **Internal / friendly** | An existing tenant estate (e.g. the Uniphore production tenant, `uniphore.rackai.rax.io`) | Lower contractual friction; faster to first operated estate; safe place to build runbooks | May not exercise the *regulated/sovereign* control boundary that is the actual identity test |
| **External / regulated** | A regulated design-partner customer | Tests the real compliance-envelope + control boundary; a genuine proof of the identity | Gated by the compliance envelope (Proof 1/3, `missing`), longer sales + attestation lead time |

**Recommendation to debate — two formally separate milestones:**

- **MOE-0 (Operator rehearsal):** internal/friendly estate; build the operating model and runbooks under the human→automated ladder. *Explicitly not the market/identity proof.*
- **MOE-1 (Identity proof):** external enterprise with a genuine private/control requirement, once the compliance envelope lands; exercises delegation **and willingness to pay.** MOE-1 is what satisfies Proof 3.

Keeping them separate prevents someone, six months out, from pointing at the friendly environment and declaring the operator model proven. We have not proven the identity until a customer delegates responsibility and pays.

**Dependencies / open questions (block adoption):**
- Ratify the MOE v1 scope and the operational-acceptance criteria ([[Minimum Operable Estate]], [[AI Operations Product]]).
- The internal-vs-external first-customer decision above.
- Minimum compliance attestation for a *real* (external, regulated) MOE — depends on the Proof 1 compliance-envelope kickoff.
- Interacts with **P-001**: the MOE's fine-tuning (if any) follows P-001's partner/ops/experiment split.

**On acceptance:** (1) name **MOE-0** (friendly estate + target date) and the **MOE-1** design-partner profile + target window as two dated Proof-3 deliverables; (2) task [[AI Operations Product]] with the operating model + operational-acceptance gate; (3) bind MOE-1 to the compliance-envelope milestone; (4) attach the commercial gate (delegation + willingness to pay) to MOE-1; (5) log a change packet.

**The four executive asks this proposal is meant to force** (the move from *executable strategy* — none are answered yet, all are open questions):

1. **MOE-0:** named friendly estate + target date.
2. **MOE-1:** named external design-partner profile/customer + target window.
3. **Proof gates:** measurable pass/fail criteria for Observe, Decide, Control, Operate.
4. **Commercial gates:** the evidence that customers will delegate this responsibility at economics that produce an attractive managed-service business.

## See Also

- [[Three Battlegrounds]] — the identity this roadmap serves
- [[Minimum Operable Estate]] — the MVP that anchors Proof 3
- [[Load-Bearing Bets]] — the partner portfolio behind it
- [[Rack AI OpenRouter Engineering Roadmap]] — source spine (inference operating system)
- [[RackAI Enterprise AI Development Plan]] — source spine (operator stack)
- [[OpenRouter Integration Plan]] — the gated GTM sequence
- [[Capability Gap Register]] — live shipped-vs-planned state
- [[Product Hub]] · [[Rack AI Knowledge Base]]
