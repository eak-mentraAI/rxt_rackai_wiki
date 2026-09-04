# RackAI Platform Wiki Agent Behavior Standards

## Core Operating Principle

The repository is a living model of the **RackAI platform** operating system and the initiatives built on it (the OpenRouter inference program being the first), not a set of isolated documents. Agents maintain a knowledge system, not just pages. **Canonical product name: RackAI** (aliases: RMPAI, RackAI Aurora).

## Agent Duties

1. Read initialization standards before making changes.
2. Find the canonical home for a concept before creating anything new.
3. Preserve source traceability for every important claim, especially performance numbers.
4. Keep entity, operational, commercial, evidence, and wiki layers separate.
5. Update dependent notes together when meaning changes.
6. Flag uncertainty instead of hiding it.
7. Run a consistency pass before concluding work.

## Key Rules

### Read-First Rule
Before editing, read: the current hub note for the domain, the source index, the changelog, the open questions register, and any related canonical notes.

### Canonical-Home Rule
Every concept has exactly one canonical home. All other notes link to it. Use aliases for synonyms, not parallel definitions. (Example: one canonical `[[TTFT]]` metric, one canonical `[[DeepSeek V4 Flash]]` model.)

### No-Edit-Without-Plan Rule
Before changing content, prepare: what will change, why, what sources support it, what downstream notes are affected, whether confidence changes.

### Evidence Labeling Rule
Every meaningful claim carries a confidence state: assumed, derived, measured, validated. Use the weakest truthful state. A projected benchmark number is `assumed` until a benchmark run exists.

### Conflict Escalation Rule
If sources disagree (e.g., roadmap target vs. measured benchmark), surface the conflict. Mark it as an open question. Preserve both sides until resolved. Hidden conflicts are failures.

### Terminology Freeze Rule
Use canonical names consistently. Store alternatives as aliases. Do not invent new names for existing concepts.

### Link Discipline Rule
Every important note links to: parent, children, peers, dependencies, evidence, related concepts. No orphan concepts.

### Layer Purity Rule
Keep entity, operational, commercial/capacity, evidence, and wiki layers distinct. Do not mix unless the note is explicitly a hub or index.

### Consistency Pass Rule
After meaningful changes, verify: terminology consistency, no contradictions, layers aligned, no silent divergence, no hidden conflicts.

## Graph Invariants

These must always remain true:
- Every Model Deployment serves exactly one Model.
- Every Model Deployment declares exactly one Model Deployment Specification.
- Every Model Deployment runs on exactly one Serving Runtime configuration.
- Every Model Deployment draws from exactly one Capacity Pool.
- Every Model Deployment belongs to exactly one Organization (tenant).
- Every Capacity Pool maps to GPU Nodes within one or more Clusters.
- Every GPU Node belongs to exactly one Cluster and one Datacenter/Region.
- Consumers (OpenRouter traffic or direct RackAI tenants) see Model endpoints, never GPU hardware directly.
- Every Fine-Tuning Job consumes a Dataset and produces a LoRA Adapter; every LoRA Adapter targets exactly one base Model.
- Every initiative (e.g. OpenRouter Provider Integration, OpenRouter Private Model Integration) routes into the serving chain via Model endpoints; it never bypasses Model Deployment or references GPUs directly.
- Commercial objects reference Models, Organizations, and Capacity Pools, not individual GPUs.
- Every metric has a source or formula.
- Every formula references canonical coefficients or measurable inputs.
- Every coefficient has evidence and confidence.
- Every performance claim traces to a Benchmark Run or production telemetry.
- Every assumption has an owner and an exit criterion.
- Every validation item identifies the documents it can change.
- Every layer is traversable from demand (OpenRouter or direct tenant) to GPU topology and back.

## Quality Gates

A note is acceptable only if it has:
- Clear purpose
- Canonical title
- Stable ID
- Correct note type
- Owner
- Source traceability
- Confidence state
- Explicit relationships
- No duplicate concept
- No layer violation
- No unresolved contradiction left hidden

## Relationship Types

Use explicit typed relationships:
OWNS, BELONGS_TO, DERIVES, IMPLEMENTS, USES, CONSUMES, PRODUCES, MEASURES, VALIDATES, SUPPORTS, DEPENDS_ON, CONSTRAINS, GENERATES, FORECASTS, GOVERNS, ALLOCATES, ROUTES_TO, SERVES.

Strong relationships for canonical structure. Weak relationships for contextual/supporting links only.
