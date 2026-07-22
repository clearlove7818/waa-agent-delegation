# waa-agent-delegation

`waa-agent-delegation` is a cross-platform Agent Skill for preparing and governing an actual delegation after a primary agent has decided to create or invoke a subagent.

It helps the primary agent choose an ordinary execution subagent, a task-specific specialist, or an already-authorized named agent; check capability and permission boundaries; construct a risk-sized task packet; and receive the result without transferring final responsibility.

## What it does not do

- It does not decide that every complex task should be delegated.
- It does not activate named agents without explicit authorization.
- It does not grant tools, permissions, sandbox exceptions, or external authority.
- It does not automatically start independent evaluation or a review loop.
- It does not install itself into Codex, Claude Code, or Agy CLI.

## Architecture

The repository separates three concerns:

| Layer | Files | Purpose |
| --- | --- | --- |
| Shared runtime | [`SKILL.md`](SKILL.md), [`references/protocol.md`](references/protocol.md) | Stable delegation semantics and contract patterns |
| Platform runtime | [`references/platform-compatibility.md`](references/platform-compatibility.md), platform-specific maps | Discovery facts, native interface mapping, permissions, and known unknowns |
| Maintenance and evidence | [`MAINTAINING.md`](MAINTAINING.md), [`evals/cases.md`](evals/cases.md) | Human iteration process and forward-case history |

`agents/openai.yaml` is Codex UI metadata. It is not an Agent definition and is not required by Claude Code or Agy CLI.

## Repository map

```text
waa-agent-delegation/
├── README.md
├── MAINTAINING.md
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── protocol.md
│   ├── platform-compatibility.md
│   ├── platform-codex.md
│   ├── platform-claude-code.md
│   └── platform-agy-cli.md
└── evals/cases.md
```

## Manual installation candidates

This repository does not include or run an installer. Review the target and manually copy or symbolically link the whole repository directory.

| Platform | User candidate | Project candidate |
| --- | --- | --- |
| Codex CLI | `~/.agents/skills/waa-agent-delegation/` | `<project>/.agents/skills/waa-agent-delegation/` |
| Claude Code | `~/.claude/skills/waa-agent-delegation/` | `<project>/.claude/skills/waa-agent-delegation/` |
| Agy CLI | `~/.gemini/config/skills/waa-agent-delegation/` | `<project>/.agents/skills/waa-agent-delegation/` |

Example manual symlink shape on macOS or Linux:

```bash
ln -s /absolute/path/to/waa-agent-delegation /chosen/discovery/path/waa-agent-delegation
```

Example manual copy shape:

```bash
cp -R /absolute/path/to/waa-agent-delegation /chosen/discovery/path/waa-agent-delegation
```

Do not run both methods for the same destination. Confirm the destination is absent or intentionally replaceable before acting. Restart or refresh the platform if it does not detect the Skill automatically.

To uninstall, remove only the exact copy or symbolic link that you created manually after verifying its resolved target. To switch versions, update the source checkout or replace the exact installed copy deliberately.

## Validate locally

From this repository:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

Also parse the YAML files, check local Markdown links, and work through [`evals/cases.md`](evals/cases.md). Cases are regression prompts, not a fixed score or automated quality gate.

## Continue improving the Skill

Follow [`MAINTAINING.md`](MAINTAINING.md):

1. Capture a real routing, contract, platform, or result-reception problem as a case.
2. Update the smallest responsible layer.
3. Run structural validation and the affected cases.
4. Record actual observations without inventing evidence.
5. Commit the focused change so Git remains the rollback boundary.

Update platform claims only from official documentation, official repositories, current product files, or direct runtime evidence. Keep unresolved contradictions under `PLATFORM_UNKNOWN`.
