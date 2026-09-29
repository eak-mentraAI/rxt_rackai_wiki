---
id: hub-roadmap
type: hub
status: draft
owner: product
domain: strategy
aliases: [rackai roadmap, canonical roadmap, living roadmap, roadmap hub, operator roadmap, engineering roadmap canonical, four proofs, observe decide control operate, proof roadmap]
related: [hub-root, hub-product, hub-battlegrounds, hub-load-bearing-bets, hub-minimum-operable-estate, hub-ai-operations-product, hub-enterprise-ai, hub-commercial, hub-governance, hub-evidence, src-rackai-delivery-roadmap, src-engineering-roadmap, src-rackai-dev-plan, idx-openrouter-integration-plan, idx-capability-gap-register, ent-empirical-map, ent-governed-harness]
source_docs: ["reference/RackAI - Roadmap.xlsx", "06-sources/RackAI Roadmap (Delivery Plan).md", "06-sources/Rack AI OpenRouter Engineering Roadmap.md", "06-sources/RackAI Enterprise AI Development Plan.md", "05-wiki/OpenRouter Integration Plan.md", "04-evidence/Capability Gap Register.md", "00-hub/Three Battlegrounds.md", "PM/leadership roadmap review 2026-09-28"]
confidence: derived
last_reviewed: 2026-09-28
parent: hub-root
summary: "Canonical living roadmap: four proofs of the operator identity (Observe, Decide, Control, Operate)."
---

# RackAI Roadmap

The **single canonical, living roadmap** for RackAI. It is built primarily on the **actual delivery roadmap** — the [[RackAI Roadmap (Delivery Plan)]] (`measured`; the staffed, Jira-tracked `reference/RackAI - Roadmap.xlsx`) — which this note **reorders and extends under the operator strategy**: it lifts the real delivery milestones out of their native CSP/M2 grouping and re-places them under the four operator proofs (the reordering), then adds the strategy-driven gaps and proposals the delivery plan does not yet contain (the extension). It further draws on two strategy narratives — the [[Rack AI OpenRouter Engineering Roadmap]] (`validated`, read-only) and the [[RackAI Enterprise AI Development Plan]] (`assumed`, raw projection). **This note is editable and is where planning actually lives;** all three sources remain intact — when a proposed change is accepted, it lands here first, and the sources are left unedited per the truth hierarchy. The delivery roadmap keeps its native numbering, Jira IDs, owners, and status so the corpus stays traceable to Jira.

> **Tooling.** The live roadmap — pillar items, quarterly sequencing, status, and ownership — is maintained in **Craft.io**. This wiki note carries the strategic rationale, the four-proof structure, gap analysis, and confidence states behind each roadmap item. Neither replaces the other: Craft.io is the *what and when*; this note is the *why and what we learned*. See [[Team Operating Model]] for the roadmap update process and the Craft.io↔wiki division of responsibility.

> **Confidence.** `derived` — this roadmap synthesizes two existing planning spines under the [[Three Battlegrounds|Private Enterprise AI Operator]] identity. Individual items carry the confidence of their source (phase/program/gap). Nothing here upgrades a capability to shipped; the live shipped-vs-planned state is the [[Capability Gap Register]].

---

# Executive Summary

*Read this page in five minutes; the rest of the document is the evidence beneath it. Two lines below are drafted for ratification and marked **[proposed]** — they are not yet settled.*

**Where we're going.** RackAI becomes the **Private Enterprise AI Operator** — Rackspace operates production AI for enterprises that cannot hand their data, inference, and operational responsibility to a public AI service ([[Three Battlegrounds]]).

**What customers buy. [proposed — needs ratification]** Rackspace assumes responsibility for **operating a customer's enterprise AI estate** across models, accelerators, and execution environments — providing the infrastructure and control plane *plus* the managed operational layer to run those workloads reliably, securely, and economically. The customer keeps control of their data, models, and governance boundary; Rackspace assumes an increasing share of the operational burden. *(Drafted from the MOE, [[AI Operations Product]], and the commercial gates below; the exact packaging/SKU is a live commercial decision — see Decisions Required.)*

**Why Rackspace (right to win the first estates). [`derived`]**
1. **Operator heritage** — taking operational responsibility for infrastructure someone else built is Rackspace's core identity; this is its AI-era expression.
2. **Owned + heterogeneous fleet** — an operated GPU fleet (NVIDIA + AMD) behind a supply-abstraction interface, so we own the economics rather than reselling capacity.
3. **Private / sovereign posture** — built for the controlled, regulated environments where public inference is a non-starter for a material set of workloads.
4. **We absorb what customers don't want to build** — the operating layer (harness, governance, lifecycle, economics) between raw GPUs and enterprise outcomes.
*(Right to win the **first ten** estates; the flywheel below is why estate #100 is cheaper than #1. See [[Three Battlegrounds]] and [[Load-Bearing Bets]].)*

**How we get there.** Four progressive proofs, not a feature backlog: **Observe → Decide → Control → Operate.**

**Where we are today (one line):** the measurement/identity substrate is underway (auth/audit shipped, telemetry + metering in progress); the learning advantage (Empirical Map) and the identity proof (a real operated estate) are **not yet built**.

| Proof | Status | What it means | What happens next |
|-------|:------:|---------------|-------------------|
| **Observe** | 🟡 foundations underway | Understand what's happening and what it costs | Finish telemetry + benchmarks + metering; add the missing **cost model** |
| **Decide** | 🟡 components exist | Accumulated evidence improves decisions | Build the **Empirical Map**; prove one decision beats a static baseline |
| **Control** | 🔴 not proven | Safely assume responsibility inside an enterprise boundary | **MOE-0** (rehearsal) → **MOE-1** (paid, external) |
| **Operate** | ⚪ future | Repeat it profitably across heterogeneous estates | Learn from the MOEs *before* industrializing |

**Current focus:** complete **Observe** while beginning **MOE-0** preparation and the minimum Decide/Control dependencies.

**Our moat hypothesis.** The **Empirical Map** — RackAI's accumulated evidence about how models and workloads actually behave across hardware, configurations, and operating conditions. It turns experience from prior estates into better placement, routing, capacity, and operational decisions for future estates. The flywheel: *more estates → more evidence → better decisions → better utilization / cost / reliability → better economics → more estates.*

**Next major proof:** **MOE-0** (friendly operating rehearsal). **First commercial proof:** **MOE-1** (external customer delegates responsibility **and pays**).

**Decisions required from leadership** (the four executive decisions — full detail in the *Proposed Changes → Four Executive Decisions* section below):
- **D1 — Reorient around MOE-0 → MOE-1** (manage toward a dated operating proof, not a feature backlog). *Open: name MOE-0 + date; name the MOE-1 customer profile + window.*
- **D2 — Fund the substrate that improves us with scale** (economics + supply optionality + Empirical Map).
- **D3 — Establish the minimum enterprise control envelope for MOE-1.**
- **D4 — Narrow where we differentiate** (evaluate partner(s) for fine-tuning delivery, RackAI owns integration/serving; don't prematurely build Proof 4).
- **Also unresolved (this document does not yet answer):** what we **stop/deprioritize** to fund this, and the **resource/cost** shifts D1–D4 imply.

**What would change our minds** (kill criteria): **K1** — if customers won't *delegate operational control* (only buy private inference), we may be an infrastructure platform, not an operator. **K2** — if cross-estate evidence doesn't *transfer* to beat workload-local optimization, the Empirical Map isn't a moat. **K3** — if domain-aligned models don't beat frontier for our buyers, the wedge is wrong.

---

## The Operating Loop — the system the four proofs build

The four proofs are horizons of *evidence*; this is the *machine* they assemble. Every roadmap item below is ultimately an implementation choice in service of one loop — **meter → characterize → accumulate evidence → decide → route/place → observe → feed back** — wrapped in enterprise governance and made executable across heterogeneous estates. If an item does not strengthen a turn of this loop, it is a technique, not a destination (this is the test applied hardest in Proof 2).

```mermaid
flowchart LR
    METER[Meter workload + economics] --> CHAR[Characterize the workload]
    CHAR --> MAP[Empirical Map accumulates evidence]
    MAP --> DECIDE[Choose model / runtime / accelerator / config]
    DECIDE --> PLACE[Route / place the workload]
    PLACE --> OBSERVE[Observe actual outcome]
    OBSERVE --> MAP
    GOV[Enterprise governance envelope] -.wraps.-> DECIDE
    GOV -.wraps.-> PLACE
    EST[Heterogeneous estates] -.executes across.-> PLACE
```

**How the loop maps to the four proofs** — the proofs are stages of making this loop real, not a parallel structure:

| Loop stage | Proof | Canonical home |
|------------|-------|----------------|
| Meter workload + economics | 1 Observe | [[Metering]] + cost model (P-003) → [[AI FinOps]], [[Unit Economics Model]] |
| Characterize the workload | 1→2 | [[Traffic Class]] (workload characterization) |
| Accumulate evidence | 2 Decide | [[Empirical Map]] (the moat) |
| Choose model/runtime/accelerator/config | 2 Decide | Workload placement (P-004); [[Request Routing]] |
| Route / place the workload | 2 Decide | [[Request Routing]]; [[Standard Model Deployment]] |
| Observe actual outcome → feed back | 2→loop | [[Monitoring & Observability]] → [[Empirical Map]] |
| Governance envelope around the loop | 3 Control | [[AI Governance and Assurance]], [[Governed Harness]] |
| Executable across estates | 4 Operate | [[AI Operations Product]], [[Minimum Operable Estate]] |

> **Why this framing matters.** Read as scattered milestones, the roadmap looks like a pile of inference-engineering projects. Read as this loop, most "features" (speculative decoding, AMD AIM, llm-d, Prometheus, RBAC, OpenRouter) stop being roadmap destinations and become *implementation choices in service of the loop*. The differentiated items are the ones that make a **better workload-placement decision**: characterization → Empirical Map → evidence-informed routing → closed-loop optimization. That is the flywheel; everything else serves it.

---

## Sequencing Logic — why this order, when we have no demand signal

**The honest problem this section answers.** A normal roadmap sequences by demand: build what the most customers are asking for, most-asked first. **We do not have that signal** — no signed estate, no production traffic, and the capacity work already states plainly that no measured demand exists ([[GPU Capacity Demand Rationale]]). Without demand, any ordering *looks* arbitrary, and "why cost model before the harness? why the Empirical Map before multi-region?" is a fair and dangerous question. The weak response is to invent a forecast. The strong response is to sequence by a **different, explicit logic** — and say what it is.

> **The ordering hypothesis (state this first, defend the rest against it):** *In the absence of demand signals, we sequence to **buy the most information and preserve the most optionality at the lowest irreversible cost** — not to satisfy a forecast we don't have.* Every item's place in the order should be defensible as one of: it gets more expensive the longer we wait, it keeps future paths open, or it cheaply resolves an uncertainty that would otherwise waste later work. If an item's ordering can't be justified by one of those three, its position **is** arbitrary and should be challenged.

**The three ordering principles (this is the whole logic):**

| # | Principle | The question it answers | Order by | Examples in this roadmap |
|---|-----------|-------------------------|----------|--------------------------|
| **1** | **Irreversibility / cost-of-delay** | *What gets more expensive to do the longer we wait?* | Do the cheap-now / expensive-later things first | Workload-placement interface (baking owned-fleet assumptions in later is a rewrite); cost model riding the Metering pipeline (attaching cost later means re-plumbing); compliance envelope kickoff (attestation lead times are long) |
| **2** | **Optionality** | *What keeps the most future paths open?* | Do the things that avoid lock-in before we know the answer | Supply abstraction (owned/partner/customer/hyperscaler stays open); transferable-vs-isolated telemetry split designed in from day one; partner-evaluated fine-tuning (don't build a toolchain we may not want) |
| **3** | **Evidence-generation / learning value** | *What most cheaply resolves our biggest uncertainty?* | Do the highest-information experiments first | Prototype the [[Empirical Map]] first (it tests the *thesis itself* — K2); MOE-0 → MOE-1 (tests whether customers delegate-and-pay — K1); the domain-model fine-tuning experiment (tests the central bet — K3) |

**How this maps to the four proofs (so the order isn't just asserted):**

- **Observe before Decide** — not because Observe is "phase 1," but because you cannot make an evidence-informed decision (Proof 2) before you can measure cost and outcome (Proof 1). Measurement is the cheapest, most irreversible-if-skipped substrate: every later claim reads from it. *(Principle 1 + 3.)*
- **Empirical Map early, inside Proof 2** — sequenced first *within* Decide because it is the highest-information experiment we can run: it tells us whether the differentiated thesis works **at all** before we spend on everything downstream of it. Prototyping it is how we avoid over-investing in a moat that might not compound (K2). *(Principle 3.)*
- **Control (MOE-0 → MOE-1) pulled earlier than a feature backlog would put it** — because the single largest unknown is not technical, it's *will a customer delegate operational responsibility and pay* (K1). That question is answered only by operating a real estate, so we start MOE design during Proof 1 rather than waiting. An operating proof resolves more uncertainty per dollar than another inference optimization. *(Principle 3.)*
- **Operate (Proof 4) deliberately last** — multi-region, day-zero factory, closed-loop automation are sequenced *after* the MOEs on purpose: automating and industrializing before we've operated even once would be building for a demand and an operating model we haven't validated. We **do not automate before we operate**. *(Principle 1 inverted: these are the things that are cheap to *delay* and expensive to do *speculatively*.)*

**What this buys us with a skeptical audience.** It reframes the roadmap from *"a bet on demand we can't see"* to *"a deliberately sequenced series of experiments, each chosen to cheaply de-risk the next."* The [[#Kill / Falsification Criteria (what would change the thesis)|kill criteria K1–K3]] are not just success/failure switches — they are the **ordering rationale**: we do the things that test K2 (does the moat compound?), K1 (will customers delegate and pay?), and K3 (do domain models win?) *early and cheaply*, because a "no" on any of them re-orders everything after it. Sequencing toward the kill criteria is how a pre-demand roadmap stays honest.

> **The one-line version for the exec who asks "why this order?":** *We don't have demand data, so we're not pretending to. We're ordering the work to answer our three make-or-break questions as cheaply and early as possible, and to avoid decisions that are cheap today and expensive to unwind later. Demand signal, once it exists (first MOE, first OpenRouter traffic), re-prioritizes from there.*

---

## How to Read This Roadmap

- **North star** is the operator identity, not leaderboard rank. We are building *the best operator of heterogeneous enterprise AI estates*; OpenRouter competitiveness is a **learning vehicle inside** the operator roadmap, not its critical path ([[Three Battlegrounds]]).
- **The roadmap is organized around four progressive proofs**, not around inherited technical phases: **Observe → Decide → Control → Operate.** Each proof has an exit condition phrased as a claim about *operating an estate*. The **delivery roadmap** ([[RackAI Roadmap (Delivery Plan)]]) supplies the real milestones that are **reordered under these proofs**; the two strategy spines — the [[Rack AI OpenRouter Engineering Roadmap]] (Phases 0–6) and the [[RackAI Enterprise AI Development Plan]] (Programs 1–5, P1–P9) — supply the strategy items that **extend** it. The proofs are the organizing logic.
- **Every item passes one test:** *does this make us materially better at operating a customer's AI estate?* ([[Three Battlegrounds]] strategic choice.)
- **The MVP is the [[Minimum Operable Estate]]**, not the full platform. We earn the word "Operator" by operating one estate, then ten, then automating what hurts.
- **Maturity principle:** every capability walks the ladder **human-operated → instrumented → assisted → automated** (see below). We do not automate before we operate.
- **Proofs are gates, not waterfall phases** (full callout under *The Four Proofs*).
- **Change workflow:** propose in the "Proposed Changes" section → review → on acceptance, edit the proof/workstream tables and log a change packet in `08-change-control`.

> **In one line:** Become the Private Enterprise AI Operator by proving Observe → Decide → Control → Operate — starting with one [[Minimum Operable Estate]] and automating what we learn. (The full pitch, moat, and flywheel are in the Executive Summary above.)

## Two Teams, One Roadmap

This roadmap spans two teams split at the Kubernetes line. Every milestone below carries an **Owner** tag so the boundary is explicit.

| Team | Owns | On this roadmap |
|------|------|-----------------|
| **RackAI** (this team) | **Above Kubernetes** — inference, serving runtimes, model lifecycle, **inference routing**, fine-tuning, the harness, the [[Empirical Map]], metering economics/cost model, governance software, the operating layer, [[AI Operations Product]] | Owns the operator thesis and most of Proofs 2–4; **consumes** what Infra builds |
| **Infra** | **Kubernetes and below** — cluster, nodes, GPU fleet, networking, storage, and **cluster observability** | Builds the substrate RackAI runs on; owns most of the Proof-1 CSP Platform Layer |

**The two boundary rules that matter most:**
- **Observability:** Infra **builds** cluster observability; RackAI **consumes** it (and turns it into operating intelligence — the Empirical Map).
- **Accelerator selection:** Infra **owns the choice**, but RackAI is a **constraining stakeholder** — if we need to run a model that requires specific GPUs, Infra selects within our constraints. Tagged **Joint (Infra-led)**.

**Owner tags used below:** `RackAI` · `Infra` · `Joint` (with lead noted). Where an item is "Infra builds, we consume," it's tagged `Infra → RackAI`.

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

Operating knowledge is *created by operating*, so every capability walks this ladder rather than starting automated. This is how the flywheel (Executive Summary) actually gets built — and it reduces speculative platform engineering.

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

### Proof 1 — Observe: *We understand what is happening and what it costs*

> **Technical exit:** For a production model, Rackspace can **accurately measure** its cost, performance, utilization, reliability, and operational history **on the infrastructure we operate.** Two boundaries: "operate" is *earned* by Proof 4 (Proof 1 is understanding, not yet operating on a customer's behalf), and *where/how a workload runs best* is comparative intelligence — that is Proof 2, not Proof 1.
> **Commercial gate:** we have a defensible cost model and a pricing hypothesis for operated workloads.

| Item | Traces to | Confidence |
|------|-----------|:----------:|
| Unit Economics / Cost Intelligence (cost/GPU-hour → cost/token → utilization-adjusted → margin) | Eng. 0.3; dev-plan Prog 5; [[Unit Economics Model]] | missing |
| Fleet telemetry instrumentation | Eng. 0.2 | missing |
| Initial benchmark harness | Eng. 0.4 | missing |
| Metering | Gap Register; dev-plan Prog 5.2 | planned |
| Basic reliability / observability | Eng. 2.2 / E | planned |
| GLM 5.3 Flash deployment + OpenRouter Path A (real workloads to exercise the system) | [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]]; [[OpenRouter Integration Plan]] Phase 1 | derived / planned |
| **Workload Placement Policy — the *interface*, not multi-provider scheduling** (`SupplyTarget / AcceleratorPool / ExecutionLocation`; owned H100 = impl #1) | Strategy-derived architectural requirement ([[Load-Bearing Bets]]) | assumed |
| Compliance envelope kickoff (SOC 2 scoping) | dev-plan **P1** ("start first") | missing |

*Why the placement interface is here, not later: the abstraction is cheap now and expensive later. Building the control plane against `SupplyTarget` from day one prevents baking owned-fleet assumptions into everything. We do not need multi-provider scheduling yet — only the interface.*

> **Workload Placement Policy — the unresolved product decision (open question, not just an interface).** The interface above is the *mechanism*; the *product question* is bigger and unsettled: **how much infrastructure choice does the customer get?** The strategic target is an experience closer to *"here is my workload and my constraints"* — RackAI then selects model runtime, accelerator, quantization, replicas, and routing — rather than *"give me 4 B300s."* That abstraction is what makes the [[Empirical Map]] commercially meaningful (RackAI makes the decisions the map informs). But customers have explicitly asked for control over which GPU they deploy on, and today's quota plans are defined in **GPU-centric** terms. So there is a real tension: if we abstract the GPU away, the quota model needs rethinking; if we don't, the placement intelligence has less room to act. **Open question — RackAI selects everything beyond the workload + constraints, or the customer keeps GPU-level control?** Ties to [[Capacity Pool]] quota definitions and the P-004 gap; needs PM ratification.

### Proof 2 — Decide: *Our accumulated knowledge improves decisions*

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

### Proof 3 — Control: *We can safely assume responsibility inside an enterprise boundary*

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

### Proof 4 — Operate: *We can do it repeatably and profitably across heterogeneous estates*

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

## Milestones — the execution spine

The proofs say *what we must be able to claim*; the milestones say *what the teams are actually building to get there.* **These are the real delivery milestones** from the [[RackAI Roadmap (Delivery Plan)|delivery roadmap]] (`reference/RackAI - Roadmap.xlsx`) — native numbering (IAC M1–M4, Platform M1–M4, etc.), Jira IDs, owners, status, and dates preserved so the corpus stays traceable to Jira. Each is placed under the **operator proof it serves**; that placement is the strategic lens applied *to* the delivery plan. Where a proof needs work the delivery plan does not yet contain, it appears as a **⚠ gap** and is carried to Proposed Changes — not invented as a milestone here.

> **Status/dates are the delivery roadmap's own** (`measured` — real Jira/schedule). Confidence in the last column reflects delivery status, not strategy aspiration. The strategy-side items with no delivery milestone yet are marked ⚠ and sink to the Proposed Changes queue.

### Proof 1 — Observe: *understand what is happening and what it costs*

The CSP Platform Layer is almost entirely Proof 1 — it is the measurement/identity substrate.

| Milestone | Deliverable | Jira | Owner | Team | Status | Serves |
|-----------|-------------|------|-------|------|--------|--------|
| **IAC M1** | JWT + API-key validation, identity context, APIKey CRD, Gateway auth | RACKAI-204 | Ljungstrom | Infra → RackAI | **Complete** | Identity substrate (all proofs) |
| **IAC M2** | PlatformRole/RoleBinding CRDs, Authorization Service, RBAC | RACKAI-333 | Ljungstrom | Infra → RackAI | **Complete** | Tenancy/control |
| **IAC M3** | Audit Log query API, sensitive-access + login + APIKey-lifecycle events | RACKAI-351 | Ljungstrom | Infra → RackAI | **Complete** | Auditability (→ Proof 3) |
| **Platform M1–M2** | Prometheus/DCGM/Grafana GPU dashboards; tenant-attributed service metrics | RACKAI-353/350 | Sharma | Infra → RackAI | In Progress | Telemetry (flywheel input) |
| **Platform M3–M4** | Loki logs; VictoriaMetrics 13-mo retention; FineTuningJob metrics | RACKAI-431/432 | Sharma | Infra → RackAI | In Progress | Telemetry retention |
| **Metering M1** | Project CRD + usage_records + MeteringEvent pipeline w/ inference + FT metering | RACKAI-352 | Rajak | Joint (Infra pipeline, RackAI economics) | In Progress | Cost/usage capture |
| **Observability M1** ⭐ | Metrics API (latency/rate/errors, quota util), Workload Status API | — | Audit/Obs | Infra → RackAI | Not Started (crit-path) | The operator dashboard |
| **M2: AI Performance Benchmarks** | Internal benchmarking process — **anchored to the external [[AgentX Benchmark Standard]]** (SemiAnalysis InferenceX) for the agentic-workload profile, run via NVIDIA AIPerf; fixed-sequence runs for conventional streams | — | — | **RackAI** | Not Started (Pri 5) | Ends "KPIs assumed" |
| ⚠ **Unit Economics / Cost Intelligence** (first-class workstream, not an aside) | *not a delivery milestone yet* — Metering captures **usage**, but no monetary cost is modeled: GPU-hour cost, power + colo + network allocation, accelerator depreciation, storage, cost/token, utilization-adjusted cost, → eventually margin per customer/workload | — | — | **RackAI** (FinOps; Infra + Finance data inputs) | **gap → P-003** | Cost floor — the economics the whole thesis rests on |
| ⚠ **Workload Placement Policy** (the interface *and* the product decision) | *not in delivery plan* — control plane assumes owned fleet; and the customer-choice question is unresolved | — | — | **RackAI** | **gap → P-004** | Prevents fleet lock-in; defines the operator UX |

**Proof 1 read:** measurement substrate is genuinely underway (auth/audit shipped; telemetry + metering in progress). The two strategy gaps are elevated from asides to first-class workstreams. **Cost Intelligence** is fundamental to the RackAI thesis: if we claim we can operate inference more efficiently than customers can themselves, we have to *know* our cost — and today metering deals only in metered usage, not monetary value. This likely needs to tap undercloud metrics (power, networking cost) and finance data (depreciation/lease), not just engineering telemetry. **Workload Placement Policy** is bigger than an interface — see its open product decision below.

### Proof 2 — Decide: *accumulated knowledge improves decisions*

| Milestone | Deliverable | Jira | Owner | Team | Status | Serves |
|-----------|-------------|------|-------|------|--------|--------|
**One test governs everything in this proof:** *does this capability help RackAI make a better workload-placement decision?* That test cleanly splits Proof 2 into the **strategic flywheel** (differentiating) and **techniques** (implementation choices that earn their place only when evidence says they improve an outcome we care about).

**Strategic — the flywheel (differentiating):**

| Milestone | Deliverable | Jira | Owner | Team | Status | Serves |
|-----------|-------------|------|-------|------|--------|--------|
| ⚠ **Empirical Map v1** + transferable/isolated split | *not in delivery plan* — telemetry exists, but no cross-workload knowledge store. **Highest-priority experiment: prototype first** — it tests whether the differentiated RackAI thesis works at all (K2) | — | — | **RackAI** | **gap → P-005** | **The moat** |
| ⚠ **Workload characterization** (analyze real traffic → workload classes) | partial — [[Traffic Class]] concept exists; characterization of *actual* traffic is the OpenRouter-3.3 input, not yet a placement input | — | — | **RackAI** | **gap → P-005** | Feeds the map |
| ⚠ **Evidence-informed routing** (routing reads the map) | delivery routing is llm-d/KV-cache, not empirically-driven | — | — | **RackAI** | **gap → P-005** | Flywheel |
| ⚠ **Closed-loop optimization** (outcome feeds back into the map) | Eng. Phase 6 — not in delivery plan | — | — | **RackAI** | **gap → P-007** | Closes the loop |
| **M2: Inference routing** (the substrate the map plugs into) | llm-d, ingress→llm-d→model, shared KV cache | RACKAI-311 | Chatterjee | **RackAI** | In Progress | Routing substrate |
| **M2: Accelerator selection ph3** | node inventory + GPU consumption metrics | RACKAI-336 | Nguy | Joint (Infra-led, RackAI constrains) | **Complete** | Placement inputs |

**Techniques — implementation choices, not roadmap destinations** (roadmap them only when empirical evidence says they improve an outcome we care about):

| Technique | Jira | Owner | Status | PM disposition |
|-----------|------|-------|--------|----------------|
| Speculative decoding | RACKAI-67 | Ferrer | In Progress | **Reprioritize** — assess against what other offerings already provide before independent investment |
| Refrag | RACKAI-374 | — | In Progress | **Reprioritize** — low clarity on value; do not independently roadmap without an evidenced outcome |
| AMD AIM engine / AMD+NVIDIA nodes | RACKAI-347/263 | Chatterjee/Gosavi | In Progress / Not Started | Multi-accelerator serving carries a **cost**: AIM integration trades against the feature set we want in the roadmap. Weigh explicitly |
| DPO fine-tuning | RACKAI-252 | Shah | In Progress | Preference-tuning beyond SFT — a fine-tuning *technique*; disposition follows P-001 |
| Uniphore: SFT/LoRA | — | Rajendra/Neelava | In Progress | Dataset mgmt, PEFT/LoRA adapters, deploy/undeploy (shipped-ish) |
| ⚠ **Semantic router** | — | — | **not captured in delivery** | PM flag: semantic routing work is **absent** from the plan. Only a *technique* until the map shows it improves a placement/routing outcome — then it plugs into evidence-informed routing |

> **Shared KV cache is rudimentary today** and needs more work to give the best experience — but that work needs PM input on the target experience before it is scoped. Its payoff is directly measurable under the [[AgentX Benchmark Standard]], which stresses shared-prefix reuse under agent traffic — so KV-cache work is scored against an external standard, not asserted.

> **The engine question (vLLM vs AIM vs NIM) is resolved by measurement, not argument.** The vendor-blessed engines (AIM on AMD, NIM on NVIDIA) are optional backends behind the serving abstraction; whether they beat tuned vLLM/SGLang for a given model×hardware×workload is an empirical delta the [[AgentX Benchmark Standard]] can produce on our own fleet. Adopting AIM on a "vendor engine is faster" argument would symmetrically force NIM too — so we commit to *neither* as strategy and let the [[Empirical Map]] cell (fed by AgentX) decide per cell. Anchoring to AgentX is what turns that from a debate into a number.

**Proof 2 read:** the *ingredients* of good operating decisions are being built (routing, accelerator selection, perf optimizations, fine-tuning), but the **Empirical Map** — the thing that makes decisions *evidence-informed across workloads*, i.e. the moat — is not on the delivery plan. This is the single most important strategy gap. The reframe above is the reviewer's central point: **the strategic chain is `Empirical Map → workload characterization → evidence-informed routing → closed-loop optimization`; the techniques (speculative decoding, Refrag, AMD AIM, DPO, semantic router) are in service of the loop, not destinations.** Prototype the Empirical Map first — it is the highest-value experiment because it tests the differentiated thesis itself.

### Proof 3 — Control: *safely assume responsibility inside an enterprise boundary*

| Milestone | Deliverable | Jira | Owner | Team | Status | Serves |
|-----------|-------------|------|-------|------|--------|--------|
| **IAC M3** (audit) + **Auditing M1–M3** | Audit Service, admission webhook, compliance validation, billing audit | — | Audit/Obs | Infra → RackAI | M3 done; Auditing Not Started | Auditability |
| **Metering M4** | Quota Enforcement, pre-execution admission control (429/402) | — | — | Joint (Infra pipeline, RackAI economics) | Not Started | Guardrails |
| **Uniphore: single-cluster tenancy** | namespace-per-org isolation (shipped foundation) | — | — | Joint (Infra cluster, RackAI tenancy) | In Progress | Isolation |
| ⚠ **IAC M4** (org-level RBAC + metering/billing/quota perms) | **Won't Do** — dropped from delivery | — | — | Infra → RackAI | **gap → P-006** | Org-level access control |
| ⚠ **Governed execution harness v1** | *not in delivery plan* | — | — | **RackAI** | **gap → P-006** | The operating layer |
| ⚠ **First compliance attestation** (SOC 2) | *not a delivery milestone* — "compliance validation" is an Auditing sub-task, no attestation milestone | — | — | **RackAI** (Infra evidence input) | **gap → P-006** | The gate for regulated buyers |
| ⚠ **MOE-0 / MOE-1** (operator rehearsal → paid identity proof) | *not modeled in delivery* | — | — | **RackAI** | **gap → P-002** | First proof of the identity |

**Proof 3 read:** the delivery plan builds real control-plane pieces (audit, admission control, isolation) but **stops short of the identity proof** — there is no harness, no compliance attestation milestone, no MOE, and org-level RBAC was explicitly dropped (IAC M4 "Won't Do"). This is where the strategy is furthest ahead of delivery.

> **This proof is materially underdeveloped relative to its importance, and that is backwards for an enterprise product.** We do not win merely because we can serve tokens; we win when a customer can say *"I can safely let RackAI operate this workload inside my enterprise boundary."* The delivered work is mostly authorization, auditing, quota, and tenancy, while the concepts that actually earn that sentence — governed execution, compliance attestation, the MOEs — are "not in delivery." The response is to name an explicit **Enterprise Control Plane** workstream so these stop being scattered gaps.

### The Enterprise Control Plane (the Proof-3 workstream)

The controls that let a customer delegate operation inside their boundary, treated as one workstream rather than scattered line items. Canonical homes already exist — this groups them under the operator lens; it does not redefine them.

| Control | What it covers | Canonical home | Status |
|---------|----------------|----------------|:------:|
| Policy / guardrails | Runtime policy enforcement on what the workload may do | [[AI Governance and Assurance]]; [[Action Controls]] | planned |
| Workload identity | Scoped, revocable service identities; delegated authority that expires | [[Agent Identity]] | planned |
| Model provenance | What model/version/weights ran, and the record to prove it | [[AI Governance and Assurance]] (provenance/replay) | assumed |
| Data / inference isolation | Tenant + workload isolation across the execution boundary | [[Multi-Cluster Governance Brief (Partner)]]; [[Perimeter Information-Flow Control]] | planned |
| Action authorization | Authorizing outbound actions by identity, before execution | [[Agent Identity]] → [[Action Controls]] | planned |
| Auditability | An audit that is a query against the platform | [[Audit]] (IAC M3 shipped; Auditing M1–M3 pending) | partial |
| Compliance **evidence** | The independently-verifiable evidence a regulated buyer's segment requires | [[AI Governance and Assurance]] (compliance envelope) | missing |
| Human approval where required | Approval gates on high-blast-radius actions | [[Action Controls]] (human-in-the-loop gate) | planned |
| Governed execution | The harness runtime that enforces all of the above at execution time | [[Governed Harness]] | assumed |

> **Certification is not the same as the product controls that make certification possible.** SOC 2 (and sovereign attestations) matter, but they are a **gate, not the moat** — they get us into deals and do not compound. Distinguish the *certification work* (attestation lead time, auditor evidence) from the *product controls* above that make both certification **and** day-to-day customer governance possible. Build the controls; certify against them; don't confuse the two. (Compliance evidence stays framed as an **outcome** set by the MOE-1 customer segment — see P-006 — not a pre-decided SOC 2 Type I.)

### Proof 4 — Operate: *do it repeatably and profitably across heterogeneous estates*

| Milestone | Deliverable | Jira | Owner | Team | Status | Serves |
|-----------|-------------|------|-------|------|--------|--------|
| **M2: Request new model support** | on-demand model onboarding | RACKAI-354 | Bedre | **RackAI** | In Progress | Toward model velocity |
| **M2: Sunsetting a model** | model lifecycle retirement | RACKAI-372 | — | **RackAI** | Not Started | Lifecycle |
| **M2: Multi region support** | *backlogged (Pri 6, unscheduled)* | — | — | Joint (Infra clusters, RackAI routing) | Not Started | Multi-cluster estates |
| **M2: GPU node access support** | *backlogged (Pri 6, unscheduled)* | — | — | Infra → RackAI | Not Started | Heterogeneous supply |
| ⚠ **Day-zero model factory, closed-loop optimization** | Engineering-roadmap Phases 4/6 — *not in delivery plan* | — | — | **RackAI** | **gap → P-007** | Industrialization |
| ⚠ **Managed-ops / FDE motion, multi-estate onboarding** | *not modeled* | — | — | **RackAI** | **gap → P-007** | The operator business |

**Proof 4 read:** almost entirely gap. The delivery plan has model-lifecycle fragments; multi-region and GPU-node access — prerequisites for heterogeneous multi-estate operation — are explicitly **backlogged at Pri 6**. Proof 4 is a future the delivery plan does not yet fund.

> **This may be the most important proof commercially, and it needs more weight than the plan gives it.** *Operating heterogeneous AI estates repeatably* is much closer to Rackspace's natural moat than building another inference server. The three groupings below name the operator *business* Proof 4 must fund; they sequence *after* Proofs 1–3 (P-007 is a dependency declaration, not a "start now"), but they belong on the roadmap explicitly so MOE-1 is never promised ahead of its prerequisites.

**Fleet Operations** — add/remove accelerator capacity · NVIDIA + AMD lifecycle · model deployment lifecycle · upgrade/rollback · health/remediation · capacity management. Canonical homes: [[Capacity Pool Model]], [[GPU Reallocation]], [[Canary & Rollback]], [[Standard Model Deployment]]. *PM note: **GPU node access support** — is this in this team's charter at all? Confirm before scheduling; it may belong to Infra.*

**Model Lifecycle** — request → qualify → benchmark → approve → deploy → observe → upgrade → retire. Canonical homes: [[Model Radar]] (intake), [[Model Launch Factory]] (day-zero pipeline), [[Standard Model Deployment]], [[Canary & Rollback]]. *PM notes: **request new model** will likely run through **SNOW** now (delivery-platform decision still open with RXT); **sunsetting a model** has **no PRD** yet — write it before scheduling retirement.*

**Multi-estate Operations** — RXT cloud · customer private cloud · sovereign deployments · → eventually third-party capacity. Canonical homes: [[AI Operations Product]], [[Multi-Cluster Governance Brief (Partner)]], [[Minimum Operable Estate]]. *PM note: supporting **2 regions** in `rackai.rax.io` under a single RackAI instance likely needs work here — the multi-region prerequisite that gates an external multi-region MOE-1.*

## Cross-Cutting Surfaces

Items that don't sit inside a single proof but run across them: the external distribution surface, the observability split, the fine-tuning stance, and the cost-of-doing-business floor.

### OpenRouter — External Distribution & Validation (a proving ground, not the product)

OpenRouter is **external distribution and validation**, not RackAI's enterprise UX — a mechanism kept **strategically subordinate** to the operator identity. This is the [[Three Battlegrounds|"gym and proving ground"]] framing made concrete: the point is not that OpenRouter becomes the product, but that it lets us **exercise production serving, learn model onboarding quickly, generate workload telemetry, benchmark AMD vs NVIDIA, test price/performance, consume otherwise-idle capacity, and establish public performance credibility.** Every one of those is an input to the operating loop — telemetry into the [[Empirical Map]], onboarding reps into the Model Lifecycle, price/perf into Cost Intelligence. Full sequence: [[OpenRouter Integration Plan]]; hub: [[OpenRouter Initiative]].

| Item | What it is | Serves the loop by | Status |
|------|-----------|--------------------|:------:|
| **OpenRouter Provider path** (public models) | Publish RackAI-served public models to OpenRouter traffic | Exercises serving; generates telemetry; public price/perf credibility | planned ([[OpenRouter Initiative]]) |
| **OpenRouter Private Model path** | Private/BYOM models served behind the OpenRouter surface | Onboarding reps; AMD-vs-NVIDIA benchmarking on real traffic | planned |
| ⚠ **BYOM in OpenRouter** | Bring-your-own-model onboarding via the OpenRouter surface | Fast model-onboarding learning; idle-capacity consumption | **not captured in delivery** — new item |
| ⚠ **Inference-aaS in OpenRouter** | Inference-as-a-service offering exposed through OpenRouter | Production serving exercise at scale; price/perf validation | **not captured in delivery** — new item |
| ⚠ **Inference-as-a-Service direct** (`rackai.rax.io`) | Inferencing for popular models offered as a **direct** RackAI feature | *Open question:* should IaaS be a direct product feature, or stay an OpenRouter-only proving surface? | **open question — needs PM decision** |

> **Keep it subordinate.** The risk the reframe guards against is OpenRouter accidentally becoming its own product strategy. It is a learning vehicle inside the operator roadmap; its outputs feed the loop, they are not the destination.

### Observability — two distinct surfaces, do not conflate

The delivery item *"Observability M1"* raised a fair PM question: **is this observability for the end user, or for Rackers?** The answer is both, but they are **two different products** and should be split. (Boundary rule: Infra **builds** cluster observability; RackAI **consumes** it and turns it into operating intelligence — see *Two Teams, One Roadmap*. Canonical workflow home: [[Monitoring & Observability]].)

| Surface | Audience | What it shows | Why it matters |
|---------|----------|---------------|----------------|
| **Customer observability** | The customer buying the workload | Requests, tokens, TTFT, ITL, latency percentiles, errors, throughput, cost, quotas, model/SLA performance | This is **what customers actually buy** — the operator's account of their workload |
| **RackAI operational intelligence** | RackAI operators | GPU/VRAM utilization, power, queue depth, batching, KV-cache efficiency, accelerator/model efficiency, cost/token, capacity pressure | This is the **operator's** view; it **feeds the [[Empirical Map]]** and the loop |

> The second surface is more ambitious than "model usage metrics." GPU/VRAM, TTFT, and queue length are useful but are an *infrastructure operator's* view; the customer-facing product needs the percentiles/cost/SLA framing. And the operator-intelligence side is the raw material the Empirical Map is built from — the split is not cosmetic, it decides where each metric flows.

### Fine-tuning infrastructure — host the artifact, don't own the toolchain

Consistent with **P-001** (partner delivery, keep operations + the experiment). Additional signal reinforcing the direction: **checkpointing + resume** and the broader fine-tuning stack appear to be **moving external to Rackspace** — so we should not spend scarce engineering cycles rebuilding that toolchain. The general principle: *don't build ML tooling merely because an AI platform could contain it; build the operational capabilities that strengthen RackAI's differentiation.* RackAI should **host and operate the resulting artifact** (the [[LoRA Adapter]] on the fleet — fine-tuning *operations*), not own the entire training toolchain. See P-001 for the three-way split.

### CODB — cost of doing business (surfaced from the delivery CSV, not yet on the roadmap)

Delivery has recurring **CODB** work that never surfaces into the strategic roadmap but gates the operator business. Named here so it isn't invisible:

| Item | What it is | PM note | Status |
|------|-----------|---------|:------:|
| ⚠ **Object Store** | Alternative to SeaweedFS for artifact/model/dataset storage | Requires block storage allocated to the product; alternative is **Rackspace Managed Object Store** | open — needs decision |
| ⚠ **CI system** | Builds + release pipeline | Release process exists for key components but is **missing for some (model and FT images)** | gap |

## Milestone → Proof → Objective (the line of sight)

The delivery plan front-loads Proof 1 (measurement substrate), is mid-build on Proof 2 ingredients, thin on Proof 3, and largely absent on Proof 4 — with the moat (Empirical Map) and the identity proof (MOE) as the biggest gaps.

```mermaid
flowchart LR
    subgraph OBS[Proof 1 Observe - underway]
      IAC[IAC M1-M3 done]
      TEL[Platform/Metering in progress]
    end
    subgraph DEC[Proof 2 Decide - ingredients only]
      RT[Inference routing]
      MAP[Empirical Map - GAP]
    end
    subgraph CTL[Proof 3 Control - thin]
      AUD[Audit/admission]
      MOE[Harness + MOE - GAP]
    end
    subgraph OPR[Proof 4 Operate - mostly gap]
      LIFE[Model lifecycle bits]
      EST[Multi-estate - GAP]
    end
    IAC --> TEL --> MAP
    RT --> MAP --> MOE --> EST
    MOE --> OBJ[Objective: Private Enterprise AI Operator]
    EST --> OBJ
```

- **Proof 1:** genuinely progressing — the substrate the identity rests on is being built.
- **Proof 2:** ingredients in flight, but the **Empirical Map (the moat) is missing** — the flywheel cannot compound without it.
- **Proof 3:** control-plane pieces exist, but the **identity proof (harness + attestation + MOE) is absent**, and org-level RBAC was dropped.
- **Proof 4:** the operator business is not yet funded; multi-region/GPU-node access are Pri-6 backlog.

## Material Progress — baseline → target

Each metric has a **baseline (today)** and the **delivery milestone** that first moves it, or a **gap** if no delivery milestone does. This is what turns "material progress" from assertion into a checkable claim.

| Metric | Baseline (today) | First moved by | Status |
|--------|------------------|----------------|--------|
| Identity/auth/RBAC in place | shipped | IAC M1–M2 | **Complete** |
| Auditability | shipped (query API) | IAC M3 | **Complete**; Auditing M1–M3 pending |
| GPU/tenant telemetry | partial | Platform M1–M2 | In Progress |
| Usage/metering captured | partial | Metering M1 | In Progress |
| Benchmarked perf (TTFT, tok/s/GPU) | none | M2 AI Performance Benchmarks | Not Started |
| Cost/GPU-hour known | none | — | **GAP → P-003** |
| % decisions empirically informed | 0% | — (needs Empirical Map) | **GAP → P-005** |
| Compliance attestation | none | — | **GAP → P-006** |
| Estates under management | 0 | — (needs MOE) | **GAP → P-002** |
| Contribution margin / estate | n/a | — | **GAP** (Proof 4) |

The pattern is clear: **delivery is strong on the measurement substrate (Proof 1) and weakest exactly where the operator identity lives (the moat in Proof 2, the identity proof in Proof 3).** That is the agenda for the Proposed Changes below.

## Workstream View

Cross-cutting owners run *vertically through all four proofs*. Mapped from the Engineering Roadmap's workstreams A–F plus the dev-plan programs — with **AI Operations Product** elevated to first-class, because if the identity is Operator, the operating model is part of the product, not an afterthought.

| Workstream | Pillar | Team | Owns | Source |
|-----------|--------|------|------|--------|
| **[[AI Operations Product]]** | **[[Product Operations]]** | **RackAI** | Operating model, service boundaries, SLOs, incident model, customer handoffs, FDE escalation, runbooks, lifecycle responsibility, change management, estate onboarding + operational acceptance criteria | **New — elevated from dev-plan P5/P6 + Product Operations JD** |
| Platform / Control Plane | **[[Inference and Serving Services]]** | **RackAI** | Deployment orchestration, registry, capacity, routing, API, lifecycle, **supply-abstraction interface** | Eng. A |
| Inference Performance Eng | **[[Inference Optimization]]** | **RackAI** | Runtime, kernels, quantization, caching, parallelism, topology | Eng. B |
| Model Enablement | **[[Model Services]]** | **RackAI** | Radar, intake, compatibility, functional testing, launches | Eng. C |
| GPU / Infra Eng | *Infra (below K8s)* | **Infra** | Clusters, networking, storage, topology, firmware, health | Eng. D |
| SRE / Reliability | Joint: [[Inference and Serving Services]] + Infra | Joint (Infra cluster, RackAI service) | Availability, observability, incident response, canary, rollback | Eng. E |
| FinOps / Economics | **[[Inference Optimization]]** | **RackAI** | Cost/token, GPU-hour economics, revenue/GPU-hour, contribution margin | Eng. F; dev-plan Prog 5 |
| Harness & Orchestration | **[[AI Harness]]** | **RackAI** | Execution harness, routing, context/tool controls, memory, runtime | dev-plan Program 1 |
| Governance & Assurance | **[[AI Governance and Assurance]]** | **RackAI** | Verification, perimeter info-flow, agent identity, **compliance envelope (P1)** | dev-plan Program 2 + P1 |
| Measurement & Self-Improvement | **[[AI Harness]]** | **RackAI** | Empirical Map, eval-as-CI, loop planning, self-improvement | dev-plan Program 3 |

Vertically through all four proofs: **AI Operations Product + Compliance + Economics + Telemetry.**

## Open Roadmap Gaps

Seams where the strategy is still ahead of the plan, tracked for the "Proposed Changes" pipeline. Several earlier gaps are now placed by the four-proofs restructure (harness → Proof 3; supply-abstraction interface → Proof 1; transferable-vs-isolated telemetry → Proof 2; compliance → all proofs; operator KPIs → North Star; managed-ops/FDE → AI Operations Product workstream). Remaining open items:

1. **Minimum Operable Estate spec** — needs its own canonical note defining the smallest environment where "we operate your AI" is legitimately true (candidate: 1 customer, 1 private env, 2 models, 1 harness, 1 supply source, basic routing, metering, observability, identity/policy, audit, model lifecycle, human-operated placement).
2. **Operator KPI instrumentation** — the North-Star families are defined but unmeasured; Proof 1 must land them.
3. ~~**AI Operations Product** — elevated here, but has no canonical workstream/owner note yet.~~ **Closed** — canonical note created: [[AI Operations Product]] (staffing/ownership still open).
4. **Supply-abstraction interface spec** (`SupplyTarget / AcceleratorPool / ExecutionLocation`) — an architectural requirement without a design note; now framed as **Workload Placement Policy** (Proof 1), which also carries an unresolved *product* decision (how much GPU-level choice the customer keeps vs. RackAI selecting from workload + constraints).
5. **Semantic router** — flagged absent from the delivery plan; a routing *technique* with no home until the [[Empirical Map]] shows it improves a placement outcome (Proof 2).
6. **OpenRouter BYOM + Inference-aaS**, and **Inference-as-a-Service as a direct `rackai.rax.io` feature** — surfaced in Cross-Cutting Surfaces; the direct-IaaS question needs a PM product decision.
7. **Customer-observability product surface** — distinct from operator intelligence; not yet a named deliverable (Cross-Cutting Surfaces).
8. **CODB: Object Store (SeaweedFS alternative) and CI for model/FT images** — real delivery work that gates the operator business but never surfaced strategically (Cross-Cutting Surfaces).

## Proposed Changes → Four Executive Decisions

The strategy-driven changes to the delivery plan are **not seven equivalent backlog edits** — seven proposals invite seven separate debates; **four decisions force a debate about the strategy.** The ask to leadership is to approve four decisions, name MOE-0, establish the MOE-1 customer profile, put dates against them, and have Engineering come back with the roadmap changes needed to hit those proofs. This turns the framework into a **resource-allocation mechanism**, not a feature list.

| # | Executive decision | What you're actually approving | Implements |
|---|--------------------|-------------------------------|-----------|
| **D1** | **Reorient delivery around MOE-0 → MOE-1** | Manage RackAI toward a **dated friendly operating rehearsal (MOE-0)** then a **paying external identity proof (MOE-1)** — *not* toward completion of a feature backlog | P-002 |
| **D2** | **Build the substrate that lets RackAI improve economically and operationally with scale** | Not "approve three engineering projects" — approve the substrate behind the flywheel, with three manifestations: **economics** (cost model — know our economics), **supply optionality** (supply-abstraction interface — preserve optionality over supply), and **accumulated operating intelligence** (Empirical Map — compound operating knowledge; **load-bearing**, not just a workstream) | P-003, P-004, P-005 |
| **D3** | **Establish the enterprise control envelope for MOE-1** | The **minimum** identity/authorization, governed execution, audit, isolation, and **independently-verifiable compliance evidence** required by the MOE-1 customer — outcome, not a specific implementation | P-006 |
| **D4** | **Narrow where we differentiate** | RackAI will **not** become a differentiated fine-tuning product — **evaluate partner(s) for delivery** (Uniphore leading) while RackAI owns the **integration / model-serving** function + enough first-party capability to learn; and **do not prematurely build Proof 4** — identify prerequisites, let MOE evidence drive what gets automated | P-001, P-007 |

**The single most important change (D1):** *manage toward a dated MOE-0 and MOE-1, not toward a feature backlog.*

**The flywheel D2 is betting on:** *more estates → more evidence → better decisions → better utilization / cost / reliability → better economics → ability to operate more estates.* D2 funds the substrate (economics + supply optionality + operating intelligence) that makes this loop real rather than rhetorical.

> **Below are the implementation proposals (P-001–P-007) that sit under these decisions.** They are the engineering detail; the executive surface is D1–D4. All are **Proposed, not adopted**; owners/dates stay with the delivery teams. Two were re-scoped per CEO review (2026-09-21): **P-006** is now an *outcome* (control envelope), not "reinstate IAC M4"; **P-001** is *vendor-independent* (Uniphore is a separable choice).

| # | Proposal | Decision | Class | Status |
|---|----------|:--------:|-------|--------|
| **P-002** | Commit to a first [[Minimum Operable Estate]]; name MOE-0 + MOE-1 customer | D1 | **Center of the proposal** | Proposed |
| **P-005** | Empirical Map v1 + evidence-driven routing (the moat) | D2 | **Center of the proposal** (load-bearing) | Proposed |
| **P-003** | Cost-model deliverable (internal cost/GPU-hour) on the Metering pipeline | D2 | Do-now (cheap now, expensive later) | Proposed |
| **P-004** | Supply-abstraction interface before the control plane hardens | D2 | Do-now (cheap now, expensive later) | Proposed |
| **P-006** | Minimum enterprise **control envelope** required for MOE-1 (outcome-framed) | D3 | Re-scoped from "control bundle" | Proposed |
| **P-001** | Narrow fine-tuning: evaluate partner(s) for delivery, RackAI owns integration/serving + learning | D4 | Directional; vendor-independent | Proposed |
| **P-007** | Proof-4 prerequisites as a **dependency declaration** (do not build yet) | D4 | Watch item, not a build ask | Proposed |

## Kill / Falsification Criteria (what would change the thesis)

The proof exits above are **success** criteria. A testable strategy also states what evidence would make us *change the thesis* — otherwise this is an identity we have decided must be true, not a strategy. These are deliberately uncomfortable; that is why they are useful. Leadership should be willing to own them.

| # | Thesis under test | Tested by | Kill / weaken criterion |
|---|-------------------|-----------|-------------------------|
| **K1** | **Customers will delegate operational control** (not just buy private inference) | **MOE-1** | If, by MOE-1, customers value private inference but **will not delegate operational responsibility or pay Rackspace to assume it**, the "Private Enterprise AI Operator" thesis is weakened — reconsider whether RackAI is primarily an **infrastructure platform** rather than an operator. |
| **K2** | **The Empirical Map is a real moat** (cross-workload learning **transfers**) | Empirical Map v1 (P-005) on 2–3 estates | Cross-customer learning is **not automatically valuable just because we collect telemetry.** The thing to prove: something learned from workload/customer A is **transferable enough to improve B while respecting isolation boundaries.** If most useful optimization turns out to be highly **workload-specific**, the flywheel is far weaker than the strategy assumes — the Empirical Map is not a meaningful differentiator and should **not** receive disproportionate investment. Test early. |
| **K3** | **Domain-aligned models beat frontier for our buyers** (the central bet) | Fine-tuning experiment (P-001) | Carried from [[Three Battlegrounds]]: if smaller domain-aligned models fail to reach acceptable quality/cost vs. frontier for the workloads we target, the wedge is wrong. |

K1 and K2 are the two that would most change resource allocation: K1 decides whether we are an operator at all, and K2 decides whether the moat deserves the disproportionate investment D2 asks for. Both are cross-linked to the identity-level scoreboard in [[Three Battlegrounds]].

### P-001 — Fine-tuning: partner the delivery, keep the operations, protect the experiment

**Proposed by:** CEO/product discussion, 2026-09-21. **Status: Proposed — not adopted.**

**The decision (D4, vendor-independent).** *RackAI will not invest in becoming a differentiated fine-tuning product. Fine-tuning **delivery** is a **partner-evaluation problem** — we solve it by evaluating partner(s) in that space (Uniphore the leading candidate), not by building a training toolchain. What RackAI owns is the **integration / model-serving function**: taking the resulting artifact and hosting, serving, and operating it reliably on the fleet.* This maps onto the strategic boundary between what customers build and what Rackspace operates. Which partner wins the evaluation is a **separate, downstream commercial decision** — do not let it stall the strategy decision.

> **The sharper framing (2026-09-28).** The RackAI-owned job here is **integration and model serving**, full stop — the point where a fine-tuned artifact becomes a served, operated, metered [[Model Deployment]] on our fleet. Fine-tuning *delivery* (the training service, data/context assembly, advanced methods) is something we **evaluate partner(s) to solve for**, treating it like any other build-vs-partner integration decision. This is also a **Principle 2 (optionality)** move in the [[#Sequencing Logic — why this order, when we have no demand signal|sequencing logic]]: partner-evaluating delivery avoids committing engineering to a toolchain we may not want, while keeping the serving/operations surface — the part that feeds the [[Empirical Map]] — firmly ours.

**Problem.** "Should we push fine-tuning milestones to a partner and focus early effort on operator-KPI work?" The corpus shows the org already *intends* this — [[RackAI Organizational Design]]: "Fine-Tuning — No REQs required currently — will partner with Uniphore," and the Inference pod's fine-tuning line is `[0/1]` staffed. But "fine-tuning" is three things across the [[Three Battlegrounds|harness boundary]], so a blanket defer is wrong.

**The three-way split.**

| Bucket | Disposition | Rationale |
|--------|-------------|-----------|
| Fine-tuning *delivery* — customer-facing tuning service, data/context assembly, advanced methods (RL/DPO, still "Coming Soon" + unstaffed) | **Evaluate partner(s)** (leading candidate: Uniphore, pending validation) | Business-logic-adjacent; "what customers build." A partner-evaluation/integration decision, not a build. Frees the `[2/8]` Inference pod. **Strategy is vendor-independent**; the winning partner is the implementation choice. |
| Fine-tuning *integration & serving* — taking the artifact and hosting/serving/operating it: placement, utilization, cost-per-job, [[LoRA Adapter]] lifecycle on the fleet | **Keep — ours (the core RackAI job)** | This is the model-serving function — squarely "what we operate"; feeds the [[Empirical Map]] as transferable operating knowledge. The one part we do **not** hand to a partner. |
| Fine-tuning *as strategic experiment* — one domain-model proof point on customer/representative data | **Keep thin — do not zero** | This is the wedge and the **first test of the central strategic bet** ([[Three Battlegrounds]]). Deferring all fine-tuning would defer the proof the operator thesis is viable. |

**What front-loads instead (the operator-KPI enablers already in NOW/NEXT):** cost model (Eng. 0.3), telemetry (0.2), benchmark harness (0.4), metering, compliance-envelope kickoff (dev-plan P1). These move workloads-operated, cost-per-outcome, and compliance-coverage.

**Honest trade-off to weigh before adopting.** SFT is the one capability here that is **shipped and `measured`**; most operator-KPI enablers are `missing`/`planned`. So this proposal trades a working capability's roadmap weight for net-new build — the near-term plan gets *heavier*, not lighter. That can be right, but it should be a conscious choice.

**Dependency / open question (blocks adoption):** the corpus shows the *intent* to partner fine-tuning with Uniphore but not the **commercial/contractual scope** — whether Uniphore is signed to deliver customer fine-tuning as a service, or is only a production tenant (`uniphore.rackai.rax.io`) running its own apps. This determines whether P-001 is "defer to a committed partner" or "defer to a hoped-for partner." **Confirm before adopting.**

**Strategic decision (vendor-independent):** *evaluate partner(s) to deliver fine-tuning; RackAI owns the integration / model-serving function (host, serve, operate the artifact) and retains the experimental capability.* The implementation decision — *leading delivery partner: Uniphore, pending commercial/technical validation; other partners in scope* — is separable, so the strategy does not depend on one vendor negotiation.

**Additional signal (2026-09-28 reviewer feedback).** Fine-tuning infrastructure — specifically **checkpointing + resume** and the broader training stack — appears to be **moving external to Rackspace**. This *reinforces* the P-001 direction: if the toolchain is leaving, do not invest scarce cycles rebuilding it. The line to hold is *host and operate the resulting artifact* (the [[LoRA Adapter]] on the fleet — fine-tuning **operations**, which stays ours), not owning the training toolchain. General principle: don't build ML tooling merely because an AI platform could contain it. See *Cross-Cutting Surfaces → Fine-tuning infrastructure*.

**On acceptance:** (1) move the operator-KPI enablers' priority up explicitly in Proof 1; (2) add "fine-tuning delivery" as a partner scope in [[Load-Bearing Bets]] (preferred: Uniphore, pending validation) with its own exit criterion; (3) keep one instrumented fine-tuning proof point in Proof 2 tied to the central-bet falsification test; (4) confirm whether checkpointing/resume is formally out of scope (moving external) and record it; (5) log a change packet.

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

> **P-003 through P-007 are the strategy-driven changes to the *delivery* roadmap** surfaced by reading the real plan through the operator lens (the ⚠ gaps above). Each names the delivery reality it changes, so it is a concrete edit to the plan — not an abstract wish. All are **Proposed, not adopted**; owners/dates stay with the delivery teams.

### P-003 — Add a cost-model deliverable (ride the Metering pipeline)

**Delivery reality.** Metering M1 (RACKAI-352) builds usage capture (`usage_records`, MeteringEvent, inference + FT metering). **Nowhere in the delivery roadmap is internal cost/GPU-hour modeled** — usage ≠ cost.

**Why it matters (operator lens).** The cost floor is the economics the whole operator identity rests on (Proof 1 commercial gate; [[Three Battlegrounds]] "own the economics"). Without it, every margin/pricing number stays `assumed` and [[Cost per GPU-Hour]] / [[Cost per Outcome]] cannot be computed.

**Proposed change.** Add a small cost-model deliverable *downstream of Metering M1* — attribute the metered usage against fleet cost inputs (power, depreciation/lease, networking, overhead) to produce cost/GPU-hour and cost/1M-tokens. Cheap relative to the metering pipeline it rides on.

**Blocks adoption:** owner (FinOps vs Metering team); dependency on the fleet cost inputs (some are finance data, not engineering).

### P-004 — Add the supply-abstraction interface before the control plane hardens

**Delivery reality.** M2 has "AMD+NVIDIA node support" (RACKAI-263) and "AMD AIM engine" (RACKAI-347) as *features*, and multi-region as Pri-6 backlog — i.e. supply diversity is treated as per-hardware bolt-ons on an **owned-fleet-assuming control plane**.

**Why it matters (operator lens).** "Abstract supply, own economics" ([[Three Battlegrounds]]) requires the control plane to address `SupplyTarget / AcceleratorPool / ExecutionLocation` rather than a specific fleet. The abstraction is cheap to introduce now and expensive to retrofit after IAC/Metering/routing all hardcode owned-fleet assumptions.

**Proposed change.** Introduce the supply-abstraction interface as an architectural requirement in the Platform/Control-Plane workstream; owned H100 is implementation #1, AMD (already in flight) becomes #2 behind the same interface.

> **Naming.** The *interface/mechanism* is the **supply-abstraction interface** (`SupplyTarget / AcceleratorPool / ExecutionLocation`); the *product policy* that rides on it — how much infrastructure choice the customer gets — is **Workload Placement Policy** (see Proof 1). Same architecture, two lenses: the interface preserves supply optionality; the policy decides who chooses. The unresolved product question (customer keeps GPU-level control vs. RackAI selects from workload + constraints, and the GPU-centric quota tension) belongs to the policy.

**Blocks adoption:** architectural review with Team Platform/IAC; confirm it doesn't slow the in-flight AMD work; plus the Workload Placement Policy product decision above (interacts with [[Capacity Pool]] quota definitions).

### P-005 — Empirical Map v1 + evidence-driven routing (the moat)

**Delivery reality.** Inference routing (RACKAI-311) is llm-d + ingress→model + shared KV cache. Telemetry (Platform M1–M2) produces dashboards. **Nothing turns operating data into cross-workload operating decisions** — there is no Empirical Map on the delivery plan.

**Why it matters (operator lens).** This is the single highest-leverage gap. The [[Empirical Map]] flywheel is *the moat* — the reason customer #100 is cheaper than #1 (Proof 2). Routing that reads measured cost/reliability from the map is what makes decisions evidence-informed rather than static. Without it, RackAI is a good serving stack, not an operator that compounds.

**Proposed change.** Add Empirical Map v1 as a first-class delivery workstream (Measurement & Self-Improvement): capture per-workload×model×hardware reliability + cost from the telemetry/metering already being built, with the **transferable-vs-isolated split** designed in from day one; then feed it into routing (extend RACKAI-311's successor to read the map).

**Blocks adoption:** owner (no delivery team owns "measurement/self-improvement" today); depends on Metering M1 + Platform M1–M2 landing first.

### P-006 — Define and fund the minimum enterprise control envelope for MOE-1

*(Re-scoped per CEO review 2026-09-21: framed as an **outcome**, not a fixed engineering bundle. We do not care whether the old IAC M4 is resurrected; we care that MOE-1 has sufficient control boundaries. And we do not hardcode SOC 2 Type I — the required attestation is set by the target customer segment.)*

**Delivery reality.** The delivery plan builds real control-plane pieces (audit, admission control, isolation) but stops short of the identity proof: **(a)** no governed execution harness; **(b)** "compliance validation" is a sub-task of Auditing M3, not a compliance-*evidence* milestone; **(c)** org-level RBAC + metering/billing/quota permissions were **explicitly dropped** (IAC M4 = "Won't Do").

**Why it matters (operator lens).** Proof 3 (Control) is the first proof of the identity. A regulated buyer needs an operating layer to govern (harness), sufficient organizational identity/authorization/quota/policy boundaries, audit, isolation, and the compliance evidence their segment requires.

**Proposed change — the outcome, not the implementation.** Define and fund the **minimum enterprise control envelope required for MOE-1**:
- **Identity / authorization / quota / policy boundaries** sufficient for the MOE operating model. *Whether that means resurrecting IAC M4 or a different deliverable is an architecture decision* — the roadmap sets the outcome, architecture picks the implementation.
- **Governed execution** — a harness v1 sufficient to operate the MOE workload (currently only in the dev-plan strategy source).
- **Audit + isolation** — extend the shipped audit-log API (IAC M3) to the MOE workload.
- **Minimum independently-verifiable compliance evidence required by MOE-1** — *not* a pre-decided SOC 2 Type I. Establish the evidence bar from the **first design-partner profile**, then identify the actual attestation that segment requires. Avoids building compliance because the roadmap says so rather than because the market boundary requires it.

**Blocks adoption:** the MOE-1 customer segment must be named first (its regulatory requirements set the compliance bar — ties to P-002); IAC M4 was dropped for a reason (get it before deciding whether to reinstate); harness and attestation each need a home team and (for attestation) external lead time.

### P-007 — Fund the Proof-4 operator business (sequencing, not "start now")

**Delivery reality.** Multi-region (Pri-6) and GPU-node access (Pri-6) are **backlogged/unscheduled**; there is no day-zero factory, closed-loop optimization, or managed-ops/FDE motion on the plan. Model-lifecycle exists only as fragments (request-new-model, sunsetting).

**Why it matters (operator lens).** Proof 4 (operate a heterogeneous estate, repeatably and profitably) is the actual operator *business*. Multi-region + heterogeneous supply are its prerequisites, and they currently sit at the bottom of the backlog.

**Proposed change.** This is a **sequencing dependency, not a request to start now**: flag that the Proof-4 prerequisites (multi-region, GPU-node access) must leave Pri-6 *before* an external multi-region MOE-1 is viable, and that managed-ops/FDE ([[AI Operations Product]]) needs a delivery home before estates multiply. Adopt as a **watch item** that gates P-002's MOE-1 timing.

**Blocks adoption:** premature to schedule until Proofs 1–3 land; the value now is making the dependency explicit so MOE-1 isn't promised ahead of its prerequisites.

## See Also

- [[Three Battlegrounds]] — the identity this roadmap serves
- [[Minimum Operable Estate]] — the MVP that anchors Proof 3
- [[Load-Bearing Bets]] — the partner portfolio behind it
- [[RackAI Roadmap (Delivery Plan)]] — **primary source**: the actual delivery roadmap this note reorders + extends
- [[Rack AI OpenRouter Engineering Roadmap]] — strategy spine (inference operating system)
- [[RackAI Enterprise AI Development Plan]] — strategy spine (operator stack)
- [[OpenRouter Integration Plan]] — the gated GTM sequence
- [[Capability Gap Register]] — live shipped-vs-planned state
- [[Product Hub]] · [[Rack AI Knowledge Base]]
