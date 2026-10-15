# Fractional representation pilot

Sixth bounded slice for umbrella #114/#115/#124, authorised after bits/shifts.
Correct Working the Bits units 4–5 only, with explicit finite precision, exact
values and fixed-point decoding. No learner is available: keep learner evidence
pending. Preserve the agreed period 64K terminology and independent system entry.

Baselines: website 5354b0abc4779f8b562726a903da8f9b6ee229c6; docs
5ee7c9b50b4d4b53087928309b211e40eec23838. Isolated worktrees and copies of existing
installed tooling exclude shared-checkout edits. No dependency additions.

1. Read units 4–5, the shared pseudocode contract and BASIC fraction/range lessons.
   Source-check binary representation and rounding using the Amstrad +3 manual
   p.78, p.219 and its variable layout. Deduplicate and file exactness/decoding
   findings. Do not infer storage precision from printed digits.
2. Add `audit/2026-10-fractions-pilot/verify-fractions.py` and an audit-only assembly
   fixture. Observe actual ROM arithmetic and stored exact fractions versus an
   inexact tenth; use rational host calculations to decode configured numeric
   bytes, with format assertions. Check cancellation/equality examples without
   importing another runtime's floating-point results. Execute scaled integer
   addition and byte extraction via freshly assembled tape, not injected data.
3. Edit `src/content/curriculum/foundations/working-the-bits/unit-04.mdx` and
   `unit-05.mdx`: binary floating-point has exact representable values and limits;
   equality depends on purpose; speed is target/workload dependent. State chosen
   fixed width and scale, quantisation policy, range and matching-scale addition.
   Separate interpreting 384/256 as 1.5 from shifting to obtain the whole part 1.
4. Prepare REPORT, LEARNER-TASKS and ASSESSOR in that audit folder, with exact
   identities, observed/failed/unknown/pending outcomes and separate answers.
   Cover prediction/explanation/modification/diagnosis/creation. Link optionally
   to an existing BASIC fraction explanation without requiring prior attendance.
5. Add `scripts/verification/fractions-pilot.mjs` for baseline and proposed pages.
   Prove each old page is rejected independently. Build/check, then inspect both
   lessons at 1440×900 and 390×900: keyboard disclosures, optional link/back,
   overflow, scoped axe and visual comparison. No new interpreter or UI framework.
6. Publish focused paired draft PRs; update finding/parent issues. Verify the
   approved bits/shifts deployment live and retain its publication result in
   issue comments. Verify remote retention and evidence hashes before stopping
   owned processes and removing worktrees/copies/temp outputs.

No full arithmetic course, retro game performance benchmark, screen-reader or
physical-device claim, source acquisition or broad rewrite is commissioned.
