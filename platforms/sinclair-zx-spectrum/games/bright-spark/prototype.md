# Bright Spark prototype

**Status: seven replacement lessons approved for publication, 9 September 2026; complete-game emulator checks passed.** The [approved brief](brief.md) remains the specification. The complete sequence was approved on 9 September. Publication uses descriptive lesson URLs, with topic-preserving redirects and heading aliases for the six old numbered pages.

## Implementation

The [prototype sources and evidence](https://github.com/code198x/code-samples/tree/2046aa0/sinclair-zx-spectrum/basic/bright-spark/prototype) contain three runnable checkpoints: one rectangle, four labelled panels, and manual cues selected with 1–4. The target is a stock 48K Spectrum in its 50 Hz configuration, using Sinclair BASIC.

Digits sit above the repainted panel rows so drawing cannot erase their identities. An active panel brightens and gains an asterisk; green/yellow use black cue ink and red/blue use white. Four different beeper notes accompany the cues. The drawing routine's shared variables and restored attributes are documented explicitly. The input loop captures once, rejects unrelated keys and waits for release after each cue.

## Evidence and limits

Released Emu198x Spectrum v0.22.1 on Apple silicon executed each complete listing through ROM key entry. Checks covered all four panel labels throughout sampled cue states, correct active markers, return to rest, consecutive identical cues, irrelevant input, quitting, and saving a BASIC tape followed by named loading in a fresh process. The committed results include source and emulator hashes.

Recorded audio distinguishes one held press (one sustained note) from release and another press (two notes). Short-window pitch estimates agree with the four chosen notes within 25 Hz. These are signal measurements, not subjective listening. A captured active blue panel has been visually inspected; a browser greyscale rendering of the active panel has also been inspected, retaining all four labels and the active marker. Other displays, native control feel and original hardware remain unreviewed.

A separate controlled `PAUSE 50` probe observed completion after 56 frames without a key and 12 when a key was pressed after ten frames. Both counts include BASIC execution and printing. The experiment demonstrates interruption, not a precise timing guarantee. This matches *ZX Spectrum BASIC Programming*, second edition (1983), chapter 18, “Motion”, p. 129. Chapters 16 and 19 describe the colour and beeper facilities used here.

No emulator blocker was identified. No converter, assembler or machine-code helper is required. Generated tapes and audio can be reproduced with the commands in the sample README; the committed preview is from a fresh-tape run.

## Playback choice and opening drafts

Retain the extra `PAUSE 10` and explicitly permit keys to shorten it. The [playback driver and seven opening checkpoints](https://github.com/code198x/code-samples/tree/349af70/sinclair-zx-spectrum/basic/bright-spark) supply the evidence. Fixed `314`, `22` and `1234` played in order. With two-frame tapping or a held key, identical cues retained 18 sampled frames without an active marker between them (0.36 seconds at 50 Hz), versus 26 without interference. Recorded tone windows remained separate, with about 0.54 seconds between them under interference. These observations support readable separation; they do not turn the routine into a precision timer or establish subjective listening acceptance.

Holding q from the first active marker ended playback after 22 observed frames, about 0.44 seconds. Check q between cues and tell the player to hold it: a tap entirely within a cue can be missed. The held playback key was drained before YOUR TURN, and a subsequent fresh key was read. Response validation and comparison remain later work.

The opening lessons now have seven verified checkpoints: row, rectangle, drawing routine, four-panel board; persistent active cue, returning audio/visual cue, four-cue demonstration. Checks followed the editing sequence through the ROM, rather than loading each state independently. An initial editing run failed; allowing extra settling time after entries made the unchanged sources pass. This is recorded as an automation limitation, not an isolated emulator defect.

## Remaining lessons and complete game

The third lesson develops representation through three checkpoints. Four further drafts cover fixed playback, fresh validated input and comparison, random growth and completed-round scoring, then instructions/replay/saving. There are eighteen maintained checkpoints across seven drafts. The publication change replaces the old pages with these seven lessons and redirects review links to their public destinations.

Released Emu198x Spectrum v0.22.1 passed ROM edit continuity from the final representation checkpoint through every later checkpoint. Further checks cover `314`, `22`, `1234`, repeated-cue interference, wrong first/middle/last answers, held and irrelevant keys, idle polling and release hand-off. A run seeded with `RANDOMIZE 1234` completed all sixteen rounds using responses derived from observed playback; every new order preserved its prefix. The result showed sixteen completed rounds without another playback. Replay reset the sequence and score; first-round failure scored zero and fourth-round failure after three completed rounds scored three. A named tape was saved, loaded in a fresh process, played, replayed and quit. Reproducible runners and source hashes live in `opening/verification/` on the sample branch.

The release routine captures into `a$` so it cannot erase the accepted `k$` before comparison. It checks q while waiting. Empty input loops directly back to capture; release waits follow a consumed key or a phase transition. Cues remain blocking and do not buffer typing ahead, which the player instructions state explicitly. The final saved name is `spark16`, distinct from the earlier `spark` checkpoints. A supplementary run verified that exact named save/load in a fresh process, a temporary two-round cap, rejected keys below/above the valid range, separate short repeated presses, held replay, playback quit and the proposed shorter-note experiment. The two harness corrections needed were the existing ROM-edit settling allowance and excluding the intentional partial CLS transition from label-retention assertions; no BASIC change was needed. Alternative audio was captured, not subjectively reviewed.

The final success capture was inspected with labels, completed count and replay prompt intact. The website build passed (69 tests passed, 9 skipped). The four new drafts rendered at 390 and 1440 pixels in both themes, with expanded checkpoints and answers, no document overflow or missing samples/images, and no serious/critical accessibility findings. Local links and navigation from lesson 3 into lesson 4 passed.

## Publication and remaining observation

The user approved publication on 9 September. The seven public lessons use optional
keyboard notes, with syntax and editing actions kept in the main explanation.
Question prompts have a shared, subtle visual treatment and an optional explanation;
full-source checkpoints remain separate. Bright Spark is game 1 after Meet BASIC.
The remaining published games retain their relative order, with numbering updated
to match the catalogue. Old samples and images remain available.

Native-control feel, subjective listening, independent learner observation and
original hardware remain unverified. These limits accompany the emulator evidence;
publication approval does not turn scripted input into human playtesting.
