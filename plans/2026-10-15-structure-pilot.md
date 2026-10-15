# Structure pilot

Continue umbrella #114/#115/#124 after merging semicolon PR #726. The arithmetic
pair #725/#69 remains unmerged and is not treated as approved. Work from current
main in isolated worktrees; preserve unrelated checkout changes.

1. Read Structure overview and all four units, current pseudocode specification
   and the Spectrum manual chapters on arrays and subroutines. Distinguish
   correct existing call/debug traces from gaps in bounds and copied-parameter
   examples. Deduplicate and file the confirmed bounded finding.
2. Edit only Structure overview, unit 1 and unit 3: recall used knowledge locally,
   show empty-list/bounds checks and copied numeric parameters with a caller
   trace. Preserve good unit 2/4 examples. Add optional existing system/Pattern
   links only where they explain a useful target distinction.
3. Add `audit/2026-10-structure-pilot/verify-structure.py`: exercise actual Spectrum
   fixed arrays, bound failures and shared GO SUB state through ROM entry. Keep
   target differences explicit; no pseudocode interpreter or new dependency.
   Add separate learner/assessor tasks, source/version identities and REPORT.
4. Add `scripts/verification/structure-pilot.mjs` with explicit semicolons. Check
   rendered outputs, call/debug tables against independent calculations, closed
   keyboard questions and optional links/Back on all five routes at 1440/390.
   Retain baseline, known-red and after records. Run build, repository checks,
   Vale/Ruff, semicolon parsing and bounded design detection. Inspect all after
   captures in one batched pass, allowing at most one correction/confirmation.
5. Update only relevant coverage-map status and next work, keeping the arithmetic
   draft status explicit. Push paired drafts and update parent/finding issues.
   Verify remote retention and hashes; stop task processes and clean worktrees,
   copied dependencies, symlinks and scratch output before reporting.
