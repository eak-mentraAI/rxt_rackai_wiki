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
last_reviewed: 2026-09-03
summary: "Initialization instructions and operating standard for the Rack AI OpenRouter knowledge base."
---

# INIT.md — Rack AI OpenRouter Knowledge Base Operating Standard

## Purpose

This repository is not a folder of documents. It is a living knowledge system for the Rack AI inference program on OpenRouter.

Its job is to model:
- the **canonical entities** of the inference business
- the **operational ontology** of the serving platform (the digital twin)
- the **commercial and capacity model** (unit economics, allocation, forecasting)
- the **evidence base** behind every claim (benchmarks, telemetry, assumptions)
- the **human-readable wiki** that exposes the graph

Every change must preserve semantic integrity, traceability, and narrative consistency across the corpus.

---

## Core Principle

**The repository is a living model of the Rack AI inference operating system, not a collection of documents.**

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
5. Architecture documents
6. Engineering roadmap documents
7. Strategy / commercial documents
8. Benchmarks and external references (OpenRouter data, vendor specs)
9. Assumptions
10. Informal notes

Lower layers may reference higher layers. Higher layers must not depend on lower layers.

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
Nothing may skip layers. Canonical chain:

Market Demand → Model → Model Deployment → Serving Runtime → Capacity Pool → GPU Fleet → Datacenter/Topology

OpenRouter consumers never reference GPU hardware directly.

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
- why Rack AI serves inference on OpenRouter
- what the platform is
- how it operates
- how it is priced and measured
- how it evolves

---

## Canonical Layer Model

### Layer 1 — Entity Ontology
Canonical business/domain objects.

Examples:
- Model
- Model Deployment
- Model Deployment Specification
- Serving Runtime
- GPU Node
- GPU Cluster
- Capacity Pool
- Datacenter / Region
- Topology
- OpenRouter Provider Integration
- Benchmark Run
- Request / Traffic Class

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
- pricing on OpenRouter
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
