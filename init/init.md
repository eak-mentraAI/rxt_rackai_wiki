---
id: src-init
type: source
status: validated
owner: knowledge-graph-steward
domain: governance
aliases: [init.md, operating standard, knowledge base standard]
related: [hub-root]
parent: hub-root
source_docs: []
confidence: validated
last_reviewed: 2026-09-04
summary: "Initialization instructions and operating standard for the RackAI platform knowledge base."
---

# INIT.md — RackAI Platform Knowledge Base Operating Standard

## Purpose

This repository is not a folder of documents. It is a living knowledge system for the **RackAI platform** — Rackspace's Kubernetes-native AI inference and fine-tuning platform — and the **initiatives** built on top of it. The **OpenRouter inference program** is the first such initiative: a distribution and go-to-market surface where RackAI capacity is exposed to external demand. It is one aspect of the platform, not the whole.

Its job is to model:
- the **canonical entities** of the RackAI platform and its inference business
- the **operational ontology** of the serving and fine-tuning platform (the digital twin)
- the **commercial and capacity model** (unit economics, metering, billing, allocation, forecasting)
- the **evidence base** behind every claim (benchmarks, telemetry, assumptions)
- the **human-readable wiki** that exposes the graph

Every change must preserve semantic integrity, traceability, and narrative consistency across the corpus.

---

## Scope

- **Platform (in scope, canonical):** RackAI as a product — organizations/tenancy, the model catalog and registry, model deployments and serving runtimes, fine-tuning (datasets, jobs, LoRA adapters), accelerator/GPU selection, identity & access control, metering, monitoring/observability, the control plane, and the dev/staging/production environments.
- **Initiatives (in scope, modeled as programs on the platform):** the OpenRouter inference program (public-provider path and private-model path) and any future go-to-market surface. Initiative-specific concepts link *down* into the platform concepts they depend on.
- **Canonical product name:** **RackAI**. `RMPAI` (main PRD) and `RackAI Aurora` (a technical spec) are **aliases** of the same product, not separate entities.

---

## Core Principle

**The repository is a living model of the RackAI platform operating system, not a collection of documents.**

Documents are projections of the underlying knowledge graph.

- The **entity ontology** is the semantic backbone.
- The **operational ontology** is the digital twin.
- The **wiki layer** is the human interface.
- The **evidence layer** explains why the model is trusted.
- The **consistency layer** ensures the corpus tells one coherent story.

---

## Truth Hierarchy

When sources conflict, use this order of authority:

1. Canonical object definitions
2. Canonical ontology / domain model
3. Canonical operational model (serving lifecycle, scheduling, routing)
4. Canonical APIs, events, metrics, formulas
5. RackAI platform product specs (PRDs, technical specs, API reference, product docs)
6. Architecture documents
7. Engineering roadmap documents
8. Strategy / commercial / initiative documents
9. Benchmarks and external references (OpenRouter data, vendor specs)
10. Assumptions
11. Informal notes

Lower layers may reference higher layers. Higher layers must not depend on lower layers.

Note on shipped vs. planned: RackAI platform product specs (level 5) describe the authoritative platform. Where a spec describes a *planned/roadmap* capability and a *shipped* release note or product doc contradicts it, the shipped reality wins for "what exists today" and the gap is recorded as an open question — planned capability is marked with the honest confidence state (`assumed`), not asserted as present.

---

## Non-Negotiable Standards

### 1. One Concept Rule
Each concept exists exactly once in canonical form. All other pages must link to the canonical note rather than redefining it.

### 2. Stable Identity
Every canonical object, workflow, metric, formula, event, assumption, and validation item must have a permanent ID. IDs never change. Titles may evolve.

### 3. Typed Relationships
Use explicit relationship types, not vague links:
`OWNS`, `BELONGS_TO`, `DERIVES`, `IMPLEMENTS`, `USES`, `CONSUMES`, `PRODUCES`, `MEASURES`, `VALIDATES`, `SUPPORTS`, `DEPENDS_ON`, `CONSTRAINS`, `GENERATES`, `FORECASTS`, `GOVERNS`, `ALLOCATES`, `ROUTES_TO`, `SERVES`.

### 4. Layer Integrity
Nothing may skip layers. Canonical serving chain:

Demand (OpenRouter or direct tenant) → Model → Model Deployment → Serving Runtime → Capacity Pool → GPU Fleet → Datacenter/Topology

Consumers (OpenRouter traffic or direct RackAI tenants) see Model endpoints; they never reference GPU hardware directly. Initiatives such as the OpenRouter inference program attach *above* Demand and route into this chain — they never bypass it.

### 5. Bidirectional Completeness
Every important edge should be represented in both directions where useful.
- `Model Deployment USES Capacity Pool`
- `Capacity Pool USED_BY Model Deployment`

### 6. No Orphans
Every important node must have: an owner, a source, a confidence level, inbound links, outbound links, and a lifecycle state if applicable.

### 7. Evidence First
No important claim should be untraceable. Every canonical note should answer: where did this come from, how confident are we, what supports it, what depends on it. **Every performance number must trace to a benchmark run or production telemetry.**

### 8. Confidence Propagation
Confidence must flow through the graph. Example path:
Benchmark → Coefficient → Formula → Cost/Economics → Scorecard.
The confidence of a downstream number may not exceed the weakest upstream evidence.

### 9. Semantic Drift Detection
Any update that changes meaning must trigger a review of synonyms, aliases, relationships, dependent documents, downstream formulas, metrics, assumptions, and validations.

### 10. Story Consistency
The corpus must always tell one coherent story:
- what the RackAI platform is (inference + fine-tuning, tenancy, control plane)
- how it operates
- how it is metered, priced, and measured
- how it evolves
- why the OpenRouter inference program (and future initiatives) sit on top of it, and how each initiative depends on platform capabilities

---

## Canonical Layer Model

### Layer 1 — Entity Ontology
Canonical business/domain objects.

Examples (platform):
- Organization (tenant)
- Model / Model Class
- Model Deployment
- Model Deployment Specification
- Serving Runtime
- Dataset
- Fine-Tuning Job
- LoRA Adapter
- Registry Credential
- Accelerator Class
- API Key
- RackAI Control Plane
- Environment (dev / staging / production)
- GPU Node
- GPU Cluster
- Capacity Pool
- Datacenter / Region
- Topology
- Benchmark Run
- Request / Traffic Class

Examples (OpenRouter initiative):
- OpenRouter Provider Integration
- OpenRouter Private Model Integration
- Model Catalog (`/models`) Endpoint

### Layer 2 — Operational Ontology / Digital Twin
The behavior model of the platform.

Includes:
- serving lifecycle and state transitions
- deployment, canary, and rollback workflows
- the day-zero model launch factory workflow
- autoscaling, admission control, routing, GPU reallocation
- events, metrics, formulas, coefficients, telemetry, policies
- optimization / closed-loop workflows

### Layer 3 — Commercial and Capacity Model
How demand maps to capacity, economics, and allocation.

Includes:
- unit economics (cost/1M tokens, revenue/GPU-hour, gross margin/model)
- metering and billing/payment (usage capture → invoicing/payout)
- pricing (OpenRouter and direct)
- capacity pools and dynamic allocation
- demand forecasting
- fleet yield optimization and procurement triggers

### Layer 4 — Evidence and Validation
The support structure for the model.

Includes:
- benchmark results and competitive comparisons
- assumptions
- validation items
- open questions
- confidence states
- change history

### Layer 5 — Wiki / Human Navigation Layer
The Obsidian-facing presentation layer.

Includes:
- hub pages, entity pages, workflow pages
- indexes, MOCs
- model scorecards
- evidence pages, changelogs, crosswalks

---

## Canonical Note Types

Every note must declare a type. Use one of:

`entity`, `workflow`, `event`, `metric`, `formula`, `coefficient`, `policy`, `assumption`, `validation`, `evidence`, `source`, `hub`, `index`, `change`, `glossary`.

Do not mix incompatible roles in one note unless the note is explicitly a hub or index.

---

## Frontmatter Standard

Every note begins with YAML frontmatter:

```yaml
---
id: unique-stable-id
type: entity | workflow | event | metric | formula | coefficient | policy | assumption | validation | evidence | source | hub | index | change | glossary
status: draft | reviewed | validated | deprecated
owner: team-or-role
domain: strategy | product | platform | performance | model-enablement | infrastructure | reliability | commercial | capacity | governance
aliases: []
related: []
source_docs: []
confidence: assumed | derived | measured | validated
last_reviewed: YYYY-MM-DD
parent: parent-note-id
summary: "One-line description of note purpose."
---
```

---

## Change Control Standards

### Governing Rule

> **No change is complete until the affected canonical notes, dependent notes, and fitness checks have been updated and re-passed.**

This one rule prevents drift from becoming hidden debt.

### Required Agent Execution Sequence

```
Change request
  → Impact scan (identify affected concepts and dependencies)
  → Edit canonical note (source-of-truth first)
  → Propagate dependent updates (layer order)
  → Run fitness checks
  → Run consistency pass
  → Record regressions or close them
  → Produce changelog entry
```

### Fitness Gates

1. **Structural fitness checks** — Run on every change (no duplicate concepts, no orphans, no broken backlinks, no layer violations, owner/source/confidence/relationships present, formulas/coefficients/benchmarks resolve).
2. **Story consistency checks** — Run after meaningful updates (one coherent story; commercial/operational/capacity/evidence layers agree; terminology stable; no silent redefinitions).
3. **Regression acceptance checks** — Run periodically and before release (traversal, reverse traversal, impact analysis, evidence-chain tracing, digital-twin simulation, graph health, multi-deliverable generation).

Full check definitions: `08-change-control/FITNESS_CHECKLIST.md`

### Thresholds

| Score | Status | Action |
|:-----:|--------|--------|
| 5/5 | Stable | No action required |
| 4/5 | Acceptable | Monitor; schedule improvement |
| 3.5–4/5 | Warning | Must be addressed before next release |
| < 3.5/5 | **Hard stop** | Must be fixed before merge |

### Change Packet Requirement

Before any meaningful edit, complete a change packet documenting: source of change, affected concepts, impact scan, propagation plan, confidence assessment, and open questions. Template: `08-change-control/CHANGE_PACKET.md`.

---

## Recertification Cadence

### Monthly (during active development)
- Rerun the full regression acceptance suite
- Rerun the consistency pass across all layers
- Identify newly stale assumptions (compare `last_reviewed` dates)
- Update confidence states where benchmarks or telemetry have arrived
- Refresh model scorecards with latest measured metrics
- Update score history in `08-change-control/REGRESSION_SUITE.md`

### On New Source Material or Benchmark
- Rerun structural fitness checks
- Rerun traversal and impact tests (R-01 through R-04)
- Update Source-to-Concept Crosswalk and Source Inventory
- Update affected model scorecards
- Verify no existing concept was silently redefined

### Quarterly
- Full regression suite with scoring
- Assumption Register review (exit criteria progress)
- Validation Register review
- Coefficient confidence audit

### On Milestone/Release
- Full regression suite — must score ≥ 4.0 average to pass
- No individual test below 3.5/5
- All blocking fitness check failures resolved
- Changelog published; score history updated

---

## Corpus Update Propagation

When new information enters the repository, agents must use the Corpus Update Propagation skill (defined in `.kiro/steering/corpus-update-propagation.md`). This ensures the canonical source-of-truth note is updated first, changes propagate through layers in correct order, confidence states are honestly maintained, contradictions are surfaced not hidden, and a change summary is produced. The skill is automatically active in all sessions.
