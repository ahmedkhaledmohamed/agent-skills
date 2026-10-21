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
