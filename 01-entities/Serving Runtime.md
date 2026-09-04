---
id: ent-serving-runtime
type: entity
status: draft
owner: performance-eng
domain: performance
aliases: [serving runtime, inference engine, inference runtime, serving engine]
related: [ent-model-deployment, ent-model-deployment-spec, ent-gpu-node, ent-benchmark-run, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: the inference engine, version, and config that executes a Model."
---

# Serving Runtime

## Definition

A **Serving Runtime** is the inference engine — plus its version and configuration — that actually executes a [[Model]] and turns requests into tokens. It is the software layer a [[Model Deployment]] runs on. Different engines make different tradeoffs across concurrency, prefix reuse, peak throughput, and hardware portability, so Rack AI selects the best-fit engine per model rather than standardizing on one. Each Model Deployment runs on exactly one Serving Runtime configuration.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → Serving Runtime → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Engine | Inference engine family (vLLM, SGLang, TensorRT-LLM, NVIDIA Dynamo) | enum | validated |
| Engine version | Pinned engine version | string | measured |
| Serving flags | Batching, attention, caching, and parallelism configuration | struct | measured |
| Attention/batching features | e.g., PagedAttention, continuous batching, RadixAttention, prefix caching | set | validated |
| Hardware stack | CUDA and/or ROCm — bounds which GPU types the engine can serve | enum | validated |
| Hardware portability | Whether the engine runs on non-NVIDIA (ROCm) hardware | bool | validated |
| Compile step | Whether the engine requires an ahead-of-time compile | bool | validated |
| Disaggregation support | Support for disaggregated prefill/decode serving | bool | derived |

## Supported Engines

| Engine | Strengths | Best-fit workload | Hardware stack |
|--------|-----------|-------------------|----------------|
| vLLM | PagedAttention, continuous batching, prefix caching | High concurrency, general default | CUDA **and ROCm** (runs on [[AMD Instinct]]) |
| SGLang | RadixAttention (shared-prefix reuse) | Shared-prefix workloads: chat, RAG, agents | CUDA **and ROCm** (runs on [[AMD Instinct]]) |
| TensorRT-LLM | Peak throughput on NVIDIA (~10–20% higher at high concurrency) | NVIDIA-only peak throughput | **CUDA only** — no ROCm equivalent |
| NVIDIA Dynamo (or equivalent) | Disaggregated serving (separate prefill/decode) | Large-scale disaggregated deployments | NVIDIA-oriented; ROCm path via equivalent frameworks |

**Hardware constraint:** engine choice is bounded by GPU type. On [[AMD Instinct]] (ROCm) only vLLM and SGLang are available; TensorRT-LLM is CUDA-only. See the [[GPU Type Compatibility Matrix]] for the full engine × GPU-type mapping.

## Shipped Runtimes (RackAI 1.0.0)

On the platform today, the runtime is declared by a [[Model Class]], whose `Runtime` field takes one of these shipped values (`measured`, 1.0.0):

| Runtime value | Engine | Notes |
|---------------|--------|-------|
| `vllm` | vLLM | General default |
| `nim` | NVIDIA NIM | NVIDIA inference microservice |
| `optimized-nim-vllm` | Optimized NIM (vLLM) | Tuned NIM path, image pinned by digest |
| `aim` | AMD AIM | AMD inference runtime (shipped 1.0.0); supports LoRA |

The roadmap's broader engine set (SGLang, TensorRT-LLM, NVIDIA Dynamo) is **planned** (`assumed`) — not among the shipped `Runtime` enum values above. A [[Model Deployment]] `INSTANTIATES` a Model Class, which is how a runtime binds to a deployment.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Evaluated | Engine/version under performance evaluation | Candidate for a model | Selected or rejected |
| Selected | Chosen as best-fit for a model deployment | Wins per-model evaluation | Runtime pinned to a deployment |
| Active | Executing a live Model Deployment | Deployment provisioned | Deprecated or replaced |
| Deprecated | Superseded by a newer engine/version | Better engine/version qualified | Removed |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| RUNS | [[Model Deployment]] | ← | A deployment runs on exactly one runtime config (invariant) |
| REQUIRED_BY | [[Model Deployment Specification]] | ← | Declared by the deployment spec |
| RUNS_ON | [[GPU Node]] | → | Executes on GPU hardware |
| MEASURED_BY | [[Benchmark Run]] | ← | Runtime config is a benchmark dimension |
| SELECTED_FOR | [[Model]] | → | Best engine chosen per model |

## Evidence

- Source: roadmap Milestone 1.1 (engine selection per model; vLLM, SGLang, TensorRT-LLM, and disaggregated serving via NVIDIA Dynamo or equivalent).
- Confidence rationale: engine families and their characteristic features are `validated` by the roadmap; specific versions, flags, and throughput deltas are `measured` per [[Benchmark Run]] rather than asserted here.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment]]
- [[Benchmark Run]]
