# Commodore 64 BASIC V2 Curriculum

**Platform:** Commodore 64
**Language:** BASIC V2 (stock ROM, no extensions — no Simons' BASIC, no cartridges)
**Status:** Volume 1 designed; primer shipped.
**Supersedes:** the pre-methodology `basic-skeleton.md` (a 4-game / 256-unit
"Depth Charge / Neon Nexus / Starswarm / Signal Lost" draft), deleted 2026-06-07.

---

## What this curriculum is

A front-of-curriculum BASIC track that takes an absolute beginner from their
first typed line to a complete, real-time C64 game — then hands them to assembly
with the platform's defining idea already in their hands.

**The thesis: on the C64, every POKE is a hardware register.** BASIC V2 has no
graphics keywords, no sound keywords, no sprite keywords. You reach the screen,
its colour, the SID, and the joystick the same way assembly does — by writing to
memory. That isn't a limitation to apologise for; it *is* the lesson. By the end
of Volume 1 the learner understands memory-mapped I/O not as an abstraction but
as the thing they've been doing since their second game. The bridge to assembly
becomes "same registers, faster access."

There is **no fixed unit count.** Each game is budgeted on the techniques it
must teach and the quality bar (Usborne-listing standard — a real, playable
program a learner is proud to keep), not on a unit quota. Topic counts below are
illustrative ranges, not targets.

The track is independent of the C64 assembly track; neither is a prerequisite
for the other.

---

## The on-ramp: Meet C64 BASIC (primer, shipped)

Before Volume 1, the **Meet C64 BASIC** primer (15 units) teaches the language
itself: typing and editing, `PRINT`/`LET`/`INPUT`, `IF`/`THEN`, `FOR`/`NEXT`,
`GOTO`/`GOSUB`, then the four hardware surfaces the games lean on — the screen as
memory (`POKE 1024`), colour RAM (`55296`), the SID (`54272`), the joystick
(`PEEK 56320`) — plus the animation loop, `SAVE`/`LOAD`, and reading errors. The
games assume all of it.

---

## Volume 1: First Programs (8 games)

The volume is a ramp from a static picture to a physics game, and the C64's
hardware comes on one surface at a time:

| # | Game | Headline concept | New ground (C64 BASIC) |
|---|------|------------------|------------------------|
| 1 | **Skyline** | Composition | Screen RAM + colour RAM as a canvas; `1024 + R*40 + C`; nested `FOR` |
| 2 | **Oracle** | Chance | `RND` → choice; string arrays (`DIM A$`); `ON…GOTO` |
| 3 | **Reflex** | Tension | The jiffy clock (`TI`); `GET`; border flash (`53280`) |
| 4 | **Tally** | Emergence | Numeric arrays; a POKEd bar chart; `PRINT` formatting |
| 5 | **Bleeper** | Memory | Sequences in arrays; SID notes as data; build-and-replay |
| 6 | **Safe Cracker** | Deduction | Bracket narrowing; a guess limit; colour-coded feedback |
| 7 | **Rover** | Control | The real-time joystick loop; `PEEK`-the-screen collision |
| 8 | **Dropzone** | Risk & reward | Velocity/gravity as variables; thrust; win/lose states |

**Hardware on-ramp:** Skyline owns the screen; Reflex adds the clock and the
border; Bleeper brings the SID up to a voice with rhythm; Rover takes the
joystick into a live loop; Dropzone fuses them into a game with a goal.

---

## Design concepts — headline and embedded

Each game leads with one **headline** game-design concept (the thing a player
feels) and carries one **embedded** concept (a quieter craft idea, introduced
here, reused later). This is the same structure as the Spectrum BASIC track.

| Game | Headline | Embedded |
|------|----------|----------|
| Skyline | Composition — placing parts to make a whole | Coordinates — addressing by row/column |
| Oracle | Chance — the machine surprises you | Suspense — the pause before the reveal |
| Reflex | Tension — time pressure creates engagement | Telegraphing — warn the player it's coming |
| Tally | Emergence — pattern out of many trials | Visualisation — show data as a picture |
| Bleeper | Memory — hold and reproduce a sequence | Escalation — each round raises the load |
| Safe Cracker | Deduction — narrow hidden information | Stakes — a limited number of tries |
| Rover | Control — real-time, responsive movement | Collision — the world pushes back |
| Dropzone | Risk & reward — push your luck against gravity | Physics — velocity accumulates over time |

---

## Game designs

### Game 1: Skyline — *Composition*

**Pedagogical role.** Make the screen a canvas the learner addresses by hand:
screen RAM at 1024, colour RAM at 55296, and `1024 + R*40 + C` as the one formula
that reaches any cell — the foundation every later game draws on.

**Ancestors.** Magazine "draw a picture" type-ins; the skyline/cityscape demo
that opened a hundred listings.

**Core experience.** A city rises out of black — towers of solid blocks climb
the screen, windows light up in colour, one block at a time. No input, no loop
yet: the joy is watching a picture you wrote appear.

**New ground.** Nested `FOR` (rows × columns); the colour cell that rides
alongside each screen cell; `RND` for window lights and tower heights so no two
runs match.

**Topic arc (~5–6).** A single block → a tower with `FOR` → a row of towers →
colour the windows → randomise the skyline → a sunset palette (border +
background).

**Anti-goals.** No movement, no input, no game loop — this is the canvas, not the
game. Those arrive in Rover.

---

### Game 2: Oracle — *Chance*

**Pedagogical role.** Randomness as a game ingredient: `RND` chooses, a string
array holds the choices, and `ON…GOTO`/chained `IF` turns a number into an
outcome — the selection machinery behind every later game's variety.

**Ancestors.** The Magic 8-Ball type-in; fortune-teller listings.

**Core experience.** Ask a yes/no question, press RETURN, and the Oracle *thinks*
— a beat of suspense, a colour shift — then answers. Ask again; the answers vary.

**New ground.** String arrays (`DIM A$(N)`), `RND` as an index into them, a
suspense pause, colour as the Oracle's "mood".

**Topic arc (~5–6).** One fixed answer → pick from two with `RND` → a `DIM`'d
list of answers → the thinking pause → colour-coded moods → ask-again loop.

**Anti-goals.** No scoring, no real-time input, no persistent state. One question,
one answer.

---

### Game 3: Reflex — *Tension*

**Pedagogical role.** Real time enters: the jiffy clock `TI` measures it, `GET`
reads a keypress without stopping, and the border flash is instant feedback — the
learner leaves able to *measure* and to react.

**Ancestors.** The reaction-tester, a magazine staple from 1982; stopwatch
listings.

**Core experience.** Watch the screen. Wait — the wait stretches, deliberately.
The border flashes; slam a key. Your time appears. Try to beat it.

**New ground.** `TI`/`TI$` (the 1/60s jiffy clock), `GET` vs `INPUT`, a random
wait before the signal, `POKE 53280` for the flash, a rating from the time.

**Topic arc (~6).** Flash the border → wait a random spell → time the gap with
`TI` → read the key with `GET` → show the result → rate it (and catch a too-early
press).

**Anti-goals.** No moving target, no multi-round loop, no stored bests. One
reaction, one number.

---

### Game 4: Tally — *Emergence*

**Pedagogical role.** Arrays as counters and the screen as a chart: many trials
accumulate into tallies, and those tallies POKE a live bar chart — data made
visible, the first time the program produces more than it was told.

**Ancestors.** The dice-statistics type-in; "roll 1000 times and graph it"
listings.

**Core experience.** Choose how many rolls. The C64 rolls, and bars climb cell by
cell as each face tallies up — the bell curve appears out of pure randomness.

**New ground.** Numeric arrays (`DIM T(6)`), accumulation in a `FOR` loop, a bar
chart POKEd into screen + colour RAM, `PRINT`/`TAB` formatting for labels.

**Topic arc (~6).** One die roll → tally six faces in an array → print the counts
→ draw one bar by POKE → all six bars → let the player set the run count.

**Anti-goals.** No real-time animation of each roll, no two-player play. The
result is the picture, not a race.

---

### Game 5: Bleeper — *Memory*

**Pedagogical role.** A sequence lives in an array and speaks through the SID:
the program builds a growing pattern, plays it, and checks the player's echo —
arrays-as-data plus the SID as a voice with rhythm.

**Ancestors.** *Simon* and its hundred type-in cousins; "repeat the tune"
listings.

**Core experience.** Four colour panels. The C64 plays a tone-and-flash sequence;
you repeat it. Each round it adds one. How far can you hold?

**New ground.** A sequence stored and grown in an array, SID notes chosen per
panel (`54272…`), a play-back loop, reading and comparing the player's input
with `GET`.

**Topic arc (~6–7).** Light and bleep one panel → a fixed 3-step sequence → store
it in an array → grow it by one each round → read the player's echo → score and
escalate.

**Anti-goals.** No three-voice music (that's a game's job, not a primer-adjacent
one), no high-score table. The escalation is the depth.

---

### Game 6: Safe Cracker — *Deduction*

**Pedagogical role.** Hidden information and narrowing logic: the player brackets
a secret with higher/lower feedback under a guess limit — the loop-with-a-goal
that win/lose states are built on.

**Ancestors.** Hi-Lo / "guess my number"; the safe-cracking type-in with a dial.

**Core experience.** A locked safe, a hidden code. Each guess gets a higher/lower
hint and a colour. The clock is your guess count — crack it before it runs out.

**New ground.** A secret from `RND`, the higher/lower comparison, a guess counter
and limit, colour-coded feedback, win and lose endings.

**Topic arc (~6).** Pick a secret → take a guess → higher/lower hint → loop until
right → colour the feedback → add a guess limit and a lose state.

**Anti-goals.** No multi-digit Mastermind-style pegs (that's a later, bigger
game), no real-time pressure. Pure deduction.

---

### Game 7: Rover — *Control*

**Pedagogical role.** The first real-time game: the joystick drives a continuous
loop, and `PEEK`-ing the screen *ahead* of the rover detects what it's about to
hit — live input plus collision, the core of every action game.

**Ancestors.** The maze/chase type-in; *Compute!'s Gazette* character-graphics
action games.

**Core experience.** Steer a rover around a screen of walls and pickups. It moves
while you hold the stick; it stops at walls; it scores on pickups. The screen is
the world and the rover lives in it.

**New ground.** `PEEK(56320)` in a live loop, move-erase-redraw from the primer,
`PEEK` of the target cell for collision, bounds and walls, a score.

**Topic arc (~6–7).** A rover you can place → move it by joystick → keep it on
screen → draw walls and stop at them → scatter pickups and score → a goal /
finish.

**Anti-goals.** No physics, no enemies with AI, no win-by-survival yet. Control
and collision first.

---

### Game 8: Dropzone — *Risk & reward*

**Pedagogical role.** A complete game with a goal: gravity and thrust as
accumulating variables, a craft you fly, and explicit win/lose states — the loop,
the input, the screen, and the SID all at once.

**Ancestors.** *Lunar Lander*; the "land the ship" type-in.

**Core experience.** A lander drifts down under gravity. Thrust to slow it, manage
your fall, and set down softly on the pad — or come in too fast and crash. One
clean landing is the whole reward.

**New ground.** Velocity as a variable that gravity grows and thrust shrinks,
thrust input (key or stick), a landing test (speed at touchdown), win/lose
endings, SID for thrust and crash.

**Topic arc (~7).** A falling dot → gravity accelerates it → thrust pushes back →
a landing pad → the soft-vs-hard landing test → win and crash screens → fuel as
the squeeze.

**Anti-goals.** No scrolling, no horizontal flight, no multiple levels. One pad,
one landing, done well — the capstone of the volume.

---

## Concept progression summary

**Headline concepts, by first appearance:** Composition (1) → Chance (2) →
Tension (3) → Emergence (4) → Memory (5) → Deduction (6) → Control (7) → Risk &
reward (8).

**C64 BASIC techniques, by first appearance:**
- **Skyline:** nested `FOR`; screen + colour RAM as a canvas; `1024 + R*40 + C`.
- **Oracle:** string arrays (`DIM A$`); `RND` as an index; `ON…GOTO`.
- **Reflex:** `TI` jiffy clock; `GET`; the random wait; `POKE 53280`.
- **Tally:** numeric arrays; accumulation; POKEd bar charts; `TAB`.
- **Bleeper:** sequences grown in arrays; SID notes as data; compare-the-echo.
- **Safe Cracker:** narrowing logic; a counter + limit; win/lose endings.
- **Rover:** real-time `PEEK(56320)` loop; `PEEK`-the-screen collision; walls.
- **Dropzone:** velocity/gravity variables; thrust; a landing test; fuel.

**The bridge to assembly.** Every hardware surface the volume touches — 1024,
55296, 53280/53281, 54272, 56320 — is a memory address the assembly track revisits
at machine speed. A learner finishing Dropzone has already been doing
memory-mapped I/O for seven games.

---

## Excluded (out of scope for V1)

Sprites (VIC-II `$D000…`), raster effects, custom characters, three-voice SID
music, machine-code `SYS` calls, and disk file handling beyond `SAVE`/`LOAD`.
These belong to later volumes or the assembly track; V1 stays in stock BASIC V2
on the screen-and-colour surface.

---

## Future volumes

Volume 1 is the committed scope. Further volumes (deeper games — sprites via
register POKEs, SID music, larger systems) may follow the Spectrum track's
four-volume shape, but are not designed here yet. The bridge note above is the
intended hand-off to C64 assembly regardless.
