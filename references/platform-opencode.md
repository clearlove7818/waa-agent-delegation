# OpenCode Runtime Map

Use this map only when the active harness is OpenCode. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to the native `task` interface.

## Native flow

| Delegation action | OpenCode behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through a foreground `task` call. |
| `TASK_SPECIALIST_SUBAGENT` | Select an available task-scoped Agent and include the specialist contract in the packet. |
| `NAMED_AGENT` | Select the exact configured Agent only after current-task authorization; otherwise return `CAPABILITY_OUT_OF_SCOPE`. |
| Required handshake | When the shared protocol requires a handshake, make a foreground `task` call for `ACCEPTED` or a blocked return, inspect it, preserve the returned `task_id`, then continue the same target with that identifier. If the surface cannot return and resume the same target, return `MISSING_CAPABILITY`. |
| Send additional context | Resume the same target with its `task_id`; a fresh Task call creates a separate context. |
| Receive results | Treat the foreground Task return as evidence for primary-agent inspection. |
| Stop unsafe work | Withhold continuation before execution or use an active cancellation control and confirm that execution stopped. |

After a dependency result is verified, resume the original target with its exact `task_id`. If it is unavailable, create a new packet rather than substitute a fresh target for the original continuation.

## Runtime failures

- Missing `task`, selected Agent, or resumable `task_id`: `MISSING_CAPABILITY`.
- Platform permission or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
