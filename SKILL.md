---
name: waa-agent-delegation
description: Prepare and govern an actual agent delegation after the primary agent has decided to create or invoke a subagent. Use to select an execution subagent, task-specific specialist, or already-authorized named agent; check capabilities, tools, platform compatibility, permissions, and external effects; build a risk-sized task packet; define acceptance, failure, and handoff behavior; and receive results for primary-agent verification. Do not use merely because a task is complex, while only discussing whether to delegate, for simple work better done directly, to demonstrate multi-agent behavior, to activate named agents without explicit authorization, to expand permissions, or to transfer final responsibility.
---

# Agent Delegation

Strengthen an already-chosen delegation without taking ownership of the task direction, permissions, named-agent activation, or final result.

<FAILURE-LABEL-CONTRACT>

Before composing any failure response, select one exact label. After any mandatory higher-priority host or governance prefix, put the label on the first task-status line with no translation, explanation, bullet marker, or formatting change:

```text
BLOCKED
MISSING_CAPABILITY
CAPABILITY_OUT_OF_SCOPE
PLATFORM_PERMISSION_BLOCKED
```

Mandatory mappings:

- Missing task input or conflicting contract → `BLOCKED`
- No usable subagent interface exists → `MISSING_CAPABILITY`
- A browser can submit, but the user authorized read-only work → `CAPABILITY_OUT_OF_SCOPE`
- A required sandbox or approval request was denied → `PLATFORM_PERMISSION_BLOCKED`

Classify by cause, not by the generic fact that work stopped. `BLOCKED` is reserved for missing contract input or conflict. Never use `BLOCKED` when a capability is absent, an available capability is unauthorized, or the platform denied permission.

Before returning, scan the first task-status line after any required host prefix. If it contains any other status wording, including `blocked`, `platform_blocked`, `permission_blocked`, `AUTHORITY_BLOCKED`, or a translated label, rewrite it with the exact contract label. Never violate a higher-priority requirement merely to place the label on the absolute first line.

</FAILURE-LABEL-CONTRACT>

## Run the delegation loop

1. **Confirm value.** Verify that the intended delegation has an independent workstream, specialist need, material parallel benefit, or useful independent verification. If direct execution is more reliable, do not dispatch and return control to the primary agent.
2. **Choose one executor type.** Select an execution subagent, a task-specific specialist subagent, or an already-authorized named agent. Never infer named-agent authorization from availability.
3. **Check feasibility and authority.** Confirm the required capabilities and tools exist, work on the current platform, fit the task, and remain within current permissions. Identify external effects and approval boundaries before dispatch. If a check fails, return the exact failure label defined above rather than a conversational substitute.
4. **Build a risk-sized task packet.** Include the unique outcome, owner, deliverables, minimum context and evidence, scope, permissions, prohibitions, quality checks, return shape, failure behavior, and handoff. Read [references/protocol.md](references/protocol.md) for packet and prompt patterns.
5. **Load only the active platform map.** Read [references/platform-codex.md](references/platform-codex.md), [references/platform-claude-code.md](references/platform-claude-code.md), or [references/platform-agy-cli.md](references/platform-agy-cli.md). Use [references/platform-compatibility.md](references/platform-compatibility.md) when installation, discovery, or platform certainty matters.
6. **Dispatch through the current native interface.** Preserve the task packet's authority boundary. Require `ACCEPTED / BLOCKED` before execution only when ambiguity, risk, cost, or external effects justify the handshake.
7. **Receive and verify.** Check the returned evidence, changes, tests, limitations, and failures against the packet. Reconcile conflicts and perform proportionate verification before using the result.
8. **Retain responsibility.** The primary agent owns synthesis, user communication, final verification, and the outcome. A subagent result is evidence, not acceptance.

## Choose the executor

- **Execution subagent:** Use for a bounded task that needs ordinary execution capacity and clear instructions.
- **Task-specific specialist subagent:** Use when the task requires a temporary specialist contract, uncommon expertise, or a deliberately restricted tool set. Define only what this task needs; do not create a persistent persona by default.
- **Named agent:** Use only when the user directly selected it, or the user explicitly authorized the primary agent to choose and the primary agent then made that choice. Availability, prior use, or a matching description is not authorization.

## Preserve permission boundaries

- Treat capability discovery, compatibility, and authorization as separate checks.
- Do not ask a subagent to perform an action the primary agent could not perform under the same task authority.
- Do not use delegation to bypass sandboxing, approval prompts, managed policy, or external-impact restrictions.
- Stop or return a defined failure when the contract is missing a material input or the platform cannot enforce the boundary.

## Return one exact failure label

When execution cannot proceed, make the first task-status line after any mandatory host prefix exactly one of these uppercase labels, verbatim. Do not translate, lowercase, abbreviate, or invent aliases such as `AUTHORITY_BLOCKED`, `platform_blocked`, or `permission_blocked`.

- `BLOCKED`: The task contract lacks a critical input or contains an unresolved conflict.
- `MISSING_CAPABILITY`: A required capability is absent, incompatible, or not reliably usable.
- `CAPABILITY_OUT_OF_SCOPE`: The capability exists but lies outside current rules or authorization.
- `PLATFORM_PERMISSION_BLOCKED`: Platform policy, sandboxing, or approval state prevents execution.

Do not invent extra status taxonomies unless the delegated task itself already requires them.

## Connect evaluation deliberately

Request independent evaluation only when it will materially improve confidence and the task authority permits it. Keep the evaluator independent from the executor's hidden context. Do not automatically start an evaluator, review chain, or quality loop.
