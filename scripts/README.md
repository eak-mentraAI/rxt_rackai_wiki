---
id: idx-scripts-readme
type: index
status: validated
owner: knowledge-graph-steward
domain: governance
aliases: [scripts readme, lint documentation, frontmatter lint guide]
related: [hub-root, pol-fitness-checklist]
parent: hub-root
source_docs: []
confidence: validated
last_reviewed: 2026-09-03
summary: "Documents the frontmatter compliance lint and how enforcement works in this wiki."
---

# Frontmatter Compliance Lint — Guide

## Why This Exists

The operating standards define required YAML frontmatter for every note. Nothing prevents a note from being written without it, or with a non-canonical enum value. When that happens the note becomes an orphan in the knowledge graph: queries exclude it, links break, and claims propagate without traceable confidence. The lint script enforces the standard at write-time and commit-time so decay never starts.

---

## The Required Frontmatter Standard

Every markdown file in the wiki (outside `templates/`, `.kiro/`, `.obsidian/`) must begin with YAML frontmatter containing these 12 fields:

```yaml
---
id: unique-stable-id
type: entity | workflow | event | metric | formula | coefficient | policy | assumption | validation | evidence | source | hub | index | change | glossary
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
| `type` | `entity`, `workflow`, `event`, `metric`, `formula`, `coefficient`, `policy`, `assumption`, `validation`, `evidence`, `source`, `hub`, `index`, `change`, `glossary` |
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

`templates/`, `.kiro/`, `.obsidian/`, and `.git/` are excluded — templates intentionally contain placeholder enum values (`type: entity | ...`) that are not valid final values.

---

## The Editor Hook (Kiro)

A `PostFileSave` hook runs the lint automatically whenever a `.md` file is saved:

```
.kiro/hooks/lint-frontmatter-on-save.json
```

It triggers on every `.md` save, runs the lint against the saved file only, and prints violations into the session context. It does not block the save (advisory).

---

## Optional: Pre-commit Enforcement

For enforcement at commit-time rather than save-time:

```bash
# .git/hooks/pre-commit (or use husky/lefthook)
#!/usr/bin/env bash
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$' || true)
if [ -n "$STAGED" ]; then
  ./scripts/lint-frontmatter.sh $STAGED || {
    echo ""
    echo "Commit blocked: frontmatter violations detected. Fix them and re-stage."
    exit 1
  }
fi
```

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
