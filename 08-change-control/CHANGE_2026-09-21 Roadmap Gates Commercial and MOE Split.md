---
id: chg-2026-09-21-roadmap-gates-commercial
type: change
status: reviewed
owner: product
domain: strategy
aliases: [roadmap gates change, commercial gate change, moe split change, proof gates]
related: [hub-roadmap, hub-minimum-operable-estate, hub-ai-operations-product, pol-change-packet, chg-2026-09-21-roadmap-four-proofs]
source_docs: ["CEO strategy review 2026-09-21"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-wiki
summary: "Change packet: added proofs-as-gates, commercial gates, paired north-star metrics, and the MOE-0/MOE-1 split."
---

# Change Packet — Roadmap Gates, Commercial Gate & MOE Split (2026-09-21)

## 1. Source of Change

- **Trigger:** CEO strategy review — "stop restructuring; force specificity." Refinements to sharpen exits, prevent waterfall interpretation, add the commercial/willingness-to-pay dimension, and prevent a friendly estate masquerading as the identity proof.
- **Date:** 2026-09-21
- **Requester/Owner:** CEO review → product

## 2. Affected Concept(s)

- **Primary:** [[RackAI Roadmap]] (`hub-roadmap`) — tightened (no structural rewrite).
- **Propagated:** [[Minimum Operable Estate]] (`hub-minimum-operable-estate`) — MOE-0/MOE-1 split; P-002 updated in the roadmap queue.
- **Layer:** L5 (planning hubs). **Change type:** refinement + meaning-preserving edits + propagation.

## 3. The Changes Applied

1. **Proofs are gates, not waterfall phases** — prominent callout; later-proof work starts early (compliance, MOE/identity/tenancy architecture, harness v1 design, design-partner selection), but a proof cannot be *claimed* until its exit is met.
2. **Proof 1 exit tightened** — "accurately measure … on the infrastructure we operate" (dropped "runs best on"); comparative "where/how to run" moved to Proof 2. Cleaner Observe/Decide separation.
3. **Proof 2 must beat a baseline** — exit now requires a decision informed by accumulated evidence that improves an agreed KPI vs. a static/default baseline ("built an Empirical Map" ≠ "flywheel works").
4. **Commercial gate alongside every proof** — quantify economics (P1) → quantify customer improvement (P2) → delegate **and pay** (P3) → repeat **profitably** (P4). Technical delegation + willingness to pay proven together.
5. **North star paired (anti-Goodhart)** — leading: workloads under management; strategic: customer **estates** under management; scale: workloads/FTE; economic: contribution margin/estate.
6. **Killer metric added** — % of operating decisions informed by **cross-workload** empirical evidence; plus an illustrative (explicitly non-measured) executive dashboard.
7. **MOE split into MOE-0 (operator rehearsal, does not validate the thesis) and MOE-1 (identity proof, external + paid)** — propagated to the MOE note and P-002; P-002 gains the four executive asks (MOE-0 named+date, MOE-1 profile+window, proof gates, commercial gates).

## 4. Confidence Assessment

- Roadmap remains `derived`; MOE remains `assumed`.
- Metrics and the dashboard explicitly flagged `assumed`/illustrative — **not measured**; no performance number asserted as real.
- No source narratives edited; truth hierarchy intact.

## 5. Impact Scan

| Category | Impacted Items |
|----------|---------------|
| Hub pages | [[RackAI Roadmap]] (edits), [[Minimum Operable Estate]] (MOE-0/MOE-1 split + summary) |
| Proposed changes | P-002 updated in place (MOE-0/MOE-1, commercial gate, four asks); P-001 unchanged |
| Crosswalk | No new row — same concepts, deeper; no new canonical objects |
| Formulas / Coefficients / Metrics / Scorecards | none modified — operator-metric instrumentation remains a tracked open question ([[KPI Hierarchy]], [[Model Scorecard]]) |

## 6. Edges Affected

- No new nodes. Reinforced edges: `hub-roadmap` ↔ `hub-minimum-operable-estate`; roadmap → `hub-ai-operations-product` (commercial gate + MOE-1 paid-workload row).

## 7. Prior Batch Recorded Here (paper-trail completeness)

The immediately prior batch shipped without its own packet; recorded now:
- **Added `hub-ai-operations-product`** ([[AI Operations Product]]) — operating model / SLOs / incident / FDE motion as a first-class vertical workstream; wired to roadmap (workstream row + related), root nav, crosswalk. Closed roadmap Open Gap #3.
- **Added P-002** to the roadmap Proposed-Changes queue (now further refined by this packet).

## 8. Open Questions Created / Carried

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| MOE-0: named friendly estate + target date | [[Minimum Operable Estate]], [[RackAI Roadmap]] | High |
| MOE-1: named external design-partner profile + target window | [[Minimum Operable Estate]], [[Load-Bearing Bets]] | High |
| Measurable pass/fail proof gates for Observe/Decide/Control/Operate | [[RackAI Roadmap]] | High |
| Commercial-gate evidence: delegation + willingness to pay at attractive economics | [[Commercial & Capacity Hub]], [[AI Operations Product]] | High |
| Instrument the paired north-star + killer metric | [[KPI Hierarchy]] | High |
| AI Operations Product staffing/ownership; supply-abstraction interface spec | [[RackAI Roadmap]] Open Gaps | Medium |

## 9. Contradictions Surfaced / Resolved

- **Resolved:** waterfall misread risk (proofs-as-gates callout); Observe/Decide overlap (Proof 1 exit tightened); "friendly estate = proven operator" risk (MOE-0 vs MOE-1); "built a map = flywheel works" risk (baseline requirement); workload-count Goodhart risk (paired north star).
- **Surfaced:** the economic claim (customers will pay) was previously unproven by any proof — now carried explicitly as the commercial gate.

## See Also

- [[CHANGE_PACKET]]
- [[chg-2026-09-21-roadmap-four-proofs|Prior packet — four-proofs restructure]]
- [[RackAI Roadmap]] · [[Minimum Operable Estate]] · [[AI Operations Product]]
