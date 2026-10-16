# Foundations publication and navigation sweep

The recent readiness pass covered five changed units. Check delivery of the
complete authored Foundations surface without adding exercises or widening the
curriculum. This continues #114/#124 while learner observations remain unavailable.

1. Inventory exactly 39 unit MDX files and ten module overviews at immutable
   website main. Record paths, hashes and authored Question counts in
   `audit/2026-10-foundations-publication/source.json`. Read the shared Question
   component and inspect the source inventory before trusting those expectations.
2. Add `audit/2026-10-foundations-publication/verify-live.mjs`. At 1440×900 and
   390×900, visit all 49 published routes, require successful HTTP, a visible H1,
   no document overflow/page errors, exact Question counts and keyboard-openable
   answers. Retain response identities and positive per-route results. Do not
   add a whole-site accessibility claim or screenshots of every repeated page.
3. Collect actual root-relative links inside each main region. Deduplicate and
   check HTTP success and fragment IDs on their target pages with bounded requests.
   Treat any failure as a candidate until reproduced and checked against source.
4. Run an intentionally incorrect first-page Question expectation to show the
   live verifier can fail; reject missing-route/viewport evidence in validation.
5. Reproduce and fix a concrete blocker first if found, with its own issue and
   focused verification. Otherwise write the bounded REPORT.md, source/result
   identities and SHA256SUMS. Link the snapshot from README/coverage, validate,
   commit and push a draft docs PR, update #114, and remove temporary copies.

Exact files: the plan above; the new audit directory's source.json,
verify-live.mjs, results.json, REPORT.md, validation.json, SHA256SUMS and any
explicitly labelled failure/control evidence; README.md and
`audit/2026-10-foundations-coverage.md` for navigation. No dependency, shared
component, design, native-emulator, VoiceOver or physical-touch change is planned.
