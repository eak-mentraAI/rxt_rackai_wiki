---
id: chg-2026-09-24-six-pillar-reorg
type: change
status: draft
owner: product
domain: strategy
aliases: [six pillar reorg, reorg 2026-09, pillar structure change]
related: [hub-org-design, hub-inference-serving, hub-model-services, hub-inference-optimization, hub-ai-governance-assurance, hub-ai-harness, hub-ai-operations-product, hub-roadmap, hub-battlegrounds, hub-governance]
source_docs: ["06-sources/RackAI Organizational Design.md", "reference/Enterprise AI Cloud - RackAI.pptx"]
confidence: derived
last_reviewed: 2026-09-24
parent: hub-wiki
summary: "Corpus update reflecting the six-pillar RackAI reorg: new hub pages, org design, working model, and entity link pass."
---

# Change: Six-Pillar Reorg — 2026-09-24

## Trigger

Organizational restructuring of RackAI (above the Kubernetes line) into six focus pillars, each with an assigned product manager and engineering lead. Trigger: BU leadership decision, reflected in `reference/Enterprise AI Cloud - RackAI.pptx` and the four external PDM JDs in `reference/jd/`.

## Source Reference

- `reference/Enterprise AI Cloud - RackAI.pptx` (org-design deck, added 2026-09-17)
- `reference/jd/EXTERNAL_PDM_Optimization_and_Efficiency_JD.md`
- `reference/jd/EXTERNAL_PDM_Orchestration_and_Harness_JD.md`
- `reference/jd/EXTERNAL_PDM_Assurance_and_Governance_JD.md`
- `reference/jd/EXTERNAL_PDM_Product_Operations_JD.md`

## Confidence

`derived` — the pillar structure reflects the proposed operating model from the org-design deck (itself `assumed`). Pillar scopes are derived from the JDs. No pillar is ratified or staffed (except Inference/Serving: Edward Kerr). Staffing and ratification will upgrade confidence to `measured`.

---

## Objects Added

| Object | ID | Type | Notes |
|---|---|---|---|
| Inference and Serving Services | `hub-inference-serving` | hub | New pillar hub |
| Model Services | `hub-model-services` | hub | New pillar hub |
| Inference Optimization | `hub-inference-optimization` | hub | New pillar hub |
| AI Governance and Assurance | `hub-ai-governance-assurance` | hub | New product pillar hub — distinct from corpus governance |
| AI Harness | `hub-ai-harness` | hub | New pillar hub |
| RackAI Organizational Design | `hub-org-design` | hub | Canonical org structure note |
| Pillar Working Model | `wiki-pillar-working-model` | hub (wiki layer) | Inter-pillar responsibility, joint decisions, escalation rules |

## Objects Modified

| Object | ID | Change |
|---|---|---|
| Governance Hub | `hub-governance` | Scope note added; product governance concepts table removed (→ AI Governance and Assurance hub); `related` updated |
| RackAI Roadmap | `hub-roadmap` | Workstream table: `Pillar` column added; workstream names aligned to pillar names |
| Three Battlegrounds | `hub-battlegrounds` | Operator stack Mermaid diagram updated: four abstract layers → six labeled pillar nodes |
| Product Hub | `hub-product` | Scope note added (OpenRouter initiative only); `related` expanded to all six pillar hubs + org design; alias added |
| AI Operations Product | `hub-ai-operations-product` | `related` updated: added `hub-org-design`, `wiki-pillar-working-model` |
| RackAI Org Design (source) | `src-rackai-org-design` | `related` updated: added `hub-org-design` backlink |

## Entity / Operations Link Pass (metadata only — `related:` additions)

28 notes received pillar hub backlinks. No content changed on any of these.

### → `hub-inference-serving`
`ent-model-deployment`, `ent-model-deployment-spec`, `ent-serving-runtime`, `ent-capacity-pool`, `ent-accelerator-class`, `ent-gpu-fleet`, `ent-gpu-cluster`, `ent-gpu-node`, `ent-traffic-class`

### → `hub-model-services`
`ent-model`, `ent-model-class`, `ent-model-catalog-endpoint`, `ent-fine-tuning-job`, `ent-lora-adapter`, `ent-dataset`

### → `hub-inference-optimization`
`ent-accelerator-class` (also serving), `ent-benchmark-run`, `ent-gpu-fleet` (also serving), `met-ttft`, `met-output-throughput`, `met-gpu-utilization`, `fml-tokens-per-gpu-second`, `fml-cost-per-1m-tokens`, `fml-gpu-hours-per-1m-tokens`, `coeff-fp8-throughput`, `coeff-kv-cache-hit-rate`, `coeff-spec-decode-acceptance`

### → `hub-ai-harness`
`ent-governed-harness`, `ent-empirical-map`, `ent-traffic-class` (also serving), `ent-agent-identity` (also governance)

### → `hub-ai-governance-assurance`
`ent-agent-identity` (also harness)

### → `wiki-pillar-working-model`
All six pillar hubs + `hub-ai-operations-product`

---

## Edges Added (key structural)

| From | Relationship | To |
|---|---|---|
| `hub-org-design` | SUPPORTS | all six pillar hubs |
| `hub-org-design` | DERIVES | `src-rackai-org-design` |
| `hub-ai-governance-assurance` | SUPPORTS | `hub-inference-serving` (tenant isolation joint) |
| `hub-ai-harness` | SUPPORTS → seam | `hub-ai-governance-assurance` (identity + verification) |
| `wiki-pillar-working-model` | SUPPORTS | all six pillar hubs |
| `hub-governance` | ROUTES_TO | `hub-ai-governance-assurance` (product scope redirect) |

## Edges Removed

| From | Relationship | To | Reason |
|---|---|---|---|
| `hub-governance` | SUPPORTS | `hub-battlegrounds` | Corpus governance hub does not drive strategy |
| `hub-governance` | SUPPORTS | `evd-sovereign-governed-competitors` | Product governance is now in `hub-ai-governance-assurance` |

---

## Consistency Pass Results

- **S-01 No duplicates:** Product governance concepts were in `hub-governance` table (not canonical) and in `02-operations/` entities. No duplicate canonical homes created — the table was a reference list, not a canonical definition. ✅
- **S-02 No orphans:** All new hub notes have owner, source, confidence, inbound links (from org design hub + roadmap + pillar peers). ✅
- **S-14 Stable IDs:** No existing IDs changed. Six new IDs assigned. ✅
- **S-15 Aliases preserved:** All existing aliases preserved. New aliases added only. ✅
- **C-02 Terminology stable:** Workstream names in roadmap aligned to pillar names. Old names preserved as aliases in pillar hub frontmatter. ✅
- **C-04 No silent redefinitions:** Governance Hub scope narrowed with explicit scope note; no content silently moved. ✅
- **C-07 Graph invariants:** All invariants hold — no entity/deployment/runtime relationships changed. ✅

---

## Open Questions Created

| Question | Affected Notes | Priority |
|---|---|---|
| Model Services: standalone PM seat or under Inference/Serving PM initially? | `hub-org-design`, `hub-model-services` | High |
| Product Operations Lead: distinct seat or split across P5/P6 + existing PMs? | `hub-org-design`, `hub-ai-operations-product` | High |
| "Measurement & Self-Improvement" workstream maps to AI Harness pillar — confirmed that Harness PM accepts ownership of eval-as-CI and loop-planning, not just routing? | `hub-roadmap`, `hub-ai-harness` | Medium |
| Fine-tuning engineering: does Model Services PM own product direction or does it remain under Inference/Serving? | `hub-org-design`, `hub-model-services` | Medium |
| UK Sovereign AI PM: seventh pillar or a go-to-market role on top of AI Governance & Assurance? | `hub-org-design` | Medium |
| Two PDM JDs still needed: Inference and Serving Services, Model Services | `hub-inference-serving`, `hub-model-services` | High |

---

## Notes Requiring Follow-Up Review

- `hub-ai-harness` — confidence `assumed`; no harness is shipped. Review when governed harness v1 delivery milestone is added to the roadmap.
- `hub-ai-governance-assurance` — confidence `assumed`; SOC 2 scoping not started. Review when certification timeline is established.
- `hub-org-design` — confidence `assumed`; proposed org, not ratified. Review when SVP ratifies pillar structure and open PM seats are filled.
- `hub-roadmap` workstream table — "Measurement & Self-Improvement" pillar assignment to AI Harness needs explicit confirmation from the Harness PM.

---

## See Also

- [[RackAI Organizational Design]] — the canonical org hub this change creates
- [[Pillar Working Model]] — the inter-pillar working model this change creates
- [[RackAI Roadmap]] — workstream table updated
- [[Three Battlegrounds]] — operator stack diagram updated
- [[Governance Hub]] — scope narrowed; product governance moved out
