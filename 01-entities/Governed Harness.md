---
id: ent-governed-harness
type: entity
status: draft
owner: rackai-product
domain: platform
aliases: [governed harness, harness, harness layer, agent harness, agent scaffolding]
related: [ent-model-deployment, ent-serving-runtime, ent-empirical-map, ent-agent-identity, wf-request-routing, wf-verification, hub-entities, src-rackai-dev-plan]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-entities
summary: "Canonical entity: the governed scaffolding around a model (context, tools, memory, control flow, guardrails)."
---

# Governed Harness

## Definition

A **Governed Harness** is the scaffolding around a raw model that makes it reliable for a specific workload: context assembly, tools, memory, control flow, and guardrails, wrapped by the governance and assurance planes. A raw [[Model]] is not reliable on its own; the same model behaves very differently depending on its harness. An enterprise runs **many harnesses, not one** — one per agent, domain, or workload — so the canonical goal is a *repeatable harness pattern*, not a single build.

> **Assumed confidence.** This is Program 1's near-term build in the [[RackAI Enterprise AI Development Plan]] (threads 1.2/1.3). The repeatable pattern and durable runtime are planned, not shipped; a partial precursor exists in Uniphore/RackAI tool-use and grounding today (Table 2).

## Layer

L1 — Entity Ontology. The harness sits **above** the serving chain, between demand and the model endpoint:

**Market Demand → Governed Harness → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

The harness consumes Model endpoints; it never references GPUs directly. It is the unit [[Request Routing]] and the [[Empirical Map]] are organized around (a workload runs against a harness + model pairing).

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Harness pattern | The repeatable template a specific harness instantiates | struct | assumed |
| Context assembly | How the right internal data is pulled in (messy, permission-scoped) | struct | assumed |
| Tools | Tool/integration set available to the harness | set | assumed |
| Memory policy | Keep/drop/resurface over long tasks (deep version → [[Self-Improvement Loop]]) | struct | assumed |
| Control flow | Orchestration of steps within the harness | struct | assumed |
| Guardrails | Policy checkpoints enforced during a run | set | assumed |
| Cost per outcome | Measured from day one (→ [[Cost per Outcome]]) | metric | assumed |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Pattern | Repeatable harness template defined | Program 1 thread 1.2 | Instantiated on a workload |
| Proven | Instantiated and proven on one real workload | Workload runs end to end | Repeated across domains |
| Durable | Runtime can replay and recover a run (1.3) | Observability + replay in place | Retired |
| Retired | Superseded or decommissioned | — | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| USES | [[Model]] | → | Wraps a model to make it reliable |
| CONSUMES | [[Model Deployment]] | → | Calls the model endpoint, never GPUs |
| MEASURED_BY | [[Empirical Map]] | → | Workload×harness×model reliability & cost recorded |
| ROUTED_BY | [[Request Routing]] | ← | Routing sends a task to the right harness/model/human |
| GOVERNED_BY | [[Verification]] | ← | Each step checked; evidence for assurance |
| USES | [[Agent Identity]] | → | Acts under a scoped, delegated identity |

## Evidence

- Source: dev plan Program 1 (threads 1.2 harness layer, 1.3 reliability and runtime).
- Confidence rationale: `assumed` — a working-draft build target. Precursor tool-use/grounding is `~` (partial) in the plan's coverage table; the durable, replayable runtime is a net gap.

## See Also

- [[Entity Ontology Hub]]
- [[Eight-Layer Stack]]
- [[Empirical Map]]
- [[Verification]]
