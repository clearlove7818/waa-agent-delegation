# Codex Runtime Map

Use this map only when the active harness is Codex. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to the current Codex collaboration surface.

## Native flow

| Delegation action | Codex behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through the current subagent creation interface. |
| `TASK_SPECIALIST_SUBAGENT` | Send the task-scoped specialist contract through the current interface. |
| `NAMED_AGENT` | Create the exact authorized configured Agent through the current interface. |
| Required handshake | When the shared protocol requires a handshake, send the initial packet through the current creation interface and wait for that turn's final `ACCEPTED` or blocked return. |
| Continue original executor | Use the current mailbox delivery interface when no new turn is required; use the continuation interface when the executor must resume. If the target is unavailable, create a new packet rather than claim continuation. |
| Receive results | Use the current wait/status interface. A non-final message is context, not a completed handshake or result. |
| Stop unsafe work | Use the active interruption control and confirm that execution stopped. |

## Runtime failures

- Missing creation or continuation interface: `MISSING_CAPABILITY`.
- Sandbox or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
