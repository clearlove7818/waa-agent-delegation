# Delegation Protocol

Use this reference to construct a self-contained, risk-sized TASK-006 packet. Do not force every task into a large fixed form, but never omit the packet identity fields.

## Contents

- [TASK-006 nine information classes](#task-006-nine-information-classes)
- [Packet skeleton](#packet-skeleton)
- [Executor-specific contract](#executor-specific-contract)
- [Execution protocol](#execution-protocol)
- [Acceptance handshake](#acceptance-handshake)
- [Combined single-turn return](#combined-single-turn-return)
- [Completion return](#completion-return)
- [Failure returns](#failure-returns)
- [Optional evaluation handoff](#optional-evaluation-handoff)
- [Primary-agent reception](#primary-agent-reception)

## TASK-006 nine information classes

Every delegated packet has exactly one `assembly_type` and must make all nine classes locatable. A low-risk packet may compress several classes into short sentences, but risk trimming never removes task identity, task ID, packet version, artifact ownership, or `assembly_type`.

### 1. Task identity and artifact ownership

Record the task and the one artifact version being produced:

```text
task_packet_version: <stable packet version>
task_id: <unique task identifier>
assembly_type: EXECUTION_SUBAGENT | TASK_SPECIALIST_SUBAGENT | NAMED_AGENT
artifact_id: <unique deliverable identifier>
artifact_version: <target artifact version>
owner: <sole owner of this artifact version>
```

`owner` is not a generic task coordinator. It is the sole owner of the current artifact version. The primary agent's synthesis, reception, and final responsibility do not silently change this field. A task packet, acceptance record, or result with a mismatched identity or owner is not a normal delivery for that version.

### 2. Core problem and objective

State why delegation is valuable, the core problem, the objective, and the one inspectable outcome. Do not let the executor redefine the direction or standard.

### 3. Task items and deliverables

List the bounded task items, concrete deliverables, expected artifact shape, and exclusions. Keep one outcome owner even when several files or observations are returned.

### 4. Minimum context

Provide only the context needed to act without reconstructing the primary conversation: workspace, relevant files, decisions already frozen, dependencies, and local facts. List every input source that defines the executor's reading surface rather than relying on an implied workspace-wide context.

State exactly one `input_boundary`. `LIST_ONLY` means the listed inputs are the whole permitted reading surface; reading anything else requires a new packet. `LIST_IS_START_DISCLOSE_BEYOND` means the executor may read additional material only when it remains inside every independent scope, authorization, permission, and platform boundary, and must disclose each additional source in the completion return. Leaving `input_boundary` unstated is a packet defect, not a default; return `BLOCKED` before execution rather than infer a value from an executor definition or available filesystem surface.

When an applicable resident executor definition or governing document is available, state any difference in scope, permissions, evidence duty, or return contract. A packet may add stricter task-specific limits, but it may not relax Rules, current-task authorization, governing documents, or a resident non-negotiable boundary. An apparent relaxation is a contract conflict; silent divergence is a defect even when the remaining packet is otherwise correct.

### 5. Authoritative material and evidence

List trusted sources, standards, project facts, evidence requirements, source dates and applicability, known conflicts, and unknowns. External research is allowed only when the current task authorizes it and the knowledge gap, freshness, risk, or verification need justifies it.

### 6. Scope and permissions

State the allowed scope, `permission_boundary`, `forbidden_actions`, `external_effects`, writable targets, approval boundaries, and the fact that every action must pass Rules, current task authorization, and platform permission.

`forbidden_actions` always states, at minimum, that the executor may not dispatch another Agent, subagent, background task, or parallel executor within this task and may not transfer artifact ownership. The floor also requires an explicit version-control boundary (`version_control_boundary`) and release/deploy boundary (`release_deploy_boundary`). `version_control_boundary` states whether stage, commit, merge, push, tag, rebase, reset, content-overwriting checkout, and force push are permitted, naming each permitted action and its exact repository, path, branch, or ref targets. `release_deploy_boundary` states whether release or deploy is permitted and names each permitted environment or target. These declarations record authority already supplied by Rules and the current task; they never create it. Leaving either declaration unstated is a packet defect, not a default; return `BLOCKED` before execution rather than assume permission or prohibition. The packet must also state, without a packet-level exception, that the executor may not place a credential, token, key, or password in a file, reply, log, or version control. Add task-specific prohibitions on top of this floor rather than in place of it. A packet that omits the floor is incomplete even if every task-specific prohibition is present. Any separately authorized expansion requires a new packet and a primary-agent decision; it cannot be inferred from the current packet.

### 7. Capability constraints

State `required_capabilities`, `forbidden_capabilities`, compatibility status, permitted exceptions, and the minimum tools or Skills. Capability visibility never grants authorization, and the executor may not obtain, install, create, fork, upgrade, replace, or delete a capability without a separately authorized task.

### 8. Acceptance and verification

State quality standards, acceptance conditions, evidence to return, verification commands or observations, and how unknowns and residual risk must be disclosed. `DONE`, `PARTIAL`, and `FAILED` are delivery states, not quality substitutes.

### 9. Return and exception protocol

State `output_contract`, `failure_return`, handoff recipient, required binding fields in the return, and the applicable `ACCEPTED / BLOCKED` rule. Record `mandatory_reply_prefix: none` unless a directly applicable higher-priority rule governs this executor; when one does, quote the exact prefix and record its governing source and executor applicability under `mandatory_reply_prefix_source`. A packet omission or conflict cannot cancel a directly applicable higher-priority runtime rule; obey the rule and return `BLOCKED` for the packet defect before execution. Keep execution handshake, primary-agent reception, and final synthesis as execution protocol below rather than treating them as a tenth or eleventh packet class.

## Packet skeleton

Use this compact shape for every packet, expanding the nine classes according to risk:

```text
task_packet_version: <version>
task_id: <id>
assembly_type: EXECUTION_SUBAGENT | TASK_SPECIALIST_SUBAGENT | NAMED_AGENT
artifact_id: <id>
artifact_version: <version>
owner: <sole owner>

Purpose and objective: <why delegation is useful and one outcome>
Task items and deliverables: <bounded work and concrete outputs>
Minimum context: <listed trusted task-local inputs and context>
  input_boundary: LIST_ONLY | LIST_IS_START_DISCLOSE_BEYOND
Authoritative material and evidence: <sources, standards, evidence requirements>
Scope and permissions: <allowed actions, prohibitions, external effects>
  forbidden_actions: <universal floor plus task-specific prohibitions>
  version_control_boundary: <permitted actions and exact repository, path, branch, or ref targets; or none>
  release_deploy_boundary: <permitted release/deploy actions and exact environments or targets; or none>
Capability constraints: <required, forbidden, compatibility, exceptions>
Acceptance and verification: <quality and checks>
Return and exception protocol: <output, failure, handoff, handshake>
  mandatory_reply_prefix: <none or exact text>
  mandatory_reply_prefix_source: <not applicable or governing source and executor applicability>
```

## Executor-specific contract

### `EXECUTION_SUBAGENT`

Use for bounded work that can follow clear steps or rules. It never receives a persistent personality contract. Even a low-risk packet keeps all six identity fields above; only the detail of the nine classes may be compressed. Require a handshake when ambiguity, writing, external impact, meaningful cost, unclear permission, or high failure cost exists. Low-risk, reversible, unambiguous work with no external effect may proceed without one.

Regardless of risk level, an execution subagent may not dispatch another Agent, subagent, background task, or parallel executor within this task and may not transfer artifact ownership. These prohibitions apply even when the packet omits them or the platform appears to permit the action; an omitted floor makes the packet incomplete rather than granting authority.

### `TASK_SPECIALIST_SUBAGENT`

Use only when the task requires non-mechanical professional judgment. Embed this temporary, task-scoped contract under `specialist_contract`; do not create a named Agent or persistent identity:

```text
specialist_contract:
  1_role_purpose:
    - why this professional perspective is needed now
    - which task objective it serves
    - why a job title alone is insufficient
  2_artifact_ownership:
    - the sole artifact ID and version owned in this task
    - expiry at task completion or explicit handoff
    - no cross-task responsibility or lasting personality
  3_required_professional_judgments:
    - non-mechanical judgments that must be made
    - basis for each judgment
    - decisions outside this specialist's authority
  4_required_inputs_and_reliable_basis:
    - authoritative task material, project facts, and professional sources
    - applicability, dates, conflicts, and unknowns
    - available Skills, tools, and real capability conditions
    - authorized external research only when a justified gap exists
  5_output_contract:
    - artifact shape and conclusions
    - evidence, assumptions, unknowns, and risks
    - verification method and completion declaration
  6_decision_authority_and_forbidden_boundary:
    - judgment only at the intersection of frozen goal, standard, Rules, task authorization, and platform permission
    - no standard changes, permission expansion, direction changes, or self-approval
  7_collaboration_handoff:
    - inputs, outputs, objections, and dependencies route through the primary agent
    - no direct request to the user for new authority
    - no dispatch of another Agent and no transfer of artifact ownership
  8_failure_return:
    - completed portion, concrete gap, evidence, impact, and required condition
    - only paths actually checked may be recorded as ruled out
    - never use role-play to fill a capability or evidence gap
```

`TASK_SPECIALIST_SUBAGENT` always returns `ACCEPTED` or `BLOCKED` before execution, regardless of task size. `ACCEPTED` confirms the eight sections and the packet version; it does not prove expertise or success.

Do not record invocation counts, recurring-pattern reminders, automatic persistence, or promotion signals. Any cross-task capability or Agent change requires a separately authorized task.

### `NAMED_AGENT`

Use only after the user directly selected the named Agent, or explicitly authorized the primary agent to choose and the primary agent recorded the choice. Reference the existing authorized Agent contract; do not create or modify a personality in this Skill. Include:

```text
authorization_basis: <specific current-task authorization>
named_agent: <exact identifier>
permission_reminder: <naming grants no new authority>
forbidden_delegation: <no dispatch of another Agent, subagent, background task, or parallel executor within this task; no transfer of artifact ownership>
```

`NAMED_AGENT` always returns `ACCEPTED` or `BLOCKED` before execution and must confirm the concrete authorization basis. Availability, domain fit, visibility, or recommendation is not authorization. A named Agent may not dispatch another Agent, including another instance of itself, within this task; this prohibition holds even when the packet omits it or the platform appears to permit it. Any separately authorized expansion requires a new packet and a primary-agent decision.

## Execution protocol

The stable loop is: decide whether delegation has value → select one exact executor type → check capability, tool, compatibility, Rules, task authorization, platform permission, and external effects → construct the nine-class packet → execute independently → optionally evaluate when explicitly useful and authorized → receive, reconcile, verify, and integrate under primary-agent responsibility.

The primary agent owns the decision to delegate, reception, verification, coordination, synthesis, and user communication. It does not automatically own every delegated artifact version; `owner` remains the packet's explicit single owner.

## Acceptance handshake

Apply the executor-specific rule:

- `EXECUTION_SUBAGENT`: optional only for low-risk, reversible, unambiguous work with no external effect; otherwise require it.
- `TASK_SPECIALIST_SUBAGENT`: always require it before execution.
- `NAMED_AGENT`: always require it before execution and include the authorization basis. This requirement binds the named identity to current-task authorization and does not scale down merely because the work is low risk.

Accepted form:

```text
ACCEPTED
Binding: task_packet_version=<...>; task_id=<...>; assembly_type=<...>; artifact_id=<...>; artifact_version=<...>; owner=<...>
Objective as understood: <restate the one outcome in your own words; do not copy the packet wording>
Excluded: <what you understand to be outside scope>
Contract as understood: inputs=<...>; input_boundary=<...>; evidence_and_standard=<...>; capability_and_permission_boundary=<...>; version_control_boundary=<...>; release_deploy_boundary=<...>; forbidden_boundary=<...>; return_contract=<...>
First actions: <the first two or three concrete actions you will take>
Taken on faith: <at most five packet-asserted facts you will act on without verifying>
Filled in: <non-material execution details you resolved and how; "none" only if genuinely none>
Authorization: <required for NAMED_AGENT; otherwise not applicable>
Pending platform approval: <none or specific approval>
```

`ACCEPTED` must be the first status token on the message's first line. Apply the same mandatory-prefix exception and the same prohibition on discretionary preambles, separators, and Markdown markup as the blocked form below.

Blocked form preserves both handshake disposition and root cause. The exact root-cause label must be the first status token on the message's first line:

```text
<BLOCKED | MISSING_CAPABILITY | CAPABILITY_OUT_OF_SCOPE | PLATFORM_PERMISSION_BLOCKED>
Handshake: BLOCKED
Reason: <missing input, contract conflict, capability gap, scope limit, or platform barrier>
Impact: <reliability effect and safe completed portion>
Needed: <minimum information, evidence, authority, capability, or platform change>
Handoff: <primary agent or specified recipient>
```

Apply the same mandatory-prefix rule and the same first-line purity rule as the failure contract below.

An `ACCEPTED` record proves understanding of the specified packet version only. It does not prove packet-asserted facts, capability, authorization, execution, verification, or delivery quality. `Taken on faith` exposes assertions that remain unverified; it never waives the evidence duty or converts an assertion into fact. `Filled in` is limited to non-material execution details. If an ambiguity can change the goal, scope, owner, standard, evidence duty, permission, forbidden boundary, capability condition, external effect, or return contract, return `BLOCKED` rather than resolving it silently. A changed goal, standard, permission, owner, or other material boundary invalidates the old acceptance and requires a new packet version and handshake.

## Combined single-turn return

Use this form only for an `EXECUTION_SUBAGENT` packet that explicitly permits the handshake to be omitted because the work is low-risk, reversible, unambiguous, and has no external effect. It does not replace a required handshake for a higher-risk execution subagent, a `TASK_SPECIALIST_SUBAGENT`, or a `NAMED_AGENT`.

The first status token is:

```text
ACCEPTED / <DONE | PARTIAL | FAILED>
```

Apply the same first-line purity rule as the failure contract. `ACCEPTED` records understanding of the packet version with the same limits as the handshake record; the value after the slash is the delivery state defined below. Then return the six identity fields, `Taken on faith`, `Filled in`, and every completion-return field. If the packet is insufficient or the work encounters a pre-execution failure, use the exact root-cause label instead and do not use the combined form.

## Completion return

The first status token on the completion message's first line is:

```text
ACCEPTED / <DONE | PARTIAL | FAILED>
```

Apply the same first-line purity and mandatory-prefix rule as the failure contract. In a two-stage flow, `ACCEPTED` reaffirms the packet binding accepted before execution; it is not a second handshake and does not retroactively replace a required gate. `delivery_status` repeats the value after the slash and must match it exactly.

Return compact evidence, echoing the six identity fields for every task:

```text
task_packet_version:
task_id:
assembly_type:
artifact_id:
artifact_version:
owner:
delivery_status: DONE | PARTIAL | FAILED
Outcome:
Deliverables or changes:
Evidence:
Verification performed:
Faith reconciled: <for every Taken on faith item, state verified, still unverified, or found false; use none if there were no items>
Outside-list reads: <none, or every source read beyond the packet's listed inputs under LIST_IS_START_DISCLOSE_BEYOND and why it was needed>
Definition conflict: <none, or quote the conflicting resident-definition text and governing-protocol text with their sources; do not resolve the conflict>
Concerns or unknowns:
Handoff to primary agent:
```

Use `DONE` only when the agreed minimum deliverable is complete and evidence supports it. Use `PARTIAL` only when completed items, unfinished items, impact, evidence, unknowns, and the next handoff are explicit. Use `FAILED` when the minimum deliverable was not reached, preserving cause, attempted scope, and evidence. These are post-execution delivery states and never replace a pre-execution failure label. An item taken on faith and never reconciled remains an unverified premise in the delivered result, not a closed question.

## Failure returns

Choose one exact uppercase root-cause label and put it as the first status token on the message's first line. Any applicable mandatory reply prefix must be recorded in the task packet with its exact text, governing source, and applicability to this executor. The executor does not infer a prefix from an external instruction or resident identity document that does not govern it. If a directly applicable higher-priority runtime rule is omitted from or conflicts with the packet, obey that rule and return `BLOCKED` for the packet defect before execution. Put the label immediately after an applicable prefix on the same line; otherwise the label begins the message. Put no discretionary preamble, progress note, separator, or Markdown markup before or around it. Do not translate, shorten, or invent aliases:

| Root cause | Exact label |
| --- | --- |
| Missing critical task input or conflicting contract | `BLOCKED` |
| Required capability absent, incompatible, or unreliable | `MISSING_CAPABILITY` |
| Capability available but outside Rules or current task authorization | `CAPABILITY_OUT_OF_SCOPE` |
| Platform policy, sandbox, or approval state prevents execution | `PLATFORM_PERMISSION_BLOCKED` |

Do not collapse the last three conditions into generic `BLOCKED`, and do not add new failure states.

## Optional evaluation handoff

Independent evaluation is a separate, optional connection point. Use it only after evaluation is independently authorized and useful. Never infer authorization from risk, a low score, keywords, an evaluation file, or evaluator availability; never auto-select Fei or auto-start a Loop.

### Separate participation mode from output mode

Bind one participation mode and one compatible output mode:

```text
evaluation_mode: INDEPENDENT_EVALUATION | EVALUATOR_OPTIMIZER_LOOP
evaluation_output_mode: CONVERSATION_ONLY | FILE_BACKED
```

- A general `INDEPENDENT_EVALUATION` may use either output mode.
- `CONVERSATION_ONLY` must omit `evaluation_output_path` and grants no file-writing authority.
- `FILE_BACKED` must name one unique `evaluation_output_path`; the evaluator may write only that evaluation record and legitimate non-overwriting new versions.
- A formal evaluation by the authorized named Agent Fei must use `FILE_BACKED`.
- `EVALUATOR_OPTIMIZER_LOOP` must use `FILE_BACKED` and requires separate explicit user authorization for the current task.
- Do not silently coerce an invalid mode or path combination. Return `BLOCKED` when the contract conflicts.

### Bind the evaluation relationship

Provide at least:

```text
evaluation_id
evaluation_mode
evaluation_output_mode
evaluation_output_path: <required only for FILE_BACKED; forbidden for CONVERSATION_ONLY>
task_id
artifact_id
artifact_version
standard_id
standard_version
evidence_references
evaluation_scope
```

Also state the evaluation objective, exclusions, independence requirements, capability conditions, allowed reads, permitted tools, and external-access boundary. These fields define the evaluation relationship; they do not replace or modify the original delegation packet's six identity fields. Evaluation does not transfer ownership of the delegated artifact version.

### Add Loop comparison fields only when authorized

For an explicitly authorized `EVALUATOR_OPTIMIZER_LOOP`, also provide:

```text
run_id
segment_id
round
comparison_artifact_version
change_evidence_references
previous_evaluation_path: <only when a previous evaluation record exists>
```

Keep the semantics distinct:

- `artifact_version` is the current candidate being evaluated.
- `comparison_artifact_version` is the artifact baseline for this round.
- `change_evidence_references` is the evidence that binds the current candidate to that baseline.
- `previous_evaluation_path` is evaluation-record lineage, never the artifact comparison baseline.

Do not substitute `previous_evaluation_path` for `comparison_artifact_version` or omit the change evidence.

### Hand off a frozen artifact manifest when required

Add both fields for every authorized Loop and whenever the task explicitly uses a multi-file logical artifact package:

```text
artifact_manifest_reference
manifest_sha256
```

The producer creates and freezes the manifest after producing the artifact version. The evaluator only consumes and checks it; the evaluator must not generate, modify, or repair the manifest. Stop evaluation when the manifest, hash, base-version relation, or file relation conflicts. Files marked unchanged remain part of the current logical artifact version through the frozen manifest and base-version relation. A non-Loop, single-file independent evaluation needs no manifest when the artifact version is otherwise uniquely identifiable.

### Version evaluation records without overwriting

- Create a new `evaluation_id` when the artifact version or standard version changes materially.
- Under the same artifact version and standard version, keep the same `evaluation_id`; new evidence, an objection, or a factual correction may create a non-overwriting evaluation record `v2`, `v3`, and so on.
- Never overwrite an earlier evaluation file.
- Keep evaluation-file version distinct from artifact version.

### Separate pre-evaluation defects from record anomalies

Before evaluation begins, return this status when a missing, conflicting, invalid, or non-unique object, standard, scope, mode, version, evidence, comparison, artifact-package, or output-path relationship can change the evaluation:

```text
status: BLOCKED
```

For a standard-contract problem, keep `BLOCKED` as the top-level status and add the anomaly field:

```text
status: BLOCKED
anomaly: STANDARD_CONTRACT_ANOMALY
```

`STANDARD_CONTRACT_ANOMALY` is never a top-level status. The evaluator must not guess, select, modify, or rewrite the standard. Return the defect and its evidence to the primary agent. A conflicting path contract before any write is attempted remains a pre-evaluation `BLOCKED`; do not claim `OUT_OF_SCOPE_WRITE` when no out-of-scope write occurred.

After an evaluation record exists or a write has been attempted, return this status when the record has a missing or mismatched task, artifact, artifact version, standard, standard version, manifest, artifact-package, or output-path binding; overwrites an earlier evaluation version; or omits required record fields:

```text
status: RECORD_CONTRACT_ANOMALY
```

`RECORD_CONTRACT_ANOMALY` is not an alias for pre-evaluation `BLOCKED`. Stop normal evaluation and automatic flow, preserve the record, path, and actual evidence, and return the anomaly to the primary agent. The evaluator must not overwrite, delete, clean up, supplement, or repair the anomalous record. Do not add `OUT_OF_SCOPE_WRITE` for an ordinary binding, version, manifest, record-completeness, or overwrite defect.

Only after a write actually occurs outside the task's unique authorized `evaluation_output_path` may the evaluator return:

```text
status: RECORD_CONTRACT_ANOMALY
subtype: OUT_OF_SCOPE_WRITE
```

Stop normal flow and preserve the out-of-scope file and evidence. Do not delete, overwrite, move, or repair the file. The primary agent determines impact and follow-up. A path configuration conflict without an actual write never uses this subtype.

### Keep evaluation advice separate from decisions and repairs

The evaluator may report risks, evidence, gaps, impact, unknowns, and disposition recommendations. It may recommend that the primary agent consider rework, more evidence, or risk acceptance. It must not accept, waive, close, or declare a risk resolved on the primary agent's behalf; decide merge, release, deployment, or final acceptance; assign final repair responsibility; or modify the evaluated artifact to implement a repair.

The prohibition on modifying the artifact and the prohibition on accepting risk are independent constraints. Risk acceptance, risk waiver, risk closure, repair assignment, and final artifact acceptance remain with the primary agent. The evaluator may not guess or rewrite the standard, change task or Loop state, or accept the integrated result. The primary agent receives, verifies, integrates, and remains responsible for the final outcome.

## Primary-agent reception

Before integrating a result:

1. Match all six identity fields and reject mismatched task, packet, artifact, or owner versions.
2. Confirm that the executor's `assembly_type` is one exact uppercase value and matches the packet.
3. Confirm the `TASK_SPECIALIST_SUBAGENT` contract is present and all eight sections are locatable when applicable.
4. Inspect deliverables, cited artifacts, commands, outputs, and sources.
5. Confirm the executor stayed within scope, permissions, capability constraints, and ownership.
6. Check that the first-line `ACCEPTED / <status>` value matches `delivery_status`, and that `DONE`, `PARTIAL`, or `FAILED` is truthful and complete for the evidence. Do not treat the completion line as proof that a required pre-execution gate occurred.
7. Confirm every `Taken on faith` item is reconciled as verified, still unverified, or found false; preserve unreconciled items as result limitations.
8. Check `Outside-list reads` against `input_boundary`. Reject any unlisted read under `LIST_ONLY`; under `LIST_IS_START_DISCLOSE_BEYOND`, confirm every disclosed source stayed inside all independent scope, authorization, permission, and platform boundaries.
9. Reproduce or independently verify checks in proportion to risk.
10. Record limitations, unknowns, residual risk, and any requested next action.
11. Integrate under primary-agent responsibility without silently changing artifact ownership.
12. Read the required conflict-report field. When it is not `none`, confirm that both conflicting texts and their sources are identified, record the conflict as a governance defect, and do not resolve it inside the delegated task.
