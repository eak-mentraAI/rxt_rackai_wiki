---
id: idx-kb-architecture
type: index
status: draft
owner: knowledge-graph-steward
domain: platform
aliases: [KB architecture, knowledge architecture, knowledge base design, wiki-kb-architecture]
related: [hub-root, idx-source-inventory]
source_docs: [init/init.md, init/agent_guide.md, openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Describes the Rack AI OpenRouter knowledge base architecture and design principles."
---

# Rack AI Knowledge Base Architecture

## 1. Executive Summary

This document defines the architecture of the Rack AI OpenRouter Knowledge Base — a living, layered knowledge system for Rack AI's inference program. It models canonical entities, operational behavior, commercial logic, evidence, and human-readable navigation as a coherent graph.

The knowledge base is a structured projection of an underlying knowledge graph, designed to:

- Provide a single source of truth for every canonical concept
- Maintain traceability from evidence (benchmark/telemetry) to recommendation
- Support ontology-level reasoning about the inference platform
- Serve as a navigable wiki for engineers and decision-makers
- Evolve safely as new benchmarks and telemetry arrive

It follows the same discipline as the sister AIOS Wiki so both render in the shared app and meet the same standards.

---

## 2. Design Principles

| Principle | Description |
|-----------|-------------|
| One Concept Rule | Each concept exists exactly once in canonical form |
| Stable Identity | Every canonical object has a permanent ID that never changes |
| Typed Relationships | All edges are explicit and typed (SERVES, USES, ALLOCATES, etc.) |
| Layer Integrity | Concepts follow the canonical chain without skipping layers |
| Evidence First | No important claim is untraceable; every performance number cites a source |
| Confidence Propagation | Downstream confidence ≤ weakest upstream evidence |
| Story Consistency | The corpus tells one coherent narrative |
| Canonical-First | Update existing notes; never create duplicates |
| Conflict Visibility | Surface disagreements (target vs. measured); never smooth them over |
| Layer Purity | Entity, operational, commercial, evidence, wiki layers are distinct |

---

## 3. Layer Model

```
┌─────────────────────────────────────────────────────────────┐
│  L5 — Wiki Navigation Layer                                 │
│  Hubs, indexes, MOCs, model scorecards, changelogs, glossary│
├─────────────────────────────────────────────────────────────┤
│  L4 — Evidence & Validation Layer                           │
│  Benchmarks, assumptions, validations, open questions       │
├─────────────────────────────────────────────────────────────┤
│  L3 — Commercial & Capacity Layer                           │
│  Unit economics, pricing, capacity pools, forecasting       │
├─────────────────────────────────────────────────────────────┤
│  L2 — Operational Ontology / Digital Twin                   │
│  Workflows, events, metrics, formulas, coefficients, policy │
├─────────────────────────────────────────────────────────────┤
│  L1 — Entity Ontology (Semantic Backbone)                   │
│  Models, deployments, runtimes, GPU fleet, capacity pools   │
└─────────────────────────────────────────────────────────────┘
```

Higher layers may reference lower layers. Lower layers must not depend on higher layers.

---

## 4. Canonical Abstraction Chain

```
Market Demand
  └─→ Model
       └─→ Model Deployment
            └─→ Serving Runtime
                 └─→ Capacity Pool
                      └─→ GPU Fleet
                           └─→ Datacenter / Topology
```

**Key constraint:** OpenRouter consumers see Model endpoints, not infrastructure. Commercial objects reference Models and Capacity Pools, never individual GPUs. The chain must not be bypassed.

---

## 5. Folder Structure

```
/
├── 00-hub/                     Navigation hubs
├── 01-entities/                L1 — Canonical entity notes
├── 02-operations/              L2 — Operational ontology
│   ├── workflows/
│   ├── events/
│   ├── metrics/
│   ├── formulas/
│   ├── coefficients/
│   └── policies/
├── 03-commercial/              L3 — Commercial & capacity
│   ├── economics/
│   ├── capacity-pools/
│   └── forecasting/
├── 04-evidence/                L4 — Evidence & validation
│   ├── assumptions/
│   ├── validations/
│   ├── benchmarks/
│   └── open-questions/
├── 05-wiki/                    L5 — Wiki navigation
│   ├── indexes/
│   ├── mocs/
│   ├── scorecards/
│   ├── glossary/
│   └── changelogs/
├── 06-sources/                 Source inventory & provenance
├── 08-change-control/          Fitness, regression, consistency, change packet
├── templates/                  Note type templates (15)
├── scripts/                    Frontmatter lint
└── init/                       Initialization standards
```

---

## 6. Note Type Taxonomy

| Type | Layer | Folder | Purpose |
|------|-------|--------|---------|
| `entity` | L1 | `01-entities/` | Canonical object |
| `workflow` | L2 | `02-operations/workflows/` | Process or state machine |
| `event` | L2 | `02-operations/events/` | Domain event |
| `metric` | L2 | `02-operations/metrics/` | Measurable indicator |
| `formula` | L2 | `02-operations/formulas/` | Calculation spec |
| `coefficient` | L2 | `02-operations/coefficients/` | Input value to formulas |
| `policy` | L2 | `02-operations/policies/` | Governance constraint |
| `assumption` | L4 | `04-evidence/assumptions/` | Stated belief without direct evidence |
| `validation` | L4 | `04-evidence/validations/` | Verification item |
| `evidence` | L4 | `04-evidence/benchmarks/` | Benchmark run / supporting data |
| `source` | Support | `06-sources/` | Source document provenance |
| `hub` | L5 | `00-hub/` | Navigation entry point |
| `index` | L5 | `05-wiki/indexes/` | Listing page |
| `change` | L5 | `05-wiki/changelogs/` | Change record |
| `glossary` | L5 | `05-wiki/glossary/` | Term definition |

---

## 7. Frontmatter Schema

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

### ID Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Entity | `ent-{name}` | `ent-model-deployment` |
| Workflow | `wf-{name}` | `wf-model-launch-factory` |
| Event | `evt-{name}` | `evt-deployment-canary-passed` |
| Metric | `met-{name}` | `met-tokens-per-gpu-second` |
| Formula | `fml-{name}` | `fml-cost-per-1m-tokens` |
| Coefficient | `coeff-{name}` | `coeff-fp8-throughput` |
| Policy | `pol-{name}` | `pol-admission-control` |
| Assumption | `asm-{name}` | `asm-fp8-quality-neutral` |
| Validation | `val-{name}` | `val-deepseek-h200-fp8` |
| Benchmark/Evidence | `bench-{name}` | `bench-deepseek-h200-fp8` |
| Hub | `hub-{domain}` | `hub-operations` |
| Source | `src-{name}` | `src-engineering-roadmap` |

---

## 8. Relationship Model

Edge types: `OWNS`, `BELONGS_TO`, `DERIVES`, `IMPLEMENTS`, `USES`, `CONSUMES`, `PRODUCES`, `MEASURES`, `VALIDATES`, `SUPPORTS`, `DEPENDS_ON`, `CONSTRAINS`, `GENERATES`, `FORECASTS`, `GOVERNS`, `ALLOCATES`, `ROUTES_TO`, `SERVES`.

- **Strong edges** — canonical structure (SERVES, USES, ALLOCATES, BELONGS_TO, DERIVES)
- **Weak edges** — contextual/supporting (SUPPORTS, related)
- **Bidirectional** — important edges represented both ways (`Model Deployment USES Capacity Pool` ↔ `Capacity Pool USED_BY Model Deployment`)

---

## 9. Confidence & Evidence Framework

| State | Definition | Evidence Requirement |
|-------|-----------|----------------------|
| `assumed` | No direct evidence; e.g., a projected TTFT | Rationale + exit criterion |
| `derived` | Inferred from related evidence | Reasoning documented |
| `measured` | Backed by a benchmark run or telemetry | Data source referenced |
| `validated` | Confirmed in production / against SLOs | Production observation |

Confidence flows downstream; a node's confidence may never exceed the minimum of its upstream dependencies. A roadmap or strategy target is `assumed` until a benchmark or telemetry supports it.

---

## 10. Graph Invariants

- Every Model Deployment serves exactly one Model.
- Every Model Deployment declares exactly one Model Deployment Specification.
- Every Model Deployment runs on exactly one Serving Runtime configuration.
- Every Model Deployment draws from exactly one Capacity Pool.
- Every Capacity Pool maps to GPU Nodes within one or more Clusters.
- Every GPU Node belongs to exactly one Cluster and one Datacenter/Region.
- OpenRouter consumers see Model endpoints, never GPU hardware directly.
- Commercial objects reference Models and Capacity Pools, not individual GPUs.
- Every metric has a source or formula.
- Every formula references canonical coefficients or measurable inputs.
- Every coefficient has evidence and confidence.
- Every performance claim traces to a Benchmark Run or production telemetry.
- Every assumption has an owner and an exit criterion.
- Every validation item identifies the documents it can change.
- Every layer is traversable from market demand to GPU topology and back.

---

## 11. Source Material Strategy

Source documents (the strategy and roadmap narratives, plus future benchmark exports and vendor specs) are treated as read-only reference material.

### Extraction Pipeline

```
Source Document → Source Note (06-sources/) → Canonical Note (01–05/) → Hub Update (00-hub/)
```

1. Sources are inventoried in [[Source Inventory]].
2. Concepts are extracted into canonical notes in the appropriate layer.
3. Provenance is preserved via `source_docs` frontmatter and the [[Source-to-Concept Crosswalk]].
4. Hubs and scorecards are updated to reflect new canonical content.

---

## 12. Change Control

Every meaningful change follows: Change Packet → edit canonical note → propagate → fitness checks → consistency pass → regression (if release) → changelog. See the [[Governance Hub]], [[FITNESS_CHECKLIST]], [[REGRESSION_SUITE]], [[CHANGE_PACKET]], and [[CONSISTENCY_REPORT]].

---

## 13. Implementation Roadmap

### Phase 1 — Initialization (Complete)
- [x] Steering files for agent standards
- [x] Init operating standard and agent guide
- [x] Change-control machinery (fitness, regression, consistency, change packet)
- [x] Frontmatter templates (15)
- [x] Frontmatter lint + Kiro hooks
- [x] Hub/navigation pages and this architecture document
- [x] Source inventory and crosswalk skeletons

### Phase 2 — Entity Ontology Extraction (Next)
- [ ] Extract canonical entities from the roadmap (Model, Deployment, Runtime, GPU fleet, Capacity Pool, etc.)
- [ ] Establish entity relationships and lifecycle states
- [ ] Build the entity index and source-to-concept crosswalk entries

### Phase 3 — Operational & Commercial
- [ ] Extract workflows (launch factory, autoscaling, routing, admission control)
- [ ] Extract metrics, formulas, coefficients (tokens/GPU-second, TTFT, cost/1M tokens)
- [ ] Build unit-economics model and capacity pools

### Phase 4 — Evidence & Scorecards
- [ ] Create Benchmark Library, Assumption Register, Validation Register
- [ ] Build per-model scorecards
- [ ] Establish first regression-suite baseline scores

---

## 14. Key Documents

| Document | Purpose |
|----------|---------|
| [[Rack AI Knowledge Base]] | Root navigation hub |
| [[Source Inventory]] | Source catalog |
| [[Source-to-Concept Crosswalk]] | Source-to-concept mapping |
| [[Entity Ontology Hub]] | L1 navigation |
| [[Operations Hub]] | L2 navigation |
| [[Commercial & Capacity Hub]] | L3 navigation |
| [[Evidence Hub]] | L4 navigation |
| [[Wiki Hub]] | L5 navigation |
| [[Governance Hub]] | Standards & change control |
