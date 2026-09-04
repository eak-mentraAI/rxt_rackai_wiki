---
id: src-identity-access-spec
type: source
status: reviewed
owner: platform-eng
domain: governance
aliases: [iam spec, identity prd, access control tech spec, rbac spec]
related: [hub-rackai-platform, src-rackai-api-reference]
source_docs: []
confidence: derived
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI Identity & Access Control PRD + technical spec (auth, orgs, RBAC, API keys)."
---

# Identity and Access Control Spec

## Provenance

- Origin: `reference/rackai-platform/PRD - Identity & Access Control.docx`, `Identity_Access_Control_TechSpec.docx`
- Classification: planning / architecture

## Summary

Defines RackAI's identity and access model: OIDC-based authentication (Auth0, with a Keycloak path), organization/tenant scoping mapped to Kubernetes namespaces, RBAC roles/permissions, and **API keys** for programmatic access. API-key support is the primary dependency for the [[OpenRouter Initiative]] Path A (private models). Full RBAC roles and fine-grained permissions are largely **planned** beyond the read-access RBAC shipped in 1.0.0.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Identity & access control | [[Identity & Access Control]] | L2 |
| Organization / tenancy | [[Organization]] | L1 |
| API keys | [[API Key]] | L1 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
