#!/usr/bin/env python3
"""lint-prd-spec.py — structural checks for PRD and tech-spec notes and their
roadmap links (Fitness P-09, T-09, T-10).

Checks
  For every note with `type: prd` or `type: spec` (same exclusions as
  lint-frontmatter.sh):
    L1  The document control table has a "Roadmap items" row naming at least one
        milestone; names are `;`-separated and each matches a Milestone in the
        canonical roadmap table exactly.
    L2  Each of those roadmap rows links back to the note: the PRD column (prd) or
        Tech spec column (spec) contains CONSOLE/<note-id>.             (P-09/T-10)
  For every `type: spec` note:
    L3  A "Codebase Grounding" section cites at least one code repo at a commit
        SHA (owner/repo@sha) from CODE_REPOS, and has all six subsections.  (T-09)
  For the roadmap table:
    L4  Every link in the PRD / Tech spec columns has the console form and
        resolves to an existing note of an allowed type (prd/spec, or source for
        ingested engineering documents).
    L5  Two-way: a row linking a wiki prd/spec must be named in that note's
        Roadmap items row.

Usage
  python3 scripts/lint-prd-spec.py           # whole repo (fast; run in pre-commit)
Exit 0 = pass, 1 = violations.
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROADMAP = "05-wiki/RackAI Roadmap.csv"
CONSOLE = "https://knowledge.rackspace-cloud.com/browse/rackai/"
CODE_REPOS = ("RSS-Engineering/rackai", "RSS-Engineering/rackai-ui", "RSS-Engineering/rackai-docs")
LINK_COLS = {"prd": "PRD", "spec": "Tech spec"}
ALLOWED_TARGETS = {"PRD": {"prd", "source"}, "Tech spec": {"spec", "source"}}
GROUNDING_SUBSECTIONS = (
    "Repos & revisions read",
    "Existing patterns",
    "Extension points",
    "Standards to enforce",
    "Dependencies & fork prevention",
    "Improvement & modularity opportunities",
)
SKIP_DIRS = {".git", ".obsidian", ".kiro", ".claude", "templates", "reference", "_ontology-discovery", "node_modules"}

errors = []


def err(where, msg):
    errors.append(f"ERROR: {where} — {msg}")


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def notes():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md") and fn not in ("CLAUDE.md", "AGENTS.md"):
                path = os.path.join(dirpath, fn)
                with open(path, encoding="utf-8") as f:
                    text = f.read()
                yield os.path.relpath(path, ROOT), text, frontmatter(text)


def split_cell(cell):
    return [p.strip() for p in (cell or "").split(";") if p.strip()]


def roadmap_items(text):
    m = re.search(r"^\|\s*Roadmap items\s*\|(.*)\|\s*$", text, re.M)
    if not m:
        return None
    return [re.sub(r"[`*]", "", x).strip() for x in m.group(1).split(";") if x.strip()]


def main():
    all_notes = list(notes())
    types = {fm.get("id"): fm.get("type") for _, _, fm in all_notes if fm.get("id")}

    with open(os.path.join(ROOT, ROADMAP), newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        header = reader.fieldnames or []
    for col in LINK_COLS.values():
        if col not in header:
            err(ROADMAP, f"missing column '{col}'")
    if errors:
        return finish()
    by_milestone = {}
    for i, r in enumerate(rows, 2):
        by_milestone.setdefault(r["Milestone"].strip(), []).append((i, r))

    declared = {}  # note id -> set of milestones it names
    for rel, text, fm in all_notes:
        t = fm.get("type")
        if t not in LINK_COLS:
            continue
        nid = fm.get("id", "?")
        col = LINK_COLS[t]
        items = roadmap_items(text)
        if not items:
            err(rel, "document control table has no 'Roadmap items' row (P-09/T-10)")
            continue
        declared[nid] = set(items)
        for item in items:
            if item not in by_milestone:
                err(rel, f"roadmap item '{item}' is not a Milestone in {ROADMAP}")
                continue
            for line, r in by_milestone[item]:
                if CONSOLE + nid not in split_cell(r.get(col)):
                    err(rel, f"{ROADMAP} line {line} ('{item}') {col} column does not link {CONSOLE}{nid}")
        if t == "spec":
            check_grounding(rel, text)

    for line, r in ((i, r) for i, r in enumerate(rows, 2)):
        for col, allowed in ALLOWED_TARGETS.items():
            for link in split_cell(r.get(col)):
                if not link.startswith(CONSOLE):
                    err(ROADMAP, f"line {line} {col}: '{link}' is not a {CONSOLE}<id> link")
                    continue
                tid = link[len(CONSOLE):]
                tt = types.get(tid)
                if tt is None:
                    err(ROADMAP, f"line {line} {col}: note '{tid}' does not exist")
                elif tt not in allowed:
                    err(ROADMAP, f"line {line} {col}: '{tid}' is type {tt}, expected one of {sorted(allowed)}")
                elif tt in LINK_COLS and r["Milestone"].strip() not in declared.get(tid, set()):
                    err(ROADMAP, f"line {line} {col}: links '{tid}' but that note's Roadmap items row does not name '{r['Milestone'].strip()}'")
    return finish()


def check_grounding(rel, text):
    m = re.search(r"^##\s+[\d.]*\s*Codebase Grounding.*?$(.*?)(?=^##\s)", text, re.M | re.S)
    if not m:
        err(rel, "no 'Codebase Grounding' section (T-09)")
        return
    body = m.group(1)
    pat = r"(" + "|".join(re.escape(r) for r in CODE_REPOS) + r")@[0-9a-f]{7,40}\b"
    if not re.search(pat, body):
        err(rel, "Codebase Grounding cites no code repo at a commit SHA (owner/repo@sha) (T-09)")
    for sub in GROUNDING_SUBSECTIONS:
        if not re.search(r"^###\s+[\d.]*\s*" + re.escape(sub), body, re.M | re.I):
            err(rel, f"Codebase Grounding is missing subsection '{sub}' (T-09)")


def finish():
    for e in errors:
        print(e)
    print()
    if errors:
        print(f"✗ PRD/spec lint: {len(errors)} violation(s).")
        return 1
    print("✓ PRD/spec lint passes (roadmap links, grounding).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
