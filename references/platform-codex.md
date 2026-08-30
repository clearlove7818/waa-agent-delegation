# Codex Runtime Map

Use this map only when the active harness is Codex. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to the current Codex collaboration surface.

## Native flow

| Delegation action | Codex behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through the current subagent creation interface. |
| `TASK_SPECIALIST_SUBAGENT` | Send the task-scoped specialist contract through the current interface. |
| `NAMED_AGENT` | Select the exact configured agent only after current-task authorization; otherwise return `CAPABILITY_OUT_OF_SCOPE`. |
| Required handshake | When the shared protocol requires a handshake, send the initial packet through the current creation interface and wait for that turn's final `ACCEPTED` or blocked return. After primary-agent inspection, continue the same target through the active continuation interface. If the surface cannot preserve the target and context across the exchange, return `MISSING_CAPABILITY`. |
| Send additional context | Use the current mailbox delivery interface when no new turn is required; use the continuation interface when the executor must resume work. |
| Receive results | Use the current wait/status interface. A non-final message is context, not a completed handshake or result. |
| Stop unsafe work | Use the active interruption control and confirm that execution stopped. |

Continue the original target after a dependency result is verified. If that target is no longer available, create a new packet rather than claim continuation.

## Runtime failures

- Missing creation or continuation interface: `MISSING_CAPABILITY`.
- Sandbox or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
