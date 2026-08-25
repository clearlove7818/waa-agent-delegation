# OpenCode platform evidence — 2026-08-25

## Scope

This record covers local OpenCode version, documented Skill locations, native subagent availability, and resumable Task behavior. It does not claim identical behavior across versions, configurations, agents, models, or permission policies.

## Direct observations

- `command -v opencode` resolved to `/opt/homebrew/bin/opencode`.
- `opencode --version` returned `1.18.20`.
- `opencode --help` exposed `agent`, `run`, `session`, and debugging commands.
- `opencode agent --help` exposed Agent creation and listing, while `opencode agent list` identified the built-in `general` and `explore` entries as subagents.
- `opencode debug paths` reported the global configuration directory as `~/.config/opencode`.
- The built-in OpenCode customization guidance returned by `opencode debug skill` documented global Skill locations under `~/.config/opencode/skill/` or `~/.config/opencode/skills/`, project locations under `.opencode/skill/` or `.opencode/skills/`, and compatible external `.agents/skills` locations.
- The installed 1.18.20 binary contains the native Task-tool contract: every fresh invocation starts a new subagent context unless the caller supplies the returned `task_id`, and supplying it resumes the same subagent session. The schema includes `description`, `prompt`, `subagent_type`, and optional `task_id`.

## Interpretation

OpenCode has the mechanism needed for a two-stage governance handshake: the primary agent can require an acceptance-only first Task return, inspect it, then resume the same subagent with `task_id` for execution. This remains conditional on the active agent, Task permission, model access, and exact runtime behavior. Background Task execution does not replace the inspection gate.

## Remaining unknowns

- No forward run of the OpenCode regression fixture has been performed.
- Cross-version stability and automatic Skill relevance remain `PLATFORM_UNKNOWN`.
- A running session may require refresh after Skill or Agent installation; this was not behaviorally tested in this record.
