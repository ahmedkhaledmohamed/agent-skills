---
name: deploy-prototype
description: Translate a supplied design into a native client prototype for the requested iOS or Android app and prepare its draft PR.
---

# Prepare a native mobile prototype
Use the supplied design repository, screenshot, JSON, or description. Infer the intended app/platform from context; ask when it changes scope. Do not add another platform just because an example supports both.
Read current client repository guidance and actual prototype gallery registration/build targets. Use an isolated worktree from the fetched default branch or the intended existing prototype branch; do not switch the primary checkout.
For a supplied repository, use a unique temporary checkout when needed. Inspect its source and any available local translator before running it. Do not install dependencies or trust a scaffold as a faithful rendering without review.
Translate layout and interactions using current platform patterns and the project's design-system guidance. Preserve text, hierarchy, states, accessible controls, and the important user flow. Verify token and component mappings against current sources rather than hardcoded historical tables.
Keep prototype code in the existing prototype module and register it with the actual gallery. Do not put exploratory prototype code into the production module.
Use the build wrapper, app/platform targets, environment, and flags required by the target repository. Build affected targets and run required client lint checks.
For simulator verification, identify the intended simulator and use a unique temporary artifact directory. Never remove or overwrite a shared application bundle. Install/launch only within the requested verification scope.
Compare rendered states with the supplied design and resolve material differences before publication. Do not claim an Android check from an iOS-only build.
Follow the sanitized thinking-trail and exact-diff approval workflow. Submit or update a draft PR on the intended branch when authorized; do not self-merge.
Report actual build/CI status and the project's current prototype installation instructions after verifying them. Do not promise a fixed build duration or universal distribution access.
Device installs, TestFlight uploads, merges, and distribution require the corresponding authorization. For a requested TestFlight upload, follow the workspace App Store Connect API-key workflow.
