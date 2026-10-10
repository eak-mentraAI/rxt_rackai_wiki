---
id: wiki-roadmap-narratives
type: index
status: draft
owner: product
domain: strategy
aliases: [roadmap narratives, narrative roadmap, business roadmap, moscow, moscow rating, roadmap moscow, demo to production, demo vs production, poc to production, production readiness bar, moe gate, moe gates, market gate, market unlocks, moe-2, moe-3, moe-4]
related: [pol-sovereignty-levels, hub-roadmap, wiki-milestone-release-map, hub-minimum-operable-estate, hub-ai-operations-product, ent-empirical-map, ent-solution-marketplace, ev-sovereign-private-assistant, wiki-team-operating-model, idx-capability-gap-register]
source_docs: ["05-wiki/RackAI Roadmap.csv", "00-hub/RackAI Roadmap.md", "05-wiki/Milestone Release Map.md"]
confidence: derived
last_reviewed: 2026-10-09
parent: hub-roadmap
summary: "Groups roadmap rows by business narrative and MOE market gate, with MoSCoW and a demo-to-production bar."
---

# Roadmap Narratives

A **business projection** of the canonical roadmap table (`05-wiki/RackAI Roadmap.csv`). Every row now carries three columns: **MoSCoW** (how much the six-month plan needs it), **Narrative** (the customer outcome it builds) and **MOE gate** (the market its completion unlocks). This note groups the rows by narrative so leaders see the plain engineering work as part of an outcome they can sell. Nothing new is defined here. If this note and the CSV disagree, the CSV wins and this note is stale.

> **Status: proposed (2026-10-09).** The MoSCoW ratings and narrative names are a first cut for PM ratification. The names are working titles for marketing to refine. Confidence `derived`: no capability is upgraded, and the live shipped-vs-planned state remains the [[Capability Gap Register]].

---

## Why this exists: demos are fast, production is the product

FDE proofs of concept are fast and visible. Product teams move more slowly on work that is less visible: metering, audit, isolation, SLOs, CI. Leaders see the demo's speed, but not the distance between a demo and something we can sell, operate and stand behind. That puts pressure on the teams doing the work that makes a demo real.

The fix is to **present both on one page.** Each narrative pairs the outcome (what a demo shows) with its **production bar**: the Must rows that have to ship before we can make the claim to a paying customer. A demo becomes evidence that a narrative is wanted; it does not count as progress toward shipping it.

The three views of the roadmap answer different questions:

| View | Question it answers | Audience |
|------|--------------------|----------|
| Four proofs ([[RackAI Roadmap]]) | Can we claim it yet? | Leadership: gating and sequencing |
| Five tracks ([[Milestone Release Map]]) | Which part of the system advances? | Pillar teams and engineering |
| **Eight narratives (this note)** | **What outcome does the customer get, and how close is it to production?** | **Leaders, sales, marketing, FDEs** |

---

## MoSCoW: how the column is defined

Rated against the **six-month horizon** and the **MOE-0 → MOE-1** gate ([[RackAI Roadmap#Sequencing Logic — why this order, when we have no demand signal|Sequencing Logic]]), not against all time.

| Rating | Meaning here | Test |
|--------|--------------|------|
| **Must** | MOE-1 cannot pass without it, or it captures something code cannot regenerate later (cost history, operating evidence, trust boundaries, compliance lead time), or it is a named customer commitment. The reason is tagged on each row (below) | "If this slips, does MOE-1 slip or do we lose data we can't backfill?" |
| **Should** | Strengthens the loop or the moat; MOE-1 survives without it but is weaker | "Would we ship MOE-1 knowing this is missing?" Yes, reluctantly |
| **Could** | A technique, experiment or prototype; valuable, not load-bearing this horizon | Drop it first when capacity is short |
| **Won't (this horizon)** | Proof-4 scale, backlog, or out of scope. Not "never": the CSV writes it as `Won't (this horizon)` so it can't be misread out of context | Revisit after MOE-1 |

**Why it's a Must.** Each Must row's discussion field starts with its reason, because the three reasons aren't interchangeable and not every Must is an MOE-1 prerequisite:

| Tag | Means | Rows | Examples |
|---|---|:-:|---|
| `[Gate-critical]` | The row's MOE gate cannot pass without it | 26 | Customer isolation, governed harness v1, Metering M3–M4, CI system |
| `[Evidence-critical]` | Captures evidence or history we can't backfill later | 6 | Cost model, Empirical Map v1, Metering M1, GLM 5.3 Flash (the first real-workload evidence) |
| `[Commitment-critical]` | A named customer commitment | 2 | Uniphore SFT/LoRA, Uniphore single-cluster tenancy |

A row can carry two tags (e.g. Metering M1 is `[Gate-critical; Evidence-critical]`), so the counts overlap. Only the Gate-critical rows block a gate.

Done rows keep the rating they had when they were planned, so the production bar shows what has been completed as well as what remains. The current split is 31 Must, 15 Should, 11 Could and 22 Won't across 79 rows.

---

## The eight narratives at a glance

| # | Narrative | The promise (customer voice) | Must rows done | Production bar today |
|:-:|-----------|------------------------------|:--------------:|----------------------|
| **N1** | **Tell Us the Outcome. We Run It.** | "Tell us what you want and what you won't compromise; Rackspace operates it and proves what it delivered." | 0 / 5 | 🔴 The headline promise; gated by MOE-1 |
| **N2** | **Your AI, Your Rules** | "Your data, models and policies stay inside the boundary you agree with us, and you get the evidence to show your auditor." (Agreed private boundary at MOE-1; residency in specific jurisdictions is MOE-3) | 3 / 8 (2 in progress) | 🟡 Identity and audit foundation shipped; extended audit, isolation, harness and attestation open |
| **N3** | **No Surprises** | "You always see how your AI performs and what it costs, and spend stays inside the limits you set." (Visibility and enforced limits, not a guaranteed cost outcome) | 0 / 8 (3 in progress) | 🟡 Telemetry and metering underway; SLOs and customer view missing |
| **N4** | **Smarter With Every Workload** | "Our placement and routing decisions improve as evidence from the workloads we operate accumulates." (Not automatic improvement from every workload) | 1 / 2 | 🔴 The moat; Empirical Map not started |
| **N5** | **Your Models, Operated** | "Run the models you choose, including your own fine-tuned ones, and we operate them." | 0 / 4 (2 in progress) | 🟡 GLM and Uniphore in flight; onboarding pipeline and version upgrades not started |
| **N6** | **Price-Performance Without Lock-In** | "Best performance per dollar across accelerators and suppliers, with no single-vendor lock-in." | 0 / 1 | 🔴 Architectural readiness only this horizon (the supply-abstraction interface); external claims wait for measured multi-supply at MOE-4 |
| **N7** | **Solutions, Ready to Run** | "Proven AI solutions you switch on inside your own estate, not projects you commission." | no Musts | ⚪ Prototype stage (MK.S0) until certification and repeatability are demonstrated |
| **N8** | **Built to Scale Profitably** *(internal)* | For leadership and the board: "Each estate is margin-positive, and estate #100 costs less to run than #1." | 0 / 3 | 🔴 Cost model, unit economics and CI all missing |

> **What the table shows.** The narratives with the most visible demos (N1's Concierge Engineer, N7's Sovereign Private Assistant) have the least production work done. The narratives that look dull (N2, N3) hold 16 of the 31 Musts and most of the shipped work. That is the conversation to have with leaders. Nothing is claimed as production until its MOE gate passes (see the rule below). Shipped pieces of N2, N3 and N5 can be described as available today; N1 becomes claimable at MOE-1; N4, N6 and N7 are "on the roadmap" (see [[Milestone Release Map#How to Use This Note|external-claim rule]]).

---

## Each narrative: the demo and its production bar

Rows are named by their CSV `Milestone` and stage. ✅ done · 🟡 in progress · ⬜ not started.

### N1 — Tell Us the Outcome. We Run It.

The operator identity as one sentence: the AI Operating System loop ([[RackAI Roadmap#The Operating Loop — the system the four proofs build|Operating Loop]]) delivered as a service.

- **A demo shows:** a conversational agent answering "what is my cost and latency?" or deploying a model on request ([[RackAI Roadmap#P-008 — Concierge Engineer: the user-facing side of the AI Operating System loop|Concierge Engineer]]).
- **Production bar (Must):** ⬜ Workload declaration (T1.S2) · ⬜ Minimum Operable Estate spec · ⬜ MOE-0 · ⬜ MOE-1 · ⬜ MOE-1 evidence report. See [[Minimum Operable Estate]].
- **Next (Should / Could):** Concierge Engineer v0 Answer (Should), v1 Act with confirmation (Could).
- **Not this horizon:** Concierge v2 governed autonomy; managed-ops / FDE motion at multi-estate scale.

### N2 — Your AI, Your Rules

The sovereignty and control half of the identity: identity, audit, isolation, the governed harness, assurance evidence. **Scope by gate:** MOE-1 establishes that the customer's *agreed execution boundary* is enforced and evidenced. It does not promise every residency, failover or sovereignty requirement; residency in specific jurisdictions is MOE-3.

- **A demo shows:** a private assistant answering over a customer's own corpus (e.g. the [[Sovereign Private Assistant]]). It looks sovereign; it is not sovereign until the rows below ship.
- **Production bar (Must):** ✅ IAC M1 · ✅ IAC M2 · ✅ IAC M3 (audit foundation) · 🟡 IAC M3 + Auditing M1–M3 (foundation shipped; extended audit controls pending) · 🟡 Uniphore single-cluster tenancy · ⬜ Governed execution harness v1 · ⬜ Customer isolation + private inference · ⬜ First applicable assurance attestation (e.g. SOC 2; type and scope set by the MOE-1 segment).
- **Next (Should):** IAC M4 reframed as the minimum control envelope; authority under incomplete intent.
- **Not this horizon:** full harness runtime, govern-and-assure at estate scale, multi-cluster governance, and the MOE-3 residency rows (data-residency controls, residency-aware placement and failover, per-jurisdiction compliance evidence).

### N3 — No Surprises

Performance and spend are visible to the customer and bounded by limits they set. The promise is visibility and enforced limits, not a guaranteed cost outcome.

- **A demo shows:** a dashboard of tokens, latency and spend.
- **Production bar (Must):** 🟡 Platform M1–M2 · 🟡 Platform M3–M4 (13-month retention) · 🟡 Metering M1 · ⬜ Observability M1 (operator intelligence) · ⬜ Customer observability · ⬜ Per-profile SLO thresholds · ⬜ Metering M3 (quota policy) · ⬜ Metering M4 (enforcement).
- **Why it's Must:** metering and telemetry history that isn't captured now can't be backfilled later, and no SLO can be scored until the thresholds are ratified.

### N4 — Smarter With Every Workload

The moat: the [[Empirical Map]] turns evidence from operated estates into better placement and routing decisions. It improves as evidence accumulates; a single workload doesn't automatically make the next one better.

- **A demo shows:** a router that picks a cheaper model or accelerator for a request.
- **Production bar (Must):** ✅ Accelerator inventory & consumption telemetry · ⬜ Empirical Map v1 + transferable/isolated split.
- **Next (Should / Could):** AI performance benchmarks, workload characterization, evidence-informed routing (Should); evidence-informed accelerator selection, semantic router (Could).
- **Acceptance (2026-10-09):** "beats the static baseline" is defined *before* evaluation, on the same baseline workload, across SLO attainment, cost efficiency, constraint compliance and decision quality, with each pass threshold fixed in advance, so success can't be shown on whichever measure improved. A recommendation is *evidence-backed* when a decision record exists, and *empirically validated* only once it beats the baseline across enough workloads. With few initial workloads, v1 claims evidence-backed.
- **Not this horizon:** day-zero model factory and closed-loop optimization.

### N5 — Your Models, Operated

Model choice and model lifecycle: the portfolio, fine-tuning operations, onboarding and retirement, the OpenRouter channel. Renamed 2026-10-09 from "Any Model, Day One", which implied universal, immediate support that the roadmap doesn't deliver (new-model onboarding is a Should). Finishing N5's Musts alone doesn't make it sellable: production also needs its gate's isolation (N2) and metering (N3).

- **A demo shows:** a new model or a fine-tuned adapter serving traffic.
- **Production bar (Must):** 🟡 GLM 5.3 Flash + OpenRouter Path A · 🟡 Uniphore SFT/LoRA · ⬜ Model onboarding pipeline v0 (RACKAI-354, MOE-1) · ⬜ Model version upgrade (MOE-1). The last two became Must on 2026-10-09: fast, evidenced model adoption is a competitive priority, so MOE-1 doesn't pass on hand-run model work.
- **Next (Should / Could):** Model Launch Lag instrumentation (MOE-1); multi-model operation, domain-model experiment, model sunsetting, OpenRouter Inference aaS (Should); DPO, OpenRouter BYOM, direct Inference aaS (Could).
- **Model velocity (2026-10-09):** the full day-zero [[Model Launch Factory]] stays beyond this horizon, but its middle is pulled forward. RACKAI-354 becomes a **human-gated onboarding pipeline v0** for known architectures (intake → functional validation → benchmark → canary). A new row covers **upgrading to a new version of a model we already run** (canary, automatic rollback). [[Model Launch Lag]] gets measured from the first onboarding, so "quickly" has a baseline before the <24h / <72h target is committed. The CI Must now explicitly covers model and fine-tuning images.
- **Not this horizon:** fine-tuning checkpointing (moving external).

### N6 — Price-Performance Without Lock-In

Supply and accelerator freedom, plus the inference-efficiency techniques. An aspiration this horizon: what ships is **architectural readiness** (the seam), not demonstrated supplier independence. External claims wait for measured multi-supply capability at MOE-4.

- **A demo shows:** a benchmark where a technique (speculative decoding, KV-cache reuse) or a second accelerator beats the baseline.
- **Production bar (Must):** ⬜ Supply-abstraction interface (T1.S2). The MOE-1 definition runs our own supply behind it, so the seam must exist before the control plane hardens (P-004). Must since 2026-10-09.
- **Next (Should):** llm-d inference routing, a second supply implementation.
- **Could:** speculative decoding, Refrag, shared KV-cache improvement. These are techniques, not outcomes.
- **Not this horizon:** AMD AIM, multi-region, GPU node access, heterogeneous supply, dynamic fleet management.
- **Read this as:** a strong benchmark result here is evidence for N4, not a shippable claim on its own.

### N7 — Solutions, Ready to Run

The [[Solution Marketplace]]: FDE-authored solutions that can be switched on in any estate.

- **A demo shows:** an FDE solution running for one customer. This is where the demo-vs-production gap is widest.
- **Production bar:** none this horizon. MK.S0 (one reference solution) and MK.S1 (extract the Solution Standard) are Could. The trust gate, lifecycle, catalog, certification bar and commercial model are Won't until after MOE-1, because they depend on N2's control envelope.
- **Read this as:** prototype stage until certification and repeatability are demonstrated. An FDE solution becomes a product only when it can be re-instantiated under N2's isolation and N3's metering. Fast FDE prototypes are not a reason to pull MK.S2 onward forward.

### N8 — Built to Scale Profitably *(internal)*

For leadership and the board, not external marketing: the economics and engineering hygiene of the operator business.

- **Production bar (Must):** ⬜ Cost model (internal cost/GPU-hour) · ⬜ Unit economics & margin · ⬜ CI system.
- **Next (Should):** operator KPI instrumentation; object store.
- **Not this horizon:** operational leverage (workloads/FTE), the Proof-4 acceptance measure.

---

## MOE gates: the market each one unlocks (proposed)

The `MOE gate` column assigns every roadmap row to a gate. Each gate has a plain-English label and one story: **the market it unlocks**. Narratives (N1–N8) say *what value* a row builds. Gates say *which market it opens, and in what order*. Leaders and sales use gates to answer "what does finishing this let us sell, and to whom?"

**Assignment rule.** Each row gets the **earliest gate it is needed for**:
- For a **Must** row, that gate cannot pass without it.
- For a **Should** or **Could** row, it is the gate the row is planned to land with.
- **Not gated** covers channels, techniques, experiments and customer commitments that no market gate depends on.

A consistency check holds across the CSV: every Must sits at MOE-0, MOE-1 or Not gated, and every `Won't (this horizon)` sits at MOE-2 or later or is Not gated.

**Impact rule.** Gates are stated as **markets unlocked**: which buyers can say yes, against which [[Three Battlegrounds#Who We Compete With — Organized by the Customer's Alternative|customer alternative]]. We make **no price, per-token, margin or revenue claims** until the N8 cost model and unit economics are measured. A milestone can justify an eligibility claim; only measured data can justify an economics claim. *Opens* means a new buyer can say yes. *Deepens* means we win more often or expand in existing customers.

| Gate | The market it unlocks | Opens or deepens | Rows | Musts done | What's left (key rows) |
|---|---|:-:|:-:|:-:|---|
| **MOE-0 Operator rehearsal** | **Nothing externally, and never marketed.** Proves we can operate an estate: runbooks, SLOs, incident process, metering | — | 20 | 4 / 20 (6 in progress) | Supply-abstraction interface, Observability M1, per-profile SLO thresholds, cost model, Metering M3–M4, governed harness v1, MOE spec, CI system, the MOE-0 run itself |
| **MOE-1 First operated estate** | **A first buyer from the ICP**: a *defined initial customer profile* within the ICP (large enterprises with valuable proprietary data that can't use shared or public inference for a material share of workloads) buys and delegates a *bounded* operated estate inside its agreed boundary. We beat "build it themselves" for that buyer; sales gets its first reference customer and its first operating invoice. It does **not** show the whole ICP is addressable or the offer repeatable (that's MOE-2) | **Opens** | 16 | 0 / 10 | Customer isolation + private inference, first applicable assurance attestation, customer observability, workload declaration, unit economics, Empirical Map v1 (evidence from the first estate can't be backfilled), MOE-1 evidence contract and reporting mechanism (the first completed report is the acceptance output); model onboarding pipeline v0 and model version upgrades |
| **MOE-2 Repeatable offer** *(proposed)* | **The ICP, repeatably**: sold as a repeatable offer with a reference and a standard contract, not a bespoke engagement. Workloads per ops FTE becomes measurable; the K2 moat test starts | **Opens** | 8 | — | Multi-model operation, model sunsetting, workload characterization, evidence-informed routing, managed-ops onboarding playbook |
| **MOE-3 Residency + multi-region** *(proposed)* | **Multinational and residency-bound buyers** who need workloads kept in specific jurisdictions under one operator | **Opens** | 5 | — | Multi-region support, multi-cluster governance, data-residency controls, residency-aware placement and failover, per-jurisdiction compliance evidence |
| **MOE-4 Run on your supply** *(proposed; end state)* | **Buyers with their own GPUs or a committed hyperscaler or partner deal**: we operate on capacity they already own (sovereignty Level 3), only once the platform is proven on RXT-owned hardware; and win "build it themselves" even where the hardware is bought | **Opens** | 5 | — | Second supply implementation, heterogeneous supply, evidence-informed accelerator selection, AMD AIM, govern and assure inside the customer's perimeter |
| **Beyond MOE-4 (operate at scale)** | Lower cost to serve and more autonomy across many estates; higher win rate against GPU clouds and inference platforms | Deepens | 4 | — | Closed-loop optimization, dynamic fleet, full harness runtime, Concierge v2 |
| **Not gated** | Channels and experiments that run beside the gates: OpenRouter (proving ground), the [[Solution Marketplace]] (its own MK.S0–S5 ladder; MK.S2 onward needs MOE-1's isolation), inference techniques, fine-tuning experiments, the Uniphore commitment | Deepens | 21 | 0 / 1 (Uniphore SFT/LoRA, in progress) | — |

> **MOE-2 to MOE-4 are proposed here, not ratified.** The [[Minimum Operable Estate]] defines only MOE-0 and MOE-1. These stages follow its list of what MOE-1 deliberately excludes, so each adds back one exclusion along with the market it unlocks. If they are ratified, their canonical home is the MOE hub, and this table points there. The order (repeat first, then residency, then customer supply) is a proposal; a buyer pulling hard for residency or own-supply would justify reordering.

**The ladder in one line each:**
- **MOE-1:** we can operate it responsibly for a paying customer.
- **MOE-2:** we can sell and operate it repeatedly without bespoke engineering for every customer.
- **MOE-3:** we can honour jurisdictional boundaries across regions.
- **MOE-4:** we can operate across customer-selected supply.

**Each gate also unlocks a sovereignty level** ([[Sovereignty Levels]], `assumed`): Level 0 (shared, time-sliced) is sold today; MOE-1 → Level 1 Dedicated; MOE-3 → Level 2 Dedicated in a jurisdiction; MOE-4 → Level 3 Your own hardware, the end state.

**MOE-1 acceptance logic.** Before acceptance, MOE-1's capabilities are operational and the evidence contract and reporting mechanism are validated. The first completed evidence report is an *output* of the acceptance exercise, not a prerequisite. Proof 3 passes only with a paying customer, delegated responsibility and the agreed evidence requirements satisfied. Canonical: [[Minimum Operable Estate#Exit Condition (Proof 3 = MOE-1)|MOE exit condition]].

**What the check found:**
1. **Supply-abstraction interface was rated Should, but the MOE requires it.** The [[Minimum Operable Estate]] v1 definition puts owned supply "behind the supply-abstraction interface", and P-004 says to build it before the control plane hardens. **Resolved 2026-10-09: upgraded to Must**, gated at MOE-0.
2. **MOE-3 was thin.** It had only multi-region and multi-cluster governance. **Resolved 2026-10-09: three rows added** (data-residency controls, residency-aware placement and failover, per-jurisdiction compliance evidence), all N2, unstaffed, `Won't (this horizon)`. Which jurisdictions depends on the MOE-3 target markets, not yet chosen.
3. **MOE-1 has not started.** None of its 16 rows are done or in progress. MOE-0 is a fifth shipped, with 6 Musts in flight. The distance between the market leaders want and the work under way is clearest here.

**What this gives leadership:** every engineering row now carries a market sentence. "Customer isolation + assurance attestation" isn't plumbing: **it's two of the ten Musts that let a first ICP customer buy.** An FDE demo that excites a regulated prospect produces pipeline for MOE-1. That market opens only when MOE-1's rows ship.

---

## Demo-to-production rule (proposed)

The working rule for presenting FDE and product work together. It makes the speed of demos and the progress of production work visible on the same page.

> **A demo proves technical possibility. A pilot tests customer fit and bounded operation. Production proves operational responsibility within a defined, enforceable contract.** Every production claim needs evidence for both identity centres: as **operator**, Rackspace takes responsibility for the realization, operation and evidence of the agreed outcome; as **sovereign provider**, the customer keeps authority over the boundaries that responsibility is exercised within ([[Three Battlegrounds]]).

1. **Every POC names its narrative.** An FDE demo is reported as "a demo of N2" (for example), never as a standalone feature.
2. **Every demo is shown with its production bar.** Alongside the demo, show the narrative's Must rows and their state. The demo shows the outcome is wanted; the Must rows show how far it is from being sold.
3. **Three readiness labels, no others:**

| Label | Means | Claimable to |
|-------|-------|--------------|
| **Demo** | Technical possibility: works for one audience on a happy path; no Must rows required | Internal audiences; a prospect only when explicitly labelled as a demo |
| **Pilot** | Customer fit under bounded operation: a **named scope**, **explicit constraints** and an **accountable operator** for a named customer | That customer, within the stated scope and limits |
| **Production** | Operational responsibility under an enforceable contract: the capability's required Musts are done, **the applicable MOE gate has passed**, and its operating and commercial boundaries are written down | The market, within those boundaries |

A narrative is a business lens, not an independently sellable product. Finishing one narrative's Musts never authorizes a broader RackAI production claim on its own.

4. **Demos feed the plan, not the other way round.** A demo that shows strong pull can raise a row's MoSCoW at the next roadmap review. It cannot bypass the Must rows.

Process owner: the roadmap review in [[Team Operating Model]].

---

## Maintaining this note

- **Canonical data:** the `MoSCoW (6-month horizon)`, `Narrative` and `MOE gate` columns in `05-wiki/RackAI Roadmap.csv`. Change a rating or a grouping there first, then re-project here.
- **New rows:** every new CSV row needs a MoSCoW rating, exactly one narrative and one MOE gate. If a row fits none of N1–N8, raise it at roadmap review; don't add a ninth narrative quietly.
- **Dates:** `Due` is the single date per row. `Date status` says how firm it is: **Committed** (engineering confirmed it after the estimation meeting) or **Target** (a planning date not yet confirmed; most fall on the 15th as month-level targets). Live dates stay in Craft.io.
- **Must reasons:** every Must row starts its discussion field with `[Gate-critical]`, `[Evidence-critical]` and/or `[Commitment-critical]`.
- **Decisions to protect:** eight narratives, no ninth. Concierge Engineer is an interface to the operating model, not its centre. Inference techniques (speculative decoding, Refrag, KV caching) stay subordinate to measured improvement, never standalone customer outcomes. Marketplace production stages are not pulled forward because FDE prototypes move fast; MK.S0 → MK.S1 comes first. The narratives are lenses, never eight delivery organizations.
- **Craft.io:** if the live tool gets these as fields, Craft.io holds the value and the CSV mirrors it (same division as dates and owners).

## Open questions

- **Ratify MoSCoW.** In particular: Workload declaration as Must; Concierge Engineer v0 as Should; Authority under incomplete intent as Should rather than Must for MOE-1.
- **N6 has one Must** (the supply-abstraction interface): the seam exists this horizon, but "no lock-in" can't be claimed externally until MOE-4.
- **Narrative names.** Marketing to refine; keep the N1–N8 codes stable so the CSV doesn't churn.
- **MOE-3 jurisdictions.** Which residency regimes the new MOE-3 rows target depends on the MOE-3 markets; start attestation scoping before MOE-3 is promised.
- **MOE-2 to MOE-4.** Ratify the proposed expansion gates and their order (tracked in [[Minimum Operable Estate]] open questions).
- **Which segment is the ICP's first vertical?** The market-unlock table names the ICP but not the vertical; that follows from the MOE-1 customer choice.

## See Also

- [[RackAI Roadmap]]: the canonical plan (four proofs, P-items, decisions)
- [[Milestone Release Map]]: the five-track functional projection of the same rows
- [[Minimum Operable Estate]]: the MOE-1 bar most Must ratings point at
- [[AI Operations Product]]: where the FDE motion sits
- [[Capability Gap Register]]: the authority on shipped vs planned
