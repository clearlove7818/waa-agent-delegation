# OpenCode Runtime Map

Use this mapping only when the active harness is OpenCode.

Verify the active OpenCode version, configured agents, permissions, model access, and session refresh before dispatch.

## Before dispatch

1. Confirm the active OpenCode version exposes the native `task` tool and that the exact selected agent is available. Do not infer delegation readiness from Skill discovery alone.
2. Confirm the primary agent may call the selected `subagent_type` under the resolved `task` permission, and confirm the child agent's own tool permissions fit the packet.
3. Select a configured named agent only when current-task authorization already exists. Visibility in `opencode agent list` is capability evidence, not authorization.
4. Use foreground Task calls for a required handshake. Background execution is not a substitute for primary-agent inspection before work begins.

## Dynamic unnamed-subagent child block

Require the resolved OpenCode configuration to keep `subagent_depth` at `1` for the dispatch. The native depth guard allows waa (the primary) to launch a subagent but rejects any `task` call from that child before another child session is created, so it blocks nested create or invoke, background, and parallel launches through `task`. Keep the child's `permission.task` denied for `*` unless the active configuration proves an equivalent native deny; a prompt, Skill, task packet, or agent body cannot grant or remove this boundary.

The parent retains its `task` permission and can create, continue, receive, and integrate subagents. If `subagent_depth` is unavailable, can be raised by the active configuration, or the child can reach another native agent-management or fork surface not covered by the depth/permission guard, return `MISSING_CAPABILITY`; if the resolved permission policy blocks the requested child route, return `PLATFORM_PERMISSION_BLOCKED`. Direct user `@` invocation and indirect shell or plugin routes are separate surfaces and remain unverified by this adapter.

## Map semantic actions

| Delegation action | OpenCode behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Invoke an available general or task-specific subagent with one bounded packet through the native `task` tool. |
| `TASK_SPECIALIST_SUBAGENT` | Select an available task-scoped agent and embed the eight-part `specialist_contract` in the prompt; do not create a persistent Agent merely to represent temporary expertise. |
| `NAMED_AGENT` | Select the exact configured Agent only after current-task authorization; otherwise return `CAPABILITY_OUT_OF_SCOPE`. |
| Required handshake | Make a foreground `task` call whose prompt requires only `ACCEPTED` or a blocked form and explicitly prohibits starting the assigned work. Inspect the return in the primary session, preserve the returned `task_id`, then make a second `task` call with that exact `task_id` to authorize execution. If the active surface cannot return and resume the same subagent session, return `MISSING_CAPABILITY` rather than simulate a gate. |
| Send additional context | Resume the same subagent with its `task_id`. State any binding addition explicitly; continuation does not silently widen the accepted packet. |
| Wait for results | Foreground Task calls return one result to the primary agent. Treat that result as evidence, not acceptance of the integrated outcome. |
| Stop unsafe work | Withhold the continuation after a blocked or defective handshake. During execution, use only interruption or cancellation controls actually exposed by the active surface; never claim a stop that was not confirmed. |

Each fresh Task call creates a separate context unless `task_id` resumes the prior session. Reuse the exact identifier for continuation, and keep the first handshake call separate from execution.

Do not hard-code the current Task JSON schema into the shared protocol. OpenCode transport names and parameters can change; this map records only the semantic mapping needed to preserve the protocol.

## Permission behavior

- The `task` permission can allow, ask, or deny calls by agent pattern.
- A selected subagent runs under its resolved permissions; the task packet cannot loosen them.
- Map an absent agent, missing native Task feature, or unavailable resumable continuation to `MISSING_CAPABILITY`.
- Map an approval denial or resolved permission block to `PLATFORM_PERMISSION_BLOCKED`.
- Map an available Agent or Task action excluded by current-task authorization to `CAPABILITY_OUT_OF_SCOPE`.

This adapter is not a standalone contract: use [protocol.md](protocol.md) for exact failure-label, mandatory-prefix, and first-line rules, and use this map for OpenCode-specific behavior.

## Result reception

Inspect the subagent's returned text, changed files, commands, and evidence from the primary OpenCode session. Re-run proportionate checks in the primary context. A returned `task_id`, completed Task call, or claimed test result does not transfer artifact ownership or final responsibility.
