---
id: ent-environment
type: entity
status: draft
owner: infra-eng
domain: infrastructure
aliases: [environment, deployment environment, deployment tier]
related: [ent-model-deployment, ent-gpu-cluster, ent-region, hub-entities]
source_docs: [rackai_deployment_envs]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: a deployment tier (dev/staging/production) that hosts model deployments."
---

# Environment

## Definition

An **Environment** is a deployment tier for RackAI — `dev`, `staging`, or `production` — served under `*.rackai.rax.io`. Today the platform runs single-cluster and single-region; the `production` tier is planned. An Environment hosts [[Model Deployment]] instances and maps to a [[GPU Cluster]] and a [[Region]].

## Layer

L1 — Entity Ontology. The Environment is the deployment tier that anchors the serving chain to a cluster and region:

**Environment → [[Model Deployment]] → [[Serving Runtime]] → [[Accelerator Class]] → [[GPU Cluster]] → [[Region]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Env ID | Stable identifier | string | measured |
| Tier | `dev`, `staging`, `production` | enum | measured |
| Domain | Served under `*.rackai.rax.io` | string | measured |
| Cluster topology | Single-cluster today | enum | measured |
| Region topology | Single-region today | enum | measured |
| Production status | `production` tier is planned | enum | assumed |

## Lifecycle States

Not a stateful entity. (An Environment is a standing tier, not a lifecycle-bearing object.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| HOSTS | [[Model Deployment]] | → | Deployments run within an environment |
| MAPS_TO | [[GPU Cluster]] | → | Single cluster today |
| MAPS_TO | [[Region]] | → | Single region today |

## Evidence

- Source: `rackai_deployment_envs`.
- Confidence rationale: `measured` — dev/staging tiers, the `*.rackai.rax.io` domain, and single-cluster/single-region topology are shipped. The `production` tier is `assumed` (planned) until confirmed.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment]]
- [[GPU Cluster]]
- [[Region]]
