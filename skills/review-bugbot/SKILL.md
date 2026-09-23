---
name: review-bugbot
description: Review a scoped code diff for bugs, using Bugbot only when that reviewer is available.
---

# Review for bugs
Resolve the repository and requested diff. Inspect read-only in the existing checkout when possible; use an isolated worktree for a different branch or PR.
Discover available reviewer roles/tools. If Bugbot is exposed, invoke its actual documented contract. Otherwise perform a normal code review and identify it as such; never claim Bugbot ran.
Prioritize consequential correctness, regression, and edge-case findings with file locations and evidence. Do not manufacture findings.
Do not fix code, change branches in the primary worktree, post review comments, or resolve threads unless authorized.
Report findings and material limits, including checks not run.
