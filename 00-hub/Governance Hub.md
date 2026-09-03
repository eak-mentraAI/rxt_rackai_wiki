---
id: hub-governance
type: hub
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [governance hub, standards hub]
related: [hub-root, hub-wiki]
source_docs: [init/init.md, init/agent_guide.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Navigation hub for operating standards, change control, and fitness gates."
---

# Governance Hub

The operating standards and change-control machinery that keep the corpus a coherent knowledge system rather than a folder of documents.

## Operating Standards

- `init/init.md` — the operating standard
- `init/agent_guide.md` — agent operating manual
- `.kiro/steering/rackai-operating-standards.md` — always-on standards
- `.kiro/steering/agent-behavior.md` — behavior rules and graph invariants
- `.kiro/steering/corpus-update-propagation.md` — update propagation skill (auto-included)

## Change Control

- [[CHANGE_PACKET]] — required before any meaningful edit
- [[FITNESS_CHECKLIST]] — structural, consistency, and regression gates
- [[REGRESSION_SUITE]] — acceptance tests (R-01…R-07)
- [[CONSISTENCY_REPORT]] — consistency-pass output template

## Enforcement

- `scripts/lint-frontmatter.sh` — frontmatter compliance
- `.kiro/hooks/lint-frontmatter-on-save.json` — save-time lint
- `.kiro/hooks/corpus-fitness-reminder.json` — propagation reminder
- `.kiro/hooks/validate-summary-length.json` — summary-length guard

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[Wiki Hub]]
