# Publish the bounded first session pack

The user authorised the next validation step within umbrella #114/#115/#124:
publish two activities and companion notes with a usable print view, invite
potential learners, then pause expansion until sessions produce observations.
No learner is available and no recipients are identified; prepare a short
invitation for the user to send, with feedback through existing routes.

Baselines: website f895b34fc8a316013b15b043d353daa6c24f4c66; approved docs draft
024c9f10f0f2d8f34422ddbcd296e3e228bd797d. Preserve shared checkout edits and use
isolated worktrees. No dependencies, new games or compulsory track progression.

1. Review the draft and existing lesson entry/save controls. Publish `/try/`,
   `/try/spectrum-basic/`, `/try/spectrum-assembly/`, `/try/parents-and-teachers/`,
   `/try/session-sheet/` and `/try/feedback/`. Keep each source in the website and
   replace docs draft copies with links after implementation. Reuse Layout,
   PageFrame and ReadingLayout through a scoped guide layout, with existing
   tokens/typography. Link from Start Here and Teaching only.
2. Add print behaviour scoped to this guide. Keep the session sheet legible on
   A4 and US Letter, include full lesson addresses, omit navigation in print and
   provide a keyboard-operable Print button. No new data collection service.
3. Add a bounded verifier in `scripts/verification/first-session-guide.mjs`.
   Check six routes at desktop/narrow widths, keyboard navigation, overflow and
   scoped axe. Exercise actual BASIC greeting edit/run/download/reopen and Z80
   border edit/run/download/reset through the public lesson controls. Inspect
   actual rendered output. Confirm the verifier can reject a missing route.
4. Run production build, repository checks and Vale; run the scoped design
   detector once after edits. Inspect desktop/narrow captures in one batched
   pass and A4/Letter printed output, with at most one correction pass.
5. Retain evidence and limits in docs; prepare `guides/first-session/invitation.md`
   and a small session-observation record for future reports. File confirmed
   blockers routinely. Push/merge the authorised publication PRs at verified
   heads after CI, verify the live result, and update parent issues.
6. Verify remote retention and clean worktrees, copied tooling, outputs and
   task-owned preview processes. Stop expansion: no invented learner results,
   broad epic closure or new routes beyond the two agreed activities.
