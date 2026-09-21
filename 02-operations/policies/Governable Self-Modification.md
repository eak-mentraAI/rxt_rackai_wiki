---
id: pol-governable-self-modification
type: policy
status: draft
owner: governance
domain: governance
aliases: [governable self-modification, self-modification, re-certification, certifiable self-improvement]
related: [wf-self-improvement-loop, pol-supply-chain-inventory, wf-audit, wf-canary-rollback, hub-governance, src-rackai-dev-plan]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-governance
summary: "Policy: version, attribute, replay, and re-certify a system that rewrites its own behavior, so it stays governable."
---

# Governable Self-Modification

## Purpose

A system that improves itself **changes its own behavior**. That works against what a regulator certifies — that it still behaves as it did when approved. **Governable Self-Modification** is the requirement that a self-rewriting system can be **versioned, attributed, replayed, and re-certified**. It is the same seam as the [[Self-Improvement Loop]] (thread 3.3) seen from the **audit side** (thread 2.4), and is one of the moat concepts.

> **Assumed confidence.** Program 2 thread 2.4, long-term research (`L+A`). Net-new; no product covers it today.

## Rule

Any change the system makes to its own behavior (weights, memory, skills, prompts, routing) must be versioned, attributable to what caused it, replayable, and re-certifiable against the approved baseline before it governs production. A change that cannot be re-certified may not take effect in a regulated workload.

## Scope

All self-modifications produced by the [[Self-Improvement Loop]] in any regulated [[Environment]].

## Governs

| Target | Relationship |
|--------|--------------|
| [[Self-Improvement Loop]] | GOVERNS → learning stays certifiable |
| [[Supply Chain Inventory]] | USES → what changed and its provenance |
| [[Canary & Rollback]] | USES → safe rollout / undo of a change |
| [[Audit]] | SUPPORTS → re-certification evidence |

## Enforcement

Enforced at the point a self-modification would take effect: it must carry version, attribution, and replay evidence, and pass re-certification (shadow eval / canary) before promotion.

## See Also

- [[Governance Hub]]
- [[Self-Improvement Loop]]
- [[Audit]]
