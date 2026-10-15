# Gates and the Adder pilot

Continue umbrella #114/#115/#124 after approved binary/hex #730/#72. Baselines:
website 95695874b13428e7e8da1c1e1b037a4bed8f1161; docs
945fb47017e34d212979b37442a274ff2a99459e. Preserve unrelated checkouts.

1. Read all four Gates and the Adder pages, LogicCircuit/TruthTable components,
   the Zilog ALU/register description and primary gate specifications. Record
   manufacturer provenance in the reference library before derived hardware
   claims. Deduplicate/file confirmed model/physical and carry-interpretation gaps.
2. Edit only `gates-and-the-adder/index.mdx` and units 1–3: explain stable Boolean
   model and its limits, local prerequisites, sum+2×carry reconstruction,
   zero carry-in assumptions, a worked three-column trace and retained versus
   discarded final carry. Preserve correct tables/circuits and shared layout. Correct the reproduced
   initial-row event-order gap in `TruthTable.astro` by rendering the linked
   zero-input row initially; preserve explicit overrides and non-linked tables.
   Add closed predictions and useful optional existing system connections.
3. Add `audit/2026-10-gates-adder-pilot/verify-adders.py` and audit-only Z80 fixture:
   execute half/full-adder arithmetic and all 64 pairs of three-bit inputs; compare
   actual results to an independent ripple model and whole-number sums. Include
   selected byte ADD/carry observations without claiming a physical gate layout.
4. Add `scripts/verification/gates-adder-pilot.mjs`, with explicit semicolons.
   Verify actual keyboard controls, outputs and table row synchronisation for all
   AND/OR/XOR/NOT, half-adder and full-adder input cases; check rendered trace,
   static ripple scope, disclosures and optional links at 1440/390. Keep baseline,
   known-red and after evidence, including failures. Build, run repository checks,
   Vale/Ruff, syntax/semicolon checks and bounded visual inspection.
5. Retain separate learner/assessor sheets and report with source/environment
   identities and actual scope limits. Update coverage/next work; push source and
   lesson/evidence drafts, link issues, verify retained heads/hashes, stop task
   processes and clean all worktrees/copied dependencies/scratch evidence.
