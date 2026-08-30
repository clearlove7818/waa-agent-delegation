# Delegation Protocol

Use this reference to construct a self-contained, risk-sized TASK-006 packet. Do not force every task into a large fixed form, but never omit the packet identity fields.

## TASK-006 nine information classes

Every packet locates these nine classes. Risk trimming may compress detail, but never removes the six identity fields or `assembly_type`.

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

`owner` is the sole owner of the current artifact version; primary-agent synthesis and final responsibility do not change it.

### 2. Core problem and objective

State why delegation is useful, the objective, and one inspectable outcome. The executor does not redefine direction or standard.

### 3. Task items and deliverables

List bounded work, deliverables, expected shape, exclusions, and the owner. State output-path state when it matters.

### 4. Minimum context

List only the context the executor needs. State one `input_boundary`: `LIST_ONLY` forbids unlisted reads; `LIST_IS_START_DISCLOSE_BEYOND` permits bounded additional reads that are disclosed in the return. An omitted boundary is a packet defect. A packet may tighten, never relax, governing Rules, authorization, or resident boundaries.

### 5. Authoritative material and evidence

List trusted sources, standards, evidence requirements, applicability, conflicts, and unknowns. Research requires current-task authorization and a justified gap.

### 6. Scope and permissions

State scope, permissions, external effects, writable targets, and approvals. `forbidden_actions` always includes no nested Agent/subagent/background/parallel dispatch, no ownership transfer, and no credential placement. Declare exact `version_control_boundary` and `release_deploy_boundary`; omission is a packet defect. Every action must pass Rules, current-task authorization, and platform permission.

### 7. Capability constraints

State required and forbidden capabilities, compatibility, exceptions, and minimum tools or Skills. Visibility never grants authorization; capability changes require a separate task.

### 8. Acceptance and verification

State quality, evidence, verification, and unknown handling. `DONE`, `PARTIAL`, and `FAILED` are delivery states, not quality substitutes.

### 9. Return and exception protocol

State the output, failure, handoff, binding fields, and handshake rule. Record any mandatory prefix with its source. Carry or list every required return form; a missing form is a packet defect, not an invitation to invent one. Carry the `required_form_defect_rule` from the skeleton verbatim.

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
  completion_return_form: <carried verbatim in this packet, or this protocol listed among the executor's inputs>
  acceptance_record_form: <carried verbatim in this packet, or this protocol listed among the executor's inputs; not applicable only when this packet permits the handshake to be omitted>
  required_form_defect_rule: A form this packet requires but neither carries nor lists among your readable inputs is a packet defect. Discovered before execution: return `BLOCKED` naming it, and do not start. Discovered only after execution has begun: do not claim `BLOCKED` retroactively; disclose the defect and return `PARTIAL`. If you compose anything in place of a form you were not given, label it as composed and name what it was derived from.
```

## Executor-specific contract

### `EXECUTION_SUBAGENT`

Use for bounded work with clear rules. Keep the identity fields; a low-risk, reversible, unambiguous task with no external effect may omit the handshake.

An execution subagent may not dispatch another Agent, subagent, background task, or parallel executor, or transfer artifact ownership. An omitted floor makes the packet incomplete.

### `TASK_SPECIALIST_SUBAGENT`

Use only for non-mechanical professional judgment. Embed this temporary contract; do not create a persistent identity:

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

`TASK_SPECIALIST_SUBAGENT` always returns `ACCEPTED` or `BLOCKED` before execution. `ACCEPTED` confirms the contract and packet version, not expertise or success.

### `NAMED_AGENT`

Use only after current-task authorization and selection. Reference the existing Agent contract; do not create or modify a personality here. Include:

```text
authorization_basis: <specific current-task authorization>
named_agent: <exact identifier>
permission_reminder: <naming grants no new authority>
forbidden_delegation: <no dispatch of another Agent, subagent, background task, or parallel executor within this task; no transfer of artifact ownership>
```

`NAMED_AGENT` always returns `ACCEPTED` or `BLOCKED` before execution and confirms the authorization basis. Availability, fit, and visibility are not authorization. A named Agent may not dispatch another Agent within this task; expansion requires a new packet and primary-agent decision.

## Execution protocol

The loop is: select one executor after the primary decision → check capability, compatibility, authority, permission, and effects → build the packet → execute → receive, verify, and integrate. Optional evaluation is a separate authorized branch. The primary agent owns coordination, verification, synthesis, and final communication; `owner` remains the packet's artifact-version owner.

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

`ACCEPTED` is the first status token on the first line, subject only to an applicable mandatory prefix.

Blocked form preserves both handshake disposition and root cause. The exact root-cause label must be the first status token on the message's first line:

```text
<BLOCKED | MISSING_CAPABILITY | CAPABILITY_OUT_OF_SCOPE | PLATFORM_PERMISSION_BLOCKED>
Handshake: BLOCKED
Reason: <missing input, contract conflict, capability gap, scope limit, or platform barrier>
Impact: <reliability effect and safe completed portion>
Needed: <minimum information, evidence, authority, capability, or platform change>
Handoff: <primary agent or specified recipient>
```

The blocked form uses the same first-line rule as failure returns. `ACCEPTED` proves understanding of the packet version only; material ambiguity or boundary change requires `BLOCKED` and a new packet.

## Combined single-turn return

Use this form only for an `EXECUTION_SUBAGENT` packet that explicitly permits the handshake to be omitted because the work is low-risk, reversible, unambiguous, and has no external effect. It does not replace a required handshake for a higher-risk execution subagent, a `TASK_SPECIALIST_SUBAGENT`, or a `NAMED_AGENT`.

The first status token is:

```text
ACCEPTED / <DONE | PARTIAL | FAILED>
```

Use the same first-line rule. The combined form is only for an explicitly handshake-free low-risk `EXECUTION_SUBAGENT`; otherwise use the handshake or an exact failure label.

## Completion return

The first status token on the completion message's first line is:

```text
ACCEPTED / <DONE | PARTIAL | FAILED>
```

Use the same first-line rule. In a two-stage flow, `ACCEPTED` reaffirms the binding; `delivery_status` must match the value after the slash.

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
Safest next action: <for PARTIAL, the continuation that will not compound the partial state; for FAILED, a recovery or diagnostic action when residual state or blind retry could cause harm; otherwise not applicable>
Requested-form substitution: <none, or the requested form not produced; why producing it would have been false; the in-scope substitute actually delivered>
```

Use `DONE` only when the minimum deliverable is complete and evidenced. `PARTIAL` discloses completed and unfinished work, impact, evidence, unknowns, handoff, and a safe next action. `FAILED` discloses cause, attempted scope, evidence, and residual-state uncertainty; add recovery or diagnostics when needed. Delivery states do not replace pre-execution failure labels. A false requested form is `PARTIAL` only after execution begins and only when the substitute stays within the packet boundary; otherwise return `BLOCKED` or do not produce it.

## Failure returns

Choose one exact uppercase root-cause label and put it as the first status token on the message's first line. Any applicable mandatory reply prefix must be recorded in the task packet with its exact text, governing source, and applicability to this executor. The executor does not infer a prefix from an external instruction or resident identity document that does not govern it. If a directly applicable higher-priority runtime rule is omitted from or conflicts with the packet, obey that rule and return `BLOCKED` for the packet defect before execution. Put the label immediately after an applicable prefix on the same line; otherwise the label begins the message. Put no discretionary preamble, progress note, separator, or Markdown markup before or around it. Do not translate, shorten, or invent aliases:

| Root cause | Exact label |
| --- | --- |
| Missing critical task input or conflicting contract | `BLOCKED` |
| Required capability absent, incompatible, or unreliable | `MISSING_CAPABILITY` |
| Capability available but outside Rules or current task authorization | `CAPABILITY_OUT_OF_SCOPE` |
| Platform policy, sandbox, or approval state prevents execution | `PLATFORM_PERMISSION_BLOCKED` |

Do not collapse the last three conditions into generic `BLOCKED`, and do not add new failure states.

`RECORD_CONTRACT_ANOMALY` is not a fifth root-cause label and does not belong in the table above. It is an evaluation-record status that reports a broken record contract rather than a cause of failed execution, and it is available only to an authorized evaluator after a record exists or a write has been attempted. It occupies the same first-line position under the same mandatory-prefix and purity rules.

## Optional evaluation handoff

Evaluation is a separate, authorized branch. Read [evaluation.md](evaluation.md) only when it is requested; it never starts automatically or transfers artifact ownership.

## Primary-agent reception

Before integrating a result:

1. Match all six identity fields and reject mismatched task, packet, artifact, or owner versions.
2. Confirm that the executor's `assembly_type` is one exact uppercase value and matches the packet.
3. Confirm the `TASK_SPECIALIST_SUBAGENT` contract is present and all eight sections are locatable when applicable.
4. Inspect deliverables, cited artifacts, commands, outputs, and sources.
5. Confirm the executor stayed within scope, permissions, capability constraints, and ownership.
6. Check that the first-line `ACCEPTED / <status>` value matches `delivery_status`, and that `DONE`, `PARTIAL`, or `FAILED` is truthful and complete for the evidence. When the delivered artifact uses a form other than the requested form, require `PARTIAL` and confirm that `Requested-form substitution` names the unproduced form, why producing it would have been false, and the in-scope substitute delivered; reject `DONE` claimed on a substituted form. Confirm the substitution did not widen artifact shape, scope, permissions, ownership, or the return contract; otherwise reject integration and require a new packet. When `delivery_status` is `PARTIAL`, confirm `Safest next action` names a continuation rather than `not applicable`, and that it is not merely a restatement of the handoff recipient. When `delivery_status` is `FAILED`, reject `not applicable` if residual state is possible or blind retry could cause harm; require a recovery or diagnostic action instead. Do not treat the completion line as proof that a required pre-execution gate occurred.
7. Confirm every `Taken on faith` item is reconciled as verified, still unverified, or found false; preserve unreconciled items as result limitations.
8. Check `Outside-list reads` against `input_boundary`. Reject any unlisted read under `LIST_ONLY`; under `LIST_IS_START_DISCLOSE_BEYOND`, confirm every disclosed source stayed inside all independent scope, authorization, permission, and platform boundaries.
9. Reproduce or independently verify checks in proportion to risk.
10. Record limitations, unknowns, residual risk, and any requested next action.
11. Integrate under primary-agent responsibility without silently changing artifact ownership.
12. Read the required conflict-report field. When it is not `none`, confirm that both conflicting texts and their sources are identified, record the conflict as a governance defect, and do not resolve it inside the delegated task.
