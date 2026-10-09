---
id: chg-2026-10-09-roadmap-moscow-narratives
type: change
status: draft
owner: product
domain: strategy
aliases: [roadmap moscow change, roadmap narratives change 2026-10-09]
related: [wiki-roadmap-narratives, hub-roadmap, wiki-milestone-release-map, hub-minimum-operable-estate, idx-fleet-inventory, wf-model-launch-factory, met-model-launch-lag]
source_docs: ["05-wiki/RackAI Roadmap.csv", "00-hub/RackAI Roadmap.md", "05-wiki/Milestone Release Map.md"]
confidence: derived
last_reviewed: 2026-10-09
parent: hub-wiki
summary: "Added MoSCoW and Narrative columns to the roadmap CSV, plus a Roadmap Narratives note with a demo-to-production rule."
---

# 2026-10-09 — Roadmap MoSCoW and Narratives

## Trigger

Product owner request: add a **MoSCoW** rating to the roadmap, and group the engineering milestones into **business narratives**. The problem it addresses: FDE proofs of concept are fast and visible, so leaders see their speed but not that they aren't production-ready. That puts pressure on product teams whose slower, less visible work is what makes outcomes production-ready.

## Objects Changed

- **Changed:** `05-wiki/RackAI Roadmap.csv`: two columns appended, `MoSCoW (6-month horizon)` and `Narrative`, on all 74 rows (28 Must, 16 Should, 11 Could, 19 `Won't (this horizon)`). The header and value spell out the horizon so the column can't be read as "never" out of context. No existing cell changed.
- **Added:** `05-wiki/Roadmap Narratives.md` (`wiki-roadmap-narratives`, type `index`, `derived`). Defines MoSCoW against the six-month horizon and the MOE-1 gate; groups the rows into eight narratives (N1 *Tell Us the Outcome. We Run It.*, N2 *Your AI, Your Rules*, N3 *No Surprises*, N4 *Smarter With Every Workload*, N5 *Your Models, Operated* (renamed same day from *Any Model, Day One*), N6 *Price-Performance Without Lock-In*, N7 *Solutions, Ready to Run*, N8 *Built to Scale Profitably* (internal)); shows each narrative's production bar; proposes a demo-to-production rule (Demo / Pilot / Production labels).
- **Added (same day):** a *Market unlocks* section in [[Roadmap Narratives]]. Business impact is stated as markets unlocked (who can buy, against which customer alternative), never as price, per-token or revenue claims, until N8 is measured. It proposes MOE-2 (repeat in segment), MOE-3 (residency and multi-region) and MOE-4 (operate on customer supply), each adding back one MOE-1 exclusion. These are proposed only; an open question is added to [[Minimum Operable Estate]], their canonical home if ratified.
- **Changed (same day):** a third CSV column, `MOE gate`, assigns every row to the earliest gate it is needed for (MOE-0 20 rows, MOE-1 13, MOE-2 9, MOE-3 2, MOE-4 5, Beyond MOE-4 4, Not gated 21). The *Market unlocks* section of [[Roadmap Narratives]] became *MOE gates: the market each one unlocks*. The consistency check found: the supply-abstraction interface is rated Should but required by the MOE definition; MOE-3 lacks residency-control and compliance rows; none of MOE-1's rows have started.
- **Changed (same day, product owner decision):** *Supply-abstraction interface* upgraded Should → Must (the MOE v1 definition requires it; P-004). **Added** three unstaffed MOE-3 rows: *Data-residency controls* (T2.S5), *Residency-aware placement and failover* (T1.S4), *Per-jurisdiction compliance evidence* (T2.S5), all N2 and `Won't (this horizon)`. The CSV now has 77 rows: 29 Must, 15 Should, 11 Could, 22 Won't.
- **Changed (same day, review pass; no new initiatives, narratives or frameworks):**
  - **MOE-1 acceptance logic** made non-circular. Capabilities are operational and the evidence contract + reporting mechanism are validated *before* acceptance; the first completed report is the acceptance *output*; Proof 3 passes with a paying customer, delegated responsibility and agreed evidence. MOE-1 claims a *defined initial customer profile* and a *bounded* estate; ICP-wide repeatability moves to MOE-2. Canonical in [[Minimum Operable Estate]] (Exit Condition), mirrored in the CSV MOE-1 and evidence-report rows.
  - **Must reasons tagged** in the CSV discussion field: `[Gate-critical]` 24, `[Evidence-critical]` 6, `[Commitment-critical]` 2 (two rows carry two tags).
  - **Production rule tightened:** Production = required Musts done + the applicable MOE gate passed + operating and commercial boundaries written down. Pilot = named scope, explicit constraints, accountable operator. A demo proves technical possibility, a pilot tests customer fit, and production proves operational responsibility under an enforceable contract, evidencing both identity centres.
  - **Claims matched to proof:** N2 distinguishes the agreed private boundary (MOE-1) from residency in specific jurisdictions (MOE-3). *First compliance attestation (SOC 2)* renamed **First applicable assurance attestation** in the CSV, [[RackAI Roadmap]] and [[AI Governance and Assurance]]. N3 promises visibility and enforced limits, not cost outcomes. N4 improves as evidence accumulates. N6 is architectural readiness this horizon. N7 is prototype stage. The audit status wording separates the shipped foundation from pending extended controls.
  - **Empirical Map acceptance:** improvement is defined in advance on the same baseline workload (SLO attainment, cost efficiency, constraint compliance, decision quality, thresholds fixed first). *Evidence-backed* recommendations are distinguished from *empirically validated* ones.
  - **N5 renamed** *Any Model, Day One* → **Your Models, Operated** (code N5 unchanged).
  - **Not applied:** the review's claim that MOE-1 rows were in progress; all 13 are Not started in the CSV.
- **Changed:** [[RackAI Roadmap]]: one pointer under "Which file is current", one See Also link, and `related`. No meaning change to the proofs or P-items.
- **Changed:** [[Milestone Release Map]]: the marketing guidance now points to [[Roadmap Narratives]]; the five tracks remain the engineering view. See Also and `related` updated.
- **Deprecated:** none.

## Knowledge platform rendering (same day)

The roadmap CSV never appeared on the knowledge platform: ingestion only discovered `.md` files and its CSV parser was never called. Fixed in knowledge-platform PR #21 (opt-in `data_files` frontmatter; each declared CSV renders as a filterable, sortable table on the note's page and is indexed for semantic search). Wiki side:

- `data_files` added to [[RackAI Roadmap]] (`05-wiki/RackAI Roadmap.csv`) and [[Fleet Inventory]] (`04-evidence/benchmarks/fleet-inventory.csv`).
- Optional `data_files` field documented in the frontmatter standard (`.kiro/steering/rackai-operating-standards.md`).
- **Data fix:** `fleet-inventory.csv` row 1 had an unquoted interconnect value containing commas, which split one field into three (11 fields under 9 headers). Quoted it; values unchanged.

## Model velocity (same day)

Question: does the roadmap let us adopt new models and new versions quickly, benchmark them, and stay competitive? Finding: the [[Model Launch Factory]], [[Benchmark Evidence Chain]] and [[Canary & Rollback]] were designed but not funded. The factory was `Won't (this horizon)`, new-model support was a ServiceNow request, benchmarking was blocked on SLO thresholds, CI lacked model images, and there was no path for upgrading a served model to a new version. Changes (product owner decision; no new narrative or framework):

- **CI system** (Must): scope now explicitly includes building and releasing model-serving and fine-tuning images.
- **M2: Request new model support** (RACKAI-354): **rescoped (proposed, confirm against Jira)** to a human-gated onboarding pipeline v0 for known architectures (intake → functional validation → benchmark → canary). Proof 4 → Proof 2, MOE-2 → MOE-1, still Should. Jira, owner and due date unchanged.
- **Added:** *Model version upgrade (canary rollout)* (T1.S3, Should, N5, MOE-1) and *Model Launch Lag instrumentation* (T3.S1, Should, N5, MOE-1), both unstaffed.
- **Annotated:** AI Performance Benchmarks and Per-profile SLO thresholds (SLO ratification unblocks the onboarding benchmark gate); the day-zero factory row (its middle is pulled forward).
- **Upgraded to Must (product owner, same day):** the onboarding pipeline v0 (RACKAI-354) and *Model version upgrade*, both `[Gate-critical]` at MOE-1. MOE-1 now has 10 Musts; the CSV has 31 Must, 15 Should.
- **Propagated:** [[Roadmap Narratives]] (N5, gate table: MOE-1 now 16 rows), [[RackAI Roadmap]] delivery table, [[Model Launch Factory]] and [[Model Launch Lag]] (roadmap-status callouts). The CSV now has 79 rows: 29 Must, 17 Should, 11 Could, 22 Won't.

## Browse tree fix (same day)

The knowledge platform's Browse tree showed none of the RackAI wiki. Cause: the root note [[Rack AI Knowledge Base]] (`hub-root`) declared `parent: hub-root`, making it its own parent; it had done so since the initial import. Browse builds its tree from parentless notes, so `hub-root` and everything under it (238 of 259 objects) was unreachable. Set `parent: null`, matching the AIOS wiki's root. A simulated rebuild shows all 259 objects reachable, with no other cycles.

## Dates and owners refreshed (same day)

Refreshed `Due`, `Release date (post-eng meeting)`, `Potential owner` and `Jira` in `05-wiki/RackAI Roadmap.csv` from the product owner's updated plan, matched by milestone; no other column changed. Due dates were set on all 74 matched rows (10/20/2026 to 9/15/2027); 21 release dates were filled in; 4 owners changed (AI Performance Benchmarks, Speculative decoding and Refrag: Alberto/Deshna → Deshna; DPO fine tuning: unassigned → Deshna); Jira already matched. The five rows added today have no dates or owners yet.

## One date per row (same day)

`Release date (post-eng meeting)` was replaced by `Date status` in `05-wiki/RackAI Roadmap.csv` (same column position). Every filled release date equalled its `Due`, so the column only signalled engineering confirmation. Now: **Committed** for the 21 rows that had a release date, **Target** for 53 with only a Due date, blank for the 5 undated rows added today. No dates lost: `Due` is unchanged. Documented under *Maintaining* in [[Roadmap Narratives]].

## Edges

- **Added:** hub-roadmap → wiki-roadmap-narratives; wiki-milestone-release-map → wiki-roadmap-narratives; wiki-roadmap-narratives → hub-roadmap (parent), Minimum Operable Estate, Empirical Map, Solution Marketplace, Sovereign Private Assistant, Team Operating Model, Capability Gap Register.
- **Removed:** none.

## Confidence Changes

None. Ratings and narrative names are `derived` and marked **proposed** pending PM ratification. No capability is upgraded to shipped.

## Open Questions

- Ratify the MoSCoW ratings (flagged: Workload declaration = Must; Concierge Engineer v0 = Should; Authority under incomplete intent = Should).
- N6 has no Must rows this horizon, so "no lock-in" can't yet be claimed externally. Confirm this is intended.
- Ratify MOE-2 to MOE-4 and their order.
- Which jurisdictions the MOE-3 residency rows target (depends on the MOE-3 markets).
- Narrative names are working titles for marketing to refine; the N1–N8 codes stay stable.
- Whether Craft.io gets MoSCoW and Narrative fields (if so, Craft.io holds the value and the CSV mirrors it).
