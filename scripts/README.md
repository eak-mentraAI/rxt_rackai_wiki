---
id: idx-scripts-readme
type: index
status: validated
owner: knowledge-graph-steward
domain: governance
aliases: [scripts readme, lint documentation, frontmatter lint guide, link check guide]
related: [hub-root, pol-fitness-checklist]
parent: hub-root
source_docs: []
confidence: validated
last_reviewed: 2026-10-10
summary: "Documents the frontmatter lint, the link check, and how enforcement works in this wiki."
---

# Frontmatter Lint and Link Check — Guide

## Why This Exists

The operating standards define required YAML frontmatter for every note. Nothing prevents a note from being written without it, or with a non-canonical enum value. When that happens the note becomes an orphan in the knowledge graph: queries exclude it, links break, and claims propagate without traceable confidence. The lint script enforces the standard at write-time and commit-time so decay never starts.

---

## The Required Frontmatter Standard

Every markdown file in the wiki (outside `templates/`, `.kiro/`, `.obsidian/`) must begin with YAML frontmatter containing these 12 fields:

```yaml
---
id: unique-stable-id
type: entity | workflow | event | metric | formula | coefficient | policy | assumption | validation | evidence | source | hub | index | change | glossary | prd | projection | companion
status: draft | reviewed | validated | deprecated
owner: team-or-role
domain: strategy | product | platform | performance | model-enablement | infrastructure | reliability | commercial | capacity | governance
aliases: []
related: []
source_docs: []
confidence: assumed | derived | measured | validated
last_reviewed: YYYY-MM-DD
parent: parent-note-id
summary: "One-line description of note purpose."
---
```

### Enum Constraints

| Field | Valid Values |
|-------|-------------|
| `type` | `entity`, `workflow`, `event`, `metric`, `formula`, `coefficient`, `policy`, `assumption`, `validation`, `evidence`, `source`, `hub`, `index`, `change`, `glossary`, `prd`, `projection`, `companion` |
| `status` | `draft`, `reviewed`, `validated`, `deprecated` |
| `confidence` | `assumed`, `derived`, `measured`, `validated` |
| `domain` | `strategy`, `product`, `platform`, `performance`, `model-enablement`, `infrastructure`, `reliability`, `commercial`, `capacity`, `governance` |

---

## The Lint Script

### Location
```
scripts/lint-frontmatter.sh
```

### What It Checks
1. File starts with `---` (frontmatter delimiter present)
2. All 12 required fields exist within the frontmatter block
3. `type`, `status`, `confidence`, and `domain` values are in their canonical enum lists

### Usage
```bash
# Lint all markdown files in the repo
./scripts/lint-frontmatter.sh

# Lint a single file
./scripts/lint-frontmatter.sh path/to/file.md

# Lint multiple specific files
./scripts/lint-frontmatter.sh file1.md file2.md file3.md
```

### Exit Codes
| Code | Meaning |
|:---:|---|
| 0 | All files pass validation |
| 1 | One or more files have violations |

`templates/`, `.kiro/`, `.obsidian/`, and `.git/` are excluded — templates intentionally contain placeholder enum values (`type: entity | ...`) that are not valid final values. `reference/` is also excluded (raw context material for AI agents, no frontmatter by design), except `* - Companion.md` files, which are structured notes and are linted. This applies both to full-repo runs and to files passed explicitly (so the pre-commit hook skips them too).

---

## The Editor Hook (Kiro)

A `PostFileSave` hook runs the lint automatically whenever a `.md` file is saved:

```
.kiro/hooks/lint-frontmatter-on-save.json
```

It triggers on every `.md` save, runs the lint against the saved file only, and prints violations into the session context. It does not block the save (advisory).

---

## Pre-commit Enforcement

Commit-time enforcement is provided by a git `pre-commit` hook that lints the **staged** `.md` files and **blocks** the commit on any violation (missing field, invalid enum, or over-length summary).

Because `.git/hooks/` is not version-controlled, the hook is installed from a tracked script. After cloning, run once:

```bash
./scripts/install-git-hooks.sh
```

This writes `.git/hooks/pre-commit`, which runs:

```bash
# staged .md paths, read NUL-delimited so filenames with spaces are linted
git diff --cached --name-only --diff-filter=ACM -z  →  ./scripts/lint-frontmatter.sh "${STAGED[@]}"
```

- Only staged/changed markdown is checked (fast; won't fail on pre-existing violations elsewhere).
- A non-zero lint exit aborts the commit.
- Emergency bypass (use sparingly): `git commit --no-verify`.

To change what the hook does, edit `scripts/install-git-hooks.sh` and re-run it — not `.git/hooks/pre-commit` directly — so the hook stays reproducible across clones.

> **Note:** the hook enforces the same rules as the knowledge-platform ingestion schema (including `summary` ≤ 120 chars). Over-length summaries are silently dropped as unstructured shadow nodes on ingestion, so blocking them at commit-time keeps notes renderable in the console.

---

## Link Check

The Knowledge Console renders every `[[wiki link]]` and relative `.md` link in a note body as a link to the object it references. A link that doesn't resolve renders as dotted-underlined dead text, so this corpus is kept at **zero unresolved links**.

### Location
```
scripts/lint-links.sh
.kiro/hooks/lint-links-on-save.json
```

The script wraps the platform's checker (`packages/ingestion/src/check-links.ts` in the knowledge-platform repo). It expects this corpus at `knowledge-platform/corpora/rackai`; otherwise set `KNOWLEDGE_PLATFORM_ROOT` to your platform checkout. It always scans the whole corpus (resolution needs every note). The Kiro hook runs it after every `.md` save (advisory, does not block the save).

### Usage
```bash
./scripts/lint-links.sh                      # must report 0 unresolved
MAX_UNRESOLVED=3 ./scripts/lint-links.sh     # temporary tolerance while cleaning up
```

Exit codes: `0` all links resolve, or the platform checker was not found (check skipped; prints `SKIP:` to stderr), `1` unresolved links (listed by file).

### Link Contract

Targets resolve case-insensitively, in this order: (1) object `id`, (2) frontmatter `aliases`, (3) file name or path without `.md`, (4) the note's H1 title, (5) slug/hyphenated variants.

- **Prefer ID-pinned links** for anything that may be renamed: `[[ent-model-deployment|Model Deployment]]`.
- `[[Target#Heading]]` and `[[Target|Display]]` are supported; inside a table cell escape the pipe: `[[Target\|Display]]`.
- Links inside inline code or code fences are ignored — use backticks to talk *about* a note that doesn't exist yet or about link syntax.
- A note whose frontmatter fails platform validation (e.g. `summary` over 120 characters) becomes a shadow object: it resolves only by file name/path, not by `id` or alias.
- To fix an unresolved link: point it at an existing id, add the link text to the target's `aliases`, or make it plain text if the target doesn't exist.

Full contract: `docs/CORPUS_COMPLIANCE_GUIDE.md` → "Wiki Links (Cross-References)" in the knowledge-platform repo.

To enforce at commit time, add `./scripts/lint-links.sh || exit 1` to the pre-commit hook above.

---

## Adjusting the Enums

If a new canonical type or domain is introduced, edit the variables at the top of `lint-frontmatter.sh`:

```bash
VALID_TYPES="entity|workflow|event|..."
VALID_STATUS="draft|reviewed|validated|deprecated"
VALID_CONFIDENCE="assumed|derived|measured|validated"
VALID_DOMAIN="strategy|product|platform|..."
REQUIRED_FIELDS="id type status owner domain confidence last_reviewed aliases related source_docs parent summary"
```

Keep these in sync with `.kiro/steering/rackai-operating-standards.md`. The steering file defines the rules; the lint enforces them; the hook makes enforcement frictionless.

---

## Graph Query Tool — `scripts/kg.py`

Fast, read-only knowledge-graph lookups over the working tree (Python stdlib, no install). It resolves both link systems — frontmatter IDs (`id` / `parent` / `related`) and body `[[wikilinks]]` (by filename, vault path, id, H1 title, or alias) — plus typed edges from `## Relationships` tables.

```bash
python3 scripts/kg.py find <text>     # id/title/alias, then summary matches
python3 scripts/kg.py show <ref>      # frontmatter + section headings (no body) — then read only the needed section
python3 scripts/kg.py out <ref>       # parent, related IDs, typed Relationship edges, other links
python3 scripts/kg.py in <ref>        # children, typed inbound edges, related-by, backlinks (propagation impact)
python3 scripts/kg.py children|type <type> [domain]|hubs|broken|stats   # add --json for machine output
```

Use it before bulk-reading files: `find` → `show` → read one section → expand with `out` / `in`. `broken` lists unresolved references (fitness check S-03). The same file is shared verbatim across the sister wikis; the canonical copy lives in RackAI Wiki.


## lint-prd-spec.py

Checks `type: prd` / `type: spec` notes against the canonical roadmap table (Fitness P-09, T-09, T-10):
- every roadmap item a PRD or spec names exists in `05-wiki/RackAI Roadmap.csv`
- each of those rows links the note back in its `PRD` / `Tech spec` column
- every link in those columns resolves to a real note of an allowed type
- every tech spec has a read-only Codebase Grounding section citing `RSS-Engineering/<repo>@<sha>`, with all six subsections

Run with `python3 scripts/lint-prd-spec.py`. The pre-commit hook runs it too.
