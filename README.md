# planner-docs

User documentation for Stutastic Planner, built with
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Live at: https://docs.planner.danplace.tech/

## Content source

This site documents released Stutastic Planner behavior. Product and architecture
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

The `VERSION` file selects the app release documented by this site. Set it to the
release version before merging documentation changes to `main`. The deployment
workflow strictly builds the site, publishes it under that version, and moves
the `latest` alias and root redirect to it. Previously published versions stay
available.

GitHub Pages serves the site from the `gh-pages` branch. Its **Pages source must
be set to that branch** (Settings → Pages) the first time publishing is set up.
