---
id: chg-2026-10-06-smp-prd-v2
type: change
status: draft
owner: product
domain: product
aliases: [solution marketplace prd v2, prd eng review incorporation]
related: [prd-solution-marketplace, ent-solution-marketplace, ent-packaged-solution, wiki-milestone-release-map]
source_docs: ["05-wiki/Solution Marketplace PRD.md", "PM/eng-arch PRD review 2026-10-06"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Folded Eng/Arch review into the Solution Marketplace PRD: manifest, two-layer trust, lifecycle FRs, metric ladder."
---

# 2026-10-06 — Solution Marketplace PRD v2 (Eng/Arch Review Incorporation)

## Trigger

Eng/Arch review rated the PRD ~8/10 and ready for initial review, with six substantive tightenings before it becomes committed roadmap work. All incorporated. Review's central theme — *prove one reusable solution before extracting the generic contract* — matches the corpus "operate before automate" ladder, so it drove a phasing re-sequence as well as content.

## Objects Changed — all in [[Solution Marketplace PRD]]

1. **Capability/Permission Manifest = the central primitive.** New lead-in + FR-1/FR-2/FR-3: a solution ships a manifest declaring models/data/network/tools/secrets/resources/identity/telemetry; it is the contract linking **SDK → certification → customer approval → runtime enforcement → audit**, enforced at runtime.
2. **Two-layer trust (split certification).** FR-8 **package certification** (artifact trusted) vs FR-8a **instantiation validation** (this solution + these bindings + this estate valid against estate policy). Proposition rewritten: *package once, certify the artifact once, validate each instantiation.* ("Certified once" was too strong given customer-bound models/data.)
3. **Binding policy (loosened FR-10).** New *Binding policy* subsection + FR-2/FR-11: each model/data dependency is **fixed / constrained / customer-bindable**, declared in the manifest. Replaces the old "every instantiation binds the customer's own models and corpus" (over-constrained — some solutions need a specific model/adapter/embedding).
4. **Solution lifecycle & maintenance (new FR group).** FR-14–21: independent versioning; estate↔version tracking; version↔platform compatibility; author-publishes-without-mutating-instances; **revocation/emergency disable that reaches running instances** (distinct from catalog delisting); deprecation/EOL; retired-model behavior. This was the largest functional hole.
5. **Metric ladder (strengthened §9).** Replaced the single re-instantiation ratio with: marketplace **leverage** (production instances ÷ solutions) · **adoption** (% eligible estates) · **consumption** (workload attributable) · **FDE delivery leverage** (hours for the Nth estate vs the first — the headline, directly testing §2) · **operating leverage** (workloads/Ops FTE, now separated from delivery effort) · moat instrumentation · trust bar.
6. **Prototype-first phasing (§8).** Re-sequenced: **MK.S0** reference prototype (smallest convention) → **MK.S1** extract the standard → **MK.S2** two-layer trust gate → **MK.S3** lifecycle + second solution → **MK.S4** surface → **MK.S5** third-party. Explicitly reverses the old "SDK → certification → reference solution" order.
7. **Open Decisions.** Added **D-0** (what is the minimum reusable unit that qualifies as a Packaged Solution — gates everything; FR-4's definition is only the hypothesis, S0/S1 discovers it) and **D-6** (upgrade behavior: auto / admin-approved / author-controlled).
8. **Risks** updated to prototype-first + FDE-delivery-leverage framing.

- **Also changed:** [[Milestone Release Map]] — marketplace capability-stage table re-sequenced to MK.S0-first to match the PRD.

## Edges

- **Added:** PRD → [[Model Class]] (constrained binding), reinforced links to [[Metering]], [[Agent Identity]], [[AI Governance and Assurance]]. Release map ↔ PRD phasing kept in sync.
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| prd-solution-marketplace | assumed | assumed | Deepened spec for a still-proposed initiative; no capability built. |

No performance numbers asserted. Metric baselines remain zero/none; the ladder names *postures*. FR-count grew 15→24 (+ FR-8a); none asserts a shipped capability.

## Open Questions / Decisions

- **Created:** D-0 (minimum reusable unit — now the gating decision), D-6 (upgrade behavior). The capability manifest + two-layer trust also sharpen D-2 (the bar now explicitly covers both package certification and instantiation validation).

## Downstream Propagation Check

- **Dependent notes updated?** Release map re-synced. The [[Solution Marketplace]] and [[Packaged Solution]] *entities* were checked — their definitions still hold (the manifest/binding/lifecycle detail is PRD-level requirement depth, not a redefinition of the entity); the entity's lifecycle-states remain consistent with the new phasing. No entity edit required.
- **Canonical IDs/aliases preserved?** Yes.
- **Formulas/metrics/coefficients/scorecards?** The metric ladder names product metrics (delivery leverage, adoption) that are **PRD-local success measures**, not new canonical [[Metric Index|Metric]] notes; if any graduate to tracked metrics they'd get canonical homes then. None created now.
- **Source-to-Concept Crosswalk?** No new source concept — same 2026-10-06 initiative, deeper spec; logged here.
- **One-Concept / layer purity?** Held — PRD projects from the entities; manifest/binding/lifecycle are requirements, not competing definitions.

## Fitness / Consistency Result

- Structural: **Pass** — all PRD wikilinks resolve; FR ids FR-1…FR-24 (+FR-8a) and D-0…D-6 coherent; stale FR-6/6a certification reference corrected to FR-8/8a.
- Consistency: **Pass** — PRD phasing (MK.S0-first) matches the [[Milestone Release Map]]; proposition, risks, metrics, and open decisions all reference the renumbered FRs; prototype-first is consistent with the roadmap "operate before automate."
- Confidence propagation: **Pass** — `assumed` throughout; no capability upgraded.
- Regressions: none.

## See Also

- [[Solution Marketplace PRD]] · [[Solution Marketplace]] · [[Packaged Solution]]
- [[Milestone Release Map]]
- [[Wiki Hub]] · [[CHANGE_PACKET]]

---

# 2026-10-06 (addendum) — PRD v2 polish (second review pass)

Five surgical fixes from the second Eng/Arch pass; the reviewer called the PRD a credible discovery-stage document and advised stopping after these. All in [[Solution Marketplace PRD]].

1. **§2 stale claim fixed** — "packaged to a standard, certified once, and instantiated many times" → "packaged to a standard, **certified as a reusable artifact, and safely validated and instantiated across many estates**." Removes the re-introduced "certified once" the two-layer trust model had corrected elsewhere. (Remaining "certified once" strings are deliberate — the proposition callout and FR-8a both *critique* it.)
2. **FR-13 SHOULD → MUST** — repeatable instantiation across compatible estates **without modification to the packaged artifact**. It is the marketplace thesis, not a nice-to-have; the "without modification" clause prevents satisfying "repeatable" by editing the package each time.
3. **Default-deny invariant added** (after the manifest facet table) — *a Packaged Solution gets no access to models/data/tools/secrets/network/actions unless declared in its manifest and approved for the target estate.* Elevates the manifest's "network default none" into a marketplace-wide security principle: **declare → certify → approve → enforce → audit**.
4. **FR-18 split** — **FR-18 platform security revocation** (RackAI immediately prevents execution when certification/security integrity is invalidated) vs **FR-18a operational withdrawal/deprecation** (author bug / EOL / customer-initiated — follows notification + change-management policy, owned by the [[AI Operations Product]] responsibility model). Separates "who may kill a customer's production workload, and under what authority."
5. **§10 FDE dependency reworded** — "AI Operations Product supplies the first authors" → "**FDE supplies the first authors and reference solutions; [[AI Operations Product]] defines the operating/handoff model**." Preserves the boundary (FDE is its own delivery capability; AIOps owns the operating model, not FDE itself).

**Confidence:** unchanged (`assumed`). **FR count:** +FR-18a. **Links:** all resolve. **Consistency:** FR-13 MUST aligns with the §2 thesis; FR-18/18a authority split ties to D-6 and AIOps; default-deny consistent with the manifest + isolation NFR. No capability upgraded; nothing else propagates.
