# Cipher — teaching progression

**Status:** The user authorised the compact lesson sequence around the native
prototype. Six lessons use five runnable checkpoints; the local lesson preview
requires review before publication. No larger game scope is introduced.

## Endpoint and teaching shape

The finished source remains byte-identical to
`code-samples/sinclair-zx-spectrum/basic/cipher/prototype/cipher.bas`.
The native trial uses stock 48K PAL Sinclair BASIC with deliberate silence,
direct letters, seven distinct mistakes, free repeats, pause, scores and a
24-word list. Existing published lessons stay available until replacement.

| Lesson | Checkpoint | Result and explanation |
|---|---|---|
| Reveal the matches | reveal | New ten-line program; hidden/revealed strings, LEN, loops, slicing and a fixed T guess; STOP |
| Choose a letter | guess | One press through a release gate; CODE/CHR$ case handling, letter validation and retained knowledge; unlimited guesses, Enter quits |
| Make a round | rules | Tried/missed strings, duplicate guard, seven-miss limit, endings, score retention and explicit pause/reset/quit; fixed BOTTLE |
| Read the board | board | Stored alphabet, one-/zero-based positions, two-row mapping, mistake markers and selective redraw; fixed BOTTLE |
| Choose another word | finished | DATA/READ/RESTORE, bounded random index, immediate-repeat rejection, title and complete replay |
| Keep Cipher | reuse finished | SAVE with LINE 10, tape export, fresh load and complete-cycle checks; program saving is not session persistence |

The early limits are explicit. The first program is a new listing, without an
instruction to add every line. Later instructions name exact additions,
replacements and deletions. Short checkpoints show full source directly; larger
ones show changed lines and provide complete source in a disclosure.

Check T revealing both positions in BOTTLE, L revealing one, Z revealing none,
retained guesses, free repeats and seven distinct misses. Explain why the word,
revealed string, history, miss list and alphabet answer different questions.
Keep Q and R available as guesses by moving their menu actions behind Enter.

Content guidance rejects word length as a complete difficulty scale. The total
must match the DATA count, and immediate-repeat rejection needs at least two
distinct entries. The current layout's authoring scope stays at four to eight
uppercase letters per word; there is no promised shuffled deck.

## Verification and integration

Enter all five sources independently through the ROM and save auto-starting
TAPs. Load them in fresh processes; check intermediate rules and menus and run
the complete prototype suite against the finished tape. Bind evidence to source
and executable identities; label diagnostic setup separately from ordinary play.
Intermediate execution is not independent learner review.

Prepare the overview and six topic pages, preserve numeric identities, and
redirect old canonical/legacy topics by subject. Place Cipher in Boards and
deduction locally; keep the release note a draft. Check production, desktop and
mobile pages, keyboard disclosure, images and accessibility before lesson review.

Sources are Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC
Programming*, second edition (1983), especially chapters 3–6, 8–11, 14–16, 18
and 20. The primary text was inspected for DATA/RESTORE and slicing; native
execution checks the maintained examples. Learner pages cite public chapters.

See [implementation and evidence](lessons.md).
