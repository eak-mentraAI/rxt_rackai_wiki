---
id: ent-workload-declaration
type: entity
status: draft
owner: rackai-product
domain: product
aliases: [workload declaration, declaration, declaration surface, intent and constraints declaration, customer declaration, declared workload, workload intent]
related: [ent-model-deployment-spec, ent-model-deployment, ent-organization, ent-model, ent-capacity-pool, ent-traffic-class, ent-empirical-map, ent-governed-harness, pol-sovereignty-levels, hub-battlegrounds, hub-roadmap, prd-workload-declaration-placement, spec-workload-declaration-placement, met-slo-attainment, ent-evidence-report]
source_docs: ["00-hub/Three Battlegrounds.md", "00-hub/RackAI Roadmap.md", "01-entities/Model Deployment Specification.md", "05-wiki/Milestone Release Map.md"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-entities
summary: "Canonical entity: the customer's versioned statement of what a serving workload needs and must never violate."
---

# Workload Declaration

## Definition

A **Workload Declaration** is the customer-facing, versioned statement of what a model-serving workload must achieve and what it must never violate: the model or capability wanted, the workload profile and its service level, and the constraints on where and how it may run, each marked **hard** (never violated) or **soft** (a preference RackAI trades off). RackAI derives the [[Model Deployment Specification]] and the placement from it. The declaration is the customer's *what*; the specification and placement are RackAI's *how*.

It is the serving-workload form of the intent-and-constraints contract in [[Three Battlegrounds]] ("you tell us what you want, what matters, and what you won't compromise"). Placement principle (adopted 2026-10-06): *RackAI chooses by default; customers constrain when necessary.* A customer who requires specific hardware states it as a hard constraint; it is not the base consumption model.

> **Status: proposed, not built.** No declaration object exists in RackAI today: a customer names hardware on the deployment (an accelerator class) or takes the default scheduler, and cannot state a profile, service level, residency, sovereignty level or cost preference (read-only code survey, `RSS-Engineering/rackai@79ca4de`). Everything below is `assumed` until delivered. The product contract is specified in [[Workload Declaration & Placement PRD]].

## Layer

L1 — Entity Ontology. It sits at the head of the serving chain, where demand becomes a contract:

**Market Demand → [[Workload Declaration]] → [[Model]] / [[Model Deployment Specification]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

## Attributes

| Attribute | Description | Hard / soft | Type | Confidence |
|-----------|-------------|:-:|------|:----------:|
| Scope | The [[Organization]] (and project) the workload belongs to | n/a | ref | assumed |
| Model or capability | A specific [[Model]] and version, or a capability class RackAI may satisfy with a model of its choosing | Hard when a model is named | ref / enum | assumed |
| Workload profile | The declared shape of the workload (e.g. interactive, throughput, long context); the measured counterpart is [[Traffic Class]] | Hard | enum | assumed |
| Service level | Latency and attainment targets for the profile. Thresholds per profile are a pending decision (roadmap row 11); [[SLO Attainment]] measures them | Hard or soft, declared per target | struct | assumed |
| Expected load | Expected request rate / concurrency and growth, so capacity can be sized | Soft | struct | assumed |
| Sovereignty level | Which level of [[Sovereignty Levels]] the workload requires (0 Shared, 1 Dedicated; 2 and 3 later) | Hard | enum | assumed |
| Location / residency | Where execution (and data) may and may not be. Single region today; jurisdiction pinning is MOE-3 | Hard | set | assumed |
| Approved hardware / vendors | Optional allow- or deny-list of accelerators or vendors (e.g. "NVIDIA only", a specific GPU) | Hard | set | assumed |
| Economics preference | How to trade cost against performance headroom inside the hard constraints | Soft | enum / weights | assumed |
| Inherited constraints | Constraints the declarer does not write but that apply: organization policy, delegated authority, approved models, quotas. Shown on the declaration, not editable by it | Hard | ref | assumed |
| Version | Every change is a new version; the realised placement records which version it satisfies | n/a | int | assumed |

Constraint *sources* follow [[Three Battlegrounds]]: **declared** (this note), **inherited** (governance, delegated authority), **discovered** (what the estate makes possible: capacity, measured performance, via the [[Empirical Map]]), and **derived** (what follows from the chosen plan). Adaptive constraints (that change with context) are out of scope for v1.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Draft | Being written; not evaluated | Customer starts a declaration | Submitted |
| Submitted | Awaiting a feasibility decision | Customer submits a version | Found feasible or infeasible |
| Infeasible | No placement satisfies every hard constraint; RackAI has said which constraints conflict and what would make it feasible | Feasibility check fails | Customer amends, or withdraws |
| Accepted | Feasible, and a placement has been chosen and approved by an authorized operator. Each option is marked *performance verified* or *performance unverified*; approving an unverified option never implies the service level will be met | Feasibility check passes and the initial realization is approved | Feasibility revalidated at commitment: Realised, or back to Submitted/Infeasible |
| Realised | Running on a placement that satisfies every hard constraint | Deployment ready | Amended, or retired |
| Amended | A new version replaces the current one; the running placement stays until the new version is accepted | Customer submits a new version | Back to Submitted |
| Retired | No longer served | Customer withdraws or retires the workload | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| DERIVES | [[Model Deployment Specification]] | → | The specification is derived from the declaration, never authored in its place |
| CONSTRAINS | [[Model Deployment]] | → | Every hard constraint holds for the deployment's whole life |
| BELONGS_TO | [[Organization]] | → | Scoped to one tenant |
| USES | [[Model]] | → | When a specific model is declared |
| CONSTRAINS | [[Capacity Pool]] | → | Placement may draw only from pools satisfying the hard constraints |
| CONSUMES | [[Empirical Map]] | ← | The map's recommendations rank only options that satisfy the hard constraints |
| GOVERNS | [[Governed Harness]] | ← | Delegated authority and enforcement (inherited constraints) are owned there, not here |
| USES | [[Sovereignty Levels]] | → | The declared level is a hard constraint |

## Graph Invariants

- Every Workload Declaration belongs to exactly one [[Organization]].
- A realised placement satisfies **every** hard constraint of the declaration version it records. A hard constraint is never relaxed without the customer amending the declaration. A violation found at runtime is detected, contained and evidenced, never accepted.
- Every [[Model Deployment Specification]] derived from a declaration records the declaration version it satisfies.

## Evidence

- Source: `source_docs` (strategy and roadmap; no shipped implementation).
- Confidence rationale: `assumed` — a proposed product contract (P-004); nothing is built. Attributes beyond those named in the adopted placement principle (model, SLA, residency, approved vendor, economics) are proposals of the [[Workload Declaration & Placement PRD]] and await product approval.

## See Also

- [[Workload Declaration & Placement PRD]] — the product contract for declaring and placing
- [[Workload Declaration & Placement Tech Spec]] — the proposed engineering design (draft)
- [[Three Battlegrounds]] — the intent-and-constraints contract this is the serving form of
- [[Model Deployment Specification]] — RackAI's realization record, derived from this
- [[Entity Ontology Hub]]
