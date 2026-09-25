#!/usr/bin/env bash
set -euo pipefail

legacy_version="2.126.49"
legacy_commit="b8f9946f64d0847dc1e6817b2509b44bdd9bafd5"
legacy_dir="$(mktemp -d "${RUNNER_TEMP}/planner-docs-legacy.XXXXXX")"
rmdir "$legacy_dir"

if ! git -C "$GITHUB_WORKSPACE" show-ref --quiet --verify refs/remotes/origin/gh-pages; then
  echo "origin/gh-pages must exist before bootstrapping docs versions" >&2
  exit 1
fi

if git -C "$GITHUB_WORKSPACE" cat-file -e "origin/gh-pages:${legacy_version}/index.html" 2>/dev/null; then
  echo "Docs version ${legacy_version} already exists; leaving it unchanged"
  exit 0
fi

git -C "$GITHUB_WORKSPACE" worktree add --detach "$legacy_dir" "$legacy_commit"
cleanup() {
  git -C "$GITHUB_WORKSPACE" worktree remove --force "$legacy_dir"
}
trap cleanup EXIT

cat >> "$legacy_dir/mkdocs.yml" <<'EOF'

extra:
  version:
    provider: mike
    default: latest
EOF
(
  cd "$legacy_dir"
  mike deploy --push "$legacy_version"
)
