---
id: chg-2026-09-04-capability-gap-register
type: change
status: draft
owner: product
domain: strategy
aliases: [capability gap register change, gap register change]
related: [idx-capability-gap-register, hub-evidence, idx-open-questions, idx-kpi-hierarchy, hub-rackai-platform]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md, rackai_platform_prd, rackai_release_1_0_0, metering_spec, identity_access_spec, monitoring_audit_spec]
confidence: derived
last_reviewed: 2026-09-04
parent: hub-wiki
summary: "Added the Capability Gap Register: a capability-vs-goal matrix of what's missing to reach the strategic project-level goals."
---

# 2026-09-04 — Capability Gap Register

## Trigger

Analysis request: given the shipped state of the platform, what capabilities are missing to reach the **strategic project-level goals** — the whole project, not just the OpenRouter initiative. The finding was captured as a tracked evidence-layer index rather than a one-off answer.

## Objects Changed

### Added
- [[Capability Gap Register]] (`idx-capability-gap-register`) — new Layer-4 index under `04-evidence/`. A capability-vs-goal matrix across five goal areas: commercial/unit-economics, performance & evidence (ground truth), model velocity, dynamic fleet allocation, and platform-product completeness. Each required capability carries a state (`shipped`/`partial`/`planned`/`missing`), a confidence, and a link to its [[Open Questions]] entry where one exists.

### Edited
- [[Evidence Hub]] — added the Capability Gap Register to the Registers list (inbound link; resolves orphan risk).

## Edges Affected

- `hub-evidence` → `idx-capability-gap-register` (Registers listing; inbound).
- `idx-capability-gap-register` → existing canonical notes only (Billing & Payment, Metering, Cost per GPU-Hour, KPI metrics, routing/admission/reallocation, tenancy features, source narratives). No new canonical concepts introduced; the register links to homes, it does not redefine them.

## Confidence

- `idx-capability-gap-register` — `derived`. Gaps are traced from documented shipped-vs-planned status and the [[Open Questions]] register; no telemetry confirms the shipped side performs to goal. No new performance numbers asserted.

## Open Questions

- None created. The register consumes existing [[Open Questions]] entries (billing P0, API Key ship status, RL/DPO, cost model, hardware fit, etc.) rather than adding new ones. It also records the standing caveat that no dedicated platform-whole OKR document exists — platform-level goals are inferred from [[RackAI Platform]] plus the initiative narratives.

## Fitness / Consistency Result

- **Structural:** Pass — new file passes `scripts/lint-frontmatter.sh`; `idx-capability-gap-register` is unique; all 29 wikilinks resolve to existing notes; not an orphan (Evidence Hub links in). (Pre-existing `reference/` lint errors are unrelated raw source material.)
- **Story consistency:** Pass — separates shipped from planned/missing honestly; targets kept distinct from results (all remain `assumed`); surfaces the billing non-goal conflict rather than smoothing it; keeps the platform-vs-initiative distinction.
- **Layer integrity:** Pass — sits in Layer 4 (evidence) as an index; references canonical homes without redefining them; no layer bypass.

## See Also

- [[Capability Gap Register]]
- [[Evidence Hub]]
- [[Open Questions]]
- [[KPI Hierarchy]]
