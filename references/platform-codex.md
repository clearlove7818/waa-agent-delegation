# Codex Runtime Map

Use this mapping only when the active harness is Codex.

Evidence reviewed: 2026-08-16. Current Codex releases expose subagents by default, but the detailed orchestration behavior below is bound to the collaboration tool contracts exposed by the active session and must be rechecked when those contracts change.

## Before dispatch

1. Confirm that the current Codex surface exposes collaboration or subagent tools. Do not infer availability from documentation alone.
2. Confirm that repository guidance, current user authority, sandboxing, and managed policy allow the delegated work.
3. Select an existing named agent only when authorization is already established and the agent is actually available.
4. Treat model selection, context-fork behavior, worktree use, and concurrency as platform options, not rights granted by the task packet.

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

A final answer ends that executor turn, not the reusable target. A later `followup_task` can continue the same target only while the original target still exists; creating a replacement does not restore the prior target's complete context. Context compaction can summarize older history, so restate any binding decision added after the handshake in the follow-up task and keep protocol-critical state in the message or an authorized artifact instead of assuming unstated history remains verbatim.

Codex transport does not impose the governance protocol's response-body prefixes or status tokens. Those requirements come from the applicable runtime rules and task packet. Do not hard-code a tool JSON schema in the shared protocol: tool names, parameters, and delivery behavior can vary by Codex surface and release.

## Evidence sources

Accessed 2026-08-16:

- <https://developers.openai.com/codex/multi-agent/>
- <https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/multi_agents_spec.rs>
- The collaboration tool contracts exposed in the active Codex session.
- [User-confirmed platform-facts evidence](../evals/evidence/2026-08-16-platform-facts.md), source-report SHA-256 `09e0e116bda5502ca4ec0e10f3964f5f2d9e0bdd205e6ceb81ae062ef93d19c6`.

## Permission behavior

- Subagents do not create new task authority.
- A subagent or the primary agent may still encounter sandbox approval or an unavailable tool.
- Map a missing collaboration feature to `MISSING_CAPABILITY`.
- Map a sandbox or approval denial to `PLATFORM_PERMISSION_BLOCKED`.
- Map an available tool that the task did not authorize to `CAPABILITY_OUT_OF_SCOPE`.

This adapter is not a standalone contract: use [protocol.md](protocol.md) for exact failure-label, mandatory-prefix, and first-line rules, and use this map for Codex-specific behavior.

## Result reception

Read the subagent's returned artifacts and evidence. Re-run proportionate checks from the primary context. Do not treat a completion message, commit, or claimed test result as final acceptance without inspection.
