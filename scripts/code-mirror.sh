#!/usr/bin/env bash
#
# code-mirror.sh — keep READ-ONLY local mirrors of the RackAI code repos for
# tech-spec Codebase Grounding (tech-spec-standards.md; Fitness T-09).
#
# Auth: uses a second gh account (default EAKERR4, the work account with access
# to RSS-Engineering) ONLY for these repos. Your active gh account (used to push
# this wiki) is never switched. The token is fetched from gh's keychain on each
# git call via a credential helper; it is never written to disk or git config.
#
# Read-only by construction: each mirror's push URL is set to "no-push", and the
# local agent hook .claude/hooks/code-repo-guard.sh denies writes/PRs.
#
# Usage:
#   scripts/code-mirror.sh sync              # clone missing repos, fetch + fast-forward existing ones
#   scripts/code-mirror.sh status            # repo, branch, HEAD sha, push URL
#   scripts/code-mirror.sh gh api <path>     # read-only gh call as the code account (GET only)
#
# One-time setup (interactive, in a terminal):
#   gh auth login --hostname github.com --git-protocol https --web   # sign in as the work account
#   gh auth switch --user eak-mentraAI                               # restore the wiki account as active
#
# Env: RACKAI_CODE_GH_USER (default EAKERR4), RACKAI_CODE_DIR (default ~/Projects/rackai-code)

set -euo pipefail

# gh stores the login with GitHub's casing (EAKERR4) and `--user` is case-sensitive.
GH_USER="${RACKAI_CODE_GH_USER:-EAKERR4}"
DIR="${RACKAI_CODE_DIR:-$HOME/Projects/rackai-code}"
ORG="RSS-Engineering"
REPOS=(rackai rackai-ui rackai-docs)
# Resolved at call time, so the token never lands in .git/config.
HELPER="!f() { test \"\$1\" = get || exit 0; echo username=x-access-token; echo \"password=\$(gh auth token --hostname github.com --user $GH_USER)\"; }; f"

need_account() {
  if ! gh auth token --hostname github.com --user "$GH_USER" >/dev/null 2>&1; then
    echo "gh has no login for '$GH_USER'. Run once in a terminal:" >&2
    echo "  gh auth login --hostname github.com --git-protocol https --web" >&2
    echo "  gh auth switch --user eak-mentraAI" >&2
    exit 1
  fi
}

git_ro() { git -c credential.helper= -c "credential.helper=$HELPER" "$@"; }

sync() {
  need_account
  mkdir -p "$DIR"
  for r in "${REPOS[@]}"; do
    local path="$DIR/$r"
    if [ ! -d "$path/.git" ]; then
      echo "== cloning $ORG/$r"
      git_ro clone --quiet "https://github.com/$ORG/$r.git" "$path"
    else
      echo "== fetching $ORG/$r"
      git_ro -C "$path" fetch --quiet --prune origin
      git -C "$path" merge --ff-only --quiet "@{u}" 2>/dev/null || echo "   (not fast-forwarded: local changes or detached HEAD)"
    fi
    # Per-mirror config: account-scoped helper for future fetches; pushing disabled.
    git -C "$path" config --replace-all credential.helper ""
    git -C "$path" config --add credential.helper "$HELPER"
    git -C "$path" remote set-url --push origin no-push
  done
  status
}

status() {
  for r in "${REPOS[@]}"; do
    local path="$DIR/$r"
    if [ -d "$path/.git" ]; then
      printf '%-12s %-20s %s  push=%s\n' "$r" "$(git -C "$path" rev-parse --abbrev-ref HEAD)" \
        "$(git -C "$path" rev-parse --short=12 HEAD)" "$(git -C "$path" remote get-url --push origin)"
    else
      printf '%-12s (not cloned)\n' "$r"
    fi
  done
}

case "${1:-}" in
  sync) sync ;;
  status) status ;;
  gh)
    shift
    need_account
    # GET-only: refuse anything that could write.
    if printf '%s ' "$@" | grep -qiE '(-X|--method)[[:space:]=]*(POST|PUT|PATCH|DELETE)|(^|[[:space:]])(-f|-F|--field|--raw-field|--input)([[:space:]]|=)'; then
      echo "code-mirror.sh gh: read-only; write methods and request bodies are refused." >&2; exit 1
    fi
    GH_TOKEN="$(gh auth token --hostname github.com --user "$GH_USER")" gh "$@" ;;
  *) sed -n '2,25p' "$0"; exit 1 ;;
esac
