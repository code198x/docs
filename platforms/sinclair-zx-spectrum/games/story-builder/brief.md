# Story Builder — Brief

**Title (working):** Story Builder
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 1 of 8
**Headline concept:** Output — the first program speaks
**Embedded concept:** First impressions — what the player sees first shapes everything after
**Topics:** 4 topics, ~4–6 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that a program is a conversation — the computer speaks with PRINT, listens with INPUT, and assembles something from what it hears — so the learner arrives at Lucky Number already comfortable with the idea that programs respond to people.

---

## 2. Classic Ancestors

- **Mad Libs** (Roger Price & Leonard Stern, 1958) — the original fill-in-the-blanks word game. The mechanic: provide words without knowing the context, then read the absurd result. Travelled to every home computer as a type-in staple.
- **Usborne type-in tradition** — *Computer Spacegames* (1982) and *Practise Your BASIC* (1983) open with programs that PRINT and INPUT before anything else. The very first listing in most Usborne books is a conversation between the player and the computer.

---

## 3. Core Experience

Answer a few silly questions, then read back the story the computer built from your words. The laugh when the story appears — your words in ridiculous context — is the moment the learner realises the program *used* what they typed. Short, repeatable, and the kind of thing you show someone.

---

## 4. Visual Direction

- Dark theme (BORDER 0, PAPER 0, INK 7) from unit 2 onwards — recipe line, taught formally in unit 8.
- Title centred with PRINT AT, BRIGHT 1. DRAW quill/pen illustration on title screen (~4 DRAW commands).
- Block-graphic divider (CHR$ 131) between title and questions in unit 8.
- Story reveal: cyan INK on black — the colour shift marks "this is the output."
- The screen looks designed from the start. No grey-on-grey units.

---

## 5. Audio Direction

- **Silent** during questions — the learner is typing.
- **One BEEP** when the story starts printing — a "here it comes" signal.
- Deliberately minimal. Sound arrives properly in later games; here the focus is text.

---

## 6. Anti-goals

- No loops — the program runs once, top to bottom. GO TO arrives in Lucky Number.
- No randomness — the learner's words are the content. RND arrives in Lucky Number.
- No decisions — no IF/THEN branching. The program always does the same thing with different words. Decisions arrive in Lucky Number.
- No game state — no score, no win condition. This is a toy, not a game. The curriculum names it as a "program" not a "game" in the prose.
- Maximum 20 lines of BASIC at the final topic.

---

## 7. Topic Progression

1. **Hello, Spectrum.** Type `10 PRINT "Hello"`. Type `RUN`. The screen prints `Hello`. Try changing the word. Try adding more PRINT lines. Try `CLS` to clear the screen first. The learner's first act: telling the computer what to say, and watching it obey. **New:** PRINT, RUN, line numbers, CLS. **Program:** 3–5 lines of PRINT statements. **Polish beat:** which words did you choose? You're already making decisions about what the program says.

2. **Asking questions.** Add `INPUT "What is your name? "; n$`. The computer pauses and waits. Whatever the learner types goes into `n$`. Then `PRINT "Hello, "; n$` proves the computer remembered. Add two more INPUTs — an adjective, an animal. The program now knows three things about the player's imagination. **New:** INPUT, string variables (`n$`), semicolons in PRINT. **Program:** ~8 lines. **Polish beat:** which questions did you choose? The sillier the question, the better the result.

3. **The big reveal.** Add PRINT lines that weave the player's words into a short story: `PRINT "Once upon a time, "; n$; " the "; a$; " "; b$`. Add more sentences. The story should be 4–6 lines of narrative, absurd by construction. The learner sees their words used in a context they didn't expect — that's the Mad Libs payoff. **New:** string concatenation with semicolons, multi-part PRINT. **Program:** ~15 lines. **Polish beat:** read it aloud. Does it make someone laugh? If not, change the story template.

4. **Make it yours.** The program works, but it's your story template. Change the questions — ask for a colour, a place, a food, a number. Change the story — write your own sentences that use the answers. Add a title at the top (`PRINT "*** STORY BUILDER ***"`). Add `PAUSE 0` before the story so the player has to press a key ("Press any key for your story..."). Add a colour shift: `INK 5` (cyan) before the story prints. The learner now owns a program they made choices about — and it's the kind of thing they want to show someone else. **New:** PAUSE, INK (touched lightly — colour taught properly in Bright Spark). **Program:** ~18–20 lines. **Polish beat:** show it to someone. Watch their face when the story appears. That reaction is what programs are for.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new concept per topic (PRINT → INPUT → concatenation → polish)
- [ ] The final story is genuinely funny when read aloud with typical answers
- [ ] No BASIC concepts from later games leak in (no GO TO, no IF, no RND, no LET with numbers)
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **basic** — INPUT-to-PRINT pipeline: ask questions, store in string variables, weave into output. The simplest form of "gather data, produce result" — the pattern behind every form, every report, every template engine.

---

## 10. Vault Tie-ins

- **Mad Libs** (Price & Stern, 1958) — the fill-in-the-blanks word game as cultural ancestor.
- **Usborne computer books** — *Computer Spacegames*, *Practise Your BASIC* as the pedagogical tradition this volume follows.
- ZX Spectrum keyboard modes (K/L) — the learner's first encounter with the Spectrum's modal keyboard.
