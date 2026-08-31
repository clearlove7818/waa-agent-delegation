# Claude Code Runtime Map

Use this map only when the active harness is Claude Code. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to the active native delegation interface.

Keep the packet self-contained because the executor has an independent context. Use only delegation and continuation names actually exposed by the active surface.

## Native flow

| Delegation action | Claude Code behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through the active native delegation interface. |
| `TASK_SPECIALIST_SUBAGENT` | Send the task-scoped specialist contract or select an already available suitable custom subagent. |
| `NAMED_AGENT` | Create the exact authorized Agent through the active native interface. |
| Required handshake | When the shared protocol requires a handshake, use one foreground delegation exchange for `ACCEPTED` or a blocked return. |
| Continue original executor | Continue or resume the same Agent through the active native interface. If identity and context cannot be preserved, return `MISSING_CAPABILITY`. |
| Receive results | Receive the native delegation result in the primary session and preserve the packet identity. |
| Stop unsafe work | Use the active cancellation or stop control and confirm that execution stopped. |

## Runtime failures

- Missing delegation or continuation interface: `MISSING_CAPABILITY`.
- Platform permission or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
