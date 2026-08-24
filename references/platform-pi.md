# Pi Runtime Map

Discovery status: Pi 0.84.2 was installed locally and checked on 2026-08-24. ccswitch-managed installations may point Pi and Claude Code at the same shared Skill target. Pi also supports explicit `--skill <path>` loading and trusted project skill locations. Automatic relevance, project trust, and extension loading remain runtime conditions, not authorization.

Use this mapping only when the active harness is Pi CLI (`pi`).

## Before dispatch

1. Confirm the active Pi version and currently loaded extensions or packages. Do not infer a delegation surface from Skill discovery alone.
2. Confirm the project is trusted before relying on project-local `.pi` resources or `.agents/skills`.
3. Confirm that an extension or package actually provides the required subagent surface. Pi core does not include subagents.
4. Treat ccswitch shared-target management as installation plumbing only; it does not grant delegation authority or prove the extension handshake.

## Map semantic actions

| Delegation action | Pi behavior |
| --- | --- |
| `EXECUTION_SUBAGENT` | Use the currently loaded extension or package that provides a bounded subagent tool. Pi core alone is `MISSING_CAPABILITY`. |
| `TASK_SPECIALIST_SUBAGENT` | Use a task-scoped packet and the active extension mechanism only when it preserves the specialist contract and return form. Do not create a persistent Agent definition automatically. |
| `NAMED_AGENT` | Select an exact currently available Pi Agent definition only after current-task authorization. User-level and project-local scopes are separate; visibility is not authorization. |
| Required handshake | Require the active extension to prove a parent-visible pre-execution `ACCEPTED` gate followed by preserving continuation. An immediate child-process result or merged response is not automatically a handshake; otherwise return `MISSING_CAPABILITY`. |
| Run concurrently | Use only the active extension parallel mode when the work is independent, the packet permits it, and each artifact version has one owner. |
| Inspect or stop work | Use only the active extension controls. A child-process abort or timeout does not prove external effects were rolled back; preserve residual-state uncertainty. |

Pi core deliberately leaves subagent orchestration to extensions, packages, tmux, or other user-managed mechanisms. Do not hard-code any extension low-level tool schema into the shared protocol.

## Permission behavior

- Pi project-local Skills and Agent definitions require the project to be trusted before they are usable.
- Pi core has no built-in subagent approval contract; an extension or package may add its own gates.
- Map an absent or incompatible subagent extension to `MISSING_CAPABILITY`.
- Map an available extension action that the packet did not authorize to `CAPABILITY_OUT_OF_SCOPE`.
- Map a project-trust or extension approval denial to `PLATFORM_PERMISSION_BLOCKED`.

Place the exact uppercase label as the first status token on the first line of the failure return. Use a mandatory prefix only when the task packet records its exact text, governing source, and applicability to this executor. Never infer a prefix from Pi’s resident `AGENT.md` or an extension prompt that does not govern the executor.

## Result reception

Inspect child output, changed files, commands, and evidence from the primary Pi session. Re-run proportionate checks in the primary context. An isolated child process or successful tool return is not final acceptance, and it does not transfer artifact ownership or final responsibility.
