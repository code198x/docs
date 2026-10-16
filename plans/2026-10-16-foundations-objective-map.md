# Foundations per-unit objective and prerequisite map

Continue umbrella #114 after approved docs #83 merges. Keep the independent
system entry points and current curriculum structure. This is a source review,
not a rewrite or a learner trial.

1. Pin website source and read all ten module overviews and 39 authored units.
   Retain paths, titles, hashes and source excerpts supporting each mapped goal.
2. Create `audit/2026-10-foundations-objectives/units.json` and `MAP.md`.
   Map each unit's concrete learning goals, knowledge used, local explanations,
   optional support links and present understanding checks. Distinguish stated
   learning goals from reviewer inference; knowledge is not required attendance.
3. Reconcile with existing pilot evidence and specifications in `REPORT.md`.
   The Working the Bits overview still repeats claims corrected in units 2/4
   and requires prior attendance. File the deduplicated overview finding; prepare
   a small correction in website `src/content/curriculum/foundations/working-the-bits/index.mdx`
   and the stale From Source to Silicon tagline/skills in `src/content/modules/foundations.yaml`.
   Preserve all catalogue order/requires data.
   Reuse existing explanations, add no behaviour/dependency, and verify the built
   page text plus website production/content checks.
   Separate complete inventory coverage from conceptual/example verification and
   learner effectiveness. Deduplicate and file only specific evidenced gaps.
4. Verify exact source-set coverage, hashes, source excerpts, positive counts,
   dependency targets and local links. Deliberately remove a unit/change a hash
   to confirm validation fails. Run prose and whitespace checks.
5. Link README and Foundations coverage, commit and push a draft PR. Update #114
   with findings, limits and next bounded work. Verify remote retention and remove
   the task worktree and temporary files; preserve unrelated original changes.

Exact verification code belongs in `verify.py` beside the retained records.
Do not treat source metadata or a green inventory check as execution evidence.
