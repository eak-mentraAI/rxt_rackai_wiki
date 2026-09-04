---
id: chg-2026-09-04-openrouter-integration-plan
type: change
status: draft
owner: product
domain: strategy
aliases: [openrouter integration plan change, openrouter merged deliverable change]
related: [idx-openrouter-integration-plan, hub-openrouter, hub-product, ent-openrouter-private-model, ent-openrouter-integration, idx-first-bet-glm, idx-capability-gap-register]
source_docs: [openrouter_concepts_integration_provider, openrouter_strategic_vision.md, openrouter_engineering_roadmap.md, rackai_release_1_0_0, metering_spec, identity_access_spec]
confidence: derived
last_reviewed: 2026-09-04
parent: hub-wiki
summary: "Merged the two OpenRouter reference artifacts into one deliverable with the phased A → quick-wins → public-GLM → AMD-scale sequencing."
---

# 2026-09-04 — OpenRouter Integration Plan

## Trigger

Request: merge the two `reference/openrouter/` artifacts (the concepts/integration/provider source doc and its verified product-owner annotations) into one deliverable, and make the sequencing explicit — pursue the private hosted model first for experience/telemetry/early wins; then target one public model (GLM 5.3 Flash) that fits our limited hardware, is trending, has sufficient token usage, and has strong coding use cases; clear quick wins in one sweep in between; tackle the bigger elements by priority; then, once AMD capacity arrives, evaluate two more models and establish the rapid day-one deployment pipeline.

## Objects Changed

### Added
- [[OpenRouter Integration Plan]] (`idx-openrouter-integration-plan`) — new Layer-5 deliverable under `05-wiki/`. Merges marketplace mechanics (two routing decisions, routing modes, buyer-side fee, price-first routing), the two integration paths (A private / B public), the verified P0/P1 provider requirements with confidence, and the four-phase sequenced plan with an at-a-glance table and open decisions.

### Edited
- [[OpenRouter Initiative]] — added an "Execution Plan" section and a Related entry pointing to the merged plan (inbound link).
- [[Product Hub]] — added an execution-plan line under the First Bet section pointing to the merged plan (inbound link).

## Edges Affected

- `hub-openrouter` → `idx-openrouter-integration-plan` (Execution Plan + Related; inbound).
- `hub-product` → `idx-openrouter-integration-plan` (First Bet section; inbound).
- `idx-openrouter-integration-plan` → existing canonical homes only ([[OpenRouter Private Model Integration]], [[OpenRouter Provider Integration]], [[Model Catalog Endpoint]], [[Billing & Payment]], [[API Key]], [[First Bet — GLM 5.3 Flash]], [[Phase 1 Execution Plan — GLM 5.3 Flash Proof Point]], [[AMD Instinct]], [[Capability Gap Register]], [[Open Questions]]). No new canonical concepts introduced.

## Source Reconciliation

- The `.docx` provided the concept/requirement skeleton; the `.annotations.md` provided the vendor-doc-verified mechanics (routing, fee, streaming, error→uptime map, `/models` schema, Auto Exacto, uptime tiers, Private Models entry criteria, automated-payment gate). Verified mechanics are carried at `measured` where the annotations cite OpenRouter documentation; endpoint conformance (streaming/usage) stays `assumed` until tested. Vendor-doc content rephrased for compliance with licensing restrictions.

## Confidence

- `idx-openrouter-integration-plan` — `derived`. It is a recommended sequencing built from `measured` OpenRouter mechanics applied to shipped-vs-planned platform reality and the fleet topology constraint. No new performance numbers asserted; targets (24h launch, top-five rank) remain `assumed`.

## Open Questions

- None created. The plan consumes existing [[Open Questions]] entries (Path A vs B decision, billing ownership/funding, API Key ship status, AMD MI350P quantity/ETA) and surfaces them as its four Open Decisions rather than adding new ones.

## Crosswalk

- No new source added — `openrouter_concepts_integration_provider` already appears in the [[Source-to-Concept Crosswalk]] and [[Source Inventory]]. This deliverable is a new projection over existing sources, so no crosswalk row is required. (Optional future enhancement: add a crosswalk row mapping the source doc to this plan.)

## Fitness / Consistency Result

- **Structural:** Pass — new files pass `scripts/lint-frontmatter.sh`; `idx-openrouter-integration-plan` unique; all 21 body wikilinks resolve; `related` IDs resolve (fixed `ent-amd-instinct` → `ent-gpu-amd-instinct`); not an orphan (two hubs link in).
- **Story consistency:** Pass — keeps the platform-vs-initiative and Path A vs B distinctions; separates verified (`measured`) mechanics from `assumed` endpoint conformance and targets; surfaces the billing gate and Path decision as open, not smoothed.
- **Layer integrity:** Pass — sits in Layer 5 as a projection over Layer-1 entities and source narratives; references canonical homes without redefining them.

## See Also

- [[OpenRouter Integration Plan]]
- [[OpenRouter Initiative]]
- [[Capability Gap Register]]
- [[Wiki Hub]]

---

## Follow-up (same day) — Path A modeled into the strategy narratives

**Trigger:** rather than flagging that the strategy docs don't model the private-model path, bring the corpus into harmony by modeling Path A directly in them and reflecting it in the merged plan.

**Objects changed:**
- [[Rack AI OpenRouter Strategic Vision]] — added a "Two Entry Paths (sequenced)" section (Path A first, then the Path-B model bets); labeled the three model bets as the Path-B portfolio. `related` extended; `last_reviewed` → 2026-09-04.
- [[Rack AI OpenRouter Engineering Roadmap]] — added an "Entry Sequencing: Path A First, Then the Path B Build" section; retitled "Roadmap Overview" → "Roadmap Overview (Path B build)". `related` extended; `last_reviewed` → 2026-09-04.
- [[OpenRouter Initiative]] — replaced "Path A is the entry the roadmap does not model" with "both paths are now modeled … sequence Path A first."
- [[OpenRouter Integration Plan]] — same stale line replaced with the harmonized framing.
- [[Source-to-Concept Crosswalk]] — added a row mapping Strategic Vision + Engineering Roadmap → the two-paths concept ([[OpenRouter Integration Plan]], [[OpenRouter Private Model Integration]]).

**Edges affected:** `src-strategic-vision` and `src-engineering-roadmap` now relate to `idx-openrouter-integration-plan`, `ent-openrouter-private-model`, `ent-openrouter-integration`.

**Confidence:** source narratives remain `validated` as documents; the Path-A framing added to them is `derived` and cross-links to the `derived` plan. No new performance numbers; targets remain `assumed`.

**Semantic-drift note:** the meaning of the strategy docs widened from "public-provider strategy" to "two-path, Path-A-first strategy." The dependent hub ([[OpenRouter Initiative]]), the plan, and the crosswalk were updated in the same pass so no note still says the paths are unmodeled.

**Fitness:** Pass — lint clean on all touched files; new body wikilinks and `related` IDs resolve; no orphan; conflict framing removed rather than left hidden.

---

## Follow-up (same day) — Executive review hardening

**Trigger:** reviewed the plan through a technical executive's lens and added the checkpoints and answers a funder would demand.

**Objects changed:**
- [[OpenRouter Integration Plan]] — added a **Go / No-Go Gates** table (G1 Path-A dependencies, G2 integration surface proven, G3 price competitiveness, G4 billing funded+owned, G5 AMD capacity) with fail-paths and a note that Phase 2 serving-proxy work is not on the API-key critical path; added an **Executive Q&A — Risks & Mitigations** table (7 concerns); sharpened the Phase 1 outcome to state precisely what Path A validates (integration surface) vs. does not (competitive routing/price/rank) — "integration de-risking, not strategy proof"; extended Open Decisions with the G3 and SPOT-reliability risks.
- [[Open Questions]] — added two entries: price-competitiveness routing gate (G3) and SPOT-capacity reliability vs the >99.9% availability target.

**Edges affected:** plan → [[Cost per GPU-Hour]] (new); Open Questions rows → [[OpenRouter Integration Plan]], [[Cost per 1M Tokens]], [[Cost per GPU-Hour]], [[GLM 5.3 Flash]], [[Availability]], [[Fleet Inventory]].

**Confidence:** unchanged — plan stays `derived`. The gates and Q&A assert no new numbers; G3's price band and the SPOT-reliability question are explicitly registered as `open`, and the economics answer reiterates cost/GPU-hour is `assumed`.

**Open questions created:** two (price-competitiveness gate G3; SPOT-capacity reliability) — both now backing the corresponding go/no-go gates rather than sitting hidden in the plan.

**Fitness:** Pass — lint clean on all touched files; every new wikilink resolves; each new gate is backed by a tracked Open Question (no dangling checkpoints); risks surfaced, not smoothed.

---

## Follow-up (same day) — Source attribution

**Trigger:** the verified OpenRouter mechanics carried `measured` tags but no traceable source in the plan. Add subtle citations to every externally verifiable claim without bloating the prose.

**Objects changed:**
- [[OpenRouter Integration Plan]] — added five markdown footnote references (`[^routing]`, `[^fee]`, `[^private]`, `[^providers]`, `[^residency]`) as inline superscript markers on each externally verifiable claim (routing decisions/modes, buyer-side fee, private-model visibility, the P0/P1 provider requirements table, uptime tiers, compliance flags), and a compact **Sources** section resolving them to OpenRouter's own docs (plus secondary sources for the `derived` fee). Carried the compliance-rephrasing note into Sources. These are the same URLs the `reference/openrouter/` annotations verified against.

**Edges affected:** none in the graph (external URL citations, not wikilinks). Evidence traceability improved per standard S-13 — externally verifiable claims now trace to a named source.

**Confidence:** unchanged — `measured` claims now show their vendor-doc source; the fee stays `derived` (secondary sources; payout terms unverified).

**Fitness:** Pass — all five footnote refs resolve to definitions (no orphans); lint clean; no consecutive-verbatim reproduction (claims paraphrased, ≤30 words per source).
