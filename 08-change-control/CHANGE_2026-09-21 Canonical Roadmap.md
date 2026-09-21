---
id: chg-2026-09-21-canonical-roadmap
type: change
status: reviewed
owner: product
domain: strategy
aliases: [canonical roadmap change, roadmap hub change]
related: [hub-roadmap, hub-battlegrounds, src-engineering-roadmap, src-rackai-dev-plan, pol-change-packet, chg-2026-09-21-operator-identity]
source_docs: ["06-sources/Rack AI OpenRouter Engineering Roadmap.md", "06-sources/RackAI Enterprise AI Development Plan.md", "CEO direction 2026-09-21"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-wiki
summary: "Change packet: created the canonical, living RackAI Roadmap that synthesizes both source spines under the operator identity, with a Proposed-Changes intake for future roadmap edits."
---

# Change Packet — Canonical Living Roadmap (2026-09-21)

## 1. Source of Change

- **Trigger:** business decision — establish an editable, living canonical roadmap as the single planning home before proposing strategy-aligned changes.
- **Date:** 2026-09-21
- **Requester/Owner:** CEO direction → product

## 2. Affected Concept(s)

- **Primary:** [[RackAI Roadmap]] (`hub-roadmap`) — new canonical planning hub.
- **Layer:** L5 (navigation/planning hub).
- **Change type:** new object + edge additions.

## 3. Impact Scan

| Category | Impacted Items |
|----------|---------------|
| Hub pages | [[Rack AI Knowledge Base]] (nav + related), [[Product Hub]] (roadmap pointer + related) |
| Sources | [[Rack AI OpenRouter Engineering Roadmap]] (related edge only — content untouched, stays `validated` read-only), [[RackAI Enterprise AI Development Plan]] (related edge only) |
| Crosswalk | [[Source-to-Concept Crosswalk]] — 1 row added |
| Entities / Formulas / Coefficients / Metrics / Benchmarks / Scorecards | none modified (referenced only) |

## 4. Confidence Assessment

- New roadmap hub: `derived` (synthesis of two existing spines). Individual items inherit source confidence (phase = validated; program = assumed; gaps = missing/planned).
- **Operator KPI tier is explicitly marked `proposed`, not adopted** — its metrics have no benchmark/telemetry yet and are not asserted as active.
- No performance numbers introduced; all remain traced to their source phase/program or flagged missing per [[Capability Gap Register]].
- Source narratives unchanged — truth hierarchy preserved (planning happens in the canonical hub, not in the `validated` source).

## 5. Objects Added / Edges

- **Added:** `hub-roadmap` — `00-hub/RackAI Roadmap.md`.
- **Edges:** `hub-root` and `hub-product` → `hub-roadmap`; `hub-roadmap` → both source spines, `hub-battlegrounds`, `hub-load-bearing-bets`, `ent-empirical-map`, `ent-governed-harness`, planning notes; source spines → `hub-roadmap` (up-pointer).

## 6. Open Questions Created

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Adopt the operator KPI tier (workloads operated, cost-per-outcome, transferable-telemetry capture, compliance coverage)? | [[RackAI Roadmap]], [[KPI Hierarchy]] | High |
| Where do the 6 open roadmap gaps (harness, supply abstraction, transferable-vs-isolated telemetry, compliance envelope, operator KPIs, managed-ops/FDE) land in the horizons? | [[RackAI Roadmap]] | High |
| First batch of operator-alignment proposals for the Proposed-Changes queue | [[RackAI Roadmap]] | High |

## 7. Contradictions Surfaced

None hidden. The core tension — two unreconciled source spines (inference-provider vs operator) — is now made explicit and reconciled in one hub; the "Open Roadmap Gaps" section names exactly where the strategy is ahead of both sources.

## See Also

- [[CHANGE_PACKET]]
- [[RackAI Roadmap]]
- [[Three Battlegrounds]]
