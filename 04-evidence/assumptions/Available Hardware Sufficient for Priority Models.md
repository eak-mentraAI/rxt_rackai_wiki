---
id: asm-h200-sufficient
type: assumption
status: draft
owner: performance-eng
domain: performance
aliases: [available hardware sufficient, h100 sufficient, fleet hardware fit assumption, h200 sufficient]
related: [hub-evidence, bench-deepseek-h200-fp8, asm-fp8-quality-neutral, ent-gpu-h100, ent-gpu-amd-instinct, idx-fleet-inventory]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Belief that the current/incoming fleet (H100 now, AMD Instinct soon) can serve the priority MoE models competitively — awaiting hardware-fit and benchmark runs."
---

# Available Hardware Sufficient for Priority Models

> **Stable-ID note:** the frontmatter ID (`asm-h200-sufficient`) retains its original slug. The assumption has been corrected to the actual fleet — there are **no H200s** (see [[Fleet Inventory]]). "h200 sufficient" is kept as an alias.

## Statement

The hardware Rack AI actually has and has on order — [[NVIDIA H100]] NVL now, [[AMD Instinct]] MI350P from ~October 2026 — can serve **fitting (~27B-class) models** at competitive TTFT and throughput. It **cannot** serve frontier-class MoE models competitively; that requires SXM/UBB8 topology (see [[Fleet Competitiveness]]).

## Rationale

The binding limit is interconnect topology, not raw specs. The fleet's H100s are **NVL PCIe** — NVLink pairs only (2 coupled, 4/node, no clustering) — so a replica must fit within a small coupled group (2–4 GPUs at FP8). Fitting models in the ~27B class sit comfortably inside that and can be served well, especially with FP8 and prefix/KV caching. The incoming **MI350P** adds capacity but is also **PCIe**, so it does not raise the size ceiling. The [[NVIDIA L40S]] (48 GB GDDR6, no NVLink) and [[NVIDIA A30]] (24 GB, no FP8) are staging/small-model capacity. This is an architectural expectation, not a measured hardware-fit result; competitors on H200/Blackwell SXM hold a decisive advantage on large models.

## Exit Criterion

Automated hardware-fit testing (roadmap Milestone 4.5) plus benchmark runs (Milestone 0.4 / Phase 3) confirming minimum GPU count, memory headroom, and competitive TTFT / tokens-per-GPU-second on [[NVIDIA H100]] — and, once it lands, on [[AMD Instinct]]. Until then this remains `assumed`.

## Impacts

| Impacted | Type |
|----------|------|
| [[GPU Node]] | CONSTRAINS |
| [[Capacity Pool]] | CONSTRAINS |
| [[NVIDIA H100]] | SUPPORTS |
| [[AMD Instinct]] | SUPPORTS |
| [[DeepSeek H100 FP8 Benchmark]] | SUPPORTS |

## Status

- Confidence: assumed
- Owner: performance-eng
- Target resolution date: TBD (Phase 0 harness + Phase 4 hardware-fit; AMD after ~Oct 2026 arrival)

## See Also

- [[Evidence Hub]]
- [[Assumption Register]]
- [[Fleet Inventory]]
