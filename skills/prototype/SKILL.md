---
name: prototype
description: Build or revise an interactive mobile-app prototype in an existing product catalog.
---

# Build a mobile-app prototype
Resolve the target surface, platform, user flow, and requested interaction. Read current Catalog README and repository guidance before selecting files or commands.
Use the installed catalog-publishing workflow for source registration, validation, contribution approval, and release. Use an isolated worktree from the fetched default branch.
Research supplied Figma designs and the project's current design-system component/token/icon tools where available. Discover actual tool schemas instead of assuming legacy MCP names. Report missing access rather than inventing design fidelity.
Follow the current maintained prototype source and local patterns. Some prototypes use React bundles and others use HTML; do not force one format or hand-edit generated outputs.
Represent the relevant phone viewport, navigation, content, and state transitions. Use real supported icons and verified tokens, and distinguish illustrative data from measurements.
Provide meaningful interactions: navigation, dismiss/CTA behavior, state changes, and scrolling appropriate to the requested flow. Avoid decorative controls that appear functional but do nothing.
Register the prototype through maintained records and generators for the current navigation/search structure. Do not manually change generated SEARCH_INDEX.
Run required builds and checks and inspect rendered states at relevant viewport sizes. Use static previews for content where suitable; runtime server startup may modify persistent state and needs a disposable data boundary.
Follow the existing thinking-trail and exact-diff approval requirements before publication. A prototype request does not authorize merging.
After an authorized merge, wait for the repository's automatic CI/CD deployment and verify the changed live flow. Manual deployment requires explicit direction or confirmation that CI/CD is broken.
Prototype behavior is exploratory, not proof of a supported production capability.
