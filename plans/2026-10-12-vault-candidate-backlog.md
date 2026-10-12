# Structure the Vault candidate backlog

## Agreed outcome

Keep one structured backlog in the documentation repository. Open a website issue only when a subject is ready to write. Candidates do not create public pages or reserve article URLs.

## Work and verification

- [x] Convert all 2,780 rows in `vault-candidates.md` to `vault-candidates.csv`, preserving each subject, proposed category, reason and referring entry. Assign stable IDs and initialise every row as `needs-triage`. Preserve the existing scope notes in the guide.
- [x] Replace `vault-candidates.md` with the field definitions, triage workflow and issue handoff. Update `specifications/vault.md` and the README index to point to the structured backlog. Use existing issue labels; no new taxonomy.
- [x] Add `scripts/check_vault_candidates.py` to validate IDs, fields, statuses and issue links, and to list candidates by status/category or referring-entry count. Add regression tests in `scripts/test_vault_candidates.py`. Verify malformed data fails and the migration preserves every original row. No bulk issues or automatic deletion.

Delivery: commit one coherent change and open a docs PR. Verify the remote commit before removing this task's worktree and disposable caches. Preserve the unrelated edits in the main docs checkout.

## Verification record

- An independent comparison against the original Markdown at `d22f9eb` confirms all 2,780 subjects, categories, reasons and ordered backlink lists are preserved, in their original row order. IDs run from `VC-0001` to `VC-2780`; every record starts as `needs-triage` with no issue assigned.
- All 7,952 referring-entry references resolve against website main at `d22b8555`; they cover 1,453 distinct entries. Both original scope notes survive in the guide.
- All 10 regression tests pass, including empty-input rejection, CSV quoting, duplicate IDs and subjects, issue URL validation, incomplete triage transitions, missing entry paths and an invalid row outside a selected filter. The two Xenon candidates remain distinct by category.
- Ruff formatting and lint checks pass. Initial checker naming and lint errors were corrected before the successful run.
- Changed documentation links resolve and `git diff --check` passes. No website build is needed: this change creates no public content and changes no site code.
- The issue outline uses the existing website labels `enhancement` and `area:curriculum`. No candidate is promoted by this migration and no writing issue is created.
