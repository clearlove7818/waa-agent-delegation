# Maintaining waa-agent-delegation

Use this document for human maintenance. Do not link it from `SKILL.md`; it is not runtime instruction.

## Invariants

Every change must preserve these rules:

1. The primary agent chooses an actual delegation before this Skill activates; complexity or discussion alone is not enough.
2. Use exactly one executor type. Named-agent availability never grants authorization.
3. Keep capability, compatibility, authorization, and platform permission separate; delegation cannot expand them.
4. Subagents cannot dispatch another Agent/subagent/background/parallel executor or transfer artifact ownership.
5. Packets keep the six identity fields and one exact `assembly_type`; specialists use the temporary eight-part contract.
6. Keep the four uppercase failure labels unchanged. `RECORD_CONTRACT_ANOMALY` is evaluator-only.
7. Completion returns start with `ACCEPTED / <DONE | PARTIAL | FAILED>` and expose evidence, unknowns, and safe continuation when needed.
8. The primary agent remains responsible for reception, verification, synthesis, communication, and final acceptance; packet ownership stays with the artifact-version owner.
9. Evaluation is optional and separately authorized. Root `SKILL.md` is the semantic source; installation is separate.

## Placement rule for protocol text

Keep packet and return forms in `references/protocol.md`; keep only the minimum routing or role guidance in resident definitions. The protocol's defect floor may be repeated where it must survive a defective packet, but do not copy the full forms elsewhere.

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
| Structural conformance of fixture records | `evals/fixture_conformance_runner.py` |
| Codex UI wording | `agents/openai.yaml` |
| Dispatch-time packet rendering | `references/packet-template.md` |

Do not duplicate rules across runtime files. `references/packet-template.md` is the one sanctioned rendering; update its fenced blocks with the protocol and compare them byte for byte.

## Iteration loop

1. Reproduce or capture a concrete defect before changing behavior.
2. Change the smallest responsible layer and keep one semantic source of truth.
3. Keep evidence separate from behavior: `missing evidence` means no forward run, not a pass.
4. Refresh platform facts from official sources or direct runtime evidence; retain unknowns instead of guessing.
5. Run the affected structural and syntax checks, then inspect the diff for permission expansion, named-agent activation, automatic evaluation, or responsibility transfer.

Do not add fixed scores, KPIs, automatic review loops, or checks that cannot fail against a known positive. For `missing evidence`, retain `no forward run of this fixture` in the evidence text.

## Refresh platform evidence

Use official documentation, official source, or direct runtime evidence for platform claims. Record access dates, separate documented behavior from local observation, and keep unresolved conflicts as `PLATFORM_UNKNOWN`. Do not turn an undocumented low-level schema into a stable contract.

## Validation checklist

- `SKILL.md` frontmatter, name, trigger boundary, and direct reference links are valid.
- `agents/openai.yaml`, YAML, JSON, Python syntax, and local Markdown links validate.
- Protocol/template fenced blocks remain byte-identical; the four failure labels and three executor types are unchanged.
- Named agents still require current-task authorization; capability is not authorization.
- Packets retain the identity fields, input boundary, permission boundaries, and credential floor.
- Completion forms, evaluator-only anomaly status, ownership, and primary-agent responsibility remain intact.
- Platform maps do not claim unverified behavior and all four active maps remain reachable.
- Fixtures remain structural records; no runner path judges model behavior.
- No installer, hook, persistent Agent definition, credential, or real platform configuration was added.

## Current regression watch

Keep Cases 7A and 7B and their `trigger-cases.json` regression-watch entries. Until a reproducible run exists, keep their status as `missing evidence` and retain `no forward run of this fixture`.

## Git discipline and rollback

Inspect status before staging, stage explicit paths, keep commits focused, and use Git history as the rollback boundary. Do not reset, overwrite, or clean another contributor's work. Add a changelog only when versioned consumers need migration history beyond Git.

## Public release checklist

- Run structural, syntax, and link checks before publication.
- Confirm no credentials, private paths, internal instructions, or confidential artifacts entered the tree.
- Keep installation guidance manual and platform claims current; re-run affected boundary cases before claiming a fix.
