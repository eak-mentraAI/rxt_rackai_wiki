---
id: idx-validation-register
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [validation register, validation index]
related: [hub-evidence, val-deepseek-h200-fp8, val-launch-lag-24h]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Register of validation items — what must be verified, each currently open."
---

# Validation Register

## Purpose

The register of validation items — claims, coefficients, and configurations that must be verified before their confidence can rise. Per the [[Evidence Hub]] framework, every item starts `open` and nothing is `validated` until confirmed against a benchmark run, telemetry, or SLO. This index is `assumed` because it describes verification intent, not results.

> No validation item has been completed. All items below are open.

## Entries

| Item | ID | Method | Status |
|------|----|--------|--------|
| [[Validate DeepSeek H100 FP8]] | val-deepseek-h200-fp8 | Benchmark harness + competitive comparison pipeline | open |
| [[Validate Launch Lag Under 24h]] | val-launch-lag-24h | Instrument Model Launch Factory + measure launch lag | open |

The register extends as items are added.

## See Also

- [[Evidence Hub]]
- [[Benchmark Library]]
- [[Open Questions]]
