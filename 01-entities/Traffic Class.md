---
id: ent-traffic-class
type: entity
status: draft
owner: performance-eng
domain: performance
aliases: [traffic class, workload class, request class, workload profile]
related: [ent-model, ent-model-deployment, ent-benchmark-run, ent-openrouter-integration, hub-entities, hub-inference-serving, hub-ai-harness, ent-market-demand, met-ttft, wf-request-routing, pol-admission-control, coeff-kv-cache-hit-rate, wf-admission-control, bench-agentx-standard, pol-benchmark-evidence-chain, prd-empirical-map-routing, spec-empirical-map-routing]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-08
parent: hub-entities
summary: "Canonical entity: a characterized class of request workload used to drive routing and benchmarking."
---

# Traffic Class

## Definition

A **Traffic Class** is a characterized class of request workload — a named shape of traffic with distinct token, latency, and concurrency characteristics. Examples include short chat, long-context, coding, tool calls, structured output, high-output, and concurrent/burst. Traffic Classes let Rack AI benchmark against representative workloads and route each shape to the deployment configuration that serves it best.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A Traffic Class characterizes the market demand that flows into a Model — it is how demand shape is made explicit for benchmarking and routing.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Class name | Named workload shape | enum | validated |
| Prompt length profile | Typical input token distribution | struct | assumed |
| Output length profile | Typical output token distribution | struct | assumed |
| Prefix-sharing | Degree of shared prefixes (chat/RAG/agents) | enum | derived |
| Latency sensitivity | TTFT/interactive sensitivity | enum | derived |
| Concurrency/burst | Concurrency and burstiness characteristics | struct | assumed |
| Capability usage | Tool calls, structured output, streaming usage | set | assumed |

## Class Examples

| Class | Shape | Notes |
|-------|-------|-------|
| Short chat | Small prompt, short output, interactive | Latency-sensitive |
| Long-context | Large prompt, moderate output | Context-bound |
| Coding | Structured code in/out | Often prefix-shared |
| Tool calls | Function/tool invocation | Capability-dependent |
| Structured output | Schema-constrained generation | Capability-dependent |
| High-output | Long generations | Throughput-bound |
| Concurrent / burst | Spiky, high concurrency | Stresses batching/scaling |

### Standard benchmark profiles

The [[Benchmark Evidence Chain]] defines four standard profiles built from the classes above. Each qualification marks each profile required, conditional, or not applicable (input/output distributions, arrival processes, and SLO thresholds not yet ratified):

| Profile | Built from | Primary read |
|---------|------------|--------------|
| Interactive | Short chat | [[TTFT]] + [[TPOT]] p95/p99, [[Goodput]] |
| Throughput | High-output | [[Tokens per GPU-Second]], [[Energy per Token]] |
| Long Context / RAG | Long-context | TTFT vs. context length, HBM use |
| Agentic | Coding + tool calls (multi-turn) | [[AgentX Benchmark Standard]] |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Proposed | Candidate class identified | Observed distinct workload shape | Characterized |
| Characterized | Profile measured and documented | Sufficient samples | Used for routing/benchmarking |
| Active | Driving routing and benchmarks | Profile validated | Retired or merged |
| Retired | No longer distinct or relevant | Merged/obsoleted | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CHARACTERIZES | [[Model]] | → | Real workload shape observed per Model |
| USED_BY | [[Benchmark Run]] | ← | Drives representative benchmark workloads (canonical: USES ←) |
| USED_BY | [[Benchmark Evidence Chain]] | ← | Standard benchmark profiles |
| ROUTED_BY | [[OpenRouter Provider Integration]] | ← | Observed shapes inform routing |
| CONSTRAINS | [[Model Deployment]] | → | Deployment config tuned to the class |
| USES | [[Market Demand]] | ← | Demand is segmented by Traffic Class (canonical form of CHARACTERIZES) |
| MEASURES | [[TTFT]] | ← | Latency tracked per class |
| DEPENDS_ON | [[Request Routing]] | ← | Classification input |
| CONSTRAINS | [[Admission Control Policy]] | ← | Shaping differentiated by class |

## Evidence

- Source: roadmap Milestone 2.3 / 3.3 (workload characterization and traffic-aware routing).
- Confidence rationale: the concept of characterized traffic classes is `validated` by the roadmap; the per-class profiles are `assumed` until workload characterization exists (roadmap *Workload characterization*, not started; no characterization is produced today, 2026-10-10). [[Empirical Map & Evidence-Informed Routing PRD]] proposes how they are measured.

## See Also

- [[Entity Ontology Hub]]
- [[Model]]
- [[Benchmark Run]]
- [[Empirical Map & Evidence-Informed Routing PRD]] — workload characterization (draft)

