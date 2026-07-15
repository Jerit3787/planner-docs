# Subjects & Academics

The structural layer everything else hangs off: **programmes** → **semesters/years** → **subjects**,
plus automatic GPA/CGPA calculation from your grades.

## Programmes

If you're tracking more than one course of study (a degree plus a minor, or a programme change
part-way through), each one is its own programme with its own semesters and subjects — switching your
active programme filters everything else in the app down to just that programme's data. A programme
can set default grading settings so every new semester under it starts pre-configured.

## Semesters and periods

A semester has a date range and, optionally, a set of **periods** inside it — lecture weeks, breaks,
revision week, exam period, holidays — each with its own date range. These periods drive:

- The teaching-week number shown on the Calendar and Schedule.
- No-class banners on days that fall inside a break/exam/holiday period.
- The [biweekly anchor date](schedule.md#alternating-biweekly-classes) for Week A/B classes.

The app always tries to default to whichever semester's date range actually **covers today** rather
than just the most recently created one — and flags on the semester picker if you've selected one that
hasn't started yet, or has already finished.

## Subjects and grading

Add the subjects you're taking each semester, along with credit hours and a grading scale. As you enter
grades, the app computes your semester GPA and running CGPA automatically. If you're exempted from a
subject requirement under a different programme (a transfer credit, for example), you can mark that
directly from a subject's details.

## GPA/CGPA on the Dashboard

Your active semester's GPA, alongside a study streak and upcoming deadlines, is summarized right on the
[Dashboard](dashboard.md) — no need to open Academics just to check where you stand.
