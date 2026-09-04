---
id: src-monitoring-audit-spec
type: source
status: reviewed
owner: reliability
domain: reliability
aliases: [monitoring prd, platform monitoring tech spec, observability spec, auditability spec, compliance spec]
related: [hub-rackai-platform, src-rackai-release-1-0-0]
source_docs: []
confidence: derived
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI Monitoring + Auditability PRDs and technical specs (platform + tenant observability, audit)."
---

# Monitoring and Auditability Spec

## Provenance

- Origin: `reference/rackai-platform/PRD - Monitoring.docx`, `Platform_Monitoring_TechSpec.docx`, `PRD - Auditability and Observability.docx`, `Auditability_Compliance_TechSpec.docx`, `InTenant_Observability_TechSpec.docx`
- Classification: planning / architecture

## Summary

Two related concerns:

- **Platform monitoring** — operator-facing telemetry (Prometheus scrape targets incl. kube-state-metrics, AMD GPU, kubelet/cAdvisor; a `rackai-monitoring` Helm chart shipped in 1.0.0). This is the operator view.
- **In-tenant observability & auditability** — tenant-facing metrics, logs, and an immutable **audit** trail. These are **planned/draft**, not shipped.

Compliance: the specs describe aspirational controls (immutable audit, OIDC/RBAC/mTLS) but make **no concrete HIPAA/SOC2/GDPR/zero-data-retention claims** — relevant to the [[OpenRouter Initiative]] "declare compliance per model" requirement, where we currently can declare little.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Monitoring / observability | [[Monitoring & Observability]] | L2 |
| Audit trail | [[Audit]] | L2 |
| Operator telemetry (shipped) | [[Productive GPU Utilization]] and fleet metrics | L2 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
