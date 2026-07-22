# Platform Compatibility

Last reviewed: 2026-07-22.

This repository uses one root `SKILL.md` as the semantic source. Platform discovery paths and delegation interfaces remain platform-specific. A repository checkout is not automatically installed on any platform.

## Compatibility matrix

| Platform | Shared root `SKILL.md` | User discovery candidate | Project discovery candidate | Delegation surface | Product-specific Skill adapter |
| --- | --- | --- | --- | --- | --- |
| Codex CLI | Yes | `~/.agents/skills/waa-agent-delegation/` | `.agents/skills/waa-agent-delegation/` | Current collaboration/subagent tools | `agents/openai.yaml` for Codex UI metadata only |
| Claude Code | Yes | `~/.claude/skills/waa-agent-delegation/` | `.claude/skills/waa-agent-delegation/` | Current `Agent` tool and available subagents | None required |
| Agy CLI | Yes, based on current general Skills docs and Agy 1.1.5 evidence | `~/.gemini/config/skills/waa-agent-delegation/` | `.agents/skills/waa-agent-delegation/` | `invoke_subagent`, session-level `define_subagent`, and authorized agent selection | None required |

Copy or symbolically link the same repository directory into each chosen discovery path manually. Do not copy the `SKILL.md` body into three maintained variants.

## Proven common facts

- All three platforms can consume a directory-based Skill whose entry point is `SKILL.md` with `name` and `description` frontmatter.
- Discovery and automatic triggering depend on the platform scanning an installed path; a GitHub checkout elsewhere is not enough.
- Subagents use separate or reduced context. Build self-contained task packets instead of assuming the primary conversation is inherited.
- Platform availability or tool exposure does not establish task authorization.
- `ACCEPTED`, the four failure returns, and named-agent authorization are governance protocol, not native cross-platform statuses.
- No platform-specific Agent definition is needed for this Skill because it teaches the primary agent how to delegate; it does not define a persistent executor.

## Installation boundary

This repository is an installation candidate only. Repository creation, validation, Git operations, and GitHub publication do not authorize writes to any of these locations:

- `~/.agents/skills`
- `~/.codex`
- `~/.claude`
- `~/.gemini`
- project `.agents/skills`
- project `.claude/skills`

Install, update, switch, or remove the Skill manually after reviewing the target path.

## Official sources

Accessed 2026-07-22:

### Agent Skills standard

- <https://agentskills.io/specification>
- <https://github.com/agentskills/agentskills>

### Codex

- <https://developers.openai.com/codex/skills>
- <https://developers.openai.com/codex/plugins/build>
- <https://github.com/openai/plugins>

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
- <https://github.com/google-antigravity/antigravity-cli>

## PLATFORM_UNKNOWN

- Automatic Skill and Agent relevance algorithms and thresholds are not public on the three platforms; no description can guarantee identical triggering across models and versions.
- Native subagent tools do not expose one stable cross-platform parameter schema. Use the current platform interface instead of hard-coding low-level call shapes.
- Claude managed policy can prohibit user or project Skills even when the documented path is correct.
- Agy's general Skills documentation describes directory-based `SKILL.md` packages under `~/.gemini/config/skills`, while its CLI Plugins page also describes flat Skill files under other paths. The precedence, merging, and deprecation rules are not sufficiently documented. Current general docs, Agy 1.1.5 product evidence, and the local configuration layout support the directory-based candidate used here.
- Agy has not documented how arbitrary adjunct files such as `agents/openai.yaml` are handled. Only `SKILL.md` is treated as its entry point here.
- Agy model-backed discovery and delegation were not live-tested because the local Agy CLI was not authenticated during research.
- `agents/openai.yaml` is confirmed as Codex metadata; Claude and Agy do not document it as their interface and must not depend on it.
