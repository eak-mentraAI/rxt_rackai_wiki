---
id: chg-2026-09-24-gpu-capacity-demand-rationale
type: change
status: draft
owner: product
domain: capacity
aliases: [gpu capacity demand change, capacity demand rationale change packet]
related: [pol-fitness-checklist, pol-change-packet, idx-gpu-capacity-demand-rationale, wf-demand-forecasting, idx-assumption-register]
source_docs: ["reference/RackAI - GPU Capacity.xlsx"]
confidence: validated
last_reviewed: 2026-09-24
parent: hub-wiki
summary: "Change packet: new GPU Capacity Demand Rationale note and three supporting assumption notes."
---

# Change Packet — GPU Capacity Demand Rationale

## 1. Source of Change

- **Trigger:** New source document + business decision (capacity proposal from Jovan/Paavan requiring demand derivation before upstream submission to Amine/Guy)
- **Source reference:** `reference/RackAI - GPU Capacity.xlsx` (Paavan's prod GPU count proposal)
- **Date:** 2026-09-24
- **Requester/Owner:** Edward Kerr (product)

## 2. Affected Concepts

- **Primary concept:** GPU Capacity Demand Rationale (`idx-gpu-capacity-demand-rationale`) — **new object**, Layer 3 Commercial/Capacity
- **Supporting new objects:** Three assumption notes (Layer 4 Evidence)
- **Updated objects:** Demand Forecasting, Assumption Register, Commercial & Capacity Hub (link additions only)

## 3. Impact Scan

| Category | Impacted Items |
|----------|----------------|
| Entities | None — no entity definitions changed |
| Workflows | [[Demand Forecasting]] — added `related` link and `See Also` entry |
| Formulas | [[GPUs per Replica]], [[Tokens per GPU-Second Formula]] — referenced (read-only); no changes needed |
| Coefficients | [[Cost per GPU-Hour]] — referenced as a known gap; no change |
| Metrics / KPIs | [[Productive GPU Utilization]] — referenced in `asm-openrouter-initial-share`; no change |
| Benchmark Runs | None — no benchmark run created; all numbers remain `assumed` |
| Assumptions | Three new assumptions added (see below) |
| Validations | None |
| Events | None |
| Policies | None |
| Model Scorecards | None |
| Hub pages | [[Commercial & Capacity Hub]] — one row added to Capacity & Allocation table |
| Indexes | [[Assumption Register]] — three new entries, now wikilinked |
| Source-to-Concept Crosswalk | No crosswalk file exists in corpus; N/A |

## 4. Propagation Sequence Executed

1. Created `03-commercial/forecasting/GPU Capacity Demand Rationale.md` (primary note)
2. Updated `03-commercial/forecasting/Demand Forecasting.md` — added `related` ID and `See Also` link
3. Created three standalone assumption notes in `04-evidence/assumptions/`
4. Updated `04-evidence/assumptions/Assumption Register.md` — three new wikilinked entries
5. Updated `00-hub/Commercial & Capacity Hub.md` — one row in Capacity & Allocation table
6. This change packet

## 5. Objects Changed

**Added:**

| Object | ID | Type | Layer |
|--------|----|------|-------|
| GPU Capacity Demand Rationale | idx-gpu-capacity-demand-rationale | index | L3 Commercial |
| OpenRouter Initial Market Share | asm-openrouter-initial-share | assumption | L4 Evidence |
| Traffic Peak Multiplier | asm-traffic-peak-multiplier | assumption | L4 Evidence |
| Gemma Replica Sizing | asm-gemma-replica-sizing | assumption | L4 Evidence |

**Modified (links only):**

| Object | Change |
|--------|--------|
| Demand Forecasting | Added `related: idx-gpu-capacity-demand-rationale`; added `See Also` link |
| Assumption Register | Three new wikilinked rows |
| Commercial & Capacity Hub | One row added to Capacity & Allocation table |

## 6. Edges Added

| From | Relationship | To |
|------|-------------|-----|
| idx-gpu-capacity-demand-rationale | DEPENDS_ON | wf-demand-forecasting |
| idx-gpu-capacity-demand-rationale | DEPENDS_ON | bench-openrouter-leaderboard-2026-09 |
| idx-gpu-capacity-demand-rationale | CONSUMES | fml-gpus-per-replica |
| idx-gpu-capacity-demand-rationale | CONSUMES | fml-tokens-per-gpu-second |
| idx-gpu-capacity-demand-rationale | CONSUMES | idx-unit-economics |
| idx-gpu-capacity-demand-rationale | SUPPORTS | asm-openrouter-initial-share |
| idx-gpu-capacity-demand-rationale | SUPPORTS | asm-traffic-peak-multiplier |
| idx-gpu-capacity-demand-rationale | SUPPORTS | asm-gemma-replica-sizing |
| wf-demand-forecasting | GENERATES | idx-gpu-capacity-demand-rationale |
| hub-commercial | CONTAINS | idx-gpu-capacity-demand-rationale |

## 7. Confidence Assessment

- All new notes: `assumed` — correct and intentional. No production traffic exists; all numbers are derived from leaderboard observation, topology math, and analytical reasoning.
- No existing note had its confidence state changed.
- Weakest link: `coeff-cost-per-gpu-hour` (TBD/assumed) — caps the economics chain. This note does not compute economics, so the cap does not apply directly here.
- Confidence propagation: valid. The new note's `assumed` state is consistent with its upstream dependencies (leaderboard snapshot is `measured` as a point-in-time observation; GPUs per Replica formula inputs are `assumed`).

## 8. Open Questions Created

| # | Question | Affected Docs | Priority |
|---|----------|---------------|----------|
| OQ-1 | What is RackAI's actual peak-to-average traffic ratio? (3× is assumed) | Traffic Peak Multiplier, GPU Capacity Demand Rationale | High — resolves at Phase 1 telemetry |
| OQ-2 | What is RackAI's actual market share of the GLM provider pool at launch? | OpenRouter Initial Market Share, GPU Capacity Demand Rationale | High — resolves at Phase 3 launch |
| OQ-3 | Does Gemma 4 31B at BF16 + 262k context actually require 2× H100? | Gemma Replica Sizing, GPU Capacity Demand Rationale | Medium — resolves at M2 benchmark |
| OQ-4 | Which GLM Flash hardware option (MI350P / H100 / L40S) is selected for prod? | GPU Capacity Demand Rationale, RackAI - GPU Capacity.xlsx | High — must resolve before capacity proposal goes upstream |

## 9. Fitness Checklist Results

| Check | Status | Notes |
|-------|:------:|-------|
| S-01 No duplicate concepts | ✅ Pass | New note is net-new; no existing concept covers prod capacity demand derivation |
| S-02 No orphan nodes | ✅ Pass | All four new notes have inbound links (Register + Hub + parent note) |
| S-03 No broken backlinks | ✅ Pass | All wikilinks verified to resolve against existing .md files |
| S-04 No layer violations | ✅ Pass | Rationale note in 03-commercial/; assumptions in 04-evidence/ |
| S-05 Owner assigned | ✅ Pass | All notes have owner field |
| S-06 Source traceability | ✅ Pass | `reference/RackAI - GPU Capacity.xlsx` declared in source_docs |
| S-07 Confidence declared | ✅ Pass | All notes: `assumed` |
| S-08 Relationships explicit | ✅ Pass | Impacts tables present in all four new notes |
| S-09 Formulas resolve | ✅ Pass | All formula wikilinks verified |
| S-10 Coefficients resolve | ✅ Pass | No new coefficients introduced |
| S-11 Assumptions linked | ✅ Pass | All three new assumptions have standalone notes with exit criteria |
| S-12 Validations linked | ✅ Pass | No new validations introduced |
| S-13 Benchmarks resolve | ✅ Pass | 750 tok/GPU-sec labelled illustrative, traced to [[Tokens per GPU-Second Formula]] |
| S-14 Stable IDs preserved | ✅ Pass | No existing IDs changed |
| S-15 Aliases preserved | ✅ Pass | No existing aliases removed |
| S-16 Summary ≤ 120 chars | ✅ Pass | All summaries verified at ≤ 116 chars |
| C-06 Confidence propagation | ✅ Pass | No downstream note exceeds weakest upstream |
| C-08 No hidden conflicts | ✅ Pass | CoreWeave reference limitation surfaced explicitly in the note |
| C-09 Targets vs. results | ✅ Pass | All numbers labelled `assumed` / illustrative |

**Overall: ✅ Pass — no blocking issues.**

## See Also

- [[FITNESS_CHECKLIST]]
- [[GPU Capacity Demand Rationale]]
- [[Assumption Register]]
