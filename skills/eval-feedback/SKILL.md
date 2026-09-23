---
name: eval-feedback
description: Record explicit user feedback about a specific AI artifact for later evaluation and calibration.
---

# Capture feedback
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Identify the artifact and version being rated. When ambiguous, ask which output the feedback concerns.
For explicit 1–5 ratings, preserve the original rating and scale in metadata and map to 0.2–1.0 for the existing FeedbackSignal API. Record the user's words when appropriate for local feedback storage, excluding secrets and unrelated private context.
For text feedback, preserve the text and dimension. Do not silently convert sentiment into a human numerical rating. If the existing schema requires a number, obtain a rating or keep the note separately from numeric calibration.
Use core.feedback.FeedbackSignal and append_feedback only for authorized logging. Confirm the artifact and rating recorded.
Committed, deployed, heavily edited, and abandoned are workflow events. Existing numeric defaults in the legacy engine are heuristic values, not human quality ratings. Keep them labeled and exclude them from human calibration.
When collecting retrospective ratings, let the user skip artifacts. Do not turn absence of a rating into dissatisfaction.
