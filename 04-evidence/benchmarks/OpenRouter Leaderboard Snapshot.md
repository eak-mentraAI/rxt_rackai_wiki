---
id: bench-openrouter-leaderboard-2026-09
type: evidence
status: draft
owner: product
domain: strategy
aliases: [openrouter leaderboard, leaderboard snapshot, top models snapshot, openrouter rankings]
related: [hub-evidence, idx-first-bet-glm, ent-glm-5-3-flash, ent-deepseek-v4-flash, ent-openrouter-integration]
source_docs: []
confidence: measured
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Dated snapshot of the OpenRouter overall LLM leaderboard (Month/Week/New) used to select the first model bet."
---

# OpenRouter Leaderboard Snapshot

## What This Is

A dated snapshot of the **overall** OpenRouter LLM leaderboard (all models, ranked by tokens processed), captured from operator screenshots on **2026-09-03**. It is the demand-side evidence behind [[First Bet — GLM 5.3 Flash]]. Ranking data on OpenRouter is published under CC BY 4.0; figures below are transcribed from the operator's screenshots.

> **Confidence:** `measured` as a point-in-time observation of what the operator saw on that date. Rankings shift daily — re-snapshot before major decisions.

## This Month (All Models)

| # | Model | Provider | Tokens | Trend |
|---|-------|----------|-------:|-------|
| 1 | DeepSeek V4 Flash 0731 | deepseek | 47.8T | ↑>999% |
| 2 | Hy3 | tencent | 34.1T | ↑251% |
| 3 | MiMo-V2.5 | xiaomi | 29.1T | ↓13% |
| 4 | GPT-5.6 Luna | openai | 27.8T | ↑772% |
| 5 | Ox Alpha | stealth | 27.2T | new |
| 6 | DeepSeek V4 Flash 0423 | deepseek | 22.8T | ↓12% |
| 7 | Nemotron 3 Ultra (free) | nvidia | 15.8T | ↑52% |
| 8 | **GLM 5.2** | z-ai | 14.7T | ↑7% |
| 9 | **GLM 5.3 Flash** | z-ai | 11.8T | new |
| 10 | DeepSeek V4 Pro 0423 | deepseek | 9.18T | ↓28% |

## This Week (All Models)

| # | Model | Provider | Tokens | Trend |
|---|-------|----------|-------:|-------|
| 1 | GPT-5.6 Luna | openai | 11.6T | ↑183% |
| 2 | **GLM 5.3 Flash** | z-ai | 11.4T | ↑>999% |
| 3 | DeepSeek V4 Flash 0731 | deepseek | 11.4T | ↓8% |
| 4 | Hy4 preview | tencent | 7.99T | new |
| 5 | MiMo-V2.5 | xiaomi | 6.11T | ↓41% |
| 6 | Hy3 | tencent | 5.59T | ↓20% |
| 7 | DeepSeek V4 Flash 0423 | deepseek | 5.18T | ↓7% |
| 8 | MiniMax M3 (free) | minimax | 4.55T | ↑>999% |
| 9 | Nemotron 3 Ultra (free) | nvidia | 4.4T | ↓19% |
| 10 | Gemini 3.7 Flash | google | 2.83T | ↓19% |

## Read-Through for Rack AI

Filtering the board against what we can self-host on **NVL PCIe** topology (~27B-class fit — see [[Fleet Competitiveness]]):

- **Closed / can't self-host:** GPT-5.6 Luna, Gemini 3.7 Flash, Ox Alpha (stealth), MiMo-V2.5.
- **Too large for PCIe pairs:** Nemotron 3 Ultra (550B), Hy3/Hy4 (770B-total MoE), the large DeepSeek V4 Flash/Pro MoEs (footprint fights the topology).
- **Open-weight and fits:** **GLM 5.3 Flash / GLM 5.2 (z-ai)** — on the overall board and, critically, **GLM 5.3 Flash is #2 this week with ↑>999% growth**.

This is why the first bet is GLM 5.3 Flash: it is the best-ranked open-weight model that also fits our topology, and it is the current breakout mover. See [[First Bet — GLM 5.3 Flash]].

## See Also

- [[First Bet — GLM 5.3 Flash]]
- [[Fleet Competitiveness]]
- [[Evidence Hub]]
