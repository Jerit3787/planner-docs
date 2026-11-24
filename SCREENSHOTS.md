# Documentation screenshots

Every image in `docs/img/` is a capture of the current app, filled with a synthetic student so no
real person's data appears. Retake them when the screens they show change.

## Rules

- Capture the released app, not an older interface.
- Use the synthetic data below, never a real account. Don't capture from the Mac app on a machine
  where Stutastic Planner is installed: a local build shares its bundle id and opens the installed
  app's data.
- Check that text is readable and that no personal information, account id or internal URL appears.
- Give every image alt text that says what it shows.
- Phone captures go in at 480 px wide and show at `{ width="240" }` to `{ width="260" }`, two or
  three to a line. Wide captures (iPad landscape) go in at 1400 px and show full width.
- Name files `phone-<screen>.png` or `ipad-<screen>.png`, and update the table below.

## The synthetic student

`tools/screenshot-data/make_dataset.py` writes a Stutastic Planner backup for a second-year Computer
Science student on 24 November 2026: five subjects with marks, nine weekly classes (one cancelled
date), tasks, study topics, quizzes and final exams, events and a holiday, attendance marks with one
subject past the warning line, and focus history.

```bash
python3 tools/screenshot-data/make_dataset.py > tools/screenshot-data/sample-student.json
```

Change `TODAY` in the script to move the whole semester around a different capture date.

## Capturing on the iOS Simulator

1. Boot an iPhone or iPad Pro 11-inch simulator, set its clock display with
   `xcrun simctl status_bar <udid> override --time 9:41`, and install a build of the app.
2. Copy `sample-student.json` into the simulator's **On My iPhone** folder: the `File Provider
   Storage` folder of the `group.com.apple.FileProvider.LocalStorage` app group
   (`xcrun simctl get_app_container <udid> group.com.apple.FileProvider.LocalStorage groups`).
3. The dataset is built around `TODAY`. Capture on that date, or set `TODAY` to the day you capture
   and regenerate the file.
4. Launch the app, choose **Restore a backup → Choose a backup file**, pick `sample-student.json` and
   **Restore**.
5. Capture with `xcrun simctl io <udid> screenshot <file>.png`. It also captures system sheets, such
   as the file picker, that some simulator tools miss.
6. Rotate the iPad to landscape for the wide layouts. Resize: phone captures to 480 px wide, iPad landscape to 1400 px.

## Current captures

| Image | Used on |
|---|---|
| `phone-welcome`, `phone-setup-1`, `phone-setup-2`, `phone-no-semester` | First-run setup |
| `phone-nav-planner-group`, `phone-nav-coursework-group`, `ipad-dashboard`, `ipad-tasks-detail` | Getting around |
| `phone-dashboard`, `phone-dashboard-trends`, `phone-dashboard-dark`, `ipad-dashboard-wide` | Home, Dashboard |
| `phone-planner-month`, `-week`, `-day`, `-add`, `-menu`, `phone-class-new`, `phone-class-detail`, `phone-class-cancel-date`, `phone-paste-timetable`, `ipad-planner-week-wide` | Planner |
| `phone-agenda`, `phone-holiday-new` | Agenda, events and holidays |
| `phone-tasks`, `phone-task-detail`, `phone-task-new` | Tasks |
| `phone-study` | Study topics |
| `phone-quizzes`, `phone-final-exam-detail` | Quizzes and exams, Study topics |
| `phone-subjects`, `phone-subject-detail`, `phone-subject-grades`, `phone-academics`, `phone-semester-detail`, `ipad-subject-grades` | Subjects and academics |
| `phone-subject-attendance`, `phone-attendance-menu`, `phone-settings-attendance` | Attendance |
| `phone-focus-plan`, `-settings`, `-ready`, `-running`, `-timer`, `-lockscreen` (JPEG), `-whats-next` | Focus sessions |
| `phone-settings-reminders` | Reminders |
| `phone-settings`, `phone-settings-more`, `phone-settings-appearance`, `phone-settings-appearance-dark`, `phone-settings-google-calendar` | Settings |
| `phone-restore-backup` | Export and import |

Not captured: the Mac menu bar and the Linux tray are described in words only.
