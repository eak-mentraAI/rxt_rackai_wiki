---
id: ent-benchmark-run
type: entity
status: draft
owner: performance-eng
domain: performance
aliases: [benchmark run, benchmark, perf run, performance test]
related: [ent-model, ent-model-deployment, ent-serving-runtime, ent-gpu-node, ent-traffic-class, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: a single measured performance test that anchors every performance claim."
---

# Benchmark Run

## Definition

A **Benchmark Run** is a single, measured performance test of a specific combination of [[Model]] + [[Serving Runtime]] + quantization + hardware + configuration, producing concrete numbers: time-to-first-token (TTFT), throughput, tokens-per-GPU-second, and cost. It is the evidence anchor of the platform — every performance claim traces back to a Benchmark Run or to production telemetry. Benchmark Runs record measurements; they do not assert targets.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A Benchmark Run is a measurement over a point in this chain — it observes a Model on a runtime and hardware config and produces evidence.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Run ID | Stable identifier for the run | string | validated |
| Model + version | Model under test | ref | validated |
| Serving runtime + version | Engine and version used | ref | validated |
| Quantization | Precision under test (BF16/FP8/FP4/INT8) | enum | validated |
| Hardware | GPU type/count and node config | struct | validated |
| Config | Parallelism and serving flags | struct | validated |
| Traffic profile | Workload shape used (see [[Traffic Class]]) | ref | validated |
| TTFT | Time to first token | measure | measured |
| Throughput | Output tokens per second | measure | measured |
| Tokens per GPU-second | Efficiency metric | measure | measured |
| Cost | Cost per token/request under the config | measure | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Queued | Run defined and scheduled | Config and profile set | Execution starts |
| Running | Measurement in progress | Harness executing | Measurement complete |
| Recorded | Results captured and stored | Run finished | Superseded |
| Superseded | Replaced by a newer run for the same config | Newer run recorded | Archived |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Model Deployment]] | → | Records performance of a deployment config |
| MEASURES | [[Serving Runtime]] | → | Runtime is a benchmark dimension |
| USES | [[Traffic Class]] | → | Run is driven by a characterized workload |
| VALIDATES | [[Model Deployment Specification]] | → | Confirms the spec's benchmark profile |
| RUN_ON | [[GPU Node]] | → | Measured on specific hardware |

## Graph Invariants

- Every performance claim traces to a Benchmark Run or production telemetry.
- Benchmark Runs are `measured` evidence, never roadmap targets.

## Evidence

- Source: roadmap Milestone 0.4 (benchmark harness producing TTFT, throughput, tokens-per-GPU-second, and cost).
- Confidence rationale: the entity structure is `validated` by the roadmap; the numbers a run produces are `measured` by definition. This note deliberately records no specific figures — those live on individual Benchmark Run instances and the evidence layer.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment]]
- [[Traffic Class]]
