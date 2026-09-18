# Cipher — native prototype record

**Status:** The bounded native trial is built and verified. The user authorised
the [compact lesson sequence](lesson-brief.md) around this endpoint. The
replacement lesson preview is subject to review before publication. The [brief](brief.md) defines scope and [review](review.md) records
the inherited source findings.

## Implementation

The source is `code-samples/sinclair-zx-spectrum/basic/cipher/prototype/cipher.bas`.
The auto-starting tape and reproducible checks live in its `verification/` tree.
The prototype uses stock 48K PAL Sinclair BASIC and is deliberately silent.

Twenty-four familiar uppercase words support seven-mistake rounds. Direct letter
keys reveal every match; a tried-letter string prevents repeat costs. A second
string stores the available alphabet, with dots for used letters. Misses are
listed separately. Counts, markers and text convey outcomes without colour.

Enter opens a pause menu; C resumes, R resets words and scores, and Q quits.
During play, Q and R are ordinary guesses. Results reveal the answer, update
wins/losses and wait for Space, R or Q. New rounds reject the immediately previous
word, without claiming a shuffled deck or permanently unseen words.

## Execution evidence

Seventeen execution groups pass, including fresh-ROM tape auto-start and stored
token identity; title controls; lowercase/uppercase input; ignored nonletters;
all matching positions; free repeated hits/misses; pause preservation; legal
wins and losses; result retention; score carry-over; reset; held letters; quit;
and Q/R as guesses. Twenty-four explicitly labelled ROM-command fixtures load
and complete every authored word. They use `LET pick=...` and `GO TO 230` after
quitting; no direct memory writes are used. Public-facing captures come from
ordinary play, not those content fixtures.

The source/target audit checks ordered unique line numbers, literal targets,
TAP checksums, auto-start at ten, saved tokens, source hashes and executable
identity. The emulator reports 0.24.0; its exact binary SHA-256 and server identity
are in `verification/evidence/build.json` and `results.json`. The local binary
was built from Emu198x `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3`.

An initial full-board redraw repeatedly scanned guess history for each alphabet
cell. It delayed readiness by up to 325 additional emulated frames in the test.
The current program updates one alphabet cell and the dynamic fields during
play, reserving full redraws for new words, menus and results. Ordinary guesses
reached input readiness within 30 polling frames after the test key event;
the largest result transition required 110. These exclude the input helper's
key/release frames and are configuration-specific observations, not human
reaction times or original-hardware measurements.

The opening, revealed word, repeated guess, missed letter, pause and both ending
captures were inspected. Native execution establishes behaviour; player feedback
must still establish whether the word choices and pacing are enjoyable. The
existing website lessons are unchanged, and the prototype is not published.
