# AMOS and Blitz course and tooling briefs

Prepare three proposals for discussion before replacing lessons or implementing
language tooling. Both courses must welcome a first-time programmer and let an
experienced reader enter later. They may use different projects. Implementing an
interpreter or compiler is an option to investigate, not an agreed architecture.

## Tasks and verification

1. Read `PROJECT.md`, `specifications/curriculum.md`, `specifications/unit.md`
   and `specifications/brief.md`, the current Meet AMOS and Meet Blitz lessons,
   and the setup and verification evidence. Consult the family decisions on
   general tools and tooling migration. Separate source observations from
   execution and learner evidence.
2. Draft `platforms/commodore-amiga/amos/course-brief.md`: audience, outcomes,
   project alternatives, proposed opening stages, early saving and recovery,
   experienced entry, reuse and observable acceptance checks.
3. Draft `platforms/commodore-amiga/blitz/course-brief.md` with the same teaching
   responsibilities but an independently justified project and sequence. Resolve
   the distinction between original Blitz BASIC and AmiBlitz before promising
   a replacement execution route.
4. Draft `platforms/commodore-amiga/tooling-feasibility.md`: requirements from
   the courses, available evidence, three implementation options, compatibility
   obligations and a bounded experiment that would inform a tooling decision.
   Keep tool ownership and implementation subject to a separate agreement.
5. Link the proposals from `platforms/README.md`. Review the prose and every
   relative link, run `git diff --check`, and confirm proposal status, existing
   content preservation and agreement with the charter. Commit and push only
   this bounded documentation change, make a reviewable PR, and remove the
   temporary worktree after verifying the remote retains the commit.

## Scope

Do not change the live lessons, catalogues or samples. Do not download
dependencies, create a new tool repository, implement either language, or claim
that these project designs have been executed or tried by a learner. Preserve
the existing documentation checkout's unrelated README and work queue edits.

## Review revision

The agreed design constraints now favour a game over the drawing toy, keep the
opening gentle, allow the full AMOS track to grow towards substantial games, and
make distinct games the default across tracks and systems. Repeated games need
an explicitly agreed teaching purpose. Project candidates remain proposals.

1. Compare the four systems' current module catalogues and the relevant authored
   lessons and retained designs. Record positive examples of overlapping play,
   distinguishing published material from inherited proposals. Store the bounded
   comparison and a short candidate list in
   `platforms/commodore-amiga/amos/opening-candidates.md`.
2. Record the agreed distinct-game principle in `PROJECT.md`,
   `specifications/curriculum.md` and `specifications/brief.md`. It applies to
   new choices; do not remove existing games or rewrite catalogue status.
3. Revise the AMOS brief around a gentle proposed game and a full-track ambition.
   Recheck Blitz alternatives and align the tooling brief and platforms index.
   Do not start a game prototype or language implementation before its design
   is agreed.
4. Check changed prose, relative links, proposal status and whitespace; push one
   follow-up commit to the existing PR. Update its description to the resulting
   scope. Verify the remote commit and remove the temporary worktree.

## Bank or risk design

The agreed opening direction is now a solo dice game: approach a visible limit,
bank the current total or roll again, and lose the unbanked total if the roll
takes it over the limit. Take-away is not the selected direction. Keep the first
game small; do not add a dealer, card rules or a multi-round economy.

1. Write `platforms/commodore-amiga/games/bank-or-risk/brief.md` with concrete
   provisional tuning, input, scoring, finish/replay behaviour and teaching
   stages. Distinguish the agreed mechanic from numbers awaiting native play.
2. Check the rules using exact die-outcome enumeration and decision analysis.
   Store a reproducible rules check and its results beside the brief, labelled
   as a host model rather than AMOS execution. Include controls that reject
   banking a bust and treating equality with the limit as a bust.
3. Replace the take-away recommendation in the AMOS brief and candidate review;
   align the index and tooling requirements, including random selection and
   increasing risk. Keep the existing comparison scope and distinct-game rule.
4. Check local links, style, model results and the final diff. Push the bounded
   design change to PR #103, update its description and clean the worktree after
   verifying remote retention. Live lessons, runtime implementations and learner
   effectiveness are outside this design pass.

## Tune before the native trial

Compare settings before fixing the first prototype's balance. Keep one die,
bank-or-roll, a visible limit and a short target challenge; do not add features.

1. Parameterise the existing rules model by limit, rounds and target. Preserve
   the 21/5/90 result as a regression case. Compare the safe stopping policy,
   fixed riskier policies, the optimal target policy and recovery after a bust.
2. Compare a bounded set of settings, including retaining 21 and lowering the
   limit. Check that safe play does not guarantee success, a bust can leave a
   credible recovery, and choices can change with the session state. Separate
   a mathematically possible recovery from its calculated chance.
3. Cross-check policy probabilities with an independent round-score distribution
   and convolution. Retain negative controls and exact boundary checks. Treat
   all probabilities as ideal-die analysis, not player or AMOS measurements.
4. Replace the numerical recommendation in the game brief and linked course
   proposals. Record comparison results, trade-offs and what remains for native
   play. Run the model, Ruff, prose, links and diff checks, push to PR #103 and
   remove the temporary worktree after verifying the remote commit.
