---
name: catalog-publishing
description: Publish approved research or product references through a product catalog's maintained sources, generators, and reviewed deployment workflow.
---

# Publish to a product catalog
Resolve the actual repository through the workspace path; read current upstream README, applicable AGENTS/CLAUDE guidance, package scripts, and maintained source mappings. Do not assume historical navigation or generator names remain current.
Use an isolated worktree from the fetched default branch. Preserve unrelated changes and manual editorial decisions.
Identify the maintained records or generators for the requested pages. Edit those sources rather than generated search indexes or compiled prototype bundles. Run affected generators, then required dependent search/directory generation and catalog checks as specified by the current README.
Preserve measurement windows, query/source revisions, population, exclusions, and evidence limitations. Rebuild dates are not evidence-refresh dates. Change evidence hashes only after reviewing the corresponding artifact.
Keep product contracts, delivery status, research, and exploratory prototypes distinct. Register new content in the current reader navigation and discovery sources.
Use a static preview for content changes when suitable. Inspect server startup before treating it as read-only; database initialization or migrations can change persistent state. Runtime tests need a disposable data boundary.
Check changed reader paths, mobile/desktop readability, keyboard access, and meaningful loading/error states. Report what was actually verified.
Follow sanitized thinking-trail and exact-diff approval requirements before pushing/creating a PR. Never self-merge without explicit authorization.
After an authorized merge, wait for the repository's automatic CI/CD deployment and verify the changed live behavior with an authorized reader. An SSO redirect alone is not a successful smoke test. Manual deployment requires explicit permission or confirmation that CI/CD is broken.
