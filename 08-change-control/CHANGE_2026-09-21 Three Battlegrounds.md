---
id: chg-2026-09-21-three-battlegrounds
type: change
status: reviewed
owner: product
domain: strategy
aliases: [three battlegrounds change packet, battlegrounds change, competitor notes change]
related: [hub-battlegrounds, evd-inference-serving-competitors, evd-gpu-neocloud-competitors, evd-sovereign-governed-competitors, pol-change-packet, hub-evidence]
source_docs: ["web research 2026-09-21", "reference/jd/EXTERNAL_PDM_Orchestration_and_Harness_JD.md", "04-evidence/assumptions/Fleet Competitiveness.md", "04-evidence/Capability Gap Register.md"]
confidence: assumed
last_reviewed: 2026-09-21
parent: hub-wiki
summary: "Change packet: added the Three Battlegrounds positioning hub and three per-battleground competitor evidence notes, wired to hubs and crosswalk."
---

# Change Packet — Three Battlegrounds & Competitor Evidence Notes (2026-09-21)

## 1. Source of Change

- **Trigger:** business decision (leadership positioning question) + competitive datapoints (web research)
- **Source reference:** market/competitor web research 2026-09-21; grounded in [[Fleet Competitiveness]], [[Capability Gap Register]], [[Enterprise AI Portfolio]], the Orchestration & Harness and Assurance & Governance JDs.
- **Date:** 2026-09-21
- **Requester/Owner:** product

## 2. Affected Concept(s)

- **Primary concept:** [[Three Battlegrounds]] (`hub-battlegrounds`) — new positioning model
- **Layer:** L5 (wiki/navigation, strategy hub) + L4 (evidence — competitor teardowns)
- **Change type:** new objects + relationship (edge) additions to existing hubs

## 3. Impact Scan

| Category | Impacted Items |
|----------|---------------|
| Hub pages | [[Rack AI Knowledge Base]], [[Product Hub]], [[Evidence Hub]], [[Governance Hub]], [[Enterprise AI Portfolio]], [[Commercial & Capacity Hub]] (edges added) |
| Evidence | 3 new teardowns; sits alongside [[Erebine Competitive Analysis]] |
| Crosswalk | [[Source-to-Concept Crosswalk]] — 4 rows added |
| Entities / Formulas / Coefficients / Metrics / Benchmarks | none modified (referenced only) |
| Assumptions / Validations / Events / Policies / Scorecards | none modified |

## 4. Confidence Assessment

- **Confidence of new information:** strategy hub `assumed`; competitor teardowns `derived` overall (hardware specs `measured`; funding valuations `derived`; vendor security/compliance claims `assumed`; Palantir FedRAMP High `validated` via FedRAMP Marketplace).
- **Confidence change on existing notes:** unchanged (edges only).
- **Weakest link:** the positioning recommendation depends on capabilities that are `assumed`/planned per [[Capability Gap Register]] — the identity claim is directional, not shipped.

## 5. Objects Added

- `hub-battlegrounds` — `00-hub/Three Battlegrounds.md`
- `evd-inference-serving-competitors` — `04-evidence/Inference Serving Competitors.md` (Fireworks, Together, Baseten, Anyscale)
- `evd-gpu-neocloud-competitors` — `04-evidence/GPU Neocloud Competitors.md` (CoreWeave, Lambda)
- `evd-sovereign-governed-competitors` — `04-evidence/Sovereign & Governed AI Competitors.md` (Palantir, Cohere, Mistral, Scale AI)

## 6. Edges Added

- `hub-battlegrounds` ROUTES_TO/SUPPORTS the three teardowns; teardowns SUPPORT `hub-battlegrounds`.
- Back-links added: `hub-root`, `hub-product`, `hub-evidence`, `hub-governance`, `hub-enterprise-ai`, `hub-commercial` → `hub-battlegrounds` and relevant teardowns.
- `idx-crosswalk` maps 2026-09-21 research → the four new notes.

## 7. Open Questions Created

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Does Baseten's self-hosted VPC + HIPAA posture directly contest RackAI's sovereign wedge? | [[Inference Serving Competitors]], [[Sovereign & Governed AI Competitors]] | High |
| Palantir partner-vs-competitor boundary: which layers do we cede vs. contest? | [[Sovereign & Governed AI Competitors]], [[Enterprise AI Portfolio]] | High |
| Minimum viable compliance gate (FedRAMP High? IL? ISO 42001?) for the first regulated buyer | [[Governance Hub]] | High |
| Should RackAI source overflow capacity from a neocloud partner rather than compete? | [[Commercial & Capacity Hub]], [[Capacity Pool]] | Medium |
| Confirm Fireworks and Mistral certification sets against vendor trust pages | teardowns | Medium |

## 8. Contradictions Surfaced

None hidden. The tension that RackAI's battleground-(c) advantages are `assumed`/planned while competitors already hold gating certifications is surfaced explicitly in [[Three Battlegrounds]] (Honest Caveats) and each teardown's Threat Assessment.

## See Also

- [[CHANGE_PACKET]]
- [[FITNESS_CHECKLIST]]
- [[Three Battlegrounds]]
