#!/usr/bin/env python3
"""kg — fast knowledge-graph lookups over a wiki working tree (stdlib only, no install).

Shared across the sister wikis (RackAI Wiki, AIOS Wiki, VCFRaxWiki): keep scripts/kg.py identical in all
three; canonical copy lives in RackAI Wiki. Use it before bulk-reading files — find -> show (headings) ->
read only the needed section -> expand with out/in.

Resolves the two link systems in these wikis in one place:
  * frontmatter IDs   (id / parent / related)   — IDs are NOT filenames
  * body wikilinks    ([[Note Title]] / [[Title|alias]] / [[Title#section]]) — resolved by
                      filename, vault path, id, H1 title, or alias
plus typed edges from "## Relationships" tables (| EDGE | [[Target]] | → | notes |).

Usage (run from anywhere inside the repo): python3 scripts/kg.py <cmd>
  kg.py find <text>        id / title / alias / summary match  → id, type, path, summary
  kg.py show <ref>         frontmatter + summary + section headings for one note (no body)
  kg.py out <ref>          outbound: parent, related IDs, typed Relationship edges, other wikilinks
  kg.py in <ref>           inbound: children (parent=), related-by, wikilink backlinks
  kg.py children <ref>     notes whose parent is <ref>
  kg.py type <type> [domain]   list notes of a type (optionally one domain)
  kg.py hubs               all hub/index notes — the navigation entry points
  kg.py broken             wikilinks and related/parent IDs that resolve to nothing
  kg.py stats              counts by type / domain / confidence

<ref> may be an id (ent-model-deployment), a title ("Model Deployment"), or an alias.
Add --json for machine-readable output.
"""
import json
import os
import re
import subprocess
import sys

SKIP_DIRS = {".git", ".obsidian", ".kiro", ".claude", "templates", "node_modules", "_ontology-discovery"}
WIKILINK = re.compile(r"\[\[([^\]|#\\]+)(?:\\?#[^\]|]*)?(?:\\?\|[^\]]*)?\]\]")  # tolerates table-escaped \|



def _parent(raw):
    """A root note declares `parent: null` (or ~ / empty): no parent."""
    v = raw.strip().strip("'\"")
    return "" if v.lower() in ("null", "~", "none") else v

def repo_root():
    try:
        return subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True,
                                       stderr=subprocess.DEVNULL).strip()
    except Exception:
        return os.getcwd()


def parse_list(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
    return [v.strip("'\"")] if v else []


def parse_note(path, rel):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    fm, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block, body = text[3:end], text[end + 4:]
            key = None
            for line in block.splitlines():
                m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
                if m:
                    key, val = m.group(1), m.group(2)
                    fm[key] = val
                elif key and line.strip().startswith("- "):  # YAML block list
                    fm[key] = (fm.get(key) or "") + ("," if fm.get(key) else "") + line.strip()[2:]
    for k in ("aliases", "related", "source_docs"):
        if k in fm:
            raw = fm[k]
            fm[k] = parse_list(raw if raw.startswith("[") else "[" + raw + "]")
    title = os.path.splitext(os.path.basename(rel))[0]
    rel_section = ""
    m = re.search(r"^##\s+Relationships\s*$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    if m:
        rel_section = m.group(1)
    edges = []
    for line in rel_section.splitlines():  # row-by-row: 3-col (Edge|Target|Notes) or 4-col (Edge|Target|Dir|Notes)
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        edge = cells[0].strip("`* ")
        if not re.fullmatch(r"[A-Z][A-Z_]+", edge) or edge in ("RELATIONSHIP", "EDGE", "TYPE"):
            continue
        direction = cells[2] if len(cells) > 2 and re.fullmatch(r"[←→↔<>-]+", cells[2]) else "→"
        targets = WIKILINK.findall(cells[1]) or [t.strip("`* ") for t in re.split(r"[,;]", cells[1]) if t.strip("`* ")]
        for t in targets:
            edges.append((edge, t.strip(), direction))
    return {
        "path": rel,
        "title": title,
        "id": fm.get("id", "").strip().strip("'\""),
        "type": fm.get("type", "").strip(),
        "domain": fm.get("domain", "").strip(),
        "owner": fm.get("owner", "").strip(),
        "status": fm.get("status", "").strip(),
        "confidence": fm.get("confidence", "").strip(),
        "parent": _parent(fm.get("parent", "")),
        "related": fm.get("related", []),
        "aliases": fm.get("aliases", []),
        "summary": fm.get("summary", "").strip().strip("'\""),
        "has_fm": bool(fm),
        # ignore [[...]] inside code spans/fences (examples, not links)
        "links": sorted({l.strip() for l in WIKILINK.findall(re.sub(r"```.*?```|`[^`\n]*`", "", body, flags=re.S))}),
        "edges": edges,
        "headings": re.findall(r"^#{2,3}\s+(.+)$", body, re.M),
        "h1": (re.search(r"^#\s+(.+?)\s*$", body, re.M) or [None, ""])[1],
    }


def load(root):
    notes = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                p = os.path.join(d, f)
                n = parse_note(p, os.path.relpath(p, root))
                if n:
                    notes.append(n)
    by_id = {n["id"]: n for n in notes if n["id"]}
    by_title = {}
    for n in notes:
        by_title.setdefault(n["title"].lower(), n)
    for n in notes:  # vault-path links: [[platforms/x/hub-networking|Label]] (unique when filenames repeat)
        by_title.setdefault(os.path.splitext(n["path"])[0].replace(os.sep, "/").lower(), n)
    for n in notes:  # wikilinks may target the H1 title (e.g. VCF: [[Hub: Networking (RC)]] -> hub-networking.md)
        if n["h1"]:
            by_title.setdefault(n["h1"].lower(), n)
    by_alias = {}
    for n in notes:
        for a in n["aliases"]:
            by_alias.setdefault(a.lower(), n)
    return notes, by_id, by_title, by_alias


def resolve(ref, by_id, by_title, by_alias):
    r = ref.strip()
    return by_id.get(r) or by_title.get(r.lower()) or by_alias.get(r.lower())


def row(n):
    return f"{n['id'] or '-':40} {n['type'] or '-':11} {n['path']}" + (f"\n    {n['summary']}" if n["summary"] else "")


def main(argv):
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv:
        print(__doc__)
        return 1
    cmd, args = argv[0], argv[1:]
    root = repo_root()
    notes, by_id, by_title, by_alias = load(root)
    out = []

    def need():
        if not args:
            sys.exit(f"usage: kg.py {cmd} <ref>")
        n = resolve(" ".join(args), by_id, by_title, by_alias)
        if not n:
            sys.exit(f"no note matches '{' '.join(args)}' (try: kg.py find {' '.join(args)})")
        return n

    if cmd == "find":
        q = " ".join(args).lower()
        hits = [n for n in notes if q in n["id"].lower() or q in n["title"].lower()
                or any(q in a.lower() for a in n["aliases"])]
        hits += [n for n in notes if n not in hits and q in n["summary"].lower()]
        out = hits
        if not as_json:
            print("\n".join(row(n) for n in hits) or "no matches")
    elif cmd == "show":
        n = need()
        out = n
        if not as_json:
            print(row(n))
            print(f"    status={n['status']} confidence={n['confidence']} domain={n['domain']} owner={n['owner']} parent={n['parent']}")
            print(f"    aliases={n['aliases']}\n    related={n['related']}")
            print("    sections: " + " | ".join(n["headings"]))
    elif cmd == "out":
        n = need()
        par = by_id.get(n["parent"])
        rel = [(r, by_id.get(r)) for r in n["related"]]
        edge_titles = {t.lower() for _, t, _ in n["edges"]}
        other = [l for l in n["links"] if l.lower() not in edge_titles]
        out = {"parent": n["parent"], "related": n["related"], "edges": n["edges"], "links": other}
        if not as_json:
            print(f"{n['title']} ({n['id']})")
            print(f"  parent  {n['parent']} -> {par['path'] if par else 'UNRESOLVED'}")
            for r, t in rel:
                print(f"  related {r} -> {t['path'] if t else 'UNRESOLVED'}")
            for e, t, d in n["edges"]:
                tn = resolve(t, by_id, by_title, by_alias)
                print(f"  {d} {e:16} {t}" + ("" if tn else "  [UNRESOLVED]"))
            if other:
                print("  links   " + ", ".join(other))
    elif cmd in ("in", "children"):
        n = need()
        kids = [m for m in notes if n["id"] and m["parent"] == n["id"] and m is not n]
        if cmd == "children":
            out = kids
            if not as_json:
                print("\n".join(row(m) for m in kids) or "no children")
        else:
            relby = [m for m in notes if n["id"] and n["id"] in m["related"] and m is not n]
            keys = ({n["title"].lower(), n["h1"].lower(), n["id"].lower(),
                     os.path.splitext(n["path"])[0].replace(os.sep, "/").lower()} - {""}) | {a.lower() for a in n["aliases"]}
            back = [m for m in notes if m is not n and any(l.lower() in keys for l in m["links"])]
            typed = [(m, e, d) for m in notes for e, t, d in m["edges"] if t.lower() in keys and m is not n]
            out = {"children": [m["path"] for m in kids], "related_by": [m["path"] for m in relby],
                   "typed_edges": [(m["path"], e, d) for m, e, d in typed],
                   "backlinks": [m["path"] for m in back]}
            if not as_json:
                print(f"{n['title']} ({n['id']})")
                for m in kids:
                    print(f"  child       {m['path']}")
                for m, e, d in typed:
                    print(f"  {e:11} {m['path']}  ({d})")
                for m in relby:
                    print(f"  related-by  {m['path']}")
                rest = [m for m in back if m not in kids and m not in relby and m not in [x for x, _, _ in typed]]
                for m in rest:
                    print(f"  backlink    {m['path']}")
    elif cmd == "type":
        t = args[0] if args else ""
        dom = args[1] if len(args) > 1 else None
        out = [n for n in notes if n["type"] == t and (not dom or n["domain"] == dom)]
        if not as_json:
            print("\n".join(row(n) for n in out) or "none")
    elif cmd == "hubs":
        out = [n for n in notes if n["type"] in ("hub", "index")]
        if not as_json:
            print("\n".join(row(n) for n in sorted(out, key=lambda n: n["path"])))
    elif cmd == "broken":
        bad = []
        for n in notes:
            for l in n["links"]:
                if os.path.splitext(l)[1] and not l.endswith(".md") and os.path.exists(
                        os.path.join(root, os.path.dirname(n["path"]), l)):
                    continue  # attachment link to an existing non-markdown file
                if not resolve(l, by_id, by_title, by_alias):
                    bad.append((n["path"], "wikilink", l))
            for r in ([n["parent"]] if n["parent"] else []) + n["related"]:
                if r not in by_id and not r.startswith("universal:"):
                    bad.append((n["path"], "id", r))
        out = bad
        if not as_json:
            for p, k, t in bad:
                print(f"{k:8} {t:45} in {p}")
            print(f"{len(bad)} unresolved references")
    elif cmd == "stats":
        from collections import Counter
        out = {k: Counter(n[k] or "(none)" for n in notes) for k in ("type", "domain", "confidence")}
        if not as_json:
            print(f"{len(notes)} notes ({sum(1 for n in notes if n['has_fm'])} with frontmatter)")
            for k, c in out.items():
                print(f"{k}: " + ", ".join(f"{a}={b}" for a, b in c.most_common()))
    else:
        print(__doc__)
        return 1
    if as_json:
        print(json.dumps(out, default=str, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
