---
id: wiki-pillar-working-model
type: hub
status: draft
owner: product
domain: strategy
aliases: [pillar working model, pillar boundaries, inter-pillar model, how pillars work together, raci pillars, pillar responsibilities]
related: [hub-org-design, hub-inference-serving, hub-model-services, hub-inference-optimization, hub-ai-governance-assurance, hub-ai-harness, hub-ai-operations-product, hub-roadmap, wiki-team-operating-model]
source_docs: ["06-sources/RackAI Organizational Design.md", "reference/jd/EXTERNAL_PDM_Optimization_and_Efficiency_JD.md", "reference/jd/EXTERNAL_PDM_Orchestration_and_Harness_JD.md", "reference/jd/EXTERNAL_PDM_Assurance_and_Governance_JD.md", "reference/jd/EXTERNAL_PDM_Product_Operations_JD.md"]
confidence: derived
last_reviewed: 2026-09-24
parent: hub-org-design
summary: "How the six RackAI pillars divide responsibility, make joint decisions, and interact day-to-day."
---

# RackAI Pillar Working Model

This document defines how the six RackAI pillars above the Kubernetes line work with and independently of each other. It is written for internal teams — PMs, engineering leads, and anyone who needs to know where a decision belongs, who to involve, and what each pillar is accountable for delivering.

---

## The Simplest Way to Think About the Boundaries

Before the detail: seven responsibility domains, one question each.

| Domain | The question it answers |
|---|---|
| **[[Model Services]]** | What models can customers use? |
| **[[Inference Optimization]]** | How should we run them efficiently and economically? |
| **[[Inference and Serving Services]]** | How do we reliably serve them at production scale? |
| **[[AI Governance & Assurance]]** | What rules must AI activity obey, and how do we prove it? |
| **[[AI Harness]]** | How do models, context, tools, and agents work together to accomplish a task? |
| **[[Product Operations]]** | What has to be true for all of this to operate as a sellable, supportable product? |
| **Infra** *(below K8s — not a pillar)* | What compute, network, storage, and Kubernetes foundation does all of this run on? |

Everything that follows is the evidence and operational detail behind those seven sentences.

> **Layer boundary.** All six pillars live above Kubernetes. Infra owns Kubernetes and below — cluster, nodes, GPU fleet, networking, storage, cluster observability. Where this document says "Infra," it means that team, not one of the six pillars. The distinction deserves emphasis: **Infra owns physical supply and Kubernetes capacity. Inference and Serving Services owns how that provisioned supply is exposed, allocated, and consumed by inference workloads.**

---

## The Six Pillars at a Glance

| Pillar | Owns | Does Not Own |
|---|---|---|
| **[[Inference and Serving Services]]** | Deployments, runtimes, autoscaling, how provisioned capacity is allocated and consumed, API surface | Physical infrastructure and Kubernetes (Infra); which models to serve (Model Services); how efficiently they run (Optimization) |
| **[[Model Services]]** | Whether a model can enter and remain in the catalog: intake, compatibility, launch pipeline, versioning, fine-tuning, LoRA lifecycle | Making an approved model reliably runnable in production (Serving); whether it's economically/performance viable (Optimization) |
| **[[Inference Optimization]]** | Whether a catalog model can be run well and economically: throughput, latency, cost-per-token, benchmark harness, optimization techniques, performance-regression gate | The serving infrastructure itself; the catalog |
| **[[AI Governance & Assurance]]** | What rules AI activity must obey and the evidence it happened: runtime policy, tenant isolation, provenance/audit, agent identity design, compliance certifications | The harness runtime that enforces those rules at execution time |
| **[[AI Harness]]** | How models, context, tools, and agents work together: context assembly, tool controls, memory, guardrails, orchestration routing, Empirical Map as decision surface | Business logic customers build on top; raw serving below; policy rule definitions (those come from Governance) |
| **[[Product Operations]]** | What makes capabilities operable as offers: launch-readiness gates, metering/showback wiring, capacity provisioning coordination, compliance evidence assembly, cross-pillar runbooks | Any single product layer; external product direction (internal-facing role) |

### The three-pillar model for model economics

The Model Services → Optimization → Serving chain has a clean mental model worth stating explicitly:

> **Model Services** asks: *Can/should we offer it?*  
> **Inference Optimization** asks: *Can we run it well and economically?*  
> **Inference and Serving Services** asks: *Can we run it reliably at production scale?*

A model that passes Model Services but fails Optimization economics doesn't launch. A model that passes both but can't be reliably deployed by Serving doesn't launch either. The model launch gate (seam 1 below) is where all three converge.

---

## How Each Pillar Works Independently

### Inference and Serving Services — works alone when:
- Choosing, configuring, or upgrading a serving runtime (vLLM, NIM, TensorRT-LLM) for an already-approved model
- Managing deployment lifecycle events: scaling, canary rollouts, rollbacks, environment promotion
- Evaluating and integrating autoscaling policy changes
- Debugging serving-plane incidents (latency, error rate, node failures)
- Designing and implementing supply-abstraction interface changes
- Multi-region topology and infrastructure decisions (with Infra as the execution partner, not a gating approver)

### Model Services — works alone when:
- Triaging model candidates from the radar and deciding whether to begin intake
- Running hardware compatibility and runtime compatibility checks on a new model
- Managing fine-tuning job submissions, monitoring, and adapter lifecycle for existing customers
- Deciding versioning and deprecation schedules for catalog models
- Updating Registry Credentials and resolving license / access issues

### Inference Optimization — works alone when:
- Selecting and prioritizing optimization techniques (quantization precision, caching strategy, batching config) for a specific model/hardware pair
- Running benchmarks and publishing results to the benchmark harness
- Setting and updating the performance-regression gate thresholds
- Evaluating AMD/ROCm readiness against the target economics bar
- Building and maintaining the cost-floor model (cost-per-GPU-hour → cost-per-1M-tokens)

### AI Governance & Assurance — works alone when:
- Defining runtime policy rules and their enforcement logic
- Owning the compliance roadmap: sequencing SOC 2, ISO 27001, ISO 42001, NIST AI RMF; managing the certification process with the named certification owner
- Designing tenant isolation architecture and enforcement
- Defining the agent identity and scoped-token model (structure, expiry rules, delegation scope)
- Assembling and maintaining the audit evidence package

### AI Harness — works alone when:
- Designing the harness context assembly pattern and guardrail logic
- Building the durable runtime (replay, recovery, observable traces)
- Designing orchestration routing rules: task → model/harness/human assignment logic
- Defining the Empirical Map product surface: what data it exposes, how routing reads it
- Sequencing the harness roadmap: one proven workload before generalization

### Product Operations — works alone when:
- Running the launch-readiness gate process for a new model or capability going live
- Maintaining metering and showback wiring (usage capture, tenant attribution, cost reporting)
- Writing and updating cross-pillar runbooks based on post-launch learnings
- Coordinating capacity-pool provisioning and reserve/warm/canary allocation
- Assembling compliance evidence packages for audits across governance, engineering, and security teams

---

## Where Pillars Must Work Together (Joint Responsibilities)

This section is the most important one to get right. These are the seams where decisions cannot be made unilaterally — both pillars must be in the room.

> **The compatibility seam to keep in mind:** Model Services runs hardware and runtime compatibility checks, while Serving validates runtime configuration for a specific deployment. If a model doesn't work correctly on a specific runtime/hardware combination in production, the split is: **Model Services owns whether the model can enter and remain in the catalog. Serving owns making an approved model reliably runnable in production.** Optimization owns whether doing so is economically and performance viable. A failure that blocks catalog entry is Model Services' problem. A failure that occurs in a live deployment is Serving's. A failure of economics (runs but burns margin) is Optimization's.

---

### 1. Model Launch Gate
**Pillars:** Model Services + Inference Optimization + Inference and Serving Services + Product Operations

When a model is ready to go live, all four must sign off before it enters production:

| Pillar | Their gate |
|---|---|
| **Model Services** | Intake passed (compatibility, license, safety review); deployment spec prepared |
| **Inference Optimization** | Benchmark baseline established for this model/hardware pair; cost-per-1M-tokens known; performance-regression baseline set |
| **Inference and Serving Services** | Runtime config validated; capacity allocated; canary plan ready |
| **Product Operations** | Launch-readiness checklist cleared: metering wired, pricing inputs provided, support readiness confirmed |

**Decision owner:** Product Operations calls the gate. No pillar can unilaterally bypass it. A model that passes optimization but has no metering wired does not launch.

---

### 2. Performance-Regression Gate on Serving Changes
**Pillars:** Inference and Serving Services + Inference Optimization

Any change to a runtime, quantization config, or serving configuration must clear the performance-regression gate before it reaches production.

| Responsibility | Owner |
|---|---|
| Set and maintain gate thresholds (latency, throughput, quality) | Inference Optimization |
| Submit changes for gate evaluation | Inference and Serving Services |
| Run benchmarks when thresholds are ambiguous | Inference Optimization |
| Decide whether a tradeoff (e.g., throughput ↑ but latency ↑) is acceptable | Joint — both PMs must agree |

**Escalation:** If the two PMs disagree on a tradeoff, it escalates to the SVP.

---

### 3. Agent Identity and Policy Enforcement Seam
**Pillars:** AI Governance & Assurance + AI Harness

This is the sharpest shared seam in the entire org. Neither pillar owns it unilaterally.

| Responsibility | Owner |
|---|---|
| Define the agent identity model (scoped tokens, delegation rules, expiry) | AI Governance & Assurance |
| Enforce identity and permissions at runtime within a harness execution | AI Harness |
| Define what per-step verification checks must prove and what evidence they produce | AI Governance & Assurance |
| Decide where in a harness execution run the verification checks execute | AI Harness |
| Ensure verification check output is formatted as audit evidence | Joint design — both must agree |

**Working rule:** neither pillar ships a design that touches this seam without a written agreement (even a one-page spec) co-signed by both PMs. No exceptions — this is where governance promises break if not coordinated.

---

### 4. Empirical Map Ownership
**Pillars:** AI Harness + Inference Optimization + Inference and Serving Services

The [[Empirical Map]] is fed by multiple pillars but owned by one.

| Responsibility | Owner |
|---|---|
| Own the Empirical Map as a product surface (what it exposes, how routing reads it) | AI Harness |
| Produce the benchmark and efficiency data that feeds the Map | Inference Optimization |
| Produce the serving telemetry (latency, error, utilization) that feeds the Map | Inference and Serving Services |
| Define what is transferable vs. customer-isolated in the Map | AI Harness (with input from AI Governance & Assurance on isolation rules) |

**Why AI Harness owns the Map:** The Empirical Map's primary purpose is to provide the decision surface used for workload routing and orchestration — answering "which model, on which hardware, for this workload?" at task-assignment time. That makes it a core Harness product, not a standalone intelligence asset. Inference Optimization and Inference and Serving Services remain authoritative for the underlying data they produce; they do not control the schema or the surface. If the Map's purpose evolves beyond routing (e.g., becomes a standalone capacity-planning or pricing signal), ownership should be revisited.

**Working rule:** Inference Optimization and Inference and Serving Services are producers; AI Harness is the owner and consumer. Producers do not set the Map's schema — they produce data to a contract AI Harness defines.

---

### 5. Compliance Evidence Assembly
**Pillars:** AI Governance & Assurance + Product Operations + (all pillars as evidence contributors)

SOC 2 and future certifications require evidence from every team. Product Operations assembles it; Governance owns what "sufficient" means.

| Responsibility | Owner |
|---|---|
| Define what evidence is required per certification | AI Governance & Assurance |
| Assemble evidence across teams and maintain the audit package | Product Operations |
| Produce engineering evidence (deployment records, change logs, test results) | Inference and Serving Services |
| Produce security and policy evidence (policy configs, isolation tests, agent identity logs) | AI Governance & Assurance |
| Produce optimization evidence (performance baselines, regression gate results) | Inference Optimization |
| Produce harness evidence (trace records, policy enforcement logs) | AI Harness |

**Working rule:** Product Operations owns the calendar and the package. Governance owns the bar. If evidence is missing, Governance flags it; Product Operations is accountable for getting it from the right team.

---

### 6. Tenant Isolation
**Pillars:** Inference and Serving Services + AI Governance & Assurance

Namespace-level isolation is an infrastructure concern and a compliance concern simultaneously.

| Responsibility | Owner |
|---|---|
| Implement namespace-per-org isolation in the serving plane | Inference and Serving Services |
| Define the isolation requirements (what must never cross a tenant boundary) | AI Governance & Assurance |
| Test and certify that isolation holds | AI Governance & Assurance (with Inference and Serving Services as the executing team) |
| Respond to isolation-related incidents | Joint — both teams are on the incident bridge |

---

### 7. Harness-to-Serving Interface
**Pillars:** AI Harness + Inference and Serving Services

The harness consumes inference endpoints. When the serving plane changes its API surface or behavior, the harness must be informed and vice versa.

| Responsibility | Owner |
|---|---|
| Maintain the serving API contract (what endpoints the harness can rely on) | Inference and Serving Services |
| Communicate harness requirements back to the serving API (latency SLOs, streaming behavior, token-level control needs) | AI Harness |
| Validate that a serving runtime change does not break harness contracts | Joint — Harness signs off before Serving ships |

---

## Escalation and Decision Rules

| Situation | Rule |
|---|---|
| A change affects only one pillar's owned scope | That pillar's PM decides unilaterally |
| A change affects a seam defined in this document | Both PMs must agree; disagreements escalate to SVP |
| A launch-readiness gate is disputed | Product Operations calls the gate; blocked gates escalate to SVP |
| A change affects the compliance envelope | AI Governance & Assurance has veto; no other pillar can override a compliance hold |
| A change affects the Empirical Map schema | AI Harness decides the schema; producers adapt |
| A performance-regression tradeoff is disputed | Inference Optimization and Inference and Serving Services must agree; escalates to SVP if not resolved in 48h |

---

## What Product Operations Is NOT

Because this role is cross-cutting, its scope is frequently misunderstood. For clarity:

| Product Operations does | Product Operations does NOT |
|---|---|
| Run the launch-readiness gate process | Own the product roadmap for any pillar |
| Wire metering and showback across teams | Make product decisions about what to build |
| Coordinate capacity provisioning at launch time | Own engineering delivery for any workstream |
| Assemble compliance evidence packages | Define compliance requirements (that is Governance) |
| Write and maintain cross-pillar runbooks | Write pillar-specific runbooks (those stay with the pillar) |
| Surface recurring cross-team friction and fix the process | Resolve technical disputes between pillars (escalation goes to SVP) |

---

## The Infra Boundary (below Kubernetes)

None of the six pillars own anything below the Kubernetes line. The rules from the [[RackAI Roadmap]]:

- **Observability:** Infra builds cluster observability; the above-K8s pillars consume it
- **Accelerator selection:** Infra owns the hardware choice; Inference and Serving Services is a constraining stakeholder (if a model requires specific hardware, Infra selects within our constraints)
- **Cluster and node provisioning:** Infra. Capacity Pool allocation within a provisioned cluster belongs to Inference and Serving Services

---

## Quick-Reference: Who to Call

| Question | Call |
|---|---|
| Can we serve this model on our hardware? | Inference and Serving Services (capacity) + Inference Optimization (economics) |
| Should we add this model to the catalog? | Model Services |
| Why is latency degraded on model X? | Inference Optimization (benchmark) + Inference and Serving Services (serving plane) |
| Does this deployment satisfy our compliance posture? | AI Governance & Assurance |
| How do we route a multi-step agent task? | AI Harness |
| When can we launch this new capability? | Product Operations (launch gate) |
| How are we tracking against the cost floor? | Inference Optimization |
| What evidence do we need for the SOC 2 audit? | AI Governance & Assurance (requirements) + Product Operations (assembly) |
| Is the Empirical Map data for model X trustworthy? | AI Harness (owns the Map) + Inference Optimization (produced the data) |
| Who owns the agent identity spec? | AI Governance & Assurance (design) + AI Harness (enforcement) |

---

## See Also

- [[RackAI Organizational Design]] — org chart, headcount, and reporting structure
- [[Inference and Serving Services]] — pillar hub
- [[Model Services]] — pillar hub
- [[Inference Optimization]] — pillar hub
- [[AI Governance and Assurance]] — pillar hub
- [[AI Harness]] — pillar hub
- [[AI Operations Product]] — the Product Operations workstream hub
- [[RackAI Roadmap]] — roadmap ownership by pillar
- [[Three Battlegrounds]] — the harness boundary and operator stack that defines why these boundaries exist
