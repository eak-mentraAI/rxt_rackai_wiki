---
id: chg-2026-10-10-prd-spec-workflow-skill
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd spec workflow skill, spec ingestion support, knowledge platform spec type]
related: [chg-2026-10-10-tech-spec-prd-v2, chg-2026-10-10-prd-a-workload-declaration, pol-fitness-checklist, prd-workload-declaration-placement]
source_docs: ["PM direction 2026-10-10: make the process a tracked reusable skill for all wikis; knowledge console must ingest PRDs and specs before push", "eak-mentraAI/knowledge-platform PR #23"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Added the tracked PRD→spec→roadmap workflow skill to all three wikis; knowledge-platform spec type opened as PR #23."
---

# CHANGE 2026-10-10 — PRD/Spec Workflow Skill and Spec Ingestion

## Trigger

After PRD A was approved, the product owner asked for:
- the PRD → tech spec → roadmap process as a reusable skill, tracked and usable by every wiki
- the knowledge console able to ingest PRDs and tech specs **before** wiki changes are pushed, and before the first tech spec is written

## What Changed

**Skill.** New `.claude/skills/prd-spec-workflow/SKILL.md`, tracked in git. It has three modes:
- draft or revise a PRD
- convert an approved PRD into a tech spec
- record as-built drift

It sets explicit stop points for product and engineering approval, and holds no rules of its own. It points to the steering files and templates, and reads repo-specific facts (code repos, roadmap table, scripts) from the operating standards.

**Tracking.** `.claude/` stays excluded locally through `.git/info/exclude`, but the rule is now `.claude/*` with an exception for `!.claude/skills/`. Hooks and local settings stay untracked.

**Portable pack.**
- `scripts/sync-prd-standard.sh` now carries the skill and rewrites the exclude rule on `--apply`.
- Applied to **AIOS Wiki** and **VCFRaxWiki**. Each now has:
  - the `spec` type in its operating standards (and AIOS's lint)
  - the fitness checks P-09 to P-11 and Section 2c (T-01 to T-11), generalized for that repo
  - a *Code Repositories (read-only)* placeholder to fill before its first tech spec
- AIOS's lint now skips `.claude/`, matching RackAI.
- Each sibling is committed locally, staging only the standard-pack paths. Neither is pushed.

**Knowledge platform.** [eak-mentraAI/knowledge-platform#23](https://github.com/eak-mentraAI/knowledge-platform/pull/23) adds:
- `spec` as a first-class object type, with prefix `spec-`
- structural expectations for `spec` keyed to the tech-spec template
- `prd` structural expectations re-keyed to PRD template v2
- tests

Verification:
- A local full build of this corpus (commit `62fce30`) plus a probe spec ingested PRD A as a typed `prd` and the probe as a typed `spec`.
- There were 0 blocking errors outside `reference/`.
- Knowledge-platform tests: 182 passed. Lint and typecheck are clean.
- Hidden folders (`.claude`, `.kiro`) are already skipped by ingestion, so the skill never appears in the console.

## Impact

- **Do not push any wiki before PR #23 is merged and deployed.** After deploying, sync the corpus and confirm in the console that PRD A appears as a PRD.
- The first tech spec waits for that confirmation.

## Open Questions

- Deploying knowledge-platform to production is a separate step and needs the product owner's go-ahead.
