---
name: cursor-migrate-to-builds
description: Assess or migrate a Cursor Cloud Agent environment to prebuilt environments when supported.
---

# cursor migrate to builds
Inspect the named Cursor environment and current provider documentation. Discover the available inspection/build tools and determine whether the migration is supported.
Identify install, startup, image/snapshot, dependencies, and persistent state from the real configuration.
For an assessment, report compatibility and proposed changes without mutating the environment.
For an authorized migration, preserve the old configuration, validate the proposed build in an isolated environment, and report actual results before switching anything that requires separate authority.
Do not follow missing legacy reference files or treat Cursor migration instructions as Codex environment guidance.
