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

## Leadership Structure

Two leaders run this operating model as peers. The SVP (Chetan Gupta) is the strategic authority and escalation point — not an operating participant in the day-to-day cadence described below.

| Role | Person | What they lead |
|---|---|---|
| **Head of Product** | Edward Kerr | Owns and runs the product strategy, the PM pillar leads, the roadmap process, and this operating model. Sets the singular product strategy; pillar PMs execute within it. |
| **Head of Engineering** | Jovan Rajapakse | Owns the engineering delivery, the engineering pillar leads, and the architecture function. Engineering pillar leads are the PM pillar leads' counterparts — same pillars, different accountability. |
| **SVP** | Chetan Gupta | Sets overall BU strategy and resourcing; approves major strategic pivots; is the escalation point when the two heads cannot align. Does not own the operating cadence described here. |

**How the two heads work together:** Edward and Jovan operate as one leadership unit for this team. Every meeting in this model includes both of them. Product direction comes from Edward; engineering delivery and feasibility come from Jovan. Neither overrides the other — when they disagree, they resolve it before bringing it to the team. When they cannot resolve it, it escalates to the SVP.

**How pillar leads work:** Each pillar has a PM (reports to Edward) and an engineering lead (reports to Jovan). They are a pair. The PM owns what we build and why; the engineering lead owns how. Both attend the same meetings for their pillar.

---

## The Governing Principle

> **One strategy. Executed by the right people. Communicated without drowning anyone.**

The Head of Product sets and owns the singular product strategy for RackAI — the Private Enterprise AI Operator identity, the four operator proofs, and the priorities that flow from them. Each pillar PM owns the product execution of their slice; each engineering lead owns the delivery. The job of the operating model is to make sure those mandates compound rather than collide.

Three failure modes this model is designed to prevent:

| Failure mode | What it looks like | What prevents it |
|---|---|---|
| **Fragmentation** | Each pillar runs its own strategy; the product feels like six products | Strategy is set once at the top; pillars execute within it, not around it |
| **Coordination tax** | Every decision requires six people in a room; nothing ships | Clear decision rights mean most decisions never need a meeting |
| **Communication overload** | Every pillar sends updates to every other pillar constantly | Pillar leads own their own comms; structured cadence replaces ad-hoc updates |

---

## Decision Rights

Before the meetings and cadence: who can decide what, alone.

### The Head of Product decides alone (product scope):
- The singular product strategy: where we play, what we don't build, what the four proofs are
- Product priority conflicts between pillars when pillar PMs cannot resolve them
- Any decision that changes the operator identity or the market positioning
- What gets on the roadmap and in what sequence

### The Head of Engineering decides alone (engineering scope):
- Engineering architecture and technical approach within each pillar
- Engineering resourcing and team allocation across pillars
- Engineering priority conflicts between pillar engineering leads
- Build approach, tooling, and infrastructure decisions below the product API surface

### Heads of Product and Engineering decide jointly:
- Quarterly roadmap ratification — product priorities must be feasible; engineering delivery must serve product outcomes
- Headcount allocation when it affects product scope or delivery timeline
- Any decision that requires trading product scope against engineering capacity

### Each pillar PM decides alone (within their owned product scope):
- Their roadmap sequencing and quarterly priorities, within the strategy
- Unilateral scope decisions that don't touch a seam defined in the [[Pillar Working Model]]
- How they communicate their pillar's work to their stakeholders

### Each engineering lead decides alone (within their owned engineering scope):
- Technical implementation decisions within their pillar
- Engineering team processes and delivery cadence
- Technical debt and refactoring decisions within their pillar

### Pillar leads decide jointly (seam decisions):
- Any decision listed as a seam in the [[Pillar Working Model]] — the seven joint responsibilities
- Launch-readiness calls (Product Operations calls the gate; all relevant pillar PMs and engineering leads sign off)
- Any change to the Empirical Map schema
- Any design that touches the agent identity / governance-harness seam

**The rule:** if a decision is in your owned scope and doesn't touch a seam, make it. Don't ask. If you're unsure whether it touches a seam, look it up in the Pillar Working Model. If it's genuinely ambiguous, flag it in the weekly Seam Check rather than blocking yourself.

---

## Meeting Cadence

Five meeting types. Each has a single owner, a defined purpose, and a hard scope.

---

### 1. Strategy Sync — Monthly, 60 min
**Owner:** Head of Product (Edward)
**Attendees:** Edward + Jovan + all six pillar PMs + all six engineering leads + Product Operations Lead
**Purpose:** The singular strategy meeting. Not a status meeting. Agenda is always: (1) what did we learn this month that might change a priority, (2) are the four operator proofs on track or drifting, (3) are there decisions required, (4) are any kill criteria approaching their threshold.

**Rules:**
- Edward runs it and sets the agenda; Jovan co-presents on engineering signal
- Pillar leads (both PM and engineering) come with one strategy-relevant signal each — not a status update
- Decisions made here are logged in the Decisions Register
- No deep dives into individual pillar work — that belongs in pillar readouts
- SVP is not a regular attendee; Edward briefs the SVP separately after this meeting with any decisions requiring BU-level awareness

**Output:** Decisions Register entry (if decisions made); any strategy signals that need to propagate to roadmaps before the next roadmap cycle.

---

### 2. Pillar Readout — Bi-weekly, 45 min per pillar (rotating)
**Owner:** Pillar PM leads their own readout
**Attendees:** Edward + Jovan + the pillar PM + the pillar engineering lead + any pillar leads (PM + eng) who share a live seam with this pillar
**Purpose:** The pillar PM and engineering lead show what shipped, what's in flight, what's blocked, and what decisions they need. This is the empowerment meeting — the pillar leads are presenting their program, not being reviewed.

**Rules:**
- The pillar PM leads the readout; the engineering lead presents delivery status and flags technical blockers
- Other pillar leads attend only if they have a live seam dependency with the presenting pillar — not to listen in generally
- Edward's role is to unblock product decisions; Jovan's role is to unblock engineering decisions; neither redirects strategy in this meeting — that goes to the monthly Strategy Sync
- 45 min hard stop; anything needing more time becomes a separate working session

**Output:** Unblocked items actioned by Edward or Jovan; seam items flagged to the Seam Check if they involve another pillar.

---

### 3. Seam Check — Weekly, 30 min
**Owner:** Product Operations Lead
**Attendees:** Product Operations Lead + any pillar leads (PM and engineering) with an active seam item that week — not all twelve every week
**Purpose:** The only standing cross-pillar coordination meeting. Covers the seven seams defined in the [[Pillar Working Model]] only: (1) seam items that are blocked or ambiguous, (2) launch-readiness gate items needing multi-pillar sign-off, (3) unresolved escalations from the prior week.

**Rules:**
- Product Operations Lead owns the agenda, distributed 24h in advance; if there's nothing on the agenda, the meeting is cancelled
- Attendees are per item, not per meeting — only the pillars relevant to each agenda item attend for that item
- Both the PM and engineering lead for an affected pillar attend together — seam decisions require both perspectives
- No decisions made without both relevant pillar leads (PM + eng) present; if one is absent, the item moves to async
- Edward and Jovan do not attend the Seam Check unless an item requires escalation — Product Operations Lead escalates to them in writing if needed

**Output:** Seam items resolved or escalated to Edward/Jovan; launch-readiness gate status updated by Product Operations Lead in the shared gate tracker.

---

### 4. Roadmap Update Session — Quarterly, 2 hours
**Owner:** Head of Product (Edward), co-run with Head of Engineering (Jovan)
**Attendees:** Edward + Jovan + all six pillar PMs + all six engineering leads + Product Operations Lead
**Purpose:** Each pillar PM presents their proposed next-quarter roadmap alongside their engineering lead's delivery assessment. Edward reviews for strategy alignment; Jovan reviews for engineering feasibility. This is not a negotiation meeting — pillar leads arrive with a proposal; feedback is given; adjustments are made offline within one week.

**Rules:**
- Each pillar pair (PM + engineering lead) has 12 min: 8 min to present, 4 min for Edward and Jovan feedback
- Edward's feedback is on product strategy alignment; Jovan's feedback is on engineering feasibility and sequencing
- Seam dependencies between pillars are flagged in each presentation so the full picture is visible
- Product Operations Lead presents the cross-pillar launch calendar as the final item — this is where resource and timing conflicts surface
- SVP may attend as an observer but does not run this session

**Output:** Ratified quarterly roadmap per pillar, with seam dependencies logged; launch calendar updated by Product Operations Lead.

---

### 5. Working Sessions — As needed, 45 min max
**Owner:** Whoever calls it
**Attendees:** Only the people needed to resolve a specific question — typically a PM + engineering lead pair, or two pillar pairs for cross-seam design
**Purpose:** Point-in-time problem-solving. Not a recurring meeting. Used when a seam item is too complex to resolve in the Seam Check, or when two pillars need to co-design something (e.g., the agent identity spec, the Empirical Map schema contract).

**Rules:**
- The person who calls it owns the outcome — a decision, a draft spec, a written agreement
- Written output is required; it goes into the relevant hub note or pillar wiki page
- If a working session keeps recurring on the same topic, that's a signal the seam isn't clearly owned — fix the Pillar Working Model, don't keep scheduling meetings

---

## Communication Model

**Pillar leads own their communication outward. They do not own everyone else's attention.**

### What each pillar PM owns:
- A written **Pillar Status Note** (template below), updated before each bi-weekly readout
- One paragraph in the monthly **All-Pillar Update** (assembled by Product Operations Lead)
- Direct communication to their engineering counterpart — always first, before broadcasting more widely
- Seam-specific communications to the pillar PMs they share seams with — async, in writing

### What each engineering lead owns:
- Delivery status input to their PM's Pillar Status Note
- Direct communication to their PM counterpart — always first
- Engineering team communication — format and frequency at their discretion
- Technical signal to Jovan on anything that changes delivery timeline or technical feasibility

### What Product Operations owns:
- The monthly **All-Pillar Update** — one paragraph per pillar, launch calendar, gate status; distributed to the full product+engineering team and any stakeholders Edward designates
- The **Launch Calendar** — single source of truth for what is launching, when, and what gates it needs
- The **Seam Check agenda** — owned and distributed 24h in advance
- The **Decisions Register** — log of decisions made at the Strategy Sync and escalations resolved by Edward or Jovan

### What the Head of Product (Edward) owns:
- The **Strategy Brief** — one page, updated quarterly: singular strategy, current operator proof, top three priorities, any decisions or kill criteria that changed. Every pillar roadmap is written against this document.
- Briefing the SVP after the monthly Strategy Sync on anything requiring BU-level awareness or approval
- Distribution of the All-Pillar Update to stakeholders outside the product team

### What the Head of Engineering (Jovan) owns:
- The **Engineering Delivery Brief** — a matching one-page document, updated quarterly: delivery status against the four proofs, engineering risks, resourcing reality, and any feasibility signals that affect product roadmap assumptions
- Alignment with Edward before the Strategy Sync so the two briefs are consistent

### What nobody owns (and therefore nobody should do):
- Sending individual pillar updates to the full team outside the All-Pillar Update cadence
- Calling all-pillar or all-hands meetings without Edward and Jovan both agreeing
- Asking other pillar leads for sign-off on decisions within your owned scope

---

## Roadmap Update Process

Roadmaps are updated on a defined cycle — not continuously. The canonical roadmap tool is **Craft.io** — all roadmap updates are made there. The wiki (pillar hub pages) carries the strategic rationale, confidence states, and open questions behind each roadmap item; Craft.io carries the live roadmap itself. Neither replaces the other.

### Cycle

| Event | Trigger | Owner | Output |
|---|---|---|---|
| **Quarterly roadmap update** | Start of each quarter | Pillar PM + engineering lead pair | Proposed next-quarter roadmap updated in Craft.io; presented at Roadmap Update Session |
| **Strategy-triggered update** | Strategy Sync decision changes a priority | Edward signals to affected pillar PM; Jovan to affected engineering lead | Craft.io updated within one week; seam impacts flagged in writing to affected peers |
| **Seam-triggered update** | A Seam Check resolution changes scope for a pillar | Affected pillar PM | Craft.io updated within 48h; Product Operations Lead updates launch calendar |
| **Delivery-reality update** | Shipped reality contradicts a planned capability | Pillar PM + engineering lead | Craft.io and capability gap register updated immediately; flagged to Edward, Jovan, and Product Operations Lead |

### What a roadmap update must contain

A roadmap item in Craft.io should specify:

1. **What it is and why** — the product outcome, not just the feature name; linked to the operator proof it serves
2. **What is now in / out** of the next quarter
3. **Seam impacts** — tag any other pillars affected so their PMs are notified
4. **Confidence state** — assumed / derived / measured / validated (use Craft.io's status field consistently with the wiki confidence vocabulary)
5. **Open questions** — anything requiring Edward, Jovan, or another pillar lead to decide before this item can be executed; flag as a blocker in Craft.io and note the owner

For significant changes — ones that shift strategic direction, change a proof's exit condition, or resolve a gap — also update the relevant pillar hub page in the wiki with the rationale. Craft.io carries the *what and when*; the wiki carries the *why and what we learned*.

Product Operations Lead reviews every roadmap update for launch-calendar impacts before it is considered final.

---

## Pillar Status Note — Template

Each pillar PM maintains this with input from their engineering lead. It is the input to the bi-weekly readout and the monthly All-Pillar Update.

```
## [Pillar Name] — Status as of [Date]
PM: [Name] | Engineering Lead: [Name]

### Shipped since last update
- [Item]: [what it does / confidence: measured]

### In flight
- [Item]: [target date / confidence: planned]

### Blocked
- [Item]: [what is blocking it / who needs to unblock it (Edward / Jovan / other pillar)]

### Decisions needed
- [Decision]: [what needs to be decided, by whom (Edward / Jovan / joint), by when]

### Seam flags
- [Seam]: [what changed or what the other pillar needs to know]

### One strategy-relevant signal
- [What we learned this period that is relevant to the broader operator strategy — not a status item]
```

The one strategy-relevant signal is the most important field. It is the discipline that keeps pillar execution connected to the singular strategy and is the input Edward needs for the monthly Strategy Sync.

---

## Empowerment Guardrails

This model only works if pillar leads actually feel empowered. These are the explicit commitments Edward and Jovan make:

| Commitment | What it means |
|---|---|
| **We won't redirect your roadmap in a readout** | Strategy redirections go to the monthly Strategy Sync. The readout is yours to run. |
| **We won't add seam sign-offs that aren't in the Pillar Working Model** | If a new cross-pillar dependency is needed, it goes into the Pillar Working Model first. |
| **We will make escalated seam decisions within 48 hours** | When a seam decision is escalated to either of us, we decide in writing within 48 hours. |
| **Edward will update the Strategy Brief quarterly** | There will always be a written anchor for your product roadmap. If the strategy changes, you'll know before your roadmap is expected to reflect it. |
| **Jovan will update the Engineering Delivery Brief quarterly** | There will always be a written view of engineering capacity and feasibility. Pillar PMs will not be surprised by delivery reality. |
| **We will not create communication obligations outside this model** | No ad-hoc all-hands, no surprise stakeholder requests, no asks to present outside the defined cadence without advance notice. |

Pillar lead commitments to each other:

| Commitment | What it means |
|---|---|
| **I will flag seam impacts in writing before they become blockers** | If my roadmap changes in a way that affects your seam, I tell you at the time of the change — not when you discover the impact. |
| **I will not ask for sign-off on decisions within my owned scope** | I will make those decisions. I may share as an FYI, but I will not ask for approval. |
| **I will come to the Seam Check prepared** | If I add an item to the agenda, I come with a proposed resolution, not just a problem statement. |
| **I will keep my Pillar Status Note current** | My bi-weekly readout will not be the first time you hear what I'm working on. |
| **I will talk to my PM/engineering counterpart first** | Before broadcasting a seam flag or decision to the wider team, I align with my pillar counterpart. |

---

## How New Seams or Scope Changes Work

When a new seam is identified that isn't yet documented:

1. Either pillar lead flags it in the Seam Check as an unresolved boundary
2. Product Operations Lead adds it as an open item in the Pillar Working Model
3. The two affected pillar pairs (PM + engineering lead for each) schedule a Working Session to define the boundary
4. Output is a written addition to the [[Pillar Working Model]] — not a verbal agreement
5. Once both pillar pairs agree and Edward + Jovan are notified, the boundary is canonical

No scope change that affects another pillar is effective until it is in writing in the Pillar Working Model.

---

## See Also

- [[Pillar Working Model]] — scope boundaries, joint responsibilities, and decision rules for each seam
- [[RackAI Organizational Design]] — org chart, headcount, and reporting structure
- [[RackAI Roadmap]] — the canonical living roadmap each pillar executes against
- [[Three Battlegrounds]] — the singular strategy this operating model is designed to execute
