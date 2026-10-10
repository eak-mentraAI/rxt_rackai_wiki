---
id: ent-serving-configuration-identity
type: entity
status: draft
owner: ai-harness
domain: performance
aliases: [serving configuration identity, scid, serving configuration id, configuration digest, serving config identity]
related: [prd-empirical-map-routing, spec-empirical-map-routing, prd-workload-declaration-placement, spec-workload-declaration-placement, prd-model-lifecycle, spec-model-lifecycle, ent-empirical-map, ent-benchmark-run, pol-benchmark-evidence-chain, pol-verification-status, ent-model-deployment-spec, ent-accelerator-class, ent-serving-runtime, hub-entities]
source_docs: ["05-wiki/Empirical Map & Evidence-Informed Routing Tech Spec.md", "05-wiki/Workload Declaration & Placement Tech Spec.md", "02-operations/policies/Benchmark Evidence Chain.md", "Product-owner review disposition 2026-10-10 (X-2)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-entities
summary: "Canonical entity: scid, the versioned digest that names one serving configuration for qualification and evidence."
---

# Serving Configuration Identity

## Definition

A **Serving Configuration Identity** (`scid`) is the single canonical name of one serving configuration: the exact combination of model artifact, runtime, engine settings and accelerator shape that a [[Model Deployment]] runs. Two configurations with the same `scid` are the same configuration for every qualification and performance claim. Two with different `scid`s are different, however similar they look.

**Ownership (product-owner ruling X-2, 2026-10-10):** [[Empirical Map & Evidence-Informed Routing PRD]] (G) owns the schema, digest, schema versioning, compatibility rules and verification semantics. [[Model Lifecycle PRD]] (F) produces an `scid` for every configuration at qualification. [[Workload Declaration & Placement PRD]] (A) computes it for each feasible option and uses it to match evidence. G validates every registered artifact against it.

> **Assumed confidence.** Proposed design; nothing is built. The field set below is schema version 1 as proposed in [[Empirical Map & Evidence-Informed Routing Tech Spec]] §4.2.

## Layer

L1 — Entity Ontology. It names a configuration at the [[Model Deployment]] → [[Serving Runtime]] → [[Accelerator Class]] step of the chain:
Market Demand → Model → Model Deployment → **Serving Runtime (+ configuration)** → Capacity Pool → GPU Fleet → Topology.

The infrastructure profile (the Validated Cluster Profile of the [[Benchmark Evidence Chain]]) is deliberately **not** part of `scid`. The chain keeps infrastructure and serving versions separate so that a serving change doesn't force hardware re-acceptance. Evidence carries both, and both are matched.

## Attributes

**Schema version 1 fields** (all required; an absent optional value is encoded as an explicit `null`, never omitted):

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| `schemaVersion` | Identity schema version (`1`) | int | assumed |
| `runtime` | `ModelClass` runtime enum (e.g. `vllm`, `optimized-nim-vllm`, `aim`) | enum | assumed |
| `servingPath` | `isvc` or `llmisvc`, while both paths are live | enum | assumed |
| `runtimeImageDigest` | Image digest, never a tag | string | assumed |
| `engineVersion` | Engine version reported by the image | string | assumed |
| `modelArtifactDigest` | Digest of the model weights artifact | string | assumed |
| `modelRevision`, `tokenizerRevision` | Pinned revisions | string | assumed |
| `precision` | Weights and compute precision, including quantization format | enum | assumed |
| `parallelism` | `{ tp, pp, ep }` | struct | assumed |
| `gpusPerReplica` | Devices per replica | int | assumed |
| `acceleratorType` | Vendor and GPU type (not the class name) | string | assumed |
| `engineArgsDigest` | SHA-256 of the canonical merged engine args, minus the version's declared identity-neutral list (e.g. served model name, port) | string | assumed |
| `schedulerFlagsDigest` | SHA-256 of the canonical routing scheduler configuration, or `null` | string | assumed |

**Digest.** `scid = "scid:v" + schemaVersion + ":" + hex(SHA-256(JCS(record)))`, where `record` is the field set above and JCS is the RFC 8785 JSON canonicalization. Every producer and consumer computes it through one shared library with versioned golden test vectors in CI. Nobody re-implements it.

**Identity record.** Every artifact, qualification record and evidence row stores the full field values next to the `scid`, not only the digest. That is what lets later schema versions be checked against older evidence.

## Schema Versioning and Compatibility

1. **Frozen versions.** Once a schema version is released, its field set, its identity-neutral args list and its canonicalization never change. Any change, whether adding, removing or redefining a field, creates version *N+1*. So the same configuration always yields the same digest at a given version, across releases and components.
2. **Matching uses the evidence's version.** To compare a candidate with evidence recorded at version *N*, the consumer recomputes the candidate's digest **at version *N*** from the candidate's full identity record. Digests of different versions are never compared directly.
3. **Added fields need a declared equivalence.** Version *N+1* declares, for each added field, the value that every version-*N* record implicitly had (for example, `servingPath: isvc` for records made before llmisvc existed), or declares that none is known. Version-*N* evidence matches an *N+1* candidate only if the candidate's value for each added field equals that declared value.
4. **No silent invalidation, no silent pass.** When rule 3 can't be satisfied, the evidence is not deleted and not passed. Its performance status for that candidate is `unverified` with reason `IdentityVersionMismatch`, visibly, per [[Verification Status Vocabulary]]. It may still be used as ranking evidence. Re-registering or re-qualifying the configuration at the new version restores it. Each version bump publishes a migration note and a count of evidence downgraded.
5. **Supported versions.** Each release lists the versions it still supports. Evidence at a retired version is `unverified` with reason `IdentityVersionRetired`.

## Verification Semantics

- `scid` equality is **necessary, never sufficient**. A `qualification: qualified` status (F) also needs F's gates. A `performance: verified` status (G's rules, applied by A) also needs matching infrastructure profile, provenance, load coverage, target and freshness ([[Empirical Map & Evidence-Informed Routing PRD]] PD-3 to PD-6).
- A status of one type is never evidence for another ([[Verification Status Vocabulary]]). A qualified `scid` may be *offered*; it is not thereby `performance: verified`.
- A running deployment whose observed configuration no longer yields its recorded `scid` (for example, after an image change) has drifted. Every claim bound to the old `scid` lapses for it.

## Lifecycle States

These are the states of a **schema version**, not of an individual `scid`.

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Draft | Proposed field set under review | Proposed by G | Released |
| Current | Used for all new `scid`s | Released with golden vectors and equivalence declarations | Superseded by *N+1* |
| Supported | Still matched for existing evidence (rule 2) | Superseded | Retired |
| Retired | No longer matched; evidence becomes `IdentityVersionRetired` | Announced retirement in a release | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| GOVERNS | [[Empirical Map]] | → | Cells are keyed by `scid` |
| USES | [[Benchmark Run]] | ← | Each B3/B4 artifact carries its `scid` and identity record |
| USES | [[Model Deployment Specification]] | ← | The realised spec records its `scid` |
| DEPENDS_ON | [[Serving Runtime]] | → | Runtime, image and engine fields |
| DEPENDS_ON | [[Accelerator Class]] | → | Accelerator type and GPUs per replica |
| CONSTRAINS | [[Benchmark Evidence Chain]] | → | Defines the serving-configuration ID on the card header |

## Evidence

- Source: `source_docs`. Product-owner ruling X-2 (2026-10-10): one canonical identity, owned by G.
- Confidence rationale: `assumed`. Design only. Today the code has no configuration identity; `AcceleratorClass` and `ModelClass` are referenced by name (`RSS-Engineering/rackai@79ca4de`).

## See Also

- [[Entity Ontology Hub]]
- [[Empirical Map & Evidence-Informed Routing Tech Spec]] — computation and use
- [[Verification Status Vocabulary]]
- [[Model Lifecycle Tech Spec]] — produces `scid` at qualification
