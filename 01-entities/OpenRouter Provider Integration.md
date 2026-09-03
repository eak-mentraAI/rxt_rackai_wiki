---
id: ent-openrouter-integration
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [openrouter provider integration, openrouter integration, provider integration, openrouter provider]
related: [ent-model, ent-model-deployment, ent-traffic-class, ent-benchmark-run, hub-entities]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: the integration exposing Rack AI Model endpoints on OpenRouter."
---

# OpenRouter Provider Integration

## Definition

The **OpenRouter Provider Integration** is the integration that exposes Rack AI's [[Model]] endpoints on OpenRouter as a provider. It publishes each model's endpoint, metadata, pricing, and capability surface; reports token usage and request accounting; supports streaming; authenticates requests; and surfaces health/status. Critically, it presents models — never GPU hardware — to OpenRouter consumers.

OpenRouter routes requests among providers of the *same* model based on latency (TTFT), throughput (output tokens/sec), uptime, price, and quantization. Well-performing providers receive proportionally more traffic. Model selection (which model) and provider selection (which provider of that model) are two independent routing decisions — Rack AI competes on the second.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

The integration sits at the top of the chain, publishing Models to the market. It is the boundary that hides everything below the Model from consumers.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Endpoint | Published provider endpoint per model | ref | validated |
| Model metadata | Model identity and version exposed to OpenRouter | struct | validated |
| Pricing | Per-token price published to OpenRouter | struct | validated |
| Context/capability metadata | Context window and capability flags advertised | set | validated |
| Token usage reporting | Reported prompt/completion token usage | struct | validated |
| Auth | Authentication for the provider integration | ref | validated |
| Request accounting | Per-request accounting and reconciliation | struct | validated |
| Streaming | Streaming response support | bool | validated |
| Health/status | Health and status signals surfaced to OpenRouter | ref | validated |

## Routing Signals (Provider Selection)

| Signal | Description | Notes |
|--------|-------------|-------|
| Latency (TTFT) | Time to first token | Lower is favored |
| Throughput | Output tokens per second | Higher is favored |
| Uptime | Provider availability | Higher is favored |
| Price | Per-token price | Lower is favored |
| Quantization | Serving precision advertised | Considered in selection |

Model selection and provider selection are independent decisions. Content was rephrased for compliance with licensing restrictions.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Applied | Provider application submitted | Model ready to publish | Approved |
| Published | Model endpoint live on OpenRouter | Approval + health green | Traffic flowing |
| Serving | Receiving routed production traffic | Meets routing signals | Deprioritized or withdrawn |
| Withdrawn | Endpoint removed from OpenRouter | Model retired or paused | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| PUBLISHES | [[Model]] | → | Exposes Model endpoints to consumers |
| ROUTES_TO | [[Model Deployment]] | → | Routes external traffic to deployments |
| REPORTS | [[Benchmark Run]] | → | Production signals reconcile with benchmark evidence |
| CHARACTERIZES | [[Traffic Class]] | → | Observed request shapes feed traffic classification |

## Graph Invariants

- OpenRouter consumers see Model endpoints, never GPU hardware.
- Provider selection is independent of model selection.

## Evidence

- Source: roadmap Milestone 2.1 (OpenRouter provider integration) and strategy narrative (competing on provider selection). Provider-selection mechanics per OpenRouter documentation: [provider application](https://openrouter.ai/providers/apply) and [provider selection routing](https://openrouter.ai/docs/guides/routing/provider-selection).
- Confidence rationale: the integration surface and routing signals are `validated` by the roadmap and OpenRouter's own documentation; live traffic shares are `measured` from production telemetry. Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Entity Ontology Hub]]
- [[Model]]
- [[Model Deployment]]
