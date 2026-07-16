# FAQ

**Does the app work offline?**
Yes — every page reads and writes to a local database first. See [Offline & sync](offline-and-sync.md).

**Do I need an account?**
No. You can use the entire app as a guest; your data just stays on that one device. See
[Guest mode vs. an account](getting-started/guest-vs-account.md).

**I used the app as a guest and want to switch devices — how do I bring my data with me?**
Either sign in with a real account (which uploads your guest data automatically), or export your data as
JSON and import it on the new device. See [Export & import](data/export-import.md).

**Why did my scheduled class/deadline time shift after I traveled or changed my device's timezone?**
Times are stored as a fixed point in time and displayed converted to your device's current timezone —
the same way most calendar apps behave, so a class you scheduled at 9am your original timezone shows
correctly whichever timezone you're actually in later.

**My programme is based in a different country than where I'm actually studying — how do I handle that?**
Set a timezone override on that Programme (in Academics). Classes, quizzes/exams, and task due times
are then authored in that timezone, but always display converted for wherever you actually are. See
[Programmes](features/academics.md#programmes).

**How does the app know which week is "Week A" for my alternating classes?**
From the biweekly anchor date you set on your semester. See
[Alternating (biweekly) classes](features/schedule.md#alternating-biweekly-classes).

**Why does my GPA show a "~" in front of it?**
It means the number is still an estimate — at least one subject in that calculation isn't finally
graded yet. See [Subjects and grading](features/academics.md#subjects-and-grading).

**I'm on iPhone/iPad and notifications won't turn on — why?**
Add the app to your Home Screen first (Safari's **Share → Add to Home Screen**), then open it from
that icon and try again — Safari only delivers push notifications to an installed PWA, not a regular
browser tab. See [Notifications on iOS](features/notifications.md#iphoneipad-ios).

**I'm using guest mode on an iPhone/iPad — is my data safe if I don't open the app for a while?**
Not indefinitely. iOS can clear a web app's local storage after about two weeks of it going unopened,
and guest data has no cloud backup to fall back on. Open the app periodically, or
[create an account](getting-started/guest-vs-account.md) so it's backed up to the cloud instead.

**Is my data ever sold or shared?**
No. See [Privacy & terms](data/privacy-and-terms.md).

**How do I delete my account?**
From [Settings](features/settings.md) → Delete account. This is permanent and removes everything on
every device.

**I found a bug or have a feature request — where do I report it?**
Email [support@danplace.tech](mailto:support@danplace.tech).
