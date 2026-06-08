# Safe Cracker — Brief

**Title (working):** Safe Cracker
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 6 of 8
**Headline concept:** Deduction — narrow hidden information
**Embedded concept:** Stakes — a limited number of tries
**Topics:** 6 topics, ~6–8 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach the loop-with-a-goal — a loop that runs until the player either succeeds or runs out of tries — so the learner leaves holding the win/lose structure that every later game is built on, and arrives at Rover and Dropzone knowing how a game ends, not just how it runs.

---

## 2. Classic Ancestors

- **Hi-Lo / "guess my number"** — the type-in that taught a generation what `RND` and `IF` were for. The computer hides a number; you guess; it tells you higher or lower. The whole game in a dozen lines, and a fixture of every beginner's BASIC book.
- **The safe-cracking type-in with a dial** — the dressed-up cousin, where the bare number becomes a combination and the higher/lower hint becomes the click of a tumbler. Same machinery, more theatre.

---

## 3. Core Experience

A locked safe, a hidden code. You spin in a guess; the safe answers higher or lower, and the colour warms as you close in. Your guess count is the clock — every try spent is a try gone. Crack it before the dial runs out, and the safe swings open; run out first, and it stays shut. Pure deduction, no rush — the pressure is the dwindling number of tries, not the ticking second.

---

## 4. Visual Direction

- **A safe-cracking frame.** A drawn safe door fills the centre — a border of block characters POKEd into screen RAM with a combination dial at its face. The guess you type and the safe's answer ("HIGHER" / "LOWER") sit below it, redrawn each go so the screen is the dial, not a scroll of text.
- **Colour carries the feedback.** The hint isn't only words — the screen says it in colour. Warmer as you close in (the background via `POKE 53281` shifts toward red/orange as the gap narrows), or a straight red-for-too-high / green-for-too-low split written into colour RAM. Either way the learner reads the safe's mood before they read the word.
- **The tries remaining are on screen.** A row of dial marks, or a plain counter, POKEd into a fixed cell and decremented each guess — the player watches their stake shrink. The background (`POKE 53281`) goes green on the crack, red on lockout — the whole screen carrying the ending, since white-on-border doesn't read reliably in capture and the background is the bolder signal anyway.
- **Magazine-screenshot test:** a Commodore-magazine screenshot — the safe drawn in PETSCII blocks, "HIGHER" under the dial in a warm colour, "GUESSES LEFT: 3" along the bottom. A reader flicking past would know the game at a glance.

---

## 5. Audio Direction

- **A tumbler click per guess.** The SID at 54272 (a single voice) ticks a short click or tone each time the player commits a guess — the dial turning, one notch.
- **A triumphant tone on the crack.** When the code is found, a rising tone or short flourish on the same voice — the safe swinging open.
- **A buzzer on lockout.** Out of guesses: a low, harsh buzz — the safe staying shut. The opposite shape to the crack, so the ear knows which ending it got.
- **Otherwise silent.** Sound marks the three moments that matter — guess, crack, lockout — and nothing else. This is C64 SID, not Spectrum BEEP: the learner writes the frequency and gate registers at 54272 by hand, the same memory-mapped surface the primer introduced.

---

## 6. Anti-goals

- No multi-digit Mastermind-style pegs — no per-position "right digit, wrong place" feedback. That's a later, bigger game. Here the secret is one number and the only hint is higher/lower.
- No real-time pressure — no jiffy clock, no countdown timer. The stake is the guess limit, not the second hand. Deduction, not reflex.
- No difficulty menu — the range (1–100) and the guess limit are fixed. The challenge lives in the maths, not in options.
- No high-score table, no stored bests across runs. One safe, one crack, play again.
- Keep it small — well under the size the win/lose structure needs, not padded toward a bigger game.

---

## 7. Topic Progression

1. **Pick a secret.** Generate the hidden code: `S = INT(RND(1)*100)+1`. Print it (just this once) to prove it exists and lands in range. No guessing yet — the learner makes the machine choose, and confirms `RND` gives a whole number from 1 to 100. **New:** `RND` shaped into an integer range. **Program:** ~4 lines. **Polish beat:** is the range 1–100, or 1–1000? The range decides how many guesses a fair crack needs — pick it on purpose, not by accident.

2. **Take a guess.** Hide the secret. `INPUT "YOUR GUESS"; G`. Compare: `IF G = S THEN PRINT "CRACKED IT!"`. One guess, one verdict — right or not. The first real interaction: the player puts a number against the safe's. **New:** `INPUT` of a number, the equality test. **Program:** ~8 lines. **Polish beat:** what if the player types 0, or 200, or letters? A guess outside 1–100 can never be right — decide whether to scold it or just let it miss.

3. **Higher or lower.** When the guess is wrong, say which way: `IF G < S THEN PRINT "HIGHER"` and `IF G > S THEN PRINT "LOWER"`. Now a wrong guess teaches something — the player learns the secret is above or below, and the search has a direction. **New:** the two-way `IF` comparison that turns a miss into information. **Program:** ~12 lines. **Polish beat:** phrase the hint from the safe's point of view — "the code is HIGHER than that" — so the player knows which number to move, not just that they were wrong.

4. **Loop until right.** Wrap the guess in a loop that runs until the safe is cracked: `GOTO` back to the input, and only the correct guess breaks out. This is the loop-with-a-goal — not a `FOR` that counts to a fixed number, but a loop that runs until something specific happens. The player can now narrow in, guess after guess, until the safe opens. **New:** loop-until-condition (the structural pattern), the exit branch. **Program:** ~16 lines. **Polish beat:** the moment the safe opens after a run of near-misses — make the "CRACKED IT!" land, give it the screen to itself.

5. **Colour the feedback.** Move the hint into colour. Write the background with `POKE 53281` — red when the guess is too high, green when too low (or warmer as the gap shrinks), so the safe answers in colour before it answers in words. POKE the guess count and the safe frame into screen + colour RAM. **New:** colour RAM / `POKE 53281` as feedback, the safe drawn by POKE. **Program:** ~24 lines. **Polish beat:** does warmer-as-you-close-in feel better than a flat red/green? Try both on the emulator and look — the one that makes the player *feel* the gap closing wins.

6. **Add a guess limit and a lose state.** Give the safe a fixed number of tries: count each guess, and when the count hits the limit before the crack, the safe locks — a lose ending, buzzer and all. Now there are two ways the loop ends, win and lose, and the guess count is the clock. The complete game: a secret, a narrowing search, and a stake that can run out. **New:** a counter against a limit, the lose branch, win *and* lose endings. **Program:** ~30 lines. **Polish beat:** set the limit so a player using the hints well just makes it, and a player guessing blind just fails. Seven tries for 1–100 is the deduction made fair — tune it until losing feels like your own fault.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] Loop-with-a-goal is distinct from `FOR`/`NEXT` — the learner understands "loop until won or out of tries" vs "loop N times"
- [ ] Both endings work — the safe cracks on a correct guess and locks when the limit is reached
- [ ] The guess counter decrements correctly and is visible during play
- [ ] Colour feedback matches the hint — too-high and too-low are never the same colour
- [ ] Out-of-range guesses are handled, not silently ignored
- [ ] Gradual progression — a reader can follow from topic 1 to the final topic without gaps
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **basic** — loop-with-a-goal: a loop that runs until the player wins or runs out of tries, with two exit branches instead of one. The structural ancestor of every game loop that ends in a win or a lose state — Rover's finish, Dropzone's landing. Cross-platform.
- **basic** — narrowing search via higher/lower: turn a wrong answer into a direction so each guess halves the space. The core of binary search, met here as a game before it's met as an algorithm.
- **basic** — a counter against a limit: increment each turn, compare to a fixed cap, branch when it's reached. The simplest stake — one variable that turns an endless loop into a game you can lose.
- **basic** — colour as feedback: `POKE 53281` / colour RAM carrying state the player reads before the words. The C64's memory-mapped colour surface used to *mean* something, not decorate.

---

## 10. Vault Tie-ins

- **Hi-Lo / "guess my number"** — the type-in tradition; how `RND` and `IF` first reached beginners through a guessing game.
- **Binary search** — the deduction the game teaches in disguise; higher/lower as the everyday face of a fundamental algorithm.
- **MOS 6581 SID** — the sound chip at 54272; the single-voice click/crack/buzzer as a first taste of writing its registers by hand.
- **VIC-II colour RAM and `$D020`/`$D021`** — the background and border registers (53280/53281) the colour feedback writes to; the same surface the assembly track revisits at machine speed.
