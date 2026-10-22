# Portable agent workflows

Reusable instructions for product research, evidence review, writing, artifact reconciliation and bounded execution. Select the workflows that fit your task and provide your own authorized sources and local policy.

This repository is a separately maintained portable collection, not a mirror of an installed skills directory.

## Start here

Read [porting and workflow selection](PORTING.md) to choose a small skill set. Before making a repository public, complete the [publication review](PUBLICATION.md), including reachable history and remote surfaces.

For reproducible workspace setup, use the [PM AI Partner Framework](https://github.com/ahmedkhaledmohamed/PM-AI-Partner-Framework). It distributes a selected reviewed bundle without requiring access to this repository. This collection owns workflow instructions; private content, local source bindings and credentials remain separate.

- Session startup and continuation: `workspace-context`.
- Sustained authorized work and completion: `work-execution`.
- Documents, spreadsheets and derived views: `artifact-reconciliation`.

## Contents

- Product work: analysis, briefs, writing, meeting preparation, strategy, and critical review.
- Evidence and delivery: messaging claims, portfolio reconciliation, knowledge-base workflows, catalog publishing, and prototypes.
- Evaluation: artifact review, explicit feedback, calibration, regression analysis, and reporting.
- Runtime workflows: scoped Cursor guidance, code review, and in-session monitoring.
- Evidence-backed specifications: map owned features and source systems, reconcile historical delivery and current intended behavior, review source and intent drift, and assess stakeholder gaps with [`evidence-backed-specs`](skills/evidence-backed-specs/SKILL.md).

Each skill lives under `skills/<name>/SKILL.md`. Cursor-specific skills target Cursor, even when read by another agent. The evaluation skills require the separate personal evaluation framework with `core/` and `plugin/rubrics/`; set `AI_EVALS_FRAMEWORK_DIR` to its checkout. That framework and its dependencies are not bundled here.

## Scope and maintenance

Company-specific names, internal links, document identifiers, local machine paths, reference inventories, account configuration, and session history are excluded. Third-party plugins and their bundled resources are not copied here. Public product names and standard configuration paths remain where needed to identify the intended runtime.

Planning, knowledge-base, document, and publishing workflows discover the tools authorized for the target environment; they do not include internal integrations or credentials. Sanitized workflows may need local configuration before use.

Review changes to these copies independently. Do not automatically synchronize an installed directory into this repository. If installing a selected skill, check for an existing skill with the same name and preserve the original before replacing it. Installing the whole collection may duplicate skills already provided by other sources.

Updates use a feature branch and reviewed pull request. Keep private context outside this repository and review the full diff before any push.

## Portable specification workflow

Start with the [operating model](skills/evidence-backed-specs/references/operating-model.md) and [architecture](skills/evidence-backed-specs/references/architecture.md). The [artifact model](skills/evidence-backed-specs/references/artifact-model.md) and [illustrative schema](skills/evidence-backed-specs/references/record.schema.json) separate observed implementation, approved requirements, proposed needs, historical deliverables, verification stages, and gap decisions. [Change review](skills/evidence-backed-specs/references/change-loop.md), [evaluation](skills/evidence-backed-specs/references/evaluation.md), and the [porting guide](skills/evidence-backed-specs/references/porting-guide.md) cover maintenance and local adapters.

The [generic example bundle](skills/evidence-backed-specs/examples/bundle.json) can be checked locally:

```bash
python3 skills/evidence-backed-specs/scripts/validate_bundle.py skills/evidence-backed-specs/examples/bundle.json
```

That script checks IDs, references, and coverage of the bundle's declared source, feature, and assessed-need scope. It does not inspect source systems, validate every schema field, establish the team's full ownership boundary, or judge evidence quality. Provide authenticated source readers, accountable reviewers, and a publication path in the target environment.

## License and external dependencies

Repository material is distributed under the [MIT License](LICENSE). Referenced tools, providers and external evaluation frameworks are separate dependencies with their own terms; this repository does not bundle or relicense them. Product names identify integration targets and do not imply endorsement or certification.
