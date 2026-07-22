# Contributing

Thank you for helping improve `waa-agent-delegation`.

## Before opening a change

- Start from a reproducible delegation, routing, permission, platform, or result-reception problem.
- Preserve the boundary that the primary agent already intends an actual delegation before this Skill applies.
- Keep capability availability, compatibility, authorization, and platform permission as separate checks.
- Do not add automatic named-agent activation, permission expansion, independent evaluation, or a review loop.

## Submit a focused change

1. Open an issue for substantial behavior or platform changes so the scope and evidence can be discussed.
2. Add or update a case in [`evals/cases.md`](evals/cases.md) before changing intended behavior.
3. Make the smallest change in the responsible runtime or reference file.
4. Run the checks in [`MAINTAINING.md`](MAINTAINING.md).
5. Describe the problem, evidence, changed behavior, checks run, and remaining unknowns in the pull request.

Platform claims must cite current official documentation, an official repository, current product files, or reproducible runtime evidence.
