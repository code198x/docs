# Bright Spark prototype

**Status: board and manual cues implemented and checked, 6 September 2026.** The [approved brief](brief.md) remains the specification. This is a bounded prototype, not replacement lessons or a complete memory game.

## Implementation

The [prototype sources and evidence](https://github.com/code198x/code-samples/tree/2046aa0/sinclair-zx-spectrum/basic/bright-spark/prototype) contain three runnable checkpoints: one rectangle, four labelled panels, and manual cues selected with 1–4. The target is a stock 48K Spectrum in its 50 Hz configuration, using Sinclair BASIC.

Digits sit above the repainted panel rows so drawing cannot erase their identities. An active panel brightens and gains an asterisk; green/yellow use black cue ink and red/blue use white. Four different beeper notes accompany the cues. The drawing routine's shared variables and restored attributes are documented explicitly. The input loop captures once, rejects unrelated keys and waits for release after each cue.

## Evidence and limits

Released Emu198x Spectrum v0.22.1 on Apple silicon executed each complete listing through ROM key entry. Checks covered all four panel labels throughout sampled cue states, correct active markers, return to rest, consecutive identical cues, irrelevant input, quitting, and saving a BASIC tape followed by named loading in a fresh process. The committed results include source and emulator hashes.

Recorded audio distinguishes one held press (one sustained note) from release and another press (two notes). Short-window pitch estimates agree with the four chosen notes within 25 Hz. These are signal measurements, not subjective listening. A captured active blue panel has been visually inspected; monochrome, other displays, native control feel and original hardware remain unreviewed.

A separate controlled `PAUSE 50` probe observed completion after 56 frames without a key and 12 when a key was pressed after ten frames. Both counts include BASIC execution and printing. The experiment demonstrates interruption, not a precise timing guarantee. This matches *ZX Spectrum BASIC Programming*, second edition (1983), chapter 18, “Motion”, p. 129. Chapters 16 and 19 describe the colour and beeper facilities used here.

No emulator blocker was identified. No converter, assembler or machine-code helper is required. Generated tapes and audio can be reproduced with the commands in the sample README; the committed preview is from a fresh-tape run.

## Next bounded work

Settle automatic playback timing against the approved brief before publishing the rewritten lessons. Exercise repeated panels and keys pressed or held during WATCH; decide and explain whether interruption is permitted or the wait must resist it. Do not describe `PAUSE` as an unconditional timer or replace it with an unexplained calibrated loop.

Then develop the board and cue lessons from these checkpoints, recalling relevant Meet BASIC and Foundations explanations locally. The three source checkpoints do not fix the number of learner-facing milestones. Sequence storage, response comparison, growth, the 16-round boundary and replay remain unimplemented in this replacement prototype.
