# Cipher — BASIC prototype brief

**Status:** The user authorised the compact [six-lesson progression](lesson-brief.md)
around the native prototype, with five independently runnable checkpoints.
The [replacement lessons](lessons.md) are verified and ready for local review. The source review is in [review.md](review.md).

## Experience and scope

Find a hidden familiar word by choosing letters. A correct guess reveals every
occurrence; a miss consumes one of seven mistakes. Repeating a guessed letter
costs nothing. The board shows the word, untried alphabet, missed letters and a
remaining-mistake count with seven markers. There is no time limit.

The first trial uses 24 uppercase everyday words, four to eight letters each.
A random selection rejects the immediately preceding word; earlier words can
return. There is no promise of a full shuffled deck. Content includes repeated
letters so revealing all matches matters. Word length is not a difficulty scale:
familiarity, plausible alternatives and letter distribution also affect play.

Guess using letter keys directly. Enter pauses; the pause menu offers continue,
reset of words/scores, and quit. Q and R remain ordinary guesses during play.
At a result, reveal the answer and wait for Space to choose the next word, R to
reset the session or Q to quit. Wins and losses persist across completed rounds.
Reset abandons the current session rather than recording another loss.

## Target and presentation

Stock 48K PAL Spectrum, Sinclair BASIC, keyboard and tape. Build and execution
use the family emulator with the ordinary ROM editor and tape interface.
The development host is not part of the runtime requirement.

Use a black background, cyan headings, a generously spaced word, white alphabet
and yellow status text. Tried letters become dots; missed letters also have a
separate explicit list. Colour supplements text, counters and shapes. The
prototype is deliberately silent. No gallows, speed pressure, whole-word entry,
cryptographic puzzle, difficulty selector or content expansion is required.

## Teaching value and scope decisions

The distinct relationship is between a hidden string, a revealed string and a
record of attempted letters. A loop reveals every matching position; a scan
prevents repeated guesses from changing the result. An alphabet string marks
used letters; play updates one alphabet cell and the changing fields instead
of clearing and rebuilding the board after every guess. DATA separates the word
list from the game rules. A release gate makes one press one guess.

The intended home is a compact project in Boards and deduction, subject to play
and lesson review. Do not inherit the old Volume 2 prerequisites, fixed line
budget, eight-topic quota or claims about word length. DATA and arrays alone do
not justify a long progression after the revised board games.

A later teaching sequence can start with one visible word and partial reveal,
then add a guess, duplicate handling, mistake limits, the board, a word list and
replay. The playable prototype determines the endpoint before lessons are split.

## Verification and decision gate

Enter the complete source through ROM keyword keys, save an auto-starting TAP
and load it in a fresh process. Check input normalisation, ignored nonletters,
all occurrences of a repeated letter, free repeats of hits and misses, seven
unique misses, complete-word success, held input, pause/continue, reset, quit,
score retention and rejection of an immediate repeat. Exercise every DATA word;
label direct ROM diagnostic setup separately from normal play captures.

Inspect the board and both endings. Native execution establishes observed rules,
not that the word choices are satisfying. Ask for play feedback before lesson
authoring. If this is too thin or familiar, shorten or defer it rather than add
systems to justify a course-sized game.
