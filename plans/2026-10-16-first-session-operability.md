# First-session operability qualification

After approved website #751/docs #82 merge, address website #749 under umbrella
#124, preserving #123's family-wide accessibility ownership. Isolated docs worktree;
website worktree only for a confirmed defect or repeatable verifier. No dependencies.

Declared matrix before exercising the route:
- Actual installed Safari on macOS 27: native UI through computer-use tools;
  /try/ → BASIC guide → unit 1. Discovery, editable source, run/change, deliberate
  error/repair, reset, tape download/reopen where exposed; keyboard actions on
  relevant controls, native accessibility tree and visible machine/text observations.
- Installed Playwright WebKit exists as a possible repeatable engineering-test
  configuration; it is not shipping Safari or physical iOS. Use only if needed
  and separate its results from native Safari.
- VoiceOver is installed but off. The user explicitly chose to skip it on
  16 October. Do not toggle it. Native AX inspection is not a screen-reader pass;
  preserve this limit and keep broader qualification incomplete.
- No physical touch device is currently exposed by available tools. Physical
  mobile/touch is skipped, not inferred from viewport emulation.

1. Read current route/first-session instructions, source/machine controls and
   prior evidence. Record source/deployment identities. Inspect native UI without
   changing user tabs; create one task Safari tab and close only that tab at end.
2. Execute the declared route; record actions/results, input method, actual Safari
   version/window size, exposed names/states and whether visual/audio information
   has an alternative. Keep audio delivery, AT semantics and learner understanding
   separate. Save only task observations; exclude unrelated Safari/tab content.
3. Verify any blocker twice with a reduced procedure, inspect its source cause,
   deduplicate #123/site issues, then file bounded findings. Do not widen to a
   redesign or invent a defect from unavailable hardware/tool affordances.
4. If approved, exercise VoiceOver navigation/output/error/control announcements
   on this task tab, then restore its initial off state. If not, document skipped
   AT operation and keep #749's remaining scope visible.
5. Retain bounded report, exact matrix/outcomes and evidence under
   `audit/2026-10-first-session-operability/`; link current coverage/README. Verify
   links/identities/prose, push reviewable draft PR(s), update tracking issues,
   verify remote retention and clean task tab/worktrees/processes/downloads.
