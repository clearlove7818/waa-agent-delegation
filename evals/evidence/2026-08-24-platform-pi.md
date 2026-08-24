# Pi platform evidence — 2026-08-24

## Scope

This record covers Pi Skill discovery and the availability boundary for delegation. It does not claim that every Pi installation, extension, package, or version preserves the same behavior.

## Direct local observations

- `command -v pi` resolved to `/opt/homebrew/bin/pi`.
- `pi --version` returned `0.84.2`.
- `pi --help` exposed `--skill <path>`, `--extension <path>`, `--no-skills`, and `--no-extensions`; it listed built-in tools but no built-in subagent tool.
- `pi list` returned `No packages installed.` in the local environment; its startup lock attempt was denied by the sandbox, so package enumeration is local evidence from the command result, not a claim about another environment.
- `/Users/sanjin/.pi/agent/skills/waa-agent-delegation` is a symbolic link to the shared `/Users/sanjin/.agents/skills/waa-agent-delegation` checkout. The repository and installed target compared identical while excluding Git and operating-system metadata.
- The Claude Code path is also a symbolic link to the same shared target, consistent with ccswitch-managed shared-path routing.

## Decision

Pi is supported as a Skill host through the ccswitch-managed shared target. Pi-specific delegation dispatch is supported only through a currently loaded extension or package that passes the platform gates and proves the required handshake; Pi core alone returns `MISSING_CAPABILITY` for an actual delegation request.
