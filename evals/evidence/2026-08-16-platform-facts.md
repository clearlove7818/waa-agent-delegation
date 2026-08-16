# Codex and Agy Handshake Platform Facts

## Evidence identity

- Method: owo tested the current Codex collaboration-tool contracts and Agy CLI 1.1.13, then supplied a fact report for the platform maps. On 2026-08-16 owo explicitly confirmed that the report is first-hand test evidence rather than an unverified third-party summary.
- Date: 2026-08-16 local time.
- Source report: `平台握手事实-给Codex更新平台图-2026-08-16.md`, 4,267 bytes, SHA-256 `09e0e116bda5502ca4ec0e10f3964f5f2d9e0bdd205e6ceb81ae062ef93d19c6`.

## Observed platform facts

- Agy scope: version 1.1.13; idle-target continuation through `send_message`; tested idle-lifetime boundaries for an interactive parent process, server or backend restart, headless-wrapper timeout, explicit kill, context-window pressure, and per-turn step limits.
- Codex scope: `spawn_agent` initial dispatch; a final-answer handshake ending the executor's turn; same-target continuation through `followup_task`; queue-only `send_message`; non-final `MESSAGE` handling; `interrupt_agent`; target-lifetime and context-compaction boundaries; and the absence of a transport-imposed response-body prefix.

## Scope limit and reconciliation

These are user-confirmed observations of the tested versions and exposed tool contracts, not a cross-version or cross-installation guarantee. Public documentation and current official source remain the authority for public product status. The report's statement that public Codex multi-agent documentation still described the feature as beta was superseded by the official page reviewed on 2026-08-16, which states that current Codex releases enable subagents by default while the feature can continue to evolve.
