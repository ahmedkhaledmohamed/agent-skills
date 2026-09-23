---
name: review-security
description: Review a scoped code diff for security issues, using a specialized reviewer when available.
---

# Review security
Resolve the repository, change, and relevant security boundary. Inspect the diff read-only or use an isolated worktree when another checkout is required.
Use a specialized security reviewer only if the actual runtime exposes one; otherwise conduct a local defensive review and disclose the method.
Trace plausible exploit paths and preconditions. Prioritize evidenced findings over speculative checklist issues.
Do not exploit live services, alter production data, fix code, or post external findings without authorization.
Report severity, location, evidence, impact, and assessment limits. Do not claim automated review or tests ran unless verified.
