# Three in a Row — prototype record

**Status:** The user accepted the native game after play, reporting that it works well and mostly draws. They agreed to retain this difficulty and develop lessons. The [teaching progression](lesson-brief.md) preserves the accepted source.

## Implemented game

Stock 48K PAL Sinclair BASIC, one 3×3 board, X for the human and O for the computer. Direct 1–9 keys place a mark; occupied or invalid keys preserve the turn. A release gate prevents a held key from becoming another move after O replies. S starts; R restarts or replays; Q quits from title, play or result.

The computer uses the reviewed win → block → centre → corners → edges policy and prints the branch that chose its move. It scans a shared DATA table for either side's immediate opportunity. First free corner in 1/3/7/9 order wins a corner tie; the edge fallback takes the last free cell. Numeric state owns legality and results. The larger vector board, substantial X/O marks, remaining square numbers and yellow winning line stay visible at the end. The game is silent.

The human starts the first round. Completed rounds alternate the starter and update the session tally once. Restarting an unfinished round keeps its starter and does not score it. The verified samples baseline is commit `46ca3c6`. The source is `code-samples/sinclair-zx-spectrum/basic/three-in-a-row/prototype/three.bas`; the self-starting tape is under its `verification/evidence/three.tap`.

## Verification

The complete source was entered using ROM keyword keys and saved to tape. Two later message-padding corrections were also entered through the ROM after a fresh tape load; unchanged stored lines were checked byte-for-byte before re-saving. A separate process then loads the final tape. The audit checks line identities, literal branch targets, tape checksums, auto-start line 10 and source/evidence hashes.

The independent line-count model enumerates all legal human replies under both starters. Human-first yields 489 terminal sequences: 12 human wins, 127 draws and 350 computer wins. Computer-first yields 94: 14 draws and 80 computer wins. There are 314 distinct computer-turn positions across the two runs. These are exhaustive path counts for this exact policy, not human win probabilities. The known 1/8/7/4 human sequence still exploits a fork when the human starts. Computer-first has no losing path in this model.

The final local emulator passes **40 check groups and 123 observed human moves**. Checks cover legal paths through both starting orders, each available reason, immediate-win priority, the retained fork, win/loss/draw, stable results, invalid and occupied input, a held key across O's turn, reset/replay, tally updates and all quit routes. Displayed O choices and reasons match the independent model.

All eight winning lines for both marks are additionally checked using sixteen explicit diagnostic boards entered with ordinary BASIC DIM/LET commands after STOP. A full-board winning diagnostic checks that a last-cell win is not reported as a draw. These fixtures are not ordinary play, use no direct memory writes and do not supply public playthrough captures. Representative original captures from legal rounds were inspected.

## Rendering verification

The released Emu198x Spectrum 0.25.0 executable and the current local checkout at `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3` both pass the gameplay suite. The local executable reports 0.24.0 and is the one opened for native play. No emulator source was edited.

The original fork-win captures from both builds are byte-identical. A separate diagnostic compares all 49,152 screen bitmap pixels with the emitted PNG's foreground, checking black paper, non-black ink and FLASH off. It reads original image pixels and never edits the PNG. This makes the capture check independent of an image preview's appearance. `renderer-comparison.json` records both executable hashes and links their capture checks; `release-results.json` retains the release's gameplay run separately.

The maintained verification commands are in the sample README. `manifest.json` binds the final source, tape, results and captures. Native playability is accepted. The user's report of mostly drawn games is qualitative feedback, not a measured frequency or an unbeatable-policy claim. No original-hardware timing or learner-outcome claim is made.
