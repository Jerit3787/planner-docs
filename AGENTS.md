# Public Documentation Instructions

This is the independently deployed public help site for Student Planner.

## Content boundary

- Document released user behavior, not unfinished plans or internal architecture.
- When checked out inside the shared Planner workspace, consult
  `../docs/product/` and the parity/platform catalogues before describing changed
  behavior.
- Distinguish PWA, iPhone/iPad, Android and desktop behavior where the user must
  take different steps.
- Do not claim a platform or feature is supported until its release evidence is
  recorded.

## Safety and privacy

- Never include credentials, internal service URLs, account identifiers,
  private test data, raw logs or screenshots containing personal information.
- Use synthetic example data in prose and screenshots.
- Keep setup instructions task-focused and describe recovery for destructive or
  irreversible actions.

## Style

- Use plain language, short procedures and the terms shown in the current app.
- Update navigation in `mkdocs.yml` when adding or moving a page.
- Update screenshots only from an approved release candidate and cover both
  narrow and wide layouts when they materially differ.

## Verification

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs build --strict
```

Do not run `mkdocs gh-deploy` without an explicit publishing request.
