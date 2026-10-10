---
id: chg-2026-10-09-why-now
type: change
status: draft
owner: product
domain: strategy
aliases: [why now change, why now 2026-10-09]
related: [hub-why-now, evd-compute-supply-sovereign-demand-2026, asm-dc-capacity-available, ent-gpu-amd-instinct, hub-battlegrounds, hub-evidence, idx-assumption-register]
source_docs: ["product owner direction (2026-10-09)", "web research 2026-10-09"]
confidence: derived
last_reviewed: 2026-10-09
parent: hub-wiki
summary: "Added a sourced Why Now argument: compute and power scarcity, sovereign demand, MI350P capacity, DC space."
---

# 2026-10-09 — Why Now

## Trigger

Product owner direction for the leadership deck: add a why-now moment. Demand continues to outpace supply; Rackspace has a large fleet of power-efficient, cost-effective MI350P and underused datacenter space; combined with the long-term identity as a private/sovereign provider and operator, the timing makes sense. Research it and add canonical notes.

## Objects Changed

- **Added:** [[Why Now]] (`hub-why-now`, hub, `assumed`, parent [[Three Battlegrounds]]). Four conditions, each with its evidence, confidence and what would weaken it; why the moment favours an operator rather than a GPU cloud; claim rules; falsifiers; open questions.
- **Added:** [[AI Compute Supply and Sovereign Demand 2026]] (`evd-compute-supply-sovereign-demand-2026`, evidence, `derived`). Sourced, dated external evidence: compute demand vs supply, power and space as the gate, sovereign demand, and counter-evidence (falling GPU-hour prices, overbuild warnings). Secondary-only items are marked for checking before external use.
- **Added:** [[Underused Datacenter Capacity Available]] (`asm-dc-capacity-available`, assumption, `assumed`, owner infrastructure), registered in the [[Assumption Register]].
- **Changed:** [[AMD Instinct]]: three vendor-spec rows (power and cooling, memory, compute), labelled as AMD figures, plus a note that B1 confirms them and no independent benchmark exists.
- **Changed:** [[Three Battlegrounds]] and [[Evidence Hub]]: links and `related`.

## How the Product Owner's Statement Was Recorded

| Statement | Recorded as | Why |
|-----------|-------------|-----|
| Demand continues to outpace supply | `derived`, with counter-evidence | Strong primary and third-party evidence; commodity GPU-hour prices falling is a real counter-signal |
| A large fleet of MI350P | Deployed (operator-reported); quantity open | The corpus records a "large order"; quantity is decision D4 |
| Power-efficient | AMD's power envelope only (600 W, air-cooled) | No performance-per-watt measurement exists |
| Cost-effective | Belief, via [[MI350P Serving Competitive]] C3 | Needs the cost model and B5; impact rule bars economics claims until then |
| Underused DC space | New assumption, no figure | No site or MW data in the corpus |

## Edges

- **Added:** hub-why-now → hub-battlegrounds (parent), evd-compute-supply-sovereign-demand-2026, asm-dc-capacity-available, asm-mi350p-serving-competitive, ent-gpu-amd-instinct; reverse links from Three Battlegrounds, Evidence Hub and AMD Instinct.
- **Removed:** none.

## Confidence Changes

None upgraded. The new hub is `assumed` because two of its legs are.

## Open Questions

- MI350P quantity and per-node topology (D4).
- Per-site record of underused DC space.
- Whether the available space matches the MOE-3 target jurisdictions.
