# OpenCode Runtime Map

Use this map only when the active harness is OpenCode. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to the native `task` interface.

## Native flow

| Delegation action | OpenCode behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through a foreground `task` call. |
| `TASK_SPECIALIST_SUBAGENT` | Select an available task-scoped Agent and include the specialist contract in the packet. |
| `NAMED_AGENT` | Create the exact authorized configured Agent through `task`. |
| Required handshake | When the shared protocol requires a handshake, make a foreground `task` call for `ACCEPTED` or a blocked return and inspect it. |
| Continue original executor | Resume the same target with its returned `task_id`; a fresh `task` call creates a separate context. If the original target is unavailable, create a new packet rather than claim continuation. |
| Receive results | Treat the foreground Task return as evidence for primary-agent inspection. |
| Stop unsafe work | Withhold continuation before execution or use an active cancellation control and confirm that execution stopped. |

## Runtime failures

- Missing `task`, selected Agent, or resumable `task_id`: `MISSING_CAPABILITY`.
- Platform permission or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
