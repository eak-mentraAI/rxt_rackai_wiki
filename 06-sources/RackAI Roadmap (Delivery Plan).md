---
id: src-rackai-delivery-roadmap
type: source
status: validated
owner: rackai-product
domain: platform
aliases: [delivery roadmap, rackai delivery plan, software delivery plan, csp platform layer, rackai m2, roadmap xlsx, the roadmap]
related: [hub-roadmap, hub-product, src-engineering-roadmap, src-rackai-dev-plan, idx-openrouter-integration-plan, idx-capability-gap-register, src-rackai-org-design]
source_docs: ["reference/RackAI - Roadmap.xlsx", "reference/rackai-roadmap-csv/"]
confidence: measured
last_reviewed: 2026-09-21
parent: hub-roadmap
summary: "Companion of the delivery-roadmap xlsx: CSP Platform Layer, RackAI M2 features, and Uniphore Phase 1, with Jira/dates."
---

# RackAI Delivery Roadmap (Software Delivery Plan)

> **Companion note.** Faithful markdown projection of `reference/RackAI - Roadmap.xlsx` — the **actual, staffed, Jira-tracked delivery roadmap** the engineering teams are executing. Per-sheet CSVs are stored alongside at `reference/rackai-roadmap-csv/` (the diffable source of truth). This is a *source projection*, not a canonical note; concepts are extracted into the graph separately and tracked in [[Source Inventory]] and [[Source-to-Concept Crosswalk]].
>
> **Confidence:** `measured` — this is real delivery data (status, owners, Jira IDs, dates, man-week effort). Per the truth hierarchy, **shipped reality here beats planned capability** in the strategy sources: where this shows a capability Complete/In Progress, it corrects the planned/`assumed`/`missing` states elsewhere in the corpus.

The workbook has 7 sheets. The three delivery sheets are below; the questions and action tracker are summarized at the end. **Native milestone numbering (IAC M1–M4, Platform M1–M4, etc.) and Jira IDs are preserved** so the corpus stays traceable to Jira.

## 1. CSP Platform Layer — real schedule (Jun 2026 – Feb 2027)

Per "CSP Project Plan – FINAL": Identity, Monitoring, Metering, Auditing, Observability. Effort in man-weeks; dates are week-start (Mon). Source: `reference/rackai-roadmap-csv/rackai-2026-roadmap.csv`.

| Workstream | M# | Deliverable | Jira | Owner | Status | Effort | Start → End | Depends on |
|-----------|----|-------------|------|-------|--------|:------:|-------------|------------|
| IAC | M1 | JWT + API-key validation, identity context headers, APIKey CRD, Gateway auth | RACKAI-204 | Erik Ljungstrom | **Complete** | 2 | 7/6 → 7/17 | — (day-one foundation) |
| IAC | M2 | PlatformRole + RoleBinding CRDs, Authorization Service, RBAC enforcement | RACKAI-333 | Erik Ljungstrom | **Complete** | 1 | 7/20 → 7/24 | IAC M1 |
| IAC | M3 | Audit Log query API, sensitive-access logging, login events, APIKey lifecycle events | RACKAI-351 | Erik Ljungstrom | **Complete** | 1 | 7/27 → 7/31 | IAC M2 |
| IAC | M4 | Metering/billing/quota/observability permission integration, org-level RBAC | — | — | **Won't Do** | 3 | 8/3 → 8/21 | IAC M3 |
| Platform | M1 | Prometheus Operator, DCGM, node-exporter, AlertManager, Grafana, GPU/cluster dashboards | RACKAI-353 | Abhimanyu Sharma | In Progress | 4 | 7/13 → 8/3 | — |
| Platform | M2 | Aurora service metrics (Gateway/Auth/Quota), tenant-attributed dashboards, metering pipeline lag metric | RACKAI-350 | Abhimanyu Sharma | In Progress | 3 | 8/3 → 8/21 | Platform M1 |
| Platform | M3 | Loki log aggregation, structured log fields (tenant/project/service), AlertManager e2e | RACKAI-431 | Abhimanyu Sharma | In Progress | 6 | 8/24 → 9/28 | Platform M2 |
| Platform | M4 | VictoriaMetrics remote-write, 13-month retention, FineTuningJob Controller metrics | RACKAI-432 | Abhimanyu Sharma | In Progress | 3 | 10/5 → 10/19 | Platform M3 |
| Metering | M1 | Project CRD + usage_records schema + MeteringEvent queue; full pipeline w/ identity context, inference metering, FineTuningJob CRD | RACKAI-352 | Rohit Rajak | In Progress | 8 | 7/27 → 9/14 | IAC M1 (identity) |
| Metering | M2 | UsageSummary + UsageRecord APIs, historical usage, usage:view enforcement, FineTuningJob metering | — | — | Not Started | 2 | 9/14 → 9/21 | Metering M1, IAC M2 |
| Metering | M3 | QuotaPolicy CRD, soft quota alerts | — | — | Not Started | 4 | 9/28 → 10/19 | Metering M2 |
| Metering | M4 | Quota Enforcement Service, Redis counters, pre-execution admission control (429/402) | — | — | Not Started | 1 | 10/26 | Metering M3 |
| Auditing | M1 | Audit Service core (Redis Streams, PostgreSQL audit-001), audit-003 CRD fields, request_id; K8s admission webhook, proposed-actor flow, FineTuningJob audit events | — | Team Audit/Obs | Not Started | 7 | 8/17 → 9/28 | IAC M1 (soft), Gateway request_id |
| Auditing | M2 | audit-002 migration, audit-004 deletion fields, Pattern A controllers, quota/dataset/config audit logs, deletion events, finalizers | — | Team Audit/Obs | Not Started | 2 | 10/5 → 10/12 | Audit M1; Pattern A (IAC+Metering) |
| Auditing | M3 | Billing audit, compliance validation | — | Team Audit/Obs | Not Started | 3 | 10/19 → 11/2 | Audit M2 |
| Observability | M1 | Metrics API (inference latency/rate/errors, quota utilization), Workload Status API | — | Team Audit/Obs | Not Started | 3 | 9/14 → 9/28 | IAC M2 + Platform M1 ⭐ crit-path |
| Observability | M2 | Logs API (Loki proxy), Alert Rule CRUD, 60s evaluation loop, webhook delivery | — | Team Audit/Obs | Not Started | 5 | 10/5 → 11/2 | Obs M1, Platform M3 |
| Maintenance | — | Ongoing product maintenance & support | — | Product | Not Started | 35 | 6/29 → 2/22 | Continuous |

## 2. RackAI M2 Features (sprints S4–S11, ~46–50 man-weeks)

Product feature delivery from the "RackAI M2" sheet, anchored to July. Source: `reference/rackai-roadmap-csv/rackai-m2.csv`.

| Feature | Sprint | Jira | Owner | Status | Pri | Effort |
|---------|--------|------|-------|--------|:---:|:------:|
| Inference routing (llm-d, ingress→llm-d→model, shared KV cache) | S4–S5 | RACKAI-311 | Neelava Chatterjee | In Progress | 1 | 4 |
| API Layer Validation | S4 | RACKAI-261 | Ajay Bedre | **Complete** | 1 | 1 |
| CODB: Upgrade KServe and friends | S4 | RACKAI-258 | Neelava Chatterjee | **Complete** | 1 | 1 |
| CODB: Fix FT to be context parallel | S4 | RACKAI-340 | Rajendra Gosavi | **Complete** | 1 | 3 |
| CODB: Model parameter / recipe enhancements | S4 | RACKAI-269 | Unassigned | Not Started | 1 | 1 |
| AMD+NVIDIA node support | S4 | RACKAI-263 | Rajendra Gosavi | Not Started | 1 | 2 |
| Accelerator selection phase 3 | S5 | RACKAI-336 | Kim Nguy | **Complete** | 1 | 2 |
| AMD AIM engine integration | S5–S8 | RACKAI-347 | Neelava Chatterjee | In Progress | 2 | 8 |
| Observability for RackAI user | — | — | — | (planned) | 2 | 4 |
| Speculative Decoding | S6 | RACKAI-67 | Alberto Ferrer | In Progress | 3 | 2 |
| DPO fine tuning | S6–S7 | RACKAI-252 | Deshna Shah | In Progress | 3 | 4 |
| SLM support | S7 | RACKAI-360 | Unassigned | Not Started | 4 | 2 |
| Refrag | S8 | RACKAI-374 | Unassigned | In Progress | 4 | 2 |
| Dataset Management Improvement | S8–S9 | RACKAI-385 | Unassigned | In Progress | 4 | 4 |
| Synthetic Data Generation | S9–S10 | RACKAI-380 | Unassigned | In Progress | 5 | 4 |
| AI Performance Benchmarks (internal benchmarking process) | S9–S10 | — | — | Not Started | 5 | 4 |
| Request new model support | TBD | RACKAI-354 | Ajay Bedre | In Progress | — | 2 |
| Fine Tuning — checkpointing + resume | TBD | RACKAI-379 | Alberto Ferrer | Not Started | — | — |
| Model Performance Benchmarking in RackAI | TBD | RACKAI-382 | Unassigned | In Progress | — | — |
| Sunsetting a model in RackAI | TBD | RACKAI-372 | — | Not Started | — | — |
| **GPU node access support** | TBD | — | — | Not Started (backlog) | 6 | — |
| **Multi region support** | TBD | — | — | Not Started (backlog) | 6 | — |

Maintenance items: openCenter upgrades (Dev/Staging), Deploy Prod RackAI (RACKAI-359), end-to-end deployment automation (RACKAI-224, Dan Hand, In Progress).

## 3. Uniphore Phase 1 (MVP)

The first customer delivery. Source: `reference/rackai-roadmap-csv/uniphore-phase-1.csv`. Feature groups: Inference APIs, Inference optimization, NIM model support, Fine Tuning (SFT/LoRA), Model Registry, Authentication.

Highlights (all P0, milestone "MVP" unless noted):

- **Inference APIs** — API name standardization (Complete; `rmpai.rackspace.com`), publish API docs (In progress, Neelava), Model Deployment API + OpenAI-compat for Uniphore (Not started, pending doc), token issuance automation-friendly (In progress, Auth0), UI token management (Kim).
- **Inference optimization** — use Uniphore's optimized NIM models (Gemma 27, Mistral 24, GPT-OSS 20, Llama 3.1 8B, Llama 3.2 11B visual).
- **NIM model support** — deployment config for NIM/vLLM (In progress, Ajay), bootstrap with Uniphore NIM models, Model Deployment impl for NIM, LoRA adapters with NIM (to be scoped).
- **Fine Tuning (SFT)** — dataset mgmt file upload (In progress, Rohit); PEFT/LoRA job to generate adapters (In progress, Rajendra); training-job status; store/deploy LoRA adapters; **multi-LoRA, import/export, shared-infra deploy proposed to post-May (M?)**.
- **Model Registry** — save models to registry, out-of-box registry on RMPAI, UI workflows (first cut may be HuggingFace).
- **Authentication (M1, P1, post-May)** — remove Auth0 dependency → Zitadel, else Rackspace IDP via Keycloak.

## 4. Questions & Action Tracker

- **Questions to Uniphore** (`questions-to-uniphore.csv`): OpenAI-only APIs (yes); no Anthropic; SFT-first with PEFT/LoRA/QLoRA; NIM *models* only (not ecosystem); single-cluster for now; API + CLI a must; private model registry priority TBD.
- **Questions to RXT** (`questions-to-rxt.csv`): Delivery Platform (SNOW?), Billing, Authentication — all open.
- **Action Tracker**: BGV reports, Jira board, GitHub mirroring, publish tech spec/PRD, stand-ups, Teams channel.
- **Future ideas / requirements**: token accounting; NIM-vs-vLLM deployment-time toggle.

## Reading This Against the Strategy

The [[RackAI Roadmap]] (canonical) applies the operator four-proofs lens *to* this delivery plan and proposes strategy-driven changes to it. This note is the ground-truth input; the canonical roadmap is where the strategic reading and proposals live. Notable seams the operator lens surfaces (detailed there): IAC M4 "Won't Do" (org-level RBAC dropped), no governed-harness / MOE / estate concept in delivery yet, no compliance-attestation milestone, multi-region backlogged, billing still an open question to RXT.

## See Also

- [[RackAI Roadmap]] — canonical roadmap + strategic reading
- [[Rack AI OpenRouter Engineering Roadmap]] · [[RackAI Enterprise AI Development Plan]] — the strategy-side spines
- [[Capability Gap Register]] — shipped-vs-planned (to be reconciled against this)
- [[Source Inventory]] · [[Source-to-Concept Crosswalk]]
