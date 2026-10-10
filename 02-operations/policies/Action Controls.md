---
id: pol-action-controls
type: policy
status: draft
owner: governance
domain: governance
aliases: [action controls, blast radius, action controls and blast radius, approval gates, containment]
related: [ent-agent-identity, wf-perimeter-info-flow, pol-supply-chain-inventory, hub-governance, src-rackai-dev-plan, ent-governed-harness, prd-governed-execution-authority, spec-governed-execution-authority, prd-concierge-engineer]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-governance
summary: "Policy: gate what an agent can do to the world — approval gates, rate limits, reversibility, containment."
---

# Action Controls

## Purpose

**Action Controls** gate what an agent can do **to the world**: approval gates, rate limits, reversibility, and containment. It is the operations-plane control on **outbound actions** — the blast-radius limit. Authorization by identity is **upstream** in [[Agent Identity]]; this policy governs what a known, authorized actor is then allowed to *do*. Productization item **P8**.

> **Assumed confidence.** P8, dev track. Net-new as a canonical control.

## Rule

An agent's outbound actions are constrained by approval gates, rate limits, reversibility requirements, and containment boundaries appropriate to the action's blast radius. High-blast-radius actions require an explicit gate (human approval or policy check) before execution.

## Scope

All outbound/side-effecting actions taken by a [[Governed Harness]] or its agents against external systems.

## Governs

| Target | Relationship |
|--------|--------------|
| [[Governed Harness]] | CONSTRAINS → outbound actions gated |
| [[Agent Identity]] | DEPENDS_ON ← must know the actor before gating actions |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSTRAINS | [[Governed Harness]] | → | Outbound actions gated |
| DEPENDS_ON | [[Agent Identity]] | → | Must know the actor before gating actions |

## Enforcement

Enforced in the operations plane at the point an agent attempts a side-effecting action; gates, rate limiters, and reversibility/containment wrappers.

## See Also

- [[Governance Hub]]
- [[Agent Identity]]
- [[Supply Chain Inventory]]
- [[Governed Execution & Delegated Authority PRD]] — action classes, bound authorisations, emergency path (draft)
- [[Concierge Engineer PRD]] — first consumer (v1 actions) (draft)

