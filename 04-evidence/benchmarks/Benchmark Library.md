---
id: idx-benchmark-library
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [benchmark library, benchmark register, benchmark run register]
related: [hub-evidence, bench-deepseek-h200-fp8, bench-agentx-standard, val-deepseek-h200-fp8, idx-fleet-inventory, pol-benchmark-evidence-chain, bench-amd-mi350p-qualification]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-evidence
summary: "Register of planned and pending Benchmark Runs — no measured results exist yet."
---

# Benchmark Library

## Purpose

The register of all [[Benchmark Run]] definitions and their status. This is an **index of intent**, not a results archive. Per the [[Evidence Hub]] confidence framework, a roadmap target is never a measured result, so every entry here begins as `planned — no run yet`. Rows become `measured` only once the harness executes and data is recorded on the individual evidence note.

> No benchmark has been run. All entries below are planned / illustrative to define scope; none carry measured numbers.

## Governing Standard

Every entry is governed by the [[Benchmark Evidence Chain]]. Each run declares its tier (B1–B5) and test class (standard-compliant / standard-inspired / RackAI-internal). B3+ runs cite a Validated Cluster Profile (infrastructure) and a serving configuration. Each card summarizes a retained evidence bundle (raw data, scripts, repeats). Scope follows a qualification matrix (required / conditional / not applicable profiles; standard checkpoints with early stop). Freshness follows the policy's change-impact rules. Cards without a bundle link, both version IDs, or a test class are not registered.

## Harness Dimensions

The benchmark harness (roadmap Milestone 0.4) is designed to test each priority model against candidate GPU configurations across these dimensions:

| Dimension | What It Captures |
|-----------|------------------|
| TTFT | Time to first token (P50 / P95) |
| Output tokens/sec | Generation throughput per request |
| Tokens/sec/GPU | Infrastructure efficiency per GPU |
| Prefill throughput | Prompt-processing rate |
| Concurrency scaling | Behavior as concurrent requests rise |
| Latency under load | Latency degradation under saturation |
| Context-length behavior | Effect of long context on latency/throughput |
| Tool calling | Correctness and cost of tool-call paths |
| Structured output | JSON / schema-constrained generation |
| Memory consumption | HBM footprint per configuration |
| Throughput at batch sizes | Throughput across batch configurations |
| Agentic-workload replay ([[AgentX Benchmark Standard\|AgentX]]) | Multi-turn coding-agent sessions: KV/prefix reuse, inter-turn tool time, TTFT + interactivity + throughput under a concurrency sweep |

> **External anchor.** RackAI anchors its **agentic** serving benchmarks to the SemiAnalysis InferenceX **[[AgentX Benchmark Standard]]** (run via NVIDIA AIPerf, dated-corpus-pinned) so our numbers are comparable to an external reference rather than a home-grown harness. AgentX measures serving performance only (not model quality) and is `asserted` until we execute a run on our fleet.

## Entries

Priority-model runs planned against the harness, targeting the **actual fleet** (see [[Fleet Inventory]]): [[NVIDIA H100]] first, [[AMD Instinct]] once it lands (~Oct 2026, vLLM/SGLang only — no TensorRT-LLM on ROCm), and [[NVIDIA L40S]] for staging/canary. There are no H200s. Engines under evaluation: vLLM, SGLang, TensorRT-LLM (CUDA only). Quantization candidates: FP8 (A30 has no FP8). All rows are pending — no measurements recorded.

| Run | Model | Runtime | Quantization | Hardware | Status |
|-----|-------|---------|--------------|----------|--------|
| [[DeepSeek H100 FP8 Benchmark]] | [[DeepSeek V4 Flash]] | vLLM / SGLang / TensorRT-LLM | FP8 | [[NVIDIA H100]] | planned — no run yet |
| GLM H100 FP8 (planned) | [[GLM 5.3 Flash]] | vLLM / SGLang / TensorRT-LLM | FP8 | [[NVIDIA H100]] | planned — no run yet |
| Nemotron H100 FP8 (planned) | [[Nemotron 3 Ultra]] | vLLM / SGLang / TensorRT-LLM | FP8 | [[NVIDIA H100]] | planned — no run yet |
| [[AMD MI350P Qualification Plan]] (Pass 0 → 3) | Reference model + [[GLM 5.3 Flash]] | vLLM on ROCm (primary); SGLang / AIM as challengers | FP8 if Pass 0 passes (+ BF16) | [[AMD Instinct]] MI350P (GPU count set by fit analysis) | planned — Pass 0 blocked on topology confirmation |
| DeepSeek AMD Instinct FP8 (planned) | [[DeepSeek V4 Flash]] | vLLM / SGLang (ROCm — no TensorRT-LLM) | FP8 | [[AMD Instinct]] | planned — awaiting hardware ~Oct 2026 |
| GLM AMD Instinct FP8 (planned) | [[GLM 5.3 Flash]] | vLLM / SGLang (ROCm) | FP8 | [[AMD Instinct]] | planned — absorbed into [[AMD MI350P Qualification Plan]] B3 |
| DeepSeek L40S FP8 (staging) | [[DeepSeek V4 Flash]] | vLLM / SGLang / TensorRT-LLM | FP8 | [[NVIDIA L40S]] | planned — staging/canary |
| GLM AgentX (agentic standard) | [[GLM 5.3 Flash]] | vLLM / SGLang (+ NIM/AIM as measured backends) | FP8 | [[NVIDIA H100]] → [[AMD Instinct]] | planned — [[AgentX Benchmark Standard\|AgentX]] via AIPerf |
| DeepSeek AgentX (agentic standard) | [[DeepSeek V4 Flash]] | vLLM / SGLang | FP8 | [[NVIDIA H100]] | planned — [[AgentX Benchmark Standard\|AgentX]] via AIPerf |
| Nemotron AgentX (agentic standard) | [[Nemotron 3 Ultra]] | vLLM / SGLang (+ NIM as measured backend) | FP8 | [[NVIDIA H100]] | planned — [[AgentX Benchmark Standard\|AgentX]] via AIPerf |

The register extends as additional runs, hardware configurations, or engines are added. The **AgentX** rows are the agentic-workload standard runs; the FP8 rows above them remain the fixed-sequence throughput runs. Both are needed — AgentX for agent-traffic realism, fixed-sequence for conventional request streams.

## See Also

- [[Evidence Hub]]
- [[Benchmark Run]]
- [[Benchmark Evidence Chain]]
- [[Validation Register]]
