# Rack AI OpenRouter Knowledge Base Operating Standards

This repository is a living knowledge system for the Rack AI inference program on OpenRouter, not a folder of documents.

## Core Principle

The repository models:
- Canonical entities of the inference business (models, deployments, GPU fleet, capacity pools)
- Operational ontology of the serving platform (workflows, events, metrics, formulas, coefficients, policies)
- Commercial and capacity model (unit economics, pricing, fleet allocation, forecasting)
- Evidence base behind every claim (benchmarks, assumptions, validations, open questions)
- Human-readable wiki exposing the graph

Documents are projections of the underlying knowledge graph.

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

Lower layers may reference higher. Higher layers must not depend on lower.

## Non-Negotiable Standards

1. **One Concept Rule** — Each concept exists exactly once in canonical form. All other pages link to it.
2. **Stable Identity** — Every canonical object has a permanent ID. IDs never change.
3. **Typed Relationships** — Use explicit relationship types: OWNS, BELONGS_TO, DERIVES, IMPLEMENTS, USES, CONSUMES, PRODUCES, MEASURES, VALIDATES, SUPPORTS, DEPENDS_ON, CONSTRAINS, GENERATES, FORECASTS, GOVERNS, ALLOCATES, ROUTES_TO, SERVES.
4. **Layer Integrity** — Nothing may skip layers. Market Demand → Model → Model Deployment → Serving Runtime → Capacity Pool → GPU Fleet → Datacenter/Topology.
5. **Bidirectional Completeness** — Every important edge represented in both directions.
6. **No Orphans** — Every node needs an owner, source, confidence level, inbound/outbound links.
7. **Evidence First** — No important claim should be untraceable. Every performance number carries a benchmark or telemetry source.
8. **Confidence Propagation** — Confidence flows through the graph. Downstream confidence may not exceed weakest upstream evidence.
9. **Semantic Drift Detection** — Meaning changes trigger review of synonyms, aliases, relationships, dependent docs.
10. **Story Consistency** — The corpus tells one coherent story about why Rack AI serves inference on OpenRouter, what the platform is, how it operates, how it is priced and measured, and how it evolves.

## Canonical Layer Model

### Layer 1 — Entity Ontology
Canonical business/domain objects: Model, Model Deployment, Serving Runtime, GPU Node, GPU Cluster, Capacity Pool, Datacenter/Region, Topology, OpenRouter Provider Integration, Benchmark Run, Model Deployment Specification, Request/Traffic Class.

### Layer 2 — Operational Ontology / Digital Twin
Serving lifecycle, deployment workflows, model-launch (day-zero factory) workflow, autoscaling, admission control, routing, canary/rollback, events, metrics, formulas, coefficients, policies, telemetry, optimization loops.

### Layer 3 — Commercial and Capacity Model
Unit economics (cost/1M tokens, revenue/GPU-hour, gross margin/model), pricing, capacity pools and allocation, demand forecasting, fleet yield optimization, procurement triggers.

### Layer 4 — Evidence and Validation
Benchmark results, competitive comparisons, assumptions, validation items, open questions, confidence states, change history.

### Layer 5 — Wiki / Human Navigation Layer
Hub pages, entity pages, workflow pages, indexes, MOCs, evidence pages, changelogs, crosswalks, model scorecards.

## Canonical Note Types

Every note must declare a type: `entity`, `workflow`, `event`, `metric`, `formula`, `coefficient`, `policy`, `assumption`, `validation`, `evidence`, `source`, `hub`, `index`, `change`, `glossary`.

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

## Confidence States

- `assumed` — no direct evidence yet (e.g., a projected TTFT before benchmarking)
- `derived` — inferred from related evidence (e.g., cost/token extrapolated from a partial benchmark)
- `measured` — supported by a benchmark run or production telemetry
- `validated` — confirmed through production observation against SLOs or competitive data

## Output Format Standards

All content must be **renderable without specialized tooling**. Preferred output formats:

1. **Markdown** — prose, tables, lists, headers. The default for all notes.
2. **CSV** — tabular data (fleet inventory, benchmark matrices, scorecards). Stored alongside any source spreadsheet.
3. **Mermaid** — all diagrams and flowcharts. Fenced `mermaid` code blocks inside markdown. No image-based diagrams, no ASCII art, no PlantUML.
4. **YAML frontmatter** — structured metadata (already standard).

### Diagram Rules

- All architecture diagrams, serving flows, sequence diagrams, and state machines MUST use Mermaid syntax.
- Mermaid blocks go inside markdown files as fenced code blocks (` ```mermaid `).
- Standalone `.mmd` files are acceptable for large diagrams.
- No embedded images for diagrams that can be expressed as Mermaid.
- If a diagram cannot be expressed in Mermaid (e.g., a vendor topology PDF), reference it by filename rather than embedding.
- **No forced colors or inline styles in Mermaid diagrams.** No `style` declarations, no `classDef` with colors, no `fill:`/`stroke:` overrides. Let the rendering theme handle appearance.

### Why

- Mermaid renders natively in Obsidian, GitHub, and most markdown viewers — the same rendering app the sister AIOS Wiki targets.
- CSV is universally parseable and diffable in git.
- Markdown is the lingua franca. No proprietary formats for content that can be plain text.
