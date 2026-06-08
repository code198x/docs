# Oracle Stone — Brief

**Title (working):** Oracle Stone
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 3 of 8
**Headline concept:** Chance — the program decides
**Embedded concept:** Anticipation — the pause before the answer matters more than the answer
**Topics:** 5 topics, ~5–7 hours
**Constraint position:** period-faithful

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that chaining IF/THEN with RND creates the illusion of a thinking program — so the learner understands that "the computer chose" is really "the programmer wrote the choices and the computer picked one," setting up the deliberate decision-making in Reflex and the structured randomness in Dice Roller.

---

## 2. Classic Ancestors

- **Magic 8-Ball** (Mattel, 1950) — the original fortune-telling toy. Shake it, read the answer in the window. Twenty pre-written responses, randomly selected. The mechanic: the illusion of wisdom from a bounded set of answers.
- **Fortune-teller type-ins** — a staple of early home-computer magazines and books. *Input* magazine, *Computer Spacegames*, and dozens of Spectrum listings published variants. The program pretends to know your future; the player pretends to believe it.

---

## 3. Core Experience

Type a question — any question. The screen pauses dramatically, then reveals the Oracle's answer. The answer is random but delivered with enough ceremony that the player half-believes it. Short, silly, and endlessly repeatable — the kind of program you pass around a room.

---

## 4. Visual Direction

- Blue theme (BORDER 1, PAPER 1, INK 7) from unit 1. Mystical atmosphere from the start, not deferred to unit 9.
- DRAW crystal ball on title screen (CIRCLE + DRAW base, ~5 commands).
- Pondering animation: dots appear one by one (`. . .`) with descending BEEP tones. Replaces static PAUSE/BEEP block.
- FLASH 1 on the Oracle's answer — blinks on screen, mystical and arresting.
- Block-graphic frame (CHR$ 143 in INK 5 cyan) around the answer instead of equals signs.

---

## 5. Audio Direction

- **Dramatic pause with sound.** A descending or wavering tone sequence while the Oracle "thinks" — 3–4 BEEPs over 2 seconds. This is the anticipation: the sound says "something is about to happen."
- **Reveal BEEP.** A single clear tone when the answer appears.
- **No other sound.** The silence around the reveal makes the reveal louder.

---

## 6. Anti-goals

- No real intelligence — the Oracle picks from a fixed list. No parsing of the question, no keyword matching. The question is ignored entirely; only the ceremony of asking matters.
- No DATA/READ — answers are selected via chained IF/THEN on a random number, not read from a DATA block. DATA/READ arrives at Cipher (V2 slot 9).
- No loops — the program runs once per question. The learner runs it again manually. GO TO is available from Lucky Number but deliberately unused here to keep the program linear and short.
- No scoring or tracking — no count of questions asked, no history. Each consultation stands alone.
- Maximum ~15–20 lines of BASIC.

---

## 7. Topic Progression

1. **Ask the Oracle.** `INPUT "Ask your question: "; q$`. The computer waits for the player to type a question. Then `PRINT "The Oracle says... YES"`. The answer is always YES. Trivial — but the shape is there: ask, then answer. **New:** reinforcement of INPUT/PRINT from Lucky Number. **Program:** 3 lines. **Polish beat:** write the prompt in the Oracle's voice — "Speak, mortal" feels different from "Type your question."

2. **The Oracle chooses.** Replace the fixed answer with a random one. `LET r = INT(RND*4)+1`. Then chain four IF/THEN lines: `IF r = 1 THEN PRINT "YES"`, `IF r = 2 THEN PRINT "NO"`, `IF r = 3 THEN PRINT "PERHAPS"`, `IF r = 4 THEN PRINT "ASK AGAIN"`. Run it several times — the Oracle gives different answers. The learner wrote every possible answer, but the *player* doesn't know which one is coming. That gap is **Chance**. **New:** chained IF/THEN on a random number (pattern, not new keywords). **Program:** ~8 lines. **Polish beat:** write answers that sound mystical, not mechanical. "THE SIGNS POINT TO YES" beats "YES."

3. **Make it dramatic.** The answer appears instantly — too fast for a mystical Oracle. Add a thinking sequence: `PRINT "The Oracle ponders..."` followed by `PAUSE 50` and 3–4 BEEPs with descending pitch. The pause builds **anticipation** — the embedded concept. The answer means more when you've waited for it. Add `CLS` before the reveal so the answer gets the screen to itself. **New:** PAUSE for dramatic timing, BEEP sequences for atmosphere. **Program:** ~12 lines. **Polish beat:** how long should the Oracle think? Too short feels fake; too long feels broken. Find the sweet spot.

4. **More answers, more mystery.** Four answers isn't enough — the player sees repeats quickly. Expand to 8 or 10: "THE STARS SAY YES", "ABSOLUTELY NOT", "NOT ON A TUESDAY", "THE ORACLE IS UNSURE", "SIGNS POINT TO MAYBE", "DO NOT ASK AGAIN". More chained IF/THEN lines, wider RND range. The Oracle starts to feel like it has a personality. **New:** scaling the chained-IF pattern (more branches, same structure). **Program:** ~16 lines. **Polish beat:** write at least one answer that makes people laugh. The funny answers are the ones people remember.

5. **The Oracle's chamber.** The program works but looks like text on a screen. Add a decorative frame: a border of asterisks or dashes around the answer using PRINT. Add a title — "*** THE ORACLE STONE ***" — in a different colour (INK). Add PAPER 1 (dark blue) and INK 5 (cyan) for a mystical palette. The program now looks like a place, not a prompt. **New:** PRINT as layout (decorative frames), INK/PAPER reinforcement. **Program:** ~18–20 lines. **Polish beat:** does the screen look like somewhere you'd go to ask a question? If the colours and framing create a mood, the Oracle works even before you type.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] The chained-IF pattern is clear — the learner can add more answers by following the pattern
- [ ] The dramatic pause creates genuine anticipation (test: does the player lean forward?)
- [ ] At least 8 answers in the final version, with a mix of yes/no/maybe/funny
- [ ] The visual framing creates atmosphere — dark background, bright answers, decorative border
- [ ] No new BASIC keywords introduced (this is a pattern game, not a keyword game)
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **basic** — chained IF/THEN selection: `LET r = INT(RND*n)+1` followed by `IF r = 1 THEN ...` / `IF r = 2 THEN ...`. The pattern for selecting from a fixed set without arrays or DATA. Simple, readable, and the learner's first encounter with "structure as a substitute for data structures."
- **basic** — dramatic reveal: PAUSE + BEEP sequence before a result. The pattern of building anticipation through timing — used in every game that has a moment of revelation (card flips, door openings, result screens).

---

## 10. Vault Tie-ins

- **Magic 8-Ball** (Mattel, 1950) — the fortune-telling toy as cultural ancestor.
- **Fortune-teller type-ins** — magazine listings and Usborne programs in the tradition.
- **Chance and randomness in game design** — the design principle that random selection from authored content creates the *illusion* of intelligence.
