# Subjects & Academics

<!-- screenshot: academics-overview.png (see SCREENSHOTS.md) -->

The structural layer everything else hangs off: **programmes** → **semesters/years** → **subjects**,
plus automatic GPA/CGPA calculation from your grades.

## Programmes

If you're tracking more than one course of study (a degree plus a minor, or a programme change
part-way through), each one is its own programme with its own semesters and subjects — switching your
active programme filters everything else in the app down to just that programme's data. A programme
can set default grading settings so every new semester under it starts pre-configured.

!!! info "Studying abroad? A programme can have its own timezone"
    <!-- screenshot: academics-programme-timezone.png (see SCREENSHOTS.md) -->
    If your programme is based somewhere other than where you're physically studying (an exchange
    semester, a fully-remote degree in another country), open the programme and set a **timezone
    override**. Every class, quiz/exam, and task due time you enter under that programme's semesters is
    then interpreted in *that* timezone — but still displays correctly converted for wherever you
    actually are when you check the app, and reminders still fire at the right real-world moment.
    Leave it unset (the default) and everything just uses your device's own current timezone, same as
    always.

## Semesters and periods

A semester has a date range and, optionally, a set of **periods** inside it — lecture weeks, breaks,
revision week, exam period, holidays, or a fully **custom** period (any name you choose, with its own
"classes run" and "counts as a teaching week" flags — useful for something like an orientation week or
reading week that doesn't fit the built-in types). Each period drives:

- The teaching-week number shown on the Calendar and Schedule.
- No-class banners on days that fall inside a break/exam/holiday period.
- The [biweekly anchor date](schedule.md#alternating-biweekly-classes) for Week A/B classes.

!!! tip "Adding periods is faster than it looks"
    <!-- screenshot: academics-periods-editor.png (see SCREENSHOTS.md) -->
    A new period's start date auto-fills from wherever the previous one left off (or the semester's own
    start date, for the very first period), with a 1-day placeholder end date — so you're mostly just
    adjusting end dates and picking a type as you go, not typing every date from scratch.

The app always tries to default to whichever semester's date range actually **covers today** rather
than just the most recently created one — and flags on the semester picker if you've selected one that
hasn't started yet, or has already finished.

Opening a semester splits into two tabs — **Overview** (its GPA, where you are in the term, every
period in the term, and a running "cumulative up to here" CGPA scoped to that semester's own programme)
and **Classes** (every subject in it with its credits and grade). Editing a semester is split the same
way — **Details** (name, dates, grading mode/scale) and **Periods** (the period list and biweekly
anchor date).

## Subjects and grading

Add the subjects you're taking each semester, along with credit hours and a grading scale. As you enter
grades, the app computes your semester GPA and running CGPA automatically.

!!! note "\"~\" means an estimate"
    A GPA shown with a leading `~` (e.g. `~3.81`) means it's still a projection — one or more subjects
    in that calculation don't have a final grade yet. Once every subject in the semester is graded, the
    `~` drops and the figure is locked in.

If you're exempted from a subject requirement under a different programme (a transfer credit, for
example), you can mark that directly from a subject's details — exempted subjects can be edited or
removed later from that programme's own page, not just added.

## GPA/CGPA on the Dashboard

Your active semester's GPA, alongside a study streak and upcoming deadlines, is summarized right on the
[Dashboard](dashboard.md) — no need to open Academics just to check where you stand.
