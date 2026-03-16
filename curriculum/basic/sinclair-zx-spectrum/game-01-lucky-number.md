# Game 01: Lucky Number

**Track:** Spectrum BASIC
**Genre:** Number guessing game
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~100 (starter program), ~20 understood by end

---

## Premise

The computer picks a number between 1 and 100. You guess. The computer tells you higher or lower. Keep guessing until you find it.

This is the very first program the learner encounters. They have never programmed before. But their first experience of the Spectrum isn't `10 PRINT "Hello"` on a blank screen — it's typing in a complete, visually impressive game and watching it come alive. A rainbow title screen. Big block-pixel letters. A temperature bar that shifts from blue to white. Sound effects. A victory celebration.

The learner types in the full program before they understand any of it. This mirrors how millions of children first encountered programming in the 1980s: type-in listings from magazines. You typed the lines, you ran the program, you marvelled at the result, and then — slowly — you started to understand how it worked.

Over the eight units that follow, the learner takes the program apart — but they never leave it. Each unit teaches a concept by modifying the running game. The learner changes what the game says, what it knows, what it asks, how it decides, and how it looks. Every unit produces a visible, runnable result. The visual subroutines (the rainbow cascade, the block-pixel fonts, the temperature bar) remain black boxes for now — they're magic. What matters is that each concept is understood through its visual effect on the game.

By the end of Game 1, the learner understands variables, input, decisions, and loops. They've customised the game with their own messages, colours, and scoring. And their very first Spectrum program was something that looked and sounded like a real game.

---

## Core Mechanics

The player types a number. The program compares it to a secret number and prints "Too high", "Too low", or "You got it!" The game loops until the player guesses correctly. The secret number is random each time. A temperature bar shows how close the guess is. The current guess is displayed as large block-pixel digits. Border colour shifts with distance. Sound effects punctuate every guess and celebrate a win.

---

## The Starter Program

The learner types in a ~100-line program in Unit 1. This program includes:

- **Title screen:** Rainbow cascade (rows 0-7 in ascending PAPER colours), block-pixel "LUCKY NUMBER" rendered from DATA strings, "Press any key" prompt with FLASH.
- **Game screen:** Header bar in PAPER 1, guess counter, temperature bar (blue→yellow→red→white), large block-pixel digit display of the current guess, border colour feedback, directional hints.
- **Win screen:** Border strobe celebration, ascending BEEP tones, green colour flood across the temperature bar, guess count and scoring tier message, play again prompt.
- **Subroutines:** Digit renderer at line 8000 (draws a 4×5 block-pixel digit from DATA), number renderer at 8200 (centres 1-3 digit numbers on screen). These are black boxes — the learner types them in but doesn't need to understand them yet.
- **DATA statements:** Block-pixel font patterns for "LUCKY" and "NUMBER" (lines 5000-5015), digit patterns 0-9 (lines 5100-5195).

The program uses concepts from across the first six games: FOR/NEXT, PRINT AT, INK/PAPER/BORDER/BRIGHT, BEEP, DATA/READ/RESTORE, GO SUB/RETURN. None of these are formally taught in Game 1. They arrive via the starter program and are understood later, each in the game that introduces them properly.

The game logic — the part the learner will understand by Unit 8 — is roughly 20 lines buried within the larger program. Everything else is visual scaffolding.

---

## Unit Breakdown

### Unit 1: The Magic Program

**Concept:** What a program is, line numbers, the Spectrum keyboard (K-mode and L-mode), RUN

The learner types in the full Lucky Number program from a guided listing. This is a type-in experience — follow the listing, line by line.

Four checkpoints break the type-in into stages. At each checkpoint, the learner types RUN and sees the program so far:

1. **Lines 1-60** → RUN. The screen goes black, then the rainbow cascade fills the top eight rows — eight bands of colour sweeping left to right, each with a rising tone. The learner's first moment of wonder.
2. **Lines 70-240** → RUN. The rainbow appears again, then block-pixel "LUCKY NUMBER" materialises below it in yellow and cyan. A flashing "Press any key" prompt appears at the bottom. The title screen is complete.
3. **Lines 250-680 + 5100-5195 + 8000-8440** → RUN. After the title screen, the game begins: a blue header bar, a guess counter, and a working game. The temperature bar fills with colour. Big digits appear. The border shifts. The game plays.
4. **Lines 700-930 + 5000-5015** → RUN. The full game. Win and the border strobes random colours, the temperature bar floods green, ascending tones play, a scoring tier appears. Complete.

Each checkpoint is a reward. If something looks wrong, the learner can compare their screen against the expected result and find the mistake before typing more.

**Visual moments:** Rainbow cascade building row by row. Block-pixel title appearing. Temperature bar filling. Big digits rendering. Win celebration with border strobe and green flood.

---

### Unit 2: Changing What It Says

**Concept:** PRINT, strings, how line numbers control order

The game talks to the player through PRINT. Every message on screen — "Too low!", "Too high!", "YOU GOT IT!", "Incredible!" — is a string inside a PRINT command. The learner finds these lines and changes them.

**Modifications to Lucky Number:**
- Change `"Too low!"` (line 660) to `"Warmer..."` — RUN and guess low. The new message appears in yellow.
- Change `"Too high!"` (line 670) to `"Cooler..."` — RUN and guess high. The new message appears in magenta.
- Change `"YOU GOT IT!"` (line 850) to their own victory message — RUN and win. Their words flash on screen in bright green.
- Change the scoring tier messages (lines 880-896) — their own ratings instead of "Incredible!" and "Keep practising!"

**The minimal example:** After modifying the game, the learner creates a fresh two-line program to understand PRINT in isolation: `10 PRINT "Hello"` / `20 PRINT "World"`. One instruction, one result. Two instructions, two results, in order. Then back to Lucky Number — PRINT does the same thing there, just with colour and positioning added (which they'll learn in later games).

**Visual moments:** The game with personalised messages. The feedback text changing colour. Their victory message flashing on screen.

---

### Unit 3: Changing What It Knows

**Concept:** LET, numeric variables, string variables

Every number the game uses is stored in a variable. Change the variable, change the game.

**Modifications to Lucky Number:**
- Find `LET n = INT(RND*100)+1` (line 280). Change it to `LET n = 50`. RUN. Now the learner knows the answer. The game still works — the temperature bar climbs, the big digits track the guess, the border shifts — but the surprise is gone. The variable `n` controls everything.
- Find `LET pc = 6` (line 430). Change `6` to `2`. RUN and guess. The big digits render in red instead of yellow. One number changed the look of the game.
- Find `LET pc = 4` (line 770). Change `4` to `5`. RUN and win. The victory digits render in cyan instead of green.
- Change the scoring thresholds: `IF c<=5` (line 880) to `IF c<=3`. Now "Incredible!" requires three guesses, not five. Harder to earn.

**The key insight:** LET stores a number. That number controls something visible. Change the number, change what the game does. The learner doesn't need to understand the subroutines to know that `pc` controls the digit colour — they can see it.

**Visual moments:** Big digits in red instead of yellow. Victory digits in cyan instead of green. The game with a known answer (the temperature bar always climbs to maximum).

---

### Unit 4: Asking the Player

**Concept:** INPUT, prompts, string variables in context

INPUT is the moment the game stops and listens. Without it, the program runs and the player watches. With it, the player participates.

**Modifications to Lucky Number:**
- Find `INPUT "Your guess (1-100): "; g` (line 400). Change the prompt: `INPUT "Pick a number: "; g`. RUN — the new prompt appears at the bottom of the screen.
- Add a line before the game starts: `270 INPUT "What is your name? "; p$`. The game asks for the player's name. The variable `p$` holds whatever they type.
- Change the win message (line 870) to include the name: `PRINT AT 16,7; INK 7; "Well done, "; p$; "!"`. RUN, enter a name, win the game. The victory screen greets them personally.
- Change the play-again prompt (line 898) to: `PRINT AT 20,5; INK 7; "Play again, "; p$; "? (y/n)"`. The game remembers their name throughout.

**The key insight:** INPUT is what makes a program interactive. The player types, the variable remembers, and the game uses it. Strings (`p$`) hold text. Numbers (`g`) hold guesses. Both come from the player.

**Visual moments:** A personalised win screen with the player's name. A custom prompt at the bottom of the screen. The play-again message addressing the player by name.

---

### Unit 5: How It Decides

**Concept:** IF/THEN, `=`, `<`, `>` comparisons

Three lines are the heart of Lucky Number: `IF g = n`, `IF g < n`, `IF g > n`. But IF/THEN controls far more than the game logic — it controls every visual decision in the program. The border colour, the temperature bar bands, the scoring tiers, the feedback colours. Every visual change is an IF/THEN.

**Modifications to Lucky Number:**
- Find the border colour decisions (lines 590-620). Change `BORDER 2` to `BORDER 4` — when the guess is within 5, the border turns green instead of red. Change `BORDER 6` to `BORDER 3` — medium distance turns magenta instead of yellow. The border now uses the learner's colour scheme.
- Add a new scoring tier above "Incredible!": add line `878 IF c<=2 THEN PRINT AT 18,7; INK 7; BRIGHT 1; "LEGENDARY!": GO TO 897`. Win in two guesses and the new tier appears in bright white.
- Swap the feedback colours: in line 660, change `INK 6` to `INK 4` and in line 670, change `INK 3` to `INK 2`. "Too low" appears in green, "Too high" in red. The colour logic is reversed.
- Change the temperature bar colour bands (lines 510-540): swap `PAPER 1` and `PAPER 2`. The bar starts red-hot and ends cold blue — an inverted thermometer.

**The key insight:** IF/THEN is a gate. If the condition is true, the instruction runs. If not, the program skips it. Every visual change in the game — every colour shift, every scoring message — passes through an IF/THEN gate. Change the condition or change the instruction, and the game looks different.

**Visual moments:** The border in a custom colour scheme. An inverted temperature bar (red→blue instead of blue→red). A new "LEGENDARY!" scoring tier in bright white. Feedback messages in swapped colours.

---

### Unit 6: The Loop That Makes It Live

**Concept:** GO TO, loops, REM

Delete line 680 (`GO TO 370`). RUN. Guess once. The game shows the temperature bar, the big digits, the border colour, the feedback — and then stops. One guess. No second chance. The visual elements appear once and freeze.

Put line 680 back: `680 GO TO 370`. RUN. Now the game loops. Every guess updates the temperature bar, redraws the digits, shifts the border, shows new feedback. The loop is what makes every visual element come alive. Without it, the game is a single static frame. With it, the game breathes.

**Modifications to Lucky Number:**
- Restore line 680. Confirm the game works again.
- Change `GO TO 370` to `GO TO 380` — skip the guess counter increment. RUN. The counter stays at 0 forever. The loop still runs, but it skips one step. GO TO controls exactly where the program jumps.
- Fix it back to `GO TO 370`.
- Add REM comments to the sections the learner now understands:
  - `250 REM === NEW GAME ===` (already there)
  - `370 REM === Guess loop ===` (already there)
  - `630 REM === Feedback ===` (already there)
  - `700 REM === WIN! ===` (already there)
  - The learner reads through the listing and sees that the REM comments mark the flow: setup → loop → win. The program has a shape.

**The key insight:** GO TO is the instruction that makes programs loop. Without it, a program runs once and stops. With it, visual elements update, counters increment, and the game keeps asking. The loop is the heartbeat.

**Visual moments:** The game frozen after one guess (no loop). The game alive again (loop restored). The listing with REM comments marking the structure.

---

### Unit 7: A Different Number Every Time

**Concept:** RND, INT, randomness

Remove `LET n = 50` (from Unit 3). Restore line 280 to `LET n = INT(RND*100)+1`. RUN. The game surprises again — the learner doesn't know the answer. The temperature bar starts cold and climbs unpredictably. The border shifts. The big digits show different numbers each time. Randomness makes the game replayable.

**Exploration:**
- `PRINT RND` in a fresh program. A decimal between 0 and 1. Run it again — a different number. Again — different. The computer is generating unpredictable values.
- `PRINT RND * 100` — a decimal between 0 and 100. `PRINT INT(RND * 100)` — a whole number. `PRINT INT(RND * 100) + 1` — a whole number between 1 and 100. That's the formula in Lucky Number.
- Back in Lucky Number: find the win celebration (line 720): `BORDER INT(RND*8)`. That's RND choosing a random border colour for the strobe effect. Eight possible colours, chosen randomly, twenty times. That's why the celebration looks different every time.
- Change `RND*100` to `RND*50` in line 280. The range shrinks to 1-50. Also change the INPUT prompt and validation (line 410) to match. RUN — the temperature bar reacts more sharply to each guess because the range is smaller. The distance values are different, so the visual feedback changes character.

**Visual moments:** The game unpredictable again. The win celebration's random border strobe. The game with a 1-50 range — the temperature bar filling faster, the border shifting sooner.

---

### Unit 8: Your Version

**Concept:** Counting with variables, combining strings and numbers in PRINT, experimentation and ownership

The learner now understands the game logic: INPUT asks, LET stores, IF/THEN decides, GO TO loops, RND randomises. They've already changed messages, colours, thresholds, and the range. This unit pushes further — the goal is a version that looks, sounds, and feels like their own game.

**Modifications to Lucky Number:**
- **Change the range** to 1-200. Update line 280 (`RND*200`), line 410 (validation), and the INPUT prompt. The temperature bar spreads across a wider range — guesses feel colder because the distance is greater. The big digits now show three-digit numbers.
- **Design a colour scheme.** Choose border colours for each distance band (lines 590-620). Choose temperature bar colours (lines 510-540). Choose feedback text colours (lines 660-670). Choose the win digit colour (line 770). The learner picks every colour in the game.
- **Change every BEEP.** The guess tone (line 570): change the pitch formula. The win tones (line 730): change the base pitch and increment. The temperature bar flood (line 810): change the pitch. The game should sound different.
- **Rewrite the scoring tiers.** Five tiers instead of four. New thresholds, new messages, new colours. The learner decides what counts as "Incredible!" in their version.
- **Change the title.** Edit the "LUCKY NUMBER" text in lines 340 and the DATA at 5000-5015. The header bar can say anything — the block-pixel title on the title screen is harder to change (it's DATA-driven), but the learner can change the PAPER colour of the title words (lines 120, 200) without understanding the DATA.
- **Add a guess counter message.** After the guess count display, add a line that prints encouragement based on how many guesses have been made: `385 IF c>10 THEN PRINT AT 2,20; INK 2; "Keep trying!"`. The game talks more as the count climbs.

**The key insight:** The learner has changed roughly 20 lines of a 100-line program and made it feel entirely different. They understand the game logic. The visual subroutines are still black boxes — and that's fine. They don't need to understand the rainbow cascade to change the border colours. They don't need to understand the digit renderer to change what colour the digits appear in. The program is theirs.

**Visual moments:** A game with a completely custom colour scheme. A 1-200 range with three-digit numbers. Custom scoring tiers. Custom sounds. A game that looks and sounds different from the original — because the learner changed it.

---

**Milestone:** The learner has typed in, run, and understood a complete interactive program — by modifying it, not by studying it in isolation. They know PRINT, LET, INPUT, IF/THEN, GO TO, RND, and INT. They've changed the messages, the colours, the range, the scoring, and the sounds. Every unit produced a visible result. And their very first Spectrum program was something worth showing to a friend.

---

## Technical Notes

### Key Variables

```
n   - the secret number (overridden to 50 in unit 3, restored to random in unit 7)
g   - the player's guess
c   - guess counter
d   - distance from correct answer (ABS(g-n))
h   - heat bar length
pc  - PAPER colour for digit renderer
v   - value to display as big digits
dr  - display row for digit renderer
dc  - display column for digit renderer
f   - digit value (0-9) for single digit renderer
p$  - player name (added in unit 4)
```

### The Subroutine Black Boxes

The starter program contains two subroutines the learner doesn't need to understand in Game 1:

- **Line 8000 (Draw digit):** Takes a digit value `f` and screen position `dr`, `dc`, reads 5 rows of DATA for that digit, prints PAPER-coloured spaces where the pattern has a "1". Each digit is 4 columns x 5 rows.
- **Line 8200 (Draw number):** Takes a number `v`, clears the display area, splits into digits, centres them on screen, calls the digit renderer for each.

These subroutines use FOR/NEXT (Game 3), PRINT AT (Game 4), DATA/READ/RESTORE (Game 5), and GO SUB/RETURN (Game 6). Each concept is formally introduced in the game listed. Until then, the subroutines are magic that works.

### Visual Elements the Learner Can Modify Without Understanding

The learner doesn't need to understand how a visual element works to change its parameters:

| What to change | Which line | What to modify | Visual effect |
|----------------|-----------|----------------|---------------|
| Big digit colour | 430 | `LET pc = 6` → different number | Digits render in a different colour |
| Win digit colour | 770 | `LET pc = 4` → different number | Victory digits change colour |
| Border near/far colours | 590-620 | `BORDER n` → different number | Border feedback uses new colours |
| Temperature bar colours | 510-540 | `PAPER n` → different number | Bar bands change colour |
| Feedback text colours | 660-670 | `INK n` → different number | "Too low"/"Too high" change colour |
| Title word colours | 120, 200 | `PAPER n` → different number | "LUCKY"/"NUMBER" change colour |
| Header bar colour | 320, 340 | `PAPER n` → different number | Top bar changes colour |
| Guess sound pitch | 570 | Change the formula | Sound changes pitch per guess |
| Win sound | 730 | Change `10+i` | Victory tones shift pitch |

This table is a reference for units 3-8. The learner can experiment with any of these at any point.

### Line Numbering

- 1-9: Setup (BORDER, PAPER, INK, CLS)
- 10-60: Rainbow cascade (title screen)
- 70-220: Block-pixel title rendering from DATA
- 230-240: "Press any key" prompt
- 250-680: Game logic (the part the learner understands by Unit 8)
- 700-930: Win screen and play again
- 5000-5015: Title font DATA ("LUCKY", "NUMBER")
- 5100-5195: Digit font DATA (0-9)
- 8000-8080: Digit renderer subroutine
- 8200-8440: Number renderer subroutine

### Memory

~3 KB including DATA statements and subroutines. Comfortable on a 48K Spectrum.

### Spectrum-Specific Notes

- The Spectrum 48K has no ELSE keyword. Each comparison needs its own IF/THEN line.
- The K-mode cursor (keyword mode) appears when the Spectrum expects a command. The learner needs to understand this before they can type their first line. Unit 1 addresses this directly as part of the type-in experience.
- `GO TO` is two words on the Spectrum, not `GOTO`.
- The type-in experience in Unit 1 should include guidance on common mistakes: missing spaces, wrong mode (K vs L), mistyped line numbers. Typing errors are part of the learning.

### Pedagogical Notes

The "type first, understand later" approach mirrors the magazine type-in culture of the 1980s. Research on worked examples (Sweller, 1988) supports studying complete solutions before constructing new ones — the learner builds a mental model from the whole before tackling the parts.

The risk is that 100 lines feels overwhelming. Mitigation: the type-in is guided step by step, with four checkpoints ("type lines 1-60, then RUN — you should see the rainbow"). The learner sees progress before they've finished typing. If something goes wrong, they can RUN what they have so far and compare.

The revised approach (v3.0) keeps the learner inside Lucky Number for all eight units. Concepts are taught by modifying the running game, not by building toy examples in isolation. This means:
- Every unit produces a visible, runnable result
- The learner never loses contact with the visual program
- Each concept is understood through its effect on something the learner can see
- The brief standalone example (e.g. `10 PRINT "Hello"` in Unit 2) exists to isolate the concept, not to replace the game as the primary learning context

The visual subroutines must NOT be explained in Game 1. Premature explanation would overload the learner and steal the teaching moment from the later game where each concept is properly introduced. The correct response to "how does the rainbow work?" is "we'll get to that — for now, it's magic."

---

## Changelog

- **v3.0 (2026-03-16):** Revised unit breakdown. Concepts taught by modifying the running game, not in isolation. Each unit produces visible results. Added "Visual Elements the Learner Can Modify" reference table. Units are denser with visual moments while keeping the count at 8.
- **v2.0 (2026-03-16):** Rewritten for starter-kit approach. The learner types in a complete visual program first, then learns the game logic over 8 units. Visual subroutines are black boxes understood in later games.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum. 20-line text-only program.
