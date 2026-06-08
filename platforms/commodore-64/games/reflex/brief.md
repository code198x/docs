# Reflex — Brief

**Title (working):** Reflex
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 3 of 8
**Headline concept:** Tension — time pressure creates engagement
**Embedded concept:** Telegraphing — showing the player what's about to happen so they can prepare
**Topics:** 6 topics, ~7–9 hours
**Constraint position:** period-faithful

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that the C64 measures real time itself — the jiffy clock `TI` counts in 1/60-second ticks, so the program can time an event instead of estimating it with a loop — and that `GET` reads the keyboard without stopping the program, unlike `INPUT`. The learner arrives at Tally able to *measure* and to *react*, with `POKE 53281` already proven as instant visual feedback.

---

## 2. Classic Ancestors

- **Reaction testers** — a staple of Commodore magazines from 1982 onwards (*Compute!'s Gazette*, *Your Commodore*). The mechanic: wait for a signal, press a key as fast as you can, measure the time. Short enough for a type-in listing, satisfying enough to play ten times in a row.
- **Stopwatch programs** — the C64's hardware jiffy clock made reaction measurement a natural first real-time program. Where other machines counted loop iterations, the C64 had a clock in ROM you could read with one variable.

---

## 3. Core Experience

Watch the screen. Wait — the wait stretches, deliberately. The screen flashes white; slam a key. Your reaction time appears in jiffies, then in seconds. Try again. Try to beat your own number. The pleasure is in the tension of waiting and the satisfaction of seeing the number drop.

---

## 4. Visual Direction

- Dark screen — black background (`POKE 53281,0`), light text. The quiet, still screen makes the flash land harder.
- The signal is a **screen flash**: `POKE 53281,1` slams the whole background white, then back to black. The entire screen lighting up is the boldest signal the C64 has — bigger than a border flash, and impossible to miss. (The border register `53280` is the natural sibling, but white reads weakly there; the background is the surface that lands.)
- Colour-coded result, set via `POKE 646` (text colour) before the `PRINT`: **green** for lightning-fast, **cyan** for quick, **yellow** for OK, **red** for slow. The number, the word, and the colour all say the same thing at once.
- Magazine-screenshot test: a Commodore-magazine listing page showing the result line — `YOUR TIME: 14 JIFFIES (0.23 SEC)` in green on black, the screen still settling — the kind of frame that sold a type-in.

---

## 5. Audio Direction

C64 SID at 54272, a single voice — set up once (waveform + envelope), then triggered by gating. Not Spectrum `BEEP`.

- **Tick during the wait.** A short, quiet blip each beat of the wait — building rhythm, building anticipation without telling the player *when*.
- **Signal tone.** A sharp, high tone the instant the screen flashes — loud and distinct, the cue to react. Unmistakable.
- **Result tone.** A high note for a fast time, a low note for a slow one — the SID echoing the number.
- Deliberately silent the rest of the time: the still screen and silence are what make the signal loud.

---

## 6. Anti-goals

- No moving target — the player reacts to the screen flash, not a moving object. Moving targets arrive later.
- No multi-round loop — the program measures one reaction. The learner runs it again manually. Automatic retry loops belong to later games.
- No stored bests — no arrays, no persistent state. Just this attempt, this number.
- One reaction, one number. Keep it small.

---

## 7. Topic Progression

1. **Flash the screen.** The signal on its own: clear the screen, `PRINT "WATCH THE SCREEN..."`, then `POKE 53281,1` to slam the whole background white and `POKE 53281,0` to drop it back. No timing, no input yet — just the shape of the event the rest of the game is built around. **New:** `POKE 53281` (the background-colour register) as an instant visual event. **Program:** ~6 lines. **Polish beat:** how long should the flash hold? A frame or two reads as a flash; too long and it stops feeling sharp.

2. **Wait a random spell.** Before the flash, make the program pause for an unpredictable stretch: `POKE 53281,0`, then a delay loop whose length comes from `RND` — `W = INT(RND(1)*120)+60` — so no two runs wait the same. The unpredictability is the point: the player cannot anticipate the signal. **New:** `RND` driving the length of the wait. **Program:** ~9 lines. **Polish beat:** what's the right range? Too short is unfair; too long is boring. Find the spell that makes the player lean in.

3. **Time the gap with `TI`.** Read the jiffy clock. Set `TI$ = "000000"` (or note `TI`) the instant the screen flashes, and read `TI` again the instant the reaction is registered — the difference is the reaction time in 1/60ths of a second. Print it: `PRINT "YOUR TIME:"; T; "JIFFIES"`. The number is real time now, not loop counts. **New:** `TI` / `TI$`, the C64's built-in 1/60-second jiffy clock. **Program:** ~12 lines. **Polish beat:** divide by 60 to show seconds too — `T/60` — and watch the two numbers tell the same story.

4. **Read the key with `GET`.** Replace any wait-for-`INPUT` with a `GET` loop: `GET A$: IF A$ = "" THEN` keep looping. `GET` reads the keyboard and carries on without stopping the program — so the clock keeps ticking while the program watches for the press. This is the difference between a reaction tester and a program that just asks a question. **New:** `GET` (non-blocking key read) versus `INPUT` (stop and wait). **Program:** ~15 lines. **Polish beat:** press the moment the screen flashes — the `GET` loop catches it instantly, with no RETURN needed.

5. **Show the result.** Turn the raw number into a readout: clear a line, print the jiffies and the seconds together, and hold it on screen so the player can read it before running again. The result is the reward — give it room. **New:** formatting the result line (`PRINT` with a number and a label, jiffies and seconds side by side). **Program:** ~18 lines. **Polish beat:** does the number sit where the eye lands? Centre it; let it be the thing on the screen.

6. **Rate it — and catch a cheat.** Add chained `IF` on the time: under 12 jiffies is "LIGHTNING!" in green, under 24 "QUICK" in cyan, under 45 "OK" in yellow, otherwise "SLOW" in red. And guard the start: if a key is already down *before* the flash, print "TOO SOON!" and don't score it — the player can't jump the gun. The learner finishes with a complete reaction tester: real-time timing, instant input, multi-channel feedback, and an honest result. **New:** colour-coded rating from the time; catching a too-early press. **Program:** ~22 lines. **Polish beat:** play ten times and calibrate the thresholds — they should feel fair but make "LIGHTNING!" something you have to earn.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] `GET` loop is responsive — no perceptible lag between keypress and the time being read
- [ ] The random wait genuinely varies run to run — the player cannot anticipate the signal
- [ ] Screen flash is unmissable — the `POKE 53281` change is bold enough to trigger an instant reaction
- [ ] Reaction time in jiffies is consistent across runs (same speed of reaction = similar number)
- [ ] The too-early guard fires — a key held before the flash is rejected, not scored
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **input** — `GET` polling loop: `GET A$: IF A$ = "" THEN` loop. Non-blocking keyboard read — the foundation of every real-time C64 game from here forward. Cross-platform concept (polling versus blocking input).
- **basic** — the jiffy clock as a timer: zero `TI$`, read `TI`, take the difference. Real hardware timing in 1/60ths, used by every later game that measures reaction or elapsed time.
- **rendering** — the background register (`53281`) as an instant full-screen signal: one POKE floods the whole screen. Reused wherever the game needs unmissable feedback without drawing anything.

---

## 10. Vault Tie-ins

- **Reaction testers** — the Commodore magazine type-in tradition; a universal first program for teaching real-time input.
- C64 jiffy clock (`TI` / `TI$`) — the 1/60-second software clock the KERNAL maintains, the C64's native way to measure elapsed time.
- VIC-II background register (`$D021` / 53281) — the memory-mapped colour register that makes the whole screen a one-POKE visual event.
