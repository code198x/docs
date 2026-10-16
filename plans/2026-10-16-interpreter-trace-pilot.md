# Interpreter trace and evidence boundaries

Continue #114 after approved website #759/docs #87 merge. Keep the teaching change in
From Source to Silicon unit 2, with existing components and notation. A reproduced
narrow trace defect also requires restoring the existing TraceTable scroll design.

1. Read the actual unit, shared specifications, original Spectrum manual and
   earlier source/translation evidence. Search open/closed findings. Distinguish
   correct examples from missing independent prediction and assumed loop knowledge.
2. Check six finite accumulator models: empty, one, three and thousand visits,
   changed initial value and changed increment. Independently check count and
   final value. Reject a reset-inside-loop policy. These are paper-model rules,
   not an interpreter runtime, CPU trace or timing measurement.
3. Keyboard-enter corresponding ROM BASIC programs with the maintained transport.
   Require all output rows, normal completion and unchanged stored program bytes
   across RUN. Repeat one unchanged program, then observe a separately instrumented
   short trace. Preserve line records/tokens and tool/source identities. Run an
   actual reset-inside wrong variant against the intended result; require nonzero.
4. Add two closed prediction/explanation questions and local assignment/loop/output
   recall to `src/content/curriculum/foundations/from-source-to-silicon/unit-02.mdx`.
   Link counted-loop practice optionally. Keep source operations, machine
   instructions and time distinct; qualify the unmeasured opening cost claim.
5. Retain `audit/2026-10-interpreter-trace/` report, prompts, assessor notes,
   models/native/browser results and validator. Update docs README and coverage;
   preserve the full per-unit map's immutable baseline.
6. Reuse installed build assets; run build, repository checks and focused wide/narrow
   output/table/keyboard/link checks. Inspect readable captures; report scoped axe
   results including incomplete records. Use explicit JavaScript semicolons.
7. Repair `src/components/diagrams/TraceTable.astro` so inherited arbitrary word
   breaking cannot split numeric values. Restore natural table display, keep overflow
   in its existing wrapper and make that region keyboard reachable and labelled.
   Record before/after geometry and captures for all seven authored consumers at
   both widths, comparing their cells and keyboard access to the final column.
   The before interpreter check must fail at narrow scrolling; retain the failure.
8. Check source hashes, transcripts, local links, negative controls and manifest.
   Push separate website bug/teaching commits and one docs commit and draft PRs, update #114, verify remote retention,
   stop task processes and remove temporary worktrees/caches. Learner outcomes,
   hardware, screen readers, instruction counts and performance remain unverified.
