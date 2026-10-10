---
id: hub-governance
type: hub
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [governance hub, standards hub, corpus governance hub, wiki governance]
related: [hub-root, hub-wiki, hub-ai-governance-assurance]
source_docs: [init/init.md, init/agent_guide.md]
confidence: validated
last_reviewed: 2026-09-24
parent: hub-root
summary: "Navigation hub for corpus operating standards, change control, and fitness gates."
---

# Governance Hub

> **Scope note.** This hub covers **corpus governance** — the operating standards, change-control machinery, and fitness gates that keep this knowledge system coherent. It is not the same as the RackAI product pillar for AI Governance & Assurance (runtime policy, provenance, compliance envelope, certifications). For the product, see [[AI Governance and Assurance]].

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

## Product Governance & Assurance

Runtime policy, agent identity, compliance envelope (SOC 2, ISO 42001, NIST AI RMF), provenance and audit — these are the **product** of the [[AI Governance and Assurance]] pillar, not corpus standards. See that hub for ownership, scope, and roadmap alignment.

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[Wiki Hub]]
- [[AI Governance and Assurance]]
