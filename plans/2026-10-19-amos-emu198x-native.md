# Run the AMOS opening through Emu198x

The user directed us to use Emu198x for native execution and treat deficiencies
as bugs. The broken desktop-control connection is not a prerequisite for the
emulator's own script or MCP interface.

1. Read the current Amiga launcher/runtime interface and use a source-built
   headless `emu198x-amiga` at a recorded revision. Reuse lawful local firmware
   and AMOS media; record identities without committing licensed bytes.
2. Boot AMOS through its disk image, inspect a capture, then use real emulated
   keyboard input and native editor operations to import or enter the sample.
   Preserve setup/capture scripts and actual outcomes in
   `audit/2026-10-amos-bank-or-risk-emu198x/`.
3. Qualify syntax and run the prepared fixed-roll cases, fresh/held input,
   once-only scores, replay, quit and independent save/reopen where possible.
   Do not substitute host-calculated results for observed AMOS output.
4. Reproduce any emulator failure in the smallest suitable case, check existing issues
   in `emu198x/emu198x`, and file a concrete bug with the revision, configuration,
   script, expected/observed result and non-licensed evidence. Investigate the
   cause before proposing a fix. Follow the emulator's rules for code changes.
5. Update `platforms/commodore-amiga/games/bank-or-risk/prototype.md` with actual
   results and remaining limits. Commit and push evidence, verify remote
   retention, and clean task-owned worktrees, builds, media copies and processes.

Keep the accepted 10/5/30 game and progressive drawing/colour/sound direction.
The first task is to establish original-runtime correctness. Native play and
an eventual uncoached beginner trial remain distinct evidence.
