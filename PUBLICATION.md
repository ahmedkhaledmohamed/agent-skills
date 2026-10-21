# Publication review

Changing repository visibility exposes history and repository surfaces as well as the current files. Keep visibility unchanged until the review is complete and the owner approves the exact action.

## Content boundary

Export reusable methods, independently written fictional examples and public integration terminology. Exclude employer details, business plans/requests, internal identifiers/URLs, datasets, source code, conversations, credentials, private account configuration and personal machine paths. Do not turn private material into a superficially renamed example. Third-party plugin code or instruction bundles require their own rights and attribution; they are not included by default.

## Checks

```sh
python3 scripts/check_portability.py .
python3 scripts/check_portability.py . --history
```

Supply organization-specific `--deny-pattern` values locally; never commit those terms or the matched private text into a publication report. The checker reports locations/object IDs and rule names, not matched values. It checks tracked and unignored new text files; history mode also checks reachable blobs and commit metadata across local refs. Fetch the remote branches and tags intended for publication before relying on that scope.

Inspect findings manually, including source ownership, binaries and examples. Also review remote branch/tag coverage, issues, pull requests and comments, releases/assets, wikis, automation artifacts and any other enabled repository surfaces. A clean pattern check does not establish safe disclosure or licensing clearance. Deleting a file from the current branch does not remove it from history. History rewriting, asset deletion and visibility changes are separate owner decisions.

Record the reviewed revision, filters, exclusions and unresolved findings in the private publication working record. Public contribution records should contain only sanitized decisions and outcomes. Do not paste private findings into a public issue or PR.

## License and ownership decision

The repository license describes the permitted reuse of material the owner has the rights to publish. Before publication, confirm that the owner can license the included instructions, scripts and examples under that license. Source scans and contribution records cannot establish authorship or clear third-party rights. Review any adapted material for its original license and required attribution; exclude it or preserve the applicable notice when appropriate.

External runtimes, providers, plugins and evaluation frameworks remain separate dependencies. A reference to a product is not permission to copy its resources or a claim that its integration has been tested. Review the selected skill's dependencies and current validation limits before promoting it.

## Record the final visibility decision

Keep the publication working record private. Record the reviewed default-branch revision and every exposed branch/tag/PR revision, the checked remote surfaces, exclusions or missing access, licensing/ownership decision, and exact visibility action approved by the owner. Refresh this review after new commits or remote comments when they materially change the reviewed scope. Do not treat an inaccessible surface, an absent CI result or a clean pattern scan as an all-clear result.

Repository-linked projects can have separate access controls; check their association and visibility rather than assuming they become public or remain private with the repository. Review available Actions logs and artifacts as well as source files. Removing material, rewriting history, merging pending changes and changing visibility remain separate authorized actions.
