#!/usr/bin/env bash
# Push the current branch, refusing if its pull request has already been merged.
#
# Three times on 2026-09-03, commits were pushed to a branch whose PR was
# already merged. They sit on a merged head with no PR watching them and reach
# main only if someone notices. Writing the rule down did not stop it, so this
# checks instead.
#
# The naive test, "is the branch tip an ancestor of main", does not work: after
# the merge the branch grows past the merged commit, so its tip is no longer
# contained in main and the branch looks live. The question is whether a PR for
# this branch has been merged and the branch has moved on since. Ask GitHub.
#
# Usage: GH_TOKEN=... tools/push.sh [remote]
set -euo pipefail

REPO=morischumacher/Diploma_Thesis
BRANCH=$(git rev-parse --abbrev-ref HEAD)
REMOTE=${1:-origin}

if [ "$BRANCH" = "main" ]; then
  echo "REFUSED: never push to main directly (ANWEISUNGEN 1.3)." >&2
  exit 1
fi

git fetch origin --quiet

if [ -n "${GH_TOKEN:-}" ]; then
  MERGED_SHA=$(curl -s --noproxy '*' \
    -H "Authorization: Bearer $GH_TOKEN" \
    -H "Accept: application/vnd.github+json" \
    "https://api.github.com/repos/$REPO/pulls?head=${REPO%%/*}:$BRANCH&state=closed&per_page=100" \
    | python3 -c '
import sys, json
try:
    prs = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if not isinstance(prs, list):
    sys.exit(0)
merged = [p for p in prs if p.get("merged_at")]
if merged:
    print(merged[0]["head"]["sha"], merged[0]["number"])
')
  if [ -n "$MERGED_SHA" ]; then
    SHA=$(echo "$MERGED_SHA" | cut -d' ' -f1)
    NUM=$(echo "$MERGED_SHA" | cut -d' ' -f2)
    if [ "$(git rev-parse HEAD)" != "$SHA" ]; then
      AHEAD=$(git rev-list --count "$SHA..HEAD" 2>/dev/null || echo '?')
      echo "REFUSED: PR #$NUM for '$BRANCH' is already merged (at ${SHA:0:7})." >&2
      echo "  $AHEAD commit(s) here are past the merge point and would be stranded." >&2
      echo "  A merged branch is closed. Start again from main:" >&2
      echo "    git checkout -b <new-branch> origin/main" >&2
      echo "    git cherry-pick $SHA..HEAD" >&2
      exit 1
    fi
  fi
else
  echo "warning: GH_TOKEN unset, skipping the merged-PR check." >&2
fi

git -c http.proxy= -c https.proxy= push "$REMOTE" "$BRANCH"
