# Repetition progress and exit pilot

Continue umbrella #114/#115/#124 after Decisions #742/#76 merge. Website baseline
114f3614f5f0f6be107e550aa64d26785afa07a2; docs baseline
fa2f02934d3f075a9afdb37d26c18422f1996d5a. Preserve original checkouts.

1. Read all Repeating pages and the earlier repetition/Decisions evidence; check
   current pseudocode/unit specifications. Deduplicate/file reachable-exit versus
   guaranteed completion and loop-progress/reset gaps.
2. Edit only `repeating/index.mdx`, `unit-02.mdx`, `unit-03.mdx`: local knowledge,
   bound game-loop claims, valid numeric guesses, input-dependent completion,
   pre/post-test boundary and a decreasing whole-lives trace; show why an inner
   reset defeats progress. Use existing Question prompts and diagrams. Add a
   scoped progress/termination authoring note in `specifications/pseudocode.md`.
3. Add native `verify-progress.py`: eight natural pre/post-test cases at initial
   lives 0–3, one inner-reset counterexample capped by an explicit audit guard,
   and a deliberately failing missing-decrement control. Read actual target trace
   bytes and completion/guard messages. Do not call guard intervention a natural
   exit or infer all execution from a finite observation.
4. Add explicit-semicolon browser verifier for overview/units 2–3 at 1440/390:
   outputs, flow diagrams, trace and keyboard explanations/links. Retain baseline,
   known-red and after evidence; build/check, Vale/Ruff, syntax/semicolon checks,
   bounded wide/narrow review and explicit contrast scope.
5. Retain learner/assessor sheets, report and hashes. Update coverage/next gaps;
   push paired drafts and parent updates. Verify remote retention and clean
   worktrees/copied dependencies/task processes/scratch evidence.
