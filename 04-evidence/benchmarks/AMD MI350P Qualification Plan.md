---
id: bench-amd-mi350p-qualification
type: evidence
status: draft
owner: performance-eng
domain: performance
aliases: [mi350p qualification plan, mi350p benchmark plan, mi350p first run, amd mi350p benchmarking, mi350p first-run plan]
related: [pol-benchmark-evidence-chain, ent-gpu-amd-instinct, idx-benchmark-library, ent-benchmark-run, bench-agentx-standard, asm-mi350p-serving-competitive, val-mi350p-qualification, ent-glm-5-3-flash, ent-traffic-class, idx-fleet-inventory, fml-gpus-per-replica, coeff-model-weight-footprint, asm-fp8-quality-neutral, hub-evidence]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "critical review of benchmarking notes (2026-10-07)", "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html", "https://github.com/ROCm/rccl-tests", "https://mlcommons.org/benchmarks/inference-datacenter/"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-evidence
summary: "Planned progressive qualification of the AMD MI350P fleet: fit check, then three passes across B1–B5. No results yet."
---

# AMD MI350P Qualification Plan

> **Planned — no results recorded.** This note applies the [[Benchmark Evidence Chain]] to the newly deployed [[AMD Instinct]] MI350P capacity. It defines *what should happen*. What actually happens — per-tier decisions, evidence IDs, sign-offs — is recorded in [[Validate MI350P Qualification]]. Every figure here is a target, a posture, or pending.

**Ownership.** Steward: Inference Optimization. Execution owners: per tier (Infra B1/B2; Inference Optimization B3/B5; Inference and Serving Services B4). Approval: per decision gate in the policy.

## What We Need to Prove

Not "run every benchmark", but enough to make four decisions about MI350P:

| Decision | What must be true to say yes |
|----------|------------------------------|
| Hardware acceptance | Nodes meet spec; the cluster meets agreed infrastructure requirements. Whether reproducing a named AMD reference also gates acceptance is open (D1/D3) |
| Serving selection | A specific runtime × parallelism × quantization config for [[GLM 5.3 Flash]] is the best feasible one on this topology |
| Product qualification | That config holds ratified SLOs for named traffic classes under interference and failure, inside a controlled boundary |
| Commercial qualification | Cost per 1M successful tokens at the qualified point, at realistic utilization, supports a price RackAI would accept |

The qualification answers three customer-facing objectives: **technically validated** (performs consistently against reproducible vendor and industry references), **enterprise production-ready** (sustains defined SLOs under realistic load, tenant interference and failure), and **commercially differentiated** (for which workloads RackAI offers better economics at equal quality, latency and reliability). Which comes first is decision D0.

Cross-vendor comparison is a **supporting workstream**, not a qualification objective. It follows the comparator hierarchy in [[MI350P Serving Competitive]]: AMD references, our own baselines, current NVIDIA platforms via comparable published data, then what customers would actually buy. H100 is an internal reference only.

## Pass 0 — Confirm Before Testing (gates the matrix)

No test matrix is fixed until these are answered. **D4 comes first.**

| Step | Question | Method | Owner |
|------|----------|--------|-------|
| 0.1 Topology (D4) | How many MI350P per node, how many nodes, what interconnect between GPUs (PCIe only? any bridge?), how much HBM per GPU? | Physical inventory + vendor spec, recorded in the VCP | Infra |
| 0.2 Model compatibility | Is the exact GLM 5.3 Flash revision, architecture, and weight format supported by vLLM on the pinned ROCm version? | Load + smoke test; runtime support matrix | Inference Optimization |
| 0.3 FP8 readiness | Does the runtime support this model's FP8 format with efficient ROCm kernels? Is quality acceptable vs. BF16? | Kernel path check; quality comparison per [[FP8 Quality Neutral]] | Inference Optimization + Model Services |
| 0.4 Model fit | Smallest viable GPUs per replica at each precision? KV-cache budget at target context × concurrency? | [[GPUs per Replica]] using [[Model Weight Footprint]] and measured per-GPU memory | Inference Optimization |
| 0.5 Topology choice | Expected tensor-parallel overhead over the available interconnect. Would several smaller replicas beat one wide TP deployment? Does any candidate need cross-node pipeline parallelism, and is that commercially sensible? | Analysis from 0.1 + 0.4 + B2 collective results; selects the TP candidates for Pass 2 | Inference Optimization |

Larger per-GPU memory can cut the tensor-parallel degree needed, and that can be a real serving advantage on PCIe even without a compute lead. **The goal is to optimize the deployment topology, not to benchmark a predetermined eight-GPU configuration.**

## Serving Backend Hierarchy

| Role | Backend | When it is tested |
|------|---------|-------------------|
| **Primary qualification** | vLLM on ROCm | Always. The qualified configuration is built on it |
| **Optimization challenger** | SGLang on ROCm | Only when there is a plausible performance or capability advantage for the profile (e.g. prefix-heavy agentic traffic) |
| **Product-integration challenger** | AMD AIM (RACKAI-347) | For operational integration and performance where it supports the model |
| Excluded | TensorRT-LLM, FlashAttention-3 | CUDA-only |

This separates *software-stack compatibility* (does it run?) from *competitive performance* (is it best?). Challengers do not each need a full qualification.

## Pass 1 — Baseline: the stack works

| Tier | Scope | Artifact | Exit gate |
|------|-------|----------|-----------|
| B1 | All nodes: HBM bandwidth, compute per precision, GPU–GPU P2P over the actual interconnect, 24 h power/thermal soak, error counters | Node Acceptance Records | All nodes within vendor-spec tolerance; outliers excluded |
| B2 | RCCL collectives at the GPU counts from 0.5; storage → HBM load time for reference and GLM weights; AMD reference comparison under a **reproduction contract** (named AMD published result, model, settings, permitted deviations, tolerance — fixed before running); power envelope; Accelerator Class + Capacity Pool exposure | **VCP** `VCP-MI350P-001@v1` (+ reference comparison record) | VCP accepted by Inference and Serving Services → **hardware acceptance**; reference performance validated or not, recorded separately |
| B3 (reference) | Reference model (D1), one serving config (vLLM, primary), Throughput profile, closed-loop checkpoints, ≥ 3 repeats | Reference Benchmark Card + bundle | Card registered — establishes external comparability |

## Pass 2 — Competitive serving: find the best config for GLM 5.3 Flash

| Tier | Scope | Artifact | Exit gate |
|------|-------|----------|-----------|
| B3 | GLM 5.3 Flash × **Interactive (required) + Throughput (required)**; TP/replica candidates from 0.5 only; FP8 (if 0.3 passes) vs BF16; challenger backends only where justified; closed-loop checkpoints 1/8/32/64/128 with early stop; ≥ 3 repeats | Benchmark Cards + bundles; provisional goodput with named thresholds | Default serving configuration chosen → **serving selection** decision (T4.S5); regression-gate baseline set |

## Pass 3 — Enterprise readiness: can it be sold and operated

| Tier | Scope | Artifact | Exit gate |
|------|-------|----------|-----------|
| B3 (conditional) | Long Context / RAG — *if* GLM is offered at long context; Agentic via [[AgentX Benchmark Standard\|AgentX]] — *if* it is targeted at agent workloads | Cards | Profile in or out of the supported service profile |
| B4 | Chosen config: open-loop arrival-rate sweep; **performance isolation** (aggressor/victim, quota enforcement, fairness, tenant-boundary tests); **operational resilience** (replica kill, node drain, rollback, model switch, 24–72 h soak, failed-request behavior); **private/sovereign operation** (egress audit, controlled registries, artifact provenance, management-plane/support-access dependencies) | Service Qualification Record (may be *qualified with restrictions*) | Ratified SLOs (D2) met → **product qualification** decision (launch-readiness gate) |
| B5 | At the SQR operating point: cost per 1M successful output tokens, tokens/GPU-hour, usable capacity at SLO, utilization and idle-allocation assumptions, demand-pattern assumption, energy cost from measured J/token | Economics Sheet (confidence ≤ [[Cost per GPU-Hour]], `assumed` today) | → **commercial qualification** decision |

### Scope matrix (initial)

| Profile | Reference model | GLM 5.3 Flash |
|---------|-----------------|---------------|
| Interactive | not applicable (Pass 1 is a stack check) | **required** (Pass 2) |
| Throughput | **required** (Pass 1) | **required** (Pass 2) |
| Long Context / RAG | not applicable | conditional — if offered at long context |
| Agentic | not applicable | conditional — if targeted at agent workloads |

This starts at 1 reference card plus GLM × 2 profiles × the TP candidates that survive Pass 0, not a full 4-profile × 5-rung × 4-TP grid. The matrix expands only when a result would change a decision.

## Benchmark Card Skeleton (pending)

`MI350P × <n from 0.5> | VCP-MI350P-001@v1 | serving config <id> (vLLM <ver>, image <digest>) | GLM 5.3 Flash <rev> | FP8 <format> | Interactive | closed-loop | harness <name@ver> | workload set <date> | test class standard-inspired`

| Concurrency | TTFT p95 | TPOT p95 | Provisional goodput | tok/s/GPU | GPU util | J/token | Variance |
|:-----------:|:--------:|:--------:|:-------------------:|:---------:|:--------:|:-------:|:--------:|
| 1 | pending | pending | pending | pending | pending | pending | pending |
| 8 | pending | pending | pending | pending | pending | pending | pending |
| 32 | pending | pending | pending | pending | pending | pending | pending |
| 64 | pending | pending | pending | pending | pending | pending | pending |
| 128 | pending | pending | pending | pending | pending | pending | pending |

Concurrency here means **concurrent requests**, not users.

## What We Will Be Able to Say — and When

| After | Claim (posture, not result) |
|-------|-----------------------------|
| Pass 1 / B2 | "MI350P capacity is deployed and validated." Once reference performance is validated: "it reproduces <named AMD reference> within <tolerance> on our cluster." |
| Pass 2 / B3 | "GLM 5.3 Flash on MI350P (<config>) achieves <card values> for Interactive and Throughput" — with full header and test class. |
| Pass 3 / B4 | "SLO-qualified for <profiles> at <operating point>, under tenant interference and failover, with no uncontrolled egress" — including any restrictions. |
| Pass 3 / B5 | "At that SLO, ~$<X> per 1M successful tokens at <utilization> (`assumed` — cost model pending)." User counts only with a stated user model (arrival rate, think time, active fraction). |

## Validates

| Claim / Object | ID | Tier | Confidence after |
|----------------|----|------|------------------|
| [[AMD Instinct]] topology/memory attributes | ent-gpu-amd-instinct | Pass 0 / B2 | measured |
| [[FP8 Quality Neutral]] (GLM on ROCm FP8) | asm-fp8-quality-neutral | Pass 0.3 | partially |
| [[Tokens per GPU-Second]], [[TPOT]], [[TTFT]], [[Energy per Token]] (MI350P) | met-* | B3 | measured |
| [[FP8 Throughput Factor]] (ROCm) | coeff-fp8-throughput | B3 (FP8 vs BF16) | measured |
| [[Available Hardware Sufficient for Priority Models]] (AMD half) | asm-h200-sufficient | B3 | partially |
| [[MI350P Serving Competitive]] | asm-mi350p-serving-competitive | — | Partially: C2 at B4 directly; C1 and C3 also need comparator evidence (levels 1–4 of its hierarchy) |

## Open Decisions (in order)

Also: inventory existing MI350P evidence (vendor, engineering, earlier tests) before Pass 1, and reuse what meets the evidence-bundle bar (policy rule 12).

| # | Decision | Owner | Blocks |
|---|----------|-------|--------|
| **D0** | What customer claim are we trying to earn with MI350P first: technically validated, enterprise production-ready, or commercially differentiated? (All three eventually; this sets the order and the minimum evidence) | Leadership | Pass ordering, initial scope |
| **D4** | MI350P quantity, per-GPU HBM, node topology, interconnect — **first technical decision** | Infra | Pass 0, VCP, all sizing |
| **D1** | Reference model (Llama-70B class vs gpt-oss class), the reproduction contract (published result, conditions, tolerance), and whether reference validation gates infrastructure acceptance or serving qualification — after 0.2 compatibility | Inference Optimization + Infra | Reference comparison, reference card |
| **D3** | Who runs the B2 vendor-reference reproduction | Infra + Inference Optimization | VCP acceptance |
| **D2** | Profile shapes and per-profile SLO thresholds — needed before anyone claims qualified goodput | Product (PM Inference/Serving) | Pass 3 / B4 |

All are recorded in [[Open Questions]].

## See Also

- [[Benchmark Evidence Chain]] · [[Validate MI350P Qualification]] · [[MI350P Serving Competitive]]
- [[Benchmark Library]] · [[AMD Instinct]] · [[AgentX Benchmark Standard]]
- [[GPUs per Replica]] · [[Model Weight Footprint]] · [[Fleet Inventory]] · [[Fleet Competitiveness]]
- [[Evidence Hub]]
