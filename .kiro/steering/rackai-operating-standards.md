# RackAI Platform Knowledge Base Operating Standards

This repository is a living knowledge system for the **RackAI platform** — Rackspace's Kubernetes-native AI inference and fine-tuning platform — and the **initiatives** built on it. The **OpenRouter inference program** is the first initiative (a distribution/go-to-market surface), one aspect of the platform rather than the whole. This is not a folder of documents.

**Canonical product name:** RackAI. `RMPAI` and `RackAI Aurora` are aliases of the same product.

## Core Principle

The repository models:
- Canonical entities of the RackAI platform (organizations/tenancy, models, deployments, serving runtimes, fine-tuning jobs, datasets, LoRA adapters, accelerator classes, GPU fleet, capacity pools, control plane, environments)
- Operational ontology of the serving and fine-tuning platform (workflows, events, metrics, formulas, coefficients, policies)
- Commercial and capacity model (unit economics, metering, billing, pricing, fleet allocation, forecasting)
- Evidence base behind every claim (benchmarks, assumptions, validations, open questions)
- Initiatives on the platform (OpenRouter provider path and private-model path, and future surfaces)
- Human-readable wiki exposing the graph

Documents are projections of the underlying knowledge graph.

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

Shipped beats planned: where a platform spec describes a planned capability and a shipped release note/product doc contradicts it, shipped reality wins for "what exists today" and the gap becomes an open question. Planned capability carries `assumed` confidence, never asserted as present.

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
10. **Story Consistency** — The corpus tells one coherent story: what the RackAI platform is (inference + fine-tuning, tenancy, control plane), how it operates, how it is metered/priced/measured, how it evolves, and why the OpenRouter inference program and future initiatives sit on top of it.

## Canonical Layer Model

### Layer 1 — Entity Ontology
Canonical business/domain objects.
- **Platform:** Organization (tenant), Model, Model Class, Model Deployment, Model Deployment Specification, Serving Runtime, Dataset, Fine-Tuning Job, LoRA Adapter, Registry Credential, Accelerator Class, API Key, RackAI Control Plane, Environment (dev/staging/production), GPU Node, GPU Cluster, Capacity Pool, Datacenter/Region, Topology, Benchmark Run, Request/Traffic Class.
- **OpenRouter initiative:** OpenRouter Provider Integration, OpenRouter Private Model Integration, Model Catalog (`/models`) Endpoint.

### Layer 2 — Operational Ontology / Digital Twin
Serving lifecycle, deployment workflows, fine-tuning workflow, model-launch (day-zero factory) workflow, autoscaling, admission control, routing, canary/rollback, metering, monitoring/observability, identity & access control, audit, events, metrics, formulas, coefficients, policies, telemetry, optimization loops.

### Layer 3 — Commercial and Capacity Model
Unit economics (cost/1M tokens, revenue/GPU-hour, gross margin/model), metering and billing/payment, pricing (OpenRouter and direct), capacity pools and allocation, demand forecasting, fleet yield optimization, procurement triggers.

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
