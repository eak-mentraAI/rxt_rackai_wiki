---
id: wiki-team-operating-model
type: hub
status: draft
owner: product
domain: strategy
aliases: [team operating model, operating cadence, team governance, how we work, team meetings, roadmap process, communication model]
related: [wiki-pillar-working-model, hub-org-design, hub-roadmap, hub-battlegrounds]
source_docs: ["05-wiki/Pillar Working Model.md", "00-hub/RackAI Organizational Design.md"]
confidence: derived
last_reviewed: 2026-09-24
parent: hub-org-design
summary: "How the RackAI product team operationalizes one strategy: ownership, empowerment, cadence, and communication."
---

# RackAI Team Operating Model

This document answers a specific question: **how does a team organized into six pillars execute one coherent strategy without either fragmenting into six independent programs or creating a coordination tax so high that people stop collaborating?**

It covers who is empowered to decide what, how we meet and why, how roadmap updates are created and shared, and who owns communication between pillars. It is a companion to the [[Pillar Working Model]], which defines the *what* of each pillar's scope. This document defines the *how* of operating as one team.

---

## The Governing Principle

> **One strategy. Executed by the right people. Communicated without drowning anyone.**

The SVP sets and owns the singular strategy for RackAI — the Private Enterprise AI Operator identity, the four operator proofs, and the priorities that flow from them. Each pillar leader owns the execution of their slice of that strategy: they are not handed a task list, they are handed a mandate. The job of the operating model is to make sure those mandates compound rather than collide.

Three failure modes this model is designed to prevent:

| Failure mode | What it looks like | What prevents it |
|---|---|---|
| **Fragmentation** | Each pillar runs its own strategy; the product feels like six products | Strategy is set once at the top; pillars execute within it, not around it |
| **Coordination tax** | Every decision requires six people in a room; nothing ships | Clear decision rights mean most decisions never need a meeting |
| **Communication overload** | Every pillar sends updates to every other pillar constantly | Pillar leads own their own comms; structured cadence replaces ad-hoc updates |

---

## Decision Rights

Before the meetings and cadence: who can decide what, alone.

### The SVP decides alone:
- The singular strategy: where we play, what we don't build, what the four proofs are
- Priority conflicts between pillars when pillar leads cannot resolve them
- Resourcing and headcount allocation across pillars
- Any decision that changes the operator identity or the market positioning

### Each pillar lead decides alone (within their owned scope):
- Their roadmap sequencing and quarterly priorities, within the strategy
- Their team's engineering approach and technical decisions
- Unilateral scope decisions that don't touch a seam defined in the [[Pillar Working Model]]
- How they communicate their pillar's work to their own engineering team

### Pillar leads decide jointly (seam decisions):
- Any decision listed as a seam in the [[Pillar Working Model]] — the six joint responsibilities
- Launch-readiness calls (Product Operations calls the gate, all four model-launch pillars must have signed off)
- Any change to the Empirical Map schema
- Any design that touches the agent identity / governance-harness seam

**The rule:** if a decision is in your owned scope and doesn't touch a seam, make it. Don't ask. Don't loop in other pillars unless you need their input to make a better decision — not for sign-off. If you're unsure whether it touches a seam, look it up in the Pillar Working Model. If it's genuinely ambiguous, flag it in the weekly seam check (below) rather than blocking yourself.

---

## Meeting Cadence

Five meeting types. Each has a single owner, a defined purpose, and a hard scope — it does not expand into adjacent territory.

---

### 1. Strategy Sync — Monthly, 60 min
**Owner:** SVP  
**Attendees:** SVP + all six pillar leads + Product Operations Lead  
**Purpose:** The singular strategy meeting. Not a status meeting. Agenda is always: (1) what did we learn this month that might change a priority, (2) are the four proofs on track or drifting, (3) are there decisions required from leadership, (4) any kill criteria getting close to their threshold.

**Rules:**
- SVP runs it; sets the agenda
- Pillar leads come prepared with one thing they learned that is strategy-relevant, not a status update
- Decisions made here are logged in the Decisions Register and become inputs to roadmaps
- No deep dives into individual pillar work — that belongs in pillar readouts

**Output:** Decisions log entry (if any decisions made), any strategy signals that need to propagate to roadmaps before the next roadmap update cycle.

---

### 2. Pillar Readout — Bi-weekly, 30 min per pillar (rotating)
**Owner:** Each pillar lead runs their own  
**Attendees:** SVP + the pillar lead + any pillar leads who own a seam with the presenting pillar  
**Purpose:** The pillar lead shows what shipped, what's in flight, what's blocked, and what decisions they need. This is the empowerment meeting — the pillar lead is presenting their program, not being reviewed.

**Rules:**
- The pillar lead chooses what to show; there is no mandated template beyond: shipped / in flight / blocked / decisions needed
- Other pillar leads attend only if they have a live seam dependency with the presenting pillar — not to listen in generally
- SVP's role is to unblock, not to redirect; strategy redirections go to the monthly Strategy Sync
- 30 min hard stop; if something needs more time it becomes a separate working session

**Output:** Unblocked items actioned by SVP; seam items flagged to the Seam Check (below) if they involve another pillar.

---

### 3. Seam Check — Weekly, 30 min
**Owner:** Product Operations Lead  
**Attendees:** Any pillar leads with an active seam item that week; not all six every week  
**Purpose:** The only standing cross-pillar coordination meeting. Covers the seven seams defined in the [[Pillar Working Model]] — not general updates, not strategy, not status. Only: (1) seam items that are blocked or ambiguous, (2) launch-readiness gate items that need multi-pillar sign-off, (3) escalations from the prior week that weren't resolved.

**Rules:**
- Product Operations Lead owns the agenda and sends it 24h in advance; if there's nothing on the agenda, the meeting is cancelled that week
- If your seam item isn't on the agenda, it doesn't get discussed — add it to the agenda before the 24h cutoff
- Attendees are invited per item, not per meeting — only the pillars relevant to each agenda item attend for that item
- No decisions made here without both relevant pillar leads present; if one is absent, the item moves to async

**Output:** Seam items resolved or escalated to SVP; launch-readiness gate status updated by Product Operations Lead in the shared gate tracker.

---

### 4. Roadmap Update Session — Quarterly, 90 min
**Owner:** SVP  
**Attendees:** SVP + all six pillar leads + Product Operations Lead  
**Purpose:** Each pillar lead presents their next-quarter roadmap for the SVP to review against the singular strategy. This is not a negotiation meeting — pillar leads arrive with a proposed roadmap, SVP reviews for strategy alignment, and feedback is given. Adjustments are made offline and finalized within one week.

**Rules:**
- Each pillar lead has 10 min to present their proposed quarter; 5 min for SVP feedback
- SVP feedback is specifically on strategy alignment, not engineering approach
- Seam dependencies between pillars are flagged in each presentation so the full picture is visible
- Product Operations Lead presents the cross-pillar launch calendar as the last item — this is where resource conflicts become visible

**Output:** Ratified quarterly roadmap per pillar, with seam dependencies logged; launch calendar updated by Product Operations Lead.

---

### 5. Working Sessions — As needed, 45 min max
**Owner:** Whoever calls it  
**Attendees:** Only the people needed to resolve a specific question  
**Purpose:** Point-in-time problem-solving. Not a recurring meeting. Used when a seam item is too complex to resolve in the Seam Check or when two pillars need to co-design something (e.g., the agent identity spec, the Empirical Map schema contract).

**Rules:**
- The person who calls it owns the outcome — a decision, a draft spec, a written agreement
- Written output is required; the output goes into the relevant hub note or pillar wiki page, not just into someone's notes
- If a working session keeps recurring on the same topic, that's a signal the seam ownership isn't clear — fix the Pillar Working Model, don't keep scheduling meetings

---

## Communication Model

The operating principle: **pillar leads own their communication outward; they do not own everyone else's attention.**

### What each pillar lead owns:
- A written **Pillar Status Note** (see template below), updated before each bi-weekly readout
- One paragraph in the monthly **All-Pillar Update** (assembled by Product Operations Lead)
- Their own engineering team communication — format and frequency at their discretion
- Seam-specific communications to the pillar leads they share seams with — async, in writing

### What Product Operations owns:
- The monthly **All-Pillar Update** — assembles one paragraph from each pillar lead into a single document, adds the launch calendar and gate status, distributes to the full product team and any stakeholders the SVP designates
- The **Launch Calendar** — single source of truth for what is launching, when, and what gates it needs to clear
- The **Seam Check agenda** — owned and distributed 24h before each weekly session
- The **Decisions Register** — log of decisions made at the Strategy Sync and escalations resolved by SVP

### What the SVP owns:
- The **Strategy Brief** — a short (one page) written document, updated quarterly, that states the singular strategy, the current proof we are trying to advance, the top three priorities, and any decisions or kill criteria that have changed. This is the anchor document every pillar roadmap is written against.
- Distribution of the All-Pillar Update to leadership and stakeholders outside the product team

### What nobody owns (and therefore nobody should do):
- Sending individual pillar updates to the full team outside the All-Pillar Update cadence
- Calling all-hands or all-pillar meetings without SVP approval
- Asking other pillar leads for sign-off on decisions that are within your owned scope

---

## Roadmap Update Process

Roadmaps are living documents. They are not updated constantly — they are updated on a defined cycle with a defined process.

### Cycle

| Event | Trigger | Owner | Output |
|---|---|---|---|
| **Quarterly roadmap update** | Start of each quarter | Each pillar lead | Proposed next-quarter roadmap; presented at Roadmap Update Session |
| **Strategy-triggered update** | Strategy Sync decision changes a priority | SVP signals to affected pillar lead(s) | Pillar lead updates their roadmap within one week; flags any seam impacts in writing to affected peers |
| **Seam-triggered update** | A seam resolution in the Seam Check changes scope for a pillar | Affected pillar lead | Updates their roadmap within 48h; Product Operations Lead updates the launch calendar |
| **Emergency update** | A shipped reality contradicts a planned capability | Pillar lead who owns the capability | Updates the capability gap register and roadmap immediately; flags to SVP and Product Operations Lead |

### What a roadmap update must contain

A roadmap update is not a slide deck. It is a written note in the wiki (or an update to the existing pillar hub page) that specifies:

1. **What changed** and why (strategy signal, seam resolution, or delivery reality)
2. **What is now in / out** of the next quarter
3. **Seam impacts** — which other pillars are affected and what they need to know
4. **Confidence state** — is this planned, in flight, or shipped? (use the canonical confidence states: assumed / derived / measured / validated)
5. **Open questions** — anything that requires SVP or another pillar lead to decide before this roadmap can be executed

Product Operations Lead reviews every roadmap update for launch-calendar impacts before it is considered final.

---

## Pillar Status Note — Template

Each pillar lead maintains this. It is the input to the bi-weekly readout and the monthly All-Pillar Update. It lives in the pillar's hub page or as a linked note.

```
## [Pillar Name] — Status as of [Date]

### Shipped since last update
- [Item]: [what it does, confidence: measured]

### In flight
- [Item]: [what it is, target date, confidence: planned]
- [Item]: [what it is, target date, confidence: planned]

### Blocked
- [Item]: [what is blocking it, who needs to unblock it]

### Decisions needed
- [Decision]: [what needs to be decided, by whom, by when]

### Seam flags
- [Seam]: [what changed or what the other pillar needs to know]

### One strategy-relevant signal
- [What we learned this month that is relevant to the broader strategy — not a status item]
```

This note does not need to be long. Its purpose is to force each pillar lead to articulate the one strategy-relevant signal from their pillar's work — because that is the input the SVP needs for the monthly Strategy Sync, and it is the discipline that keeps pillar execution connected to the singular strategy.

---

## Empowerment Guardrails

This model only works if pillar leads actually feel empowered to execute. These are the explicit commitments the SVP makes to pillar leads:

| Commitment | What it means |
|---|---|
| **I won't redirect your roadmap in a readout** | Strategy redirections go to the monthly Strategy Sync, not the bi-weekly readout. The readout is yours to run. |
| **I won't add seam sign-offs that aren't in the Pillar Working Model** | If I need a new cross-pillar dependency, I add it to the Pillar Working Model first, not as an ad-hoc ask. |
| **I will make escalated seam decisions within 48 hours** | When a seam decision is escalated to me, I will decide in writing within 48 hours so you are not blocked. |
| **I will update the Strategy Brief quarterly** | You will always have a written anchor for your roadmap. If the strategy changes, you will know before I ask your roadmap to reflect it. |
| **I will not create communication obligations outside this model** | No ad-hoc all-hands, no surprise stakeholder requests, no asks to present outside the defined cadence without advance notice and your consent. |

And the commitments pillar leads make to each other:

| Commitment | What it means |
|---|---|
| **I will flag seam impacts in writing before they become blockers** | If my roadmap changes in a way that affects your seam, I tell you in writing at the time of the change — not when you discover the impact. |
| **I will not ask for sign-off on decisions within my owned scope** | I will make those decisions. I may share them as an FYI, but I will not ask for approval. |
| **I will come to the Seam Check prepared** | If I add an item to the agenda, I come with a proposed resolution, not just a problem statement. |
| **I will keep my Pillar Status Note current** | My bi-weekly readout will not be the first time you hear what I'm working on. |

---

## How New Pillars or Scope Changes Work

When a new seam is identified (a boundary between two pillars that isn't yet documented), the process is:

1. Either pillar lead flags it in the Seam Check as an unresolved boundary
2. Product Operations Lead adds it as an open item in the Pillar Working Model
3. The two affected pillar leads schedule a Working Session to define the boundary
4. Output is a written addition to the [[Pillar Working Model]] — not a verbal agreement
5. Once both pillar leads agree and SVP is notified, the boundary is canonical

No scope change that affects another pillar is effective until it is in writing in the Pillar Working Model.

---

## See Also

- [[Pillar Working Model]] — scope boundaries, joint responsibilities, and decision rules for each seam
- [[RackAI Organizational Design]] — org chart, headcount, and reporting structure
- [[RackAI Roadmap]] — the canonical living roadmap each pillar executes against
- [[Three Battlegrounds]] — the singular strategy this operating model is designed to execute
