---
id: ent-empirical-map
type: entity
status: draft
owner: rackai-product
domain: performance
aliases: [empirical map, the map, per-workload measurement, reliability map, cost map]
related: [ent-governed-harness, ent-model, ent-benchmark-run, wf-request-routing, wf-verification, wf-eval-as-ci, met-cost-per-outcome, hub-entities, src-rackai-dev-plan]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-entities
summary: "Canonical entity: the living record of where each model is reliable and what it costs, from our operating data."
---

# Empirical Map

## Definition

The **Empirical Map** is the living record of **where each model is reliable and what it costs**, measured per workload from Rackspace's own operating data rather than from public benchmarks. A public benchmark measures the model in the abstract; the map measures *this workload, with these tools and this context* against several models. Each cell of the map is a (workload × [[Governed Harness|harness]] × [[Model]]) result: what the model did, whether it passed the checks, and what it cost.

> **Assumed confidence.** Program 1 thread 1.5 (build) with a research tail on trust/prediction. Net-new in the plan's coverage table (no product covers it today). This is one of the **moat** concepts — it only accrues value from operating inside the perimeter.

## Layer

L1 — Entity Ontology. The map is a derived record that overlays the serving chain; it is built on the [[Governed Harness]] + [[Model]] pairing and read downstream by routing and the loop.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Cell | One (workload × harness × model) measurement | struct | assumed |
| Reliability | Where a model is reliable for a workload (from [[Verification]] checks) | metric | assumed |
| Cost dimension | Measured token cost per workload (the cost spine of the loop) | metric | assumed |
| Coverage/trust | How much measurement is enough to trust a cell (research tail) | metric | assumed |
| Predictiveness | Whether a cell predicts production behavior (research tail) | metric | assumed |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Governed Harness]] | → | Records harness×model reliability & cost |
| MEASURES | [[Model]] | → | Per-workload, not abstract benchmark |
| DERIVES | [[Benchmark Run]] | ← | Built from eval runs across models |
| USED_BY | [[Request Routing]] | ← | Routing reads measured cost & reliability from the map |
| USED_BY | [[Self-Improvement Loop]] | ← | The loop builds on the map |
| PRODUCES | [[Cost per Outcome]] | → | The cost dimension feeds cost-per-outcome economics |
| DEPENDS_ON | [[Verification]] | → | Checks supply the reliability signal |

## Evidence

- Source: dev plan Program 1 thread 1.5; cost loop ("meter → govern → route → reason").
- Confidence rationale: `assumed` — planned build. Downstream confidence (routing, FinOps) may not exceed the map's `assumed` state until the eval framework is measured.

## See Also

- [[Entity Ontology Hub]]
- [[Eight-Layer Stack]]
- [[Verification]]
- [[Request Routing]]
- [[Cost per Outcome]]
