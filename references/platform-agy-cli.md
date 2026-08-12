# Agy CLI Runtime Map

Discovery status: the user-level directory candidate has current local installation evidence and user-reported successful loading as of 2026-08-12. Independent model-backed discovery is still `PLATFORM_UNKNOWN` because the inspected Agy CLI was not authenticated. Project-level Skill discovery remains `PLATFORM_UNKNOWN`.

Use this mapping only when the active harness is Google Antigravity CLI (`agy`).

## Before dispatch

1. Confirm the installed Agy version and the currently exposed subagent tools rather than relying only on documentation. Do not treat a visible directory or `SKILL.md` as proof that Agy discovered or loaded the Skill.
2. Confirm the current workspace, sandbox, command rules, file scopes, and approval state.
3. Treat `/agents` session-agent selection and task-level `invoke_subagent` as different operations.
4. Do not create persistent `.agents/agents` or `~/.gemini/config/agents` definitions merely to adapt this Skill. This does not prohibit selecting or using an already-existing definition that is explicitly authorized for the current task.

## Map semantic actions

| Delegation action | Agy behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Use `invoke_subagent` with a suitable currently available type and a self-contained task packet. |
| `TASK_SPECIALIST_SUBAGENT` | When justified and supported, use session-level `define_subagent` to describe the temporary role and minimum tools, then invoke it. Do not persist it automatically. |
| `NAMED_AGENT` | Agy 1.1.12 exposes `--agent <name>` for selecting the current CLI session Agent and `agy agents` for listing configured identifiers. Use such a current selection surface only after authorization. These surfaces do not by themselves prove that a running primary session can invoke the named Agent as a child task; if that exact delegation surface is absent, return `MISSING_CAPABILITY`. |
| Required handshake | A parent-visible pre-execution handshake round trip is `PLATFORM_UNKNOWN` in current independent evidence. Do not treat a merged final status as a primary-agent-inspected gate. If the packet requires a gate and no preserving continuation mechanism is verified, return `MISSING_CAPABILITY`. |
| Run concurrently | Use current background subagent support only for independent work that does not share unsafe state. |
| Inspect or stop work | Use the current `/agents` or task-management surface without changing the contract. |

Do not hard-code the complete parameters of `invoke_subagent` or `define_subagent`; their low-level schema is not a stable cross-platform interface. If the current CLI cannot prove the Skill discovery path or tool surface, record `PLATFORM_UNKNOWN` as an evidence state rather than guessing. `PLATFORM_UNKNOWN` is not a task failure label.

## Permission behavior

- Agy permission rules use `deny`, `ask`, and `allow`, with deny taking precedence over ask and allow.
- Subagents inherit parent-approved command prefixes and file scopes and cannot create new user authority.
- Web access, commands, MCP tools, workspace-external files, and sandbox configuration can require approval.
- Never use unsafe permission-bypass flags to satisfy a delegated task unless the user explicitly requested that separate action and the platform permits it.

Map absent or incompatible tools to `MISSING_CAPABILITY`, unauthorized available tools to `CAPABILITY_OUT_OF_SCOPE`, and sandbox or approval barriers to `PLATFORM_PERMISSION_BLOCKED`.

Place the exact uppercase label as the first status token on the first line. Use a mandatory prefix only when the task packet records its exact text, governing source, and applicability to this executor, or when a directly applicable higher-priority runtime rule controls despite a packet defect. Never infer a prefix from an external instruction or resident identity document that does not govern the executor; obey a directly applicable rule and return `BLOCKED` for any packet omission or conflict before execution. Put no markup around the label and do not translate it or replace it with an Agy task-state name.

## Result reception

Wait for the task-level result, inspect artifacts and evidence, and verify from the primary session. Do not confuse selection of a session Agent with successful completion of a delegated task.
