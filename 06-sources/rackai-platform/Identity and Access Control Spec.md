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
last_reviewed: 2026-10-10
parent: hub-rackai-platform
summary: "Source: RackAI Identity & Access Control PRD + tech spec with as-built deltas (Keycloak, orgs, RBAC, API keys)."
---

# Identity and Access Control Spec

## Provenance

- Origin (current): `reference/PRD/Identity_Access_Control_TechSpec.docx` (received 2026-10-10) — supersedes the rackai-platform copy of the tech spec; same header (v0.2, Draft, created 04/05/2026) but adds dated AS BUILT / PROPOSED-NOT-BUILT annotations (2026-09-14, 2026-09-18).
- Origin (prior, ingested 2026-09-04): `reference/rackai-platform/PRD - Identity & Access Control.docx`, `Identity_Access_Control_TechSpec.docx`. The PRD is unchanged in `reference/PRD/`.
- Classification: planning / architecture, with as-built annotations

## Summary

Defines RackAI's identity and access model: OIDC/JWT authentication via per-realm Keycloak (with SAML federation to Rackspace's Astra for staff; Auth0 is the legacy provider being cut over and decommissioned), a four-tier scope hierarchy (platform → CustomerOrg → Organization/tenant → Project) mapped to Kubernetes namespaces, RBAC via `PlatformRole` + `RoleBinding` CRDs, and **HMAC-validated API keys** for programmatic access. API-key support is the primary dependency for the [[OpenRouter Initiative]] Path A (private models).

As of the 2026-09-14 annotations, the IAC M1 core is **built**: the Authorization Service (Envoy ext_authz) evaluating RoleBindings, the CustomerOrg/Organization/RoleBinding CRDs and admission webhooks, and scope-constrained realm validation. Built behaviour diverges from the original design in places — see As-Built Deltas. Multi-CustomerOrg operation ships gated off, and the CustomerOrg→billing-account link is proposed only.

## As-Built Deltas (spec revisions through 2026-09-29)

Source: annotations in the 2026-10-10 copy of the IAC tech spec (v0.2). Shipped behaviour takes precedence over the original design text.

- **`Organization.spec.orgRef` removed (AS BUILT 2026-09-14).** Organization is now a *namespaced* CRD living in its owning CustomerOrg's namespace; `metadata.namespace` is the ownership record. `spec.orgRef`, its validations, controller backfill, and the `customer-org` label are deleted. Driver: a cluster-scoped resource cannot be scoped per customer in Kubernetes RBAC, so org-admins could not manage their own tenants. Migration was delete-and-recreate.
- **Creation path is a real namespaced path.** `POST /namespaces/{customer-org}/organizations` places the object in that namespace; the gateway rewrite and two Envoy Lua filters that forced orgRef to match are deleted. The webhook rejects a `{customer-org}` that is not an existing CustomerOrg.
- **Org lookup by name is a LIST.** The evaluator resolves a tenant's CustomerOrg via a cached `OrganizationNameIndex` (webhooks use a field selector; the RoleBinding controller filters in Go). More than one match fails closed (503).
- **Global tenant-name uniqueness (AS BUILT, not in original design).** Because tenant name derives the workload namespace and Keycloak realm, the Organization webhook enforces uniqueness across CustomerOrg namespaces; without it namespacing would have allowed cross-tenant collision.
- **Second authorization layer (§7.5, AS BUILT, load-bearing).** A request allowed by the ext_authz evaluator (layer 1) is forwarded to the inner `rackai-apiserver`, which applies Kubernetes RBAC to the bridged identity (`X-Remote-User`/`X-Remote-Group`). Both must allow. `rbac.k8sGrants.enabled` is required whenever `rbac.enforcement.mode=enforce`, else everyone (including platform admins) is denied. Staff reach cluster-scoped resources via an `aurora-system` bridge-group override. Authoritative grant list lives in the code repo (`docs/operations/rbac.md`).
- **Single-CustomerOrg guard is gated, not removed.** `rbac.multiOrg.enabled` (default off) lifts the "one CustomerOrg" 422; reserved-name and uniqueness checks stay unconditional. Ships inert; not enabled on any long-lived deployment.
- **CustomerOrg deletion cascades (SUPERSEDED the "blocked if referenced" rule, 2026-09-14).** Deleting a CustomerOrg deletes its namespace and each tenant (finalizers emit audit, deprovision realm and namespace). Cascade kept by operator decision; the cascade stamps every tenant with the CustomerOrg's deleter and request ID so offboarding is one auditable operation. Risk: a stuck tenant finalizer hangs the CustomerOrg; force-removing it skips the audit event and leaks the realm.
- **`CustomerOrg.status.tenantCount` NOT BUILT** (and may not be needed — a namespaced list gives the count).
- **`CustomerOrg.spec.cmsAccountId` — PROPOSED 2026-09-18, NOT BUILT.** The Rackspace Customer Number (RCN) a CustomerOrg bills to; today nothing maps a CustomerOrg to anything invoiceable. Proposal: required on create when multi-org is on, immutable once set, seeded on sovereign installs from Helm `rbac.defaultOrg.cmsAccountId` (sourced from the cloud-environments record), deliberately kept out of realms/JWTs (joined at billing-query time).
- Unchanged: scope-constrained realm validation for tenant/project RoleBindings is resolved and built (now derives the CustomerOrg from `org.Namespace`).

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Identity & access control | [[Identity & Access Control]] | L2 |
| Organization / tenancy | [[Organization]] | L1 |
| API keys | [[API Key]] | L1 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
