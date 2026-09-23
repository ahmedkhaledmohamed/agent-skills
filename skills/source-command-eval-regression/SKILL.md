---
name: source-command-eval-regression
description: Investigate changes in eval results using compatible baselines and observed artifacts.
---

# Investigate a regression
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Inspect baseline and recent populations, rubric/model versions, and sample counts before comparing scores.
Use core.regression functions when the requested data is available. Treat configured alert thresholds as investigation signals, not causal evidence.
Inspect representative changed artifacts and relevant skill/code revisions. Correlation with an instruction change does not establish causation.
Separate task-mix shifts, detector/rubric changes, missing records, and actual output deterioration. Do not edit skills or configuration for a diagnostic request.
Report observed counts and likely explanations with uncertainty. No available baseline means the regression assessment is unavailable, not all clear.
