# Character codes: assessor notes

No learner is available. Every learner outcome below is **not observed**. Keep
this file separate from LEARNER-TASKS during the trial. Technical correctness
and browser checks cannot establish educational effectiveness.

Record the learner's experience, page revision and device/browser. Ask them to
think aloud without teaching the answer. For each task retain the prediction,
explanation, changes of mind, time spent if useful, help requested and help given.
Distinguish independent success, success after reading the answer, success after
coaching, incomplete work and unclear evidence. Do not infer understanding from
repeating the displayed output. Stop or pause if they wish.

| Task | Expected distinction | Learner outcome |
| --- | --- | --- |
| 1: predict | CODE "7" is 55; subtracting CODE "0" (48) gives 7 for a validated single digit. A gives 17 but is not a digit. | Not observed |
| 2: explain | Quantity, character, encoded code and drawn glyph are distinct. Check the encoding and the operation's table. | Not observed |
| 3: diagnose | Only "7" passes length-one and digit-range checks. CODE "73" is 55 on Spectrum BASIC; CODE empty is 0. Neither converts 73. | Not observed |
| 4: mask | A→a; a→a; 7→7; @→backtick. Setting a bit does not toggle it or validate a letter. | Not observed |
| 5: modify | Guard 65–90 for capitals, 97–122 for lower case; set 32 or clear with 223 respectively. Reject or deliberately preserve nonletters. Test both endpoints and neighbours. | Not observed |
| 6: create | Check exactly one character and code 48–57 before subtraction. Successful 7→7; reject empty, 73, A. Other valid examples accepted. | Not observed |
| Optional BASIC | Quoted text is a sequence of characters; a string variable stores it. No demand to have completed the BASIC arc. | Not observed |
| Optional C64 | In the chart's upper-case example, PRINT uses PETSCII 65; screen memory uses screen code 1. Check selected character set as well as destination. | Not observed |

The native audit observed twelve Spectrum ROM outputs and thirteen representative
Z80 cases. It did not execute teaching notation, C64 code or the complete BASIC
arc in the browser. Spectrum VAL evaluates a numeric expression: VAL "2*3" is 6.
Do not recommend it as a general safe digit-only parser. The public lesson leaves
language-specific whole-string parsing to the chosen language.

A learner may reasonably choose a response other than rejection for nonletters
in a case converter; require them to state that contract. In the one-digit task,
rejection is explicit. A glyph is a drawn form, not the numeric character code;
raw screen memory may use another numbering. The optional C64 comparison is
source-checked only in this slice.

After a real trial, file reproducible blockers in the owning repository, link
this pack and record the observation without guessing its cause. Revise the
lesson from evidence, then repeat only the affected tasks. Keep #114/#115/#124
open until their broader acceptance criteria are met.
