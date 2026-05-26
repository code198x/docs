# Locksmith — Brief

**Title (working):** Locksmith
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 3 of 8 (slot 11)
**Headline concept:** Deduction — encoded clues, reasoned through
**Embedded concept:** Information layering — each guess reveals more than the answer
**Topics:** 8 topics, ~8–12 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach numeric arrays as indexed storage for game state — so the learner arrives at Sonar able to use arrays for grids, not just lists.

---

## 2. Classic Ancestors

- **Mastermind** (Mordecai Meirowitz, 1970) — the code-breaking board game. The mechanic: guess a hidden sequence, receive clues ("right colour right place", "right colour wrong place"), reason your way to the answer.
- **Bulls and Cows** — the pencil-and-paper predecessor. "Bulls" for exact matches, "cows" for right-digit-wrong-position. Predates Mastermind by decades.

---

## 3. Core Experience

The computer picks a secret code — four coloured pegs (represented as digits 1–6). You guess a code. The computer tells you how many are the right colour in the right position (bulls) and how many are the right colour in the wrong position (cows). Reason through the clues. Crack the code in as few guesses as possible.

---

## 4. Visual Direction

- **Code display.** Four coloured squares (PAPER blocks) per guess, arranged in rows — one row per attempt. The screen fills from top to bottom as guesses accumulate. Each guess is a visual record the player can refer back to.
- **Clue display.** Bulls and cows shown alongside each guess row — small marks (asterisks for bulls, circles for cows) or a simple "2 bulls, 1 cow" text.
- **Hidden code.** Revealed at game end — the "aha" moment.
- **Magazine-screenshot test:** six rows of coloured guesses with clues beside each, the player narrowing in — you can read their reasoning from the screenshot.

---

## 5. Audio Direction

- **Bull.** High short tone per bull in the clue.
- **Cow.** Lower short tone per cow.
- **No bulls, no cows.** A flat tone — nothing matched.
- **Code cracked.** Ascending fanfare.

---

## 6. Level Design Direction

- **Content source:** The secret code is randomly generated at the start — no DATA needed. Code length (4) and colour count (6) are the difficulty parameters.
- **Difficulty curve.** Fixed difficulty — 4 pegs from 6 colours. The inherent difficulty of the deduction is the curve. Optional: the learner can adjust code length (3 for easy, 5 for hard) or colour count.
- **Scale:** 10 guesses allowed. Experienced Mastermind players can solve in 5–6; 10 gives beginners room.
- **Onboarding:** First guess is always uninformed — any 4 digits. The clue from the first guess is where deduction begins.

---

## 7. Anti-goals

- No computer-as-guesser mode — the player always guesses, the computer always sets. AI codebreaking is beyond V2 scope.
- No duplicate-colour option at first — each colour appears at most once in the code (simplifies the bulls/cows algorithm). Duplicates are an optional extension.
- No graphical pegs — colours shown as PAPER blocks or coloured numbers.
- Maximum ~45 lines of BASIC.

---

## 8. Topic Progression

1. **A secret code.** Generate a random 4-digit code using a numeric array: `DIM c(4)`. Fill with random values 1–6: `FOR i = 1 TO 4: LET c(i) = INT(RND*6)+1: NEXT i`. Display as hidden: `? ? ? ?`. **New:** DIM for numeric arrays, filling arrays with a FOR loop. **Program:** ~8 lines.

2. **The player guesses.** INPUT a 4-digit guess. Store in a second array: `DIM g(4)`. Parse the input digit by digit. Display the guess as coloured blocks. **New:** parsing a multi-digit input into array positions, displaying array contents. **Program:** ~14 lines.

3. **Counting bulls.** Compare each position: `IF c(i) = g(i)` — that is a bull. Count them. Display the bull count after the guess. **New:** position-by-position array comparison. **Program:** ~18 lines.

4. **Counting cows.** For each guess digit that is not a bull, check if it appears *anywhere* in the code (nested loop). Count cows. The nested loop — checking one array against another — is the core algorithm. **New:** nested FOR loops for cross-array searching. **Program:** ~24 lines.

5. **Multiple guesses.** Wrap in a loop: up to 10 guesses. Each guess prints on a new row with its clue alongside. Previous guesses remain visible — the screen is a history of reasoning. **New:** accumulating display (no CLS between guesses), guess-limited loop. **Program:** ~28 lines.

6. **Win and lose.** If all 4 are bulls, the player wins — reveal the code, show the guess count. If 10 guesses pass, reveal the code — "The code was: 3 1 5 2." **New:** win/lose conditions, revealing hidden state. **Program:** ~32 lines.

7. **Colour and polish.** Each digit value mapped to a PAPER colour (1=red, 2=blue, etc.). Guess rows display as coloured blocks instead of numbers. The visual record becomes a colour puzzle. Add the title screen and replay prompt. **New:** numeric-to-colour mapping, the game as a visual artefact. **Program:** ~40 lines.

8. **Make it yours.** Adjust the difficulty: code length 3 (easy) or 5 (hard), colour count 4 (easy) or 8 (hard). The arrays resize with DIM — the algorithm works unchanged. The design lesson: parameterised difficulty via array dimensions. **New:** parameterised design (one variable changes the game's feel). **Program:** ~45 lines.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] Bull counting is correct (right colour, right position)
- [ ] Cow counting is correct (right colour, wrong position) — no double-counting
- [ ] Guess history displays correctly without overwriting previous rows
- [ ] Win detection works (4 bulls)
- [ ] Code reveal works at game end (win or lose)
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **basic** — DIM numeric arrays: indexed storage for game state. The foundation of grids, inventories, and positional data.
- **basic** — position-by-position comparison: `IF a(i) = b(i)` across two arrays. The pattern behind every "how similar are these two sequences?" check.
- **basic** — nested FOR search: checking whether a value from one array appears anywhere in another. The simplest "contains?" algorithm.

---

## 11. Vault Tie-ins

- **Mastermind** (Mordecai Meirowitz, 1970) — the code-breaking board game as direct ancestor.
- **Bulls and Cows** — the pencil-and-paper predecessor to Mastermind.
- **Deduction as game design** — the principle that each move reveals information, and the player's skill is in extracting maximum information per guess.
