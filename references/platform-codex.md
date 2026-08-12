# Codex Runtime Map

Use this mapping only when the active harness is Codex.

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
| Required handshake | Use a separate parent-visible exchange: the executor returns `ACCEPTED` or a blocked form and stops; after the primary agent checks it, continue the same executor through the current follow-up mechanism. If the surface cannot preserve executor identity and context across that exchange, return `MISSING_CAPABILITY` rather than simulate a gate. |
| Send additional context | Use the current follow-up/message mechanism without silently changing the task contract. |
| Wait for results | Use the current wait/status mechanism and retain primary-agent responsibility. |
| Stop unsafe work | Interrupt or stop the subagent when authority, scope, or the core contract is violated. |

Do not hard-code a tool JSON schema in the shared protocol. Tool names and parameters can vary by Codex surface and release.

## Permission behavior

- Subagents do not create new task authority.
- A subagent or the primary agent may still encounter sandbox approval or an unavailable tool.
- Map a missing collaboration feature to `MISSING_CAPABILITY`.
- Map a sandbox or approval denial to `PLATFORM_PERMISSION_BLOCKED`.
- Map an available tool that the task did not authorize to `CAPABILITY_OUT_OF_SCOPE`.

Place that exact uppercase label as the first status token on the first line of the failure return. A mandatory host or project prefix may precede it on the same line; otherwise nothing may appear before it. Put no markup around it and do not substitute a platform-native or conversational status name.

## Result reception

Read the subagent's returned artifacts and evidence. Re-run proportionate checks from the primary context. Do not treat a completion message, commit, or claimed test result as final acceptance without inspection.
