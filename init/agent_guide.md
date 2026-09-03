---
id: src-agent-guide
type: source
status: validated
owner: knowledge-graph-steward
domain: governance
aliases: [agent guide, agent standards, agent operating manual]
related: [hub-root, src-init]
parent: hub-root
source_docs: []
confidence: validated
last_reviewed: 2026-09-03
summary: "Agent operating guide for Rack AI OpenRouter knowledge base maintenance."
---

# AGENT_GUIDE.md — Rack AI OpenRouter Wiki Agent Standards

## Purpose

This file defines the operating standards for any agent working in the Rack AI OpenRouter knowledge base.

The repository is a living knowledge graph that models canonical entities, operational ontology, commercial and capacity logic, evidence and validation, and human-readable wiki navigation. Every agent must protect semantic integrity, traceability, and corpus consistency.

---

## Core Operating Principle

**The repository is a living model of the Rack AI inference operating system, not a set of isolated documents.**

Agents do not merely edit pages. They maintain a knowledge system.

- Entity ontology is the semantic backbone.
- Operational ontology is the digital twin.
- Wiki pages are the human interface.
- Evidence pages explain why the model is trusted.
- Consistency checks ensure the corpus tells one coherent story.

---

## Agent Duties

1. Read the initialization standards before making changes.
2. Find the canonical home for a concept before creating anything new.
3. Preserve source traceability for every important claim, especially performance numbers.
4. Keep entity, operational, commercial, evidence, and wiki layers separate.
5. Update dependent notes together when meaning changes.
6. Flag uncertainty instead of hiding it.
7. Run a consistency pass before concluding work.

---

## Read-First Rule

Before editing, read:
- `INIT.md`
- the current hub note for the relevant domain
- the source index
- the changelog
- the open questions register
- any directly related canonical notes

If the relevant concept already exists, extend it rather than duplicating it.

---

## Canonical-Home Rule

Every concept must have exactly one canonical home. Examples:
- one canonical `[[DeepSeek V4 Flash]]`
- one canonical `[[Capacity Pool]]`
- one canonical `[[TTFT]]`
- one canonical `[[Tokens per GPU-Second]]`

All other notes must link to the canonical note rather than redefining the concept. If a concept needs synonyms, add aliases. Do not create parallel definitions.

---

## No-Edit-Without-Plan Rule

Before changing content, prepare a short internal change plan: what will change, why, what source files support it, what downstream notes may be affected, whether confidence or evidence changes. Do not edit blindly.

---

## Evidence Labeling Rule

Every meaningful claim must carry a confidence state: `assumed`, `derived`, `measured`, `validated`. Use the weakest truthful state. If evidence is incomplete, say so. Do not present assumptions or roadmap targets as measured facts.

---

## Conflict Escalation Rule

If sources disagree (e.g., a roadmap target vs. an actual benchmark, or two competitive datapoints), do not smooth over the inconsistency. Surface it, mark it as an open question or validation item, identify the affected documents, and preserve both sides until resolved. Hidden conflicts are failures.

---

## Terminology Freeze Rule

Use canonical names consistently. If a term has multiple names, choose one canonical name, store the others as aliases, and update references. Do not invent new names for existing concepts.

---

## Link Discipline Rule

Every important note should link to its parent, children, peers, dependencies, evidence, and related concepts. No orphan concepts. If a note is isolated, decide whether it is missing links, belongs elsewhere, should be a hub, or should be deprecated.

---

## Layer Purity Rule

Keep layers distinct:
- **Entity layer** — canonical objects (models, deployments, runtimes, GPU fleet, capacity pools).
- **Operational layer** — serving lifecycle, workflows, events, metrics, formulas, telemetry, routing.
- **Commercial and capacity layer** — unit economics, pricing, allocation, forecasting.
- **Evidence layer** — benchmarks, assumptions, validations, competitive data.
- **Wiki layer** — navigation, indexes, MOCs, scorecards, human-friendly explanations.

Do not mix these layers unless the note is explicitly a hub or index.

---

## Fitness Check Rule

When new sources or benchmarks are added, perform a fitness check. Ask:
- Does this create a new canonical object?
- Does an existing object need new attributes, relationships, aliases, or lifecycle states?
- Does a workflow need to change?
- Does a metric, formula, coefficient, or event need updating?
- Does the confidence of an existing concept need to change?
- Does the new source alter the story the corpus tells?

A source is not fully incorporated until the relevant notes have been reviewed for impact.

---

## Consistency Pass Rule

After any meaningful change, run a consistency pass. Verify:
- terminology is consistent
- definitions do not contradict
- commercial, operational, and capacity models align
- dependencies live in the correct layer
- no note silently diverges from the canonical model
- no open question is being treated as resolved
- no new conflict remains hidden
- no performance number appears without a benchmark or telemetry source

If the corpus is inconsistent, flag it and record it.

---

## Deprecation and Migration Rule

When a concept changes, do not erase the old one without a trace. Mark the old note/term deprecated, preserve backward-compatible aliases, add the new canonical term, update dependent notes, record the migration date, and explain the reason.

---

## Graph Invariants

These must always remain true:
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

## Relationship Standards

Use explicit relationship types rather than vague links:
`OWNS`, `BELONGS_TO`, `DERIVES`, `IMPLEMENTS`, `USES`, `CONSUMES`, `PRODUCES`, `MEASURES`, `VALIDATES`, `SUPPORTS`, `DEPENDS_ON`, `CONSTRAINS`, `GENERATES`, `FORECASTS`, `GOVERNS`, `ALLOCATES`, `ROUTES_TO`, `SERVES`.

Strong relationships for canonical structure. Weak relationships for contextual or supporting links only.

---

## Change Control Rule

Every significant change must be summarized in a changelog entry capturing: objects added/changed, edges added/removed, notes requiring review, open questions created, validations impacted, assumptions impacted, downstream documents affected. No silent edits.

---

## Quality Gates

A note or update is acceptable only if it has: a clear purpose, a canonical title, a stable ID, the correct note type, an owner, source traceability, a confidence state, explicit relationships, no duplicate concept, no layer violation, and no unresolved contradiction left hidden.

---

## See Also

- [[Rack AI Knowledge Base]] — root navigation hub
- [[Evidence Hub]] — confidence and evidence framework
- [[Governance Hub]] — governance standards
- [[Source Inventory]] — corpus inventory
