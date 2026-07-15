# planner-docs

User documentation for Student Planner, built with
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Live at: https://docs.planner.danplace.tech/

## Local development

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

## Deployment

`.github/workflows/deploy.yml` runs `mkdocs gh-deploy` on every push to `main`, publishing to the
`gh-pages` branch. The repo's **Pages source must be set to the `gh-pages` branch** (Settings → Pages)
the first time this is set up.
