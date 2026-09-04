---
id: gls-index
type: glossary
status: draft
owner: knowledge-graph-steward
domain: platform
aliases: [glossary, terms, definitions, inference glossary]
related: [hub-wiki, idx-metrics, idx-entities]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Canonical one-paragraph definitions of inference-serving terms, each pointing to its canonical note where one exists."
---

# Glossary

Canonical, brief definitions of the recurring terms in the RackAI platform corpus. Where a term has a canonical L1/L2 note, the definition points to it as the single source of truth; the glossary summarizes rather than redefines.

## RackAI

Rackspace's Kubernetes-native AI inference and fine-tuning platform — the product this knowledge base models. **RackAI is the canonical name; `RMPAI` (the platform PRD) and `RackAI Aurora` (a technical spec) are aliases of the same product**, not separate systems. The OpenRouter inference program is one initiative built on RackAI.

- **Canonical Note:** [[RackAI Platform]]

## Organization

The top-level tenant workspace in RackAI; every resource (models, deployments, datasets, jobs, adapters, credentials) is scoped to one, and it maps to a Kubernetes namespace. Rackspace provisions organizations via the identity provider — there is no self-service signup.

- **Canonical Note:** [[Organization]]

## Model Class

A template binding a base model to a serving runtime and its engine configuration (the shipped `Runtime` values are `vllm`, `nim`, `optimized-nim-vllm`, `aim`). A model deployment instantiates a Model Class.

- **Canonical Note:** [[Model Class]]

## Accelerator Class

The cluster-scoped abstraction by which a deployment selects GPU hardware (vendor, node affinity, sizing), backed by automated inventory reporting allocatable vs used capacity. Shipped in RackAI 1.0.0.

- **Canonical Note:** [[Accelerator Class]]

## LoRA / QLoRA

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that trains a small adapter instead of the full model; QLoRA runs LoRA over a quantized copy of the base model to cut memory. In RackAI a fine-tuning job produces a [[LoRA Adapter]] that is applied on top of a base model deployment.

- **Canonical Note:** [[LoRA Adapter]]

## Metering vs Billing

**Metering** captures usage (tokens/requests) per tenant. **Billing** prices that usage and moves money (invoices/top-ups/payout). RackAI has planned metering but **no billing** — pricing/billing logic is an explicit non-goal of the metering spec. The distinction matters because becoming an OpenRouter public provider requires billing.

- **Canonical Notes:** [[Metering]], [[Billing & Payment]]

## OpenRouter Private Model

The Path A OpenRouter integration: registering a RackAI tenant deployment into OpenRouter as a restricted, non-public model, distinct from operating a public provider (Path B).

- **Canonical Note:** [[OpenRouter Private Model Integration]]

## TTFT

Time To First Token — the elapsed time between a request arriving and the first output token being returned to the user. Measured as a latency distribution (P50, P95, P99) and tracked separately from output-token throughput because the two require different optimization strategies.

- **Canonical Note:** [[TTFT]]

## Tokens per GPU-Second

The count of tokens produced per second of GPU time — the platform's primary internal efficiency measure. Rising tokens/GPU-second lowers cost per token and improves price competitiveness.

- **Canonical Note:** [[Tokens per GPU-Second]]

## MoE (Mixture of Experts)

A model architecture where each token is routed to a small subset of specialized sub-networks ("experts") rather than the full parameter set, so only a fraction of parameters are active per token. This raises capacity without a proportional compute cost and makes topology-aware expert placement an explicit serving optimization.

## MLA (Multi-head Latent Attention)

An attention variant that compresses the key/value representation into a lower-dimensional latent space, cutting KV-cache memory and bandwidth pressure while preserving model quality. Notable for reducing the memory cost of long-context serving.

## Expert Parallelism

A parallelism strategy for MoE models that distributes the experts across multiple GPUs so their compute and memory can scale out. Effective expert parallelism depends on the interconnect topology between the participating GPUs.

## KV Cache / Prefix Cache

The KV cache stores the key and value tensors already computed for a sequence so tokens are not recomputed during decoding. A prefix cache extends this by reusing the cached state of a shared prompt prefix across requests, avoiding repeated prefill work when prompts overlap.

## Continuous Batching

A serving scheduling technique that admits and retires requests at the token-step level rather than as fixed static batches, keeping the GPU busy by continuously filling freed slots. It improves throughput but must be tuned so it does not degrade TTFT.

## Speculative Decoding

A decoding acceleration technique in which a smaller draft model proposes several tokens that the target model verifies in parallel, accepting the correct ones. It can raise throughput at some added memory cost, with gains dependent on the draft acceptance rate.

## Quantization (FP8/FP4/INT8)

Representing model weights and/or activations at reduced numeric precision (e.g. FP8, FP4, INT8) instead of BF16 to cut GPU memory use and increase throughput. It is a controlled engineering decision benchmarked against quality, throughput, memory, and cost per token — not merely a deployment switch.

## Prefill vs Decode

The two phases of inference. Prefill processes the entire input prompt in parallel to build initial state and is compute-bound; decode generates output tokens one at a time and is memory-bandwidth-bound. Their differing profiles justify tuning — and sometimes separating — hardware and scheduling for each.

## Disaggregated Serving

An architecture that separates the prefill and decode phases onto distinct worker pools so each can be sized and optimized independently. Applied where workload economics justify the added routing complexity.

## Capacity Pool

A software-controlled logical grouping of GPU capacity (for example per model, plus launch/canary, reserve, and spot pools) from which deployments draw. Making capacity allocation software-controlled is what allows GPUs to move toward the highest-value workloads.

- **Canonical Note:** [[Capacity Pool]]

## Model Launch Lag

The elapsed time from a model's publicly usable weights being available to a production Rack AI endpoint serving it. Targeted at under 24-hour median and under 72-hour P90, with day-zero readiness for models identified ahead of launch.

- **Canonical Note:** [[Model Launch Lag]]

## OpenRouter Provider

Rack AI's integration as a serving provider on the OpenRouter marketplace, covering endpoint integration, model and pricing metadata, token-usage reporting, authentication, and health/status handling. OpenRouter is both a distribution channel for otherwise idle GPU capacity and a public proving ground for inference performance.

- **Canonical Note:** [[OpenRouter Provider Integration]]

## Warm Pool

Capacity kept ready-to-serve so it can be rapidly reassigned to traffic spikes, newly released models, or failing deployments, rather than committing the entire fleet permanently. It trades a small standing cost for launch and burst responsiveness.

## See Also

- [[Wiki Hub]]
- [[Metric Index]]
- [[Entity Index]]
