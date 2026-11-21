# Privacy Policy

**Last updated: 21 November 2026**

This Privacy Policy describes how Stutastic Planner, published by Danish Studio Production, handles
information when you use the app and its support tracker. For privacy questions or requests, use the
[support tracker](https://support.danplace.tech/p/stu) and choose **Private** for anything personal.

## Information the app handles

### Planner records

Planner records can include programme, semester, subject, class, event, task, quiz, result, study
topic, focus-session, and preference information that you enter.

- In **guest mode**, planner records stay in the app's local database on that device and are not
  synced to an account.
- When you use a **signed-in account**, planner records are stored locally and synced through
  PowerSync and Supabase so you can use them on your other signed-in devices.
- If you use the support tracker, we receive the information you submit there — see
  [Support tracker](#support-tracker). Please do not upload passwords, sign-in codes, or private
  academic records.

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

- **IIUM:** the app signs in to i-Ma'luum directly from your device. Your student ID and password go
  only to IIUM's own sign-in page, over an encrypted connection, and are never sent to us. Your
  timetable and results are read on your device the same way.
- **Other universities:** the app sends your chosen university, student ID and portal password over
  an encrypted connection to the Stutastic Planner import service. The service uses them only to
  sign in to your university's portal and return your timetable to the app. It doesn't store your
  password, student ID or timetable, and its logs are turned off.
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
  synced. Choose **Forget my login** at **Settings → Your university** to delete it; signing out
  or deleting your account also deletes it. This option isn't offered on the web.
- The import service is free software under the GNU Affero General Public License. Its source code
  is available at
  [github.com/Jerit3787/planner-connect](https://github.com/Jerit3787/planner-connect).

## Support tracker

Bug reports, feature requests, votes, and replies are handled through the support tracker at
[support.danplace.tech](https://support.danplace.tech/p/stu). You can browse and search public issues
without an account. Reporters do not need to sign in.

When you submit a report, you provide:

- the app and area, a summary, what happened, optional steps to reproduce, expected and actual
  results, and the environment (for example, device and browser);
- how much it affects you, and optionally up to five attachments (images, video, PDF, text, or log
  files, up to 15 MB each);
- whether the report is **Public** (anyone can see, vote, and reply) or **Private** (only you and the
  team can see it);
- your name and email address.

Your email address is never shown publicly. It is used to send you a private link to follow your
report and to email you when its status changes. **Email me my links** at
[support.danplace.tech/links](https://support.danplace.tech/links) sends a fresh private link for
every report submitted from your address.

The tracker stores reports, votes, replies, attachments, and the name and email you provide. Public
reports and their attachments are visible to anyone; choose **Private** for account details, personal
information, or anything you do not want public. Do not upload passwords, sign-in codes, or private
academic records.

The tracker is hosted by Vercel. Support reports are a separate record from your Stutastic Planner
account: deleting the account does not automatically delete them. We keep them for as long as needed
to investigate the issue and keep a record of it. To ask us to delete a report or your contact
details, reply on the private link emailed to you or submit a Private report.

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
- [Vercel privacy policy](https://vercel.com/legal/privacy-policy) — hosting for the support tracker.

## Retention and deletion

Signed-in planner records remain associated with your account until you delete the account. To remove
your Stutastic Planner account and synced planner records, choose **Delete my account** at
**Settings → Account**. The app requires an internet connection to complete deletion of synced data.
Account deletion also removes the server-side Google Calendar sync token and mapping. If the app
cannot confirm that cleanup, it stops deletion so you can retry. The dedicated calendar is managed by
Google and may remain in your Google Account if Google cannot complete its removal.

Support reports, votes, replies, attachments, and the name and email you provide are kept for as long
as needed to investigate the issue and keep a record of it. You can ask us to delete a report or your
contact details using the private link emailed to you or by submitting a Private report. Deleting
your Stutastic Planner account does not automatically delete support reports.

Turning Analytics off stops future collection from that device. Information already collected by
Firebase Analytics follows Google's retention settings. Service providers may retain copies in
backups according to their own retention practices.

You can export planner records as a JSON file from **Settings → Your data**. The export contains
planner records, not account credentials. Protect the file as you would any personal study record.

## Children and audience

Stutastic Planner is intended for students generally and is not specifically directed to children
under 13. The app does not ask you to enter your age or date of birth. If you have a question about a
child's use of the app or their information, submit a **Private** report at
[support.danplace.tech/p/stu/report](https://support.danplace.tech/p/stu/report).

## Changes to this policy

If this policy changes, the updated version and its date will be published on this page.
