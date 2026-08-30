# Agy CLI Runtime Map

Discovery, automatic relevance, portability, and cross-version behavior are installation-specific; verify the active Agy session.

Use this mapping only when the active harness is Google Antigravity CLI (`agy`).

## Before dispatch

1. Confirm the installed Agy version and the currently exposed subagent tools rather than relying only on documentation. Do not treat a visible directory or `SKILL.md` as proof that Agy discovered or loaded the Skill.
2. Confirm the current workspace, sandbox, command rules, file scopes, and approval state.
3. Treat `/agents` session-agent selection and task-level `invoke_subagent` as different operations.
4. Do not create persistent `.agents/agents` or `~/.gemini/config/agents` definitions merely to adapt this Skill. This does not prohibit selecting or using an already-existing definition that is explicitly authorized for the current task.

## Dynamic unnamed-subagent child block

Agy's public subagent docs expose transient `define_subagent`, per-agent tool lists, asynchronous execution, peer messaging, and a nesting limit, but do not document a child-only switch that removes every collaboration route. A `tools` allowlist is a native block only when the active tool schema exposes and excludes all child collaboration tools: `invoke_subagent`, `define_subagent`, `send_message`, `manage_subagents`, and any fork or team control.

If the active `define_subagent` surface exposes an explicit child-tool disable, verify that it removes the full set before relying on it; this is not a public cross-version guarantee. If no native child-only block is exposed or enforced, return `MISSING_CAPABILITY`; if the platform rejects the requested child tool boundary, return `PLATFORM_PERMISSION_BLOCKED`. The parent keeps its own collaboration tools and can still create, continue, receive, and integrate subagents. Do not use a prompt, Skill, task packet, or Markdown body as the enforcement mechanism.

## Map semantic actions

| Delegation action | Agy behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Use the currently exposed `invoke_subagent` surface with a suitable type and a self-contained packet. |
| `TASK_SPECIALIST_SUBAGENT` | When supported, use the current transient specialist surface and minimum tools; do not persist a definition automatically. |
| `NAMED_AGENT` | Session Agent selection and task-level invocation are separate. Use the exact child surface only after authorization; if it is absent, return `MISSING_CAPABILITY`. |
| Required handshake | Use a parent-visible acceptance exchange, then continue the same target through the active continuation surface. If identity or context cannot be preserved, return `MISSING_CAPABILITY`. |
| Run concurrently | Use current background subagent support only for independent work that does not share unsafe state. |
| Inspect or stop work | Use the current `/agents` or task-management surface without changing the contract. Treat a killed target as unavailable unless the active platform proves recovery. |

Idle is a continuation state, not a durability guarantee. If the original target is killed or unavailable, start a new packet and conversation rather than claim that the prior gate was preserved.

Do not hard-code the complete parameters of `invoke_subagent`, `send_message`, or `define_subagent`; their low-level schema is not a stable cross-platform interface. If the current CLI cannot prove the Skill discovery path or tool surface, record `PLATFORM_UNKNOWN` as an evidence state rather than guessing. `PLATFORM_UNKNOWN` is not a task failure label.

## Permission behavior

- Agy permission rules use `deny`, `ask`, and `allow`, with deny taking precedence over ask and allow.
- Subagents inherit parent-approved command prefixes and file scopes and cannot create new user authority.
- Web access, commands, MCP tools, workspace-external files, and sandbox configuration can require approval.
- Never use unsafe permission-bypass flags to satisfy a delegated task unless the user explicitly requested that separate action and the platform permits it.

Map absent or incompatible tools to `MISSING_CAPABILITY`, unauthorized available tools to `CAPABILITY_OUT_OF_SCOPE`, and sandbox or approval barriers to `PLATFORM_PERMISSION_BLOCKED`.

This adapter is not a standalone contract: use [protocol.md](protocol.md) for exact failure-label, mandatory-prefix, and first-line rules, and use this map for Agy-specific behavior.

## Result reception

Wait for the task-level result, inspect artifacts and evidence, and verify from the primary session. When continuation preserves a required gate, confirm the same conversation and packet identity are retained. Do not confuse selection of a session Agent with successful completion of a delegated task.
