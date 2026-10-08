#!/usr/bin/env bash
#
# sync-prd-standard.sh — propagate the portable PRD standard pack from this
# (canonical) wiki repo into the sibling wiki repos.
#
# Canonical source: RackAI Wiki. The pack is three files:
#   .kiro/steering/prd-standards.md
#   templates/prd.md
#   08-change-control/FITNESS_CHECKLIST.md   (contains the P-01..P-08 PRD checks)
#
# The sibling wikis share the 00-hub..08-change-control + .kiro + templates
# structure, so the pack is drop-in identical. Re-run after any change to the
# standard in the canonical source.
#
# Usage:
#   scripts/sync-prd-standard.sh            # dry run (default) — shows what would copy
#   scripts/sync-prd-standard.sh --apply    # actually copy
#
# Notes:
#  - FITNESS_CHECKLIST.md is MERGED by hand, not overwritten, because sibling
#    repos may have repo-specific checks. The script copies the steering file and
#    template, and for the checklist it only reports whether the P-checks are present.
#  - Edit SIBLINGS below if the set of wiki repos changes.

set -euo pipefail

# Resolve this repo root (the canonical source) = parent of the scripts/ dir.
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECTS="$(cd "$SRC/.." && pwd)"

# Sibling wiki repos (relative to the Projects dir). Keep this list current.
SIBLINGS=(
  "AIOS Wiki"
  "VCFRaxWiki"
)

APPLY=0
[[ "${1:-}" == "--apply" ]] && APPLY=1

echo "Canonical source: $SRC"
echo "Mode: $([[ $APPLY == 1 ]] && echo APPLY || echo 'DRY RUN (pass --apply to copy)')"
echo

copy_file() {
  local rel="$1" dest_root="$2"
  local src_path="$SRC/$rel" dest_path="$dest_root/$rel"
  if [[ ! -f "$src_path" ]]; then
    echo "  ! source missing: $rel (skipping)"; return
  fi
  mkdir -p "$(dirname "$dest_path")"
  if [[ $APPLY == 1 ]]; then
    cp "$src_path" "$dest_path"
    echo "  copied: $rel"
  else
    echo "  would copy: $rel -> $dest_path"
  fi
}

for repo in "${SIBLINGS[@]}"; do
  dest="$PROJECTS/$repo"
  echo "=== $repo ==="
  if [[ ! -d "$dest" ]]; then
    echo "  ! not found at $dest (skipping)"; echo; continue
  fi
  # Overwrite-safe files (identical everywhere):
  copy_file ".kiro/steering/prd-standards.md" "$dest"
  copy_file "templates/prd.md" "$dest"
  # Checklist: do NOT overwrite — report whether P-checks already present.
  if grep -q "P-01" "$dest/08-change-control/FITNESS_CHECKLIST.md" 2>/dev/null; then
    echo "  ok: FITNESS_CHECKLIST.md already has PRD P-checks"
  else
    echo "  ACTION: merge the 'Section 2b — PRD Checks' block into $repo/08-change-control/FITNESS_CHECKLIST.md by hand (not auto-overwritten to preserve repo-specific checks)"
  fi
  echo
done

echo "Done. Review changes in each sibling repo and commit there separately."
