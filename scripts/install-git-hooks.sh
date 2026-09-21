#!/usr/bin/env bash
#
# Installs the repo's git hooks into .git/hooks/.
#
# .git/hooks/ is not version-controlled, so this installer makes the tracked
# pre-commit hook active in a clone. Run once after cloning:
#
#     ./scripts/install-git-hooks.sh
#
# The installed pre-commit hook runs scripts/lint-frontmatter.sh against the
# staged .md files and blocks the commit if any fail frontmatter validation
# (missing fields, invalid enums, or over-length summary). This mirrors the
# knowledge-platform ingestion rules so bad frontmatter never reaches main.
#
# Matches the "Optional: Pre-commit Enforcement" pattern documented in
# scripts/README.md.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"
PRE_COMMIT="$HOOKS_DIR/pre-commit"

mkdir -p "$HOOKS_DIR"

cat > "$PRE_COMMIT" <<'HOOK'
#!/usr/bin/env bash
# Pre-commit: frontmatter compliance on staged markdown.
# Installed by scripts/install-git-hooks.sh. Do not edit here; edit the
# installer and re-run it so the hook stays reproducible across clones.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"

# Only the markdown files staged for this commit (Added/Copied/Modified).
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$' || true)

if [ -z "$STAGED" ]; then
  exit 0
fi

# Pass the staged files to the shared lint script. It exits non-zero on any
# violation, which aborts the commit.
if ! (cd "$REPO_ROOT" && IFS=$'\n' ./scripts/lint-frontmatter.sh $STAGED); then
  echo ""
  echo "Commit blocked: frontmatter violations detected in staged markdown."
  echo "Fix the issues above and re-stage. To bypass in an emergency: git commit --no-verify"
  exit 1
fi
HOOK

chmod +x "$PRE_COMMIT"
echo "Installed pre-commit hook at $PRE_COMMIT"
echo "It lints staged .md files with scripts/lint-frontmatter.sh and blocks non-compliant commits."
