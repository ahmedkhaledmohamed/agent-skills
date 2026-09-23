---
name: cursor-create-hook
description: Create or update Cursor hooks for a requested Cursor agent event.
---

# cursor create hook
Confirm the requested event, effect, scope, and fail-open/fail-closed behavior from context.
Read current Cursor hook documentation and existing .cursor/hooks.json or user hooks before writing. Verify event names and JSON contracts; do not reuse another runtime's hook schema.
Use project hooks for shared project behavior or user hooks when requested. Preserve existing hooks.
Validate the script's input/output and failure behavior without performing the production action it gates.
For Codex hooks, use the current Codex documentation and runtime-specific configuration.
