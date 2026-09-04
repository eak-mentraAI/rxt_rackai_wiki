---
id: hub-product
type: hub
status: draft
owner: product
domain: strategy
aliases: [product hub, strategy hub]
related: [hub-root, hub-rackai-platform, hub-openrouter, hub-commercial]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-04
parent: hub-root
summary: "Strategy, model bets, and engineering roadmap for the OpenRouter initiative on the RackAI platform."
---

# Product Hub

Strategy and roadmap for the **OpenRouter inference program** — the first initiative on the [[RackAI Platform]]: the model bets, the operating metrics that drive them, and the phased engineering roadmap. This hub covers the initiative's strategy; the platform it runs on is described in [[RackAI Platform]], and the initiative's integration paths and readiness gaps live in [[OpenRouter Initiative]].

## Model Bets

| Bet | Model | Objective |
|-----|-------|-----------|
| Win now | DeepSeek V4 Flash | Win the benchmark; prove elite performance/efficiency |
| Win now | GLM 5.3 Flash | Capture the growth curve in coding/agentic workloads |
| Bet ahead | Nemotron 3 Ultra | Forward bet on NVIDIA-aligned agentic workloads |

The third slot is intentionally rotatable — Rack AI always maintains one emerging-model bet.

## First Bet & Execution Plan (fit-aware)

Given the fleet's NVL-PCIe topology ceiling (~27B class — see [[Fleet Competitiveness]]), the first production bet is **[[First Bet — GLM 5.3 Flash]]**: the best-ranked open-weight model that also fits what we can serve well. The near-term plan is to prove a modular host-and-deploy pipeline on it — **[[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]]** — then parameterize for the next model.

- Grounded in the [[OpenRouter Leaderboard Snapshot]] and [[Model Portfolio Capacity]].
- The DeepSeek→GLM proof-point swap is recorded as a resolved decision: [[DeepSeek-First vs GLM-First Sequencing]].

## Source Narratives

- [[Rack AI OpenRouter Strategic Vision]] — focused model strategy and KPIs
- [[Rack AI OpenRouter Engineering Roadmap]] — phases 0–6 and milestone sequence

## Headline KPIs

Productive GPU utilization, tokens/GPU-second, TTFT, and model launch lag — with availability, cost/1M tokens, and revenue/GPU-hour as guardrails. Top-five OpenRouter rank is treated as an outcome, not a directly optimized target.

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[Commercial & Capacity Hub]]
