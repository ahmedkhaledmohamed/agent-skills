---
name: source-command-eval-improve
description: Propose evidence-backed skill or rubric improvements from evaluation patterns; apply only approved changes.
---

# Improve evaluation workflows
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Read the relevant evaluation samples, user feedback, task context, and scoring implementation before interpreting aggregates. Treat core.insights output as hypotheses.
Distinguish an output failure from a detector error, inappropriate rubric, missing evidence, and changed task mix. Inspect concrete examples of each proposed issue.
Prefer fixes that improve factual grounding, task completion, scope, and usability. Do not add required headings or remove honest uncertainty merely to increase scores.
Show each proposed change, supporting examples, expected behavioral benefit, and limitations. --dry-run is read-only. --apply allows implementation only within the user's approved changes and repository workflow.
After an approved change, evaluate realistic held-out tasks or relevant existing checks. A rescore of the same template is not proof of improved behavior. Report tradeoffs and regressions as well as improvements.
