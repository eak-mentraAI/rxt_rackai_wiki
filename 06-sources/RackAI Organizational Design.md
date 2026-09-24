---
id: src-rackai-org-design
type: source
status: draft
owner: rackai-product
domain: strategy
aliases: [org design, organizational design, rackai org, operating model, reorg, resourcing asks]
related: [hub-product, hub-root, hub-governance, src-rackai-dev-plan, src-strategic-vision, hub-roadmap, hub-org-design]
source_docs: ["reference/Enterprise AI Cloud - RackAI.pptx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-product
summary: "Markdown companion of the BU org-design deck: four functions, RackAI org structure, and reorg actions."
---

# RACKSPACE AI CLOUD — Organizational Design

> **Companion note.** Faithful markdown representation of `reference/Enterprise AI Cloud - RackAI.pptx` (added 2026-09-17 by the BU business leader). This is a *raw source projection*, not a canonical note. The deck is an **organizational-design** artifact (people, roles, reporting lines, headcount), distinct from the [[RackAI Enterprise AI Development Plan]] which is the *work* plan. Slide notes contained only slide numbers (no speaker notes). Org-chart slides are captured as structured lists/tables since the source expresses them as boxes and connectors.
>
> **Confidence:** `assumed` — a proposed operating model / internal strategy draft, not a ratified org. Names, headcounts (`[filled/total]`), and REQs are point-in-time and will change.
>
> **Sensitivity:** the deck is marked *Confidential — Internal Strategy Draft* and contains named individuals and employee IDs. This companion preserves names and roles as given (real project people, per PII handling for actual project docs) but is itself internal.

> **Cross-team boundary (editorial note, not from the deck).** This deck covers **RackAI's internal structure** (Product / Engineering / Research / AI Strategy pods). The **RackAI ↔ Infra delivery boundary** — RackAI above Kubernetes (inference, serving, routing, models, fine-tuning, harness, Empirical Map, economics, governance software, operating layer) vs. Infra at Kubernetes and below (cluster, nodes, GPU fleet, networking, storage, cluster observability), with the two handoff rules (Infra builds observability / RackAI consumes; Infra-led accelerator selection with RackAI as constraining stakeholder) — is defined and applied per-milestone in the [[RackAI Roadmap#Two Teams, One Roadmap|RackAI Roadmap]]. The deck itself does not describe the Infra team.

---

## Slide 1 — Title

- **RACKSPACE AI CLOUD**
- Organizational Design for landing and growing Enterprise AI
- A Proposed Operating Model — Core Pillars, Extended Functions, and Sub-Organization Structures
- Prepared for Executive Leadership Review
- Confidential — Internal Strategy Draft

## Slide 2 — Section divider

- **RACKSPACE AI CLOUD / RackAI**
- Prepared for Executive Leadership Review
- Confidential — Internal Strategy Draft

## Slide 3 — RackAI: Four Functions and Their Scope

*Product · Engineering · Research · AI Strategy & Capability*

### Product — "Owns what we build and why"
- Own the RackAI offering and roadmap — inference up to the governed layer
- Define what we build and why; write the requirements engineering executes
- Own the product surface — API, SDK, console, onboarding (P2)
- Set priorities and sequencing; own the P1–P9 backlog
- Manage partner and stack fit — RackAI, Uniphore, Palantir; the offering boundary

### Engineering — "Builds the stack"
- Build and operate the governed harness — serving, runtime, routing (Prog 1)
- Build the governance and assurance planes — policy, provenance, security (Prog 2)
- Build productization & operations — eval-CI, release, ops, certification
- Deliver the empirical map (1.5) and cost / tokenomics instrumentation
- Integrate the stack into one operated system + the enterprise control plane

### Research — "Works ahead on the moat"
- Verification — reward signal and audit evidence (3.1); the hardest problem
- The learning loop and safe, governable self-improvement (3.3)
- Loop planning, credit assignment, failure prediction (3.2)
- The moat edges — self-modification (2.4), perimeter info-flow (2.3), transfer
- Substrate research — AMD/ROCm inference (4.1), edge–core, fine-tuning

### AI Strategy & Capability — "Office-of-the-CTO for AI — standing, forward-looking"
- Keep the enterprise-AI thesis and POV current against a moving target
- Own the Assurance & Governance roadmap that feeds Program 2
- FinOps / tokeneconomics foundation feeding 5.1 and the cost loop
- Run the continuous field feed from consulting into the roadmap
- Internal enablement; a source for GTM messaging, not its owner

> Summary line: *Product & Engineering build the platform · Research works ahead on the moat · AI Strategy & Capability keeps direction current and bridges the field.*

## Slide 4 — RackAI: Overall Structure

*Core pillar — RackAI.*

- **SVP, RackAI Product & Engineering — Chetan Gupta**
  - Technical Program / Project Manager — PM
  - **Product** — "Owns what we build and why." Five roles: Inference/serving, AI Orchestration & Harness, AI Assurance & Governance, Product Partnership, Internal RackAI. Lead: **Neeraj Yadav** — `[1/6]`
  - **Engineering** — "Builds the AI Cloud Stack; owns four engineering pods mapped to the stack layers & key partner integrations." Lead: **Jovan Rajapakse** — `[13/30]`, `[0/1]`
  - **Research** — "Works on research problems ahead of productization." — `[0/4]`
  - **AI Strategy and Capability** — "Keeps our thesis current, AI FinOps and tokenomics, governance and assurance, Consulting feedback, thought leadership." Lead: **TBD** — `[0/4]`; noted `[4/4] (Lokesh to be transferred)`

## Slide 5 — RackAI: Product Management & Engineering Structure

*Core pillar — RackAI.*

### Product Management (under SVP Chetan Gupta)
- Technical Program / Project Manager — PM
- **PM Inference/Serving — Edward Kerr**
- PM AI Harness & Orchestration — `[0/1]`
- PM AI Assurance & Governance — `[0/1]`
- PM Product Partnership — `[0/1]` (Ramesh to nominate)
- PM RackAI Internal — `[0/1]`
- PM UK Sovereign AI — `[0/1]`

### Engineering (Jovan Rajapakse — `[13/30]`) — four pods
"Builds & operates the AI Cloud Stack; owns four engineering pods mapped to the stack layers & key partner integrations."

- **Platform** — `[10/11]` — Platform, UI, Core services (Inference — Model router, catalog, hosting)
- **Inference** — `[2/8]` — Perf tuning, quantization, cost-per-token benchmarking
  - Fine-tuning — Fine-tuning of deployed models w/ Uniphore — `[0/1]`
- **Harness and Orchestration** — `[0/2]` — Agent SDK, runtime, hosting & eval
- **Governance and Assurance** — `[0/4]` — Model, cost, data, compliance governance; integration testing and quality assurance
- **Partner Integrations** — `[0/2]` — Integrations w/ Sovereign, Uniphore, Palantir & others

Cross-cutting labels shown: Security, Compliance & Governance · Observability · Data Services & Tools. Grouping headers: "AI Inference and Serving" and "AI Harness, Orchestration and Governance."

## Slide 6 — RackAI: Product Management Structure

*Core pillar — RackAI.* (PM-only view of Slide 5.)

- **SVP, RackAI Product & Engineering — Chetan Gupta**
  - **PM Inference/Serving — Edward Kerr**
  - PM AI Harness and Orchestration — `[0/1]`
  - PM AI Assurance and Governance — `[0/1]` (Ramesh to nominate)
  - PM Product Partnership — `[0/1]`
  - PM Internal RackAI — `[0/1]`
  - PM UK Sovereign AI — `[0/1]`

## Slide 7 — RackAI: Engineering Structure

*Core pillar — RackAI.* Engineering under **Jovan Rajapakse — `[13/30]`**, organized into pods:

### AI Inference and Serving
- REQ — Director, AI Inference and Serving — `[0/1]`
- REQ — Senior Manager, Model Inferencing and Fine-Tuning
- REQ — Inference Optimization Engineer IV
- REQ — Inference Optimization Engineer V
- REQ — R-23629 S/W Dev IV → change to Inference Optimization Engineer IV
- REQ — S/W Dev III (C) – HGS → change to Inference Optimization Engineer III (×2)
- Named team: Alberto Ferrer, Deshna Shah, Erik Ljungstrom, Abhimanyu Sharma, Pandiyaraja Ramamoorthy, Mohammed Imran Kasab, Paavan Shanbhag (C), Ajay Bedre (C), Kim Nguy (C), Neelava Chaterjee (C), Rajendra Gosavi (C), Rohit Rajak (C)
- **Fine-Tuning** — No REQs required currently — will partner with Uniphore

### AI Harness, Orchestration and Governance
- REQ — Director, AI Harness, Orchestration and Governance — `[0/1]`
- **Harness and Orchestration** — `[0/2]`
  - REQ — Chief Architect, AI Orchestration
  - REQ — Principal Engineer, AI Harness
- **Governance and Assurance** — `[0/4]`
  - REQ — S/W Dev IV (C) – HGS
  - REQ — AI Governance Engineer V
  - REQ — AI Assurance Engineer V
  - REQ — Quality Engineer V (×2)

### AI Partner Integrations — `[0/2]`
- REQ — Chief Architect, AI Partner Integrations
- REQ — Lead Solutions Architect, UK Sovereign

### Pod headcount summary (as shown)
- RackAI Platform — `[10/11]`
- Inference — `[2/8]`
- Harness and Orchestration — `[0/2]`
- Governance and Assurance — `[0/4]`

## Slide 8 — RackAI: Re-org actions

*Core pillar — RackAI.* Note: *Assumes new Cost Center will be created for BU / Org / Sub-org.*

| Employee ID | Racker Name | Current Manager | New Manager | Function / New Cost Center | Notes |
|----|----|----|----|----|----|
| X74783 | Jovan Rajapakse | Guy Cotton | Chetan Gupta | RackAI – Engineering Lead | |
| 24501 | Edward Kerr | Bryan Litchford | Chetan Gupta | Inferencing – Product Lead | |
| 15673 | Erik Ljungstrom | Jovan Rajapakse | Jovan Rajapakse | AI Inference and Serving | |
| 21589 | Abhimanyu Sharma | Jovan Rajapakse | Jovan Rajapakse | AI Inference and Serving | |
| 39598 | Pandiyaraja Ramamoorthy | Akshay Ravi Jadhav | Jovan Rajapakse | AI Inference and Serving | |
| 39651 | Mohammed Imran Kasab | Akshay Ravi Jadhav | Jovan Rajapakse | AI Inference and Serving | |
| 28057 | Alberto Ferrer | Amine Badaoui | Jovan Rajapakse | AI Inference and Serving | R/C as Inference Optimization Engineer IV |
| 39290 | Deshna Shah | Amine Badaoui | Jovan Rajapakse | AI Inference and Serving | R/C as Inference Optimization Engineer IV |
| 39448 | Paavan Shanbhag (C) | Jovan Rajapakse | Jovan Rajapakse | AI Inference and Serving | P9 Contractor |
| 39450 | Ajay Bedre (C) | Jovan Rajapakse | Paavan Shanbhag | AI Inference and Serving | P9 Contractor |
| 39449 | Kim Nguy (C) | Jovan Rajapakse | Paavan Shanbhag | AI Inference and Serving | P9 Contractor |
| 39475 | Neelava Chaterjee (C) | Jovan Rajapakse | Paavan Shanbhag | AI Inference and Serving | P9 Contractor |
| 39467 | Rajendra Gosavi (C) | Jovan Rajapakse | Paavan Shanbhag | AI Inference and Serving | P9 Contractor |
| 39476 | Rohit Rajak (C) | Jovan Rajapakse | Paavan Shanbhag | AI Inference and Serving | P9 Contractor |

## Slide 9 — RackAI: Resourcing Asks

*Core pillar — RackAI.* Hiring manager for all engineering reqs below: Jovan Rajapakse; PM reqs: Chetan Gupta.

| Priority | Role | Location | Function | Internal Candidate | Notes |
|----|----|----|----|----|----|
| 1 | Director, AI Inference and Serving | US \| UK | AI Inference and Serving | | |
| 2 | Senior Manager, Model Inferencing and Fine-Tuning | US \| UK | AI Inference and Serving | | |
| 3 | Inference Optimization Engineer V | US \| UK \| MX \| IN | AI Inference and Serving | | |
| 4 | Quality Engineer V | IN | AI Harness, Orchestration and Governance | | |
| 5 | Director, AI Harness, Orchestration and Governance | US \| UK | AI Harness, Orchestration and Governance | | |
| 6 | Principal Engineer, AI Harness | US \| UK | AI Harness, Orchestration and Governance | Y | |
| 7 | Chief Architect, AI Orchestration | US \| UK | AI Harness, Orchestration and Governance | Y | |
| 8 | Chief Architect, AI Partner Integrations | US \| UK | AI Partner Integrations | Y | |
| 9 | AI Governance Engineer V | US \| UK \| MX \| IN | AI Harness, Orchestration and Governance | | |
| 10 | AI Assurance Engineer V | US \| UK \| MX \| IN | AI Harness, Orchestration and Governance | | |
| 11 | Lead Solutions Architect, Sovereign AI | UK | AI Partner Integrations | | |
| 12 | Inference Optimization Engineer IV | US \| UK \| MX \| IN | AI Inference and Serving | | |
| 13 | Quality Engineer V | IN | AI Harness, Orchestration and Governance | | |
| 14 | [OPEN REQ] Software Developer IV (R-23629) | IN | AI Inference and Serving | | Move to Inference |
| 15 | [HGS] Software Developer IV – UI (C) | IN | AI Inference and Serving | | |
| 16 | [HGS] Software Developer III (C) | | AI Inference and Serving | | Move to Inference |
| 17 | [HGS] Software Developer III (C) | | AI Inference and Serving | | Move to Inference |

PM resourcing asks (hiring manager Chetan Gupta):
- Technical Program Manager V — Technical Program Management
- Product Manager, Harness & Orchestration — Product Management
- Product Manager, AI Governance & Assurance — Product Management
- Product Manager, AI Partnerships — Product Management
- Product Manager, RackAI Internal — Product Management
- Product Manager, UK Sovereign AI — Product Management

## Slide 10 — Closing

- **RACKSPACE AI CLOUD / RackAI**
- Prepared for Executive Leadership Review
- Confidential — Internal Strategy Draft
