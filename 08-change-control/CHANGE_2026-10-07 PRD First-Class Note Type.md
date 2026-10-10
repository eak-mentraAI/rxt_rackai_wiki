---
id: chg-2026-10-07-prd-first-class-type
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd note type change, prd first-class type, companion note type, note type alignment 2026-10-07]
related: [pol-fitness-checklist, chg-2026-10-06-prd-standard-pack, prd-solution-marketplace, bench-agentx-standard]
source_docs: ["PM request: make PRD and companion first-class note types across all three wikis 2026-10-07"]
confidence: validated
last_reviewed: 2026-10-07
parent: hub-wiki
summary: "prd and companion made first-class note types across all three wikis and knowledge-platform; lint debt cleared."
---

# 2026-10-07 — PRD and Companion as First-Class Note Types

## Trigger

The portable PRD standard ([[CHANGE_2026-10-06 PRD Standard Pack (Portable)]]) specified `type: prd`, but nothing downstream accepted it:

- This repo's lint (`scripts/lint-frontmatter.sh`) rejected `prd`, so [[Solution Marketplace PRD]] used the `index` fallback.
- knowledge-platform ingestion rejected `prd` and `companion`. Any note with an unknown type fails frontmatter validation (blocking) and is downgraded to an unstructured shadow node. That already affected 13 `type: prd` and 17 `type: companion` notes in VCFRaxWiki.
- knowledge-platform accepted `projection`, but this repo's lint rejected it.

## What Changed

**knowledge-platform** (branch `feat/prd-companion-note-types`)
- Added `prd` (prefix `prd-`) and `companion` (prefix `cmp-`) to `KNOWLEDGE_OBJECT_TYPES` (17 → 19).
- `prd` structural expectations key on the template's section headings and are recommendation-level only. `companion` has none, because it mirrors its source.
- Updated tests and `docs/CORPUS_COMPLIANCE_GUIDE.md`. Typecheck and the full test suite pass (163/163).

**RackAI Wiki (canonical source of the PRD standard)**
- Lint `VALID_TYPES` now includes `prd`, `projection` and `companion`.
- The lint skips `reference/` (raw AI-agent context, no frontmatter by design), except `* - Companion.md` files. It also skips the gitignored `_ontology-discovery/`. The skip applies to full runs and to explicit file arguments, so the pre-commit hook follows it too.
- `.kiro/steering/rackai-operating-standards.md`, `init/init.md`, `scripts/README.md`: updated the type lists and added a `companion` definition.
- `.kiro/steering/prd-standards.md`, `templates/prd.md`: `prd` is first-class, and the `index` fallback was removed.
- [[Solution Marketplace PRD]]: `type: index` → `type: prd`. The kill criterion moved out of Risks into its own §12, per template and fitness check P-05. Open Decisions is now §13, and its in-text reference is updated.
- **Lint debt cleared:** shortened 19 over-length summaries, preserving their meaning. [[AgentX Benchmark Standard]] used the non-canonical confidence `asserted`, which is now `assumed`, the weakest canonical state. The note's banner and exit-criterion text were updated to match; the meaning is unchanged (external claims, unverified by RackAI). The full repo lint now passes (224/224).

**AIOS Wiki**
- Lint, operating standards, `init/init.md`, `scripts/README.md`: added `prd` and `companion`.
- Re-synced the PRD standard pack (`scripts/sync-prd-standard.sh --apply`).
- Its existing companions live in `06-sources/reference/` as `type: source`. They are left as-is; new companions should use `companion`.

**VCFRaxWiki**
- Already listed `prd` and `companion`. Re-synced the PRD standard pack only.

## Why

One type for one kind of note. Using `index` as a stand-in hid PRDs among real indexes, and the type mismatch between wiki and platform silently turned valid notes into shadow nodes.

## Impact

- **Deploy order:** merge and deploy knowledge-platform **before** pushing wiki commits that use `type: prd` or `type: companion`. Otherwise those notes become shadow nodes until the platform catches up. The summary and confidence fixes are valid under the current platform and can be pushed first.
- After the deploy and a corpus rebuild, VCFRaxWiki's 13 PRDs and 17 companions become structured objects.
- VCFRaxWiki companion IDs have no `cmp-` prefix, so the platform will raise non-blocking `id-format` warnings for them.

## Open Questions

- AIOS Wiki has 20 pre-existing lint failures (mostly missing `summary`/`parent`, including its companions). Not addressed here.
- Should AIOS Wiki's 12 `type: source` companions migrate to `companion`?
