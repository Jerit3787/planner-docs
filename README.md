# planner-docs

User documentation for the local-first Student Planner application, built with
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Live at: https://docs.planner.danplace.tech/

## Content source

This site documents released Student Planner behavior. Product and architecture
plans live in the main Planner repository and are not automatically public
documentation. A feature page changes when the corresponding behavior is
released and verified.

## Local development

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
.venv/bin/mkdocs build --strict
```

## Deployment

`.github/workflows/deploy.yml` runs `mkdocs gh-deploy` on every push to `main`, publishing to the
`gh-pages` branch. The repo's **Pages source must be set to the `gh-pages` branch** (Settings → Pages)
the first time this is set up.
