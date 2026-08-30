# waa-agent-delegation

`waa-agent-delegation` is a cross-platform Agent Skill for preparing and governing an actual delegation after a primary agent has decided to create or invoke a subagent.

It helps the primary agent choose exactly one `EXECUTION_SUBAGENT`, `TASK_SPECIALIST_SUBAGENT`, or explicitly authorized `NAMED_AGENT`; check capability and permission boundaries; construct a risk-sized TASK-006 packet; and receive the result without transferring final responsibility.

中文摘要：这是一个以单一语义源适配 Codex CLI、Claude Code、Agy CLI 和 OpenCode 的 Agent 委派 Skill。它只增强已经决定执行的委派，不替主 Agent 决定任务方向、扩大权限或转移最终责任。各平台的发现路径、原生子代理接口和权限行为由对应的平台说明处理。

## What it does not do

- It does not decide that every complex task should be delegated.
- It does not activate named agents without explicit authorization.
- It does not grant tools, permissions, sandbox exceptions, or external authority.
- It does not automatically start independent evaluation or a review loop.
- It does not install itself into Codex, Claude Code, Agy CLI, or OpenCode.

## Architecture

`SKILL.md` is the shared entry point. `references/protocol.md` and `references/packet-template.md` define packet and return contracts; one active `references/platform-*.md` maps the native surface; `references/evaluation.md` is loaded only for an authorized evaluation. `MAINTAINING.md`, `CONTRIBUTING.md`, and `SECURITY.md` are human-facing.

`agents/openai.yaml` is Codex UI metadata only.

## Runtime-facing repository map

```text
waa-agent-delegation/
├── README.md
├── MAINTAINING.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── SKILL.md
├── agents/openai.yaml
└── references/
│   ├── protocol.md
│   ├── packet-template.md
│   ├── platform-compatibility.md
│   ├── platform-codex.md
│   ├── platform-claude-code.md
│   ├── platform-agy-cli.md
│   └── platform-opencode.md
```

## Usage

Use this Skill only after the primary agent has already decided that an actual delegation is useful and authorized.

1. Select exactly one executor type.
2. Check capability, authority, platform permission, prohibited actions, and external effects.
3. Build one self-contained packet from [`references/packet-template.md`](references/packet-template.md).
4. Use the applicable handshake and continuation mechanism.
5. Inspect returned artifacts and evidence before integration.

[`references/protocol.md`](references/protocol.md) is authoritative when any summary, platform mapping, or packet rendering differs from it.

## Install manually

This repository does not include or run an installer. Review the target and manually copy or symbolically link the whole repository directory.

### CC Switch

Add the public repository root and select the `main` branch:

```text
https://github.com/clearlove7818/waa-agent-delegation
```

Use the repository root URL without `/tree/main`, `/blob/...`, a trailing slash, or a file path. The root `SKILL.md` is the shared semantic entry point.

### Native Skill discovery candidates

| Platform | User candidate | Project candidate |
| --- | --- | --- |
| Codex CLI | `~/.agents/skills/waa-agent-delegation/` | `<project>/.agents/skills/waa-agent-delegation/` |
| Claude Code | `~/.claude/skills/waa-agent-delegation/` | `<project>/.claude/skills/waa-agent-delegation/` |
| Agy CLI | `~/.gemini/config/skills/waa-agent-delegation/` | `PLATFORM_UNKNOWN` |
| OpenCode | `~/.config/opencode/skills/waa-agent-delegation/` or `~/.agents/skills/waa-agent-delegation/` | `.opencode/skills/waa-agent-delegation/` or `.agents/skills/waa-agent-delegation/` |

Discovery paths and native delegation interfaces can vary by product version and configuration. Confirm the active platform before dispatch and follow the corresponding file under [`references/`](references/).

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

## Contributing

Maintenance rules live in [`MAINTAINING.md`](MAINTAINING.md). Contributions are welcome through [`CONTRIBUTING.md`](CONTRIBUTING.md). Report security-sensitive issues according to [`SECURITY.md`](SECURITY.md).

## License

The source is publicly visible, but no open-source license is granted. See [`LICENSE`](LICENSE).
