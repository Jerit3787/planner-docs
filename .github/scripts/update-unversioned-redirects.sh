#!/usr/bin/env bash
set -euo pipefail

workspace="${GITHUB_WORKSPACE:?GITHUB_WORKSPACE must be set}"
runner_temp="${RUNNER_TEMP:?RUNNER_TEMP must be set}"
redirect_dir="$(mktemp -d "${runner_temp}/planner-docs-redirects.XXXXXX")"
rmdir "$redirect_dir"

git -C "$workspace" fetch origin gh-pages:refs/remotes/origin/gh-pages
git -C "$workspace" worktree add --detach "$redirect_dir" refs/remotes/origin/gh-pages
cleanup() {
  git -C "$workspace" worktree remove --force "$redirect_dir"
}
trap cleanup EXIT

write_redirect() {
  local path="$1"
  local destination="$2"
  local title="$3"
  local target="/latest/${destination}/"

  mkdir -p "${redirect_dir}/${path}"
  cat > "${redirect_dir}/${path}/index.html" <<EOF
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="0; url=${target}">
    <link rel="canonical" href="https://docs.planner.danplace.tech${target}">
    <title>${title} - Stutastic Planner Docs</title>
    <script>window.location.replace("${target}");</script>
  </head>
  <body>
    <p>This page has moved to <a href="${target}">${title}</a>.</p>
  </body>
</html>
EOF
}

write_redirect "support" "support" "Support"
write_redirect "data/privacy-policy" "data/privacy-policy" "Privacy policy"

git -C "$redirect_dir" add -- support/index.html data/privacy-policy/index.html
if git -C "$redirect_dir" diff --cached --quiet; then
  echo "Unversioned Help and Privacy redirects already point to latest"
  exit 0
fi

git -C "$redirect_dir" commit -m "chore(docs): redirect Help and Privacy URLs to latest"
git -C "$redirect_dir" push origin HEAD:gh-pages
