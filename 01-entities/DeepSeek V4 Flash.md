---
id: ent-deepseek-v4-flash
type: entity
status: draft
owner: model-enablement
domain: model-enablement
aliases: [deepseek v4 flash, deepseek v4, deepseek flash]
related: [ent-model, ent-model-deployment, ent-serving-runtime, ent-capacity-pool, ent-benchmark-run, hub-entities, ent-market-demand, idx-scorecard-deepseek, val-deepseek-h200-fp8, wf-model-launch-factory, coeff-model-weight-footprint, fml-gpus-per-replica, asm-fleet-competitiveness, bench-openrouter-leaderboard-2026-09]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-entities
summary: "Priority Model instance: DeepSeek V4 Flash, the win-now / benchmark bet (MoE + MLA)."
---

# DeepSeek V4 Flash

## Definition

**DeepSeek V4 Flash** is a priority [[Model]] instance — Rack AI's "win now / benchmark" bet. It is a Mixture-of-Experts (MoE) model using Multi-head Latent Attention (MLA), which compresses the KV cache into a latent vector. Serving it well requires expert parallelism, and its multi-node serving bottleneck is expert load imbalance combined with all-to-all communication between experts. It is an instance of the [[Model]] entity and inherits that note's canonical definition.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

DeepSeek V4 Flash is a specific Model; its deployments follow the standard chain below it.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Strategic role | Win now — benchmark | enum | validated |
| Architecture | MoE with Multi-head Latent Attention (MLA) | enum | validated |
| KV cache handling | MLA compresses the KV cache into a latent vector | mechanism | validated |
| Parallelism need | Expert parallelism required for MoE | enum | validated |
| Multi-node bottleneck | Expert load imbalance + all-to-all communication | mechanism | validated |
| Total parameters | V4 Flash count not yet confirmed here | int | assumed |
| Active parameters | V4 Flash count not yet confirmed here | int | assumed |
| Context length | Not yet confirmed here | int | assumed |

> **Open question:** Specific V4 Flash parameter counts and context length are not yet confirmed and are marked `assumed`. Reference point from the DeepSeek-V3 Technical Report: 671B total / 37B active parameters. Confirm V4 Flash figures against primary release notes before promoting confidence.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Prepare | Readiness work for the model bet | Strategically prioritized | Weights usable |
| Launch Candidate | Moving through the launch factory | Usable weights + intake pass | Production gate passed |
| Production | Serving live OpenRouter traffic | Canary passed | Retired or superseded |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| INSTANCE_OF | [[Model]] | → | Priority Model instance (canonical: BELONGS_TO →) |
| SERVED_BY | [[Model Deployment]] | → | One or more deployments (canonical: SERVES ←) |
| REQUIRES | [[Serving Runtime]] | → | Expert-parallel-capable engine (e.g., disaggregated serving) (canonical: DEPENDS_ON →) |
| ASSIGNED_TO | [[Capacity Pool]] | → | Dedicated per-model DeepSeek pool (canonical: ALLOCATES ←) |
| VALIDATED_BY | [[Benchmark Run]] | → | Performance evidence per config (canonical: VALIDATES ←) |
| ROUTES_TO | [[Market Demand]] | ← | OpenRouter pool 47.8T tokens/month (measured snapshot); long-context/coding split assumed |
| MEASURES | [[DeepSeek V4 Flash Scorecard]] | ← | Operating scorecard (all rows assumed; no run yet) |
| VALIDATES | [[Validate DeepSeek H100 FP8]] | ← | Open: TTFT and tokens/GPU-s at FP8 on H100 |
| MEASURES | [[DeepSeek H100 FP8 Benchmark]] | ← | Planned run, not executed |
| DEPENDS_ON | [[Model Launch Factory]] | → | Launch Candidate state runs through the factory |
| MEASURES | [[Model Weight Footprint]] | ← | ~671 GB at FP8 (V3 reference, assumed) |
| DEPENDS_ON | [[GPUs per Replica]] | → | ~10 H100 for weights at FP8: exceeds the NVL-PCIe coupled group (illustrative) |
| CONSTRAINS | [[Fleet Competitiveness]] | ← | Large MoE fights the topology ceiling |

## Evidence

- Source: strategy narrative (win-now benchmark bet) and roadmap (priority model enablement). Architecture references: [DeepSeek-V3 Technical Report (arXiv:2412.19437)](https://arxiv.org/abs/2412.19437) and [DeepSeek-V2 (arXiv:2405.04434)](https://arxiv.org/abs/2405.04434).
- Confidence rationale: the strategic role and the MoE/MLA architecture and its serving bottleneck are `validated`; specific V4 Flash parameter counts and context length are `assumed` pending confirmation. Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Entity Ontology Hub]]
- [[Model]]
- [[Serving Runtime]]
