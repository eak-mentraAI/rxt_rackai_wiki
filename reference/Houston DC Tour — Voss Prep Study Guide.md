# Houston DC Tour — Study Guide (Voss Capital + DataJourney)

> **Status:** Personal prep doc, not canonical wiki content. This deal (Together.ai anchor tenant, Houston GB300 cluster, DataJourney, Voss) is **not** in the knowledge base, and parts of the KB describe the *old* PCIe fleet constraint — do not cite wiki fleet numbers in the room. See the landmine note at the end.
> **Items to confirm before the tour (outside this doc):** (1) is the 5 MW figure IT load or total facility load; (2) total DC runway beyond this 5 MW wave; (3) that the full Houston BOM qualifies for whatever formal NVIDIA designation is being claimed (see §5). All unconfirmed — speak to them only if verified.

---

## The investment thesis, in three moves

Hold this shape in your head. Everything else is detail hanging off it.

1. **De-risk the entry — Together.ai.** A committed anchor deployment establishes real demand from day one and justifies Phase 1.
2. **Prove repeatability — dedicated GPU clusters.** Turn what we build for Together into a deployment and operating *pattern* that sells repeatedly, instead of treating every AI deployment as custom engineering.
3. **Increase value density — RackAI.** Move from selling operated infrastructure toward selling managed AI capabilities *on top of* that infrastructure.

**Anchor → Repeat → Move up-stack.** And underneath all three: **expand capital against demand.**

You don't need to tell Voss this produces a return. Describe the mechanics well enough that they reach that conclusion themselves.

---

## The room, in one sentence

DataJourney runs the tour and owns the building. Rackspace is there to prove there is a **credible demand-and-operations plan** for the space — an anchor deployment is committed, the buildout is repeatable, compute expands against demand, and Rackspace's operating capability is what turns raw megawatts into consumable, higher-value capacity.

> **DataJourney makes the megawatts usable. Rackspace makes the megawatts consumable.**
> A customer doesn't buy five megawatts. They buy a working AI cluster, or an AI service. Rackspace's job is everything required to turn physical capacity into something a customer can actually consume: bring-up, fabric, provisioning, fleet health, lifecycle, observability, capacity management, and ultimately the platform services above it. That's why Voss needs *both* DataJourney and Rackspace.

---

## 1. The deal narrative (say it the same way every time)

Phase 1 is anchored by a **committed Together.ai deployment**, giving the initial buildout a real demand base from day one. It's dedicated **NVIDIA GB300 NVL72** infrastructure with **NVIDIA InfiniBand scale-out networking**, based on NVIDIA's reference architecture. The anchor de-risks Phase 1, and Phase 1 is the **first of a repeatable pattern** — subsequent clusters added as demand materializes.

**Initial wave specs:**
- **5 MW** *(confirm: IT vs. total facility load before the tour)*
- **32 cabinets** of GB300 NVL72
- **~2,300 GPUs** (32 × 72 = 2,304)

> **Precision guardrail — anchor vs. utilization.** "Together is committed" and "5 MW is committed" are **different statements.** Unless Together has contractually committed to essentially the entire 5 MW, say: *"Phase 1 is anchored by a committed Together.ai deployment, giving the initial buildout a real demand base from day one."* Do **not** say "the 5 MW wave is anchor-committed" — that overstates contracted utilization.

Keep this to three or four sentences. Anchor → repeatable → expand against demand.

---

## 2. Rackspace vs. DataJourney — the line Voss explicitly wants drawn

There is a hard boundary at the datacenter/infrastructure line. Be concrete about which side you're on.

| DataJourney / facility layer | Rackspace — inside the computer room |
|---|---|
| The building, power, cooling (incl. liquid/direct-to-chip for GB300), physical space, the datacenter itself | Operating the cluster and everything above the metal: bring-up, provisioning, GPU fleet health, InfiniBand fabric health, serving, lifecycle, observability, capacity management, and the RackAI platform on top |

The line to say out loud: **"Our team operates within the computer room."** Follow it immediately with *why it matters economically*: **DataJourney makes the megawatts usable; Rackspace makes them consumable.** A customer buys a working cluster or an AI service, not raw power — Rackspace is everything that turns capacity into something consumable. This mirrors the KB's own split: physical supply and the facility below the line; the operating layer above it. Rackspace's historical identity is exactly this — *take complicated infrastructure someone else built and assume operational responsibility for making it work.*

---

## 3. Why Rackspace is more than a colo landlord — value density

This is the differentiation, and it's what makes the *rest* of the room worth more than bare-metal leases.

- **Bare metal is the foundation.** Dedicated clusters (like Together's) are the base offer.
- **RackAI moves us higher in the value stack.** On the same AI infrastructure, Rackspace can add model serving, inference optimization, fine-tuning, governance, metering, and managed operations. That's a path to monetize not just infrastructure capacity, but the operating and platform capabilities around it.
- **The point for Voss:** *the same physical capacity supports multiple commercial models. Dedicated clusters establish the infrastructure business; RackAI creates a path to greater value per deployed megawatt.*

> **Language guardrail — value density, not proven margin.** Don't say "RackAI is the margin layer" — it invites *"what's the margin difference?"* and you don't have a built cost model. Frame it as **value density** and a **path** to greater value per megawatt. Defensible without final unit economics.

---

## 4. The fill / ROI story — three paths to utilization, one repeatable base

Next-phase growth is a **mix**. These are **three paths to utilization against one repeatable infrastructure base** — not independent bets. (A sophisticated audience will notice they're all exposed to the same enterprise-AI-infrastructure demand, GPU economics, and model-efficiency trends, so don't call them "independent.")

1. **Together.ai expansion** — lowest-risk path. Proven anchor, growing. Covers the near-term curve.
2. **Net-new dedicated-cluster tenants** — the repeatability proof. Shows Houston isn't a one-off; the reference design becomes a repeatable pattern others want. "First of many," made concrete.
3. **RackAI platform capacity** — the value-density path. Rackspace-operated platform tenants on the same fabric — the part a pure colo can't do.

**Capital discipline — likely the most important point for Voss.** The facility gives us expansion runway, but **compute can be deployed in phases against demand.** We don't populate the entire room with GPUs on day one and hope utilization follows. Together anchors the first deployment; subsequent clusters are added as customer demand materializes. The financing model is:

> **secure scarce power/cooling capacity → land anchor → deploy compute → establish operating pattern → add demand → deploy incremental compute**

— not *finance a giant AI build → hope somebody rents it.*

**Honest boundary to hold:** the anchor (Together) is committed; the other two paths are **forward** demand, not signed. Credible line — *"Anchor is committed; the buildout gives us runway to fill three ways, and we add compute against demand rather than speculatively."* Do not imply net-new or RackAI tenants are contracted.

---

## 5. Depth signals + Q&A defense

**Depth signals — drop these to show mastery:**
- **What "GB300 NVL72" actually means:** within the rack, 72 Blackwell Ultra GPUs operate as a tightly-coupled **NVLink compute domain**. **InfiniBand** provides the scale-out fabric that connects those domains into a much larger cluster. That tight coupling is what lets you serve large/frontier models and command premium tenants — the opposite of a loosely-coupled PCIe setup.
- GB300 NVL72 is **liquid-cooled (direct-to-chip)** — a facility requirement, and squarely DataJourney's side of the line. Naming it shows you know where your boundary sits.
- Anchor-tenant model de-risks a build; capacity can be pooled and reallocated as tenants come and go.

> **NVIDIA-architecture language guardrail.** The **GB300 NVL72 itself** is NVIDIA's rack-scale system architecture; InfiniBand is the scale-out networking between racks. Don't call the whole thing "NVIDIA's blessed reference architecture" as if it's a certification unless someone who owns the architecture confirms the **full Houston BOM** qualifies for that formal designation. Safe phrasing: *"We're deploying NVIDIA GB300 NVL72 rack-scale systems with NVIDIA InfiniBand scale-out networking, based on NVIDIA's reference architecture."*

**Likely hard questions:**
- **"Is that 5 MW compute or total?"** — *Confirm before tour.* A single GB300 NVL72 rack is roughly ~120–140 kW; 32 racks ≈ ~4 MW IT load before cooling overhead, so 5 MW is tight-but-plausible as an IT envelope. Know the basis; don't guess in the room.
- **"How big can this get / what's the runway?"** — *Confirm total DC size before tour.* If unknown, speak to the demand-paced deployment logic, not a ceiling.
- **"What's the margin difference between bare metal and RackAI?"** — **Do not invent numbers.** No cost model is built; KB figures are placeholders. Speak to the *mechanism*: same physical capacity, multiple commercial models, a path to greater value per megawatt. Value density, not a quoted margin.
- **"Is the 5 MW leased/committed by Together?"** — Separate anchor from utilization (see §1 guardrail). Committed *deployment*, real demand base — not necessarily the full 5 MW.

**The landmine — do not step on it:** The KB's fleet notes describe RackAI's *current* fleet as ~16× H100 NVL PCIe with a ~27B-class model ceiling, and file B300/UBB8 as the frontier tier RackAI "does not have." That's the **old constraint**, not this cluster. This Houston deal is precisely the tightly-coupled fabric that removes that ceiling — frame it as a strategic **upgrade**, and make sure no one on your side cites the old PCIe numbers. Also: the KB currently files **Together.ai as a competitor**, not a customer — another reason to keep the deal narrative sourced from you, not the wiki.

---

## 6. Physical walkthrough — what to point at, and what to say

For an under-construction tour, tie each physical thing DataJourney shows you back to **GB300, Together, RackAI, scalability, or economics** in 10–20 seconds. Have one credible line ready for each.

| What they show you | Your 10–20 second Rackspace line |
|---|---|
| **Power delivery** (feeds, switchgear, substation) | "This is the scarce resource — securing power capacity is what makes the whole thesis work. We deploy compute against demand into this envelope rather than all at once. *(Note the 5 MW basis — IT vs. total — once confirmed.)*" |
| **Liquid cooling / CDUs** | "GB300 NVL72 is direct-to-chip liquid-cooled — this cooling loop is a hard requirement for the density, not an upgrade. This is DataJourney's domain; our fleet sits on top of it." |
| **Racks / cabinet rows** | "Each of these is a GB300 NVL72 — 72 Blackwell Ultra GPUs as one tightly-coupled NVLink domain. 32 cabinets, ~2,300 GPUs in this wave. Together anchors the first block; the rows are how repeatability shows up physically." |
| **Network / fiber / IB spine** | "This is the InfiniBand scale-out fabric — it stitches the per-rack NVLink domains into one large cluster. Bringing up and keeping this fabric healthy is squarely Rackspace's job inside the room." |
| **Meet-me room / carrier / cross-connects** | "Connectivity into the room — matters for how tenants and platform traffic actually reach the clusters. Part of what makes capacity *consumable* rather than just present." |
| **Security / access control** | "Physical security underpins the private, dedicated posture tenants like Together expect — dedicated clusters, controlled access. Supports the enterprise/governance story RackAI carries above the metal." |
| **Loading dock / staging / build progress** | "This is deploy-against-demand in action — we phase compute in as clusters are needed rather than filling the room speculatively. Under-construction is the point: capacity runway now, GPUs as demand lands." |

---

## 30-second open (if you get one line)

> "This starts with a committed anchor deployment for Together.ai: dedicated NVIDIA GB300 NVL72 infrastructure with InfiniBand scale-out networking. DataJourney provides the facility and the physical capacity; Rackspace operates inside the computer room and turns that capacity into something customers can actually consume — bringing up and operating the clusters, managing the fabric and fleet, and ultimately adding platforms like RackAI on top. Together de-risks the first deployment. From there we have three paths to utilization: Together expansion, additional dedicated-cluster customers, and RackAI platform capacity. And importantly, we add compute against demand rather than making the entire GPU investment speculatively upfront. That's the model: land an anchor, establish a repeatable operating pattern, fill incrementally, and move higher in the value stack."
