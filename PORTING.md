# Using these skills in another workspace

## Choose a workflow

| Need | Skill |
| --- | --- |
| Start or resume with relevant context | [workspace-context](skills/workspace-context/SKILL.md) |
| Carry an agreed task through verification and handoff | [work-execution](skills/work-execution/SKILL.md) |
| Reconcile documents, sheets and published views | [artifact-reconciliation](skills/artifact-reconciliation/SKILL.md) |
| Review planning semantics and tools | [planning-workflow](skills/planning-workflow/SKILL.md) |
| Reconcile work across periods and outcomes | [portfolio-reconciliation](skills/portfolio-reconciliation/SKILL.md) |
| Establish or maintain source-backed specifications | [evidence-backed-specs](skills/evidence-backed-specs/SKILL.md) |
| Investigate product measurements | [data-analyst](skills/data-analyst/SKILL.md) |
| Compare competing solutions | [competitor-analyst](skills/competitor-analyst/SKILL.md) |
| Design or interpret an experiment | [hypothesis-tester](skills/hypothesis-tester/SKILL.md) |
| Record material contribution safely | [thinking-trail](skills/thinking-trail/SKILL.md) |
| Review documents and collaborator changes | [document-collaboration](skills/document-collaboration/SKILL.md) |

Start with the smallest useful selection. Core product skills are usable without planning APIs, databases, a knowledge index or a publishing site. Deeper workflows need source readers and reviewers supplied by the target environment. A missing integration is a stated limitation, not permission to invent data.

## Install selectively

Read the chosen skill and references, inspect dependencies, then copy its complete directory into a skill location supported by the target runtime. For Codex, a project `.agents/skills/` or user `~/.agents/skills/` is a discoverable option; verify the installed version's behavior. Use the runtime's own installation guidance for other agents.

Compare an existing same-named skill before replacing it. Keep a backup and preserve local customizations. Do not install the complete collection by default: Cursor-specific workflows, evaluation adapters and domain extensions are optional.

Supply local settings separately: repository/source locations, authorized connectors, accounts, publication policy and review authority. Do not put private mappings or credentials in these skill files. Prefer native repository instructions with a concise entry point; avoid startup hooks that inject the same full instructions again.

## Skill ownership and framework packaging

This collection maintains portable skill content. The public PM framework may bundle a selected snapshot with file hashes so it works without access to this repository. A bundle is a reviewed export, not a live installation mirror or an automatic sync of local skills. Keep framework navigation, templates and installer behavior in the framework repository.

New lessons belong here when they change decisions for a distinct repeatable task. Task-specific facts belong in the target workspace's working document. Inspect realistic inputs and observable outputs before broadening a rule; a correction in one project is not automatically a universal policy.

## Incorporate a lesson

Use an observed failure or repeated friction, not a hypothetical preference, as the input. Identify what decision would have changed and choose the smallest maintained home:

| Lesson | Maintained home |
| --- | --- |
| A changing fact or one task's accepted decision | Existing task document |
| A personal preference or account/authorization policy | Local user instructions |
| A repository convention | That repository's instructions |
| A procedure that generalizes to a repeated user goal | The relevant skill |
| A demonstrated failure or important decision boundary | A behavioral case, alongside the narrow correction |

Record the observation and proposed placement in the existing task's review, make a focused change, and check the same representative input before and after. One incident does not automatically justify a global prohibition or a new skill. Preserve the user's approval requirements; do not rewrite global instructions or synchronize installed directories automatically.

## Check a workflow change

[Behavioral cases](evals/README.md) provide fictional inputs, expected observable actions and reviewer criteria. The checker scores normalized recorded observations with linked trace evidence; it does not run a model or independently interpret prose. Keep the same cases when comparing versions and report unavailable cases. Evaluator unit tests are synthetic checks of the checker, not successful agent executions.

[Skill groups](catalog.json) identify runtime targets and external dependencies without duplicating skill descriptions. Generic guidance is not a guarantee that a connector or editor version works in a particular environment.
