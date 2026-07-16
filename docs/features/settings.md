# Settings

<!-- screenshot: settings-overview.png (see SCREENSHOTS.md) -->

All app-wide preferences and data/account management live on a dedicated Settings page, reachable from
the sidebar.

## Preferences

- **Default class duration** — how long a class or task's time block is when you don't set an end time
  yourself; used by Schedule, the Homework due-time picker, and Quiz custom-time mode.
- **Default examination length** — the same idea, but specifically for a [Final Exam](quiz.md#final-exams)'s
  end time, since exams usually run much longer than a regular class (defaults to 2 hours).
- **Exam sessions** — a free-form, editable list of named time presets (e.g. "Morning" at 09:00,
  "Evening" at 14:30) that show up as quick-pick buttons on a Final Exam's start time field. Add,
  rename, or remove sessions to match however your institution actually schedules exams — it's not
  locked to just morning and evening.
- **Notification reminder timing** — see [Notifications](notifications.md).

!!! tip "iPhone/iPad users"
    If notifications aren't turning on, check whether the app was added to your Home Screen first —
    see the note in [Notifications](notifications.md#iphoneipad-ios).

## Data & account

<!-- screenshot: settings-data-account.png (see SCREENSHOTS.md) -->

- **Export my data** — downloads everything you've entered as a single JSON file. Works fully offline
  and for guests too, since it reads straight from the local database.
- **Import data** — load a previously exported JSON file back in.
- **Delete account** — permanently removes your account and everything in it, on every device.

!!! danger "This can't be undone"
    Deleting your account removes everything — schedule, tasks, tests, study progress, grades — on
    every device, with no recovery option. [Export your data](../data/export-import.md) first if there's
    any chance you'll want it later.

## About

The About card shows the current app version, a changelog of what's new in recent updates (with a
"View update history" button for everything before that), and links to the
[Privacy Policy](../data/privacy-and-terms.md), [Terms and Conditions](../data/privacy-and-terms.md),
and open-source licenses used by the app.
