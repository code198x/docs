# Locksmith — BASIC prototype brief

**Status:** The user selected Locksmith after the remaining-course review. The user accepted the native trial: “Locksmith is great”. Retain its rules and ten-guess difficulty as the BASIC baseline; the [nine-lesson progression](lesson-brief.md) now has seven [verified checkpoints](lessons.md). The overview and nine replacement lessons are authored for local review. See the [execution record](prototype.md).
**Target:** Stock 48K PAL ZX Spectrum, Sinclair BASIC, keyboard and ROM-loaded tape. No machine-code helper.
**Evidence:** The earlier six lessons and `code-samples/sinclair-zx-spectrum/basic/locksmith/unit-06/locksmith.bas` supply the repeated-digit scoring algorithm. The new trial lives in `code-samples/sinclair-zx-spectrum/basic/locksmith/prototype/`. Existing published lessons remain available during development.

## Experience

Crack one hidden four-digit code. Each digit is 1–6 and may repeat. Submit a guess, read two aggregate clues, and combine them with earlier results. EXACT counts correct digits in their correct positions; OTHER counts correct digits in different positions. Each occurrence can contribute only once. The clues describe the guess as a whole, not individual positions.

The first trial allows ten guesses, retains every submitted guess and both counts on one screen, and reveals the code after success or exhaustion. Repeating a guess consumes a turn. R begins a new random code; Q quits from title, play or result. The ten-guess limit is retained after native acceptance. Repeated digits are part of the baseline, reconciling the old source and the contradictory old brief.

The pleasure should come from testing a hypothesis and narrowing the possibilities. There is no timer, reflex requirement, changing secret or misleading clue. Initial scope excludes a computer solver, hints, difficulty modes, cumulative scores, campaign and encryption narrative. If ten guesses encourage arbitrary attempts rather than reasoning, revise the budget or feedback after native play.

## Presentation and controls

Use a dark one-screen board with four spaced digit cells per row, clearly labelled EXACT and OTHER columns, and an editable guess beneath the history. Digits and numeric clues carry all essential information. Colour reinforces the labels but never determines scoring or which digit matched. Title instructions explain repetitions and single counting. Deliberate silence keeps the trial focused on deduction.

Digits 1–6 fill the guess. D or the Spectrum DELETE key removes its last digit. Enter submits exactly four digits. Other characters and excess digits do not change the guess; incomplete submission keeps the same attempt. A held digit produces one entry until released. Input editing and replay are part of the game, not ROM command-entry exercises.

The title's lock panel is original text artwork. No borrowed assets or custom font are needed for this trial.

## Teaching role

The replacement website catalogue places Locksmith in Boards and deduction alongside Sonar and Crates. It extends combining clues with an algorithm for matching repeated values. Arrays and loops are recalled locally rather than treated as attendance requirements. Separate the stored code, current editable guess, scoring and display.

The central algorithm counts each digit in both arrays, sums the smaller count for each value, then subtracts exact matches to obtain OTHER. Compare it with a naive pairwise search that can count one occurrence several times. A worked example with repeated digits is essential. A later Pattern Library entry could explain matching multisets, but the game must supply its own explanation.

## Teaching progression

The [lesson brief](lesson-brief.md) defines nine lessons supported by seven [executed checkpoints](lessons.md): board, editable guess, exact scoring, repeated-digit clues, visible history, hidden random rounds and the accepted title/game. Deduction and saving reuse existing programs. The final teaching source is byte-identical to the accepted prototype. Full replacement lesson prose and publication are next.

## Tools and verification

Build on the existing ROM keyboard-entry harness, using Emu198x Spectrum 0.25.0 and a configured lawful 48K ROM. SAVE produces a self-starting TAP; verification loads it through the ROM in fresh emulator processes. The host enters source and drives keys; it supplies no runtime helper.

Compare actual BASIC scores with an independent host occurrence-matching model over multiple real rounds. Observe the randomly generated code for verification without writing it or any game state. Check four exact matches, zero matches where available, repeated-digit overcount cases, valid score bounds, full ten-row history, incomplete and invalid input, deletion, overflow, held digits, win, loss, new rounds and quit. Check tape blocks and stored-source identity. Retain and visually inspect original emulator captures.

Automated checks establish configuration-specific execution. The user accepted the native experience. Independent learner outcomes remain untested. Define and verify the teaching checkpoints before authoring replacement lessons.
