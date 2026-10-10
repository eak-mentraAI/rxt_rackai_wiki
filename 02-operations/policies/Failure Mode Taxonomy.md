---
id: pol-failure-taxonomy
type: policy
status: draft
owner: rackai-product
domain: governance
aliases: [failure taxonomy, fail open fail closed, failure classes, degraded mode policy]
related: [prd-workload-declaration-placement, prd-operator-economics, prd-governed-execution-authority, prd-customer-observability-evidence, prd-sovereign-isolation-assurance, prd-inference-access-distribution, prd-fine-tuning-operations, pol-verification-status, pol-release-readiness]
source_docs: ["Product-owner review disposition, PRD batch B–J, 2026-10-10 (finding S-4)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-governance
summary: "One vocabulary for what continues, stops or degrades when a subsystem fails, by failure class, with notification."
---

# Failure Mode Taxonomy

## Purpose

The PRDs used *fail-open*, *fail-closed*, *quarantine*, *contain*, *stop*, *unverified* and *not offered* independently. Each choice was defensible on its own, but undocumented differences interact badly. For example, inference keeps running through a metering outage while new fine-tuning jobs fail closed. That is fine only if the exposure is explicit. This note gives every PRD one vocabulary to state its failure behaviour in.

## Rule

Every tech spec's failure-handling section classifies each failure by **class** and states its **response** using the terms below. It also says what continues, what stops, what degrades, who is notified, and any exposure limit.

**Failure classes**

| Class | What fails | Default response |
|---|---|---|
| **Admission** | A check before new work starts (feasibility, policy, authority, quota, qualification) | **Fail closed**: nothing new starts |
| **Execution** | Running work (a runtime, node or pod) | **Degrade or contain**, per the owning PRD |
| **Evidence** | Producing or collecting evidence or audit records | Placement actions **wait** (fail closed). Safety actions **proceed**, with evidence back-filled and flagged |
| **Metering** | Usage capture | New fine-tuning GPU jobs **fail closed**. Inference **may fail open** only within a stated maximum unreconciled exposure, after which new paid admission is **suspended** |
| **Authority** | The authorisation source (C) | **Fail closed** for new or disruptive actions. Containment still completes |
| **Containment** | A safety action itself | **Escalate**: page the operator and run the runbook. Never silently delete or relax |

**Response terms**
- **Fail closed:** the action is refused. Running work is unaffected unless the PRD says otherwise.
- **Fail open:** the action proceeds. The gap is recorded, and there must be an exposure limit.
- **Degrade:** the action continues with reduced capability, and that is visible to the people affected.
- **Quarantine:** a resource (pool, endpoint, evidence) is excluded from new use while existing use is kept.
- **Contain:** an active risk is stopped or isolated. The containment policy says how, by severity.
- **Stop:** a workload is brought to zero replicas. It is not deleted.
- **Not offered:** a capability is excluded from selection because it is unqualified. This is not a failure of a running workload.
- **Unverified:** a claim lacks evidence. It is not a failure state ([[Verification Status Vocabulary]]).

**Notification:** each response names who is told (customer, operator, both) and through what (status condition, alert, evidence record).

## Scope

Section 9 (Failure Handling) of every RackAI tech spec, and section 12 (Failure Handling) of every PRD.

## Governs

| Target | Relationship |
|--------|--------------|
| [[Workload Declaration & Placement Tech Spec]] | CONSTRAINS → §9 |
| [[Inference Access & Distribution PRD]] | CONSTRAINS → metering exposure limit |
| [[Fine-Tuning Operations PRD]] | CONSTRAINS → metering fail-closed |

## Enforcement

Applied at review: a spec whose failure table uses a term outside this list, or omits the class, the continue/stop/degrade statement or the notification, is not review-ready (Fitness T-05).

## See Also

- [[Verification Status Vocabulary]]
- [[Release Readiness States]]
- [[Governance Hub]]
