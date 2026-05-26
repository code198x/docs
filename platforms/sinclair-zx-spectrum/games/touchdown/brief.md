# Touchdown — Brief

**Title (working):** Touchdown
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 8 of 8
**Headline concept:** Descent — the program runs whether you act or not
**Embedded concept:** Ambient feedback — the environment communicates game state without explicit UI
**Topics:** 8 topics, ~10–14 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that a game loop can run continuously — updating state every iteration whether the player acts or not — so the learner crosses into Volume 2 understanding the difference between "wait for input, then act" (Lucky Number's model) and "the world runs, input steers it" (every real-time game's model). Touchdown is the bridge from turn-based to real-time.

---

## 2. Classic Ancestors

- **Lunar Lander** (various, 1969 onwards) — one of the oldest computer games. Originally a text simulation on DEC PDP-8 (Jim Storer, 1969), then graphical versions on every platform. The mechanic: gravity pulls you down, thrust pushes you up, fuel is finite. Land gently or crash.
- **Jupiter Lander** (HAL Labs, 1982) — the Commodore 64 graphical version that defined how the genre looked on 8-bit home computers. Spectrum type-in variants appeared in *Your Computer*, *Sinclair Programs*, and *Computer Spacegames* (Usborne, 1982).

---

## 3. Core Experience

The lander descends. Gravity pulls. Fuel burns. You fire the thruster — the descent slows, the fuel drops. Too fast at the ground and you crash. Too slow and you run out of fuel. The pleasure is in the last ten metres: watching the speed number, nursing the fuel, timing the final burst. Every landing is a negotiation with physics.

---

## 4. Visual Direction

- **Text-mode instrument panel.** Altitude, speed, fuel — three numbers at fixed screen positions (PRINT AT), updating every loop iteration. The numbers are the game. The learner's first real-time dashboard.
- **Simple lander display.** A character (an asterisk, a `V`, or a simple text symbol) at a PRINT AT position that moves down the screen as altitude decreases. No pixel graphics — the position on screen *is* the altitude.
- **Ground line.** A row of dashes or equals signs at the bottom of the screen. The lander approaches it. Contact at low speed = "TOUCHDOWN!" in green. Contact at high speed = "CRASH!" in red.
- **Fuel gauge.** A horizontal bar (PRINT-character) that shrinks as fuel burns. Ambient feedback — the learner sees fuel draining peripherally while watching altitude.
- **Magazine-screenshot test:** the lander symbol halfway down the screen, speed reading "12", fuel bar half-empty — the player in the middle of the decision. Will they burn fuel now or coast?

---

## 5. Audio Direction

- **Thrust sound.** A short BEEP on each frame when the player holds the thrust key. The sound of burning fuel.
- **Crash.** A low, harsh tone — unmistakable failure.
- **Touchdown.** An ascending fanfare — brief, celebratory.
- **Low-fuel warning.** A distinct repeating tone when fuel drops below 20%. Ambient feedback through sound — the player hears trouble before they see it.

---

## 6. Anti-goals

- No horizontal movement — the lander goes straight down. Horizontal movement and wind arrive in V3 games.
- No terrain — flat ground only. Terrain generation is V4 territory.
- No pixel-level graphics — the lander is a text character. Smooth movement is an assembly-track concern.
- No physics beyond gravity and thrust — no rotation, no angular momentum, no atmospheric drag.
- No multiple lives — one attempt per run. The learner restarts the program.
- Maximum ~35 lines of BASIC.

---

## 7. Topic Progression

1. **Falling.** A number counts down: `LET alt = 100`, loop with `LET alt = alt - 1`, `PRINT AT 10, 10; alt; " "`. The number decreases — the lander is falling. When `alt = 0`, `PRINT "LANDED"`. No input, no control — just gravity. The program runs without the player doing anything. That's the headline: **Descent**. **New:** the concept of a continuously-running loop that updates state (the game loop). **Program:** ~6 lines. **Polish beat:** how fast should it fall? PAUSE inside the loop controls the pace. Find the speed that feels like falling, not counting.

2. **Speed.** Add velocity: `LET spd = 0`, `LET spd = spd + 1` each iteration (gravity accelerates), `LET alt = alt - spd`. The lander falls faster and faster. Display speed alongside altitude. At touchdown, check speed: `IF spd > 5 THEN PRINT "CRASH!"` else `PRINT "TOUCHDOWN!"`. Now the outcome depends on something. **New:** acceleration (velocity changes over time), outcome based on state at a specific moment. **Program:** ~10 lines. **Polish beat:** what speed threshold feels fair? Too low and landing is impossible; too high and there's no challenge.

3. **Thrust.** Add `IF INKEY$ = " " THEN LET spd = spd - 2` inside the loop. Press space — speed drops. Release — gravity takes over. The player now controls the descent. The game exists: gravity vs thrust, falling vs braking. **New:** INKEY$ inside a game loop (combining the Reflex polling pattern with continuous-update state). **Program:** ~12 lines. **Polish beat:** how much thrust per press? `spd - 1` is subtle; `spd - 3` is dramatic. The number shapes the game feel.

4. **Fuel.** Add `LET fuel = 50`. Each thrust burns one unit: `IF INKEY$ = " " AND fuel > 0 THEN LET spd = spd - 2: LET fuel = fuel - 1`. Display fuel alongside altitude and speed. When fuel hits zero, thrust stops working — the player coasts on whatever speed they have. Finite resources create the core tension: brake too early and you run out; brake too late and you crash. **New:** resource management (fuel as a depletable resource), AND for compound conditions in INKEY$ checks. **Program:** ~16 lines. **Polish beat:** how much fuel is fair? 50 units means every burn matters. 200 means the player can hover. Find the number where fuel is scarce but sufficient.

5. **The dashboard.** Replace scrolling PRINT output with a fixed dashboard: PRINT AT positions for altitude, speed, and fuel, updated every loop. Add labels: "ALT:", "SPD:", "FUEL:". Clear each value before reprinting (trailing spaces). The screen is now an instrument panel, not a scrolling log. **New:** PRINT AT dashboard (reinforces Dice Roller), clearing previous values with spaces. **Program:** ~20 lines. **Polish beat:** where should each instrument sit? The layout is a design decision — altitude top, speed middle, fuel bottom? Or all in a row?

6. **The lander on screen.** Add a character that moves down the screen: `PRINT AT 20 - alt/5, 15; "V"`. Clear the previous position first. The lander's position *is* the altitude — no separate display needed. Add the ground line: `PRINT AT 20, 0;` followed by dashes. The player now sees the lander approaching the ground. **New:** PRINT AT with computed position (a variable controlling screen placement), clearing previous character position. **Program:** ~25 lines. **Polish beat:** the moment the "V" touches the dashes — does it feel like landing? The visual and the number should agree.

7. **Ambient feedback.** Add BORDER colour that shifts with altitude: blue at high altitude (safe), cyan in the middle, yellow getting close, red near the ground. Add the low-fuel warning: `IF fuel < 10 THEN BEEP 0.02, 20` inside the loop — a rapid tick when fuel is critical. Add the thrust sound: a brief BEEP when space is pressed. The environment now communicates game state through colour and sound without the player reading numbers. That's **ambient feedback**. **New:** BORDER driven by game state (reinforces Lucky Number), conditional sound inside the game loop. **Program:** ~30 lines. **Polish beat:** play with the dashboard hidden (cover it with your hand). Can you land using only the ambient feedback? If yes, the feedback works.

8. **Make it yours.** Add a title screen: "*** TOUCHDOWN ***" with instructions ("SPACE to thrust"). Add a landing rating based on speed at contact: `IF spd <= 2 THEN PRINT "Perfect landing!"`, `IF spd <= 5 THEN PRINT "Bumpy but safe"`, otherwise `"CRASH!"`. Add the fuel bar: a shrinking row of PRINT characters alongside the fuel number. Add a replay prompt. The V1 curriculum ends here — the learner has built a real-time game with physics, resource management, and ambient feedback in ~35 lines of BASIC. **New:** landing rating, fuel bar visualisation, replay loop. **Program:** ~35 lines. **Polish beat:** this is the V1 capstone. Does it feel like a game someone would play for five minutes, not just run once? If yes, Volume 1 is done.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] The game loop runs continuously — state updates whether the player presses a key or not
- [ ] Gravity acceleration feels physical — the lander speeds up over time
- [ ] Thrust feels responsive — pressing space immediately affects speed
- [ ] Fuel depletion creates genuine tension — the player must budget burns
- [ ] Soft landing is achievable but requires skill — not trivially easy, not impossible
- [ ] Dashboard updates without screen flicker (trailing-space clearing works)
- [ ] Ambient feedback (BORDER colour + sound) carries enough information to land without reading numbers
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **framework** — the continuous game loop: a `GO TO` loop that updates state every iteration whether the player acts or not. The structural foundation of every real-time game. Cross-platform.
- **physics** — gravity + thrust model: `spd = spd + gravity`, `IF thrust THEN spd = spd - power`. The simplest physics simulation — two forces, one variable. The pattern behind every platformer's jump, every vehicle's acceleration.
- **framework** — resource depletion: `fuel = fuel - 1` gated by `fuel > 0`. Finite resources as a tension mechanic. Cross-platform.
- **rendering** — PRINT AT with computed position: `PRINT AT row_from_variable, col; character`. The pattern behind every character-cell game's movement — the variable *is* the position.

---

## 10. Vault Tie-ins

- **Lunar Lander** (Jim Storer, 1969; DEC PDP-8) — one of the oldest computer games. The original text simulation.
- **Jupiter Lander** (HAL Labs, 1982) — the C64 graphical version that defined the genre on 8-bit.
- *Computer Spacegames* (Usborne, 1982) — includes a Lunar Lander variant as one of its type-in programs.
- **The game loop** — the structural concept that distinguishes real-time programs from turn-based. Every game from V2 onwards inherits this.
