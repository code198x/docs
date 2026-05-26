# Quiz Master — Brief

**Title (working):** Quiz Master
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 2 of 8 (slot 10)
**Headline concept:** Progression — the player grows, the score climbs
**Embedded concept:** Ratings as social proof — "Quiz Master" feels like an earned title
**Topics:** 10 topics, ~10–14 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach DIM arrays and RESTORE as tools for structured, indexed data — so the learner arrives at Locksmith able to store and retrieve values by position, not just sequentially.

---

## 2. Classic Ancestors

- **Trivial Pursuit** (Horn Abbot, 1981) — category-based trivia with a progression arc. The mechanic: answer questions across categories, earn recognition for breadth of knowledge.
- **Quiz type-ins** — a universal magazine listing genre. Every home-computer magazine published quiz programs as DATA/READ demonstrations with score tracking.

---

## 3. Core Experience

Four categories, eight questions. Each question shows a prompt and four multiple-choice answers. Get it right and your score climbs. Get it wrong and you learn the answer. At the end, a rating — from "Beginner" to "Quiz Master" — frames how you did. The pleasure is in the climbing score and the final title.

---

## 4. Visual Direction

- **Question card.** A coloured header bar (category colour), the question text, and four numbered options below. Each category gets its own INK/PAPER combination — the learner sees colour-as-category for the first time.
- **Score display.** Running total visible at all times, top-right via PRINT AT.
- **Results screen.** Final score, per-category breakdown, and the earned rating in a distinct colour.
- **Magazine-screenshot test:** a question card mid-quiz — coloured header, four options, score in the corner. Instantly recognisable as a quiz game.

---

## 5. Audio Direction

- **Correct answer.** Ascending tone.
- **Wrong answer.** Descending tone, followed by the correct answer displayed.
- **End-of-quiz fanfare.** A brief ascending scale before the rating appears.

---

## 6. Level Design Direction

- **Content source:** DATA statements hold questions, options, and correct answers. Each question is a block of DATA: question text, four options, correct answer number.
- **Categories.** Four categories, two questions each (8 total for a manageable first quiz). Category names in DATA alongside questions.
- **Difficulty curve.** First question per category is easier; second is harder. The DATA order *is* the difficulty curve.
- **Scale:** 8 questions total. The learner adds their own categories and questions.
- **Onboarding:** First question should be obviously answerable — the player learns the interface on a guaranteed win.

---

## 7. Anti-goals

- No timer — the player thinks at their own pace. Timed quizzes are a V3 concept.
- No lifelines or hints — get it right or learn the answer.
- No persistent high scores — the rating is the reward, not a leaderboard.
- No random question order — categories play in sequence. Randomisation adds complexity without pedagogical value here.
- Maximum ~50 lines of BASIC + DATA.

---

## 8. Topic Progression

1. **One question.** DATA holding a question and answer. READ them. PRINT the question. INPUT the player's answer. Check if correct. **New:** multi-field DATA blocks (question + answer as a unit). **Program:** ~8 lines.

2. **Multiple choice.** Four options per question, stored in DATA. Display them numbered 1–4. The player types a number, not the answer text. **New:** reading multiple DATA fields per question, numeric input for option selection. **Program:** ~14 lines.

3. **Keeping score.** A counter increments on correct answers. Display running total. After all questions, show the final score. **New:** score accumulation across multiple rounds (reinforces Lucky Number's counter pattern). **Program:** ~18 lines.

4. **String arrays.** `DIM q$(8)` — store questions in an indexed array. Read all DATA into the array at the start: `FOR i = 1 TO 8: READ q$(i): NEXT i`. Access by index: `PRINT q$(round)`. **New:** DIM, string arrays, indexed access. **Program:** ~24 lines.

5. **Categories.** Four colour-coded categories. Each category gets its own PAPER colour for the question card header. `RESTORE` between categories to rewind to the right DATA block. **New:** RESTORE for navigating DATA, colour-as-category. **Program:** ~30 lines + DATA.

6. **The question card.** A structured display: coloured header bar (PAPER + PRINT AT), question text below, four numbered options, score in the corner. CLS between questions. The screen is a *card*, not a scrolling log. **New:** PRINT AT layout for a structured multi-element display. **Program:** ~36 lines + DATA.

7. **Ratings.** Final score mapped to a title: 8/8 is "Quiz Master!", 6–7 is "Expert", 4–5 is "Not bad", below 4 is "Keep trying." The title prints in a distinct colour. The rating *names* the player's achievement — it reframes a number as an identity. **New:** rating as identity (the embedded concept). **Program:** ~40 lines + DATA.

8. **Per-category scores.** Track correct answers per category (four separate counters). Display a category breakdown at the end alongside the overall rating. The player sees where they were strong and where they were weak. **New:** multiple counters tracked in parallel. **Program:** ~44 lines + DATA.

9. **Replay and expansion.** "Play again?" prompt. The learner adds their own questions to the DATA — new categories, more questions per category. The quiz grows by adding DATA, not by changing code. **New:** none (reinforces data-driven design from Cipher). **Program:** ~48 lines + DATA.

10. **Make it yours.** Title screen. Add a "category select" option — the player chooses which category to play. Add per-round feedback ("3 out of 4 in Science — good!"). The quiz is now a complete, expandable program. **New:** simple menu (INPUT + chained IF for category choice). **Program:** ~50 lines + DATA.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] Every topic produces a working, runnable result
- [ ] DIM arrays correctly sized and indexed
- [ ] RESTORE navigates to the right DATA block per category
- [ ] All 8 questions display correctly with 4 options each
- [ ] Score tracking is correct across all rounds
- [ ] Ratings map correctly to score ranges
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **basic** — DIM string arrays: indexed storage for structured data. The foundation of every game with named objects, inventories, or level data.
- **basic** — RESTORE for DATA navigation: rewinding and re-reading DATA blocks by category. The pre-file technique for segmented content.
- **basic** — multi-field DATA blocks: grouping related fields (question, options, answer) as a logical unit. The simplest form of a "record."

---

## 11. Vault Tie-ins

- **Trivial Pursuit** (Horn Abbot, 1981) — category-based trivia as cultural ancestor.
- **Quiz type-ins** — the magazine tradition of DATA-driven quiz programs.
- **Progression as design concept** — the feeling of climbing toward a named achievement.
