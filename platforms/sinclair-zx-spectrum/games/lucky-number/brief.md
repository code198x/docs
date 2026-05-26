# Lucky Number — Brief

**Title (working):** Lucky Number
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 2 of 8
**Headline concept:** Response — the game communicates without words
**Embedded concept:** Juice — the non-essential signal that makes the essential feel alive
**Topics:** 9 topics, ~10–15 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that programs can respond to the player through colour, sound, and spatial cues — not just text — so the learner arrives at Oracle Stone understanding that a program's feedback channels are design choices, not accidents.

---

## 2. Classic Ancestors

- **Number-guessing games** — a universal magazine type-in staple from 1978 onwards. Every computing magazine published one; most home-computer manuals included one. The mechanic is ancient (the paper-and-pencil "higher/lower" game predates computers), but the computer version adds the possibility of *ambient feedback* — colour, sound, proximity cues — that paper can't do.
- **Usborne type-in tradition** — *Computer Spacegames* (1982) and *Practise Your BASIC* (1983). The gradual-build pedagogy: start with the smallest working program, add one concept per step.

---

## 3. Core Experience

Guess the number, watch the screen respond. The border shifts from cold blue to hot white as you close in. A low tone says "go higher"; a high tone says "go lower". The words confirm what the colours and sounds already told you. A short session — three to five minutes per round — that feels like a conversation with the machine.

---

## 4. Visual Direction

- **Border as thermometer.** Blue (cold, far away) through cyan, yellow, red to white (hot, very close). The player reads proximity from the edge of their vision before reading the text.
- **Text feedback centre-screen.** "Too high" / "Too low" / "Got it!" — functional, not decorative.
- **Win celebration.** Border strobes, ascending tones, congratulatory text with guess count. The only moment the program shouts.
- **Magazine-screenshot test:** the screen mid-guess with a white-hot border, "Too low!" on screen, and six previous guesses scrolled above — you can read the player's strategy from the screenshot.

---

## 5. Audio Direction

- **Directional BEEP on every guess.** `BEEP 0.1, (n - g) / 10` — ascending tone when the guess is too low (go higher), descending when too high (go lower). The player can close their eyes and still know which way to go.
- **Win fanfare.** Ascending scale or rapid trill — a brief celebration, not a composition.
- **Deliberately absent:** no title music, no background sound. The BEEPs are information, not decoration.

---

## 6. Anti-goals

- No graphics — no PLOT, no DRAW, no UDGs. The screen is text and colour only.
- No subroutines — no GO SUB. Code runs top to bottom with GO TO for the loop.
- No arrays — single variables only.
- No multi-game features — no difficulty select, no high-score table. One round, one number, one loop.
- Maximum ~25–35 lines of BASIC at the final topic.

---

## 7. Topic Progression

1. **Your first program.** `10 PRINT "Hello"`. `RUN`. The screen prints `Hello`. Try more PRINT lines. Try `5 CLS`. The learner already met PRINT in Story Builder — this is a quick warm-up, not a full introduction. **New:** reinforcement of PRINT, CLS, line numbers. **Program:** 3–5 lines. **Polish beat:** choose your welcome message — this is Lucky Number's opening screen.

2. **Remembering things.** `LET n = 42`. `PRINT n`. The computer remembers what you told it. Try `LET n = n + 1` — the value changes. Variables are named boxes that hold numbers. **New:** LET, numeric variables, arithmetic with variables. **Program:** ~5 lines. **Polish beat:** what number would you pick as the secret? That choice matters.

3. **Asking the player.** `INPUT "Your guess: "; g`. The computer pauses and waits. The player's answer goes into `g`. Then `PRINT "You said "; g` proves the computer heard them. The learner met INPUT with strings in Story Builder — now it works with numbers. **New:** INPUT with numeric variables (reinforces string INPUT from Story Builder). **Program:** ~6 lines. **Polish beat:** write a prompt that sounds like a game, not a form.

4. **Making decisions.** `IF g > n THEN PRINT "Too high"`. `IF g < n THEN PRINT "Too low"`. `IF g = n THEN PRINT "Got it!"`. The computer responds differently depending on the guess. Response — introduced in topic 1 as "the computer says what you told it to" — now has teeth: the computer reasons about your input. **New:** IF/THEN, comparisons (`=`, `<`, `>`). **Program:** ~8 lines. **Polish beat:** try `<>` — what does "not equal" feel like as feedback?

5. **Going round again.** The program stops after one guess. Add `GO TO 30` after the wrong-guess messages — the program loops back to INPUT and asks again. The game keeps going until the player wins. That loop is the *game loop* — the structural shape every interactive program shares. **New:** GO TO, loops, the concept of a game loop. **Program:** ~10 lines. **Polish beat:** REM out the GO TO and run it — feel the difference between one-shot and loop.

6. **A different number every time.** The secret is always 42. Replace `LET n = 42` with `LET n = INT(RND*100)+1`. Take it apart: RND gives 0–1, multiply by 100, INT rounds down, +1 shifts to 1–100. Add `RANDOMIZE` at line 1 so the sequence differs each run. The game is now replayable. **New:** RND, INT, RANDOMIZE, the range formula. **Program:** ~12 lines. **Polish beat:** try `INT(RND*10)+1` for easy, `INT(RND*1000)+1` for hard. One line changes the entire experience.

7. **Make it feel like a game.** The game works but speaks only in words. Compute the distance: `LET d = ABS(g - n)`. Set the border based on distance: blue when far, white when close. Now the screen *shows* how close you are before you read the text. **New:** ABS, BORDER, distance-driven feedback. **Program:** ~18 lines. **Polish beat:** play with the thresholds — when should the border shift from blue to cyan? From red to white? You're tuning feel, not logic.

8. **Sound that means something.** Add `BEEP 0.1, (n - g) / 10` after each guess. When the guess is too low, the tone ascends — go higher. When too high, the tone descends — go lower. The player can hear the direction without reading the text. This is *audio feedback* — sound carrying meaning, not decoration. **New:** BEEP (pitch + duration), the idea that sound can carry information. **Program:** ~22 lines. **Polish beat:** close your eyes and play by ear alone. If you can, the audio feedback works.

9. **Make it your own.** Lucky Number works. The final topic is polish — the layer that makes it *your* game. Add a title screen: a few PRINTs in your own voice, with `PAUSE 0` for drama. Add a guess counter: `LET c = c + 1` each guess, displayed at the end. Add ratings: under 5 guesses prints "Incredible!"; under 10 prints "Not bad"; otherwise "Keep trying". This layer — celebration, rating, presentation — is what later designers call **juice**: signal that isn't essential but makes the essential feel alive. The game works without it. Does it *feel* like a game without it? **New:** PAUSE, counter pattern (`c = c + 1`), multi-tier IF for ratings. **Program:** ~25–35 lines. **Polish beat:** show it to someone. Watch them play. The ratings are for them, not you.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new concept per topic — no topic introduces two major ideas
- [ ] Topic 5 produces a complete playable game (the "it works" moment is mid-game, not end)
- [ ] Distance-driven border feedback is visually readable — the learner can feel proximity from the border alone
- [ ] Directional BEEP carries meaning — a blindfolded player can tell "higher" from "lower"
- [ ] The final program is under 35 lines and every line is understood by the learner
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **basic** — distance-driven BORDER feedback: `ABS(g - n)` mapped to a colour range. The pattern — a numeric distance mapped to a visual range — recurs in every game with proximity, danger, or progress signals. Cross-platform.
- **audio** — directional BEEP: `BEEP 0.1, (n - g) / 10` produces ascending pitch when the guess is too low, descending when too high. Sound carrying semantic direction. Spectrum-specific in implementation; the design principle generalises.
- **basic** — counter pattern: `LET c = c + 1` for tracking guesses. The simplest accumulator — the foundation of scores, timers, and resource tracking in every game that follows.
- **basic** — range formula: `INT(RND*range)+base` for generating random integers in a specific range. Used in every game from here forward.

---

## 10. Vault Tie-ins

- **Number-guessing games** — the magazine type-in tradition; every major Spectrum magazine published variants.
- **Usborne computer books** — *Computer Spacegames* (1982), *Practise Your BASIC* (1983) as pedagogical ancestors.
- ZX Spectrum BORDER register — port $FE bit 2:0 colour output.
- ZX Spectrum BEEP command — single-channel square wave, duration + pitch.
