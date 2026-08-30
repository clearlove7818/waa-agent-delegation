# Agy Runtime Map

Use this map only when the active harness is Agy. Apply the shared dependency handoff and task contract from [protocol.md](protocol.md); this file maps them to Agy's active task-level subagent surface.

Session Agent selection and task-level subagent invocation are different operations. Use the task-level interface for delegation and keep the packet self-contained.

## Native flow

| Delegation action | Agy behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Create one bounded executor through the active task-level subagent interface. |
| `TASK_SPECIALIST_SUBAGENT` | Send the task-scoped specialist contract through an available transient specialist or subagent interface. |
| `NAMED_AGENT` | Invoke the exact authorized child Agent through the task-level interface; a session Agent selection alone is not delegation. |
| Required handshake | When the shared protocol requires a handshake, require a parent-visible `ACCEPTED` or blocked return, inspect it, then continue the same conversation through the active continuation interface. If the conversation identity cannot be preserved, return `MISSING_CAPABILITY`. |
| Receive results | Receive the task-level return in the primary session and preserve the packet identity. |
| Stop unsafe work | Use the active task-management control. A terminated target is unavailable and requires a new packet. |

Continue the original conversation after a dependency result is verified. Do not treat an idle or listed Agent as proof that the original delegated conversation completed.

## Runtime failures

- Missing task-level creation or continuation interface: `MISSING_CAPABILITY`.
- Sandbox or approval denial: `PLATFORM_PERMISSION_BLOCKED`.
- Available action outside current-task authorization: `CAPABILITY_OUT_OF_SCOPE`.
