# Platform Compatibility

Last reviewed: 2026-08-30.

This repository uses one root `SKILL.md` as the semantic source. Platform discovery paths and delegation interfaces remain platform-specific. A repository checkout is not automatically installed on any platform.

## Compatibility matrix

| Platform | Shared root `SKILL.md` | User discovery candidate | Project discovery candidate | Delegation surface | Product-specific Skill adapter |
| --- | --- | --- | --- | --- | --- |
| Codex CLI | Yes | `~/.agents/skills/waa-agent-delegation/` | `.agents/skills/waa-agent-delegation/` | Current collaboration/subagent tools | `agents/openai.yaml` for Codex UI metadata only |
| Claude Code | Yes | `~/.claude/skills/waa-agent-delegation/` | `.claude/skills/waa-agent-delegation/` | Current `Agent` tool and available subagents | None required |
| Agy CLI | `SKILL.md` | `~/.gemini/config/skills/waa-agent-delegation/` | `PLATFORM_UNKNOWN` | Current Agy subagent surface; verify `invoke_subagent`, continuation, and any transient specialist interface in the active session. | None required |
| OpenCode | Yes | `~/.config/opencode/skills/waa-agent-delegation/` or `~/.agents/skills/waa-agent-delegation/` | `.opencode/skills/waa-agent-delegation/` or `.agents/skills/waa-agent-delegation/` | Native `task` tool with configured subagents and resumable `task_id` | None required |

Copy or symbolically link the same repository directory into a documented discovery path manually. OpenCode also scans compatible `.agents/skills` locations. Skill discovery does not prove that the selected subagent, `task` permission, or resumable handshake is available in the active session. Do not copy the `SKILL.md` body into maintained platform variants.

## Shared facts

- Root `SKILL.md` is the semantic source; platform maps only translate discovery, native interfaces, permissions, and known unknowns.
- `EXECUTION_SUBAGENT`, `TASK_SPECIALIST_SUBAGENT`, and `NAMED_AGENT` are governance values, not native tool names.
- Discovery or tool exposure never proves task authorization. Packets remain self-contained because child context may be separate or reduced.
- The four failure labels, named-agent authorization, and the parent-visible handshake are Skill rules, not portable native statuses.
- No persistent Agent definition is needed for this Skill.

## Installation boundary

This repository is an installation candidate only. Install, update, switch, or remove the Skill manually after reviewing the exact target path; repository or GitHub operations do not authorize those writes.

## PLATFORM_UNKNOWN

- Automatic Skill and Agent relevance algorithms and thresholds are not public across these platforms; no description can guarantee identical triggering across models and versions.
- Native subagent tools do not expose one stable cross-platform parameter schema. Use the current platform interface instead of hard-coding low-level call shapes.
- Claude managed policy can prohibit user or project Skills even when the documented path is correct.
- Agy's user-supplied 1.1.13 run verified explicit loading and one named-Agent handshake on one installation; discovery, portability, retention, and cross-version behavior remain unknown.
- `agents/openai.yaml` is Codex UI metadata only; other platforms must not depend on it.
- OpenCode's native `task` interface and resumable `task_id` are versioned runtime facts; agent availability, permissions, refresh, and nested behavior still require an active-session check.
