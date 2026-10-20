# AMOS bank or risk native prototype

Use the accepted trial tuning: one six-sided die, limit 10, at most five rounds,
target 30. Prove the endpoint before writing a lesson sequence. Preserve the
separate Blitz and language-tooling decisions.

1. Read the game brief and original AMOS documentation for random integers,
   seed, fresh-key input, loops and storage. Reuse the previously approved
   official AMOS revision and existing FS-UAE/media configuration in an isolated
   test directory; do not install dependencies or change system settings.
2. Write the native program in code-samples at
   `commodore-amiga/amos/bank-or-risk/prototype/bank-or-risk.amos`.
   Keep text presentation, labelled totals, roll/bank decisions, exact-limit
   banking, bust, target/reachability, fresh-input boundaries, replay and quit.
   Use a separate, documented fixed-roll test variant to exercise native rules
   without presenting it as random play.
3. Import and run the exact source in AMOS Professional 2.00. Record source,
   runtime/media identities, inputs and observations. Check boundary rolls,
   limit equality/bust, once-only scoring, recovery, success/failure, invalid and
   held input, replay, quit, and save/reopen through the actual editor.
4. Retain original screenshots and a concise execution report beside the game
   brief. Separate source/model evidence, native observations and manual play;
   no learner effectiveness or original-hardware claim follows from this trial.
5. Run meaningful source/checkpoint verification, lint and documentation checks.
   Commit/push each repository's bounded change and open a samples review PR;
   update docs PR #103. Retain work on verified remote refs, stop task-owned
   processes and remove temporary worktrees and runtime copies before finishing.

Do not publish lessons, change the website catalogue or merge unapproved PRs.
If native work exposes a fault, reproduce it and isolate its cause before fixing
it; after repeated failed attempts, reduce the experiment instead of expanding
the game or changing language implementations.
