# Maintaining waa-agent-delegation

Use this document for human maintenance. Do not link it from `SKILL.md`; it is not runtime instruction.

## Invariants

Every change must preserve these rules:

1. The primary agent already intends an actual delegation before this Skill activates.
2. Complexity alone never requires delegation.
3. Named-agent availability never implies authorization.
4. Capability availability, compatibility, and authorization remain separate checks.
5. Delegation cannot expand permissions or bypass platform controls.
6. `ACCEPTED` means contract comprehension only.
7. Independent evaluation remains optional and never starts automatically.
8. The primary agent remains responsible for synthesis, verification, user communication, and the integrated outcome without automatically owning each delegated artifact version.
9. Root `SKILL.md` is the single semantic source across platforms.
10. Real installation is a separate manual action.
11. `assembly_type` is exactly one of `EXECUTION_SUBAGENT`, `TASK_SPECIALIST_SUBAGENT`, or `NAMED_AGENT`; lowercase aliases are invalid.
12. Every packet carries `task_packet_version`, `task_id`, `assembly_type`, `artifact_id`, `artifact_version`, and one artifact-version `owner`, including low-risk packets.
13. TASK-006 has nine locatable information classes; `TASK_SPECIALIST_SUBAGENT` has an eight-part temporary `specialist_contract`.
14. Failure labels remain uppercase and verbatim; translated, shortened, or invented aliases are invalid.
15. Primary-agent final responsibility does not silently change artifact-version ownership.
16. A mandatory reply prefix is packet-recorded with exact text, source, and executor applicability; an executor never infers it from an identity document that does not govern that executor, and a packet cannot cancel a directly applicable higher-priority runtime rule.
17. Every post-execution completion message starts with `ACCEPTED / <DONE | PARTIAL | FAILED>`, and the repeated `delivery_status` matches it.
18. Every completion return includes `Definition conflict`, using `none` or identifying both conflicting provisions for primary-agent reception.
19. Every packet declares exactly one `input_boundary`; missing input policy is a packet defect, not an executor-selected default.
20. Every packet explicitly declares version-control and release/deploy boundaries without creating authority, and no packet may waive the credential-placement prohibition.
21. Evaluation statuses obey the shared first-line purity rule; `RECORD_CONTRACT_ANOMALY` remains an evaluator-only record status outside the four root-cause labels.
22. A `PARTIAL` return reports the safest next action separately from the handoff recipient, including when the obvious resumption point would compound the partial state.
23. A `FAILED` return may still require a safe recovery or diagnostic action when execution may have left residual state or blind retry could cause harm; delivery failure does not prove execution-state cleanliness or imply a valid partial deliverable.
24. A delivery made in a form other than the requested form, because the requested form would have been false, is `PARTIAL` only when the substitute stays within the packet boundary; it names the unproduced form, the reason, and the substitute, and never returns `DONE` or creates authority to change artifact shape or scope.

## Placement rule for protocol text

When editing this Skill or any resident executor definition, classify each sentence before writing it. Output form — the field names, field order, and status placement an executor must emit — lives only in this Skill's protocol and reaches the executor through the task packet; a copy inside a resident definition drifts, and the definition's own precedence clause makes it lose to the protocol anyway. A list of fields an executor must check for is a detection duty, not an output form: it may stay in a definition, but it drifts the same way, so keep a check that proves the two sets still match. A floor that must survive a defective packet lives at both ends. How a role thinks lives only in its definition. One exception: the form needed to report a defective packet has to survive one, so the first-line status contract stays in both.

This rule spans all three executor types. An execution subagent or a task specialist has no resident definition — everything it must emit reaches it through the packet, and a `specialist_contract` embedded in a packet is packet content, not a resident definition, so no second copy can exist for them by construction. The rule bites wherever resident text exists: today the named-agent definitions; tomorrow any new resident surface. A definition that supplies a default the protocol says to treat as a packet defect is not a safety net; it silences the report.

## Change the smallest responsible layer

| Change type | Primary file |
| --- | --- |
| Trigger or exclusion behavior | `SKILL.md` frontmatter description |
| Stable delegation sequence or responsibility | `SKILL.md` |
| Task packet, prompt, return, or failure contract | `references/protocol.md` |
| Cross-platform discovery or shared fact | `references/platform-compatibility.md` |
| Native platform behavior | Corresponding `references/platform-*.md` |
| Human workflow or repository explanation | `README.md` or this file |
| Regression evidence | `evals/cases.md` |
| Machine-readable regression fixture | `evals/trigger-cases.json` |
| Codex UI wording | `agents/openai.yaml` |

Do not duplicate the same rule in multiple runtime files unless one occurrence is a short routing reminder and the other is the authoritative detail.

## Iteration loop

1. Reproduce a real problem or capture a credible forward case in `evals/cases.md` and, when applicable, `evals/trigger-cases.json`.
2. Add or update the case before changing the intended behavior.
3. Identify whether the defect is routing, protocol, platform mapping, or result reception.
4. Make the smallest change that fixes the mechanism.
5. Run structural validation, link checks, YAML parsing, invariant searches, and affected cases.
6. Record the observed behavior and remaining uncertainty.
7. Review the diff for accidental permission expansion, named-agent activation, automatic evaluation, or responsibility transfer.
8. Commit only the files belonging to the change.

Do not add a fixed total score, KPI, or automatic review loop. The purpose of cases is to reveal design defects and prevent regressions.

An absence-oriented invariant check is not evidence on its own. Before recording a zero match as passed, make it able to fail: cite a prior nonzero count produced by the same matcher, run it against a known positive, or enumerate the category and inspect the result. Also confirm that the intended live target or extracted range is nonempty. For an empty diff or unchanged hash, verify the intended inputs and limit the claim to their identity; neither result proves semantic correctness. Record a check that cannot be made falsifiable as `unverified`. Searching only for wording chosen by the maintainer is the cheapest form of this error, because absence of that wording is not absence of the underlying condition.

## Refresh platform evidence

- Prefer official product documentation, official source repositories, changelogs, and direct current-version runtime evidence.
- Record the access date for material platform claims.
- Separate documented behavior from local-machine observations.
- Preserve unresolved documentation conflicts under `PLATFORM_UNKNOWN`.
- Do not turn an undocumented low-level tool schema into a stable contract.
- Re-check installation paths and permission behavior before changing manual installation guidance.

## Validation checklist

- `SKILL.md` frontmatter contains only `name` and `description`.
- The directory name matches the Skill name.
- `agents/openai.yaml` parses and matches the current Skill purpose.
- Every runtime reference is linked directly from `SKILL.md`.
- Every local Markdown link resolves.
- Simple work and delegation discussions remain negative cases.
- Named agents require an explicit authorization basis.
- Capability availability is never phrased as authorization.
- The four failure returns remain sufficient; additions require a demonstrated decision need.
- Failure returns preserve the exact uppercase labels, especially `CAPABILITY_OUT_OF_SCOPE` and `PLATFORM_PERMISSION_BLOCKED`.
- Evaluation status blocks never use a `status:` prefix; `anomaly` and `subtype` follow the bare first-line status token.
- `RECORD_CONTRACT_ANOMALY` remains outside the four-label table and is unavailable to ordinary executors.
- The first status token has no discretionary preamble, separator, or markup; any applicable mandatory prefix is packet-recorded with exact text, source, and executor applicability, while a directly applicable higher-priority runtime rule still controls a defective packet.
- The combined single-turn return is limited to low-risk `EXECUTION_SUBAGENT` packets that explicitly permit handshake omission.
- Both combined and two-stage completion returns start with `ACCEPTED / <DONE | PARTIAL | FAILED>`, and the repeated `delivery_status` matches.
- Every `PARTIAL` completion identifies the safest next action separately from the handoff recipient and warns when the obvious resumption point is unsafe.
- Every `FAILED` completion discloses residual-state uncertainty and supplies a safe recovery or diagnostic action when `not applicable` would make a harmful retry possible.
- Every completion delivered in a form other than the requested form is `PARTIAL`, carries the three `Requested-form substitution` disclosures, and does not use substitution to widen artifact shape or scope.
- Every `Taken on faith` item is reconciled in the completion return.
- Every completion return reports `Definition conflict: none` or identifies both conflicting provisions without resolving them.
- Every packet contains one exact `input_boundary`, and every out-of-list read is either prohibited by `LIST_ONLY` or individually disclosed under `LIST_IS_START_DISCLOSE_BEYOND`.
- Every packet declares version-control and release/deploy boundaries with exact targets; omission blocks execution, and the credential floor has no packet exception.
- The three exact `assembly_type` values have zero lowercase aliases in active source.
- Every packet template contains `assembly_type`, including the low-risk `EXECUTION_SUBAGENT` path.
- All nine TASK-006 classes and all eight AGT-014 specialist sections are locatable.
- `owner` stays the sole owner of the current artifact version through reception and integration.
- All YAML and JSON files parse.
- The primary agent's final responsibility remains explicit.
- No installer, hook, persistent Agent definition, or real platform configuration has appeared accidentally.

## Current regression watch

Historical narrative observations report safe stopping but failed exact-label compliance for missing Subagent interfaces and denied sandbox approvals; no reproducible run record is stored in this repository. Keep Cases 7A and 7B and their `trigger-cases.json` regression-watch entries in every trigger or protocol revision. Do not report semantic or exact-label compliance as verified until a fresh run records its method, date, result, evidence path, and the verbatim `MISSING_CAPABILITY` or `PLATFORM_PERMISSION_BLOCKED` return.

## Git discipline and rollback

- Inspect repository status before staging.
- Stage explicit paths; do not use `git add .` when ownership is uncertain.
- Keep commits focused on one behavioral or evidence change.
- Use Git history as the rollback boundary.
- Add a changelog only when versioned consumers or releases make curated migration history more useful than the commit log.

## Public release checklist

- Run the structural validator, YAML parser, Markdown parser, and local-link check.
- Confirm the current tree and new commit contain no credentials, private keys, local absolute paths, internal-only instructions, or confidential artifacts.
- Keep named-agent examples generic unless a public integration requires an exact published identifier.
- Confirm README installation guidance matches current public platform behavior and never implies automatic installation.
- Confirm repository description, topics, license, default branch, and visibility match the intended release.
- Re-run the negative and boundary cases before claiming a behavioral regression is fixed.
