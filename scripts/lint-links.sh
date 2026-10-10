#!/usr/bin/env bash
# lint-links.sh — Check that every in-body link in this corpus resolves to a Knowledge Object
#
# Wraps the Knowledge Platform's link checker (packages/ingestion/src/check-links.ts),
# which uses the same resolution rules as the Knowledge Console:
#   1. object id  2. frontmatter aliases  3. file name / path (no .md)
#   4. H1 title   5. slug / hyphenated variants   (all case-insensitive)
# Unresolved [[wiki links]] and relative .md links render as dead dotted-underlined
# text in the console, so the corpus is kept at zero.
#
# The checker always scans the whole corpus (resolution needs every note), so file
# arguments are accepted but ignored — the hook can pass the saved file harmlessly.
#
# Platform location: defaults to two directories above this repo
# (knowledge-platform/corpora/rackai). Override with KNOWLEDGE_PLATFORM_ROOT.
#
# Usage:
#   ./scripts/lint-links.sh            # check all links
#   MAX_UNRESOLVED=3 ./scripts/lint-links.sh   # tolerate up to N while cleaning up
#
# Exit codes: 0 = all links resolve (or within MAX_UNRESOLVED), 1 = unresolved links,
#             2 = platform checker not found (check skipped)

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLATFORM_ROOT="${KNOWLEDGE_PLATFORM_ROOT:-$(cd "$REPO_ROOT/../.." 2>/dev/null && pwd)}"
INGESTION="$PLATFORM_ROOT/packages/ingestion"
CHECKER="$INGESTION/src/check-links.ts"

if [ ! -f "$CHECKER" ]; then
  echo "SKIP: link checker not found at $CHECKER"
  echo "      Set KNOWLEDGE_PLATFORM_ROOT to your knowledge-platform checkout."
  exit 2
fi

cd "$INGESTION" && npx tsx src/check-links.ts --corpus "$REPO_ROOT" --max "${MAX_UNRESOLVED:-0}"
