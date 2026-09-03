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

Extend this table as concepts are extracted into canonical notes.

## See Also

- [[Source Inventory]]
- [[Rack AI Knowledge Base]]
