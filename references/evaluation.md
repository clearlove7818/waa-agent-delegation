# Optional Evaluation Handoff

Read this reference only after independent evaluation is explicitly authorized and useful. Evaluation never starts automatically, changes the delegated artifact, or transfers final responsibility.

Evaluation returns use the protocol's first-line rule: the exact status token comes first, with `anomaly` or `subtype` on later lines; do not add a `status:` prefix.

## Modes

Use one compatible pair:

```text
evaluation_mode: INDEPENDENT_EVALUATION | EVALUATOR_OPTIMIZER_LOOP
evaluation_output_mode: CONVERSATION_ONLY | FILE_BACKED
```

- `INDEPENDENT_EVALUATION` may use either output mode.
- `CONVERSATION_ONLY` omits `evaluation_output_path` and grants no write authority.
- `FILE_BACKED` names one unique `evaluation_output_path`; the evaluator may write only that record or a non-overwriting new version.
- A formal Fei evaluation and every `EVALUATOR_OPTIMIZER_LOOP` use `FILE_BACKED`.
- Invalid mode/path combinations return `BLOCKED`; do not coerce them.

## Required binding

Every evaluation packet states:

```text
evaluation_id
evaluation_mode
evaluation_output_mode
evaluation_output_path: <required only for FILE_BACKED>
task_id
artifact_id
artifact_version
standard_id
standard_version
evidence_references
evaluation_scope
```

Also state the objective, exclusions, independence, allowed reads/tools, capability conditions, and external-access boundary. Evaluation does not replace the delegation packet or transfer artifact ownership.

## Loop-only fields

An explicitly authorized `EVALUATOR_OPTIMIZER_LOOP` additionally states:

```text
run_id
segment_id
round
comparison_artifact_version
change_evidence_references
previous_evaluation_path: <only when a prior evaluation record exists>
```

`artifact_version` is the candidate; `comparison_artifact_version` is the round baseline; `change_evidence_references` bind the candidate to that baseline; `previous_evaluation_path` is record lineage only.

For an authorized Loop, and for any explicitly multi-file logical package, also provide:

```text
artifact_manifest_reference
manifest_sha256
```

The producer freezes the manifest. The evaluator only consumes it and stops on a manifest, hash, file-relation, or base-version conflict. A single-file non-Loop evaluation needs no manifest when its version is unique.

## Record versions and defects

- Create a new `evaluation_id` when the artifact or standard version changes materially.
- Keep the same `evaluation_id` for new evidence on the same artifact and standard; write a non-overwriting record version.
- Before evaluation or a write, a missing, conflicting, invalid, or non-unique binding returns:

```text
BLOCKED
```

For a standard problem, add `anomaly: STANDARD_CONTRACT_ANOMALY` below the top-level status. The evaluator does not guess or rewrite the standard.

- After a record exists or a write was attempted, a missing or mismatched record binding, omitted field, or overwrite returns:

```text
RECORD_CONTRACT_ANOMALY
```

- Only an actual write outside the unique authorized path adds:

```text
subtype: OUT_OF_SCOPE_WRITE
```

Preserve the record and evidence; do not delete, overwrite, repair, or clean it up. `RECORD_CONTRACT_ANOMALY` is evaluator-only and is not a delegation failure label.

## Evaluator boundary

The evaluator may report evidence, risks, gaps, unknowns, and recommendations. It may not change the standard, task or Loop state, delegated artifact, ownership, repair assignment, merge/release decision, or final acceptance. The primary agent receives, verifies, integrates, and remains accountable.
