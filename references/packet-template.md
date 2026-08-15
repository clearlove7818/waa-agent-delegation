# Packet template — dispatch-time rendering

Fill the slots; do not retype the blocks. This file renders the protocol's packet skeleton and return forms so a dispatcher assembles a packet by filling slots instead of transcribing structure. `references/protocol.md` is authoritative: any change to the skeleton, a form, or the defect rule lands in both files in the same change, and reception diffs this file's fenced blocks against the protocol's before accepting either. If the two disagree, the protocol wins and this file is the defect.

Usage:

1. Copy the skeleton and fill every `<...>` slot. Risk sizing may compress detail, but never task identity, task ID, packet version, artifact ownership, or `assembly_type`.
2. Carry input content hashes in full; a truncated hash supports only prefix matching and is labeled as such.
3. State each output path's current state — absent, existing and empty, or existing with content.
4. When a handshake is required, carry the acceptance-record form verbatim from the block below; always carry the completion-return form. The `required_form_defect_rule` line travels in every packet exactly as the skeleton writes it.
5. State the packet's scratch policy: name the one permitted scratch path for temporary files, or prohibit them outright; a packet silent on scratch space makes every helper file a boundary breach.
6. Copy every closed-set token — an `assembly_type` value, a status word, a boundary mode — from its defining source; a retyped token is how a closed set gains a misspelled member.

## Skeleton (byte-identical to the protocol's)

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

## Acceptance-record form (byte-identical to the protocol's)

`ACCEPTED` must be the first status token on the message's first line, with no preamble, no separator, and no markup around it.

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

## Completion-return form (byte-identical to the protocol's)

The first line of the completion message is `ACCEPTED / <DONE | PARTIAL | FAILED>` with no preamble, no separator, and no markup around it; `delivery_status` repeats the value after the slash exactly.

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
