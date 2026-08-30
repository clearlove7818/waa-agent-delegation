# Platform Compatibility

The supported setup maintains one Skill source at `~/.agents/skills/waa-agent-delegation/`. CC Switch exposes that source to Codex, Claude Code, Agy, and OpenCode. This Skill does not maintain platform-specific discovery paths.

## Runtime surfaces

| Platform | Create | Continue and receive |
| --- | --- | --- |
| Codex | Current collaboration or subagent creation interface | Continue the same target through the current parent continuation and wait/status interfaces. |
| Claude Code | Active native delegation interface | Continue or resume the same Agent through the active native interface. |
| Agy | Active task-level subagent interface | Continue the same conversation through the active continuation interface; a terminated target requires a new packet. |
| OpenCode | Native `task` interface | Resume the same target with its returned `task_id`. |

The root `SKILL.md` is the semantic source. Platform maps translate only native creation, handshake, continuation, reception, stopping, and runtime permission outcomes. Shared dependency handoff, failure labels, authorization, ownership, and verification remain in [protocol.md](protocol.md).

Loading the Skill or exposing a tool proves capability, not current-task authorization. Use the active platform map at dispatch time; do not copy platform schemas or shared protocol text into compatibility rules.
