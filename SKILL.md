---
name: waa-agent-delegation
description: Govern an actual agent delegation only after the primary agent has decided to create or invoke a subagent. Use to choose exactly one EXECUTION_SUBAGENT, TASK_SPECIALIST_SUBAGENT, or explicitly authorized NAMED_AGENT; check capability, platform, permission, and external-effect boundaries; build a risk-sized TASK-006 packet; define handshake, failure, delivery, and handoff; and support primary-agent verification. Exclude complexity alone, delegation discussion, simple direct work, multi-agent demonstrations, unauthorized named-agent activation, permission expansion, and responsibility transfer.
---

# Agent Delegation

Govern an already-chosen delegation without taking direction, extra authority, named-agent activation rights, or final responsibility.

<FAILURE-LABEL-CONTRACT>

Before execution, put one exact root-cause label as the first status token on the message's first line:

- `BLOCKED`: critical task input is missing or the contract conflicts.
- `MISSING_CAPABILITY`: a required capability is absent, incompatible, or unreliable.
- `CAPABILITY_OUT_OF_SCOPE`: the capability exists but Rules or current task authorization excludes it.
- `PLATFORM_PERMISSION_BLOCKED`: platform policy, sandboxing, or approval prevents the action.

Preserve these labels verbatim. Record any applicable mandatory reply prefix in the task packet with its exact text, governing source, and applicability to this executor. The executor does not infer a prefix from an external instruction or resident identity document that does not govern it. If a directly applicable higher-priority runtime rule is omitted from or conflicts with the packet, obey that rule and return `BLOCKED` for the packet defect before execution. Put the label immediately after an applicable prefix on the same first line; otherwise the label begins the message. Put no discretionary preamble, progress note, separator, or Markdown markup before or around the label. If a required handshake stops, add `Handshake: BLOCKED` after the root-cause label. Delivery states apply only after execution starts.

</FAILURE-LABEL-CONTRACT>

## Run the delegation loop

1. Confirm real delegation is already chosen and useful for independent work, professional judgment, parallel benefit, or independent verification; otherwise do not dispatch.
2. Choose exactly one `EXECUTION_SUBAGENT`, `TASK_SPECIALIST_SUBAGENT`, or authorized `NAMED_AGENT`. Visibility, availability, recommendation, or fit never authorizes a named Agent.
3. Check capability fitness, platform compatibility, Rules, task authorization, platform permission, prohibitions, exceptions, and external effects.
4. Build one risk-sized TASK-006 packet with `task_packet_version`, `task_id`, `assembly_type`, `artifact_id`, `artifact_version`, and one `owner`; vary only the depth of its nine information classes. Read [references/protocol.md](references/protocol.md).
5. Load only the active map: [Codex](references/platform-codex.md), [Claude Code](references/platform-claude-code.md), or [Agy](references/platform-agy-cli.md). Read [platform compatibility](references/platform-compatibility.md) when certainty matters.
6. Apply the required handshake, dispatch through the current native interface, and preserve the packet boundary.
7. Reconcile identity and ownership, verify returned evidence, and integrate only what it supports.

## Apply executor rules

- `EXECUTION_SUBAGENT`: use for bounded work following clear rules. Low-risk, reversible, unambiguous work with no external effect may skip the handshake; otherwise require `ACCEPTED / BLOCKED`.
- `TASK_SPECIALIST_SUBAGENT`: use for non-mechanical professional judgment. Embed the eight-part temporary `specialist_contract`, always require `ACCEPTED / BLOCKED`, and create no persistent personality or tracking/promotion signal.
- `NAMED_AGENT`: use only after the user selected it, or authorized the primary agent to choose and the choice was recorded. Always require `ACCEPTED / BLOCKED` and confirmation of that authorization basis, even for low-risk work, because the handshake binds the named identity to the current-task authorization.

`ACCEPTED` confirms understanding of the packet version, objective, evidence duty, standard, capability conditions, permissions, prohibitions, and return contract. It proves neither expertise, authority, execution, verification, nor success.

## Preserve identity, ownership, and authority

Every packet has exactly one uppercase `assembly_type` and all six identity fields. The packet, required acceptance record, and result must preserve them; reject mismatches.

`owner` solely owns the current artifact version. The primary agent remains responsible for delegation, reception, verification, coordination, synthesis, user communication, and the integrated outcome without automatically owning each delegated version.

Every action must pass all three gates: Rules allow it, the packet authorizes it, and the platform permits it. Never switch capability or execution paths to bypass a gate.

## Return and evaluate deliberately

After execution begins, start the completion message with `ACCEPTED / <DONE | PARTIAL | FAILED>` under the protocol's first-line rule, then return exactly one matching delivery state:

- `DONE`: the minimum deliverable is complete and evidenced.
- `PARTIAL`: disclose completed and unfinished work, impact, evidence, unknowns, next handoff, and the safest next action.
- `FAILED`: the minimum deliverable was not reached; preserve cause, attempted scope, evidence, residual-state uncertainty, and a safe recovery or diagnostic action when blind retry could cause harm.

Independent evaluation is optional and separate. Connect it only when authorized and useful; never auto-start evaluation or a Loop. Subagent output remains evidence until the primary agent verifies and integrates it.
