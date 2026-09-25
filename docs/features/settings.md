# Settings

Settings is organised into pages. On a phone, tap a row to open it; on wider screens, the selected
page can appear beside the list.

## Available settings

- **Appearance** — choose light, dark, or system appearance.
- **Reminders** — enable or change on-device class and deadline reminders. Not available on the web.
- **Google Calendar** — connect or disconnect the dedicated calendar Stutastic Planner manages.
- **Class and exam lengths** — set default lengths and named exam start-time presets.
- **Password & email** — manage account credentials where available.
- **Account** — create an account from guest mode, sign out, or delete your account.
- **Your data** — export a backup or restore one.
- **Privacy** — turn Firebase usage analytics off or on for this device.
- **About** — see the installed version and open the documentation.

## Google Calendar

Google Calendar is optional and requires a signed-in Stutastic Planner account and Google
authorization. Planner creates and updates its own calendar for your classes, tasks, and quizzes; it
does not manage your other calendars. **Let Google Calendar remind me too** is off by default.

Use **Disconnect** in **Settings → Google Calendar** to stop the connection and remove the Planner
calendar. If you plan to delete your Stutastic Planner account, disconnect Google Calendar first.
Deleting the Planner account does not currently run the Calendar disconnect action.

## Account and data

The **Account** page offers **Create an account to sync**, **Leave without saving** or **Sign out**, and
**Delete everything** or **Delete my account**, depending on your session. See
[Guest mode vs. an account](../getting-started/guest-vs-account.md) before removing an account.

In **Your data**, choose **Export everything** to save a JSON backup or **Restore from a backup** to
load one. Restore can **Merge** the backup with existing records or **Replace** the current planner
data. Replace is destructive and asks for confirmation. See
[Export and Import](../data/export-import.md).

## Privacy and version

The **Privacy** page has a **Usage analytics** switch. It is stored per device and controls future
Firebase Analytics collection on that device. The **About** page shows the app version and links to
these docs; it does not contain an update history or an in-app update checker.
