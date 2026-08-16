# Agy CLI Runtime Map

Discovery status: the user-level directory candidate has current local installation evidence. Agy CLI 1.1.13 is the user-confirmed tested version for the 2026-08-15 live runs, which verified explicit Skill loading plus a complete named-Agent acceptance, parent-visible pause, and same-conversation completion. Automatic relevance, project-level Skill discovery, portability to other installations, and cross-version behavior remain `PLATFORM_UNKNOWN`.

Use this mapping only when the active harness is Google Antigravity CLI (`agy`).

## Before dispatch

1. Confirm the installed Agy version and the currently exposed subagent tools rather than relying only on documentation. Do not treat a visible directory or `SKILL.md` as proof that Agy discovered or loaded the Skill.
2. Confirm the current workspace, sandbox, command rules, file scopes, and approval state.
3. Treat `/agents` session-agent selection and task-level `invoke_subagent` as different operations.
4. Do not create persistent `.agents/agents` or `~/.gemini/config/agents` definitions merely to adapt this Skill. This does not prohibit selecting or using an already-existing definition that is explicitly authorized for the current task.

## Map semantic actions

| Delegation action | Agy behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Use `invoke_subagent` with a suitable currently available type and a self-contained task packet. A user-supplied suite observed this surface, but its low-risk combined return omitted `Taken on faith` and `Filled in`; enforce the complete combined form rather than treating that run as protocol conformance. |
| `TASK_SPECIALIST_SUBAGENT` | When justified and supported, use session-level `define_subagent` to describe the temporary role and minimum tools, then invoke it. A user-supplied suite observed `define_subagent`, but preserved only a truncated specialist definition and a combined completion; the required separate handshake and complete eight-part contract remain unverified. Do not persist the definition automatically. |
| `NAMED_AGENT` | Session Agent selection and task-level child invocation are different operations; neither session selection nor an agent listing alone proves child invocation. User-supplied 2026-08-15 runs verified `invoke_subagent` with named Agent `jun`, including the complete protocol forms, on the tested installation. Use the currently exposed child surface only after authorization; if it is absent, return `MISSING_CAPABILITY`. |
| Required handshake | A user-supplied 2026-08-15 B01 run verified a complete parent-visible round trip: `invoke_subagent` returned every acceptance field, the primary session displayed it and paused, and `send_message` to the original `conversationId` resumed the same target after user release to return every completion field. The user-confirmed 1.1.13 tool contract describes `send_message` as "To send an idle subagent new instructions"; official Agy documentation states, "If the recipient is idle, it will automatically wake up and process the message." Reconfirm the surface and original target state on the active installation; do not replace the gate with a merged final response, and return `MISSING_CAPABILITY` if preserving continuation is unavailable. |
| Run concurrently | Use current background subagent support only for independent work that does not share unsafe state. |
| Inspect or stop work | Use the current `/agents` or task-management surface without changing the contract. Official Agy documentation defines a killed subagent as permanently terminated and not reawakenable. A user-supplied run observed successful `manage_subagents(kill)` termination; it did not prove recovery of the killed conversation or duplicate-work avoidance after a new session starts. |

Idle is a continuation state, not a durability guarantee. User-confirmed Agy 1.1.13 tests observed no built-in idle-destruction timer while the interactive parent CLI remained alive and the target was not killed. The tested loss boundaries were a service or backend restart and a headless wrapper's outer timeout; an explicit kill is permanent under the official lifecycle. No fixed `send_message` round limit was exposed, but the context window and per-turn step limit still bound useful continuation. Public documentation does not promise a retention duration or portability of these lifetime details across installations and versions. If the original target is killed or unavailable, start a newly identified packet and conversation rather than claim that the prior gate was preserved.

Do not hard-code the complete parameters of `invoke_subagent`, `send_message`, or `define_subagent`; their low-level schema is not a stable cross-platform interface. If the current CLI cannot prove the Skill discovery path or tool surface, record `PLATFORM_UNKNOWN` as an evidence state rather than guessing. `PLATFORM_UNKNOWN` is not a task failure label.

## Evidence sources

Accessed or rechecked 2026-08-16:

- <https://antigravity.google/docs/subagents>
- <https://github.com/google-antigravity/antigravity-cli>
- Local `agy --version` output and user-confirmed tested version: `1.1.13`.
- [User-confirmed platform-facts evidence](../evals/evidence/2026-08-16-platform-facts.md), source-report SHA-256 `09e0e116bda5502ca4ec0e10f3964f5f2d9e0bdd205e6ceb81ae062ef93d19c6`.

## Permission behavior

- Agy permission rules use `deny`, `ask`, and `allow`, with deny taking precedence over ask and allow.
- Subagents inherit parent-approved command prefixes and file scopes and cannot create new user authority.
- Web access, commands, MCP tools, workspace-external files, and sandbox configuration can require approval.
- Never use unsafe permission-bypass flags to satisfy a delegated task unless the user explicitly requested that separate action and the platform permits it.

Map absent or incompatible tools to `MISSING_CAPABILITY`, unauthorized available tools to `CAPABILITY_OUT_OF_SCOPE`, and sandbox or approval barriers to `PLATFORM_PERMISSION_BLOCKED`.

The 2026-08-15 suite preserved correctly shaped `BLOCKED`, `MISSING_CAPABILITY`, and `CAPABILITY_OUT_OF_SCOPE` returns, but not the complete parent task packets used to establish each root cause. Treat those observations as output-shape evidence, not independent proof of the capability or authority facts. A real, harmless Agy permission denial was not available, so `PLATFORM_PERMISSION_BLOCKED` remains unverified.

Place the exact uppercase label as the first status token on the first line. Use a mandatory prefix only when the task packet records its exact text, governing source, and applicability to this executor, or when a directly applicable higher-priority runtime rule controls despite a packet defect. Never infer a prefix from an external instruction or resident identity document that does not govern the executor; obey a directly applicable rule and return `BLOCKED` for any packet omission or conflict before execution. Put no markup around the label and do not translate it or replace it with an Agy task-state name.

## Result reception

Wait for the task-level result, inspect artifacts and evidence, and verify from the primary session. When continuation preserves a required gate, confirm the same conversation and packet identity are retained. Do not confuse selection of a session Agent with successful completion of a delegated task.

The suite report stated that the primary session rejected five malformed in-memory returns, but it did not preserve their verbatim inputs and primary-session outputs. Identity-mismatch and status-conflict reception therefore remain unverified behavioral claims rather than recorded fixtures.
