---
id: asm-traffic-follows-performance
type: assumption
status: draft
owner: performance-eng
domain: performance
aliases: [traffic follows performance, openrouter traffic response]
related: [hub-evidence, asm-spec-decode-beneficial, asm-h200-sufficient]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Belief that improving TTFT, throughput, uptime, and price increases Rack AI's OpenRouter traffic share — awaiting observed response."
---

# OpenRouter Traffic Follows Performance

## Statement

Improving TTFT, throughput, uptime, and price will increase Rack AI's OpenRouter traffic share.

## Rationale

OpenRouter states that requests are routed on latency, throughput, uptime, and price, and that providers which perform well receive proportionally more traffic — see [OpenRouter: become a provider](https://openrouter.ai/providers/apply). Quantization is also a published provider-performance signal. If routing behaves as described, measured performance gains should translate into more routed traffic. The size and timing of that response for Rack AI specifically is unobserved. Content was rephrased for compliance with licensing restrictions.

## Exit Criterion

Observed OpenRouter traffic-share response following a measured performance improvement on a live priority model (Phase 2 production + Phase 3 competitive benchmark pipeline). Until then this remains `assumed`.

## Impacts

| Impacted | Type |
|----------|------|
| [[OpenRouter Provider Integration]] | SUPPORTS |
| [[Productive GPU Utilization]] | SUPPORTS |
| [[OpenRouter Price]] | CONSTRAINS |

## Status

- Confidence: assumed
- Owner: performance-eng
- Target resolution date: TBD (Phase 2 launch + Phase 3 competitive pipeline)

## See Also

- [[Evidence Hub]]
- [[Assumption Register]]
