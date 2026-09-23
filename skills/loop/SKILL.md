---
name: loop
description: Repeat an in-session check at a requested cadence using an available wait or scheduling mechanism.
---

# Repeat an in-session task
Resolve the task, interval, termination condition, and authorized actions. Monitoring does not authorize fixes, comments, merges, or deployments unless separately requested.
Use only the runtime's exposed wait/scheduling mechanism. In Codex, use an available clock/wait tool while the turn remains active. Do not assume shell stdout can wake a completed turn or that notify_on_output exists.
Run the check, report meaningful changes, then wait at the agreed cadence. Keep waits interruptible and respect required progress-update intervals.
Preserve the task state and respond to stop requests immediately. Do not leave orphan shell watchers.
If the user needs scheduled execution after the session ends, use an available supported automation mechanism with authorization; otherwise state that persistence is unavailable.
