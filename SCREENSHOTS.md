# Screenshot manifest

Every doc page has an `<!-- screenshot: filename.png (see SCREENSHOTS.md) -->` HTML comment marking
where a screenshot goes — invisible on the rendered site until it's replaced with a real image tag.

To add one: drop the file at `docs/img/<filename>` (create `docs/img/` if it doesn't exist yet — only
`favicon.png` lives there today) at roughly **1280×800** or your actual device size, then replace the
comment in that page with:

```markdown
![Alt text describing the screenshot](../img/filename.png)
```

(use `img/filename.png`, no `../`, for pages directly under `docs/` like `index.md`).

## Checklist

| File | Page | What to capture |
|---|---|---|
| `dashboard-overview.png` | index.md **and** features/dashboard.md | Full Dashboard: today's classes, GPA/streak/deadline cards, analytics charts. One capture, reused on both pages — no separate "hero" shot needed. |
| `schedule-week-view.png` | features/schedule.md | Full-week timetable view (desktop width). |
| `schedule-day-tabs-mobile.png` | features/schedule.md | Day-tabs view at mobile width. |
| `schedule-import-dialog.png` | features/schedule.md | The `.xlsx`/`.csv` timetable import dialog. |
| `homework-list.png` | features/homework.md | The Tasks list, ideally with a mix of progress levels. |
| `homework-add-task.png` | features/homework.md | Add/edit task form, showing the during-class/custom time picker. |
| `study-topic-list.png` | features/study.md | Study Topics list with progress bars and a linked-test indicator. |
| `quiz-list.png` | features/quiz.md | Quiz & Tests list, mixing regular tests and a Final Exam. |
| `quiz-final-exam-form.png` | features/quiz.md | Add/edit form with **Final Exam** toggled on — seat number + session quick-picks visible. |
| `academics-overview.png` | features/academics.md | Academics page, Semesters tab. |
| `academics-programme-timezone.png` | features/academics.md | Programme add/edit form, timezone override field visible. |
| `academics-periods-editor.png` | features/academics.md | Semester edit → Periods tab, a few periods listed. |
| `calendar-month-view.png` | features/calendar.md | Calendar month grid with period tinting and a holiday/event dot visible. |
| `calendar-day-detail.png` | features/calendar.md | A day's detail view (mobile inline agenda or desktop dialog — either works). |
| `notifications-settings-card.png` | features/notifications.md | Settings' Notifications card (class reminder + deadline toggles). |
| `settings-overview.png` | features/settings.md | Settings page, Preferences section (class duration, exam length, exam sessions list). |
| `settings-data-account.png` | features/settings.md | Settings' Data & account card. |
| `offline-sync-status-panel.png` | offline-and-sync.md | The sync status modal (click the cloud icon in the top bar). |
| `onboarding-welcome.png` | getting-started/onboarding.md | Onboarding wizard's Welcome step. |
| `onboarding-account-step.png` | getting-started/onboarding.md | Onboarding wizard's final account-choice step. |

Not on the list but fine to add later if useful: a Guest-vs-account screenshot (the Profile modal
showing "Create an account"), or the iOS guest-mode warning banner.
