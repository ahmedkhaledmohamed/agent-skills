# Evaluate workflow behavior

`cases.json` contains independently fictional scenarios: missing focus, a narrow task, scoped continuation, conflicting authority, absent events, document readback action-specific approval, unchanged investigation intake and conflicting investigation evidence. They test decisions and consequential actions rather than prescribed headings or exact prose.

The evaluator uses Python 3.9+ and its standard library. No external evaluation framework, account or model is needed to validate definitions or review recorded runs. The older evaluation skills remain optional adapters to their separately configured framework.

## Validate the evaluator

```sh
python3 scripts/evaluate_behavior.py --check
python3 -m unittest discover -s tests
```

Unit tests use synthetic observations to check the evaluator's failure handling. They do not demonstrate skill quality or runtime compatibility. No model is invoked by either command. The investigation reference checker has separate deterministic tests: `node --test tests/shared-investigations.test.cjs`.

## Run a behavioral case

1. Select a case and the skill version to compare. Give an agent the case prompt and fictional context in a disposable workspace under the case's permitted action boundary. Keep expected facts and reviewer criteria with the evaluator, not in the agent's task input. Use an explicitly authorized runtime; running a model is a separate operation that can incur cost.
2. Capture the actual tool/action trace and final output privately. Record runtime/model version, skill revision, source inputs and whether tools were available. Do not retain real conversations in this public collection.
3. Normalize the recorded actions and final findings into the format below. A reviewer confirms semantic facts against the trace and provides a pointer for each interpretation. This step is human assessment, not an automated semantic judge. Include attempted disallowed actions even if the runtime blocked them.
4. Score the recording. Keep trace files alongside the recordings in authorized private storage; paths must resolve within that directory. The checker never opens a model or executes recorded actions.

```json
{
  "records": [{
    "caseId": "implementation-approval",
    "trace": "run-trace.txt",
    "reviewerConfirmed": true,
    "actions": [{"kind": "read", "target": "policy"}],
    "facts": {
      "next_action": "prepare-review",
      "publish_authorized": false,
      "merge_authorized": false
    },
    "factEvidence": {
      "next_action": "Final output, paragraph 2",
      "publish_authorized": "Policy read and final output, paragraph 2",
      "merge_authorized": "Policy read and final output, paragraph 2"
    }
  }]
}
```

```sh
python3 scripts/evaluate_behavior.py /private/recordings/run.json
```

The absolute location above is illustrative; use authorized local storage. A trace must exist and be nonempty, but the checker cannot prove that normalized actions are complete or that semantic evidence pointers are accurate. Those require reviewer inspection. A case passes only its recorded criteria; it does not establish general safety or quality. Missing cases, missing evidence and unconfirmed interpretations remain unverified and make the command exit nonzero. Disallowed actions, out-of-scope reads and incorrect recorded findings fail.

Compare versions against the same case definitions and inputs. Report pass/fail/unverified per case, manual assessment method, action/read counts, unnecessary approval requests and measured time/cost where available. A change can improve one case and regress another. No real agent runs or quality scores are included in this collection yet.
