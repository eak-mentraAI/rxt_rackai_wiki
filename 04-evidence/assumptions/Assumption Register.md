---
id: idx-assumption-register
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [assumption register, assumptions index, belief register]
related: [hub-evidence, idx-validation-register, idx-open-questions]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Register of stated beliefs that lack direct evidence, each with an owner and an exit criterion."
---

# Assumption Register

## Purpose

The register of assumptions baked into the strategy and roadmap that do not yet have direct evidence. Per the [[Evidence Hub]] framework, every assumption carries an owner and an exit criterion — the specific benchmark, telemetry, or vendor confirmation that would confirm or refute it. This index is `assumed` because it catalogs beliefs, not conclusions. Each item stays `assumed` until its exit criterion is met.

## Entries

| Assumption | ID | Exit Criterion (summary) | Confidence |
|------------|----|--------------------------|:----------:|
| [[FP8 Quality Neutral]] | asm-fp8-quality-neutral | Rack AI FP8-vs-BF16 quality benchmark on priority models | assumed |
| [[Available Hardware Sufficient for Priority Models]] | asm-h200-sufficient | Hardware-fit + benchmark runs on H100 / AMD Instinct | assumed |
| [[Speculative Decoding Beneficial]] | asm-spec-decode-beneficial | Acceptance rate + throughput/TTFT under production load | assumed |
| [[OpenRouter Traffic Follows Performance]] | asm-traffic-follows-performance | Observed traffic-share response to a measured gain | assumed |
| [[Fleet Competitiveness]] | asm-fleet-competitiveness | H100 benchmark vs frontier + AMD specs + capacity plan | assumed |

The register extends as new assumptions are surfaced. When an exit criterion is met, the assumption's confidence is upgraded and a [[Benchmark Library|benchmark]] or validation item records the evidence.

## See Also

- [[Evidence Hub]]
- [[Validation Register]]
- [[Open Questions]]
