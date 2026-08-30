# Codex Runtime Map

Use this mapping only when the active harness is Codex.

Use the active session's collaboration tool contracts; product versions and transport details may change.

## Before dispatch

1. Confirm that the current Codex surface exposes collaboration or subagent tools. Do not infer availability from documentation alone.
2. Confirm that repository guidance, current user authority, sandboxing, and managed policy allow the delegated work.
3. Select an existing named agent only when authorization is already established and the agent is actually available.
4. Treat model selection, context-fork behavior, worktree use, and concurrency as platform options, not rights granted by the task packet.

## Dynamic unnamed-subagent child block

Codex documents a global multi-agent switch and a global `agents.max_depth`, but no child-only deny or per-subagent tool filter. A global switch or depth cap does not prove the required parent/child split; disabling the switch would also remove waa's delegation surface.

For a dynamic unnamed subagent that requires a native hard block, verify a platform-provided child-only control before dispatch. It must cover every native child-delegation or collaboration route exposed to that subagent: create or invoke, define, manage or interrupt, message/send, fork, background, and parallel start, plus any other exposed equivalent route. A Skill, prompt, task packet, or custom-agent file is not that control. If the active Codex surface has no such control, return `MISSING_CAPABILITY`; if the control exists but the platform denies the requested child route, return `PLATFORM_PERMISSION_BLOCKED`. Keep waa's parent multi-agent surface enabled.

## Map semantic actions

| Delegation action | Codex behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Use the current subagent creation interface with one concrete bounded task. |
| `TASK_SPECIALIST_SUBAGENT` | Supply the eight-part task-scoped specialist contract, minimum capabilities, prohibitions, and return contract through the current interface; avoid a durable agent definition. |
| `NAMED_AGENT` | Select the exact configured agent only after current-task authorization; otherwise return `CAPABILITY_OUT_OF_SCOPE`. |
| Required handshake | Use `spawn_agent` for the initial packet. Require `ACCEPTED` or a blocked form as the executor's final answer for that turn, wait until that turn is complete, and inspect the return. After the primary agent approves continuation, use `followup_task` on the same target; it triggers a new turn when the target is idle. If called while the target is still running, it can deliver at message boundaries, so it is not a hard gate. If the surface cannot preserve executor identity and context across the exchange, return `MISSING_CAPABILITY` rather than simulate a gate. |
| Send additional context | Use `send_message` only for mailbox delivery that does not need to start a new turn. It does not trigger execution; use `followup_task` when the executor must continue working. Neither mechanism silently changes the task contract. |
| Wait for results | Use the current wait/status mechanism and retain primary-agent responsibility. A non-final `MESSAGE` is information, not proof that the executor has stopped; the handshake gate requires a completed turn and its `FINAL_ANSWER`. |
| Stop unsafe work | Use `interrupt_agent` when authority, scope, or the core contract is violated. Interruption ends the current turn and leaves the target reusable, but it is not acceptance of the handshake. |

A final answer ends that executor turn, not the reusable target. Continue only the same live target; restate any material binding added after the handshake because compaction may summarize older context.

Codex transport does not impose the governance protocol's response-body prefixes or status tokens. Those requirements come from the applicable runtime rules and task packet. Do not hard-code a tool JSON schema in the shared protocol: tool names, parameters, and delivery behavior can vary by Codex surface and release.

## Permission behavior

- Subagents do not create new task authority.
- A subagent or the primary agent may still encounter sandbox approval or an unavailable tool.
- Map a missing collaboration feature to `MISSING_CAPABILITY`.
- Map a sandbox or approval denial to `PLATFORM_PERMISSION_BLOCKED`.
- Map an available tool that the task did not authorize to `CAPABILITY_OUT_OF_SCOPE`.

This adapter is not a standalone contract: use [protocol.md](protocol.md) for exact failure-label, mandatory-prefix, and first-line rules, and use this map for Codex-specific behavior.

## Result reception

Read the subagent's returned artifacts and evidence. Re-run proportionate checks from the primary context. Do not treat a completion message, commit, or claimed test result as final acceptance without inspection.
