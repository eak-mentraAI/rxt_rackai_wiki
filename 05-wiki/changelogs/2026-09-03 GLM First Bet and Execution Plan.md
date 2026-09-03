---
id: chg-2026-09-03-glm-first-bet
type: change
status: draft
owner: product
domain: strategy
aliases: [glm first bet change, execution plan change, leaderboard change]
related: [hub-wiki, idx-first-bet-glm, idx-phase1-execution-glm, idx-decision-glm-first, bench-openrouter-leaderboard-2026-09]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Recorded the OpenRouter leaderboard, selected GLM 5.3 Flash as the first bet, and added a fit-first Phase-1 execution plan."
---

# 2026-09-03 — GLM First Bet & Execution Plan

## Trigger

Operator provided (a) corrected fleet ground truth — 16 usable H100 **NVL PCIe**, MI350P incoming — and (b) OpenRouter leaderboard screenshots. Together these establish the topology ceiling and the demand picture needed to pick a first model and frame the near-term roadmap.

## Objects Changed

- Added:
  - [[OpenRouter Leaderboard Snapshot]] — dated overall board (Month/Week/New).
  - [[First Bet — GLM 5.3 Flash]] — the recommended first model.
  - [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]] — modular pipeline plan mapped to roadmap M1–M4.
  - [[DeepSeek-First vs GLM-First Sequencing]] — resolved-conflict decision note.
- Changed:
  - [[Fleet Competitiveness]] reframed around interconnect topology (PCIe vs SXM/UBB8); ~27B ceiling; dropped SPOT-uptime claim; added OpenRouter API-conformance ranking risk.
  - [[AMD Instinct]] corrected to MI350P, 8-way PCIe pool (adds capacity, not model-size ceiling).
  - [[Model Portfolio Capacity]], [[GPUs per Replica]], [[Available Hardware Sufficient for Priority Models]], [[Topology]] updated to the topology-first framing.
  - [[Fleet Inventory]] + CSV: 16 usable H100 (4 contracted), NVL PCIe, MI350P.
  - [[Product Hub]], [[Open Questions]], [[Source Inventory]] updated.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| [[OpenRouter Leaderboard Snapshot]] | — | measured | Point-in-time observation from operator screenshots |
| [[First Bet — GLM 5.3 Flash]] | — | derived | Recommendation from leaderboard + topology, not yet a live result |
| [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]] | — | derived | Planned, upgrades when GLM is live and measured |
| [[DeepSeek-First vs GLM-First Sequencing]] | — | derived | Decision recorded; validates after GLM launch |

## Conflict Surfaced & Resolved

Roadmap says DeepSeek-first; fit analysis says GLM-first. Resolved GLM-first (fit) while keeping the roadmap's M1–M4 sequence and pipeline. Source narratives left unchanged; reconciliation lives in the new notes.

## Fitness / Consistency Result

- Structural checks: **Pass** — frontmatter lint clean; all wikilinks resolve; no duplicate IDs.
- Consistency pass: **Pass** — conflict surfaced not smoothed (C-08); targets vs. recommendation distinct (C-09); confidence honest (all new strategy notes `derived`/`measured`, nothing falsely `validated`).

## See Also

- [[First Bet — GLM 5.3 Flash]]
- [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]]
- [[Wiki Hub]]
