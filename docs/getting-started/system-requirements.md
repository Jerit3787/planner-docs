# System requirements

Student Planner runs three ways — as a web app (any modern browser), an installed PWA, or a native
desktop/Android app. Requirements differ slightly depending on which one you use.

## Web app / PWA

Any evergreen browser with Service Worker and IndexedDB support works — Chrome, Edge, Firefox, or
Safari, kept reasonably up to date. There's no hard version floor beyond that, but a few notes:

- **iOS/iPadOS**: use Safari specifically — Add to Home Screen only works from Safari, and installed-PWA
  push notifications require the app to have been added to the Home Screen first (see
  [Notifications](../features/notifications.md)). iOS Safari can also evict local data after about two
  weeks of the app going unopened — a real consideration for a **guest** session with no cloud backup.
  See [Offline & Sync](../offline-and-sync.md).
- **Android**: any recent Chrome works for both the browser and the installable PWA.

## Native desktop app

| Platform | Minimum version | Notes |
|---|---|---|
| macOS | **13.0 (Ventura)** or later | Universal build (Apple Silicon + Intel). Unsigned for now — right-click → Open on first launch. |
| Windows | **Windows 10** or later, x64 or ARM64 | The Microsoft Edge WebView2 Runtime is required and auto-installs if missing. Unsigned for now — SmartScreen: "More info → Run anyway". |
| Linux | A distro with **webkit2gtk 4.1** — Ubuntu 22.04 / Debian 12 or newer, roughly | Our published `.deb`/`.AppImage`/`.rpm` builds are compiled on Ubuntu 24.04 CI runners, so the pre-built binaries additionally need glibc 2.39+. AppImage is the safest bet on an older base. |

Desktop builds check for updates automatically and install them in the background — see
[Notifications](../features/notifications.md) for how you're notified once one's ready.

## Native Android app

**Android 7.0 (API level 24)** or later. Sideloaded APK — Android will ask you to allow installing from
this source the first time; the update flow after that uses the real system installer, same as any other
app.

## Not yet available

**iOS as a native app** isn't built yet — no iOS project exists in this codebase yet, so on iPhone/iPad
the [web app / PWA](#web-app-pwa) is the only option for now.
