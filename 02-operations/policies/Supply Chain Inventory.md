---
id: pol-supply-chain-inventory
type: policy
status: draft
owner: governance
domain: governance
aliases: [supply chain inventory, config inventory, supply chain and config inventory, sbom, running-system inventory]
related: [pol-action-controls, pol-governable-self-modification, wf-audit, hub-governance, src-rackai-dev-plan]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-governance
summary: "Policy: maintain an inventory of what's in the running system — models, prompts, tools, components — with provenance."
---

# Supply Chain Inventory

## Purpose

**Supply Chain Inventory** is the record of **what's in the running system** — models, prompts, tools, components — with their **provenance and versions**. It is the operations-plane inventory a regulator will ask for. Productization item **P9**; partly covered by a data-fabric product today (`~U`).

> **Assumed confidence.** P9, dev track. Partial coverage exists; the governed, provenance-complete inventory is the gap.

## Rule

Every component running in the system (model version, prompt, tool, dependency, config) must be recorded in the inventory with its source/provenance and version. Changes update the inventory; the inventory is queryable for audit.

## Scope

All models, prompts, tools, and components deployed in any [[Environment]], across the [[Governed Harness]] instances and serving stack.

## Governs

| Target | Relationship |
|--------|--------------|
| [[Governed Harness]] | GOVERNS → components inventoried |
| [[Model Deployment]] | GOVERNS → model version + provenance recorded |
| [[Audit]] | SUPPORTS → inventory feeds audit answers |

## Enforcement

Maintained continuously in the operations plane; a change to any running component updates the inventory. Feeds [[Governable Self-Modification]] (what changed) and [[Audit]].

## See Also

- [[Governance Hub]]
- [[Audit]]
- [[Governable Self-Modification]]
