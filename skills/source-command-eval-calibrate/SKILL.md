---
name: source-command-eval-calibrate
description: Calibrate judge scores against explicit human ratings for matched artifact versions.
---

# Calibrate judge scores
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Read the requested feedback and result period. Include explicit quick_rating and retrospective human scores only. Exclude committed, deployed, heavy_edit, abandoned, inferred sentiment, and unconfirmed ratings.
Match pairs by artifact identity and version/content fingerprint when available, with rubric and judge model recorded. A shared filename or timestamps within a day are not sufficient to establish the same version. Exclude ambiguous matches and report them.
Validate scales, finite values, duplicate pairs, and variation in both score sets. If fewer than three valid pairs or either series is constant, report insufficient evidence for correlation.
Call core.judge.calibration_check(human_scores, judge_scores) for valid pairs. Report n, Spearman rho, mean signed difference, method, and the helper's approximate p-value with its limitations.
A threshold such as rho >= 0.7 is a heuristic, not proof of trustworthy scores. High rank correlation can coexist with systematic bias. State sample size, representativeness, version boundaries, and uncertainty.
Persist a calibration record only when requested, including matched and excluded counts, method, rubric/model versions, and limitations. Do not overwrite older evidence silently or fill example numbers into results.
