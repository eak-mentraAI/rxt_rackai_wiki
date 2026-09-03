---
id: src-engineering-roadmap
type: source
status: validated
owner: platform-eng
domain: strategy
aliases: [engineering roadmap, openrouter roadmap, roadmap]
related: [hub-product, hub-root, src-strategic-vision]
source_docs: []
confidence: validated
last_reviewed: 2026-09-03
parent: hub-product
summary: "Source narrative: phased engineering roadmap for the Rack AI inference operating capability."
---

# Rack AI OpenRouter Engineering Roadmap

## Mission

Build a repeatable inference operating capability that allows Rackspace to:

1. **Launch priority open-weight models within 24 hours median / 72 hours P90**
2. **Operate those models at top-tier throughput and TTFT**
3. **Maintain >99.9% production availability**
4. **Continuously increase productive GPU utilization and tokens/GPU-second**
5. **Dynamically allocate GPU capacity toward the highest-value inference workloads**

Initial model portfolio:

- **DeepSeek V4 Flash** — performance benchmark
- **GLM 5.3 Flash** — growth workload
- **Nemotron 3 Ultra** — strategic forward bet

---

# Roadmap Overview

| Phase | Primary Outcome |
|---|---|
| **0. Establish Ground Truth** | Know exactly what fleet we have and what it costs to produce inference |
| **1. Build the Inference Baseline** | One production-grade model running through a standardized serving stack |
| **2. OpenRouter Production Launch** | Rackspace becomes a measurable production provider |
| **3. Build the Performance Lab** | Systematic model-specific optimization drives top-tier performance |
| **4. Industrialize Model Launches** | New models move from weights to production through a repeatable factory |
| **5. Optimize Fleet Economics** | Capacity automatically moves toward the best-performing workloads |
| **6. Operate as an Inference Network** | Closed-loop optimization across models, clusters, demand, and economics |

---

# Phase 0 — Establish Ground Truth

## Objective

Create an authoritative understanding of the GPU fleet, its topology, available capacity, and inference economics before making model-placement decisions.

## Milestone 0.1 — GPU Fleet Inventory

Create a machine-readable inventory containing:

- GPU type and generation
- GPU count
- GPU memory
- Host configuration
- CPU/RAM
- NVLink/NVSwitch topology
- Network fabric
- Storage configuration
- Datacenter / geography
- Power envelope
- Cluster ownership
- Currently committed capacity
- Available capacity
- Maintenance state

## Milestone 0.2 — GPU Telemetry

Deploy common telemetry across all candidate inference clusters.

Minimum visibility:

- GPU compute utilization
- HBM utilization
- Memory bandwidth
- Power consumption
- Thermals
- GPU errors
- PCIe/NVLink utilization
- Network throughput
- Node utilization
- GPU-hours available vs consumed

## Milestone 0.3 — Cost Model

Establish internal cost per GPU-hour for every relevant hardware configuration.

Include:

- Power
- Datacenter allocation
- Hardware depreciation / lease economics
- Networking
- Storage
- Software/licensing
- Operational overhead

This becomes the foundation for calculating:

- **GPU-hours / 1M tokens**
- **Cost / 1M tokens**
- **Revenue / GPU-hour**

## Milestone 0.4 — Initial Model Benchmark Harness

Build a repeatable benchmark suite capable of testing:

- TTFT
- Output tokens/sec
- Tokens/sec/GPU
- Prefill throughput
- Concurrency scaling
- Latency under load
- Context-length behavior
- Tool calling
- Structured output
- Memory consumption
- Throughput at different batch sizes

Benchmark DeepSeek, GLM, and Nemotron against candidate GPU configurations.

## Phase Exit Criteria

Rackspace can answer:

> For model X, on hardware Y, in cluster Z, how many tokens can we produce and what does one million tokens cost us?

---

# Phase 1 — Build the Standard Inference Runtime

## Objective

Create a standardized production serving architecture rather than allowing every model to become its own deployment.

## Milestone 1.1 — Runtime Selection

Establish the initial supported inference engines.

Likely architecture:

### Primary Engines
- vLLM
- SGLang

### Specialized Engines Where Justified
- TensorRT-LLM
- NVIDIA Dynamo or equivalent
- Model-specific optimized runtimes

Avoid forcing every model into one runtime.

Create an abstraction allowing Rack AI to select the best serving engine by model.

## Milestone 1.2 — Standard Model Deployment Contract

Every model deployment must declare:

- Model identity/version
- Weight source
- Runtime
- Quantization
- Supported context
- GPU requirement
- Parallelism configuration
- API capabilities
- Routing policy
- Scaling policy
- Health checks
- Benchmark profile

This becomes the internal **Model Deployment Specification**.

## Milestone 1.3 — OpenAI-Compatible Serving Layer

Expose a standardized Rack AI API supporting:

- `/models`
- `/chat/completions`
- Streaming
- Tool calling
- Structured outputs
- Reasoning parameters
- Multimodal inputs where appropriate
- Usage/token reporting
- Standardized error handling

The serving layer must isolate consumers from the underlying inference engine.

## Milestone 1.4 — Model Artifact Pipeline

Standardize:

**Weights → validation → storage → deployment**

Capabilities:

- Model artifact registry
- Weight integrity verification
- Versioning
- Caching
- Distributed weight delivery
- Rollback
- Previous-version retention

Large model weights should not need to be repeatedly downloaded externally for each deployment.

## Milestone 1.5 — Basic Scheduling

Implement model-aware placement based on:

- GPU type
- Memory requirements
- Topology
- Available capacity
- Geography

Initially placement may still be operator-assisted.

The important step is making the decision explicit and reproducible.

## Phase Exit Criteria

DeepSeek V4 Flash is running on Rack AI through the standard serving API with:

- Repeatable deployment
- Production telemetry
- Benchmark results
- Reliable rollback

---

# Phase 2 — Production OpenRouter Integration

## Objective

Put Rackspace into the real competitive environment as quickly as possible.

Do not wait for the entire platform to be complete.

## Milestone 2.1 — Provider Integration

Implement everything required to operate through OpenRouter:

- Endpoint integration
- Model metadata
- Pricing
- Context/capability metadata
- Token usage reporting
- Authentication
- Request accounting
- Streaming behavior
- Health/status handling

## Milestone 2.2 — Production Observability

Create dashboards by:

**Model → deployment → cluster → GPU → request**

Track at minimum:

- Request volume
- Token volume
- TTFT
- Output throughput
- P50/P95/P99 latency
- Error rates
- Timeouts
- Queue depth
- GPU utilization
- HBM utilization
- Tokens/GPU-second
- Availability

## Milestone 2.3 — Synthetic Production Testing

Run continuous synthetic requests against Rackspace endpoints that mirror:

- Short chat
- Long-context prompts
- Coding
- Tool calls
- Structured output
- Concurrent traffic
- High-output responses

Performance problems should be detected before OpenRouter traffic exposes them.

## Milestone 2.4 — DeepSeek Production Launch

Launch DeepSeek as the first flagship workload.

Begin with controlled capacity.

Measure Rackspace directly against competing OpenRouter providers.

Establish baseline:

- Throughput rank
- TTFT rank
- Uptime
- Cost/token
- Utilization

## Milestone 2.5 — GLM Production Launch

Repeat the process with GLM.

The purpose is to prove the infrastructure is genuinely reusable rather than a DeepSeek-specific deployment.

## Phase Exit Criteria

Rackspace has:

- At least two models live
- Measurable OpenRouter traffic
- Production GPU utilization data
- Direct competitor benchmarks
- Production unit economics

---

# Phase 3 — Build the Performance Engineering System

## Objective

Move from "model hosting" to deliberate inference-performance engineering.

## Milestone 3.1 — Performance Lab

Create a dedicated environment where engineering can safely test:

- Runtime versions
- Kernels
- Quantization
- Batching strategies
- Parallelism
- Memory strategies
- Cache policies
- Networking
- Model configuration

Performance testing should not happen directly in production.

## Milestone 3.2 — Model-Specific Performance Profiles

Create a continuously maintained optimization profile for each priority model.

Example:

### DeepSeek Performance Profile

Document:

- Preferred hardware
- Minimum topology
- Inference engine/version
- Tensor parallelism
- Expert parallelism
- Batch configuration
- KV-cache configuration
- Quantization
- Speculative decoding
- Prefill configuration
- Decode configuration
- Target concurrency

Repeat for GLM and Nemotron.

## Milestone 3.3 — Workload Characterization

Analyze actual OpenRouter traffic.

Characterize:

- Average input length
- Average output length
- Concurrency
- Context distribution
- Prompt repetition
- Tool-call frequency
- Cacheability
- Burst behavior

Optimize for **the workload actually arriving**, not generic benchmark prompts.

## Milestone 3.4 — Continuous Batching Optimization

Tune:

- Maximum active sequences
- Batch composition
- Admission control
- Queue strategy
- Prefill scheduling
- Decode scheduling

Measure effect on both:

- **Tokens/sec/GPU**
- **TTFT**

so throughput improvements do not create unacceptable user latency.

## Milestone 3.5 — KV / Prefix Cache Optimization

Implement and evaluate:

- Local KV caching
- Distributed caching where appropriate
- Prefix caching
- Cache-aware request routing
- Cache hit-rate telemetry

Expose:

- **Cache hit rate**
- **GPU work avoided**

## Milestone 3.6 — Quantization Program

Evaluate model-specific:

- BF16
- FP8
- FP4 where viable
- INT8/other supported approaches

Benchmark every configuration against:

**Quality × throughput × GPU memory × cost/token**

Quantization becomes a controlled engineering decision, not simply a deployment switch.

## Milestone 3.7 — Parallelism Optimization

Evaluate:

- Tensor parallelism
- Pipeline parallelism
- Expert parallelism
- Data parallelism

for each model architecture.

For MoE models, topology-aware expert placement should become an explicit optimization area.

## Milestone 3.8 — Prefill / Decode Optimization

Where workload economics justify it, evaluate separation of:

- **Prefill workers**
- **Decode workers**

Allow hardware and capacity to be optimized differently for each phase.

## Milestone 3.9 — Speculative Decoding

Introduce speculative decoding where model/runtime compatibility allows it.

Measure:

- Acceptance rate
- Throughput gain
- Added memory cost
- Impact on TTFT
- Quality consistency

## Milestone 3.10 — Network and Topology Optimization

Validate placement assumptions against:

- NVLink
- NVSwitch
- RDMA
- InfiniBand / Ethernet fabric
- NUMA boundaries

Prevent the scheduler from placing performance-sensitive deployments on structurally inferior topology.

## Milestone 3.11 — Competitive Benchmark Pipeline

Continuously benchmark Rackspace against OpenRouter competitors.

For every priority model maintain:

| Metric | Rackspace | Provider A | Provider B | Provider C |
|---|---:|---:|---:|---:|
| TTFT | | | | |
| Output t/s | | | | |
| Availability | | | | |
| Price | | | | |

Performance engineering should always know **the gap to the competitive frontier**.

## Phase Exit Criteria

For each priority model:

- Performance bottlenecks are identified
- Optimization configuration is codified
- Competitive performance is continuously measured
- Changes can be promoted through an automated performance gate

---

# Phase 4 — Build the Day-Zero Model Factory

## Objective

Turn model launches from bespoke projects into a repeatable pipeline.

## Milestone 4.1 — Model Radar

Create an operational process that continuously tracks:

- Hugging Face
- GitHub
- NVIDIA
- Model labs
- OpenRouter
- Research announcements
- Ecosystem partners

Models move through:

**Watch → Prepare → Launch Candidate → Production**

## Milestone 4.2 — Architecture Compatibility Matrix

Maintain support profiles for common model architectures.

Examples:

- Dense transformers
- MoE
- Multimodal
- MLA
- Linear/hybrid attention
- Reasoning models

Track:

- Runtime compatibility
- Kernel readiness
- GPU requirements
- Likely serving configuration

New models using known architectures should require significantly less engineering effort.

## Milestone 4.3 — Automated Model Intake

Given a new model artifact, automatically extract:

- Architecture
- Parameter count
- Active parameter count
- Context length
- Tokenizer
- Precision
- Multimodal capabilities
- Tool support
- Memory requirements

Produce a preliminary deployment recommendation.

## Milestone 4.4 — Automated Functional Validation

Run standardized tests for:

- Loading
- Basic generation
- Streaming
- Tokenization
- Long context
- Tools
- JSON/structured output
- Reasoning controls
- Multimodal features
- Concurrency

Failures immediately identify which capability blocks production.

## Milestone 4.5 — Automated Hardware Fit Testing

Run candidate configurations against available hardware.

Determine:

- Minimum GPU count
- Preferred GPU type
- Memory headroom
- Topology requirement
- Initial parallelism profile

## Milestone 4.6 — Automated Benchmark Stage

Generate baseline measurements:

- TTFT
- Tokens/sec
- Tokens/sec/GPU
- Memory use
- Concurrency scaling
- Cost/1M tokens

Compare automatically with established performance thresholds.

## Milestone 4.7 — Canary Deployment

Automate:

**Internal → canary → limited external → production**

with rollback based on:

- Errors
- Latency
- Correctness
- GPU failures
- Availability

## Milestone 4.8 — OpenRouter Publication Pipeline

Once a model passes gates, automatically prepare:

- Endpoint
- Metadata
- Pricing
- Supported parameters
- Context
- Routing information

Goal:

> Model publishing should be the final step of a pipeline rather than an independent engineering project.

## Phase Exit Criteria

A previously unseen but supported model architecture can move from available weights to production in:

**<24 hours median**

without assembling a new cross-functional war room.

---

# Phase 5 — Dynamic Fleet and Capacity Management

## Objective

Move from static model hosting to economic orchestration of GPU capacity.

## Milestone 5.1 — Model-Level Capacity Pools

Create logical pools such as:

- DeepSeek
- GLM
- Nemotron
- Launch/canary
- Reserve
- Unallocated/spot

Capacity allocation becomes software-controlled.

## Milestone 5.2 — Demand Forecasting

Forecast demand using:

- OpenRouter request volume
- Token growth
- Hourly patterns
- Queue depth
- Utilization
- Model popularity
- Scheduled enterprise demand

Forecast at:

**Model × cluster × time window**

## Milestone 5.3 — Autoscaling

Automatically add/remove serving replicas or capacity while respecting:

- Model load time
- Weight transfer time
- Topology
- GPU availability
- Minimum warm capacity
- Latency SLO

## Milestone 5.4 — Admission Control

Introduce protection against overload.

Control:

- Maximum concurrency
- Context-heavy requests
- Queue length
- Burst traffic
- Large-output jobs

Objective:

> Protect TTFT and availability instead of letting saturated GPUs collapse endpoint performance.

## Milestone 5.5 — GPU Reallocation

Allow GPUs to move among model pools based on:

- Demand
- Utilization
- Queue depth
- Revenue/GPU-hour
- Marginal contribution
- Strategic priority

Initially recommendations can require human approval.

Later they become automatic.

## Milestone 5.6 — Warm Pool

Maintain capacity capable of being rapidly reassigned to:

- Traffic spikes
- Newly released models
- Failing deployments

Avoid having 100% of the fleet permanently committed.

## Milestone 5.7 — Capacity Yield Optimization

Introduce an optimization function approximately equivalent to:

> **Maximize productive GPU utilization and gross contribution while maintaining performance SLOs and strategic capacity reservations.**

The scheduler should increasingly understand:

**Utilization + performance + economics**

rather than simply:

**GPU available / unavailable**

## Phase Exit Criteria

Rackspace can move capacity between priority models in response to demand without manual infrastructure reconstruction.

---

# Phase 6 — Closed-Loop Inference Optimization

## Objective

Create the enduring Rack AI differentiator: a system that learns how to operate models better over time.

## Milestone 6.1 — Automated Configuration Experimentation

Continuously test:

- Batch sizes
- Cache settings
- Runtime releases
- Quantization
- Parallelism
- Kernel versions

against production-shaped workloads.

## Milestone 6.2 — Performance Regression Gates

No runtime or configuration change reaches production if it materially worsens:

- TTFT
- Tokens/sec/GPU
- Error rate
- Quality
- Cost/token

Performance becomes a CI/CD gate.

## Milestone 6.3 — Automated Configuration Promotion

When experiments demonstrate statistically meaningful improvements:

**Lab → Canary → Production**

without manually rebuilding the deployment.

## Milestone 6.4 — Hardware-Aware Routing

Route workloads to the hardware configuration that creates the best outcome.

For example:

- **Short latency-sensitive request → Pool A**
- **Large-context prefill → Pool B**
- **High-throughput agent workload → Pool C**

The customer still sees one model endpoint.

## Milestone 6.5 — Economic Routing

Factor real-time economics into scheduling:

- Incremental power
- GPU scarcity
- Token economics
- Utilization
- OpenRouter pricing
- Enterprise commitments

This creates a GPU **yield-management layer**.

## Milestone 6.6 — Operational Intelligence

Rack AI should ultimately be capable of answering:

> Why did DeepSeek tokens/GPU-second fall 11% yesterday?

or:

> Where should the next eight H200s be allocated?

using the telemetry and operating model underneath the inference fleet.

## Phase Exit Criteria

Inference performance, capacity placement, and economics operate through a measurable closed-loop system rather than manual operations.

---

# Cross-Cutting Engineering Workstreams

These should operate across every phase.

## A. Platform / Control Plane

Own:

- Deployment orchestration
- Model registry
- Capacity management
- Routing
- API
- Lifecycle management

## B. Inference Performance Engineering

Own:

- Runtime optimization
- Kernels
- Quantization
- Caching
- Parallelism
- Topology
- Benchmark performance

Primary mandate:

**Improve TTFT + tokens/sec/GPU**

## C. Model Enablement

Own:

- Model radar
- Model intake
- Architecture compatibility
- Functional testing
- New-model launches

Primary KPI:

**Model launch lag**

## D. GPU / Infrastructure Engineering

Own:

- GPU clusters
- Networking
- Storage
- Topology
- Drivers
- Firmware
- Hardware health

## E. SRE / Reliability

Own:

- Availability
- Observability
- Incident response
- Canarying
- Rollback
- Capacity protection

## F. FinOps / Economics

Own visibility into:

- Cost/token
- GPU-hour economics
- Price
- Revenue/GPU-hour
- Contribution margin
- Fleet opportunity cost

---

# Executive Milestone Sequence

### M1 — Know the Fleet
Inventory, telemetry, cost model, and benchmark harness complete.

### M2 — Serve One Model Correctly
DeepSeek running through the standard Rack AI inference stack.

### M3 — Become an OpenRouter Provider
Production DeepSeek traffic flowing and competitive measurements visible.

### M4 — Prove Repeatability
GLM deployed through the same platform without rebuilding the stack.

### M5 — Build Performance Advantage
Model-specific optimization closes the gap against leading OpenRouter providers.

### M6 — Prove Model Velocity
Nemotron or another priority model moves through the new model factory in <72 hours.

### M7 — Reach <24-Hour Launches
Known architectures become effectively automated model deployments.

### M8 — Optimize Fleet Utilization
Capacity dynamically moves between models based on real demand.

### M9 — Optimize Economics
Scheduler incorporates tokens/GPU-second, utilization, and revenue/GPU-hour.

### M10 — Close the Loop
Performance and capacity optimization become continuous automated processes.

---

# KPI Hierarchy

The roadmap should ultimately be governed by four headline engineering KPIs.

## 1. Productive GPU Utilization

**Productive inference GPU-hours / available GPU-hours**

Answers:

> Are we actually monetizing the fleet?

## 2. Tokens per GPU-Second

Measures infrastructure efficiency.

Answers:

> Are we becoming better at producing inference from the hardware we own?

## 3. TTFT

Track:

- P50
- P95

Answers:

> Is our inference responsive enough to compete for latency-sensitive traffic?

## 4. Model Launch Lag

**Usable model release → Rackspace production**

Answers:

> Can we capture demand while a new model is still accelerating?

### Supporting Guardrails

- >99.9% availability
- Error rate
- Queueing delay
- Capability coverage
- Cost / 1M tokens
- Revenue / GPU-hour
- Gross margin / model

---

# What Success Looks Like

The end state is not simply that Rackspace can host DeepSeek, GLM, or Nemotron.

It is an engineering system capable of repeatedly doing this:

**Identify promising model**  
↓  
**Understand architecture**  
↓  
**Select optimal hardware/runtime**  
↓  
**Deploy within hours**  
↓  
**Benchmark against competitors**  
↓  
**Optimize tokens/GPU-second and TTFT**  
↓  
**Expose production capacity to OpenRouter**  
↓  
**Scale with real demand**  
↓  
**Reallocate GPUs based on utilization and economics**  
↓  
**Continuously improve**

At that point, **top-five OpenRouter performance is not a project milestone. It is the external consequence of the operating system Rackspace has built.**

> **Implementation note:** Phases 1–4 should overlap heavily. The Performance Lab and Model Factory should begin forming while DeepSeek is being productionized, rather than waiting for a “platform complete” milestone.