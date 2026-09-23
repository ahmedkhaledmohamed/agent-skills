---
name: eval-runner
description: Evaluate a specified AI artifact or requested category using the local eval framework and appropriate evidence.
---

# Run an evaluation
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Identify the user's requested scope and the artifact's actual purpose before choosing a category. File extension and headings are clues, not a substitute for context.
Run applicable structural checks with python3 -m core.eval_engine --check <absolute-file> --skill <verified-skill>. A template score is a structural diagnostic, not a calibrated quality estimate.
Use a judge when semantic evaluation is requested or necessary; word count alone is not a reason to launch a paid model. The current framework judge invokes the Claude CLI with --print, not Codex --print. Verify that runtime and use its configured supported model; do not invent a model name or silently change provider.
Judge against the requested deliverable, evidence, correctness, and usefulness. Do not penalize a short update for lacking a full-document template.
For category or all requests, state the selected artifacts, dates, checks, and exclusions. Do not trigger unrelated production refreshes or mutations as a smoke test.
Report only observed scores, failures, and counts. Label structural, judge, and human signals separately. Show APQS only if actually computed, with sample count and coverage; no fabricated default summary.
