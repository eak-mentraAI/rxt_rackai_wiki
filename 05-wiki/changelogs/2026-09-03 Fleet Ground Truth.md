---
id: chg-2026-09-03-fleet-ground-truth
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [fleet ground truth, 2026-09-03 fleet, h200 correction]
related: [hub-wiki, idx-fleet-inventory, ent-gpu-fleet]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Incorporated operator-reported GPU fleet ground truth and corrected the H200 placeholder to the real fleet."
---

# 2026-09-03 — Fleet Ground Truth

## Trigger

Operator provided the actual GPU fleet composition (Phase-0 ground truth): two environments plus incoming capacity. The prior corpus used **H200** as an illustrative GPU — the fleet has **no H200s** — so this change records the real hardware and corrects the placeholder.

## Fleet (as reported)

- **SPOT:** 20× H100, 40× A30 (production-eligible spot)
- **RackAI — staging:** 4× H100, 6× L40S ("i40's", pending confirmation) — canary
- **RackAI — dev:** some A30 (count TBD)
- **Incoming (~Oct 2026):** AMD Instinct — class/qty TBD (ROCm)

## Objects Changed

- Added:
  - [[Fleet Inventory]] (+ `fleet-inventory.csv`) — Phase-0 machine-readable inventory.
  - GPU-type entities: [[NVIDIA H100]], [[NVIDIA A30]], [[NVIDIA L40S]], [[AMD Instinct]].
  - [[GPU Type Compatibility Matrix]] — engine × precision × GPU-type support, incl. the ROCm constraint.
- Changed:
  - [[GPU Node]], [[GPU Fleet]], [[Serving Runtime]] — H200 example replaced with H100; fleet composition + ROCm engine constraint added.
  - Renamed `DeepSeek H200 FP8 Benchmark` → [[DeepSeek H100 FP8 Benchmark]]; `H200 Sufficient for Priority Models` → [[Available Hardware Sufficient for Priority Models]]; `Validate DeepSeek H200 FP8` → [[Validate DeepSeek H100 FP8]]. Content retargeted to H100 + AMD Instinct.
  - [[Benchmark Library]] entries retargeted to H100 / AMD Instinct / L40S (no H200; A30 has no FP8).
  - Hubs, [[Entity Index]], [[Source Inventory]], [[Source-to-Concept Crosswalk]] updated.

## Edges

- Added: [[GPU Fleet]] INCLUDES_TYPE → each GPU type; [[AMD Instinct]] CONSTRAINS → [[Serving Runtime]] (ROCm: vLLM/SGLang only); GPU types REALIZED_BY [[GPU Node]].

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| [[Fleet Inventory]] + GPU-type notes (H100/A30/L40S) | — | measured | Operator-reported fleet snapshot + vendor specs |
| [[AMD Instinct]] | — | assumed | Order exists but class/qty/ETA unconfirmed |
| [[Available Hardware Sufficient for Priority Models]] | assumed | assumed | Corrected from H200 to real fleet; still unmeasured |

## Stable Identity Note

The IDs `bench-deepseek-h200-fp8`, `asm-h200-sufficient`, and `val-deepseek-h200-fp8` were retained (they are the example IDs defined in the [[Rack AI Knowledge Base Architecture]] ID conventions). Only titles/content were corrected; old "h200" terms are preserved as aliases.

## Open Questions Created

Fleet-fit for large MoE on H100; AMD order specifics; ROCm CUDA-only-path penalty; L40S-vs-L40 confirmation; dev A30 count; A30 suitability. See [[Open Questions]].

## Fitness / Consistency Result

- Structural checks: **Pass** — frontmatter lint clean; all wikilinks resolve; no duplicate IDs.
- Consistency pass: **Pass** — abstraction chain intact; no H200 references remain in canonical layers except explicit historical-ID notes; targets vs. measured distinct.

## See Also

- [[Fleet Inventory]]
- [[Wiki Hub]]
- [[2026-09-03 Corpus Buildout]]
