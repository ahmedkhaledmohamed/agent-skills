---
name: eval-reporter
description: Summarize existing eval results and trends with their method, coverage, and calibration limits.
---

# Report evaluation results
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Resolve the requested period and use the framework's UTC date convention. Read the existing result records and distinguish missing data from a score of zero.
Use the existing core.reporter functions for the requested daily, weekly, trend, or dashboard output. Inspect function signatures before calling. A request for an inline answer does not require creating a dashboard or extra files.
Explain which categories and artifacts were included, counts, evaluation method, rubric/model changes, and material missing data.
Present structural scores as template diagnostics. Do not describe workflow-event heuristics as human ratings or imply that an uncalibrated composite measures product quality.
Compare like-for-like periods. Flag changes in artifact mix or rubric/model versions before interpreting score movement as regression.
Return observed results and useful actions. If no records exist, say so and identify a specific evaluation that could produce them; do not claim hooks are installed or running without checking.
