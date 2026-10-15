# Decisions chains and stored state pilot

Continue umbrella #114/#115/#124 after approved Basics #739/#75 merge.
Website baseline 81033dc11717f5140f0e62420f6d2a3b4145d0cc; docs baseline
693034b18e60fd0cd5879d59997f74984d12cb92. Preserve original checkouts.

1. Read Decisions overview/units 1–4, current pseudocode/unit specifications and
   previous choice/Boolean evidence. Deduplicate/file the overlapping-chain and
   saved-comparison/reset gaps. Follow up #695's remaining overview wording.
2. Edit only `decisions/index.mdx`, `unit-02.mdx`, `unit-03.mdx`: local knowledge
   and independent entry; valid-number assumption; first-match/continuation;
   an overlapping 50/80 threshold example; saved versus recomputed comparison;
   intentional latched flag versus restart reset. Use existing Question prompts.
   Add an assignment-snapshot note in `specifications/pseudocode.md`.
3. Add native `verify-state.py`: run equivalent ordered dispatch, separate tests,
   stored/refreshed comparisons and latched/reset flags through actual Spectrum
   ROM key entry. Test all scores 0–100 through an audit-only BASIC loop, with
   independent expected bands; keep Spectrum 0/1 representation and GO TO branch
   implementation distinct from pseudocode. Include a deliberately failing wrong
   branch-order control, no expected-memory injection or performance claim.
4. Add explicit-semicolon browser verifier for overview and units 2–3 at 1440/390:
   outputs, boundary table and trace, Question disclosures. Retain baseline,
   known-red and after evidence; build/check, Vale/Ruff, syntax/semicolon checks,
   bounded wide/narrow visual review and explicit contrast limits.
5. Write learner/assessor sheets, report and hashes; update coverage and next
   remaining repetition work. Push paired drafts and parent updates. Verify
   retained remote heads and remove worktrees/caches/task processes/scratch files.
