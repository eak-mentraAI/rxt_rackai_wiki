---
id: asm-traffic-follows-performance
type: assumption
status: draft
owner: performance-eng
domain: performance
aliases: [traffic follows performance, openrouter traffic response]
related: [hub-evidence, asm-spec-decode-beneficial, asm-h200-sufficient, ent-market-demand, ent-openrouter-integration, met-gpu-utilization, coeff-openrouter-price, asm-openrouter-initial-share]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-evidence
summary: "Belief that better TTFT, throughput, uptime, and price raise Rack AI OpenRouter traffic share — awaiting response."
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

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| SUPPORTS | [[OpenRouter Provider Integration]] | → |  |
| SUPPORTS | [[Productive GPU Utilization]] | → |  |
| CONSTRAINS | [[OpenRouter Price]] | → | Price is one routing signal |
| SUPPORTS | [[Market Demand]] | → | Routed share follows measured performance |

## Status

- Confidence: assumed
- Owner: performance-eng
- Target resolution date: TBD (Phase 2 launch + Phase 3 competitive pipeline)

## See Also

- [[Evidence Hub]]
- [[Assumption Register]]
