---
id: coeff-model-weight-footprint
type: coefficient
status: draft
owner: model-enablement
domain: capacity
aliases: [model weight footprint, weight bytes, model memory footprint]
related: [hub-operations, fml-gpus-per-replica, ent-deepseek-v4-flash, ent-model]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Per-model in-memory weight footprint (bytes) at a given precision — input to GPUs-per-replica."
---

# Model Weight Footprint

## Definition

The in-memory size of a model's weights at a given precision: `params × bytes_per_param`. For MoE models the **total** parameter count applies (all experts resident), even though only a subset activate per token. It is the dominant term in [[GPUs per Replica]] and therefore in replica cost.

## Value

Per-model, per-precision. Values below are illustrative reference points, not confirmed for the specific Flash/Ultra variants (params unconfirmed — see [[Open Questions]]).

| Model | Total params (ref) | FP8 (~1 B/param) | BF16 (~2 B/param) | Confidence | As Of |
|-------|-------------------:|-----------------:|------------------:|:----------:|-------|
| [[DeepSeek V4 Flash]] | ~671B (V3 reference) | ~671 GB | ~1.34 TB | assumed | 2026-09-03 |
| [[GLM 5.3 Flash]] | TBD | TBD | TBD | assumed | 2026-09-03 |
| [[Nemotron 3 Ultra]] | TBD | TBD | TBD | assumed | 2026-09-03 |

bytes/param: BF16 = 2, FP8 = 1, FP4 ≈ 0.5.

## Evidence

- Reference point: DeepSeek-V3 = 671B total params ([arXiv:2412.19437](https://arxiv.org/abs/2412.19437)). Actual V4 Flash / GLM 5.3 Flash / Nemotron 3 Ultra counts unconfirmed. Content was rephrased for compliance with licensing restrictions.
- Exit criterion to upgrade confidence: confirmed parameter counts from each model's release + a measured loaded-memory figure from a deployment.

## Used By

| Formula | ID |
|---------|----|
| [[GPUs per Replica]] | fml-gpus-per-replica |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | Illustrative (671B ref) | Created to support replica sizing | — → assumed |

## See Also

- [[GPUs per Replica]]
- [[Operations Hub]]
