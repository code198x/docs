# Coverage and Learning Map audit

## Scope

Establish a representative repository-backed baseline for Spectrum BASIC and
assembly, Maths for Games, The Craft, Pattern Library and Vault. Separate
observed coverage, preserved verification and proposed target depth. This does
not commission courses, a site feature or a curriculum restructure.

## Tasks and checks

1. Read `PROJECT.md`, `specifications/curriculum.md`,
   `specifications/craft-coverage.md`, `specifications/maths-for-games.md`, existing
   audit reports and docs issues #277/#278/#117/#10. Inspect current remote
   revisions and preserve unrelated local edits. Verify repository identities.
2. Read representative website lessons/catalogues and maintained samples,
   verification records and helper-tool documentation. Record exact paths,
   revisions, observations and limits in
   `audit/2026-11-05-coverage-learning-map.md`. Check evidence links against Git
   trees; distinguish authored material from current execution and learning.
3. Create `specifications/coverage-learning-map.md` as the authority for the
   cross-curriculum map and evidence rules. Reuse specialist specifications.
   Add its link to `README.md` and a boundary link in
   `specifications/craft-coverage.md`. Review for unsupported completion claims.
4. Create one bounded docs tracking issue, linking #277, #278, existing Craft
   work and the audit. Link it from the specification. Validate local links,
   pinned repository paths and diff whitespace; commit without bypassing hooks,
   push a task branch and open a PR. Read back the issue and pushed files.
5. Confirm the commit exists remotely, inspect tracked/untracked/ignored files
   in the task worktree, then remove it with `git worktree remove`.

## Verification limits

This is a documentation and source audit. It adds no fresh native, browser or
learner evidence. Counts are inventories at a revision, not quality scores.
