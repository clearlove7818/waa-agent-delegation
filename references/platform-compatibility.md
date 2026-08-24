# Platform Compatibility

Last reviewed: 2026-08-24.

This repository uses one root `SKILL.md` as the semantic source. Platform discovery paths and delegation interfaces remain platform-specific. A repository checkout is not automatically installed on any platform.

## Compatibility matrix

| Platform | Shared root `SKILL.md` | User discovery candidate | Project discovery candidate | Delegation surface | Product-specific Skill adapter |
| --- | --- | --- | --- | --- | --- |
| Codex CLI | Yes | `~/.agents/skills/waa-agent-delegation/` | `.agents/skills/waa-agent-delegation/` | Current collaboration/subagent tools | `agents/openai.yaml` for Codex UI metadata only |
| Claude Code | Yes | `~/.claude/skills/waa-agent-delegation/` | `.claude/skills/waa-agent-delegation/` | Current `Agent` tool and available subagents | None required |
| Agy CLI | Explicit `SKILL.md` loading and complete two-stage named-Agent protocol forms were verified by user-supplied local runs on Agy 1.1.13 on 2026-08-15 | `~/.gemini/config/skills/waa-agent-delegation/` has current local installation evidence and working-use evidence | `PLATFORM_UNKNOWN` | Verified locally on 1.1.13: `invoke_subagent` and same-conversation `send_message` continuation. Observed but not fully protocol-verified: session-level `define_subagent`. | None required |
| Pi CLI | Yes | `~/.pi/agent/skills/waa-agent-delegation/` or `~/.agents/skills/waa-agent-delegation/` (ccswitch-managed shared target) | `.pi/skills/waa-agent-delegation/` or `.agents/skills/waa-agent-delegation/` in a trusted project | No built-in subagent interface; optional extension/package `subagent` surface | None required |

For Codex and Claude Code, copy or symbolically link the same repository directory into a documented discovery path manually. ccswitch may make Pi and Claude Code resolve to the same shared target; that shared-target arrangement is an installation choice, not a Pi delegation guarantee. Pi also supports explicit `--skill` loading and trusted project `.pi/skills` or `.agents/skills` locations. Pi core does not include subagents, so actual delegation still requires a separately loaded extension or package and must be checked on the active installation. Do not copy the `SKILL.md` body into maintained platform variants.

## Proven common facts

- The root `SKILL.md` is the shared semantic source; documented discovery support is established for Codex, Claude Code, and Pi. Agy has current user-level installation and explicit working-use evidence from user-supplied local runs, while automatic relevance, project-level discovery, portability, and version-distribution claims remain `PLATFORM_UNKNOWN`.
- All platform maps use exactly `EXECUTION_SUBAGENT`, `TASK_SPECIALIST_SUBAGENT`, and `NAMED_AGENT`; these are governance values, not native tool names.
- Where a platform supports Skill discovery, a repository checkout outside a documented discovery path is not automatically installed.
- Subagents use separate or reduced context. Build self-contained task packets instead of assuming the primary conversation is inherited.
- Platform availability or tool exposure does not establish task authorization.
- `ACCEPTED`, the four failure returns, and named-agent authorization are governance protocol, not native cross-platform statuses.
- A required handshake needs a parent-visible pre-execution exchange that preserves executor identity and task context. Each platform map states whether that exchange is verified or `PLATFORM_UNKNOWN`; a merged final return is not automatically equivalent to a gate.
- No platform-specific Agent definition is needed for this Skill because it teaches the primary agent how to delegate; it does not define a persistent executor.
- Pi core intentionally omits subagents; an optional extension or package may provide a `subagent` tool, but its handshake, continuation, agent scope, and permission behavior are extension-specific and must not be generalized to Pi itself.

## Installation boundary

This repository is an installation candidate only. Repository creation, validation, Git operations, and GitHub publication do not authorize writes to any of these locations:

- `~/.agents/skills`
- `~/.codex`
- `~/.claude`
- `~/.gemini`
- `~/.pi`
- project `.agents/skills`
- project `.claude/skills`

Install, update, switch, or remove the Skill manually after reviewing the target path.

## Official sources

Unless noted otherwise, accessed 2026-07-22.

### Agent Skills standard

- <https://agentskills.io/specification>
- <https://github.com/agentskills/agentskills>

### Codex

- <https://developers.openai.com/codex/skills>
- <https://developers.openai.com/codex/plugins/build>
- <https://github.com/openai/plugins>
- Rechecked 2026-08-16: <https://developers.openai.com/codex/multi-agent/>
- Rechecked 2026-08-16: <https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/multi_agents_spec.rs>

### Claude Code

- <https://code.claude.com/docs/en/skills>
- <https://code.claude.com/docs/en/sub-agents>
- <https://code.claude.com/docs/en/permissions>
- <https://code.claude.com/docs/en/settings>

### Agy CLI

- <https://antigravity.google/docs/skills>
- <https://antigravity.google/docs/cli/plugins>
- <https://antigravity.google/docs/subagents>
- <https://antigravity.google/docs/cli/subagents>
- <https://antigravity.google/docs/cli/commands/agents>
- <https://antigravity.google/docs/cli/permissions>
- <https://antigravity.google/docs/cli/sandbox>
- Rechecked 2026-08-16: <https://antigravity.google/docs/subagents>
- Rechecked 2026-08-16: <https://github.com/google-antigravity/antigravity-cli>

### Pi

- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md>
- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md>
- Rechecked 2026-08-24: local `pi --version` reported `0.84.2`.

## PLATFORM_UNKNOWN

- Automatic Skill and Agent relevance algorithms and thresholds are not public across these platforms; no description can guarantee identical triggering across models and versions.
- Native subagent tools do not expose one stable cross-platform parameter schema. Use the current platform interface instead of hard-coding low-level call shapes.
- Claude managed policy can prohibit user or project Skills even when the documented path is correct.
- Agy's current local configuration resolves `~/.gemini/config/skills` to the shared Skill directory. User-supplied runs on Agy 1.1.13 on 2026-08-15 verified explicit Skill loading, named-Agent child invocation, complete parent-visible pre-execution acceptance, and complete same-conversation delivery. User-confirmed 1.1.13 tests also bounded idle lifetime by explicit kill, service or backend restart, headless-wrapper timeout, context pressure, and per-turn step limits. Project-level placement, portability to other installations, precedence among documented locations, automatic relevance behavior, exact retention duration, and cross-version stability remain `PLATFORM_UNKNOWN`.
- Agy has not documented how arbitrary adjunct files such as `agents/openai.yaml` are handled. Only `SKILL.md` is treated as its entry point here.
- The Agy evidence consists of user-supplied observations on Agy 1.1.13, one installation, and one named Agent. It does not establish a distribution across versions, Agents, accounts, or environments.
- `agents/openai.yaml` is confirmed as Codex metadata; Claude and Agy do not document it as their interface and must not depend on it.
- Pi 0.84.2 was installed locally on 2026-08-24; `pi --help` exposed Skill and extension loading but no built-in subagent tool, and `pi list` reported no installed packages. The optional extension/package boundary, parent-visible handshake, and preserving continuation remain runtime facts to verify; return `MISSING_CAPABILITY` unless the active extension proves the required surface.
