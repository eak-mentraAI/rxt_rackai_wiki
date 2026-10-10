---
id: chg-2026-10-10-resolvable-links
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [resolvable links change, link check change]
related: [pol-regression-suite, pol-fitness-checklist, idx-scripts-readme, src-agent-guide, hub-wiki]
source_docs: []
confidence: validated
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Fixed the corpus's last unresolved link, linked ID references in changelogs, and added a link check."
---

# 2026-10-10 — Resolvable Links

## Trigger

The Knowledge Platform now renders `[[wiki links]]` and relative `.md` links as links to the objects they reference. Links that don't resolve render as dead dotted-underlined text. The platform link checker reported 1 unresolved link in this corpus. This change brings it to 0 and adds enforcement so it stays there.

## Objects Changed

- Added:
  - `scripts/lint-links.sh`: wraps the platform link checker (`packages/ingestion/src/check-links.ts`) and exits non-zero on any unresolved link.
  - `.kiro/hooks/lint-links-on-save.json`: runs the link check after every `.md` save (advisory).
- Changed:
  - [[REGRESSION_SUITE]]: the See Also entry for "Knowledge Graph Acceptance Test Results" was a link to a note that has never existed. It is now plain text marked "not yet created", and runs are recorded in Score History until that note exists.
  - [[2026-09-04 Capability Gap Register]] and [[2026-09-04 OpenRouter Integration Plan]]: the Edges Affected lists used backticked IDs (`hub-evidence` → `idx-capability-gap-register`). They now use wiki links, matching the earlier changelogs. Hubs, sources, and entities are ID-pinned. The two plan/register indexes are linked by file name because they are currently platform shadow objects (see Open Questions).
  - [[FITNESS_CHECKLIST]]: S-03 and the manual verification command now use `./scripts/lint-links.sh` in place of the grep/`comm` file-name check, which didn't understand ids or aliases.
  - `scripts/README.md` and `init/agent_guide.md` (Link Discipline Rule): document the link check and the link contract.
- Deprecated: none.

## Edges

- Added: none (the changelog links make existing edges navigable; no new graph relationships).
- Removed: the dangling link from [[REGRESSION_SUITE]] to the non-existent acceptance-test-results note.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| none | none | none | No content claims changed |

## Open Questions Created

| Question | Affected Docs |
|----------|---------------|
| Several notes have a `summary` longer than 120 characters. The platform rejects their frontmatter, so they become shadow objects that resolve only by file name, not by id or alias. Shorten the summaries? | [[Capability Gap Register]], [[OpenRouter Integration Plan]], [[Validate Launch Lag Under 24h]], [[RackAI Console and CLI Docs]], and the two 2026-09-04 changelogs above |
| [[REGRESSION_SUITE]] frontmatter still cites `05-wiki/Knowledge Graph Acceptance Test Results.md` in `source_docs` and `chg-kg-test-results` in `related`. Neither exists. Create the results note, or remove the references? | [[REGRESSION_SUITE]] |

## Fitness / Consistency Result

- Structural checks: Pass. `./scripts/lint-links.sh` reports 0 unresolved (was 1). The touched notes pass `./scripts/lint-frontmatter.sh`.
- Consistency pass: Pass. Edits are navigational only, and no claims or confidence states changed.
- Regressions: none.

## See Also

- [[Wiki Hub]]
- [[CHANGE_PACKET]]
- [[FITNESS_CHECKLIST]]
