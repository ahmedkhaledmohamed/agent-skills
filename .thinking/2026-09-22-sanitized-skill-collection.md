# Sanitized skill collection

## Problem Framing

Personal agent workflows needed a private version-controlled home without transferring organization-specific context, credentials, or session history.

## Approach

Prepared a separate collection of portable skill instructions in an isolated feature worktree. Generalized organization-specific workflows and names, omitted internal references and third-party plugin bundles, and retained explicit runtime and evaluation-framework dependencies.

## Key Decisions

The repository is a maintained sanitized collection rather than an automatic mirror of installed skills. Installed originals remain unchanged, and publication requires review of the exact sanitized diff.

## Outcome

Prepared 47 skills and checked their structure, folder names, local references, and sensitive-content patterns. The draft is local and uncommitted; remote publication and the first pull request await diff approval and initialization of the repository's default branch.
