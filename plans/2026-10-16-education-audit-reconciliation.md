# Reconcile the education and learner-journey audits

Approved scope: reconcile umbrella #114/#115/#116/#124 with retained evidence and recommend closure or bounded follow-ups. No lesson expansion, new dependencies or automatic closure of audit issues. Docs #99 remains a separate review.

1. Read the exact issue criteria, earlier reconciliation and later source/runtime/browser reports. Capture issue/PR states and immutable source identities; distinguish reviewed/merged work from open proposals.
2. Write a criterion-level matrix in `audit/2026-10-education-audit-reconciliation/REPORT.md`, backed by `criteria.json`, `sources.json` and retained GitHub snapshots. Explain each pass, partial, skipped, unknown and remaining gap without treating source inventories as execution or AI trials as learner results.
3. Reuse existing follow-up issues. File a new bounded issue only for a concrete uncovered gap; record at most five priorities with explicit completion evidence. Recommend which audits can close after review and which must remain open.
4. Add the report to `README.md`. Verify evidence hashes, local links, criterion coverage, issue ownership and a deliberately incomplete matrix. This docs-only change needs no website rebuild or fresh emulator run.
5. Commit, push and open one review PR. Link it from the audit issues and parent epic with clear recommendations, leave closure for acceptance, then remove the temporary worktree and helper files after verifying remote retention. Preserve unrelated README/work changes in the main checkout.
