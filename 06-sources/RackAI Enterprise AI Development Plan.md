---
id: src-rackai-dev-plan
type: source
status: draft
owner: rackai-product
domain: strategy
aliases: [dev plan, development plan, rackai dev plan, enterprise ai development plan, five programs]
related: [hub-product, hub-root, hub-governance, hub-roadmap, src-strategic-vision, src-engineering-roadmap, src-rackai-org-design]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-product
summary: "Faithful markdown companion of the BU dev plan: five programs + productization/ops on two tracks (dev/research), built on RackAI as foundation."
---

# RackAI & Enterprise AI — Development Plan

> **Companion note.** Faithful markdown representation of `reference/rackai_dev_plan 2.docx` (added 2026-09-17 by the BU business leader). This is a *raw source projection*, not a canonical note — concepts here are extracted into the graph separately and tracked in [[Source Inventory]] and [[Source-to-Concept Crosswalk]]. Content preserved as written; only formatting was normalized. The one embedded image (architecture diagram) is referenced by filename rather than embedded, per the operating standard.
>
> **Confidence:** `assumed` — this is a working draft setting direction, not a validated spec. Planned capabilities here carry `assumed` confidence until shipped reality confirms them.

---

*Working draft, internal. Sets the direction — the programs, tracks, and priorities — for the PM team to break into detailed backlog. The thesis and market view live in a separate, evolving document.*

## The lay of the land

Where we sit before the detail:

- **The stack.** Enterprise AI runs on an eight-layer stack — consumption, orchestration, harness, inference, model, data, compute, infrastructure — wrapped by three control planes (governance, assurance, operations). The full picture is in the architecture reference at the end.
- **What we own.** RackAI is our own platform, from the infrastructure up to the inference layer — sovereign/private cloud, compute, model hosting and adaptation, serving, routing. It's under development, and it's the foundation this plan builds on.
- **What we build on top.** The Enterprise AI offering — the governed, operated layer that turns the stack into something a regulated enterprise can run. That layer, plus hardening RackAI itself, is what this plan is.
- **What we integrate, not build.** For now we sit above the data layer and integrate with whatever data foundation the customer has (their own, Palantir, or Uniphore); the customer holds their own data and weights. Partners cover pieces of the stack; we assemble, govern, and operate the whole.
- **How the work is organized.** Five programs, plus the productization and operations items, all building on top of RackAI — run on two tracks: a dev track (what the RackAI team builds) and a research track (what a small team works ahead on). The programs are what we build; the tracks are who builds them and when. Table 1 lists our dev and research items by track; Table 2 sets the whole stack out by layer — what RackAI and partners already cover, and what we build or research — so RackAI's part and the gaps this plan fills are both explicit.
- **Where the gaps are.** Much of the stack exists in the products today — consumption, serving, model catalog, data fabric, the substrate. What's thin or missing clusters in the governed middle and the moat: the harness runtime, measurement, verification, the loop, and the sovereign governance edges. That's what this plan builds and researches. Table 2 has the layer-by-layer detail.

The rest of this document is the detail: the offerings, the programs and their threads, the work by track (Table 1), the coverage and gaps (Table 2), and the architecture.

## Rackspace AI offerings (for now)

Three offerings, at different levels of the stack:

- **Inference — RackAI.** Rackspace's own platform, from infrastructure up to the inference layer: sovereign/private cloud, compute, model hosting and adaptation, serving, routing. Under development.
- **Palantir.** A packaged partner product (Foundry / AIP) that sits on top of compute — ontology, authorization, provenance, context assembly, data.
- **Enterprise AI.** The governed, operated offering built on top: it uses RackAI as its inference foundation and Palantir as a packaged component, and adds the governance, assurance, and operating discipline that make it something a regulated enterprise can run.

This plan does two things: **enhance RackAI** (harden and extend the inference platform) and **build the Enterprise AI offering** (the governed, operated layer on top). RackAI is the foundation the programs assume; for now, we build above the data layer — we integrate with whatever data foundation the customer has (their own, Palantir, or Uniphore) rather than providing one, and the customer holds their own data and weights.

## The programs

The work is organized into programs — groupings of related threads, each thread a single problem we build or research. The programs mirror the architecture, so they're a stable way to hold the work even as priorities and staffing shift. Five of them, plus the productization and operations items that shipping a product requires.

- The work splits into **five programs**. The first three follow our architecture:
  - **Program 1** — the stack itself (including building the empirical map).
  - **Program 2** — the governance and assurance planes around it.
  - **Program 3** — the learning loop that measures and improves the system.
  - **Program 4** — a longer-term bet on the model and inference layer.
  - **Program 5** — what the system costs and what it's worth.
- Threads are numbered by program (1.1, 1.2, and so on); the table at the end gives each one a skill and a layer.
- Under a thread: *Develop* is engineering we can start now, *Near-term research* is research we can start now, and *Long-term research* is what stays open until that near-term work exists.

**A note on the architecture.** These programs sit on our eight-layer AI stack (consumption, orchestration, harness, inference, model, data, compute, infrastructure), wrapped by three control planes — governance and assurance (AI-specific), plus operations (the general-platform controls: identity and access, lifecycle, action controls, incident response, supply chain) — and cut by two axes, cost and lifecycle. Most of operations is operator practice, not research; the one research thread it surfaces is agent identity (2.5). Human-in-the-loop — approval, handoff, intervention — sits in consumption and operator practice, not in these programs.

**One effort, two tracks.** This is a single integrated program — dev and research together, owned and sequenced as one. Within it, the work runs on two tracks:

- **Dev track (near-term)** — what the RackAI team builds: Programs 1 and 2, plus the productization and operations work (P1–P9). This is the near-term reality and where most of the headcount goes.
- **Research track (runs ahead)** — what a small team works ahead on: the open problems in Programs 3, 4, and 5 — above all the moat: verification, the loop, and self-modification. It runs ahead so its output is ready when the dev track needs it.

**Productization and operations.** The five programs cover the platform and its research. Shipping and running RackAI as a product takes more than that: the product surface, the test-and-release machinery, the run-the-service operations, and the compliance that makes the sovereign claim real. These are the P1–P9 items — first-class dev-track work, and where the operations control plane gets built. The section below has the detail.

The programs are ordered build-first, but the tracks aren't a wall — a few threads start as build and grow a research tail (1.2, 1.4, 2.2, 2.5, 5.1). Those are the hand-off seams, where a research thread feeds a dev one (the map, verification, safe update). The seams are the one place to be explicit in the hand-off to the PM team, because they cross two owners; everything inside a thread is the owning PM's to break down. The table at the end tags every item by track.

## Program 1 — Build and operate the governed harness

Program 1 builds the governed harness and runs it. The governed harness is three things: the harness layer, the orchestration layer above it, and the governance and assurance planes around it (Program 2). An enterprise runs many harnesses, not one — one for coding, one per agent or domain — each with its own tools, prompt, and context. So we build a repeatable pattern for a harness, prove it on one real workload, make the runtime durable, then build the orchestrator that runs across the many. It also builds the empirical map (1.5) — the record of where each model is reliable and what it costs. The pieces keep moving, so re-integration never stops. This is the near-term engineering core; the research is at the edges, in the harness and the routing.

**1.1 Multi-model environment.** We can't compare local open-weight models and frontier APIs today, because we have nowhere to run them on the same workload.

- *Develop:* several models behind one interface, one workload run against all of them, results in one place.

**1.2 Harness layer.** A raw model isn't reliable on its own. The same model behaves very differently depending on the scaffolding around it: context, tools, memory, control flow, guardrails. Context means pulling the right internal data into the model — data that's messy, spread across systems, and limited to what each user may see. We'll run many harnesses, so the goal is a repeatable pattern, not one build.

- *Develop:* the harness pattern, proven on one workload, so it repeats across domains.
- *Long-term research:* pulling in the right data even when the sources are messy, and showing each user only what they're allowed to see; and memory management over long tasks — keeping, dropping, or resurfacing the right context (the deep version is 3.3).

**1.3 Reliability and runtime.** Agents built on ad-hoc scripts don't survive production. A restart loses context, and you can't snapshot and replay a non-deterministic system the way you can ordinary software.

- *Develop:* a durable, observable runtime that can replay and recover a run, with cost per outcome measured from day one.
- *Long-term research:* dependable behavior from undependable parts, and observability when every run takes a different path.

**1.4 Orchestration and routing.** With many harnesses across different domains, something has to send each task to the right harness, model, or human. Always picking the strongest model is wasteful; always picking a cheap one is risky. The same choice across a whole workload, not one step, is build-versus-buy: when a fine-tuned small model beats renting a frontier one.

- *Develop:* an orchestration layer across harnesses, with simple routing to start — the cheapest executor, at the edge or the core, that clears a fixed reliability bar. Cost is a first-class input: routing reads measured token cost per workload (from 1.5), not just reliability.
- *Near-term research:* find the small-versus-frontier crossover from the map.
- *Long-term research:* a learned optimizer — cost and reliability estimates with a search over plans, on a map that keeps moving — that also keeps the build-versus-buy line current as prices and models change. Shared with 3.2.

**1.5 Per-workload measurement.** A benchmark measures the model, not this workload with these tools and this context. Start simple: run a workload against several models, apply checks, record what each did and what it cost. This is the empirical map — the record of where each model is reliable and what it costs — which routing (1.4) reads and the learning loop (Program 3) builds on. Builds on 1.1.

- *Develop:* the eval framework — one workload, several models, results and cost in one place.
- *Long-term research:* how much measurement is enough to trust a cell of the map, and whether it predicts production behavior.

## Program 2 — Govern and assure the system inside the perimeter

Program 2 is the control plane around the others. It enforces policy while the system runs, and shows afterward that it behaved. It starts as a thin governance layer in Program 1's first workload and grows to cover everything we run.

**2.1 Governance, accountability, and provenance.** In a regulated setting we have to enforce policy as the system runs, and show afterward what happened and who's answerable when an agent gets something wrong. The provenance record matters most, since every later claim is checked against it.

- *Develop:* policy enforcement and a provenance-and-replay record, built into the first workload.
- *Long-term research:* a provenance record complete enough to reconstruct and defend any run.

**2.2 Agentic security.** An agent with tools and data access is exposed to prompt injection and cross-tenant leakage. The harder problems come later, once the attack surface moves to the semantic layer, past what access lists and pattern-matching catch.

- *Develop:* the baseline with the first workload — tenant isolation and first-line prompt-injection defenses.
- *Long-term research:* leakage where harmless pieces add up to something sensitive, and hijacking. Authorizing an agent by what it's trying to do sits in 2.5, since it depends on knowing the acting identity.

**2.3 Perimeter information-flow control.** "Policy not walls" means frontier models and protected data can work together inside the perimeter — but only if we control what data reaches which model, and can prove it.

- *Long-term research:* decide at context-assembly time what data may reach which model or jurisdiction, including whether it may leave the edge for the core, and prove afterward that it did.

**2.4 Governable self-modification.** A system that improves itself changes its own behavior. That works against what a regulator certifies — that it still behaves as it did when approved. Same seam as 3.3, from the audit side.

- *Long-term research:* version, attribute, replay, and re-certify a system that rewrites itself.

**2.5 Agent identity and delegated authority.** A person has a stable identity and a role; an agent doesn't. It acts on behalf of a user, often several hops deep, spawns sub-agents, and calls tools with borrowed credentials. So at each step we have to know who is acting and whose authority they carry, with permissions scoped down to the task rather than inherited whole. This sits upstream of 2.2 and 2.3 — you can't authorize by intent or control data flow until you know the acting identity.

- *Develop:* the baseline — service identities for agents, scoped tokens, tenant isolation, consumed from the stack where it exists.
- *Long-term research:* identity for agents that delegate to sub-agents; authority scoped to intent and revoked when the task ends; and proving after the fact which identity did what.

## Productization and operations

Introduced above: the P1–P9 items are the build-and-run work beyond the five programs, all dev-track. Ownership is assumed to be ours for now, so nothing is dropped; two are flagged as handoff candidates to the broader operator org, and one (P1) is non-negotiable.

This is also where the operations control plane gets built. Operations is mostly practice, not research — so rather than a program of its own, it's realized here: P4, P5, P8, and P9 are the operations-plane work (lifecycle, run-the-service, action controls, supply chain), and its one genuine research thread is agent identity (2.5). Productization is broader than operations, though — the product surface (P2), eval (P3), and certification (P1) are product and quality work, not operations — which is why this section keeps the wider name.

**P1 Compliance and certification.** SOC 2 and the sovereign/regulated attestations the whole offering rests on. Long lead time, gates whether a regulated buyer can adopt at all, and it is the substance of the "sovereign, governed" claim. *Non-negotiable; start first.*

**P2 Product surface.** The API, SDK, console/dashboard, docs, and onboarding — the front door to RackAI. This is RackAI's product surface, distinct from Uniphore's consumption apps.

**P3 Eval as CI.** Regression suites, release gating on eval results, and "did this model swap break anything." The engineering discipline that sits on top of the eval framework (1.5) and lets model and policy changes ship safely.

**P4 Release and deployment engineering.** Staged rollout, canary, rollback, and versioning across the fleet — the plumbing version of safe change, feeding and fed by the research on safe online update (3.3).

**P5 Run-the-service operations.** SLA, monitoring, alerting, on-call, incident response. *Handoff candidate — may sit with the broader Rackspace operator org; owned here for now so it isn't dropped.*

**P6 Support and customer-success engineering.** Debugging a customer's misbehaving workload, and the tooling behind it. *Handoff candidate.*

**P7 Feedback and ground-truth data ops.** Curating the labeled outcomes and human feedback that verification (3.1) and the loop (3.3) learn from and check against. It's a dependency of both, so it needs a clear owner.

**P8 Action controls and blast radius.** Gating what an agent can do to the world — approval gates, rate limits, reversibility, containment. The operations-plane control on outbound actions; authorization by identity is upstream in 2.5.

**P9 Supply chain and config inventory.** What's in the running system — models, prompts, tools, components — and its provenance and versions. The operations-plane inventory a regulator will ask for; partly covered by a data-fabric product today.

*The programs above are the near-term build; those below are the research that runs ahead of it. It's one effort — the split is which track leads each, not a wall between them.*

## Program 3 — Measurement and self-improvement

The empirical map is built in Program 1 (1.5): a living record of where each model is reliable and what it costs, from our own operating data rather than public benchmarks. Program 3 is the research that runs on top of it — verifying each step, planning the loop, and improving the system with use. A model vendor can't do this, because it only comes from operating inside the perimeter. This is the research-led, compounding part of the plan, and it feeds Program 5.

**3.1 Verification.** Verification checks each step of a run, not just the final answer. The same check does three jobs: it shows where a model is reliable, it's the reward signal the learning loop trains against, and it's the evidence assurance needs. The cheap default — one model grading another — is biased and won't satisfy an auditor. This is the hardest problem in the program.

- *Near-term research:* where the task allows, check a step with code or a proof instead of another model's opinion; where it doesn't, have the check say how sure it is and hand off to a person when it isn't sure.
- *Long-term research:* make those checks reliable and cheap enough to run on every step, and find a way to tell whether open-ended work went well that the system can't game.

**3.2 Loop planning and credit assignment.** Routing (1.4) picks a model for one step. Planning the whole loop is harder: how to break up the task, one agent or several, when to verify, when to stop — all for the lowest cost per outcome. To plan well you have to score the steps and credit the one that earned the result, so planning and credit assignment are the same problem.

- *Long-term research:* score multi-step work and predict failure early; credit the right step, even for effects that show up late; and plan the loop against the map. The deep version of 1.4.

**3.3 Stable, governable self-improvement.** A system can improve in a few places. It can update its weights, which means reinforcement learning against the reward signal from 3.1. Or it can change lighter things — memory, skills, prompts, routing — that leave the weights untouched and are easier to audit and undo. So the first question is when weight-level RL is worth it and when a lighter change will do. Wherever the learning sits, it has to stay stable and roll out safely.

- *Long-term research:* which path carries the learning; learning without drift; updating a live regulated workload safely, with shadow eval, canaries, and rollback; and making learning in one workload help the next without moving data. That last part is the moat. Same seam as 2.4, from the learning side.

## Program 4 — Model and inference (the maturity bet)

Programs 1 to 3 build the system now. Program 4 is a longer-term bet: serve, optimize, and adapt models on our own hardware as we mature. It stays true to the thesis because it's operating work on AMD and adaptation of others' models, not model-building. Little of it starts in year one. It's where a second researcher would sit — an inference-optimization profile, not the learning-loop one.

**4.1 Inference optimization.** AMD's ROCm stack is younger than CUDA's, so the tricks that cut cost and latency — quantization, KV-cache reuse, speculative decoding, batching — don't come for free, and what works on NVIDIA may not port. The problem is frontier-grade serving economics on AMD, held as models and kernels change, without the perimeter's governance overhead canceling the gains.

- *Near-term research:* serving optimizations on ROCm that hold up as the stack moves.
- *Long-term research:* close the cost-and-latency gap with the more mature NVIDIA stack.

**4.2 Fine-tuning for evolving data.** In a live enterprise the facts move — new products, policies, tickets — so a model tuned last quarter goes stale. The problem is keeping it current as its data changes, without a full retrain each time and without forgetting what it knew. This is the weight-level path of 3.3, run continuously.

- *Long-term research:* keep a model current as its data shifts, without forgetting and without a full retrain.

**4.3 Model explainability for governance.** A regulator wants to know why a model made a given decision, and today's explainability methods can't answer that in a way you could defend. We need explanations good enough for a specific governance claim, not general interpretability. This is closer to a research frontier than a deliverable.

- *Long-term research:* explanations a regulator would accept for a specific decision, not general interpretability.

**4.4 Edge–core inference.** Some work has to run at the edge — for latency, or because the data can't leave the region — and some is cheaper or only feasible in the core. The problem is splitting inference across the two: what runs on constrained edge hardware, when to escalate to the core, and how to place a model, or parts of it, under latency and residency limits.

- *Long-term research:* split inference across edge and core under latency and residency limits — small models at the edge, escalation to the core, or one model split across both.

## Program 5 — Economics of the running system

Programs 1 to 4 build, improve, govern, and differentiate the system. Program 5 is about cost: measuring it and bringing it down. It works at two levels. One is the cost of the AI work itself — cost per outcome, read from the map. The other is the cost of the physical substrate — metering the data centers and optimizing them. The first is a cost platform with modeling and pricing on top — engineering plus a finance or analytics partner. The second is infrastructure operations. Both are measure-then-optimize.

**5.1 Economics of a running system.** Deeper than routing cost. Two questions: which model pays off when, and how to price and forecast a system whose cost per run varies by design, where one edge case can cost many times a normal run.

- *Develop:* an AI FinOps platform — pull together the cost data from 1.3, attribute it by workload, tenant, and outcome, and provide budgets, showback, and dashboards.
- *Near-term research:* a way to reason about cost per outcome from the map, not from assumptions.
- *Long-term research:* price and forecast a system whose cost per run varies by design.

**5.2 Data-center metering and optimization.** We operate the physical substrate — GPUs, power, cooling, racks — across edge sites and core data centers, but most of it isn't measured finely enough to optimize. Meter it first: power draw, GPU utilization, cost per node, idle capacity, in one place. Then optimize: pack and schedule workloads to raise utilization and cut cost and power across the fleet, as demand shifts.

- *Develop:* fleet-wide metering, and first-pass optimization — basic packing and scheduling.
- *Long-term research:* principled fleet optimization — utilization, cost, and power together, as demand moves.

**The cost loop (tokenomics), across the threads.** Accounting for token spend and then routing on it isn't one thread — it's a loop that runs across four of them, and it's worth naming so it doesn't fall between sections:

- **Meter** — measure token spend per request, tenant, and outcome. Instrumented in the runtime (1.3) and recorded as the cost dimension of the map (1.5).
- **Govern** — budgets, quotas, and showback: what's allowed to spend. The cost-governance / FinOps work (5.1), on the Governance plane.
- **Route** — send each step to the cheapest executor that clears the reliability bar, reading measured cost from the map (1.4).
- **Reason** — turn the metered data into cost-per-outcome and pricing (5.1).

The metering is the shared spine: the same token-cost data feeds the budget controls, the routing decision, and the economics. Build it once, in the serving path, and the rest reads from it.

## Work at a glance

### Table 1. The work — every program thread and productization item — by track, skill, and kind of work.

What the team builds and researches: all program threads plus the productization and operations items (P1–P9), each tagged by track (dev or research), the skill it needs, and whether it's develop or research work. This is the hiring-and-sequencing view — read it to see who does what and in what order. What already exists in the stack or sits unowned is in Table 2, not here.

Skill: Developer (strong programmer, early-career), Architect (systems design, staff), Researcher (open problems, PhD-level). Combined entries list the main skill first; an arrow (Architect → Researcher) means the thread starts as engineering and grows into research. Track marks whether an item is dev (the RackAI team builds it) or research (the research team works it ahead); "Dev → Research" is one that starts as build and grows a research tail. **R** on a dev item marks work RackAI already delivers today (consistent with the R in Table 2) — the in-flight foundation, as opposed to new build. The table runs top to bottom through the architecture — "overall" first, then the three control planes, then the layers — and ends with the productization and operations items (P1–P9).

| Layer / plane | Thread | Track | Skill | Work |
|----|----|----|----|----|
| Overall | 5.1 Economics of a running system | Dev → Research | Architect → Researcher | Develop · Near-term research · Long-term research |
| Governance | 2.1 Governance, accountability, provenance | Dev | Architect / Developer | Develop · Long-term research |
| Governance | 2.3 Perimeter information-flow control | Research | Researcher | Long-term research |
| Governance | 2.4 Governable self-modification | Research | Researcher / Architect | Long-term research |
| Assurance | 3.1 Verification | Research | Researcher / Architect | Near-term research · Long-term research |
| Assurance | 2.2 Agentic security | Dev → Research | Architect → Researcher | Develop · Long-term research |
| Operations | 2.5 Agent identity and delegated authority | Dev → Research | Architect → Researcher | Develop · Long-term research |
| Orchestration | 1.4 Orchestration and routing | Dev · R → Research | Architect → Researcher | Develop · Near-term research · Long-term research |
| Orchestration | 3.2 Loop planning and credit assignment | Research | Researcher / Architect | Long-term research |
| Harness | 1.2 Harness layer | Dev | Architect / Developer | Develop · Long-term research |
| Harness | 1.3 Reliability and runtime | Dev | Architect / Developer | Develop · Long-term research |
| Harness | 1.5 Per-workload measurement | Dev | Architect / Developer | Develop · Long-term research |
| Harness | 3.3 Stable, governable self-improvement | Research | Researcher | Long-term research |
| Inference | 1.1 Multi-model environment | Dev · R | Developer | Develop |
| Inference | 4.1 Inference optimization | Research | Architect / Researcher | Near-term research · Long-term research |
| Inference | 4.4 Edge–core inference | Research | Architect / Researcher | Long-term research |
| Model | 4.2 Fine-tuning for evolving data | Research | Researcher | Long-term research |
| Model | 4.3 Model explainability for governance | Research | Researcher | Long-term research |
| Compute / Infrastructure | 5.2 Data-center metering and optimization | Dev → Research | Architect / Developer | Develop · Long-term research |
| Productization / Ops | P1 Compliance and certification | Dev | Architect / Developer | Develop (non-negotiable) |
| Productization / Ops | P2 Product surface (API, SDK, console) | Dev | Developer / Architect | Develop |
| Productization / Ops | P3 Eval as CI | Dev | Developer / Architect | Develop |
| Productization / Ops | P4 Release and deployment engineering | Dev | Architect / Developer | Develop |
| Productization / Ops | P5 Run-the-service operations | Dev | Architect / Developer | Develop (handoff candidate) |
| Productization / Ops | P6 Support and customer-success engineering | Dev | Developer | Develop (handoff candidate) |
| Productization / Ops | P7 Feedback and ground-truth data ops | Dev | Developer / Architect | Develop |
| Productization / Ops | P8 Action controls / blast radius | Dev | Architect / Developer | Develop |
| Productization / Ops | P9 Supply chain / config inventory | Dev | Developer / Architect | Develop |

The long-term-research threads aren't lower priority. They come later only because they need the near-term work first. A few — 3.3, 2.3, 2.4 — are the moat: the part a model vendor can't build from outside the perimeter.

## Stack and partners: coverage and gaps

### Table 2. What the stack already covers versus what we build, integrate, or partner for.

For each capability, this shows what exists in the products today (RackAI, Uniphore, Palantir), what we build or research near-term, and what's long-term — in-house or, where a partner could accelerate it, with Across.AI or a similar partner (candidate, pending diligence). It's the build-versus-consume-versus-partner view: read it to see where we lean on the stack and where the gaps are.

This maps the eight architecture layers plus the three control planes to what already exists in the stack we're assembling — RackAI (R) and Uniphore (U) — against our own research plan, and shows where a partner could accelerate the long-term work. Across.AI (A) is the candidate we've identified, pending due diligence; a similar partner could fill the same role. It's a build-versus-consume-versus-partner view of the same threads.

**RackAI is the foundation.** This plan builds on RackAI and extends it. RackAI's offering runs from the infrastructure up to the inference layer — sovereign/private cloud, compute, model hosting and adaptation, serving, routing — plus the governance and assurance we build into it. For now we build above the data layer: we integrate with the customer's data foundation — their own, Palantir, or Uniphore — rather than providing one, and the customer holds their own data and weights. So the programs below assume RackAI's inference-and-below foundation and add the governed, operated layer on top of it.

**How to read it.** *In product* is coverage today: ✓ shipping, ~ partial or planned, ⚠ claimed in marketing but unverified, — none (the letter says which product: R RackAI, U Uniphore, P Palantir). *D/S* is our near-term work: D develop, S short-term research. The last column is our long-term research: **L** in-house, **L+A** long-term work a partner could accelerate (~ marks partial). Product marks are from public positioning and should be checked against actual roadmap and contract scope; the ⚠ rows especially are diligence items. Across.AI is the partner candidate we've identified for the L+A work, pending due diligence, and its marks are early and unproven.

| Layer / plane | Feature | In product | D/S | L / L+A |
|----|----|----|----|----|
| Governance | Runtime policy enforcement (2.1) | ~R/U | D |  |
| Governance | RBAC at agent/tool/data (2.1) | ~R/U/P | D |  |
| Governance | Provenance + replay (2.1) | ~U/P | D | L+A |
| Governance | Cost governance / FinOps (5.1) | ~R | D S |  |
| Governance | Governable self-modification (2.4) | — |  | L+A |
| Assurance | Guardrails / PII (2.2) | ⚠U | D |  |
| Assurance | Observability / tracing (1.3) | ~R ⚠U | D |  |
| Assurance | Prompt-injection defense (2.2) | ⚠U | D |  |
| Assurance | Tenant isolation (2.2) | ~R/U | D |  |
| Assurance | Trustworthy per-step verification (3.1) | — | S | L+A |
| Assurance | Failure prediction / scoring (3.2) | — |  | L+A |
| Assurance | Semantic-layer security (2.2) | — |  | L |
| Operations | Agent identity + delegated authority (2.5) | ~R/U | D | L+A |
| Operations | Baseline RBAC / service identity / tokens (2.5) | ~R/U | D |  |
| Consumption | End-user assistant / chat | ✓U |  |  |
| Consumption | Prebuilt business apps | ✓U |  |  |
| Consumption | No-code app/agent builder | ✓U |  |  |
| Consumption | Multi-channel I/O | ✓U |  |  |
| Orchestration | Route step to right model (1.4) | ~R/U | D |  |
| Orchestration | Routing off a measured map (1.4) | — | S | L+A |
| Orchestration | Multi-agent coordination (3.2) | ~U |  | L+A |
| Orchestration | Route to a human (1.4) | ~U | D |  |
| Orchestration | Whole-loop planning (3.2) | — |  | L+A |
| Orchestration | Build-vs-buy over a workload (1.4) | — | S | L |
| Harness | Context assembly / grounding (1.2) | ✓U/P | D |  |
| Harness | Tool use / integrations (1.2) | ~R/U | D |  |
| Harness | Guardrail checkpoints (1.2) | ⚠U | D |  |
| Harness | Repeatable harness pattern (1.2) | ~R/U | D |  |
| Harness | Durable, replayable runtime (1.3) | — | D | L+A |
| Harness | Long-horizon memory mgmt (1.2) | — |  | L+A |
| Harness | Learning loop from traces (3.3) | ⚠U |  | L+A |
| Harness | Safe online update (3.3) | — |  | L+A |
| Harness | Transfer across deployments (3.3) | — |  | L |
| Inference | Multi-model environment (1.1) | ✓R | D |  |
| Inference | Model serving runtime | ✓R/U |  |  |
| Inference | Gateway / BYOK | ✓U |  |  |
| Inference | Per-tenant token accounting (5.1) | ~R/U | D |  |
| Inference | Inference optimization AMD/ROCm (4.1) | — | S | L |
| Inference | Edge–core inference split (4.4) | — |  | L |
| Model | Model catalog | ✓R/U | D |  |
| Model | Fine-tuning / adaptation | ✓R/U |  |  |
| Model | Fine-tuning for evolving data (4.2) | ⚠U |  | L |
| Model | Per-workload measurement / map (1.5) | — | D | L+A |
| Model | Verification: reward + audit (3.1) | — | S | L+A |
| Model | Regulator-defensible explainability (4.3) | ⚠U |  | L+A |
| Data | Data fabric / connectors | ✓U/P |  |  |
| Data | Permission-aware retrieval, query-time (1.2) | ~U/P |  | L |
| Data | Residency / classification (2.3) | ✓U/P |  | ~L |
| Data | Perimeter info-flow control (2.3) | — |  | L |
| Compute | GPU/CPU capacity | ✓R (AMD) |  |  |
| Compute | Heterogeneous scheduling (5.2) | ~R |  | ~L |
| Infrastructure | Private / sovereign cloud | ✓R |  |  |
| Infrastructure | DC metering (5.2) | — | D |  |
| Infrastructure | Fleet optimization (5.2) | — |  | L |
| Productization / Ops | P1 Compliance and certification | — | D |  |
| Productization / Ops | P2 Product surface (API, SDK, console) | — | D |  |
| Productization / Ops | P3 Eval as CI | — | D |  |
| Productization / Ops | P4 Release and deployment engineering | — | D |  |
| Productization / Ops | P5 Run-the-service operations | — | D |  |
| Productization / Ops | P6 Support and customer-success engineering | — | D |  |
| Productization / Ops | P7 Feedback and ground-truth data ops | — | D |  |
| Productization / Ops | P8 Action controls / blast radius / approval gates | — | D |  |
| Productization / Ops | P9 Supply chain / config inventory | ~U | D |  |
| Off-ladder | Adoption / change management | — |  |  |
| Off-ladder | ROI measurement | — |  |  |

**Reading the columns as an allocation plan:**

- **Consume, don't build.** Rows with a ✓ under In product — consumption, serving, model catalog, fine-tuning, data fabric, and the substrate — exist in the stack today. The team integrates and operates these rather than building them.
- **Near-term (D/S).** Mostly the governance and assurance baseline and harness plumbing. Much of it instruments the products rather than building greenfield; the ⚠ rows are consume-if-verified, build-if-not.
- **Accelerate with a partner (L+A).** The moat items — the empirical map (1.5), verification (3.1), routing off the map (1.4), the learning loop and safe update (3.3), self-modification (2.4), failure prediction (3.2), explainability (4.3). This is where a partner could accelerate us — Across.AI is the candidate, pending diligence, though a similar partner could fill the role. Either way it's the reason to hold perimeter and data-rights terms: these accrue value only inside our boundary.
- **In-house long-term (L).** The substrate research and hardest governance edges — AMD inference (4.1), edge–core (4.4), fine-tuning on evolving data (4.2), perimeter information-flow control (2.3), fleet optimization (5.2), transfer across deployments (3.3), semantic-layer security (2.2). A partner wouldn't reach these; the in-house researcher owns them regardless of whether any partnership proceeds.
- **Off-ladder and ops rows.** Adoption and ROI sit in no column — they're product and change-management, not RackAI engineering. Feedback/ground-truth data ops feeds verification and the loop, so it's owned as P7 rather than left off-ladder.

**What Palantir and Uniphore cover.** Within their own stacks, Foundry/AIP and Uniphore's data fabric cover ontology, authorization, provenance, and context assembly — so a customer already on one of them has much of the data-and-context layer. That's not RackAI's data layer, though; we build above data and integrate with whatever the customer runs. Where the data foundation is a partner's, the data-and-context rows are integrate-not-build, and our governance work concentrates on runtime enforcement, verification, and the perimeter edges those products don't reach. Which product covers what, and how it lines up with a given customer, is a diligence-and-scoping item.

## Owned in-house

These items only accrue value from operating inside our perimeter, so we build and own them in-house whether or not any partnership signs. A partner can make the work faster but shouldn't own it. Each gets a Rackspace owner (roles below are placeholders until named):

- **The empirical map — per-workload measurement (1.5).** Owner: *[Measurement]*.
- **Verification — reward signal and audit evidence (3.1).** Owner: *[Governance & Assurance]*.
- **Routing off the measured map (1.4).** Owner: *[Inference / Orchestration]*.
- **The learning loop and safe online update (3.3).** Owner: *[Governance & Assurance / Research]*.
- **Governable self-modification (2.4).** Owner: *[Governance & Assurance]*.

A partner could accelerate the harness, orchestration, and loop machinery around these — Across.AI is the candidate, pending diligence — but the map, verification, routing, and safe update stay in-house, which is why the perimeter and data-rights terms with any partner matter.

## Staffing

Staffing follows the two tracks. Detail — headcount, names, phasing — is maintained separately and will change as we hire; this is the direction, not the resourcing plan.

**Dev track — the RackAI team.** Largely staffed now, and re-pointed onto this work: the dev-track programs (1, 2) and the productization and operations items (P1–P9). This is where most of the headcount sits. It builds the buildable-now items and instruments the products we consume. Two build efforts to start early because they gate everything else: compliance and certification (P1 — long lead, gates adoption) and the product surface (P2).

**Research track — a small team, hired ahead.** The research threads across Programs 3, 4, and 5, above all the moat — verification (3.1), the loop (3.3), self-modification (2.4). Small by design: its job is to work ahead so its output is ready when the build track reaches it, and to tell us which compounding-improvement claims survive our constraints before the build team spends a quarter on one that won't.

**The two scarce, long-pole hires** — open early even though their built work comes later:

- The RL-depth researcher — verification and the map (3.1 / 1.5). The anchor of the research track and the hardest hire to fill.
- The ROCm / inference-performance engineer — AMD serving economics (4.1). Critical-path for the substrate bet; AMD co-engineering is the fallback while we hire.

**The hand-off is the thing to manage.** The straddling threads (1.2, 1.4, 2.2, 2.5, 5.1) and the map → verification → safe-update chain are where research output becomes build input. Those seams are owned across both tracks; keeping them from falling between the teams is the coordination job that sits with us.

## Architecture (reference)

The stack this plan builds on: eight layers, flanked by three control planes (governance and assurance, plus operations), cut by two cross-cutting axes (cost, lifecycle — not drawn). RackAI provides infrastructure up to inference; the data layer sits with partners; governance and assurance are what we build in.

> Architecture diagram in the source is an embedded raster image (`reference/media/a4a1acb3a37313628a1092825808a6d5f3b374b7.png`). Per the operating standard, it is referenced by filename rather than embedded; a Mermaid representation of the eight-layer / three-plane stack should be authored as a canonical note during extraction rather than reproducing the raster here.
