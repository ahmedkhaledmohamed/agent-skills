---
name: cursor-settings
description: Change Cursor editor or VS Code-compatible settings when that editor is the intended target.
---

# cursor settings
Resolve the actual editor and user/workspace settings file. On macOS Cursor normally uses ~/Library/Application Support/Cursor/User/settings.json; verify existence rather than substituting a Codex directory.
Preserve JSONC comments and unrelated values. Match the requested user or workspace scope.
Use official current documentation for Cursor-specific settings. General editor settings and agent runtime configuration are separate.
Do not infer permission to change CLI approvals, identities, or credentials from an editor appearance request.
