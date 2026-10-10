---
id: chg-2026-10-02-uniphore-recovery-plan
type: change
status: draft
owner: product
domain: governance
aliases: [uniphore recovery plan ingestion 2026-10-02, uniphore battlecard map change]
related: [idx-uniphore-recovery-plan, idx-open-questions, idx-crosswalk, hub-roadmap]
source_docs: ["05-wiki/Uniphore Recovery Plan — RackAI Input.md", "reference/FW- RackAI Project Update - Jun 4 2026.eml", "reference/RackAI-Roadmap 2.pptx", "reference/RackAI-Roadmap-Uniphore.pptx", "reference/IaaS Battlecard .pdf", "reference/FTaaS Battlecard .pdf"]
confidence: assumed
last_reviewed: 2026-10-02
parent: hub-wiki
summary: "Added the Uniphore recovery-plan note; registered its sources and three surfaced open questions."
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

---

## Revision — 2026-10-02 (Table B status clarifications)

Status updates to [[Uniphore Recovery Plan — RackAI Input]] §3-B from the owner (clarified delivery states/dates). Also reconciled the §4 battlecard tables so AMD/AIM status is consistent across the note (C-02/C-04).

- Inference routing + shared KV cache → **In progress (due 30 Oct 2026)**
- Speculative decoding, Refrag → **Planned (Q4 2026)**
- DPO; context-parallel FT → **In progress (due 30 Oct 2026)** (context-parallel FT itself already complete, RACKAI-340)
- End-to-end deployment automation (IaC) → **In progress (due 30 Oct 2026)**
- Inference observability + repeatable benchmarking → **Planned (Q4 2026)**
- AMD → **AMD inference Complete**; **AMD AIM engine Backlog (partnership-dependent)**. §4 IaaS row updated to ✅ AMD inference; §4 FTaaS row updated to ⚪ AMD FT (gated on the backlogged AIM engine).

No canonical IDs/aliases changed; confidence unchanged; no new performance numbers; crosswalk mappings still accurate. These are more precise delivery states, not new conflicts — the NIM/SFT/LoRA conflict remains the only open status conflict.

---

## Revision — 2026-10-02 (expanded §3-C Future alignment)

Expanded [[Uniphore Recovery Plan — RackAI Input]] §3 bucket C from 4 generic rows to 18 real roadmap items grouped into four value themes (C1 consumption & model choice; C2 enterprise model services; C3 advanced inference & FT; C4 secure developer & governance). Rationale: Uniphore didn't request these, but they are the natural maturation of the platform Uniphore already runs on and each removes a reason to stay on Fireworks.

- **Source:** master roadmap deck (`RackAI-Roadmap 2.pptx`, Q1 '27 Expansion + Q2 '27 Enterprise Scale) — already registered in the crosswalk; no new source.
- **Framing:** each item uses *Uniphore need → RackAI capability → expected impact*; horizons are directional, not commitments.
- **Confidence:** C-items explicitly labeled **Low** (inferred Uniphore benefit, not a documented request). Note stays `assumed`.

Propagation: no new canonical concept (all items live on [[RackAI Roadmap]]); no dependent notes, formulas, metrics, coefficients, or scorecards affected; crosswalk unchanged; no new performance numbers. Fitness gate: S-16 summary 115 chars (pass); no broken links introduced; C-09 targets-vs-results discipline preserved (directional horizons, Low confidence).
