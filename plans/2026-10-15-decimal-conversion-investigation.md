# Spectrum decimal-conversion investigation

Investigate docs #63 before further curriculum qualification. Baseline docs
b9bb712878c8a739d866ef8ad96a8be7c0232fad. No learner is available. Preserve existing
checkouts; use an isolated docs worktree and disposable copies of reference source.

1. Reproduce LET x=0.5 / 1/2 / 0.75 / 3/4 / 0.1 / 1/10 on the configured native
   binary, recording raw bytes, ROM and executable hashes and printed output.
2. Build existing vendored Fuse 1.7.0 and libspectrum 1.6.0 outside the reference
   tree using installed libraries, without adding dependencies. Use a headless
   bounded run with the same ROM and documented inputs or a validated pre-execution
   snapshot; do not use an after-result snapshot as independent execution proof.
3. Compare raw storage and executed paths. If engines differ, find the first
   relevant divergence; if they agree, trace ROM input conversion and reconcile
   the primary manual without inferring a defect merely from disagreement.
4. Retain `audit/2026-10-decimal-investigation/REPORT.md`, a reproducer and evidence
   identities/results. Keep firmware and third-party binaries out of public repos.
   Update #63 and umbrella #114/#115/#124 with actual findings and remaining limits.
5. Make only a verified, necessary correction in its owning repository. Consult
   emulator rules/decisions and agree design before any nontrivial behaviour change.
   Native library code changes would require the Rust skill and relevant tests.
6. Commit/push focused docs (and any separately authorised fix), verify retention,
   then stop owned processes and remove worktrees, build copies and temporary
   ROM/snapshot material. Do not close #63 without resolving the specific question.

This serves Spectrum launch-hardening. No changes to vendored reference code,
new dependency, architecture, public lesson or broad accuracy campaign is proposed.
