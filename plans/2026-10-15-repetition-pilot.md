# Loops and repetition pilot

Third bounded slice for umbrella #114, #115 and #124, authorised after approval
of the decisions/boundary pilot. Objective: predict loop entry and repetition,
locate work that belongs once per round, and distinguish a fresh random choice
from a guaranteed different value. Keep BASIC and assembly entry independent;
no learner is available, so educational validation remains pending.

Baselines: website `d12fdad9030586c8b5ee6c7a2109c5feb33eeac4`, docs
`3c7aec317995647ce0c2825f04126a6a58d3e526`, samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Use isolated worktrees and local
copies of the existing installed packages/UI kit, avoiding the previous slice's
Astro symlink-resolution failure. Preserve unrelated work in the normal checkouts.

1. Map Foundations `repeating/unit-01.mdx` through `unit-03.mdx`, BASIC Meet
   BASIC lessons 6–7 and assembly Meet Assembly lesson 4. Record which constructs
   each uses and what it explains locally. Source-check cross-language differences.
2. Check existing issues and file confirmed findings in the owning repository.
   Investigate the claim that a random secret is different every time against
   BASIC lesson 7's explicit repeatable-seed and repeated-choice explanation.
   Do not turn statistical observations into a claim of fairness.
3. Use the maintained native keyboard driver to check counted loops at zero,
   one and several turns, plus a fixed-seed bounded random sample. Reuse the
   live row-loop verifier for actual write count, pointer movement, same-tab
   artwork transfer, recovery and keyboard replay. Keep unsafe zero-B drawing
   outside the public eight-byte table experiment.
4. Prepare only bounded corrections justified by findings. Preserve correct
   explanations of zero-entry WHILE and post-test REPEAT, and the assembly
   lesson's explicit warning that B=0 leads to 256 DJNZ turns.
5. Prepare separate learner and assessor packs covering prediction, explanation,
   modification, fault diagnosis and creation. Use optional links without making
   shared subjects a prerequisite. State all currently untested learner tasks.
6. Run production build, appropriate repository checks and narrow/wide keyboard
   checks of the proposed lesson. Capture a live baseline and proposed result;
   confirm the correction verifier rejects the unchanged page.
7. Push focused draft PRs with evidence and link findings from #114/#115/#124.
   Keep editorial approval and publication separate from actual learner evidence.
   Verify commits on remote refs before removing task worktrees and build output.

Retain results in `audit/2026-10-repetition-pilot/`, distinguishing passed, failed,
expected-rejection, skipped and unknown outcomes. No new dependency, public
framework, pseudocode interpreter or broad rewrite is commissioned.
