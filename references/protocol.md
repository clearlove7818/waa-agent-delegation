# Delegation Protocol

Use this reference to construct a self-contained, risk-sized task packet. Do not force every task into a large fixed form.

## Core contract

Express enough of the following for the executor to act without reconstructing the primary conversation:

- Why delegation is valuable for this task.
- The single outcome and who owns it.
- The objective and concrete deliverables.
- The minimum necessary context and trusted evidence.
- Scope, permissions, prohibited actions, and external effects.
- Required capabilities, prohibited capabilities, exceptions, and compatibility state.
- Quality standards and verification requirements.
- The expected return shape.
- Failure return and handoff target.
- Whether an `ACCEPTED / BLOCKED` handshake is required.
- How the primary agent will receive, check, and synthesize the result.

For low-risk, reversible work, compress related fields into a short brief. Add explicit evidence, permissions, checkpoints, and handshake requirements as risk or ambiguity increases.

## Executor selection

### Execution subagent

Choose this executor for a bounded task that does not require a special identity or durable specialist configuration.

```text
Purpose: <why delegation is useful>
Outcome: <one inspectable result>
Task: <bounded work>
Context and evidence: <minimum trusted inputs>
Boundary: <scope, permissions, prohibitions, external effects>
Quality and verification: <acceptance evidence>
Return: <result, evidence, changes, checks, concerns>
Failure and handoff: <defined failure plus recipient>
```

### Task-specific specialist subagent

Choose this executor when the task needs temporary expertise or a restricted tool/capability profile. Define a task contract, not a personality.

```text
Specialty required: <task-specific expertise>
Purpose and outcome: <why this specialist is useful and the single result>
Deliverables: <concrete outputs>
Inputs and evidence: <authoritative sources>
Allowed capabilities and tools: <minimum set>
Prohibited capabilities and actions: <explicit exclusions>
Compatibility and permission state: <proven, unknown, or blocked>
Quality and verification: <checks and evidence>
Return, failure, and handoff: <result contract>
```

### Authorized named agent

Use this form only after authorization and selection are established outside the task packet.

```text
Authorization basis: <user selected the agent, or authorized selection and primary agent chose it>
Named agent: <exact available identifier>
Purpose and outcome: <bounded delegated result>
Task contract: <deliverables, evidence, boundary, quality, return>
Permission reminder: <no new authority is created by naming the agent>
Failure and handoff: <defined failure plus primary agent>
```

If the authorization basis cannot be stated concretely, do not use the named agent.

## Optional acceptance handshake

Require this before execution when the task has material ambiguity, external effects, costly work, sensitive permissions, or a specialized contract:

```text
Return exactly one before execution:

ACCEPTED
- Restate the outcome, boundary, required evidence, and return contract briefly.
- Identify any platform approval that may still be needed.

BLOCKED
- State the missing or conflicting contract element.
- State why execution cannot begin safely.
- State the minimum information or decision needed from the primary agent.
```

`ACCEPTED` proves only that the executor understood the packet. It does not prove capability, authorization, execution, verification, or success.

## Completion return

Ask successful executors to return compact evidence rather than a long narrative:

```text
Outcome:
Deliverables or changes:
Evidence:
Verification performed:
Concerns or unknowns:
Handoff to primary agent:
```

Keep detailed artifacts in files when that reduces context loss; return their exact paths and a short summary.

## Failure returns

After any mandatory higher-priority host prefix, start every failure return with a task-status line containing exactly one of the following uppercase labels, copied verbatim. Do not translate, lowercase, abbreviate, or create a semantically similar alias. In particular, use `CAPABILITY_OUT_OF_SCOPE` for an available but unauthorized capability and `PLATFORM_PERMISSION_BLOCKED` for a sandbox, policy, or approval barrier.

Classify the root cause before choosing the label:

| Root cause | Exact label |
| --- | --- |
| Missing critical task input or conflicting contract | `BLOCKED` |
| Required capability absent, incompatible, or unreliable | `MISSING_CAPABILITY` |
| Capability available but outside rules or authorization | `CAPABILITY_OUT_OF_SCOPE` |
| Platform policy, sandbox, or approval state prevents execution | `PLATFORM_PERMISSION_BLOCKED` |

Do not collapse the last three conditions into generic `BLOCKED`.

```text
BLOCKED
Reason: <missing input or contract conflict>
Attempted: <relevant safe checks>
Needed: <minimum resolution>
Handoff: <primary agent or specified recipient>
```

```text
MISSING_CAPABILITY
Capability: <required capability>
Evidence: <absence, incompatibility, or unreliable behavior>
Alternative: <safe viable option, if any>
Handoff: <primary agent>
```

```text
CAPABILITY_OUT_OF_SCOPE
Capability: <available capability>
Boundary: <rule or authorization that excludes it>
Needed authority: <specific approval, if appropriate>
Handoff: <primary agent>
```

```text
PLATFORM_PERMISSION_BLOCKED
Operation: <blocked action>
Platform evidence: <sandbox, policy, or approval result>
Safe progress retained: <artifacts or checks already completed>
Needed platform change: <specific approval or environment change>
Handoff: <primary agent>
```

## Primary-agent reception

Before accepting the result:

1. Match each deliverable to the task packet.
2. Inspect cited artifacts, commands, outputs, or sources.
3. Confirm the executor stayed within scope and authority.
4. Reproduce or independently verify checks in proportion to risk.
5. Resolve conflicting subagent claims instead of forwarding them unchanged.
6. Record material limitations and unknowns.
7. Synthesize the final result under the primary agent's responsibility.
