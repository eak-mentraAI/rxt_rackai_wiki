---
id: wiki-milestone-release-map
type: index
status: draft
owner: product
domain: strategy
aliases: [milestone release map, release map, roadmap release view, major releases, milestone releases, release train, five-track release map, market roadmap, release narrative]
related: [hub-roadmap, hub-product, hub-battlegrounds, hub-minimum-operable-estate, hub-inference-serving, hub-ai-governance-assurance, hub-ai-harness, hub-model-services, hub-inference-optimization, ent-empirical-map, ent-governed-harness, wiki-pillar-working-model]
source_docs: ["00-hub/RackAI Roadmap.md", "05-wiki/Pillar Working Model.md", "00-hub/Three Battlegrounds.md"]
confidence: derived
last_reviewed: 2026-10-08
parent: hub-roadmap
summary: "Market-and-internal projection of the four-proof roadmap into major milestone releases across five functional tracks."
---

# Milestone Release Map

A **communication projection** of the canonical [[RackAI Roadmap]]. The roadmap is organized around four progressive *proofs* (**Observe → Decide → Assume Responsibility → Operate**) — the right structure for sequencing and gating work, but a hard story to tell a market or a company that thinks in **what shipped and what's next**. This note takes the exact same milestones, gaps, and proposals and re-cuts them onto **five functional tracks**, each expressed as a short sequence of **major milestone releases**. Nothing new is defined here; every item traces to its canonical home and its proof in the [[RackAI Roadmap]].

> **This is a view, not a source.** The [[RackAI Roadmap]] remains the editable, canonical plan; **Craft.io** remains the live *what-and-when*. If a release here disagrees with the roadmap, the roadmap wins and this note is stale. Confidence is `derived` — a re-projection of existing `derived`/`gap` content; no capability is upgraded to shipped, and the live shipped-vs-planned state is the [[Capability Gap Register]].

> **Two axes, one plan.** Proofs are the *temporal* axis (what we can claim, and when). Tracks are the *functional* axis (what part of the system a release advances). Every release below carries its proof tag so the two never drift apart.

---

## Why Re-Cut the Roadmap This Way

- **The four proofs answer "can we claim it yet?"** — the right internal gate, but Observe/Decide/Assume-Responsibility/Operate is not how a buyer, a partner, or most of the org naturally groups the work.
- **The five tracks answer "what did we ship, by area?"** — the way a release narrative, a marketing site, and a pillar team actually think.
- **Both are the same work.** A release is just a proof-item (or a cluster of them) seen through the lens of the subsystem it advances. The map below is the crosswalk.

---

## The Five Tracks

Each track is anchored to the canonical pillar that owns it, so the release view and the [[Pillar Working Model]] stay aligned.

| # | Track | What it is | Canonical owner | The question it answers |
|---|-------|-----------|-----------------|-------------------------|
| **1** | **Core Platform** | The serving substrate: deployments, runtimes, routing, tenancy, control plane, lifecycle, multi-estate operation | [[Inference and Serving Services]] | How do we reliably serve and operate workloads at production scale? |
| **2** | **Governance & Assurance** | The enterprise control envelope: identity, policy, isolation, audit, provenance, compliance evidence, the governed harness | [[AI Governance and Assurance]] + [[AI Harness]] (harness runtime) | What rules must AI activity obey, and how do we prove it inside a customer boundary? |
| **3** | **Learning Loop** | The measurement-and-improvement engine: telemetry, workload characterization, the Empirical Map, evidence-informed routing, closed-loop optimization | [[AI Harness]] (owns the [[Empirical Map]]); fed by [[Inference Optimization]] + [[Inference and Serving Services]] | How does the system measure itself and get better with every estate? |
| **4** | **Model & Inference Bet** | The longer-term wedge: model portfolio, fine-tuning (partner-delivered, RackAI-served), domain-model proof point, engine/accelerator selection | [[Model Services]] + [[Inference Optimization]] | Which models, on which engines/accelerators, win for our buyers? |
| **5** | **Efficiency & Economics** | What the system costs and what it's worth: cost model, metering, unit economics, FinOps, pricing, contribution margin | [[Inference Optimization]] (FinOps) / [[AI FinOps]] | Can we quantify our cost and prove the operator business is attractive? |

> **Mapping to the operating loop.** Tracks 1–5 are not independent product lines — they are the subsystems of the single [[RackAI Roadmap#The Operating Loop — the system the four proofs build|operating loop]] (`meter → characterize → accumulate evidence → decide → route/place → observe → feed back`, wrapped in governance, executed across estates). Track 5 is *meter*, Track 3 is *characterize → accumulate → decide*, Track 1 is *route/place → observe → execute across estates*, Track 2 is the *governance wrapper*, Track 4 is *what gets placed*. The releases are how each subsystem matures.

---

## Capability-Stage Numbering

> **Terminology (2026-10-06).** These are **capability stages**, not committed releases. Each track advances through a short sequence of stages, numbered `T<track>.S<n>` (e.g. **Core Platform S1** = `T1.S1`). The word "stage" is deliberate: `T3.S1` must **not** be read as "Release 1 of the Learning Loop" implying a sequencing or date commitment that hasn't been made. A stage is a **capability milestone, not a date** — dates live in Craft.io, and the only things in this note that are genuine committed *releases* are the two cross-track gates (**MOE-0 → MOE-1**). A stage is "done" when its exit line is true and the proof items it absorbs are shipped.

Each track advances through a short sequence of **capability stages**, numbered `T<track>.S<n>` (e.g. **Core Platform S1** = `T1.S1`).

| Marker | Meaning |
|:------:|---------|
| 🟢 | Shipped / substantially in place today |
| 🟡 | In progress (delivery milestone active) |
| 🔴 | Gap — strategy is ahead of delivery (traces to a `P-00x` proposal) |
| ⚪ | Sequenced later (dependency declared, not started) |

---

## Product-Boundary Decisions (2026-10-06)

Three decisions from the roadmap review that shape what the tracks do and don't contain. Full rationale lives in the canonical [[RackAI Roadmap]]; summarized here because they change how to read the stages above.

| Decision | Resolution | Where it lands |
|----------|-----------|----------------|
| **Supply / placement UX** | *RackAI chooses by default; customers constrain when necessary.* Customer gives intent + constraints (model, SLA, residency, approved vendor, economics); RackAI selects the exact GPU/node/placement/routing. Explicit hardware (NVIDIA/AMD/B300) is a **placement constraint**, not the base consumption model. | T1.S2; enables the T3 Empirical Map to own the placement decision |
| **GPU-node access** | *Out of scope for RackAI.* Direct GPU-node (SSH/raw-node) consumption is GPU IaaS and belongs to the GPUaaS/IaaS product boundary. RackAI's model is "give us the workload + constraints; we operate the environment." | Removed from T1.S4; reinstate only if a concrete RackAI use case requires it |
| **Observability is two products** | *Customer observability* (percentiles, TTFT, TPS, spend, quota — the RackAI product experience) is a distinct surface from *operator intelligence* (GPU/VRAM, queue depth, cache, power, placement signals — feeds the Empirical Map). Same pipeline, different purpose. | Both live in T3.S1 as separate deliverables |

> **A note on "technique" vs "product capability."** Several items that look like roadmap destinations are actually *techniques* in service of an outcome: speculative decoding, Refrag, shared-KV-cache improvements, DPO, AMD AIM, and the semantic router are techniques serving **inference efficiency** or **routing quality** — each earns a place on the roadmap only when evidence (usually the Empirical Map) shows it improves an outcome we care about. The accompanying CSV ([[RackAI Roadmap.csv|RackAI Roadmap table]]) carries an explicit **Type** (Product capability / Technique) and **Disposition** (Committed / Experiment / Decision Required / Gap / Backlog / Out of Scope / Done) column so this distinction is machine-readable, not just prose.

---

## Track 1 — Core Platform

*Owner: [[Inference and Serving Services]]. The serving substrate the whole identity runs on.*

| Capability Stage | Theme | What it delivers | Absorbs (roadmap items) | Proof | State |
|---------|-------|------------------|-------------------------|:-----:|:-----:|
| **T1.S1 — Identity & Serving Foundations** | "We can serve a model with identity and access control" | JWT + API-key validation, APIKey CRD, gateway auth; RBAC (PlatformRole/RoleBinding); inference routing substrate (llm-d, ingress→model, shared KV cache) | IAC M1–M2; M2 Inference routing (RACKAI-311); accelerator inventory & consumption telemetry (RACKAI-336 - telemetry, not selection) | 1→2 | 🟢/🟡 |
| **T1.S2 — Workload Placement & Supply Abstraction** | "RackAI chooses by default; customers constrain when necessary" | Supply-abstraction interface (`SupplyTarget / AcceleratorPool / ExecutionLocation`), owned H100 as impl #1; Workload Placement Policy per the adopted principle (customer gives intent+constraints, RackAI picks GPU/node/placement; explicit hardware = a constraint, not the base model); **workload declaration** surface, step 1 of the AI Operating System loop (2026-10-08) | Workload Placement Policy (P-004 / D2); the interface, not multi-provider scheduling | 1 | 🔴 |
| **T1.S3 — Model Lifecycle** | "Models enter, upgrade, and retire on command" | On-demand model onboarding; model sunsetting; request-new-model flow (SNOW decision open) | M2 Request new model (RACKAI-354); M2 Sunsetting (RACKAI-372) | 4 | 🟡 |
| **T1.S4 — Multi-Estate Operation** | "We operate heterogeneous estates across regions and clouds" | Multi-region support; second supply impl (AMD/partner) behind the interface; day-zero model factory; closed-loop automation. **GPU-node access is explicitly *out of scope*** — that is GPU IaaS, a different product boundary | Multi-region (Pri-6); supply abstraction v1; Proof-4 industrialization (P-007) | 4 | ⚪/🔴 |

**Line of sight:** S1 is real today; S2 is the cheap-now/expensive-later architectural bet (do it before the control plane hardens); S3 is partial; S4 is the operator *business* and is deliberately sequenced last (we do not automate before we operate).

---

## Track 2 — Governance & Assurance

*Owner: [[AI Governance and Assurance]] (rules + evidence) with [[AI Harness]] (the governed-execution runtime). The "control envelope" that lets a customer delegate operation inside their boundary — the [[RackAI Roadmap#The Enterprise Control Plane (the Proof-3 workstream)|Enterprise Control Plane]] workstream, seen as releases.*

| Capability Stage | Theme | What it delivers | Absorbs (roadmap items) | Proof | State |
|---------|-------|------------------|-------------------------|:-----:|:-----:|
| **T2.S1 — Auditability** | "Every sensitive action is a query against the platform" | Audit Log query API; sensitive-access + login + APIKey-lifecycle events | IAC M3 (RACKAI-351); Auditing M1–M3 (pending) | 1→3 | 🟢/🟡 |
| **T2.S2 — Tenant Isolation & Guardrails** | "Workloads are isolated and quota-bounded" | Namespace-per-org isolation; quota enforcement + pre-execution admission control (429/402) | Uniphore single-cluster tenancy; Metering M4 (quota) | 3 | 🟡 |
| **T2.S3 — Enterprise Control Envelope** | "A customer can safely let RackAI operate a workload inside their boundary" | Org-level RBAC/quota/billing permissions (outcome, not necessarily reinstated IAC M4); governed execution harness v1; workload identity; model provenance; action authorization; human-approval gates | P-006 / D3; [[Governed Harness]] v1; [[Agent Identity]]; [[Action Controls]] | 3 | 🔴 |
| **T2.S4 — Compliance Evidence** | "We hold the attestation the target segment requires" | Minimum independently-verifiable compliance evidence set by the MOE-1 customer segment (not a pre-decided SOC 2 Type I); product controls that make certification possible | Compliance envelope kickoff (dev-plan P1); P-006 | 1→3 | 🔴 |
| **T2.S5 — Multi-Cluster Governance** | "The control envelope holds across clusters and estates" | Global front door; multi-cluster governance; govern-and-assure inside the perimeter at estate scale | [[Multi-Cluster Governance Brief (Partner)]]; Proof-4 governance | 4 | ⚪ |

**Line of sight:** S1–S2 are built or building; **S3–S4 are where strategy is furthest ahead of delivery** — there is no harness, no attestation milestone, and org-level RBAC was dropped (IAC M4 "Won't Do"). This track is materially underweight relative to its importance for an enterprise product.

> **Certification is a gate, not the moat.** T2.S4 is what gets us into regulated deals; it does not compound. Build the product controls (S3); certify against them (S4); don't confuse the two.

---

## Track 3 — Learning Loop

*Owner: [[AI Harness]] (owns the [[Empirical Map]] as a decision surface); **fed by** [[Inference Optimization]] (benchmark/efficiency data) and [[Inference and Serving Services]] (serving telemetry). This is the moat — the reason estate #100 is cheaper than #1.*

| Capability Stage | Theme | What it delivers | Absorbs (roadmap items) | Proof | State |
|---------|-------|------------------|-------------------------|:-----:|:-----:|
| **T3.S1 — Telemetry & Observation** | "We can measure cost, performance, utilization, reliability" | Prometheus/DCGM/Grafana GPU dashboards; tenant-attributed service metrics; Loki logs + 13-mo retention; Metrics/Workload-Status APIs; AgentX-anchored benchmark harness | Platform M1–M4; Observability M1; M2 AI Performance Benchmarks ([[AgentX Benchmark Standard]]) | 1 | 🟡/🔴 |
| **T3.S2 — Workload Characterization** | "We can turn real traffic into workload classes" | Analyze actual traffic → [[Traffic Class]] profiles usable as a placement input | Workload characterization (gap → P-005); [[Traffic Class]] | 1→2 | 🔴 |
| **T3.S3 — Empirical Map v1** | "Accumulated evidence improves a decision vs. a static baseline" | Cross-workload evidence store (per workload×model×hardware cost + reliability); the **transferable-vs-isolated split** designed in from day one | Empirical Map v1 (P-005 / D2, load-bearing); [[Empirical Map]] | 2 | 🔴 |
| **T3.S4 — Evidence-Informed Routing** | "Routing reads the map, not a static table" | Smart-routing gateway that reads measured cost/reliability from the Map (static → rules → recommendation) | Evidence-informed routing (P-005); [[Request Routing]] | 2 | 🔴 |
| **T3.S5 — Closed-Loop Optimization** | "Outcomes feed back and the system improves itself" | Observe actual outcome → feed the Map → better next decision; automate what hurts | Closed-loop optimization (P-007); Eng. Phase 6 | 2→4 | ⚪ |

**Line of sight:** S1 is in flight; **S2–S4 are the single most important strategy gap** — telemetry exists, but nothing yet turns operating data into cross-workload decisions. **Prototype S3 (the Empirical Map) first** — it is the highest-information experiment because it tests the differentiated thesis itself (kill criterion [[RackAI Roadmap#Kill / Falsification Criteria (what would change the thesis)|K2]]).

> **Two observability surfaces, don't conflate.** T3.S1 feeds *RackAI operational intelligence* (the operator's view that builds the Map). The *customer observability* product — requests, tokens, TTFT, ITL, percentiles, cost, SLA — is a distinct deliverable that belongs to Track 1's product surface. Same telemetry pipeline, two products.

---

## Track 4 — Model & Inference Bet

*Owner: [[Model Services]] (catalog, fine-tuning operations) + [[Inference Optimization]] (engine/accelerator selection). The longer-term wedge: the bet that the right model on the right engine, selected by evidence, beats frontier-on-generic for our buyers.*

| Capability Stage | Theme | What it delivers | Absorbs (roadmap items) | Proof | State |
|---------|-------|------------------|-------------------------|:-----:|:-----:|
| **T4.S1 — First Model Bet in Production** | "We serve a competitive model on our fleet" | [[GLM 5.3 Flash]] deployment; OpenRouter Path A (real workloads to exercise the system) | Phase 1 Execution Plan — GLM 5.3 Flash; [[OpenRouter Integration Plan]] Phase 1 | 1 | 🟡 |
| **T4.S2 — Multi-Model & Portfolio** | "We run a rotating portfolio, not a single model" | Multi-model operation; the win-now + bet-ahead portfolio ([[DeepSeek V4 Flash]], GLM, [[Nemotron 3 Ultra]]) | Multi-model operation (Eng. 2.5); [[Product Hub]] model bets | 2 | 🟡 |
| **T4.S3 — Fine-Tuning: Served, Not Built** | "We host and operate the artifact; a partner delivers the training" | Fine-tuning **operations** (placement, cost-per-job, [[LoRA Adapter]] lifecycle); SFT/LoRA shipped; delivery evaluated to partner(s), Uniphore leading | P-001 / D4; fine-tuning ops (dev-plan 4.2) | 2 | 🟢/🔴 |
| **T4.S4 — Domain-Model Proof Point** | "A domain-aligned model beats frontier for a target workload" | One instrumented domain-model experiment tied to the central-bet test | Fine-tuning experiment (central bet); [[Three Battlegrounds]] | 2 | 🔴 |
| **T4.S5 — Engine & Accelerator Selection** | "We pick the best engine×accelerator per cell, proven by measurement" | vLLM / AIM / NIM as measured backends behind the serving abstraction; AMD+NVIDIA nodes; selection decided by AgentX-anchored runs under the [[Benchmark Evidence Chain]] (first: [[AMD MI350P Qualification Plan]]), not argument | AMD AIM (RACKAI-347/263); engine question (AgentX); [[Inference Optimization]] Two Layers | 2 | 🟡/🔴 |

**Line of sight:** S1–S2 are the OpenRouter proving ground (subordinate to the operator identity — a gym, not the product); S3 narrows where we differentiate (partner the delivery, keep the serving); **S4 is the central-bet falsification test** ([[RackAI Roadmap#Kill / Falsification Criteria (what would change the thesis)|K3]]); S5 relocates optimization value up a layer — engine tuning is a commodity, *selection* is the moat.

---

## Track 5 — Efficiency & Economics

*Owner: [[Inference Optimization]] (FinOps) / [[AI FinOps]]. What the system costs and what it's worth — the economics the whole operator thesis rests on.*

| Capability Stage | Theme | What it delivers | Absorbs (roadmap items) | Proof | State |
|---------|-------|------------------|-------------------------|:-----:|:-----:|
| **T5.S1 — Metering** | "We capture usage, per tenant, per workload" | Project CRD + usage_records + MeteringEvent pipeline; inference + fine-tuning metering | Metering M1 (RACKAI-352) | 1 | 🟡 |
| **T5.S2 — Cost Model** | "We know our true cost/GPU-hour and cost/1M-tokens" | Monetary cost model on the metering pipeline: GPU-hour cost, power/colo/network allocation, depreciation/lease, storage → cost/token, utilization-adjusted cost | P-003 / D2; [[Cost per GPU-Hour]]; [[Unit Economics Model]] | 1 | 🔴 |
| **T5.S3 — Unit Economics & Margin** | "We can quantify margin per model, workload, and estate" | Revenue/GPU-hour, gross margin/model, contribution margin/estate; pricing hypothesis for operated workloads | [[Gross Margin per Model]]; [[Revenue per GPU-Hour]]; Proof-1 commercial gate | 1→3 | 🔴 |
| **T5.S4 — Operator Leverage** | "The business is software economics, not a labor line" | Workloads-operated-per-ops-FTE; % of decisions automated/assisted; contribution-margin-per-estate improving across estates | North-star metric families; Proof-4 commercial gate | 4 | ⚪ |

**Line of sight:** S1 is in flight; **S2 is the cost floor the whole thesis rests on** and today metering deals only in usage, not monetary cost (do it on the metering pipeline it rides on — cheap now, expensive to retrofit). S3–S4 turn "material progress" into checkable margin numbers; without them every margin/pricing figure stays `assumed`.

---

## Cross-Cutting Consumption Surfaces (how demand reaches the tracks)

Two channels sit *above* the five tracks and pull demand through them. They are not tracks (not subsystems of the operating loop) — they are **consumption surfaces** at the [[Eight-Layer Stack|Consumption layer]]. Both route into the serving chain via Model endpoints; neither is a RackAI platform product (both *consume* RackAI).

| Surface | What it distributes | Audience | Boundary | Proof | State |
|---------|---------------------|----------|----------|:-----:|:-----:|
| **OpenRouter channel** | Model endpoints | External public traffic | A proving ground / gym, kept subordinate to the operator identity | 1→2 | 🟡 |
| **[[Solution Marketplace]]** | [[Packaged Solution|Packaged Solutions]] (agents/apps/harnesses that serve an outcome) | RackAI customers | **RackAI builds the rails (marketplace + Solution SDK + certification + isolation); FDEs author the solutions** | 4 (SDK earlier) | 🔴 proposed |

**Solution Marketplace — capability stages** (proposed; **prototype-first** — build one reusable solution, then extract the standard from it, per [[Solution Marketplace PRD]] §8; mostly Proof 4, S0–S1 start earlier):

| Stage | Theme | What it delivers | State |
|-------|-------|------------------|:-----:|
| **MK.S0 — Reference implementation / learning prototype** | "Build one reusable solution before designing the standard" | FDE builds [[Sovereign Private Assistant]] with the smallest packaging convention; learn common-vs-bespoke (discovers the D-0 package contract) | 🔴 proposed |
| **MK.S1 — Extract the Solution Standard** | "Turn S0's lessons into the SDK + manifest contract" | SDK, capability/permission manifest, binding-policy model | 🔴 proposed |
| **MK.S2 — Two-layer trust gate** | "A third-party solution can run safely in a tenant" | Package certification + per-estate instantiation validation; isolation bar | 🔴 proposed |
| **MK.S3 — Lifecycle + second reference solution** | "Prove re-instantiation; manage versions" | Versioning, upgrade/rollback, revocation, EOL; second solution/estate proves re-instantiation + FDE delivery leverage | 🔴 proposed |
| **MK.S4 — Marketplace surface + catalog** | "Customers discover, instantiate, and are metered" | The catalog, instantiation, consumption metering/attribution | 🔴 proposed |
| **MK.S5 — Third-party / partner / customer authoring** | "Supply beyond FDE" | Open the standard once the trust bar + lifecycle are proven | ⚪ later |

**Concierge Engineer: capability stages** (adopted 2026-10-08, P-008). Unlike the two channels above, this *is* a RackAI product surface: the conversational, user-facing side of the AI Operating System loop (*you tell us what you want, what matters and what you won't compromise; we deliver the how, stay inside your boundaries, and prove what we accomplished*). It spans tracks rather than owning one. Rows in the roadmap CSV; entry/exit criteria in [[RackAI Roadmap]] P-008.

| Stage | Theme | Draws on | Proof | State |
|-------|-------|----------|:-----:|:-----:|
| **CE.S0 — Answer** | "Ask RackAI what is happening and what it costs" | T3.S1 (customer observability, Metrics API), T2.S1 (audit); emits content-free gap signals | 1 | 🔴 |
| **CE.S1 — Act with confirmation** | "RackAI does it, with your approval, under your authority" | T2.S3 (Agent Identity, Action Controls), T1.S2 (workload declaration) | 3 | 🔴 |
| **CE.S2 — Governed autonomy** | "RackAI acts within delegated authority and knows when to stop" | T2.S3 (incomplete-intent rule, authority decision), T3.S3 (Empirical Map, assisted rung) | 3 | ⚪ |

> **Why a marketplace, not just more features.** Each Packaged Solution is a [[Empirical Map|harness×model workload]] (feeds the moat), re-instantiable FDE output (bends workloads/FTE), and a distributable form of the sovereignty promise. It drives consumption — the demand side of Proof 4. **Boundary (2026-10-06 decision):** marketplace/SDK/governance = RackAI product org; solution authoring = FDE → partners → customers. Full definition + open questions (commercial model, sovereign-tenant certification bar): [[Solution Marketplace]].

---

## The Two Headline Releases (what to communicate externally)

The five tracks ladder up to **two cross-track releases** that are the actual market-and-internal story — the identity proofs from the roadmap, expressed as releases:

| Release | What it is | Tracks that must land | Proof | Kill criterion it tests |
|---------|-----------|------------------------|:-----:|-------------------------|
| **MOE-0 — Operator Rehearsal** *(internal/friendly)* | The smallest estate where "we operate your AI" is legitimately true, run on a friendly/internal tenant to build the operating model, runbooks, SLOs, and operational-acceptance gate | T1.S1–S2, T2.S1–S3 (harness v1), T3.S1, T5.S1–S2 | 3 (rehearsal) | — (builds capability; does **not** prove the thesis) |
| **MOE-1 — Identity Proof** *(external/regulated, paid)* | An external enterprise with a genuine private/control requirement delegates operational responsibility **and pays** | MOE-0 + T2.S4 (compliance), T2.S5 / T1.S4 (if multi-region), T5.S3 (margin) | 3 (satisfied) | [[RackAI Roadmap#Kill / Falsification Criteria (what would change the thesis)|K1]] — will customers delegate and pay? |

> **Never conflate them.** MOE-0 is a rehearsal; citing it as "we've proven the operator model" is the specific failure this split exists to prevent. MOE-1 is what satisfies [[RackAI Roadmap#Proof 3 — Assume Responsibility: *We can safely take over a real customer's AI estate*|Proof 3]] and the operator identity — it is the **integration test for the whole strategy**, not one release among many. Canonical definition: [[Minimum Operable Estate]] (the acceptance definition for the Proof-3 gate).

---

## Track × Proof Crosswalk

The one table that proves the two axes are the same plan. Read down for *when we can claim it* (proof), read across for *what subsystem advances* (track).

| Track \ Proof | 1 Observe | 2 Decide | 3 Assume Responsibility | 4 Operate |
|---------------|-----------|----------|-----------|-----------|
| **1 Core Platform** | T1.S1 (identity/serving) | T1.S1 (routing) | — | T1.S2–S4 |
| **2 Governance & Assurance** | T2.S1, T2.S4 (kickoff) | — | T2.S1–S4 | T2.S5 |
| **3 Learning Loop** | T3.S1–S2 | T3.S2–S4 | — | T3.S5 |
| **4 Model & Inference Bet** | T4.S1 | T4.S2–S5 | — | — |
| **5 Efficiency & Economics** | T5.S1–S3 | — | T5.S3 | T5.S4 |
| **Cross-track** | — | — | **MOE-0 → MOE-1** | **MOE-1** |

**What the crosswalk shows:** delivery is strong in the **Observe** column (measurement substrate), thinning across **Decide** (the Learning Loop gaps), thin in **Control** (the governance gaps), and sparse in **Operate** (the operator business is not yet funded). That diagonal of 🔴/⚪ in the lower-right is the agenda — the same conclusion the [[RackAI Roadmap]] reaches, now readable by functional area.

---

## How This Maps to the Four Executive Decisions

The releases are not a parallel ask — they implement the same [[RackAI Roadmap#Proposed Changes → Four Executive Decisions|four executive decisions (D1–D4)]]:

| Decision | What it approves | Releases it funds |
|:--------:|------------------|-------------------|
| **D1** | Reorient around MOE-0 → MOE-1 | The two headline releases (above) |
| **D2** | The substrate that improves with scale | T5.S2 (cost), T1.S2 (supply optionality), **T3.S3 (Empirical Map — load-bearing)** |
| **D3** | The enterprise control envelope for MOE-1 | T2.S3–S4 |
| **D4** | Narrow where we differentiate | T4.S3 (partner fine-tuning delivery), and *not* building T1.S4/T3.S5 prematurely |

---

## How to Use This Note

- **For market / marketing:** lead with the five tracks and the two headline releases. The 🟢/🟡 items are the "available today / shipping now" story; the 🔴/⚪ items are "on the roadmap" — do not represent them as present (confidence `gap`/`assumed`).
- **For internal planning:** use the Track × Proof crosswalk to see where a track's next release is blocked on a proof gate, and the D1–D4 table to tie a release to its funding decision.
- **For edits:** change the [[RackAI Roadmap]] first (the canonical plan), then re-project here. This note must never carry a capability the roadmap doesn't — if they diverge, this note is stale.

---

## See Also

- [[RackAI Roadmap]] — **the canonical plan this note projects** (four proofs, delivery milestones, P-001–P-007, D1–D4)
- [[Minimum Operable Estate]] — the MVP behind MOE-0 → MOE-1
- [[Pillar Working Model]] — the pillar ownership the five tracks map to
- [[Three Battlegrounds]] — the operator identity the releases serve
- [[Capability Gap Register]] — live shipped-vs-planned state (the authority on 🟢/🟡/🔴)
- [[Empirical Map]] — the Track 3 moat
- [[Solution Marketplace]] — the second consumption channel (cross-cutting); [[Packaged Solution]] · [[Sovereign Private Assistant]]
- [[Product Hub]] · [[RackAI Platform]]
