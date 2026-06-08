# Dropzone — Brief

**Title (working):** Dropzone
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 8 of 8
**Headline concept:** Risk & reward — push your luck against gravity
**Embedded concept:** Physics — velocity accumulates over time
**Topics:** ~7 topics
**Constraint position:** period-faithful

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

The volume capstone: it fuses everything the earlier seven games taught into one complete game with a goal — the continuous loop, live input, the screen-and-colour surface, and the SID, all working at once — so the learner leaves Volume 1 having built a real-time physics game from scratch, with gravity and thrust held in plain variables and an explicit win-or-crash ending. Skyline gave them the screen, Reflex the clock, Bleeper the SID voice, and Rover the live joystick loop; Dropzone is where those surfaces stop being separate lessons and become a game.

---

## 2. Classic Ancestors

- **Lunar Lander** (various, 1969 onwards) — one of the oldest computer games. Jim Storer's original was a text simulation on the DEC PDP-8; graphical versions followed on every platform. The mechanic never changes: gravity pulls you down, thrust pushes you up, fuel is finite. Land softly or crash.
- **Jupiter Lander** (HAL Labs, 1982) — the Commodore 64 cartridge that defined how the genre looked and felt on the machine the learner is using. "Land the ship" type-ins ran in *Compute!'s Gazette* and the Usborne *Computer Spacegames* (1982) alongside it.

---

## 3. Core Experience

A lander drifts down under gravity. Thrust to slow it, manage the fall, and set it down softly on the pad — or come in too fast and crash. The pleasure is in the last few rows: watching the speed reading, nursing the fuel, timing the final burst. One clean landing is the whole reward.

---

## 4. Visual Direction

- **The lander on screen RAM.** A character POKEd into screen RAM at 1024 with its colour at 55296, addressed by the `1024 + R*40 + C` formula from Skyline. It moves by erase-move-draw: blank the old cell, work out the new row from the altitude, POKE it in.
- **The pad and terrain in colour.** A ground line across the foot of the screen, with the landing pad a short run of cells in a distinct colour RAM value — the one safe place to come down, made obvious by colour, not by a label.
- **A fuel and speed readout via `PRINT`.** Altitude, descent speed, and fuel printed as a fixed readout, rewritten each loop (trailing spaces clear the old digits) so it reads like an instrument panel, not a scrolling log.
- **Colour carries the warning.** As the lander nears the pad, the speed reading or the border (53280) shifts toward danger — the player feels "too fast" before they parse the number.
- **Magazine-screenshot test:** a Commodore-magazine screenshot of the lander a few cells above the pad, the coloured pad and ground line below it, the `PRINT` readout showing altitude, speed, and fuel — a frame a reader would recognise as "the moment before the landing".

---

## 5. Audio Direction

C64 SID at 54272, single voice — reached by POKE, the same way every other surface is. This is the SID, not Spectrum BEEP.

- **Thrust rumble.** A low, continuous tone held while the player is thrusting — the sound of burning fuel. It stops the instant thrust stops.
- **Soft landing.** A gentle, brief tone on a clean touchdown — the reward sound.
- **Crash.** A harsh noise on a hard landing — noise-waveform, unmistakable failure.
- **Deliberately silent** otherwise: the quiet drift down is the tension, broken only when the player acts or the lander meets the ground.

---

## 6. Anti-goals

- No scrolling and no horizontal flight — the lander goes straight down. One axis is the whole game.
- No multiple levels — one pad, one landing, done well.
- No sprites, no custom characters, no raster effects — the lander is a screen-RAM character. Smooth pixel movement is an assembly-track concern.
- No three-voice SID music — one voice for thrust, landing, and crash.
- No multiple lives or high-score table — one attempt per run; the learner restarts the program.
- No physics beyond gravity and thrust — no rotation, no wind, no drag.
- Keep it small — a finished program a learner can read in one sitting, not a sprawl.

---

## 7. Topic Progression

1. **A falling dot.** A character drops down the screen on its own. `LET A = 0` for altitude, a loop that increases it, and the lander POKEd into screen RAM at the row the altitude picks out — erase the old cell, draw the new one. No input yet: the loop runs whether the player acts or not. **New:** a continuously-running update loop that moves a character down screen RAM by erase-move-draw. **Program:** small. **Polish beat:** how fast should it fall? Tune the loop pace until it reads as falling, not stepping.

2. **Gravity accelerates it.** Add velocity as its own variable: `V = V + G` each loop, then move by `V`. The lander starts slow and speeds up — the fall now has weight. **New:** velocity as an accumulating variable that gravity grows every frame (the embedded **Physics** concept). **Program:** a little larger. **Polish beat:** what value of gravity feels like a real drop, not a plummet or a crawl?

3. **Thrust pushes back.** Read a thrust input inside the loop — a key with `GET`, or the joystick fire button with `PEEK(56320)` — and when it's pressed, shrink the velocity: `V = V - T`. Press to slow the fall; release and gravity takes over. The game now exists: two forces, one variable. **New:** live input inside the loop (the Rover pattern) altering the physics variable. **Program:** larger. **Polish beat:** how much thrust per press? A gentle nudge versus a hard shove changes the whole feel.

4. **A landing pad.** Draw the ground line and a coloured pad across the foot of the screen using screen RAM and colour RAM. The lander now descends toward something specific — the one place it's meant to come down. **New:** drawing a fixed pad and terrain in colour RAM as the goal of the loop. **Program:** larger. **Polish beat:** where should the pad sit, and how wide? Wide enough to be fair, narrow enough to matter.

5. **The soft-vs-hard landing test.** When the lander reaches the pad, compare the descent speed at touchdown: slow enough is a soft landing, too fast is a crash. The outcome now depends on how well the player flew the last few rows. **New:** a test of velocity at the moment of contact that decides win versus lose. **Program:** larger. **Polish beat:** what speed threshold is fair — hard enough to demand a final burn, soft enough to be reachable?

6. **Win and crash screens.** Give each outcome its ending: a soft-landing screen with the gentle SID tone, a crash screen with the harsh SID noise. The loop now resolves into a clear result the player can read and feel. **New:** explicit win and lose states, each with its own SID voice (soft tone, crash noise). **Program:** larger. **Polish beat:** does the win feel earned and the crash feel like a thump? The sound should match the screen.

7. **Fuel as the squeeze.** Add a fuel store that each thrust burns, shown in the `PRINT` readout. When fuel runs out, thrust stops working and the player coasts on whatever speed they have. Finite fuel turns the game into a negotiation: brake too early and you run dry, brake too late and you crash. This is the capstone — a complete C64 game with a goal. **New:** fuel as a depletable resource gating thrust; the readout that ties altitude, speed, and fuel together. **Program:** the finished game. **Polish beat:** how much fuel is fair — scarce enough that every burn counts, sufficient that a careful pilot can set down? Find the number where Volume 1 ends on a game worth playing twice.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] The update loop runs continuously — the lander falls whether the player acts or not
- [ ] Gravity feels physical — velocity accumulates and the lander speeds up over time
- [ ] Thrust feels responsive — pressing the key or fire button immediately slows the descent
- [ ] The landing test is fair — a soft landing is achievable with care -- neither a gimme nor impossible
- [ ] Fuel creates genuine tension — the player must budget burns
- [ ] The `PRINT` readout updates without flicker (trailing-space clearing works)
- [ ] SID thrust, soft-landing, and crash sounds are distinct and carry meaning
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **physics** — gravity + thrust model: `V = V + G`, and `IF thrust THEN V = V - T`. The simplest physics simulation — two forces, one variable. The pattern behind every platformer's jump and every vehicle's acceleration.
- **framework** — the continuous game loop: a loop that updates state every iteration whether the player acts or not. The structural foundation of every real-time game.
- **rendering** — erase-move-draw on screen RAM: blank the old cell, compute the new position from a variable, POKE the character (and its colour) in. The pattern behind every character-cell game's movement — the variable *is* the position.
- **framework** — resource depletion: fuel burned per thrust and gated on a remaining count. Finite resources as a tension mechanic.
- **framework** — win/lose resolution: a test of state at a decisive moment branching into distinct endings with matched audio.

---

## 10. Vault Tie-ins

- **Lunar Lander** (Jim Storer, 1969; DEC PDP-8) — one of the oldest computer games; the original text simulation.
- **Jupiter Lander** (HAL Labs, 1982) — the C64 cartridge that defined the genre on the machine.
- *Computer Spacegames* (Usborne, 1982) — includes a Lunar Lander variant among its type-in programs.
- **The SID (6581/8580)** at 54272 — the sound chip the thrust, landing, and crash voices reach by POKE; revisited at machine speed on the assembly track.
- **The game loop** — the structural concept that separates real-time programs from turn-based; every game from Volume 2 onward inherits it.
