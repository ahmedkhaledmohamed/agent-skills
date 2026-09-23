# agent-skills

Sanitized, portable personal agent skills

Sanitized, portable copies of personal agent workflows. This repository is a separate maintained collection, not a mirror of an installed skills directory.

## Contents

- Product work: analysis, briefs, writing, meeting preparation, strategy, and critical review.
- Evidence and delivery: messaging claims, portfolio reconciliation, knowledge-base workflows, catalog publishing, and prototypes.
- Evaluation: artifact review, explicit feedback, calibration, regression analysis, and reporting.
- Runtime workflows: scoped Cursor guidance, code review, and in-session monitoring.

Each skill lives under `skills/<name>/SKILL.md`. Cursor-specific skills target Cursor, even when read by another agent. The evaluation skills require the separate personal evaluation framework with `core/` and `plugin/rubrics/`; set `AI_EVALS_FRAMEWORK_DIR` to its checkout. That framework and its dependencies are not bundled here.

## Scope and maintenance

Company-specific names, internal links, document identifiers, local machine paths, reference inventories, account configuration, and session history are excluded. Third-party plugins and their bundled resources are not copied here. Public product names and standard configuration paths remain where needed to identify the intended runtime.

Planning, knowledge-base, document, and publishing workflows discover the tools authorized for the target environment; they do not include internal integrations or credentials. Sanitized workflows may need local configuration before use.

Review changes to these copies independently. Do not automatically synchronize an installed directory into this repository. If installing a selected skill, check for an existing skill with the same name and preserve the original before replacing it. Installing the whole collection may duplicate skills already provided by other sources.

Updates use a feature branch and reviewed pull request. Keep private context outside this repository and review the full diff before any push.
