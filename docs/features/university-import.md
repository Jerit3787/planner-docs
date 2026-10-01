# Import from your university

If your university is supported, Stutastic Planner can sign in to your student portal and bring in a
semester's subjects and weekly classes, so you don't have to type them in.

## Supported universities

The app lists the universities it can import from, with the name of each one's portal. The list
currently includes IIUM (i-Ma'luum), UiTM, IIC, APU, UniKL, UTM and UPSI. Universities are added as
the import service gains support for them.

IIUM's import is available in the app on your phone, tablet or computer, but not on the web.

## Import a semester

You can start an import from four places:

- the **Bring in your timetable** step of first-run setup;
- **Settings → Your university** → **Import timetable**;
- **Planner** menu → **Import from your university**;
- a semester's details → **Import timetable**.

When the app knows your university (you chose it in setup or in **Settings → Your university**),
the import starts at signing in. Otherwise it asks which university first, and remembers it.

Then:

1. **Choose your university.** The app remembers your choice on this device.
2. **Sign in** with your student ID and portal password. Your student ID is remembered on this
   device; your password is not, unless you choose to stay signed in (see below).
   The app shows each step as it signs in and loads your timetable.
3. **Choose the semester** to import. The one matching your semester's name is chosen for you.
   Older semesters are loaded when you choose them.
4. **Review.** Each subject shows its code, name, credit hours, section, lecturer and weekly classes,
   marked **New** or **Already here**. Untick anything you don't want.
5. **Import.** The app adds what you ticked, then you can open your timetable.

### What an import changes

- **New subjects** are added with their code, name, credit hours, section, lecturer and a colour.
- **Subjects you already have** are matched by their code. Only their empty details are filled in;
  names and anything you typed are kept.
- **Classes** are matched by day and start time. A matching class gets the portal's end time and room
  and keeps its own colour, week pattern and exceptions; anything else is added.
- **Nothing is removed.** Classes in the app that aren't in the import stay as they are.

Importing the same semester again changes nothing.

## Keep your timetable up to date

On the sign-in step, tick **Keep me signed in to refresh my timetable** if you'd like the app to
notice changes at your university, such as a class moved to another room or time, or a subject added
or dropped. This option isn't available on the web.

- The app checks at most once a day, when you open it or come back to it, and only when you're
  online.
- If something changed, the Dashboard and Planner show **Your timetable changed**. Choose **Review**
  to see each change.
    - Changes are ticked to apply, except for classes **you changed yourself**, which are kept unless
      you tick them.
    - A subject dropped at your university can have its classes removed; the subject itself stays.
    - Choose **Apply** to make the ticked changes, or **Ignore** to leave your timetable as it is.
- If your portal stops accepting the kept password (for example after you change it), the app
  deletes it and asks you to **Sign in again**.

To see which semesters are kept up to date, check now, or stop, go to **Settings → Your
university** and choose **Refresh now** or **Forget my login**. Signing out or deleting your account
also deletes every kept login.

## Your password

- **IIUM:** the app signs in to i-Ma'luum directly from your device. Your password goes only to
  IIUM's sign-in page, over an encrypted connection, and never to us.
- **Other universities:** your password is sent over an encrypted connection to the Stutastic
  Planner import service, only so it can sign in to your university's portal for you. The service
  doesn't store or log it.
- If you choose to stay signed in, the password is kept **only on your device**, in its secure storage
  (the Keychain on Apple devices, Keystore-protected storage on Android). It's never synced to your
  account or included in exports.

See the [privacy policy](../data/privacy-policy.md#university-timetable-import) for details.
