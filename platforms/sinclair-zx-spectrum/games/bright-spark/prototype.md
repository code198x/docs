# Bright Spark prototype

**Status: opening checkpoints and playback policy checked; two lesson drafts ready for review, 6 September 2026.** The [approved brief](brief.md) remains the specification. The replacement game is not yet complete or published.

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

## Next bounded work

Review the two opening lesson drafts, including their local explanations, optional Foundations links, keyboard instructions and note vocabulary. They remain development-only review routes and do not replace the published Bright Spark pages. The drafts use plain changed-line listings and full checkpoints; navigation stays within the review pair.

Then develop representation and fixed-sequence playback from the verified cue contract. The timing choice above settles the first prototype question; further changes must retain the interference and repeated-cue checks. Sequence comparison, growth, the 16-round boundary, score and replay remain unimplemented in this replacement.
