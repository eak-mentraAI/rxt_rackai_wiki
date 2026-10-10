---
id: asm-mi350p-serving-competitive
type: assumption
status: draft
owner: performance-eng
domain: performance
aliases: [mi350p serving competitive, mi350p competitiveness, mi350p competitive with h100, rocm serving parity, mi350p comparator hierarchy]
related: [ent-gpu-amd-instinct, ent-gpu-h100, bench-amd-mi350p-qualification, val-mi350p-qualification, pol-benchmark-evidence-chain, bench-agentx-standard, asm-h200-sufficient, asm-fleet-competitiveness, met-goodput, fml-cost-per-1m-tokens, evd-inference-serving-competitors, evd-gpu-neocloud-competitors, idx-assumption-register]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "critical review of benchmarking notes (2026-10-07)", "product owner direction on comparators (2026-10-07)"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-evidence
summary: "On fitting priority workloads, RackAI on MI350P meets SLO at better economics than customers' alternatives."
---

# MI350P Serving Competitive

## Statement

> For selected RackAI priority workloads that fit the deployed MI350P topology, RackAI can deliver the workload on MI350P at a defined SLO, with performance and economics that compare favourably with what the customer would otherwise reasonably buy.

The claim is **workload-specific** and **outcome-framed**. It doesn't say MI350P beats a particular NVIDIA GPU. RackAI's positioning is the best operator for private and sovereign enterprise AI, not the fastest GPU cloud ([[Three Battlegrounds]]). So the test is whether RackAI produces a better customer outcome than a reasonable alternative. Performance is part of that outcome, not the whole of it.

It is split into three clauses, each validated independently:

| Clause | Claim | Validated at | Compared against | Status |
|--------|-------|:------------:|------------------|:------:|
| **C1 Performance** | MI350P delivers SLO-qualified goodput for the workload that holds up against relevant current alternatives | B3 (provisional) → B4 (qualified) | Comparator hierarchy levels 1–3 (below) | assumed |
| **C2 Operability** | MI350P passes the same B4 service qualification categories as any RackAI service (isolation, resilience, sovereignty) | B4 | RackAI's own service standard, not another vendor | assumed |
| **C3 Economics** | Fully loaded cost per 1M **successful** output tokens at the SLO-qualified point is favourable against what customers would otherwise buy | B5 | Comparator hierarchy level 4 | assumed |

MI350P doesn't need to win on all three. Lower peak throughput with better fully loaded economics at the same SLO can still make it the preferable platform. Higher peak throughput with worse p99 latency or unstable production behaviour isn't competitive.

## Comparator Hierarchy

Each comparison names its comparator and why that comparator is relevant to the customer claim being made.

| Level | Comparator | Answers | Notes |
|:-----:|------------|---------|-------|
| 1 | **AMD's published reference configurations** | Are our hardware, ROCm stack and serving runtime performing as expected? | Where AMD's exact configuration can't be reproduced, document the differences rather than claiming parity (see the reproduction contract in the [[Benchmark Evidence Chain]]) |
| 2 | **Our own repeatable workload baselines** | What can we actually deliver? | [[GLM 5.3 Flash]] and the standard [[Traffic Class]] profiles; repeated across runs and software versions |
| 3 | **Current NVIDIA platforms** (e.g. B200 / B300) | Where do we stand against the hardware customers see in the market? | We don't operate Blackwell ([[Fleet Inventory]]), so these comparisons use **published, comparable external data** (e.g. [[AgentX Benchmark Standard\|InferenceX]], MLPerf) normalized for model, precision, workload, concurrency and SLO. Don't force a comparison where conditions differ materially. Label it external and standard-inspired |
| 4 | **What customers would actually buy** | Is the RackAI offer better for this workload? | Hosted inference services, dedicated GPU infrastructure, self-managed deployments ([[Inference Serving Competitors]], [[GPU Neocloud Competitors]]) |

**H100 is an internal reference only.** It is legitimate for three narrow questions: validating the benchmark harness against a known baseline, migration economics for a customer currently on H100, and operational continuity with existing H100 serving configurations. It is never a headline comparison. Comparing our newest AMD capacity with an older NVIDIA generation invites the obvious "why not Blackwell?" challenge, and it lets one vendor's hardware define success.

## Comparison Views

Every comparison names its view:

| View | Question | Primary audience |
|------|----------|------------------|
| Per GPU | Which accelerator produces more useful work? | Engineering optimization |
| Per replica / node | Which deployed configuration delivers more capacity? | Infrastructure architecture |
| Per dollar at SLO | Which offer delivers better economics? | Customer positioning, pricing |

## Rationale

MI350P is a current AMD generation, and vLLM/SGLang run on ROCm. Larger per-GPU memory (to be confirmed in Pass 0) may allow a lower tensor-parallel degree on PCIe. Against that: no TensorRT-LLM or FlashAttention-3 on ROCm, a less mature kernel ecosystem, and the PCIe horizontal-scaling limit ([[Fleet Competitiveness]]). The net is unknown, and the answer will differ by workload.

## Exit Criterion

Each clause exits separately.

- **C1:** current B3 cards for MI350P, then B4 qualified goodput, compared against levels 1–3. External level-3 data counts only when its conditions match ours closely enough to state.
- **C2:** a B4 Service Qualification Record for MI350P against the RackAI service standard.
- **C3:** a B5 Economics Sheet set against a level-4 alternative that is priced for the same workload and SLO.

## Impacts

| Impacted | Type |
|----------|------|
| [[AMD Instinct]] | SUPPORTS |
| [[Tokens per GPU-Second]] | SUPPORTS |
| [[Cost per 1M Tokens]] | SUPPORTS |
| Milestone Release Map T4.S5 (engine × accelerator selection) | SUPPORTS |

## Status

- Confidence: assumed (all three clauses)
- Owner: Inference Optimization (C1, C3); Inference and Serving Services (C2)
- Target resolution: per clause, on its evidence; no date set

## See Also

- [[Evidence Hub]]
- [[Assumption Register]]
- [[Validate MI350P Qualification]]
