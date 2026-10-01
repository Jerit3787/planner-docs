# Privacy Policy

**Last updated: 1 October 2026**

This Privacy Policy describes how Stutastic Planner, published by Danish Studio Production, handles
information when you use the app. For privacy questions, contact
[support@danplace.tech](mailto:support@danplace.tech).

## Information the app handles

### Planner records

Planner records can include programme, semester, subject, class, event, task, quiz, result, study
topic, focus-session, and preference information that you enter.

- In **guest mode**, planner records stay in the app's local database on that device and are not
  synced to an account.
- When you use a **signed-in account**, planner records are stored locally and synced through
  PowerSync and Supabase so you can use them on your other signed-in devices.
- If you email support, we receive the information you include in your message and any attachments.
  Please do not send passwords, sign-in codes, or private academic records.

### Account information

If you create or use an account, Firebase Authentication and your chosen sign-in provider process
account information such as your email address, display name, and sign-in credentials. You can sign in
with Google or email; Apple sign-in is available on Apple platforms. Stutastic Planner does not
receive your Google or Apple account password.

### Usage analytics

Firebase Analytics is enabled by default. It sends automatic app-usage events and an app-install
identifier. Planner records are not sent through Analytics. You can turn off **Usage analytics** at
**Settings → Privacy**. This setting is stored on each device and stops future Analytics collection
from that device; it does not erase information already collected by Google.

### Reminders

On supported native platforms, class and deadline reminders are scheduled locally on your device.
The app creates and schedules reminders locally; it does not use push messaging for reminders. The
operating system displays the notification text. You can turn reminders off in the app or manage
notification permission in your device settings. Reminders are not available on the web.

### Google Calendar

Google Calendar connection is optional and requires a signed-in Stutastic Planner account and your
Google authorization. The app creates a dedicated calendar for its own classes, tasks, and quizzes.
It does not access or manage your other Google calendars. A server-side authorization token is used to
keep that calendar in sync. Choose **Disconnect** at **Settings → Google Calendar** to end the
connection and ask Google to remove the Stutastic Planner calendar. Account deletion also attempts to
disconnect Google Calendar and removes the server-side sync token and mapping. If that server-side
cleanup cannot be confirmed, account deletion stops so you can retry. Google may leave the dedicated
calendar in your Google Account if it cannot complete the removal; you can remove it from Google
Calendar yourself.

### University timetable import

Importing from your university is optional. When you use it:

- The app sends your chosen university, student ID and portal password over an encrypted connection
  to the Stutastic Planner import service. The service uses them only to sign in to your university's
  portal and return your timetable to the app. It doesn't store your password, student ID or
  timetable, and its logs are turned off.
- To prevent misuse, the service counts sign-in attempts per network address and per student ID for
  about an hour. These counts are kept under one-way (SHA-256) hashes, never the address or ID
  itself. Requests must also carry a Firebase App Check token showing they come from the app.
- Your university's portal receives your student ID and password, as when you sign in to it
  yourself. Its own privacy policy applies to that sign-in.
- The app remembers your chosen university and student ID on your device so you don't retype them.
  Your password is not kept unless you choose **Keep me signed in to refresh my timetable**.
- If you choose to stay signed in, your password is kept only on your device, in the operating
  system's secure storage. It's never synced to your account, sent to us for storage, or included in
  exports. The record of which semester follows which portal also stays on your device and isn't
  synced. Choose **Forget my login** at **Settings → University timetable** to delete it; signing out
  or deleting your account also deletes it. This option isn't offered on the web.
- The import service is free software under the GNU Affero General Public License. Its source code
  is available at
  [github.com/Jerit3787/planner-connect](https://github.com/Jerit3787/planner-connect).

## How information is used

Information is used to provide the planner, authenticate accounts, sync planner records across your
devices, import and refresh your university timetable when you ask, maintain an optional Google
Calendar connection, schedule local reminders, respond to support requests, and understand general
app usage when Analytics is enabled.

Stutastic Planner does not include advertising and does not sell your personal information.

## Service providers

The app uses third-party services to provide its features. Those providers process information as
described in their own policies:

- [Google and Firebase privacy information](https://firebase.google.com/support/privacy) — account
  authentication and usage analytics. Google Calendar also receives the planner events you choose to
  sync.
- [PowerSync privacy policy](https://powersync.com/legal/privacy-policy) — account data
  synchronization.
- [Supabase privacy policy](https://supabase.com/privacy) — storage and services used for account
  data.
- [Apple privacy policy](https://www.apple.com/legal/privacy/) — if you choose Apple sign-in.
- [Cloudflare privacy policy](https://www.cloudflare.com/privacypolicy/) — hosting for the university
  timetable import service.

## Retention and deletion

Signed-in planner records remain associated with your account until you delete the account. To remove
your Stutastic Planner account and synced planner records, choose **Delete my account** at
**Settings → Account**. The app requires an internet connection to complete deletion of synced data.
Account deletion also removes the server-side Google Calendar sync token and mapping. If the app
cannot confirm that cleanup, it stops deletion so you can retry. The dedicated calendar is managed by
Google and may remain in your Google Account if Google cannot complete its removal.

Turning Analytics off stops future collection from that device. Information already collected by
Firebase Analytics follows Google's retention settings. Service providers may retain copies in
backups according to their own retention practices.

You can export planner records as a JSON file from **Settings → Your data**. The export contains
planner records, not account credentials. Protect the file as you would any personal study record.

## Children and audience

Stutastic Planner is intended for students generally and is not specifically directed to children
under 13. The app does not ask you to enter your age or date of birth. If you have a question about a
child's use of the app or their information, contact
[support@danplace.tech](mailto:support@danplace.tech).

## Changes to this policy

If this policy changes, the updated version and its date will be published on this page.
