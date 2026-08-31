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

## Usage

Use this Skill only after the primary agent has already decided that an actual delegation is useful and authorized.

1. Select exactly one executor type.
2. Check capability, authority, platform permission, prohibited actions, and external effects.
3. Build one self-contained packet from [`references/packet-template.md`](references/packet-template.md).
4. Use the applicable handshake and continuation mechanism.
5. Inspect returned artifacts and evidence before integration.

[`references/protocol.md`](references/protocol.md) is authoritative when any summary, platform mapping, or packet rendering differs from it.

## Install with CC Switch

This repository does not include or run an installer. Configure the repository source through CC Switch; the repository itself does not modify the shared Skill link.

### CC Switch

Add the public repository root and select the `main` branch:

```text
https://github.com/clearlove7818/waa-agent-delegation
```

Use the repository root URL without `/tree/main`, `/blob/...`, a trailing slash, or a file path. The root `SKILL.md` is the shared semantic entry point.

### Shared Skill location

CC Switch maintains the shared source for all supported platforms at:

```text
~/.agents/skills/waa-agent-delegation/
```

The repository does not create or modify that link. After switching the source, load the root `SKILL.md` and use the active runtime map under [`references/`](references/) for native delegation and continuation behavior.

## Version checkpoints and rollback

Git history is the iteration record. Verified stable nodes use annotated tags named `checkpoint-YYYY-MM-DD-<slug>`; this README does not duplicate the full commit log.

The current post-streamlining checkpoint is `checkpoint-2026-08-31-post-streamlining`, pointing to commit `8e5c75a`. It preserves the shared delegation flow and four platform maps after the cleanup. Structural and document checks passed for this checkpoint; it does not claim a new four-platform behavioral forward run.

Inspect the history or create a recovery branch without moving `main`:

```bash
git log --oneline --decorate
git switch -c restore/<name> checkpoint-2026-08-31-post-streamlining
```

## Contributing

Maintenance rules live in [`MAINTAINING.md`](MAINTAINING.md). Contributions are welcome through [`CONTRIBUTING.md`](CONTRIBUTING.md). Report security-sensitive issues according to [`SECURITY.md`](SECURITY.md).

## License

The source is publicly visible, but no open-source license is granted. See [`LICENSE`](LICENSE).
