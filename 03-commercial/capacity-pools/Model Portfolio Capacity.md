---
id: idx-model-portfolio
type: index
status: draft
owner: finops
domain: capacity
aliases: [model portfolio capacity, capacity-aware portfolio, portfolio sequencing, how many models fit]
related: [hub-commercial, asm-fleet-competitiveness, fml-gpus-per-replica, idx-capacity-pools, wf-demand-forecasting, wf-gpu-reallocation]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-09-03
parent: hub-commercial
summary: "Capacity-aware view: how many priority models actually fit on the current fleet, and how to sequence the bets."
---

# Model Portfolio Capacity

## Purpose

The strategy names three simultaneous bets — [[DeepSeek V4 Flash]] + [[GLM 5.3 Flash]] (win now) and [[Nemotron 3 Ultra]] (bet ahead). This note checks that ambition against the **actual fleet** ([[Fleet Inventory]]) and the topology ceiling in [[Fleet Competitiveness]], and proposes a capacity-aware, fit-first portfolio. It feeds [[Demand Forecasting]] and [[GPU Reallocation]].

## The Constraint

Two limits, in priority order:

1. **Topology (binding):** the fleet's H100s are **NVL PCIe** — 2 GPUs NVLink-paired, 4/node, no clustering. So each model must fit within a small coupled group (realistically 2–4 GPUs at FP8). This caps servable model size to roughly the **~27B class** and rules out frontier-class MoE models regardless of count. See [[Fleet Competitiveness]] and [[GPUs per Replica]].
2. **Quantity (secondary):** **16× usable [[NVIDIA H100]]** in SPOT (4 of 20 contracted out) bounds how many fitting models we can run concurrently and how much traffic we can absorb.

| Scenario (fitting ~27B-class models) | On 16 usable H100 | Verdict |
|--------------------------------------|-------------------|---------|
| 1 model, a few replicas | Feasible | Lead here |
| 2 models concurrently | Tight but possible | Stage in |
| 3 models concurrently at scale | Constrained | Sequence, don't parallelize |
| Any frontier-class MoE | Doesn't fit the topology | Not on current hardware |

Staging (4× H100 + 6× [[NVIDIA L40S]]) and dev (A30) are pre-production and carry canary only.

## Implications for the Strategy

- **Fit first, demand second.** Pick a top-demand model that *fits the topology* (~27B class). A model we can serve well beats a bigger one we can only run degraded or not at all. This reframes the win-now bet: **[[GLM 5.3 Flash]] fits; the large DeepSeek MoE fights the topology.** See [[First Bet — GLM 5.3 Flash]].
- **Lead with one flagship, then sequence.** Prove performance + economics on one fitting model before running more — consistent with the roadmap's M2→M3→M4 (serve one right → become a provider → prove repeatability).
- **Add a hardware-fit filter to the [[Model Radar]]** so candidate models are screened against [[GPUs per Replica]] on current topology before they enter the pipeline.
- **AMD MI350P adds capacity, not ceiling.** The 8-way [[AMD Instinct]] pool (~Oct 2026) lets us run *more* fitting models concurrently, but it is PCIe — it does not raise the model-size ceiling. Frontier models and top-10 need **SXM/UBB8**.

## Capacity-Aware Sequencing (proposed)

| Phase | Fleet | Portfolio posture |
|-------|-------|-------------------|
| Now | 16 usable H100 NVL (SPOT) | One fitting flagship ([[GLM 5.3 Flash]]); optimize hard; ramp OpenRouter API conformance |
| Pre-AMD | + tuning (SGLang prefix cache, FP8, batching) | Prove rank/economics on one model; stage a second |
| Post-AMD (~Oct 2026) | + 8-way MI350P (PCIe) | Run multiple fitting models concurrently on vLLM/SGLang |
| Top-tier (future) | SXM clusters / UBB8 | Only then: frontier-class models + top-10 reach |

## Entries

| Item | ID | Role |
|------|----|------|
| [[First Bet — GLM 5.3 Flash]] | idx-first-bet-glm | The recommended first model |
| [[GPUs per Replica]] | fml-gpus-per-replica | Replica sizing / fit test |
| [[Fleet Competitiveness]] | asm-fleet-competitiveness | The topology ceiling |
| [[Capacity Pool Model]] | idx-capacity-pools | Pool taxonomy |
| [[GPU Reallocation]] | wf-gpu-reallocation | Time-sharing between models |
| [[Demand Forecasting]] | wf-demand-forecasting | What to prioritize |

## See Also

- [[Fleet Competitiveness]]
- [[Fleet Inventory]]
- [[Commercial & Capacity Hub]]
