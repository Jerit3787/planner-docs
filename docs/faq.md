# Frequently asked questions

**Does Stutastic Planner work offline?**
Yes. Planner changes are saved on your device. If you use an account, they sync when you are online.
Guest records stay on that device. See [Offline use and sync](offline-and-sync.md).

**Do I need to create an account?**
No. Choose **Not now, keep it on this device** during setup to continue as a guest. Guest records do
not sync. See [Guest mode vs. an account](getting-started/guest-vs-account.md).

**How do I use my guest data on another device?**
Create an account from **Settings → Account** to sync your current planner data, or export a backup and
restore it on the other device. See [Export and Import](data/export-import.md).

**Why are reminders unavailable in the web app?**
The web app does not schedule reminders. Use one of the apps, turn on **Settings → Reminders**, and
allow notifications in your device settings. Reminders are stored on that device and do not need
an account. See [Reminders](features/notifications.md).

**My reminders stopped.**
Reminders are scheduled two weeks ahead; open the app to schedule the next two weeks. Check that
notifications are still allowed for Stutastic Planner in your device's settings. On Linux, Planner
must be running.

**How do I connect Google Calendar?**
Sign in to Stutastic Planner, then open **Settings → Google Calendar** and choose **Connect Google
Calendar**. The app manages a dedicated calendar for its own planner items. See
[Settings](features/settings.md#google-calendar).

**How do I disconnect Google Calendar?**
Open **Settings → Google Calendar** and choose **Disconnect**. You can also delete your account
without disconnecting first; account deletion attempts to remove the Calendar connection
automatically. If that cleanup cannot be confirmed, deletion stops so you can retry.

**Can I import a timetable?**
Yes, two ways, both from the **⋯** menu on the Planner. **Import from your university** signs in to a
supported student portal and brings in your subjects and classes. **Paste a timetable** takes one
class per line. See [Bring in a timetable](features/schedule.md#bring-in-a-timetable).

**A class is cancelled this week. Do I delete it?**
No. Open the class and choose **Cancel a date**: only that date goes, and the rest of the term stays.
**Reschedule a date** moves one date instead. For a public holiday that cancels every class, add a
[holiday](features/calendar.md#holidays).

**My class alternates weeks. How do I add it?**
Set the semester's Week A anchor date, then set the class to repeat **Every 2 weeks** in Week A or
Week B. See [Alternating weeks](features/schedule.md#alternating-weeks).

**Why does my GPA have a "~" in front?**
Some subjects in it don't have a final grade yet, so it's an estimate. See
[Grading scales and GPA](features/academics.md#grading-scales-and-gpa).

**How many more classes can I miss?**
Open the subject's **Attendance** tab, or check the Dashboard's **Attendance warnings** card. See
[Attendance](features/attendance.md).

**Can I see the focus timer on my Lock Screen?**
On iPhone, yes: a running session shows on the Lock Screen and in the Dynamic Island. On Android it
shows as a notification. See [Focus sessions](features/pomodoro.md#while-it-runs).

**Are there keyboard shortcuts?**
Yes, on any device with a keyboard. See [Getting around](getting-started/navigation.md#keyboard-shortcuts).

**Can I create a backup?**
Yes. In **Settings → Your data**, choose **Export everything** to save a JSON backup. See
[Export and Import](data/export-import.md).

**How do I delete my account?**
Open **Settings → Account** and choose **Delete my account**. Export anything you want to keep first.
The app also attempts to disconnect Google Calendar; if it cannot confirm cleanup, account deletion
stops so you can retry. See [Settings](features/settings.md).

**Is planner data used for advertising?**
The app does not include advertising. Firebase usage analytics is on by default and can be turned off
for a device under **Settings → Privacy**. See the [Privacy Policy](data/privacy-policy.md).

**How do I report a problem?**
Use the [support tracker](https://support.danplace.tech/p/stu). Search existing issues first, then
choose **Report a bug**. Include the app version, device and OS, and the steps that caused the
problem. Choose **Private** if the report contains account or personal information. Do not upload
passwords, sign-in codes, or private study records. See [Support](support.md) for details.
