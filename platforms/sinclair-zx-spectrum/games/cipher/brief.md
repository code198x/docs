# Cipher — Brief

**Title (working):** Cipher
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 1 of 8 (slot 9)
**Headline concept:** Data-Driven — the content shapes the experience, not the code
**Embedded concept:** Difficulty curve via content — longer words are harder without changing any code
**Topics:** 8 topics, ~8–12 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach DATA/READ as a way to separate content from logic — so the learner understands that the same game engine can play differently by changing the data it reads, and arrives at Quiz Master with data-driven design as a working tool.

---

## 2. Classic Ancestors

- **Hangman** — the paper-and-pencil word-guessing game. Universal, ancient, and the canonical first DATA/READ program in home-computer magazines and books.
- **Usborne type-in tradition** — *Computer Spacegames* and *Practise Your BASIC* both include word-guessing games as DATA/READ demonstrations.

---

## 3. Core Experience

A row of dashes — one per letter. Guess a letter. If it is in the word, it appears in its correct position. If not, you lose a life. Guess the whole word before your lives run out. Each round is a fresh word from the hidden list; the player never knows what is coming.

---

## 4. Visual Direction

- **The word as dashes.** Centre-screen, large, clear. Each correct guess replaces a dash with a letter. The word gradually reveals itself — the visual payoff of each correct guess.
- **Lives display.** A simple count or a row of symbols that shrinks. No gallows — the curriculum avoids the hangman imagery.
- **Guessed letters.** A row of already-tried letters below the word, so the player does not repeat mistakes.
- **Magazine-screenshot test:** a half-revealed word — `_ I _ H E _` — with 3 lives remaining and a row of guessed letters below. The reader wants to solve it.

---

## 5. Audio Direction

- **Correct letter.** Short ascending tone — the satisfaction of a good guess.
- **Wrong letter.** Short low tone — a miss, not a punishment.
- **Word complete.** Brief fanfare.
- **Game over.** Low buzz, then the answer revealed.

---

## 6. Level Design Direction

- **Content source:** DATA/READ statements hold the word list. Each word is one DATA entry. The game reads a random word with RESTORE and a counted READ loop.
- **Difficulty curve via content.** Short words (3–4 letters) are easier because fewer guesses are needed and common letters cover more of the word. Long words (8+ letters) are harder. The game gets harder by including longer words in the DATA — no code change needed.
- **Scale:** 20–30 words in the initial list. The learner adds their own.
- **Onboarding:** The first word should be short and common (e.g., "CAT", "SUN"). The player learns the interface on an easy win.

---

## 7. Anti-goals

- No hangman figure — no gallows, no drawing of a person. Lives are a number, not a picture.
- No difficulty selection — word length *is* the difficulty. The list contains a mix.
- No categories — all words from one mixed pool. Categories arrive at Quiz Master.
- No two-player mode.
- Maximum ~40 lines of BASIC + DATA.

---

## 8. Topic Progression

1. **A hidden word.** `DATA "SPECTRUM": READ w$`. Print dashes for each letter: `FOR i = 1 TO LEN w$: PRINT "_ ";: NEXT i`. The word exists but is hidden. **New:** DATA/READ (the game's core tool). **Program:** ~6 lines.

2. **Guessing a letter.** `INPUT "Guess a letter: "; g$`. Loop through the word checking if `g$` matches each character: `IF w$(i) = g$ THEN ...`. Replace the matching dash with the letter. **New:** string indexing inside a search loop, replacing characters in a display string. **Program:** ~12 lines.

3. **Right and wrong.** Track wrong guesses with a counter. Display remaining lives. If lives reach zero, game over — reveal the word. If all dashes are filled, the player wins. **New:** win/lose conditions, revealing hidden state at game end. **Program:** ~18 lines.

4. **Guessed letters.** Store tried letters in a string: `LET tried$ = tried$ + g$`. Before accepting a guess, check if it has been tried: loop through `tried$`. Display the tried-letters row below the word. **New:** string-as-set (checking membership by scanning). **Program:** ~22 lines.

5. **Many words.** Add 20 words to DATA. Pick a random one: use RESTORE and a counted READ loop (`FOR i = 1 TO r: READ w$: NEXT i` where `r` is random). Each round is a different word. **New:** RESTORE (rewinding DATA), random selection from a DATA list. **Program:** ~28 lines + DATA.

6. **Making it look right.** CLS between rounds. PRINT AT for fixed positions — the word centre-screen, lives top-right, tried letters bottom. Add colour: green for correct letters, red for wrong guesses, white for dashes. **New:** PRINT AT layout for a structured game screen. **Program:** ~32 lines + DATA.

7. **Keeping score.** Track wins and losses across rounds. Display a running record: "Won 3 / Lost 1." Add a "Play again?" prompt. The DATA list makes replay natural — each round is a different word. **New:** persistent score across rounds. **Program:** ~36 lines + DATA.

8. **Make it yours.** Add your own words to the DATA. Write a title screen. Add a round counter. The design lesson: you changed the game's *content* without touching its *code*. The DATA is the level designer; the code is the engine. That separation — content vs logic — is the headline concept. **New:** none (polish topic). **Program:** ~40 lines + DATA.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] Every topic produces a working, runnable result
- [ ] DATA/READ word list is correct — no missing entries, no off-by-one in random selection
- [ ] RESTORE + counted READ correctly picks a random word
- [ ] String indexing correctly reveals matching letters
- [ ] Tried-letters check prevents duplicate guesses
- [ ] Win and loss conditions both work
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **basic** — DATA/READ content store: separate game data from game logic. The pattern behind every data-driven game — change the DATA, change the experience.
- **basic** — RESTORE + counted READ for random selection from a DATA list. The pre-array technique for picking from a set larger than chained-IF can handle.
- **basic** — string-as-set: `IF tried$(i) = g$` for membership checking. The simplest "have I seen this before?" pattern.

---

## 11. Vault Tie-ins

- **Hangman** — the paper-and-pencil word game as universal ancestor.
- **DATA/READ in BASIC** — the language feature that separates content from logic, enabling data-driven design.
- *Practise Your BASIC* (Usborne, 1983) — DATA/READ demonstrations as pedagogical precedent.
