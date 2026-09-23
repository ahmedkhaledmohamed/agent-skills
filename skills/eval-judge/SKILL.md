---
name: eval-judge
description: Assess an AI artifact against a relevant rubric, separating supported findings from assessment uncertainty.
---

# Evaluate an artifact
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Select the rubric by the artifact's task: structured-doc, open-reasoning, data-analysis, code-technical, or search-retrieval under plugin/rubrics/. Read it before scoring.
Evaluate against the user's actual request and supplied evidence, not merely headings. Keep justified uncertainty; do not reward unsupported confidence.
Use python3 -m core.judge --output <absolute-file> --rubric <absolute-rubric> when the framework judge is appropriate and available. It invokes claude --print; omit --model to use the implementation's default unless a supported model is requested.
An inline review is an inline review, not a completed framework run. Never invent machine-generated scores, timing, calibration, or stored results.
Report consequential findings with locations and evidence. If no weakness is supported, say so; do not invent one to fill a quota.
If showing scores, include the rubric, method, artifact version, sample limitations, and whether relevant calibration exists. Compare baselines only for compatible task/rubric/model versions.
