---
id: idx-decision-glm-first
type: index
status: draft
owner: product
domain: strategy
aliases: [deepseek vs glm first, sequencing decision, glm-first decision, proof point decision]
related: [hub-evidence, idx-open-questions, idx-first-bet-glm, idx-phase1-execution-glm, asm-fleet-competitiveness, ent-glm-5-3-flash, ent-deepseek-v4-flash]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: derived
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Resolved: roadmap names DeepSeek first, but topology fit makes GLM 5.3 Flash the first model."
---

# DeepSeek-First vs GLM-First Sequencing

## The Conflict

Two parts of the corpus disagree on which model to launch first. Per the Conflict Visibility rule, both sides are preserved here rather than smoothed over.

| Side | Says | Where |
|------|------|-------|
| Source roadmap/strategy | **DeepSeek** is the M2/M3 flagship proof point | [[Rack AI OpenRouter Engineering Roadmap]] (M2, M3), [[Rack AI OpenRouter Strategic Vision]] |
| Fit-aware analysis | **GLM 5.3 Flash** should be first; DeepSeek's large MoE fights our topology | [[First Bet — GLM 5.3 Flash]], [[Fleet Competitiveness]] |

## Why It Exists

The source documents were written before the fleet's **NVL-PCIe topology ceiling** (~27B class — see [[Fleet Competitiveness]]) was captured. DeepSeek V4 Flash is a large MoE whose replica needs far more tightly-coupled GPUs than pair-bridged PCIe can provide, so it cannot be served competitively on the current fleet. GLM 5.3 Flash fits and is a top-ranked open-weight model ([[OpenRouter Leaderboard Snapshot]]).

## Resolution

**Decision: GLM 5.3 Flash is the first proof point** (fit-first). The roadmap's *sequence and pipeline* (M1→M2→M3→M4) are kept; only the *proof-point model* changes. See [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]].

- This is a **sequencing correction, not a rejection** of DeepSeek. DeepSeek remains a strategic target and becomes viable if/when (a) a confirmed Flash variant fits the topology, or (b) SXM/UBB8 capacity lands.
- The source narratives are left unchanged (read-only); this note is the reconciling layer.

## Status

| Status | Result | Date |
|--------|--------|------|
| resolved (pending validation) | GLM-first adopted; DeepSeek deferred to fitting-variant or SXM/UBB8 | 2026-09-03 |

Confidence `derived` — the decision follows from the topology constraint and leaderboard evidence; it upgrades to `validated` once GLM is live and measured.

## See Also

- [[First Bet — GLM 5.3 Flash]]
- [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]]
- [[Fleet Competitiveness]]
- [[Open Questions]]
