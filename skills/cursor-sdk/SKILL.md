---
name: cursor-sdk
description: Build integrations with the Cursor SDK when the user explicitly targets Cursor agents.
---

# cursor sdk
Identify the intended runtime and installed SDK version. Cursor's SDK and OpenAI's Codex SDK are different products; do not substitute one for the other.
Inspect installed package documentation and current official Cursor SDK documentation before selecting APIs, authentication, or model IDs. TypeScript uses @cursor/sdk and Python uses cursor-sdk where supported by that version.
Use the requested local or cloud execution mode; preserve scope, credential boundaries, lifecycle cleanup, and output verification.
For OpenAI Codex SDK requests, use the available openai-docs skill instead of this workflow.
