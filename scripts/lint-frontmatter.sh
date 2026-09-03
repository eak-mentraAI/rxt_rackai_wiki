#!/usr/bin/env bash
# lint-frontmatter.sh — Validate YAML frontmatter in Rack AI OpenRouter wiki markdown files
#
# Checks:
#   1. File starts with ---
#   2. Required fields present: id, type, status, owner, domain, confidence,
#      last_reviewed, aliases, related, source_docs, parent, summary
#   3. Enum fields have valid values:
#      - type: entity|workflow|event|metric|formula|coefficient|policy|
#              assumption|validation|evidence|source|hub|index|change|glossary
#      - status: draft|reviewed|validated|deprecated
#      - confidence: assumed|derived|measured|validated
#      - domain: strategy|product|platform|performance|model-enablement|
#                infrastructure|reliability|commercial|capacity|governance
#
# Usage:
#   ./scripts/lint-frontmatter.sh              # Lint all .md files
#   ./scripts/lint-frontmatter.sh path/to.md   # Lint a single file
#
# Exit codes:
#   0 = all files pass
#   1 = one or more files have violations

set -euo pipefail

VALID_TYPES="entity|workflow|event|metric|formula|coefficient|policy|assumption|validation|evidence|source|hub|index|change|glossary"
VALID_STATUS="draft|reviewed|validated|deprecated"
VALID_CONFIDENCE="assumed|derived|measured|validated"
VALID_DOMAIN="strategy|product|platform|performance|model-enablement|infrastructure|reliability|commercial|capacity|governance"
REQUIRED_FIELDS="id type status owner domain confidence last_reviewed aliases related source_docs parent summary"

ERRORS=0
FILES_CHECKED=0
FILES_FAILED=0

lint_file() {
  local file="$1"
  local file_errors=0

  # Check file starts with ---
  if ! head -1 "$file" | grep -q "^---$"; then
    echo "ERROR: $file — missing opening frontmatter delimiter (---)"
    file_errors=$((file_errors + 1))
    ERRORS=$((ERRORS + file_errors))
    FILES_FAILED=$((FILES_FAILED + 1))
    return
  fi

  # Extract frontmatter (between first and second ---)
  local fm
  fm=$(awk '/^---$/{n++; next} n==1{print} n>=2{exit}' "$file")

  # Check required fields
  for field in $REQUIRED_FIELDS; do
    if ! echo "$fm" | grep -q "^${field}:"; then
      echo "ERROR: $file — missing required field: $field"
      file_errors=$((file_errors + 1))
    fi
  done

  # Validate type enum
  local type_val
  type_val=$(echo "$fm" | grep "^type:" | head -1 | sed 's/^type: //')
  if [ -n "$type_val" ]; then
    if ! echo "$type_val" | grep -qE "^($VALID_TYPES)$"; then
      echo "ERROR: $file — invalid type: \"$type_val\""
      echo "       Valid: $VALID_TYPES"
      file_errors=$((file_errors + 1))
    fi
  fi

  # Validate status enum
  local status_val
  status_val=$(echo "$fm" | grep "^status:" | head -1 | sed 's/^status: //')
  if [ -n "$status_val" ]; then
    if ! echo "$status_val" | grep -qE "^($VALID_STATUS)$"; then
      echo "ERROR: $file — invalid status: \"$status_val\""
      echo "       Valid: $VALID_STATUS"
      file_errors=$((file_errors + 1))
    fi
  fi

  # Validate confidence enum
  local conf_val
  conf_val=$(echo "$fm" | grep "^confidence:" | head -1 | sed 's/^confidence: //')
  if [ -n "$conf_val" ]; then
    if ! echo "$conf_val" | grep -qE "^($VALID_CONFIDENCE)$"; then
      echo "ERROR: $file — invalid confidence: \"$conf_val\""
      echo "       Valid: $VALID_CONFIDENCE"
      file_errors=$((file_errors + 1))
    fi
  fi

  # Validate domain enum
  local domain_val
  domain_val=$(echo "$fm" | grep "^domain:" | head -1 | sed 's/^domain: //')
  if [ -n "$domain_val" ]; then
    if ! echo "$domain_val" | grep -qE "^($VALID_DOMAIN)$"; then
      echo "ERROR: $file — invalid domain: \"$domain_val\""
      echo "       Valid: $VALID_DOMAIN"
      file_errors=$((file_errors + 1))
    fi
  fi

  if [ $file_errors -gt 0 ]; then
    FILES_FAILED=$((FILES_FAILED + 1))
    ERRORS=$((ERRORS + file_errors))
  fi
}

# Determine files to check
if [ $# -gt 0 ]; then
  # Lint specific files passed as arguments
  for f in "$@"; do
    if [ -f "$f" ] && [[ "$f" == *.md ]]; then
      FILES_CHECKED=$((FILES_CHECKED + 1))
      lint_file "$f"
    fi
  done
else
  # Lint all .md files in the repo (excluding .git, .obsidian, .kiro, templates)
  REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
  while IFS= read -r -d '' f; do
    FILES_CHECKED=$((FILES_CHECKED + 1))
    lint_file "$f"
  done < <(find "$REPO_ROOT" -name "*.md" \
    -not -path "*/.git/*" \
    -not -path "*/.obsidian/*" \
    -not -path "*/.kiro/*" \
    -not -path "*/templates/*" \
    -print0)
fi

# Summary
echo ""
if [ $ERRORS -eq 0 ]; then
  echo "✓ All $FILES_CHECKED files pass frontmatter validation."
  exit 0
else
  echo "✗ $FILES_FAILED of $FILES_CHECKED files have frontmatter errors ($ERRORS total violations)."
  exit 1
fi
