---
id: hub-product
type: hub
status: draft
owner: product
domain: strategy
aliases: [product hub, strategy hub]
related: [hub-root, hub-commercial]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Navigation hub for strategy, model bets, and the engineering roadmap."
---

# Product Hub

Strategy and roadmap for Rack AI on OpenRouter: the model bets, the operating metrics that drive them, and the phased engineering roadmap.

## Model Bets

| Bet | Model | Objective |
|-----|-------|-----------|
| Win now | DeepSeek V4 Flash | Win the benchmark; prove elite performance/efficiency |
| Win now | GLM 5.3 Flash | Capture the growth curve in coding/agentic workloads |
| Bet ahead | Nemotron 3 Ultra | Forward bet on NVIDIA-aligned agentic workloads |

The third slot is intentionally rotatable — Rack AI always maintains one emerging-model bet.

## First Bet (fit-aware)

Given the fleet's NVL-PCIe topology ceiling (~27B class — see [[Fleet Competitiveness]]), the recommended first production bet is **[[First Bet — GLM 5.3 Flash]]**: the best-ranked open-weight model that also fits what we can serve well. Grounded in the [[OpenRouter Leaderboard Snapshot]] and [[Model Portfolio Capacity]].

## Source Narratives

- [[Rack AI OpenRouter Strategic Vision]] — focused model strategy and KPIs
- [[Rack AI OpenRouter Engineering Roadmap]] — phases 0–6 and milestone sequence

## Headline KPIs

Productive GPU utilization, tokens/GPU-second, TTFT, and model launch lag — with availability, cost/1M tokens, and revenue/GPU-hour as guardrails. Top-five OpenRouter rank is treated as an outcome, not a directly optimized target.

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[Commercial & Capacity Hub]]
