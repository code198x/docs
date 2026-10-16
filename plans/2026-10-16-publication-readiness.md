# Publication readiness after the fixed-point pilot

Verify the approved changes on the public site before selecting more lesson work.
This is a bounded publication check under umbrella #114/#115/#124, not a new
curriculum design or learner trial.

1. Confirm website #764 and docs #90 merged at their approved heads; retain the
   resulting main identities and the deployment result.
2. Run the existing fixed-point browser and contrast verifiers against
   https://code198x.com at 1440 and 390 pixels, using the accepted model file.
   Retain actual HTTP hashes, keyboard journeys, rendered table and raw scans in
   `audit/2026-10-publication-readiness/`.
3. Verify the four other recently changed Foundations units and the public /try/
   entry at both widths using existing bounded scripts where suitable. Check
   exact required page content, links and outcomes; fail on missing pages/tasks.
   Use a deliberately incorrect expectation to confirm rejection.
4. Reconcile current open findings with these results. Fix only a reproduced
   blocker; otherwise retain VoiceOver/touch and learner limits as outstanding
   evidence needs. Write `REPORT.md`, input identities and a SHA-256 manifest;
   update the coverage navigation to the current readiness snapshot.
5. Validate the retained positive counts, links and hashes, commit and push a
   draft docs PR, update #114, and remove task worktrees/dependency copies.

No new dependency, native execution, audio, screen-reader or physical-device
qualification is planned. Earlier reports retain their original scope.
