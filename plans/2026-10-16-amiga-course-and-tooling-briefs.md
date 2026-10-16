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

Do not change the live lessons, catalogues, samples or charter. Do not download
dependencies, create a new tool repository, implement either language, or claim
that these project designs have been executed or tried by a learner. Preserve
the existing documentation checkout's unrelated README and work queue edits.
