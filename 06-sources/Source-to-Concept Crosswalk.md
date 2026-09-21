---
id: idx-crosswalk
type: index
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [crosswalk, source-to-concept crosswalk, source mapping]
related: [hub-root, idx-source-inventory]
source_docs: []
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Maps source documents to the canonical concepts they support."
---

# Source-to-Concept Crosswalk

Maps each source document to the canonical concepts extracted from it. Updated whenever new source material is incorporated (per the Corpus Update Propagation skill).

## Mapping

| Source | Concept | Canonical Note | Layer | Confidence |
|--------|---------|----------------|-------|:----------:|
| Strategic Vision | Model bets (DeepSeek, GLM, Nemotron) | [[DeepSeek V4 Flash]], [[GLM 5.3 Flash]], [[Nemotron 3 Ultra]] | L1 | assumed |
| Strategic Vision | Operating KPIs / scorecard | [[KPI Hierarchy]], [[Model Scorecard]] | L5 | validated |
| Strategic Vision | Cost/efficiency economic loop | [[Unit Economics Model]] | L3 | derived |
| Strategic Vision | Traffic-follows-performance belief | [[OpenRouter Traffic Follows Performance]] | L4 | assumed |
| Strategic Vision + Engineering Roadmap | Two entry paths, sequenced (A private → B public) | [[OpenRouter Integration Plan]], [[OpenRouter Private Model Integration]] | L5/L1 | derived |
| Engineering Roadmap | Canonical model/serving entities | [[Model]], [[Model Deployment]], [[Serving Runtime]] | L1 | validated |
| Engineering Roadmap | GPU fleet / capacity entities | [[GPU Fleet]], [[GPU Node]], [[GPU Cluster]], [[Capacity Pool]], [[Topology]], [[Region]] | L1 | validated |
| Engineering Roadmap | OpenRouter provider integration | [[OpenRouter Provider Integration]] | L1 | validated |
| Engineering Roadmap | Day-zero launch factory (Phase 4) | [[Model Radar]], [[Model Launch Factory]] | L2 | validated |
| Engineering Roadmap | Serving / scheduling workflows | [[Standard Model Deployment]], [[Canary & Rollback]], [[Autoscaling]], [[Admission Control]], [[Request Routing]], [[GPU Reallocation]], [[Closed-Loop Optimization]] | L2 | validated |
| Engineering Roadmap | Headline metrics | [[Tokens per GPU-Second]], [[TTFT]], [[Productive GPU Utilization]], [[Model Launch Lag]], [[Availability]], [[Output Throughput]] | L2 | assumed |
| Engineering Roadmap | Unit-economics formulas | [[Cost per 1M Tokens]], [[Revenue per GPU-Hour]], [[Gross Margin per Model]], [[GPU-Hours per 1M Tokens]] | L2/L3 | assumed |
| Engineering Roadmap | Cost model (Phase 0.3) | [[Cost per GPU-Hour]] | L2 | assumed |
| Engineering Roadmap | Performance optimization program (Phase 3) | [[Quantization Program]], [[FP8 Throughput Factor]], [[Speculative Decoding Acceptance Rate]], [[KV Cache Hit Rate]] | L2 | assumed |
| Engineering Roadmap | Governance policies | [[Admission Control Policy]], [[Performance Regression Gate]], [[Capacity Reservation Policy]], [[Procurement Trigger]] | L2 | validated |
| Engineering Roadmap | Benchmark harness (Phase 0.4) | [[Benchmark Library]], [[Benchmark Run]] | L1/L4 | assumed |
| Engineering Roadmap | Dynamic fleet / capacity (Phase 5) | [[Capacity Pool Model]], [[Demand Forecasting]], [[Fleet Yield Optimization]] | L3 | validated |
| Operator fleet input (2026-09-03) | GPU fleet ground truth (SPOT / staging / dev + AMD order) | [[Fleet Inventory]] | L4 | measured |
| Operator fleet input (2026-09-03) | Fleet GPU types | [[NVIDIA H100]], [[NVIDIA A30]], [[NVIDIA L40S]], [[AMD Instinct]] | L1 | measured |
| Operator fleet input (2026-09-03) | Engine × hardware constraints (ROCm) | [[GPU Type Compatibility Matrix]] | L2 | derived |
| Operator fleet input + analysis | Replica sizing / hardware competitiveness | [[GPUs per Replica]], [[Model Weight Footprint]], [[Fleet Competitiveness]], [[Model Portfolio Capacity]] | L2/L3/L4 | derived |
| RackAI Platform PRD (RMPAI) | Platform vision, multi-engine inference, LLMaaS use case | [[RackAI Platform]], [[Serving Runtime]] | hub/L1 | derived |
| RackAI 1.0.0 Release Notes | Shipped capability (accelerators, AMD, runtimes, control plane) | [[Accelerator Class]], [[Serving Runtime]], [[Model Deployment]], [[RackAI Control Plane]], [[Autoscaling]] | L1/L2 | measured |
| RackAI API Reference | Resource + identity API surface, OpenAI-compatible serving | [[RackAI Control Plane]], [[Model Deployment]], [[Organization]], [[API Key]] | L1 | measured |
| RackAI Console and CLI Docs | Tenancy + Inference/Fine-Tuning/Resources product areas | [[Organization]], [[Model]], [[Model Deployment]], [[Dataset]], [[Fine-Tuning Job]], [[LoRA Adapter]], [[Registry Credential]], [[Fine-Tuning]] | L1/L2 | measured |
| RackAI Deployment and Environments | dev/staging/prod, single-cluster/single-region | [[Environment]], [[GPU Cluster]], [[Region]] | L1 | measured |
| RackAI UI Architecture Extraction | Domain CRDs, entity status enums, implied backend systems | [[Organization]], [[Model]], [[Model Deployment]], [[Serving Runtime]], [[Accelerator Class]], [[Dataset]], [[Fine-Tuning Job]], [[LoRA Adapter]], [[Registry Credential]], [[RackAI Control Plane]] | L1 | derived |
| Identity and Access Control Spec | Auth, org→namespace, RBAC, API keys | [[Identity & Access Control]], [[Organization]], [[API Key]] | L1/L2 | derived |
| Multi-Tenancy and Metering Spec | Metering (planned), billing non-goal | [[Metering]], [[Billing & Payment]], [[Organization]] | L1/L2/L3 | derived |
| Monitoring and Auditability Spec | Platform monitoring (shipped), in-tenant observability + audit (planned) | [[Monitoring & Observability]], [[Audit]] | L2 | derived |
| Accelerator Selection Spec | AcceleratorClass, GPU scheduling/affinity | [[Accelerator Class]], [[Standard Model Deployment]], [[Fleet Inventory]] | L1/L2 | derived |
| OpenRouter provider reference | Provider vs private-model paths, P0/P1 readiness gaps | [[OpenRouter Initiative]], [[OpenRouter Provider Integration]], [[Billing & Payment]], [[Model Catalog Endpoint]] | hub/L1 | derived |
| Erebine bundle + erebine.ai + live API (2026-09-15) | Competitor: zero-lock-in OpenAI-compatible router + MCP workspace-intelligence layer | [[Erebine Competitive Analysis]] | L4 | measured |
| Market research + CEO strategy review (2026-09-21) | Company identity + theory of advantage: Private Enterprise AI Operator (three-battleground frame as internal lens) | [[Three Battlegrounds]] | hub | derived |
| CEO strategy review (2026-09-21) | Partner portfolio / load-bearing bets mapped to the operator stack; Palantir boundary | [[Load-Bearing Bets]] | hub | assumed |
| Web research (2026-09-21): Fireworks, Together, Baseten, Anyscale | Battleground (b) AI-native inference competitors | [[Inference Serving Competitors]] | L4 | derived |
| Web research (2026-09-21): CoreWeave, Lambda | Battleground (a) GPU-neocloud capacity competitors | [[GPU Neocloud Competitors]] | L4 | derived |
| Web research (2026-09-21): Palantir, Cohere, Mistral, Scale AI | Battleground (c) sovereign/governed-AI competitors | [[Sovereign & Governed AI Competitors]] | L4 | derived |
| Dev Plan (2026-09-17) | Portfolio vs product framing; eight-layer stack as a view | [[Enterprise AI Portfolio]], [[Eight-Layer Stack]] | hub/L5 | assumed |
| Dev Plan | Governed harness + agentic entities | [[Governed Harness]], [[Empirical Map]], [[Agent Identity]], [[Across.AI]] | L1 | assumed |
| Dev Plan | Assurance & self-improvement workflows | [[Verification]], [[Loop Planning & Credit Assignment]], [[Self-Improvement Loop]], [[Eval as CI]], [[Perimeter Information-Flow Control]] | L2 | assumed |
| Dev Plan | Operations/governance-plane policies | [[Action Controls]], [[Supply Chain Inventory]], [[Governable Self-Modification]] | L2 | assumed |
| Dev Plan | Cost loop / tokenomics economics | [[Cost per Outcome]], [[AI FinOps]] | L2/L3 | assumed |
| RackAI Organizational Design deck (2026-09-17) | Org/operating-model content (functions, pods, reporting lines, reqs) — **reference-only**, not modeled as canonical concepts (out of graph scope per product decision) | *(none — see [[RackAI Organizational Design]])* | — | assumed |

Extend this table as concepts are extracted into canonical notes.

## See Also

- [[Source Inventory]]
- [[Rack AI Knowledge Base]]
