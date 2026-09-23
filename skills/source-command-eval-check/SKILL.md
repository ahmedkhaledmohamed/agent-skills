---
name: source-command-eval-check
description: Run a focused quality check on one specified artifact.
---

# Check one artifact
Locate the framework checkout (AI_EVALS_FRAMEWORK_DIR when set, otherwise ask for the checkout location) and verify core/ and plugin/rubrics/ exist before running commands. Run modules from that checkout with its working Python environment. Do not guess a relative core module from the user's project.
Inspect the current implementation and CLI help when arguments or model support are uncertain. Report unavailable dependencies as unavailable, not as failed output quality.

Resolve the target explicitly; for a shorthand target, use the last discussed artifact only when unambiguous.
Select checks by the user's intended deliverable. Do not require phone frames in all HTML, full brief headings in short notes, or semantic judging based solely on word count.
Use the existing structural evaluator and relevant rubric where applicable. Verify source claims and behavior when the question requires it.
Report actual results, method, limitations, and consequential findings. Distinguish an inline review from a framework run.
Persist results only through the framework's supported workflow when authorized; avoid duplicate logging if the command already saves them.
