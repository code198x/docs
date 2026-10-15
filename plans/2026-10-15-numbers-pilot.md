# Numbers and representation pilot

Fourth bounded slice for umbrella #114, #115 and #124, authorised after approval
of the repetition pilot. Keep BASIC and assembly independent. No learner is
available: technical checks cannot establish educational effectiveness.

Baselines: website eff31273bd5c9551264b2a884d9d4825ce0d161b; docs
c0065db03fe05e683ecd7df807218c7ebde74250. Use isolated worktrees and copies of
existing installed tooling. Preserve unrelated shared-checkout work.

1. Source-check Counting in Twos units 3–4: numeric maximum versus pattern count,
   address space versus RAM, byte carry versus signed overflow. Consult Zilog
   UM008011-0816 pp.66–67 and 147 and the Amstrad +3 manual p.182. Check related
   BASIC numeric-variable and assembly byte/pair explanations. Deduplicate and
   file concrete findings in the website repository.
2. Correct only `src/content/curriculum/foundations/counting-in-twos/unit-03.mdx`
   and `unit-04.mdx`: state assumptions, add closed prediction answers and an
   optional existing system connection. Preserve language-neutral pseudocode.
3. Add `audit/2026-10-numbers-pilot/verify-numbers.py` and a small assembly fixture.
   Check BASIC 255+1 and 65535+1 through ROM entry, and actual Z80 ADD results,
   carry and P/V for 255+1, 127+1 and 5+251. Record binary/ROM/source fingerprints.
4. Prepare REPORT, LEARNER-TASKS and ASSESSOR in that audit folder. Map prerequisites
   and optional routes. Cover prediction, explanation, modification, diagnosis
   and creation without publishing assessor answers alongside learner prompts.
5. Add `scripts/verification/numbers-pilot.mjs` for both lessons. Capture the live
   baseline, prove the corrected-state verifier rejects it, run production build
   and repository checks, then verify proposed pages at 1440 and 390 pixels:
   keyboard disclosure, optional link/back, overflow and main-region axe results.
6. Publish focused paired draft PRs, update finding and parent issues, and retain
   evidence receipts. After remote-ref verification, stop owned preview processes
   and remove task worktrees, copied dependencies and temporary outputs.

Do not add dependencies, rewrite other units, create a pseudocode interpreter,
claim original-hardware coverage, or close the umbrella issues.
