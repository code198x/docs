# Verify the sound-enabled AMOS endpoint survives save/reopen

Use samples revision `1fa0675b809ef6a40bcf01571b75d6196cce0e0e` without changing game rules or input. Retain the earlier audits unchanged.

1. Reuse the sound audit’s verified media builder and pinned tools/firmware in isolated workspaces. Verify hashes and all original runtime files.
2. Import the maintained source, inspect its listing and native syntax check, save it as a tokenised AMOS program through Save As, then export the modified disk to a new path. Record scripts, reports and captures under `audit/2026-10-amos-bank-or-risk-persistence/`.
3. Validate the exported filesystem and program entry. Cold boot a separate emulator process from that exported disk, load the saved program, inspect the listing and run it. Verify title, die/board, banking and its recorded cue, replay/quit where applicable. Compare the same supplied-roll fixture before/after saving if needed to establish deterministic game state and sound equality; distinguish this from the maintained random source.
4. Update current `platforms/commodore-amiga/` AMOS prototype/brief status and the samples prototype README only where persistence claims change. Run syntax/format, media and artifact guards, JSON/link checks and inspect captured outcomes. Missing export/program and wrong source must fail verification.
5. Commit and push to the existing PR branches without merging. Remove task-owned worktrees, runtime copies, build output and processes after remote verification. Preserve unrelated changes. Listening and uncoached learner acceptance remain separate.
