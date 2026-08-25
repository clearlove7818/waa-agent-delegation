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

The repository separates three concerns:

| Layer | Files | Purpose |
| --- | --- | --- |
| Shared runtime | [`SKILL.md`](SKILL.md), [`references/protocol.md`](references/protocol.md), [`references/packet-template.md`](references/packet-template.md) | Stable delegation semantics, authoritative contracts, and dispatch-time packet rendering |
| Platform runtime | [`references/platform-compatibility.md`](references/platform-compatibility.md), platform-specific maps | Discovery facts, native interface mapping, permissions, and known unknowns |
| Maintenance | [`MAINTAINING.md`](MAINTAINING.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md) | Change ownership, contribution workflow, and security reporting |

`agents/openai.yaml` is Codex UI metadata. It is not an Agent definition and is not required by Claude Code or Agy CLI.

## Protocol identity

Every packet, including a low-risk packet that skips the handshake, carries exactly one `assembly_type` and these identity fields:

```text
task_packet_version
task_id
assembly_type: EXECUTION_SUBAGENT | TASK_SPECIALIST_SUBAGENT | NAMED_AGENT
artifact_id
artifact_version
owner
```

Risk trimming changes the depth of the nine TASK-006 information classes, not the identity fields. `TASK_SPECIALIST_SUBAGENT` additionally carries the eight-part temporary `specialist_contract`; it never creates a persistent personality. `owner` is the sole owner of the current artifact version, while primary-agent synthesis and final responsibility do not automatically change ownership.

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
2. Confirm capability, task authority, platform permission, prohibited actions, and external effects.
3. Build one self-contained task packet from [`references/packet-template.md`](references/packet-template.md).
4. Require the executor-specific handshake when applicable, then continue the same executor without changing the accepted boundary.
5. Inspect the returned artifact and verification material before integrating the result.

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
