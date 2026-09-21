---
id: chg-2026-09-21-roadmap-four-proofs
type: change
status: reviewed
owner: product
domain: strategy
aliases: [four proofs restructure, roadmap restructure change, moe change]
related: [hub-roadmap, hub-minimum-operable-estate, hub-battlegrounds, pol-change-packet, chg-2026-09-21-canonical-roadmap]
source_docs: ["CEO strategy review 2026-09-21", "00-hub/Three Battlegrounds.md"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-wiki
summary: "Change packet: restructured the roadmap into four proofs, added the Minimum Operable Estate, and the maturity ladder."
---

# Change Packet — Roadmap Four-Proofs Restructure + MOE (2026-09-21)

## 1. Source of Change

- **Trigger:** CEO strategy review — "the strategy is more mature than the roadmap." The roadmap read as two technical spines re-labeled, with the actual operator in LATER. Reorganize from first principles around proving the operator identity.
- **Date:** 2026-09-21
- **Requester/Owner:** CEO review → product

## 2. Affected Concept(s)

- **Primary:** [[RackAI Roadmap]] (`hub-roadmap`) — restructured (organizing logic changed; id/aliases preserved, aliases extended).
- **New:** [[Minimum Operable Estate]] (`hub-minimum-operable-estate`) — MVP operator target, anchors Proof 3.
- **Layer:** L5 (planning hubs).
- **Change type:** major reframe + new object + edge additions.

## 3. The Seven Changes Applied

1. **Reorganized around four proofs** — Observe → Decide → Control → Operate, each with an exit condition phrased as an operating claim. Source phases/programs now map *into* proofs.
2. **Control (Proof 3) moved up** out of LATER — it is the first actual proof of the identity.
3. **Minimum Operable Estate** added as the insisted-upon MVP; roadmap the MOE, not the full harness.
4. **Human-operated → instrumented → assisted → automated** adopted as a governing principle with placement/routing/capacity/governance worked examples ("do not automate before we operate").
5. **Metrics reworked** — north star = **production workloads under management**; families = economics / operational quality / operator leverage (incl. **workloads per ops FTE**) / flywheel / control. Old four KPIs demoted into operational-quality.
6. **Supply abstraction moved to Proof 1** as the *interface* (`SupplyTarget / AcceleratorPool / ExecutionLocation`), owned H100 = impl #1 — a strategy-derived architectural requirement (not multi-provider scheduling).
7. **AI Operations Product** elevated to a first-class workstream running vertically through all four proofs.
   Plus: **P-001 decoupled from the vendor** — strategic decision (partner delivery / retain ops + experiment) separated from the implementation choice (preferred partner Uniphore, pending validation).

## 4. Impact Scan

| Category | Impacted Items |
|----------|---------------|
| Hub pages | [[RackAI Roadmap]] (restructured), [[Minimum Operable Estate]] (new), [[Rack AI Knowledge Base]] (nav + related) |
| Crosswalk | [[Source-to-Concept Crosswalk]] — roadmap row updated + MOE row added |
| Sources | none edited (both spines remain read-only; still referenced) |
| Formulas / Coefficients / Metrics / Scorecards | none modified — but see open question on operator KPI instrumentation ([[KPI Hierarchy]], [[Model Scorecard]]) |

## 5. Confidence Assessment

- Roadmap remains `derived`; MOE is `assumed`.
- **Operator north-star metrics are explicitly `assumed`/aspirational** — none measurable today (no [[Benchmark Run]]/telemetry per [[Capability Gap Register]]). No performance numbers asserted.
- Item confidences carried from source (phase = planned/validated; program = assumed; gaps = missing).
- Truth hierarchy preserved — planning changes land in the canonical hub, not the sources.

## 6. Edges Added

- `hub-roadmap` ↔ `hub-minimum-operable-estate`; `hub-root` → `hub-minimum-operable-estate`.
- `hub-minimum-operable-estate` → `hub-battlegrounds`, `hub-load-bearing-bets`, `hub-governance`, `ent-empirical-map`, `ent-governed-harness`, `idx-capability-gap-register`.
- MOE ID verified unique; `idx-capability-gap-register` edge corrected from an initial wrong `evd-` prefix.

## 7. Open Questions Created

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Ratify the MOE v1 scope (models, supply source, mandatory controls for first attestation) | [[Minimum Operable Estate]], [[Governance Hub]] | High |
| First MOE customer — internal (Uniphore-tenant) or external estate? | [[Load-Bearing Bets]] | High |
| Instrument the operator north-star metric families (currently unmeasured) | [[RackAI Roadmap]], [[KPI Hierarchy]] | High |
| Canonical notes for AI Operations Product workstream + supply-abstraction interface spec | [[RackAI Roadmap]] Open Gaps | Medium |

## 8. Contradictions Surfaced / Resolved

- **Resolved:** the "operator in LATER" contradiction — Control now sits third of four, not last.
- **Resolved:** supply-abstraction-in-LATER risk (baking owned-fleet assumptions into the control plane) — the interface moves to Proof 1.
- **Surfaced (not hidden):** the operator metrics are defined but unmeasurable until Proof 1 lands the primitives — flagged in-note and as an open question.

## See Also

- [[CHANGE_PACKET]]
- [[chg-2026-09-21-canonical-roadmap|Prior packet — canonical roadmap creation]]
- [[RackAI Roadmap]] · [[Minimum Operable Estate]]
