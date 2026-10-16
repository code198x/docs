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
