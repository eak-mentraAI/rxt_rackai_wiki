---
id: chg-2026-10-02-uniphore-recovery-plan
type: change
status: draft
owner: product
domain: governance
aliases: [uniphore recovery plan ingestion 2026-10-02, uniphore battlecard map change]
related: [idx-uniphore-recovery-plan, idx-open-questions, idx-crosswalk, hub-rackai-roadmap]
source_docs: ["05-wiki/Uniphore Recovery Plan — RackAI Input.md", "reference/FW- RackAI Project Update - Jun 4 2026.eml", "reference/RackAI-Roadmap 2.pptx", "reference/RackAI-Roadmap-Uniphore.pptx", "reference/IaaS Battlecard .pdf", "reference/FTaaS Battlecard .pdf"]
confidence: assumed
last_reviewed: 2026-10-02
parent: hub-wiki
summary: "Added the Uniphore recovery-plan note; registered its sources and three surfaced open questions (status conflict, engagement gap, requirement currency)."
---

# 2026-10-02 — Uniphore Recovery Plan Ingestion

## Trigger

Leadership (Chetan/Vito/Mullapudy thread) requested a Uniphore partnership recovery plan. Ed owns three RackAI deliverables: current roadmap (#2), what we can offer Uniphore and when (#3), and a battlecard-mapped "what's already done" (#4). Material was synthesized from the Jun 2026 project update, the master and Uniphore roadmap decks, the M2/CSP delivery CSVs, the clarification Q&A, the environment inventory, and the two internal battlecards.

## Objects Changed

- **Added:** [[Uniphore Recovery Plan — RackAI Input]] (`idx-uniphore-recovery-plan`, L5 wiki, type `index`, confidence `assumed`). Contains deliverables #2–#4 plus caveats and the recommended Uniphore ask.
- **Updated:** [[Open Questions]] — three new entries (see below).
- **Updated:** [[Source-to-Concept Crosswalk]] — four new source rows (Jun update .eml; roadmap decks + M2 CSVs; IaaS/FTaaS battlecards; Uniphore scope CSVs) all mapped to the new note.

## Edges Affected

- `idx-uniphore-recovery-plan` → relates to `hub-wiki`, `hub-rackai-roadmap`, `ent-model-deployment`, `ent-organization`, `wf-fine-tuning`, `wf-serving-lifecycle`, `idx-open-questions`.
- New source→concept edges in the crosswalk point the six reference inputs at the recovery-plan note.
- Open-questions edges link the three new unknowns to [[Model Deployment]], [[Fine-Tuning]], [[Environment]], [[Organization]], and the recovery-plan note.

## Open Questions Created

1. **Delivery-status conflict** — Jun 2026 update reports NIM/SFT/LoRA *completed* and shared in staging; the Uniphore progress slide marks them "Milestone 2 (not yet production)." Engineering must confirm before any "in production" claim to Uniphore.
2. **Engagement gap** — a dedicated Uniphore production environment (DFW3, 8× H100) is Active, but no Uniphore acceptance, production feedback, or post-Jun priorities are on record. Is Uniphore still engaged on the DFW Prod track?
3. **Requirement currency** — the strongest "Uniphore requirements" on file are secondhand (PM-attributed, several flagged "assuming… need clarification"), not direct Uniphore statements. Which still hold?

## Fitness Gate

Per [[FITNESS_CHECKLIST]]:
- **S-01 / S-04** — note sits in `05-wiki/` as an `index`; defines no new canonical entity, so no duplicate/ layer violation. Pass.
- **S-05 / S-06 / S-07** — owner, `source_docs`, and `confidence: assumed` all set. Pass.
- **S-14 / S-15** — no canonical IDs changed or recycled; no aliases deleted. Pass.
- **S-16** — summaries on all three touched files ≤120 chars (115 / 88 / 61). Pass.
- **S-03** — all new wikilinks resolve to existing notes. Pass.
- **C-08 (no hidden conflicts)** — the Jun-vs-slide status conflict is surfaced in Open Questions rather than smoothed over. Pass.
- **C-09 (targets vs results)** — roadmap items are presented as directional/horizon-based, not as delivered results; battlecards explicitly flagged as marketing collateral, not measured capability or a Uniphore requirement. Pass.

## Notes / Caveats

- The note is `assumed` because it mixes documented delivery facts with directional roadmap framing and secondhand requirement signals; it should not be treated as a Uniphore-validated requirements set.
- The battlecards are internal "CONFIDENTIAL — INTERNAL USE ONLY" sales collateral never shared with Uniphore and must not be used as an acceptance yardstick — captured explicitly in the note's §4 framing.
- No performance numbers were introduced, so no S-13 benchmark tracing was required.

---

## Revision — 2026-10-02 (reviewer feedback incorporated)

Framing/discipline edits to [[Uniphore Recovery Plan — RackAI Input]] after leadership review. No change to canonical ID, aliases, confidence, or source mappings; no new entities, metrics, or performance numbers.

- **Softened narrative:** "The scope moved underneath the delivery" → "The requirements and priorities evolved during the engagement, including changes to the originally agreed roadmap" (closer to Amine's documented language, less rhetorical).
- **Reframed the ask:** "Uniphore commits to a definition of success" → "The one thing we need from Uniphore is a current, concrete definition of success" (collaborative, not adversarial).
- **Hardened the status-conflict caveat:** added a prominent **Status-Conflict Rule** — never resolve a delivered-vs-milestone conflict by inference; preserve both statements and flag for engineering confirmation before any customer-facing language. NIM/SFT/LoRA described only as *delivered to staging*, never "in production," until confirmed. Cross-linked to [[Open Questions]].
- **Added "Recommended meeting narrative"** — a 5–6 sentence spine for the meeting; tables are positioned as supporting evidence beneath it.

Fitness gate re-checked: S-16 summary 115 chars (pass); S-03 new `[[Open Questions]]` link resolves (pass); C-08/C-09 preserved and strengthened (conflict kept open, targets-vs-results discipline reinforced).
