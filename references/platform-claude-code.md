# Claude Code Runtime Map

Use this mapping only when the active harness is Claude Code.

## Before dispatch

1. Confirm the current `Agent` tool and the intended built-in or custom subagent are available.
2. Check user, project, plugin, and managed settings that affect Skills, tools, agents, permission modes, and worktrees.
3. Assume the subagent has an independent context. Put all material requirements and evidence into the task packet.
4. Do not create `.claude/agents` files merely to adapt this Skill. A persistent custom agent is a separate deliverable and authority decision.

## Dynamic unnamed-subagent child block

At dynamic subagent creation, apply the native tool boundary to the child: omit `Agent` (the current name; `Task` remains its compatibility alias) from the child `tools` allowlist, or add `Agent` to `disallowedTools`. Also exclude `ListAgents`, `SendMessage`, and any exposed `Task*` or `Cron*` agent-team controls when strict management blocking is required. Keep `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` as a depth backstop; at the limit, a normal Agent call is withheld and a fork call returns an error instead of spawning. These controls block native child creation, invocation, definition, management, background, parallel, and fork routes that the active surface exposes. Do not rely on a prompt, Skill, task packet, or file body.

The parent session must retain `Agent` so waa can create, continue, receive, and integrate subagents. If the active Claude surface cannot remove the child Agent/Task surface, return `MISSING_CAPABILITY`; if a configured permission rule denies the child route, return `PLATFORM_PERMISSION_BLOCKED`. Indirect shell, SDK, MCP, or externally managed session routes are not proven by this adapter; if they remain reachable and strict blocking is required, do not claim the block.

## Map semantic actions

| Delegation action | Claude Code behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Use the current `Agent` interface with a suitable available general or built-in agent. |
| `TASK_SPECIALIST_SUBAGENT` | Use the eight-part task-scoped specialist contract or an already available custom subagent with the required tools and restrictions. |
| `NAMED_AGENT` | Select or mention the exact agent only after current-task authorization has been established. |
| Required handshake | Use one Agent exchange for the handshake only. After the primary agent checks it, use the current Agent continuation mechanism to release execution while preserving the original identity and boundary. If continuation cannot preserve that context, return `MISSING_CAPABILITY`. |
| Continue or clarify | Use the current Agent continuation mechanism while preserving the original boundary. |
| Run independently | Use foreground or background execution only when the task and permission behavior support it. |

Do not hard-code the low-level `Agent` schema; it is not a stable cross-platform contract. Older Claude Code material may call this the `Task` tool, but current instructions should use the active interface.

## Permission behavior

- Subagents normally inherit the parent session's available tools, MCP context, and permission environment, subject to configured restrictions.
- Inheritance proves availability, not authorization for this task.
- Approval requests can return to the primary session. Do not interpret an agent message as user approval.
- Managed policy can prevent a documented Skill or custom agent from loading.

Return `MISSING_CAPABILITY`, `CAPABILITY_OUT_OF_SCOPE`, or `PLATFORM_PERMISSION_BLOCKED` according to the evidence instead of retrying through a wider permission mode.

This adapter is not a standalone contract: use [protocol.md](protocol.md) for exact failure-label, mandatory-prefix, and first-line rules, and use this map for Claude-specific behavior.

## Result reception

Inspect the agent's response, changed files, commands, and test evidence. Resolve questions in the primary context, then perform proportionate verification. The primary agent remains responsible for user-facing integration without automatically changing the delegated artifact owner.
