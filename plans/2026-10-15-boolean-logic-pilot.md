# Boolean logic pilot and umbrella coverage

Continue umbrella #114/#115/#124. The user's clarification pauses expansion of
the first-session pack only; it does not pause the umbrella audit. No learner is
available, so actual learner evidence remains pending while other work continues.

Baselines: website b1ddbdfc5f72e79e2a97bd6ed42ae8402e25c883; docs
b076c2c0bec0be046480975f130f3770668c5f8d. Use isolated worktrees and copies of
installed tooling; preserve shared checkout edits. No new dependencies, new
interpreter, shared-layout change or guide-pack expansion.

1. Inventory the ten Foundations modules from authored pages and the module
   catalogue. Write `audit/2026-10-foundations-coverage.md` with objectives,
   knowledge used, sampled evidence and explicit remaining gaps. Distinguish
   inventory from a full audit; include the separate game-maths gap.
2. Review `truth-tables/unit-01.mdx` through `unit-03.mdx`, Decisions unit 4,
   `specifications/pseudocode.md` and the Spectrum BASIC manual chapter 13.
   Deduplicate/file confirmed issues: Boolean scope/possible input combinations,
   non-strict AND/OR narrowing and what a truth-table equivalence proves.
3. Add native `audit/2026-10-boolean-logic-pilot/verify-logic.py` and audit-only
   Z80 fixture. Run actual ROM Boolean expressions and De Morgan pairs for all
   four Boolean inputs; compare actual Z80 AND/OR/XOR results. Record numeric
   operand differences, grouping and target evaluation behaviour separately.
   No claim that pseudocode or every language behaves like the Spectrum.
4. Correct only the truth-table overview and three units and align the existing XOR teaching
   with the notation specification. Preserve correct tables and layout. Fix the observed shared TruthTable scroll-focus gap with keyboard focus and an indicator, then check other table consumers. Add
   closed prediction checks and optional existing BASIC replay/Vault-or-Pattern
   connections with no compulsory cross-language attendance. Use existing useful
   routes only; do not fabricate a reference destination to fill the map.
5. Prepare REPORT, LEARNER-TASKS and ASSESSOR, covering prediction, explanation,
   modification, diagnosis and creation. Keep answers separate; no learner scores.
6. Add `scripts/verification/boolean-logic-pilot.mjs`. Check actual table inputs
   and outputs against independent Boolean operations, keyboard answers and
   optional link/Back at 1440×900 and 390×900. Retain live baseline, known-red
   control, after evidence and failures. Run build, repository checks, Vale/Ruff
   and the bounded detector. Inspect rendered desktop/narrow captures in one
   batched pass, with at most one correction pass if needed.
7. Push paired draft PRs, update parent issues with the coverage map and next
   bounded gap. Verify remote retention and evidence hashes; stop task-owned
   processes and remove worktrees/copied assets before reporting.
