---
id: chg-2026-10-06-prd-standard-pack
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd standard pack change, portable prd standard, prd steering change]
related: [pol-fitness-checklist, prd-solution-marketplace]
source_docs: ["PM request: consistent PRD shape across sibling wiki repos 2026-10-06"]
confidence: validated
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Added a portable PRD standard pack (steering, template, P-checks, sync script) and ported it to AIOS and VCF wikis."
---

# 2026-10-06 — Portable PRD Standard Pack

## Trigger

PRDs are now a recurring deliverable across the sibling knowledge-wiki repos. Request: set a consistent **shape** and a **minimum viable set** every PRD must answer, and apply it across the sister repos (not just RackAI). Chosen approach (option B): author a **portable pack** once in RackAI Wiki (canonical source), then copy it into the other wiki repos.

## Scope of repos

- **In scope (wiki corpora, shared structure):** RackAI Wiki (canonical source), **AIOS Wiki** (`aios-wiki` remote), **VCFRaxWiki** (`RXT-Cloud-Wiki` remote).
- **Excluded:** VCF9 Services Hub (a services/app repo, not a wiki — different owner, 35k files), Mentra* (different project), RXT Product Hub (not a wiki).
- **Duplicate finding:** `aios-wiki` is a stale, fully-pushed clone of the same remote as `AIOS Wiki` (clean tree, no unpushed commits, no stashes) — safe for the user to retire; `AIOS Wiki` is the current one (ahead: 2026-10-03 vs 2026-09-15, 141 vs 135 commits). `AIOS Wiki (Legacy)` is a non-git archive, unrelated. **Deletion left to the user** (destructive, outside workspace).

## Objects Added (canonical source — RackAI Wiki)

- **`.kiro/steering/prd-standards.md`** — the normative standard (repo-agnostic). `inclusion: fileMatch` on `*PRD*` so it loads when a PRD is in context rather than every session. Defines: what a PRD is/isn't (Layer-5 projection, not a redefinition), location/naming/type (`05-wiki/`, `prd-<slug>`, `type: prd`), required frontmatter, the **ten-item minimum viable set**, confidence discipline (proposed vs funded; no asserting unbuilt capability), shape discipline (scope line, testable numbered reqs, kill criterion, owned decisions, don't over-specify), and a **propagation header** naming the sibling repos.
- **`templates/prd.md`** (refined) — `type: prd` (index fallback noted), portable comments (summary ≤120, related MUST include canonical ID, minimum-set reminder), and the **kill/falsification criterion promoted to its own section (§12)** rather than buried in Risks. See Also de-RackAI-ized.
- **`08-change-control/FITNESS_CHECKLIST.md`** — new **Section 2b — PRD Checks (P-01…P-08)**: canonical link, minimum set, boundary stated, requirements testable, kill criterion present, open decisions owned, confidence honesty, shape compliance.
- **`scripts/sync-prd-standard.sh`** — portable propagation helper; dry-run by default, `--apply` to copy; copies steering + template, reports (does not overwrite) the checklist so repo-specific checks are preserved; sibling list editable at the top.

## Propagation performed

Ran `sync-prd-standard.sh --apply` → copied `prd-standards.md` + `templates/prd.md` into **AIOS Wiki** and **VCFRaxWiki** (verified byte-identical to source). Inserted the Section 2b P-check block before "Section 3" in each sibling's `FITNESS_CHECKLIST.md` (verified 8/8). Both siblings confirmed to share the required structure before writing.

> **Commit discipline (for the user):** both siblings carried **pre-existing uncommitted work** unrelated to this change. When committing the pack in each sibling, stage **only** the three pack paths (`.kiro/steering/prd-standards.md`, `templates/prd.md`, `08-change-control/FITNESS_CHECKLIST.md`) — do not `git add .`. Commit in each repo separately.

## Confidence

`validated` for the governance artifacts (this is a standard, not a claim about a product). The standard itself mandates `assumed` for proposed PRDs. No product capability asserted or upgraded.

## Downstream / Consistency

- The existing [[Solution Marketplace PRD]] (`prd-solution-marketplace`) predates the `prd` type and uses `type: index`; it already satisfies the minimum set and P-checks in substance. **Optional follow-up:** flip its `type` to `prd` once the `prd` note type is added to each repo's operating-standards type list (a governance decision deferred to the user — it touches the frontmatter schema the ingestion validates against).
- One-Concept / layer purity: held — the standard is governance (steering + policy); the template is a scaffold; neither defines a domain concept.
- Fitness: steering, template, and checklist self-consistent; section cross-references (kill criterion §12, minimum-set section list) reconciled after the template renumber.

## Open Decision (deferred to user)

| Decision | Note |
|----------|------|
| Add `prd` as a first-class note type in each repo's operating-standards steering file? | Cleaner than the `index` fallback; touches the schema everything validates against — flagged, not done. If adopted, flip existing PRDs' `type` and re-run the sync. |

## See Also

- `.kiro/steering/prd-standards.md` · `templates/prd.md` · `scripts/sync-prd-standard.sh`
- [[FITNESS_CHECKLIST]] — now carries P-01…P-08
- [[Solution Marketplace PRD]] — the first PRD, exemplar for the standard
- [[CHANGE_PACKET]]
