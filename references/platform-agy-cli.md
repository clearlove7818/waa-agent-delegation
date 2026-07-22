# Agy CLI Runtime Map

Use this mapping only when the active harness is Google Antigravity CLI (`agy`).

## Before dispatch

1. Confirm the installed Agy version and the currently exposed subagent tools rather than relying only on documentation.
2. Confirm the current workspace, sandbox, command rules, file scopes, and approval state.
3. Treat `/agents` session-agent selection and task-level `invoke_subagent` as different operations.
4. Do not create persistent `.agents/agents` or `~/.gemini/config/agents` definitions merely to adapt this Skill.

## Map semantic actions

| Delegation action | Agy behavior |
| --- | --- |
| Create an execution subagent | Use `invoke_subagent` with a suitable currently available type and a self-contained task packet. |
| Create a task specialist | When justified and supported, use session-level `define_subagent` to describe the temporary role and minimum tools, then invoke it. Do not persist it automatically. |
| Use a named agent | Use the current authorized agent-selection surface only after user authorization and primary-agent selection. |
| Run concurrently | Use current background subagent support only for independent work that does not share unsafe state. |
| Inspect or stop work | Use the current `/agents` or task-management surface without changing the contract. |

Do not hard-code the complete parameters of `invoke_subagent` or `define_subagent`; their low-level schema is not a stable cross-platform interface.

## Permission behavior

- Agy permission rules use `deny`, `ask`, and `allow`, with deny taking precedence over ask and allow.
- Subagents inherit parent-approved command prefixes and file scopes and cannot create new user authority.
- Web access, commands, MCP tools, workspace-external files, and sandbox configuration can require approval.
- Never use unsafe permission-bypass flags to satisfy a delegated task unless the user explicitly requested that separate action and the platform permits it.

Map absent or incompatible tools to `MISSING_CAPABILITY`, unauthorized available tools to `CAPABILITY_OUT_OF_SCOPE`, and sandbox or approval barriers to `PLATFORM_PERMISSION_BLOCKED`.

Place the exact uppercase label on the first line. Do not translate it or replace it with an Agy task-state name.

## Result reception

Wait for the task-level result, inspect artifacts and evidence, and verify from the primary session. Do not confuse selection of a session Agent with successful completion of a delegated task.
