---
name: cursor-migrate-to-skills
description: Convert selected Cursor commands or intelligent rules into Cursor skills while preserving their scope.
---

# cursor migrate to skills
Read the selected source files and current Cursor skill documentation. Preserve explicit-only behavior, arguments, file scope, and external-action authorization.
Migrate only requested files. Keep a recoverable source copy and show the mapping before retiring old entrypoints.
Use Cursor-supported destinations and verify local references. Do not perform a global text replacement of product names or move Cursor-specific APIs into Codex skills.
If the target runtime is Codex, use skill-creator and adapt the workflow to actual Codex tools instead.
