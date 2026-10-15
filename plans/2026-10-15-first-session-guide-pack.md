# First session guide pack

Draft the agreed learner guide and companion parent/teacher notes before building
public pages. Audience: mixed programming experience, including adults sharing
activities with children or students. The pack must accept further activities
without expanding the first session into a compulsory course.

Baseline: docs 21a12802ceb27052d12006ffd16a60b704d9b249; website
f895b34fc8a316013b15b043d353daa6c24f4c66. Use an isolated docs worktree and
preserve the shared checkout's README/work edits. No website, dependency or
runnable sample changes in this draft.

1. Read current entry pages, Spectrum openings, controls/save behaviour and
   publication evidence. Reuse existing complete programs and lesson explanations.
2. Write `guides/first-session/README.md` for review status, proposed publication
   shape, extension rules and verification limits. Link it from the docs index.
3. Draft `learner-guide.md`, two independent activities under `activities/`,
   `parent-teacher-guide.md`, `session-sheet.md` and `feedback.md`. Keep answers
   in the companion guide. Use stable activity names, actual lesson links and
   optional depth; no age bands, fixed duration, scoring or prerequisites between
   tracks. Provide a paper option when tools cannot be used.
4. Check all relative links and linked public destinations, exact control labels
   against existing components, expected results against maintained samples and
   existing execution records. Run Vale and diff checks. Retain a concise review
   record in the pack README; educational outcomes remain unobserved.
5. Commit and push a focused draft PR, file/track any confirmed new blockers and
   link the parent issues. Verify remote retention, inspect all files, and remove
   the temporary worktree. Public implementation and print-layout verification
   follow content review.
