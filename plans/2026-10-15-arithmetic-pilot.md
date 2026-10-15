# Working It Out pilot

Continue umbrella #114/#115/#124 after the approved Boolean pair. Baselines:
website `3c4e6f6c29d3b65ee92af8f8a34989c932fe939f`; docs
`df7c2e5` (resolve full identity in the report). Preserve unrelated checkouts.

1. Read all four Working It Out pages and the current pseudocode convention.
   Reproduce the negative-floor wording error and inspect remainder, zero, ties,
   expression order and assignment assumptions. Deduplicate and file findings.
2. Edit only `working-it-out/index.mdx` and `unit-01.mdx` through `unit-03.mdx`.
   Recall knowledge locally, show same-precedence order, add closed prediction
   checks, correct floor wording, bound remainder to non-negative whole inputs
   with a positive divisor, and state a local non-negative half-up ROUND rule.
   Preserve layouts and correct existing outputs. Link optional existing BASIC
   and Pattern examples, with no compulsory language course.
3. Clarify `specifications/pseudocode.md` where these conventions are needed.
   Add `audit/2026-10-arithmetic-pilot/verify-arithmetic.py`, using the maintained
   ROM transport. Compare actual Spectrum arithmetic, INT and assignment with
   independent expected values. Pseudocode is not a target language. Keep all
   failures, identities and limits in REPORT; separate learner and assessor sheets.
4. Add `scripts/verification/arithmetic-pilot.mjs`: capture baseline and after
   for overview/three units at 1440 and 390, verify rendered worked results,
   keyboard prediction answers and optional link/Back. Run the after assertions
   against the baseline as a known-red control. Run build, repository checks,
   Vale/Ruff and bounded design detection. Inspect captures in one batched pass,
   with at most one repair/confirmation pass.
5. Update `audit/2026-10-foundations-coverage.md`, retaining evidence boundaries
   and selecting the next bounded gap from actual text. Push paired draft PRs,
   link findings and parents, verify remote retention, and remove task worktrees,
   copied tooling and processes. Do not claim learner outcomes or close parents.
