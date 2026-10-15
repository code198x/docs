# Embedded machine latency qualification

Address website #748 after merged website #750/docs #81. Use isolated website
and docs worktrees; preserve unrelated original edits. No dependencies, product
optimisation or invented performance budget.

1. Read the current Meet BASIC first-session lesson, machine/runner code and
   previous browser evidence. Select the unit 1 greeting and exact visible outputs.
2. Add `scripts/verification/embedded-latency.mjs`. Define page navigation separately;
   startup begins at the Run click event and ends when the complete maintained
   greeting plus successful ROM completion is observed and its canvas is painted.
   Changed-code execution begins at a later Run click after a prepared source edit;
   report separately any edit-to-result time beginning with the source input event.
3. Measure five paired cold/warm trials, sequentially, on live production in one
   named Chrome/device/network configuration. Cold means a new browser context with
   empty browser storage/cache and no warmed page/WASM instance; warm means a second
   run on that same page, reusing fetched bytes/initialised module. Do not claim
   cold CDN/DNS/OS caches or mobile network conditions. Retain network/cache evidence,
   individual observations and range/median, not a single reading.
4. Require actual changed text, ROM completion and painted canvas before success.
   Reject stale/empty output and a deliberately missing expected result; retain
   failures instead of converting timeout into a fast timing. Record the sampling
   interval/uncertainty and instrumentation costs. No Core Web Vitals, accessibility
   or learner-effectiveness claim from this bounded task.
   Include an unedited warm rerun before the edited warm run in each pair, so
   startup comparisons use identical programs. This gives fifteen successful
   timed stages: five cold, five warm unchanged and five warm edited.
5. Retain raw measurements, procedure, source/runtime/deployment identities and
   screenshots under `audit/2026-10-embedded-latency/`. Verify source/result/link
   identities, positive trial counts, statistics and negative controls, JS syntax
   and explicit semicolons. Push reviewable website/docs draft PRs, update #748/#124,
   verify remote retention, then stop task processes and remove inspected worktrees.
