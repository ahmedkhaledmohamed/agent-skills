---
name: messaging-evidence-review
description: Review a messaging capability or measurement claim against current client/backend behavior, instrumentation, and primary data.
---

# Review a messaging claim
Define the exact claim, product surface, platforms, population, and observation window. Read applicable workspace and repository guidance.
Trace each relevant platform independently through trigger, eligibility, format, action handler, OS/backend interaction, fallback, and instrumentation. Resolve current repository locations rather than relying on historical service paths.
Distinguish five questions: is it implemented; enabled for this population; delivered to the user; observable with available events; and shown to improve an outcome? Evidence for one does not establish the others.
Use current client/backend source and contracts for behavior, primary datasets for measurements, and dated documents for history. Record revisions, query/event specifications, retrieval dates, and material exclusions.
Search alternate event factories, leaf specifications, and logging paths before reporting a measurement gap. No rows in one specification are not proof of an absent flow.
Use token and token age for token records, device installation for an app instance, and delivery path for APNs/FCM plus processing. Keep token validity, permission, provider acceptance, device receipt, display, and engagement separate.
For token-age cleanup, keep null/unparseable ages in the retained population unless the policy explicitly includes them. Do not infer invalidity from inactivity alone.
For FCM high-priority claims, require evidence that realistic Doze-delayed delivery materially harms user value and that the request produces a visible notification. A foreground/user-initiated trigger, async completion, or CTR does not establish eligibility.
Classify each conclusion as supported, contradicted, or unresolved with the reason and evidence needed. Report the current state by default; add recommendations only when requested.
