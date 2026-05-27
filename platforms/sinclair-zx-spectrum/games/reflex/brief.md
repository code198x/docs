# Reflex — Brief

**Title (working):** Reflex
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 4 of 8
**Headline concept:** Tension — time pressure creates engagement
**Embedded concept:** Telegraphing — showing the player what's about to happen so they can prepare
**Topics:** 6 topics, ~7–9 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that INKEY$ gives the program continuous awareness of the keyboard — not just INPUT's "stop and wait" — and that PLOT/DRAW put pixels on screen, so the learner arrives at Dice Roller with real-time input and pixel graphics as working tools.

---

## 2. Classic Ancestors

- **Reaction testers** — a staple of home-computer magazines from 1982 onwards. The mechanic: wait for a signal, press a key as fast as you can, measure the time. Simple enough for a type-in listing, satisfying enough to play ten times in a row.
- **Stopwatch programs** — the Spectrum's internal clock (accessed via timing loops or frame counting) made reaction measurement a natural first program for magazines teaching real-time input.

---

## 3. Core Experience

Watch the screen. Wait. The signal appears — press a key. Your reaction time appears on screen. Try again. Try to beat your own time. The pleasure is in the tension of waiting and the satisfaction of seeing the number drop.

---

## 4. Visual Direction

- Dark theme (BORDER 0, PAPER 0, INK 7). DRAW lightning bolt on title screen (~5 DRAW commands).
- DRAW rectangle frame around the telegraph bar area — the bar fills inside a drawn meter. Reinforces DRAW (taught in this game) in a practical context.
- Red PAPER flash on signal unchanged (core mechanic).
- BRIGHT 1 on rating text. Colour-coded feedback (green/cyan/yellow/red) unchanged.

---

## 5. Audio Direction

- **Tick sound during telegraph.** A short BEEP each time the bar advances — building rhythm, building anticipation.
- **Signal BEEP.** A loud, distinct tone when the player should react. Unmistakable.
- **Result BEEP.** High tone for fast, low tone for slow — audio feedback matching the number.

---

## 6. Anti-goals

- No moving targets — the player reacts to a static signal, not a moving object. Moving targets arrive in V3.
- No multiple rounds in a single run — the program measures one reaction. The learner runs it again manually. Automatic retry loops arrive with FOR/NEXT in Dice Roller.
- No stored high scores — no arrays, no persistent state. Just this attempt, this number.
- Maximum ~25 lines of BASIC.

---

## 7. Topic Progression

1. **Wait and respond.** The simplest reaction test: `PRINT "Wait..."`, `PAUSE` with a random delay (`PAUSE INT(RND*100)+50`), `PRINT "NOW!"`. Then a loop that waits for INKEY$: `IF INKEY$ = "" THEN GO TO 40`. When the player presses any key, `PRINT "You pressed!"`. No timing yet — just the shape of wait-then-react. **New:** INKEY$ (non-blocking keyboard check), random PAUSE for unpredictable delay. **Program:** ~8 lines. **Polish beat:** how long should the wait be? Too short is unfair; too long is boring.

2. **Measuring time.** Add a counter: `LET t = 0` before the wait loop, `LET t = t + 1` inside it. When the player presses, `PRINT "Your time: "; t`. The number is arbitrary (loop iterations, not milliseconds) but smaller is better. The learner now has a number they want to beat. **New:** counter as timer (the `t = t + 1` accumulator pattern from Lucky Number, repurposed). **Program:** ~10 lines. **Polish beat:** run it five times. Watch the number drop as you learn the rhythm.

3. **Drawing the telegraph.** Before the signal, draw a horizontal bar that fills gradually: `FOR x = 0 TO 200: PLOT x, 88: NEXT x`. The bar advances — the player watches it creep — then the signal fires. The bar telegraphs what's coming without saying when. This is the learner's first use of PLOT — putting a pixel at a coordinate. **New:** PLOT (placing a pixel), using FOR/NEXT with PLOT (preview — FOR/NEXT taught formally in Dice Roller). **Program:** ~14 lines. **Polish beat:** how fast should the bar fill? The bar speed is the tension dial.

4. **Rating the result.** Add chained IF/THEN on the time value: under 5 prints "Lightning!"; under 15 prints "Quick"; under 30 prints "OK"; otherwise "Slow". Change the INK colour to match — green for fast, yellow for OK, red for slow. The feedback is now multi-channel: number + word + colour. **New:** colour-coded result feedback (reinforces distance-driven feedback from Lucky Number). **Program:** ~18 lines. **Polish beat:** are the thresholds fair? Play ten times and calibrate.

5. **The signal flash.** Replace the plain "NOW!" text with a full-screen colour change: `PAPER 2: CLS` (red flash). The telegraph bar was subtle; the signal is not. Contrast is the design lesson — the build-up is quiet so the moment can be loud. Add `BORDER 2` alongside for the full effect. **New:** PAPER + CLS as a visual event (full-screen colour change). **Program:** ~22 lines. **Polish beat:** try different signal colours. Red screams "now"; green feels wrong. Colour carries meaning.

6. **Make it yours.** Add a title screen with the game's name and instructions. Add DRAW to extend the telegraph bar into a proper line (`DRAW 200, 0` from a starting PLOT). Add a "Press any key to start" prompt before the wait begins. The learner has built a complete reaction tester with pixel graphics, real-time input, and multi-channel feedback. **New:** DRAW (line between two points), title screen pattern. **Program:** ~25 lines. **Polish beat:** show someone. Challenge them. The program is a toy you can compete with.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] INKEY$ loop is responsive — no perceptible lag between keypress and response
- [ ] Telegraph bar creates genuine tension (test: does the player watch it?)
- [ ] Signal flash is unmissable — colour change is bold enough to trigger an instant reaction
- [ ] Reaction time number is consistent across runs (same speed of reaction = similar number)
- [ ] PLOT and DRAW produce visible pixels (not off-screen or invisible against background)
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **input** — INKEY$ polling loop: `IF INKEY$ = "" THEN GO TO n`. Non-blocking keyboard check — the foundation of every real-time game from here forward. Cross-platform concept (polling vs blocking input).
- **rendering** — PLOT/DRAW basics: placing pixels at coordinates, drawing lines. The learner's first pixel-level graphics.
- **basic** — loop-counter-as-timer: `LET t = t + 1` inside an INKEY$ wait loop. Approximate timing without hardware timers. Used in every game that measures reaction or elapsed time.

---

## 10. Vault Tie-ins

- **Reaction testers** — magazine type-in tradition; a universal first program for teaching real-time input.
- ZX Spectrum INKEY$ — the non-blocking keyboard read that underpins every real-time Spectrum program.
- ZX Spectrum PLOT/DRAW — pixel-level graphics on the 256×176 display.
