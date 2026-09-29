---
id: bench-agentx-standard
type: evidence
status: draft
owner: performance-eng
domain: performance
aliases: [agentx, agent-x, inferencex agentx, semianalysis agentx, agentx mvp, agentx benchmark standard]
related: [hub-evidence, idx-benchmark-library, ent-benchmark-run, ent-serving-runtime, ent-empirical-map, ent-glm-5-3-flash, ent-traffic-class, hub-roadmap]
source_docs: ["https://inferencex.semianalysis.com/agentx", "https://inferencex.semianalysis.com/glossary/agentx", "https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inference-x-agent-x-mvp-benchmark"]
confidence: asserted
last_reviewed: 2026-09-28
parent: hub-evidence
summary: "External serving-benchmark standard (SemiAnalysis InferenceX AgentX) RackAI anchors its agentic-workload benchmarking to."
---

# AgentX Benchmark Standard

> **This note describes an *external* standard, not a RackAI run.** Confidence is `asserted` — the methodology and figures below are SemiAnalysis/NVIDIA published claims we have not independently verified. It does **not** upgrade to `measured`; a RackAI AgentX run is a separate [[Benchmark Run]] entry in the [[Benchmark Library]] that lands `measured` once executed on our fleet. *Content rephrased for compliance with licensing restrictions.*

## What AgentX Is

**AgentX** (part of SemiAnalysis's **InferenceX** effort) is an external benchmark standard for measuring how an **inference-serving system** behaves under realistic **agent traffic** — specifically multi-turn coding-agent sessions — rather than under synthetic single-turn prompts. RackAI's decision (2026-09-28) is to **anchor our serving-performance benchmarking to this standard** rather than invent a home-grown one, so our numbers are comparable to an external, credible reference.

> **Disambiguation.** This is the *serving* AgentX ([SemiAnalysis InferenceX](https://inferencex.semianalysis.com/agentx)). It is **not** the unrelated model-capability benchmark of the same name ([Agent-X, MBZUAI, arXiv 2505.24876](https://arxiv.org/html/2505.24876v1)) for vision-centric multimodal reasoning. Only the serving one is relevant to RackAI's operator/economics thesis.

## How an AgentX Run Is Built

Per the [published methodology](https://inferencex.semianalysis.com/agentx), a run is constructed in four stages:

| Stage | What happens |
|-------|--------------|
| **Capture** | An opt-in proxy records request/response timing, token counts, and conversation + subagent IDs from real Claude Code sessions. |
| **Transform** | Original prompts, source code, and tool arguments/results are stripped; inputs become session-scoped chained hashes in 64-token blocks that preserve matching prefixes without revealing content. |
| **Reconstruct** | The harness fills those blocks with deterministic synthetic tokens and rebuilds each session as a DAG of main-agent turns, parallel subagents, and inter-turn tool time. |
| **Replay & measure** | A seeded warmup establishes cache state, then each configuration is profiled (one hour, closed-loop, across a concurrency sweep); cache-bust markers stop unrelated sessions sharing prefixes. |

**v1.0 dataset (asserted):** ~393 Claude Code sessions, median ~142k input tokens/request, median ~444 output tokens/request, ~44% of sessions using subagents; a `full` set (contexts to ~1M tokens) and a `256k` context-limited variant. Reproducible runs pin a dated corpus drop.

**Tooling:** an implementation ships in NVIDIA's AIPerf as `--scenario inferencex-agentx-mvp`, which locks the replay rules (preserve original request timing, no early stop, warm the cache before measuring, etc.) and stamps a `submission_valid` field so two teams' runs are comparable ([NVIDIA AIPerf](https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inference-x-agent-x-mvp-benchmark)). Status there is a work-in-progress MVP; the spec may still change.

## What It Measures — and What It Doesn't

| Measures (serving performance) | Does **not** measure |
|--------------------------------|----------------------|
| Throughput under agent traffic; TTFT; interactivity; behavior across a concurrency sweep; agentic throughput per provisioned power | **Model quality / correctness** — synthetic payloads can't judge whether the answer was right |

Two reading rules from the source: report **throughput together with TTFT and interactivity** (a single latency number doesn't describe the run), and only compare AgentX runs against other AgentX runs at compatible settings.

## Why RackAI Anchors to It

1. **It tests our actual bet.** [[GLM 5.3 Flash]] is the win-now **coding/agentic** model; AgentX *is* a coding-agent serving benchmark — a far better yardstick for it than abstract single-turn scores.
2. **It stresses what our KV-cache work is about.** AgentX rewards **shared-prefix reuse** and long-context KV pressure — exactly why "shared KV cache is rudimentary today" matters and why SGLang (RadixAttention) is the shared-prefix engine in [[Serving Runtime]].
3. **It is the honest referee for the engine question.** It can produce the *measured* vLLM-vs-AIM-vs-NIM delta on our own hardware that the AIM/NIM strategy debate currently lacks — turning an armchair guess into a cell in the [[Empirical Map]].
4. **Its method mirrors the Empirical Map's own discipline.** AgentX keeps **traffic shape** (lengths, timing, topology, KV-reuse) and **discards prompts/code/payloads** — the same transferable-vs-content split the Empirical Map relies on. That is external validation that "characterize the workload without keeping its content" is an accepted technique, which bears directly on kill criterion **K2**.

## Honest Limits

- **External and `asserted`** — every figure here is SemiAnalysis/NVIDIA's claim, unverified by RackAI. No number here is `measured`.
- **Serving performance only** — an AgentX cell fills the **cost/performance** side of an Empirical Map cell; the **reliability** side still needs [[Verification]].
- **MVP / moving spec** — the AIPerf implementation is a work-in-progress; pin a dated corpus drop for any comparable run.
- **Provider-side opacity** — the client can't see chat templates, proprietary tokenizers, server tools, or exact image/document token expansion; AgentX uses deterministic placeholders for these.

## Exit Criterion (asserted → measured)

This note stays `asserted`. Running AgentX (via AIPerf, dated-corpus-pinned) against a priority model on our fleet creates a `measured` [[Benchmark Run]] in the [[Benchmark Library]] and is what feeds the [[Empirical Map]] and the M2 AI Performance Benchmarks milestone.

## See Also

- [[Evidence Hub]]
- [[Benchmark Library]]
- [[Serving Runtime]]
- [[Empirical Map]]
- [[RackAI Roadmap]]
