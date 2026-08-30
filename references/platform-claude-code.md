# Claude Code Runtime Map

Use this map only when the active harness is Claude Code. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to the active native delegation interface.

Keep the packet self-contained because the executor has an independent context. Use only delegation and continuation names actually exposed by the active surface.

## Native flow

| Delegation action | Claude Code behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through the active native delegation interface. |
| `TASK_SPECIALIST_SUBAGENT` | Send the task-scoped specialist contract or select an already available suitable custom subagent. |
| `NAMED_AGENT` | Select the exact Agent only after current-task authorization; otherwise return `CAPABILITY_OUT_OF_SCOPE`. |
| Required handshake | When the shared protocol requires a handshake, use one foreground delegation exchange for `ACCEPTED` or a blocked return. After primary-agent inspection, continue or resume the same Agent through the active native interface. If identity and context cannot be preserved, return `MISSING_CAPABILITY`. |
| Run independently | Start foreground or background work only after any required handshake and only when its result returns to the primary session. |
| Stop unsafe work | Use the active cancellation or stop control and confirm that execution stopped. |

Continue the original Agent after a dependency result is verified. If the original target cannot be resumed, create a new packet rather than claim continuation.

## Runtime failures

- Missing delegation or continuation interface: `MISSING_CAPABILITY`.
- Platform permission or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
