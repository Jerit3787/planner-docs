# Pomodoro Focus Sessions

![The Pomodoro timer running a focus session, linked to a task](../img/pomodoro-timer-running.png)

Focus/break cycles you can link to a task, quiz/test, or study topic — logging time against whatever
you're actually working on, so it shows up in the [Dashboard](dashboard.md#whats-on-it)'s
time-by-subject breakdown and score/progress tracking.

## Starting a session

Pick what you're working on (a task, quiz/test, or study topic — or run a plain, unlinked session) and
start the timer. It cycles between focus and break automatically, and a small badge shows which one
you're currently in.

!!! tip "Keyboard shortcut"
    Press `p` anywhere in the app (not just on the timer itself) to pause or resume an active session
    — see the full [shortcuts list](dashboard.md#keyboard-shortcuts).

## Auto-pause for a starting class or quiz

If a class or quiz on today's schedule is about to start while you have an active focus session
running, it pauses itself automatically instead of silently running through it — resume it yourself
once you're free again.

## Android: Live Activity notification

![The Live Activity notification showing a running focus session with a pause action](../img/pomodoro-live-activity-android.png)

On Android, a running or paused session mirrors itself into a persistent notification — a live,
OS-ticked countdown while a session is running, a static "Paused" line while it isn't, and a **Pause**
action right on the notification. On Android 16 and newer, this is also promoted to a real **Live
Update** (a status-bar chip and a lock-screen surface), on top of the ordinary notification every
Android version gets.

!!! note "If the app is closed mid-session"
    The notification isn't guaranteed to clear itself if the app process is killed while a session is
    active — it self-heals the next time you open the app, since resuming a session re-syncs the
    notification automatically.

## Home screen / desktop widget

![The Pomodoro widget showing a running session at a glance](../img/pomodoro-widget-desktop.png)

Your current session — running, paused, or idle — is also available as a widget you can glance at
without opening the app. It's view-only (no start/pause controls in the widget itself) — tapping it
opens the app straight to the focus session.

- **Android** — a home screen widget ("Pomodoro Focus"), alongside 13 other calendar/agenda widgets —
  add any of them the usual way (long-press your home screen → Widgets → Student Planner).
- **Windows, Linux, and macOS** — a small floating widget window, toggled on/off from
  [Settings](settings.md#home-screen-desktop-widgets).

!!! warning "macOS's Notification Center widget isn't showing correctly right now"
    macOS also has a real Notification Center widget for this (added via the system's own Widget
    gallery), but it isn't rendering correctly on real devices at the moment — we're still tracking
    down why. **Use the floating widget window instead in the meantime** (same toggle in Settings,
    also available on macOS) — it shows the same content and works correctly today.

## Linking to a quiz/test

Logging focus time against a linked quiz/test feeds the Dashboard's Pomodoro time-by-subject chart and
its **focus suggestions** (what to revise next) — see [Quiz & Tests](quiz.md#pomodoro-focus-sessions)
and [Study Topics](study.md#linking-to-a-test).
