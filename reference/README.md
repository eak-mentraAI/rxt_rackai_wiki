# Reference Material

Authoritative source documents that feed the knowledge base. These are **raw inputs**, not canonical notes — the graph in `01-entities/` … `05-wiki/` is the projection of what these say. Every concept extracted from a file here is registered in [[Source Inventory]] and [[Source-to-Concept Crosswalk]].

## Layout

| Folder | Contents |
|--------|----------|
| `rackai-platform/` | Authoritative RackAI platform docs: PRDs, technical specs, product/console/CLI docs, API reference, deployment & environment docs. Copied from the RackAI documentation set; treated as the source of truth for the RackAI platform. |
| `openrouter/` | OpenRouter concepts & provider-onboarding reference (the initiative that sits on top of the platform), plus private working annotations. |

## Notes

- The RackAI web UI codebase (`rackai-ui-main`) is **not** copied here. Its architecture was extracted into canonical notes and a source entry; the code itself lives in the RackAI repo.
- Files named `*.annotations.md` are private working commentary and are git-ignored — they are not part of the knowledge base.
- Binary docs (`.docx`) are kept as-is per the operating standard (reference a filename rather than embedding when a source can't be expressed as markdown/Mermaid).
