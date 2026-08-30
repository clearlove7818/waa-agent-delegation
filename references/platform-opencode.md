# OpenCode Runtime Map

Use this mapping only when the active harness is OpenCode.

Evidence reviewed: 2026-08-25. OpenCode 1.18.20 was installed locally and its native `task` tool includes resumable subagent sessions. Discovery, configured agents, permissions, model access, and running-session refresh remain conditions to verify on the active installation.

## Before dispatch

1. Confirm the active OpenCode version exposes the native `task` tool and that the exact selected agent is available. Do not infer delegation readiness from Skill discovery alone.
2. Confirm the primary agent may call the selected `subagent_type` under the resolved `task` permission, and confirm the child agent's own tool permissions fit the packet.
3. Select a configured named agent only when current-task authorization already exists. Visibility in `opencode agent list` is capability evidence, not authorization.
4. Use foreground Task calls for a required handshake. Background execution is not a substitute for primary-agent inspection before work begins.

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

Each fresh Task call creates a separate subagent context unless `task_id` resumes the prior session. Reusing the exact identifier preserves the conversation but does not create new authority or excuse restating a binding change. The first call in a two-stage handshake must finish without executing the assignment; a single final result that combines acceptance and work is not a pre-execution gate.

Do not hard-code the current Task JSON schema into the shared protocol. OpenCode transport names and parameters can change; this map records only the semantic mapping needed to preserve the protocol.

## Skill and Agent discovery

OpenCode documents global Skills under `~/.config/opencode/skill/` or `~/.config/opencode/skills/`, project Skills under `.opencode/skill/` or `.opencode/skills/`, and compatible external Skills under `.agents/skills/` locations. Agent definitions may be global, project-local, or inline in OpenCode configuration. Confirm the active session has loaded the intended Skill and Agent after any installation or configuration change.

## Permission behavior

- The `task` permission can allow, ask, or deny calls by agent pattern.
- A selected subagent runs under its resolved permissions; the task packet cannot loosen them.
- Map an absent agent, missing native Task feature, or unavailable resumable continuation to `MISSING_CAPABILITY`.
- Map an approval denial or resolved permission block to `PLATFORM_PERMISSION_BLOCKED`.
- Map an available Agent or Task action excluded by current-task authorization to `CAPABILITY_OUT_OF_SCOPE`.

This adapter is not a standalone contract: use [protocol.md](protocol.md) for exact failure-label, mandatory-prefix, and first-line rules, and use this map for OpenCode-specific behavior.

## Result reception

Inspect the subagent's returned text, changed files, commands, and evidence from the primary OpenCode session. Re-run proportionate checks in the primary context. A returned `task_id`, completed Task call, or claimed test result does not transfer artifact ownership or final responsibility.

## Evidence sources

Accessed 2026-08-25:

- <https://opencode.ai/docs/skills/>
- <https://opencode.ai/docs/agents/>
- <https://opencode.ai/docs/permissions/>
- <https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/tool/task.ts>
- [Local OpenCode platform evidence](../evals/evidence/2026-08-25-platform-opencode.md).
