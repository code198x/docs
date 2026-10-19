# Show complete AMOS pictures

The user likes the arcade pass but reports brief flicker and partial redraws.
The retained native roll clip reproduces this at frames 23–24: coloured panels
and an incomplete board appear during the settled-result redraw. Drawing and
clearing happen on the visible screen. The prior settled-picture checks and
sparse preview samples missed the transition.

1. Preserve the failing clip identities and selected raw frames in a new
   `audit/2026-10-amos-bank-or-risk-complete-frames/` record. Keep the accepted
   arcade sources intact; add `stages/arcade/stable-display.amos` and explain the
   exact changes in its guide.
2. Use AMOS Double Buffer, Autoback 0 and manual swaps. Draw the whole board and
   controls before showing it; make each preview face visible only when finished.
   Copy the displayed complete image back to the hidden buffer after presenting,
   so later partial die edits start from the same board. Disable automatic object
   updating rather than allowing it to swap unfinished pictures. Preserve rules,
   random choice, sound and fresh-key behaviour.
3. Run native deterministic roll/settle, bank/round/record/rescue/replay and quit
   checks plus ordinary random play on the existing pinned configuration. Record
   continuous native video around transitions and examine every frame, including
   formerly omitted intermediate frames. Compare stable views against the arcade
   endpoint. Verify that corrupting one transition frame makes the check fail.
4. Save and independently reopen the endpoint if feasible in this bounded pass;
   distinguish this evidence from snapshot restores. Commit and push verified
   work to the existing PRs, without merging. Keep the user's active review app
   intact. Remove disposable media/builds and clean worktrees after remote proof.

Typography and broader styling are a separate design choice awaiting the user's
preference. ROM-font instructions with distinctive title/score lettering are the
recommended direction; no font download, new dependency or styling rewrite is
part of this bug fix.

The user selected ROM text with distinctive title and score. After the redraw
fix qualifies, add `styled-board.amos` as a separate complete stage: resolve and
verify the ROM font rather than assuming a font-list index, place graphical
text using measured baselines/widths, and author the small title/number bitmap
alphabet in source. Keep bright palette roles, readable instructions and all
rules. Compare settled state meanings and continuous transitions, provide exact
editing explanations, and preserve the existing review app when offering the
new version. No downloaded font dependency is needed.
