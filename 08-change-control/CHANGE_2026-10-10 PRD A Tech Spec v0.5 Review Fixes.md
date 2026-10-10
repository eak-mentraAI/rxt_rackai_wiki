---
id: chg-2026-10-10-prd-a-spec-v05-review-fixes
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd a spec v0.5, placement spec code review fixes]
related: [spec-workload-declaration-placement, prd-workload-declaration-placement]
source_docs: ["/code-review of 05-wiki/Workload Declaration & Placement Tech Spec.md at e1ae63f, 2026-10-10"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "PRD A tech spec v0.5: nine code-review fixes on top of v0.4; DV-7 and the MOE-0 TTL gate product-approved."
---

# CHANGE 2026-10-10 — PRD A Tech Spec v0.5 (Review Fixes)

## Trigger

A `/code-review` of the published [[Workload Declaration & Placement Tech Spec]] (`e1ae63f`) found ten defects. The product owner asked for them to be fixed.

## What Changed

The fixes are applied on top of v0.4 (commit `e63a578`, not yet pushed) on the local branch `spec-a-review-fixes`, so they don't conflict with v0.4. Finding 1 (§4.6, §4.6.1 and §4.7 missing) was already fixed in v0.4 (A4-13). The other nine are listed in the spec's new §0.2 (R5-1 to R5-9):

- **R5-1:** a stable violation ID, computed from the observed failing values instead of the node's `resourceVersion`.
- **R5-2:** safety decisions get their own slot and pre-empt a placement commit before stage 4.
- **R5-3:** the policy digest uses the effective generation.
- **R5-4:** the evaluation decision ID is aligned with Appendix A.
- **R5-5:** in-flight commitments cover only unbound replicas and are released when a replica is bound or reported unschedulable.
- **R5-6:** the fit check places at least one replica.
- **R5-7 / DV-7:** a new `Contained` phase. **Material; approved by the product owner 2026-10-10.**
- **R5-8:** objects are archived to the audit store, and their finalizers released, at retirement or namespace termination.
- **R5-9:** policy-owned chart values are required only for enabled features, and MOE-0 needs an approval TTL (C's value, or an explicit rehearsal-only value). **Material; approved by the product owner 2026-10-10.**

Tests for each fix were added to §12, and §9, §10, §13.0 and Appendix A were updated. The original design text is noted in each row rather than silently rewritten.

## Checks

Frontmatter lint, the PRD/spec lint and the broken-link check pass. **Product approval:** the product owner approved DV-7 and R5-9 on 2026-10-10 ("approve DV-7 and R5-9"). Engineering approval is still pending.

## Open Questions

- Pushed together with v0.4 (`e63a578`) from the Knowledge Platform session after merging `origin/main`, at the product owner's instruction (2026-10-10).
