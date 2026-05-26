# Sinclair ZX Spectrum BASIC Curriculum (v6.4 DRAFT)

**Platform:** Sinclair ZX Spectrum 48K
**Language:** Sinclair BASIC
**Games:** 32
**Volumes:** 4 (8 games each)

> **v6.4 in progress (2026-05-19).** v6.4 is a *rename pass* on v6.3 — 11 games using canonical / trademarked names get inspired-by replacements per the [inspired-by-not-clones naming convention](../../../../decisions/inspired-by-not-clones-naming.md). All v6.3 structural decisions carry forward unchanged. The renames: Magic 8-Ball → **Oracle Stone**, Hangman → **Cipher**, Mastermind → **Locksmith**, Battleship → **Sonar**, Tic-Tac-Toe → **Three in a Row**, Hunt the Wumpus → **The Caverns**, Hammurabi → **Yearfall**, Pong → **Volley**, Asteroids → **Drift**, Frogger → **Quickstep**, Pac-Man → **The Hungry Maze**. All marked first-draft, needs-workshop. Source of truth: changelog entry below, plus `memory/spectrum-basic-v6.4-reframe.md` and `decisions/spectrum-basic-v6.4-renames.md`.
>
> **v6.3 in progress (carried over).** The top-of-document tables (volumes, design concepts, embedded concepts, scope estimates) reflect v6.3 + the v6.4 names. The per-game spec sections further down still describe the v6.2 16-game lineup and are scheduled for revision. The v6.4 rename applies to whatever per-game sections eventually get written for the 11 affected games.

---

## What this curriculum is

Code198x is a comprehensive games-development education on vintage systems. The learner studies how the legends of yesterday made games that have stood the test of time — and what techniques and design ideas they used to do so. The work transfers: to other vintage systems, to modern engines, to software outside games.

**Most legendary Spectrum games were written in assembly, not BASIC.** *Manic Miner*, *Knight Lore*, *Cybernoid*, *The Hobbit* — the games whose names a Spectrum learner already knows — shipped in Z80 machine code, with the techniques that defined the era's commercial bar. The Spectrum BASIC track does not teach those games directly. It teaches the *concepts* those legends used, in vehicles drawn from the broader 80s computing tradition: magazine type-ins, toy ports, and design ideas that travelled across machines. The Spectrum Assembly track (Shadowkeep and its successors) is where the learner crosses into Z80 and learns how the legends actually built their commercial-bar games. Together, BASIC and Assembly form one Spectrum journey.

This document describes the **Sinclair BASIC track** for the ZX Spectrum 48K. It is the on-ramp: where the learner builds a vocabulary of design concepts and craft techniques on a forgiving language, before crossing to assembly to put them to work at scale.

The BASIC track teaches two things in parallel:

- **Design concepts** — universal principles that make games work as games: response, tension, pattern, physics, opponents, narrative ecology. These transfer to any platform, any language, any era. Each concept is named in *player-facing* language — the way the player experiences it — alongside the *industry term* the learner will meet later in modern engines.
- **Techniques** — the named tricks of the trade that travelled the era: PLOT/DRAW pixel rendering, custom character sets, attribute-file POKE, cell-by-cell physics ticks, verb-noun parsers. Each technique is a small piece of craft the learner can name and reuse. The *commercial-bar* techniques the Spectrum legends used (smooth scrolling, sprite multiplexing, raster work, music drivers, loaders) live in the Assembly track — not because BASIC couldn't gesture at them, but because they were genuinely shipped in Z80, and teaching them honestly means teaching them in the language they were written in.

Each game is a sequence of **topics**, each producing a working result. Topics are not uniform — some take half an hour, some take three — because real games-development work isn't uniform. Polish weaves through; it is not a finishing pass.

Every game in the lineup is **drawn from canon** — a real period game, a toy port with home-computer history, or a magazine type-in tradition. No game in this track is constructed-for-curriculum: each has historical context the learner can study alongside their build.

Volume 4 is where the curriculum first reaches the *conceptual ground* of Spectrum-native legends — the single-screen platformer (Rooftops, in the Manic Miner tradition), the wave-based shooter (Blockstorm, in the Cybernoid tradition), the parser adventure (Thornwood Manor, in The Hobbit tradition). A learner who finishes Volume 4 has built games at the *design scale* of those legends — and is ready to cross to assembly to build at their *commercial scale*.

A learner who completes the BASIC track can build games at the bar of *Computer Spacegames* (Usborne, 1982), *Practise Your BASIC* (Usborne, 1983), and the magazine type-ins of the era. They will recognise where each concept and technique they learned reappears in modern game engines and modern software.

**See also:** `sinclair-zx-spectrum-basic-visual-progression.md` — the visual design philosophy that drives how each game looks and feels.

---

## The four volumes

Each volume is 8 games. Powers-of-2 hold per-volume (8) and total (32).

| Volume | Theme | Games | Concept arc |
|--------|-------|-------|-------------|
| **1. First Programs** | The on-ramp | 1-8 | Output → Response → Chance → Tension → Accumulation → Pattern → Narrowing → Descent |
| **2. Patterns of State** | Turn-based logic, data, reasoning | 9-16 | Data-Driven → Progression → Deduction → Search → Adversary → Atmosphere → Consequences → The Rule IS the Game |
| **3. Worlds and Rules** | Real-time worlds with rules | 17-24 | The Game Won't Wait → Volley → Physics → Momentum → Timing → Pursuit → Defence → Escalation |
| **4. Stories and Systems** | Synthesis at scale | 25-32 | Character → Custom Worlds → Rooms → Designed Worlds → Generated Worlds → Parser → Systems → Living Worlds |

Each volume is its own coherent arc. A learner who finishes any volume has finished a real curriculum, not a fragment.

Each volume also has a distinct *type of game*:
- **V1** is the on-ramp — many small first programs that teach the rhythm of interactive software. Honest to the Usborne tradition of *many tiny programs*, not 4 medium ones.
- **V2** is *programs that think* — turn-based, state-driven games where the player reasons.
- **V3** is *programs that act* — real-time worlds with rules, where the world ticks whether you act or not.
- **V4** is *programs that tell stories* — bigger systems that produce character, pacing, generation, and narrative. V4 uses **2-deep tour-then-deepen** ordering: introduce two storytelling forms (Rooftops, Stonefall), deepen both; introduce two more (Dorin, Thornwood), deepen both. Volume halves at slot 28/29 (graphical traditions → narrative traditions).

---

## Rough scope estimates

Topics are variable-length, but rough scope hints help learners plan their time. Estimates below are first-pass for v6.3 (32 games); they will firm up as topics are written.

| Volume | Games | Approx. topics | Approx. hours |
|--------|-------|----------------|---------------|
| 1 First Programs | 8 | ~40-55 | ~50-80 |
| 2 Patterns of State | 8 | ~60-85 | ~90-130 |
| 3 Worlds and Rules | 8 | ~95-135 | ~140-220 |
| 4 Stories and Systems | 8 | ~130-180 | ~200-330 |
| **Total** | **32** | **~325-455** | **~480-760** |

A single topic is 60-90 minutes for the learner who reads carefully and types in patiently. Faster readers will be on the lower bound; learners who pause to experiment will run longer.

V1 games are deliberately small (3-8 topics each) — honest to the Usborne *Computer Spacegames* tradition of many short type-ins. V4 games are deliberately large (15-30 topics each) — capstone storytelling deserves the room.

Per-game rough size hints appear in each game's section below. **Lucky Number's full topic list is worked out as the v6.2 pedagogy exemplar** — every game will eventually carry a topic list of similar shape, built up topic-by-topic from the smallest working program. v6.3 adds 16 new game spec sections still to be written.

---

## Design concepts — headline and embedded

Each game carries a **headline concept** (the spine of the lesson) and one or two **embedded concepts** (named in the body text, taught as the game develops). Each headline appears in *player-facing* language with the *industry term* (where different) given alongside, so the learner internalises both the design idea and the name they will meet later in modern development.

| # | Volume | Game | Player-facing headline | Industry term |
|---|---|------|------------------------|---------------|
| 1 | V1 | Story Builder | **Output** — the first program speaks | — |
| 2 | V1 | Lucky Number | **Response** — the game communicates without words | — |
| 3 | V1 | Oracle Stone | **Chance** — the program decides | — |
| 4 | V1 | Reflex | **Tension** — time pressure creates engagement | — |
| 5 | V1 | Dice Roller | **Accumulation** — patterns emerge from randomness | — |
| 6 | V1 | Bright Spark | **Pattern** — recognise, reproduce, extend | — |
| 7 | V1 | Hi-Lo | **Narrowing** — feedback brings you closer | — |
| 8 | V1 | Touchdown | **Descent** — the program runs whether you act or not | *Game Loop* |
| 9 | V2 | Cipher | **Data-Driven** — the content shapes the experience, not the code | *Content vs Logic* |
| 10 | V2 | Quiz Master | **Progression** — the player grows, the score climbs | — |
| 11 | V2 | Locksmith | **Deduction** — encoded clues, reasoned through | — |
| 12 | V2 | Sonar | **Search** — coordinates as a way of knowing | *Grid Search* |
| 13 | V2 | Three in a Row | **Adversary** — the program plays against you | *Game AI* |
| 14 | V2 | The Caverns | **Atmosphere** — fear of the unseen | *Hidden Information* |
| 15 | V2 | Yearfall | **Consequences** — choices land later | *Resource Management* |
| 16 | V2 | Crates | **The Rule IS the Game** — the mechanic is the experience | *Mechanics as Meaning* |
| 17 | V3 | Tail Chase | **The Game Won't Wait** — the world runs whether you act or not | *Continuous Motion* |
| 18 | V3 | Volley | **Volley** — the joy of the rally | *Paddle Physics* |
| 19 | V3 | Brick Bash | **Physics** — objects obey rules that feel right | — |
| 20 | V3 | Drift | **Momentum** — the ship keeps going when you stop | *Inertia* |
| 21 | V3 | Quickstep | **Timing** — read the patterns, find the windows | *Hazard Patterns* |
| 22 | V3 | The Hungry Maze | **Pursuit** — being hunted, then turning the tables | *Chase AI* |
| 23 | V3 | Night Patrol | **Defence** — many targets, limited interceptors | *Multi-Target* |
| 24 | V3 | Blockstorm | **Escalation** — when to push, how much, what to change | *Difficulty Curves* |
| 25 | V4 | Rooftops | **Character** — a sprite that feels alive | — |
| 26 | V4 | Stonefall | **Custom Worlds** — your own grammar of characters | *Custom CHARS* |
| 27 | V4 | Skyhold | **Rooms** — exploration across screens | *Multi-Screen State* |
| 28 | V4 | Deepworks | **Designed Worlds** — hand-laid worlds, readable affordances | *Level Design* |
| 29 | V4 | Dorin | **Generated Worlds** — the computer as co-creator | *Procedural Generation* |
| 30 | V4 | Thornwood | **Parser** — speaking to the machine | *Two-Word Parser* |
| 31 | V4 | Dungeons of Dorin | **Systems** — combat, items, persistence | *RPG Mechanics* |
| 32 | V4 | Thornwood Manor | **Living Worlds** — scripted reactivity, narrative ecology | *Narrative Ecology* |

| Game | Embedded concepts |
|------|-------------------|
| 1 Story Builder | First impressions |
| 2 Lucky Number | Juice |
| 3 Oracle Stone | Anticipation |
| 4 Reflex | Telegraphing |
| 5 Dice Roller | Anticipation, mastery through practice |
| 6 Bright Spark | Signposting |
| 7 Hi-Lo | Feedback loops |
| 8 Touchdown | Ambient feedback |
| 9 Cipher | Difficulty curve via content |
| 10 Quiz Master | Ratings as social proof |
| 11 Locksmith | Information layering |
| 12 Sonar | Systematic search |
| 13 Three in a Row | AI personality |
| 14 The Caverns | Atmosphere (also headline), spatial reasoning |
| 15 Yearfall | Trade-offs, delayed consequences |
| 16 Crates | Constraint as gameplay |
| 17 Tail Chase | Failure as content |
| 18 Volley | Joy of the rally |
| 19 Brick Bash | Risk and reward |
| 20 Drift | Kinaesthetic feel, anticipation |
| 21 Quickstep | Patience as skill, anticipation |
| 22 The Hungry Maze | Power reversal, AI personality |
| 23 Night Patrol | Apparent vs actual intelligence |
| 24 Blockstorm | Resource management, difficulty curve |
| 25 Rooftops | Animation as state communication |
| 26 Stonefall | Aesthetic identity (the program's voice) |
| 27 Skyhold | Exploration, joy of new screens |
| 28 Deepworks | Authored experience, telegraphing, signposting, risk and reward |
| 29 Dorin Pt 1 | Replayability, emergent stories, risk and reward |
| 30 Thornwood | Limits of vocabulary, trade-offs |
| 31 Dorin Pt 2 | Emergent stories |
| 32 Thornwood Manor | Player agency, failure recovery, atmosphere, trade-offs, emergent stories, the world remembers |

These concepts are universal. A learner doing the Spectrum Assembly track, or a future C64 / NES / Amiga track, would encounter many of the same concepts — implemented with different tools. Repetition across tracks is reinforcement, not redundancy.

---

## Pixel graphics from early on

PLOT and DRAW arrive in Game 2 (Reflex), the second game the learner builds — early enough that the curriculum's visual identity is *pixel graphics, not character-cell workarounds*. Reflex's target marker, telegraph bar, and score display all use real pixel drawing. By Game 10 (Brick Bash), PLOT/DRAW are old friends — the new techniques there are POINT (reading pixels back), CIRCLE, and trigonometry for angle-based physics.

Lucky Number itself stays in PRINT/colour territory (the pedagogy is gradual; the first game introduces concepts cleanly without piling on PLOT/DRAW too soon), but the Spectrum's pixel capability is signalled by Game 2 and used liberally from there on. The Spectrum can draw. We teach that early — and *via the learner's own hands*, not via a starter program they typed without understanding.

---

## Polish woven through

Commercial vintage games were polished as they were built, not at the end. Every feature came with its polish: the title screen with personality, the right BEEP when the player picked up an item, the strobe on the win, the attract mode that played itself if the player walked away.

This curriculum echoes that discipline. Each game's topic list weaves polish moments through the work — *The Title Screen*, *The Win Celebration*, *Attract Mode*, *Sound Design Pass*, *The High Score Table* — sitting alongside the topics that build the game's mechanics. Polish is not a finishing chapter. It is the craft.

The pattern library hosts reusable polish patterns (title-screen frames, scoreboard digits, attract-mode dispatchers) that each game's polish topics draw on.

---

## A note on game ordering

Two ordering choices in this curriculum may surprise readers who expect the conventional textbook progression:

- **Stonefall (Game 12) introduces custom character sets (CHARS) before Rooftops (Game 13) introduces UDGs.** Most Spectrum tutorials teach UDGs first because they are a smaller, simpler subset of the same idea. Code198x does the opposite — because Stonefall needs *tile-based, full-screen* graphics where the entire font is replaced (no text co-exists), and Rooftops needs *sprite-with-text* where UDGs are the right tool to preserve the surrounding font. The curriculum chooses the right tool for each game's scope rather than the conventional easier-first order.
- **No bomb-defusal game.** A previous draft used a constructed bomb-defusal (Wire Panic) for Tension. The new Reflex (reaction tester) is more period-authentic, simpler, and teaches the same V1 language features. Bomb defusal isn't a Spectrum-era genre; reaction testing is.

---

## Volume 1: First Programs

The on-ramp. Four small games — a number-guess, a reaction tester, a Simon Says memory game, and a lunar lander — teach the fundamental rhythm of interactive software: respond, hold tension, recognise patterns, react in real time. The pedagogy is gradual: every game starts with the smallest possible working program and builds up one concept at a time. By the middle of each game the learner has something playable; by the end they have something polished. Every game in this volume has direct period canon: magazine type-ins, toy ports, and the canonical *Lunar Lander* tradition.

---

### Game 1: Lucky Number

**Volume:** 1 First Programs
**Genre:** Number guessing
**Approx. size:** 9 topics, ~10-15 hours. Grows from 1 line (topic 1) to ~25-35 lines (topic 9) of BASIC, every line owned by the learner. *(Topic list worked out below as the v6.2 pedagogy exemplar.)*

The computer picks a number between 1 and 100. The player guesses. The computer says higher or lower. Simple, ancient, and a perfect first game.

The learner builds Lucky Number from nothing. The first topic is a single line: `PRINT "Hello"`. Each subsequent topic adds one concept — variables, input, decisions, looping, randomness — and produces a working program at every step. By topic 6 the learner has a complete playable guessing game in about ten lines. Topics 7-9 layer on the polish: random numbers for replayability, colour and sound for *response*, a title screen and ratings for *juice*. By the end the learner owns every line of their Lucky Number — and has met the curriculum's first two design concepts as things they *built*, not things they *typed in*.

**Headline concept:** Response — the game communicates without words.

**Embedded:** Juice — the non-essential signal that makes the essential feel alive. The win celebration's strobing border, ascending tones, and green digit-recolour is Juice in the modern sense; the temperature bar is information design. The learner builds both; later writers separate them.

**Design lesson:**
The temperature bar is a *proximity indicator* — a design pattern used in everything from children's games to modern radar systems. The border colour shift is *ambient feedback* — information delivered through the environment rather than text. The victory celebration is *reward framing* — making the player feel their achievement. The directional BEEP (ascending for "guess higher", descending for "guess lower") is *audio feedback* — sound carrying meaning. None of this is explained as theory. The learner plays the game and feels it working.

**Topics (worked example — this is the v6.2 pedagogy demonstrated):**

Lucky Number is the curriculum's first game and the worked example of the curriculum's teaching shape: gradual concept introduction, one new BASIC idea per topic, every topic produces a working program, polish woven through the build rather than tacked on at the end. Each subsequent game in the curriculum follows the same shape — start small, build up, polish across the arc.

1. **Your first program.** Type `10 PRINT "Hello"`. Type `RUN`. The screen prints `Hello`. You've just written a program. It does what you told it to do — that is *response*, the curriculum's first design concept and the simplest one. `PRINT` puts text on the screen. **Milestone:** you understand that a numbered line of BASIC is a command the computer obeys.

2. **More to say.** Add more lines: `20 PRINT "Welcome to Lucky Number"`, `30 PRINT "Let's play!"`. Try `5 CLS` to clear the screen first. The program is starting to look like a game's opening. *Polish moment*: which message did you choose, and which order? You're already making design decisions. **Milestone:** you can build up a program from multiple PRINT statements and clear the screen.

3. **Remembering things.** Introduce `LET`. `LET n = 42` tells the computer to remember the number 42 under the name `n`. Then `PRINT n` reads it back. Try changing 42 to another value, run, see the computer remember what you told it. Now write `LET n = 42`, `LET n = n + 1`, `PRINT n`. The computer prints 43. Variables are little boxes you can write to and read from. **Milestone:** you understand variables.

4. **Asking the player.** Add `INPUT "Your guess: "; g`. Run the program. The computer pauses and waits for the player to type a number. Whatever they type goes into the variable `g`. Then `PRINT "You said "; g` proves the computer remembered it. The program now *interacts*. **Milestone:** you understand the difference between INPUT (asks the player, waits) and PRINT (tells the player, moves on).

5. **Decisions.** Add `IF/THEN`. `IF g > 50 THEN PRINT "Too high"`. `IF g < 50 THEN PRINT "Too low"`. `IF g = 50 THEN PRINT "Correct!"`. Run the program. The computer now responds *differently* depending on the guess. *Response* — introduced in topic 1 — has grown teeth: the computer reasons about what you gave it and reacts in character. Try changing `>` to `>=` and see what happens. **Milestone:** you understand comparisons (`<`, `>`, `=`) and conditional output.

6. **Going round again.** The game ends after one guess. That's not a game; that's a turn. Add `GO TO 40` after the wrong-guess messages so the program loops back to the INPUT and asks again. Run it: the game keeps asking until the player gets it right. You've just built the *game loop* — the structural shape every real-time and turn-by-turn game shares. Try `REM`-ing out the GO TO; the program runs once and stops. **Milestone:** you have a complete, playable guessing game in about ten lines.

7. **A different number every time.** The secret is always 50, which gets boring fast. Replace `LET n = 50` with `LET n = INT(RND*100)+1`. Take it apart: `RND` gives a number between 0 and 1, `RND*100` between 0 and 100, `INT` rounds down to a whole number, `+1` shifts the range to 1-100. Add `RANDOMIZE` at the start of the program so the sequence differs each run. The game is now properly random and replayable. *Polish moment*: try `INT(RND*10)+1` for an easier game (1-10), or `INT(RND*1000)+1` for a hard one. **Milestone:** you understand random numbers and can tune the difficulty by changing one line.

8. **Make it feel like a game.** The game works, but it speaks only in words. Real games speak with colour and sound too — that's *response* at its richest. Add `BORDER 1` (blue) at the start. Then, just before the response messages, compute the distance: `LET d = ABS(g - n)`. Set the border based on distance: `IF d > 50 THEN BORDER 1` (cold blue), down through `IF d < 5 THEN BORDER 7` (hot white). Now the screen surroundings *tell the player how close they are* before they read the words. Add sound: `BEEP 0.1, (n - g) / 10` plays a low note when guess is too high, a high note when too low — the directional BEEP. We now name what you've built: **Response** as a design discipline. The temperature you can feel, the tone you can hear, the words you can read — three channels saying the same thing, each in its own way. **Milestone:** you understand ambient feedback and can use the Spectrum's colour and sound model.

9. **Make it your own.** Lucky Number is now a complete, responsive guessing game. The final topic is polish — the layer that makes it feel like *your* game, not just a working program. Add a title screen: a few PRINTs at the top in your own voice, with `PAUSE` for drama before the game starts. Add a guess counter: `LET c = c + 1` on every guess, `PRINT "Guess "; c` somewhere visible. Add ratings: if the player wins in under 5 guesses, print "Incredible!"; under 10, "Pretty good"; otherwise, "Well, you got there." This *extra* layer — celebration, rating, presentation — is what later writers call **juice**: signal that isn't essential but makes the essential feel alive. The game would still work without juice. Would it *feel* like a game? Try it both ways and see. **Milestone:** you've built Lucky Number from a single PRINT to a polished, complete game — and you've met response and juice as the two sides of the same coin.

**Techniques learned:**
- **Distance-driven BORDER feedback** — using `ABS(g - n)` to compute how close the guess is and selecting a BORDER colour from the result (blue when cold, white when hot). Ambient feedback the player reads peripherally. This pattern — *a numeric distance mapped to a visual or audio range* — recurs in every game with proximity, danger, or progress signals.
- **Directional BEEP composition** — `BEEP 0.1, (n - g) / 10` plays an ascending tone when the guess was too low and a descending tone when too high. Sound carrying semantic meaning, not just decoration. The player can play with their eyes closed and still know which way to go.

**New BASIC concepts (understood by end of game):**
| Concept | What the learner discovers |
|---------|---------------------------|
| What a program is | Numbered lines, executed in order |
| The Spectrum keyboard | K-mode (keywords), L-mode (letters), how to enter a program |
| `PRINT` | Putting text on screen |
| Strings | Text in quotation marks |
| `RUN` | Executing the program |
| `LET` | Storing a value in a variable |
| Numeric variables | `g`, `n` — names that hold numbers |
| `INPUT` | Asking the player to type something |
| `IF`/`THEN` | Making a decision based on a condition |
| `=`, `<`, `>` | Comparing two values |
| `GO TO` | Jumping to a different line |
| `REM` | Comments — notes for the programmer |
| `RND` | Random numbers (introduced late, after the game works with a fixed number) |
| `RANDOMIZE` | Seeding the random number generator — different game each time |
| `INT` | Rounding to a whole number (`INT(RND*100)+1`) |
| `LIST` / `NEW` / `RUN` | Editor commands — managing and running programs |
| `STOP` / `CONTINUE` | Debugging tools — pause mid-program and resume |

**Touched at the end:** `BORDER` and `BEEP` appear in topic 8 (formally taught in Games 2-3). Lucky Number is intentionally small and gradual; the visual and audio Spectrum vocabulary that will be foundational across the curriculum is *introduced* here in service of response, then *taught properly* in the games that follow.

**Read alongside:**
- The magazine type-in tradition — Crash and Your Sinclair listings, *Sinclair Programs*. Where number-guessing games like this one were a staple of the era.
- *Computer Spacegames* (Usborne, 1982) — the closest cultural ancestor of Volume 1: short games, written gradually, each producing something playable.
- *Practise Your BASIC* (Usborne, 1983) — the gradual-build pedagogy this volume follows.

**Modern equivalents:**
Lucky Number's feedback machinery is everywhere in modern UX. The temperature bar is the same idea as a Slack typing indicator, a GitHub PR-status colour, an onboarding progress bar — *proximity-to-target* visualised at a glance. The win celebration's juice — strobe, sound, colour shift — is the same vocabulary as the modern "level complete" moment in every mobile game.

**Polish discipline:**
Lucky Number's polish lives largely in topics 8 and 9 — colour, sound, the title screen, the ratings, the celebration — because those are the layers that turn a working program into a game that *feels* like a game. But polish *thinking* starts earlier: topic 2 asks the learner to choose their welcome messages with care; topic 5 asks them to choose how the computer responds. Every topic carries a small polish beat alongside its mechanical lesson — *which phrasing felt right, which value felt fair, which colour felt apt*. The principle: polish is the discipline of asking *how does this feel?* at every step, not an afterthought.

**Milestone:** The learner has built a complete game from a single PRINT, owns every line they wrote, and has met response (introduced topic 1, given teeth in topic 5, fully demonstrated in topic 8) and juice (named and applied in topic 9) as their first two design concepts.

---

### Game 2: Reflex

**Volume:** 1 First Programs
**Genre:** Reaction tester
**Approx. size:** ~4-6 topics, ~6-10 hours. ~20 lines of BASIC.

The screen shows a target. The program prints "Ready..." and waits a random period — anywhere from one to six seconds. Then the border flashes, a BEEP sounds, and the player must press SPACE as fast as they can. The score is the number of frames between flash and press, measured by the Spectrum's hardware frame counter. Lower is better.

**Headline concept:** Tension — time pressure creates engagement.

**Embedded:** Telegraphing — the half-second loading bar that fills just before the flash gives the alert player a tiny tell. The bar's growth is the same signal as the flash, delivered earlier and quieter; reading it shaves a few frames off the score. The game *tells the player something is coming* if they can read it.

**Design lesson:**
Tension is the *wait*. The longer the player anticipates, the more they tense up — and the more they're tempted to jump the gun (jumping early is a fail). The game's drama lives entirely in the silence between the "Ready..." and the flash. *Telegraphing* — the slight slow-fill loading bar that gives just a fraction of a second of warning — makes the player's pulse quicken right before the moment of action. The score that results is honest: it measures the player's *response time* in raw frames, no negotiation, no quarter given.

**Techniques learned:**
- **PLOT/DRAW for target marker and telegraph bar** — formally introducing pixel drawing in the simplest possible game. The target is one PLOT and a few DRAW lines; the telegraph bar is a DRAW that fills frame by frame.
- **PEEK 23672 for frame-accurate timing** — reading the Spectrum's frame counter to score the player's reaction in honest frames. The same technique that paces Tail Chase later.
- **PAUSE with random duration** — `PAUSE INT(RND*N)+M` for a wait that the player can't predict.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CLS` | Clearing the screen |
| `PRINT AT` | Placing text at a specific row and column |
| `PLOT` | Drawing a single pixel at x,y coordinates |
| `DRAW` | Drawing a line from the current position |
| `INKEY$` | Checking the keyboard without waiting |
| The empty string `""` | What `INKEY$` returns when no key is pressed |
| `PAUSE` | Waiting for a set time |
| `BEEP` | Making sound (duration and pitch) |
| `PEEK 23672` | The frame counter — measuring time in 50ths of a second |
| String variables | `a$` — names that hold text |
| The difference between `INPUT` and `INKEY$` | Blocking vs non-blocking input |

**Read alongside:**
- The magazine reaction-tester type-ins (every issue of Your Sinclair and Crash ran one).
- *Daley Thompson's Decathlon* (Ocean, 1984) — the reaction-test sections at the start of each event.
- *Track and Field* — arcade reaction-test heritage.

**Modern equivalents:**
Reaction tests are everywhere — UX research uses them, mobile game tutorials demonstrate "press at the right time", music games (*Beat Saber*, *Rhythm Heaven*) extend the concept into whole songs. The fundamental loop — random wait, signal, measure response — appears in every reflex-based game ever shipped.

**Polish discipline:**
Reflex's polish is *the wait*. The exact timing of the "Ready..." message, the random delay range (too short = unfair, too long = boring), the flash colour, the score animation when results appear — every polish moment tunes the dramatic arc of a tiny game. The telegraph bar itself is a polish move: take it out and the game still works; leave it in and the player's *skill* becomes the ability to read the telegraph.

**Milestone:** The learner understands two models of input, can draw pixels on screen, can measure time in frames, and can create tension through anticipation.

---

### Game 3: Bright Spark

**Volume:** 1 First Programs
**Genre:** Memory game (Simon Says)
**Approx. size:** ~5-8 topics, ~8-12 hours. ~25 lines of BASIC.

Four chunky colour panels dominate the screen. Simon plays a sequence — each panel flashes with BRIGHT, accompanied by a distinct BEEP tone. The learner watches, then repeats. Sequences grow longer, stored in strings. The learner experiments with all 15 colours (8 base + BRIGHT) and discovers colour as a system, not a decoration.

**Headline concept:** Pattern — recognise, reproduce, extend.

**Embedded:** Signposting — each panel's BRIGHT flash *plus* distinct tone is doubly-clear signposting. The game teaches the player which signal to follow by making the signal unmissable.

**Design lesson:**
Pattern recognition and reproduction is one of the oldest game mechanics. *Sequence length* is the difficulty curve — each round adds one element. *Distinct signals* (colour + sound for each panel) make patterns memorable through multiple senses. *Immediate feedback* on each step (right/wrong) tells the player whether their mental model matches reality. The game teaches the player to build and maintain a *mental model* — the most transferable skill in all of game design.

**Techniques learned:**
- **BRIGHT for emphasis** — using BRIGHT to make one cell of the screen unmistakeable. A core attribute-file technique.
- **FOR/STEP for counted loops** — counting up, counting down, counting in twos. The shape of every iterative process on the Spectrum.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `FOR`/`NEXT` | Counted loops — do something N times |
| `BORDER` | The screen border colour |
| `PAPER` | The background colour |
| `INK` | The text/foreground colour |
| The 8 colours (0-7) | Black, blue, red, magenta, green, cyan, yellow, white |
| `BRIGHT` | Brighter versions of the colours |
| `STEP` | `FOR n=7 TO 0 STEP -1` — counting backwards, counting by twos |
| Nested loops | A `FOR` inside a `FOR` |
| The screen as a grid | 24 rows, 32 columns, each cell has INK and PAPER |

**Read alongside:**
- *Simon* (Milton Bradley, 1978) — the toy the genre is named for.
- Spectrum magazine memory-game type-ins.

**Modern equivalents:**
Pattern recognition with escalation is the spine of spaced-repetition apps (Anki), of CAPTCHA design, and of every mobile match-3 game. The "Simon Says" mechanic continues to ship — *Sequence*, *Lumines* combo systems, the rhythm tutorials in *Beat Saber*.

**Polish discipline:**
Bright Spark's polish is *the panels themselves*. The flash duration, the tone separation, the recovery delay between rounds — every polish moment tunes the *felt* difficulty of the same nominal sequence length.

**Milestone:** The learner understands loops, the Spectrum's colour model, and how pattern length creates difficulty.

---

### Game 4: Touchdown

**Volume:** 1 First Programs
**Genre:** Lunar lander
**Approx. size:** ~6-10 topics, ~10-15 hours. ~40 lines of BASIC.
**Inspired by:** *Lunar Lander* (DEC, 1969; arcade version Atari, 1979), Compute! magazine type-ins, every learn-to-program BASIC book from 1980 onward

A lunar module descends from the top of the screen. Gravity pulls it down every frame. The player presses a key to fire the thrusters, which counter-push for as long as the key is held. Fuel decreases with thrust. Land at low velocity on the pad to win; hit the surface too fast and the module crashes. The border colour shifts from cold blue (high altitude, safe) through warm yellow (close, watch your speed) to red (danger, slow down) as the module descends.

**Headline concept:** Real-Time Reactivity — the game responds the moment input arrives *(industry term: Game Loop)*.

**Embedded:** Ambient feedback — the border colour is *information delivered through the environment*. The player can read their altitude and danger level peripherally without looking at the numbers.

**Design lesson:**
Every real-time game runs the same cycle: read input, update state, draw the result. This is the *game loop* — the universal heartbeat of interactive software, the engineering name for what the player experiences as *the game responding to me, all the time*. Touchdown makes it vivid: each frame, the program reads the thruster key, applies gravity, applies thrust (if any), updates altitude and velocity, depletes fuel, and redraws. The loop runs continuously; gravity pulls whether the player presses anything or not. The structural distinction between a quiz (turn-based, event-driven within waits) and a game (continuous loop, responding inside it) is made vivid by the fact that the lunar module *falls* when the player does nothing — physics doesn't wait for input.

Touchdown is also a clean introduction to *physics as a continuous force*. The player learns that gravity isn't a one-off event — it's an acceleration applied every frame. That intuition will carry forward to Brick Bash (Game 10) where bouncing balls obey similar rules, and into every modern physics engine.

**Techniques learned:**
- **The input → update → draw pattern** — the universal shape of real-time games, written explicitly enough that the learner can identify it in any future game they meet.
- **BORDER for ambient feedback** — using the border colour as a state indicator the player reads peripherally. Altitude becomes a colour the player feels.
- **Velocity and acceleration as variables** — the lunar module's altitude changes by its velocity each frame; velocity changes by gravity (downward) plus thrust (upward, if any). Two named variables that step toward physics at Brick Bash later.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Position and velocity variables | `a` for altitude, `v` for velocity, `f` for fuel |
| Updating physics each frame | `LET v = v + g - thrust` |
| `<>`, `<=`, `>=` | More comparison operators |
| `ABS` | Speed regardless of direction |
| Fixed-point arithmetic | Velocity in tenths to give finer control |
| The game loop | Read input → update state → draw |

**Read alongside:**
- *Lunar Lander* (DEC, 1969) — the original BASIC type-in, predating every commercial port.
- Compute! magazine lander type-ins (1980-1985) — every issue ran a version.
- *Practise Your BASIC* (Usborne, 1983) — included a lander in the early chapters.

**Modern equivalents:**
The input → update → draw loop is the heartbeat of every modern engine. Unity's `Update()`, Godot's `_process()`, the browser's `requestAnimationFrame` — same shape, different language. Lunar Lander itself is one of the most-cloned game designs ever: from *Gravitar* and *Thrust* on consoles, through Flash-era browser games, to modern indie ports — every generation reimplements the formula. The maths of "altitude updated by velocity, velocity updated by gravity-minus-thrust" is unchanged in any modern physics engine.

**Polish discipline:**
Touchdown's polish is *the descent feel*. The exact gravity constant, the thrust strength, the fuel-burn rate, the colour ramp from safe to danger, the BEEP that escalates as you approach the surface, the moment of touchdown (gentle thud or catastrophic crash) — every polish moment tunes the *felt* tension of the slow drop.

**Milestone:** The learner can build a game loop with continuous physics and event-driven thrust input, understands ambient feedback through the border, and has met the building blocks (position, velocity, acceleration as named variables) that Brick Bash will extend.

---

## Volume 2: Patterns of State

Programs that think. Four turn-based games teach the player to reason — about words, about scores, about codes, about pushing crates. Each game is state-driven: no continuous motion, no real-time pressure, just the player's mind doing the work. By Volume 2's end, the learner has the full BASIC vocabulary for data and arrays, and the design intuitions for puzzle-style commercial games.

---

### Game 5: Hangman

**Volume:** 2 Patterns of State
**Genre:** Word guessing
**Approx. size:** ~8-12 topics, ~12-18 hours. ~50 lines of BASIC.

The classic. A word is hidden behind dashes. The player guesses letters one at a time. Wrong guesses build the gallows stage by stage — a head, a body, an arm, an arm, a leg, a leg. Right guesses reveal the word's positions. Win by guessing the word; lose when the gallows is complete.

**Headline concept:** Data-Driven — the content shapes the experience, not the code *(industry term: Content vs Logic)*.

**Embedded:** Difficulty curve via content — the same game logic produces "cat", "house", and "ENCYCLOPAEDIA" — and the felt difficulty shifts dramatically without changing a line of code. The learner discovers that *the data is a difficulty knob*.

**Design lesson:**
Hangman is the canonical demonstration that *the data is the design*. The word list is pure DATA — edit one line and the game is different. Easy words are easy; technical words are hard. The gallows stages are themselves DATA — six progressively-doomed stick figures, stored as DATA strings, printed sequentially. The entire game is logic + data, and changing the data changes the experience without touching the logic. This is the principle behind every level editor, mod tool, and content pipeline in modern game development.

**Techniques learned:**
- **DATA/READ for content lists** — separating game content from game code in the BASIC tradition.
- **The gallows as data-driven graphics** — the six stages of the gallows are six DATA strings, each a multi-line ASCII sprite. The graphics ARE data.
- **Letter-by-letter string scanning** — checking each character of a string against a guess, the foundation of any text-handling game.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| String variables | Using `w$` for the word, `g$` for the guess so far |
| `LEN` | How many characters in a string |
| String slicing | `w$(i)` — the i-th character |
| String concatenation | `a$ + b$` — joining strings |
| String comparison | `IF c$ = w$(i) THEN ...` |
| `DATA` | Storing a list of words and stage graphics |
| `READ` | Pulling the next value from DATA |
| Multi-line strings | Building the gallows from stacked DATA |
| Score tracking | Wins, losses, and words remaining |

**Read alongside:**
- Hangman type-ins in every BASIC tutorial book of the era (Usborne, *Practise Your BASIC*, magazine listings).
- *Wheel of Fortune*-style game shows — Hangman's commercial descendant.
- *Wordy* (Sinclair Research, 1983) — Spectrum word-play with similar DNA.

**Modern equivalents:**
Data-driven design is the principle behind every modern mod tool (*Skyrim*'s Creation Kit, *Mario Maker*, Roblox Studio), every level editor, every data-driven app config (JSON, YAML, TOML files). A game with editable content is a game with a community. *Wordle* (2021) is Hangman's recent viral descendant.

**Polish discipline:**
Hangman's polish is *the gallows*. The progression of the stick figure (head → body → arm → arm → leg → leg), the moment of doom when the final part appears, the celebratory reveal of the word when the player wins, the encouraging "you were close!" when they lose — every polish moment tunes the *feeling of stakes* through pure data.

**Milestone:** The learner can manipulate strings, store data in the program, and understands that separating content from logic makes games flexible and editable.

---

### Game 6: Quiz Master

**Volume:** 2 Patterns of State
**Genre:** Quiz game with categories
**Approx. size:** ~6-10 topics, ~10-15 hours. ~35 lines of BASIC.

A multiple-choice quiz. Four categories, ten questions each, score per round and a running total. The learner creates their own questions.

**Headline concept:** Progression — the player grows, the score climbs.

**Embedded:** Ratings as social proof — the per-round verdict ("Pretty good", "Outstanding", "Quizmaster") tells the player *who they are* in the game's universe. Ratings are tiny narratives about the player's competence.

**Design lesson:**
Progression is the feeling of *getting somewhere*. Quiz Master delivers it through *categories* (four rounds, each a different domain), *accumulating score* (the running total visible at all times), and *per-round ratings* — a player who scored 6/10 sees "Pretty good", 9/10 sees "Outstanding". The arc from "Beginner" to "Quizmaster" is the player's, not the questions'. Behind the scenes, subroutines (GO SUB) and arrays (DIM) make the round-by-round structure possible — the implementation of progression is reusable code and indexed storage. The learner builds the engine of growth.

**Techniques learned:**
- **GO SUB for reusable code** — naming a piece of code and calling it from anywhere. The question-card subroutine is written once and used for every question.
- **DIM for indexed storage** — `DIM s(4)` keeps four scores in one structure. The transition from scalar to array thinking.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `GO SUB` / `RETURN` | Reusable subroutines — code you can call from anywhere |
| `RESTORE` | Rewinding `DATA` to read it again |
| `AND` / `OR` / `NOT` | Combining and negating conditions — `IF NOT found THEN` |
| Simple arrays | `DIM s(4)` — a row of numbered boxes |
| Array access | `LET s(p) = s(p) + 1` — updating a specific element |
| Line numbering conventions | Organising code into sections (100s, 200s, etc.) |
| Multiple colons | Several commands on one line |
| `TAB` | Horizontal formatting — `PRINT TAB 10; "Score"` |

**Read alongside:**
- *Mastermind* on Spectrum — early home-computer logic and code-breaking.
- *Trivial Pursuit* and other quiz adaptations of the era.
- Pub-quiz magazine type-ins.

**Modern equivalents:**
Progression as a design force drives every leaderboard, achievement system, and habit-tracking app today. The "ratings tier" is the same idea as Duolingo's leagues, Stack Overflow's reputation badges, GitHub's contribution streak — small narratives the system tells the user about themselves.

**Polish discipline:**
Quiz Master's polish is *the verdict beat*. The pause before the rating appears, the way the score animates up, the celebratory or commiserating sound — every polish moment tunes the *felt* progression the same numeric arc creates.

**Milestone:** The learner has the full BASIC toolkit for simple programs and understands that progression — the player feeling they are getting somewhere — is something the program shapes deliberately, round by round.

---

### Game 7: Mastermind

**Volume:** 2 Patterns of State
**Genre:** Code-breaking puzzle
**Approx. size:** ~6-10 topics, ~10-15 hours. ~50 lines of BASIC.
**Inspired by:** Mastermind (Invicta, 1971), Bulls and Cows, Spectrum versions in early-80s type-in books

The computer picks a secret four-digit code — each digit between 1 and 6, no repeats. The player makes guesses. After each guess, the computer responds with markers: black for each digit correct in the right position, white for each digit correct in the wrong position. The history of guesses and markers builds up on screen. Deduce the code in ten guesses or fewer.

**Headline concept:** Deduction — encoded clues, reasoned through.

**Embedded:** Information layering — black markers and white markers carry distinct meanings, and the player learns to read both. The game's depth comes from how the player *combines* information from successive guesses.

**Design lesson:**
Deduction is the player's mind doing the work. The game shows you *information*; you derive *knowledge*. Every guess narrows the space of possible codes. The marker system is *information layered*: black and white markers carry distinct meanings, and a perfect player learns to extract every clue from each line. The game's depth comes entirely from the player's reasoning — the computer just keeps score. There's no luck once the code is set: skilful play always solves in fewer guesses.

**Techniques learned:**
- **1D arrays for guess and code** — `DIM c(4)` for the code, `DIM g(4)` for each guess. Indexed positional comparison is the foundation of the marker logic.
- **Comparison logic with state tracking** — counting exact matches (black) versus value-only matches (white) without double-counting requires careful array manipulation. A classic algorithmic exercise.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Numeric arrays | `DIM c(4)` and `DIM g(4)` |
| Array iteration | Two passes over the arrays — exact then partial |
| Used-marker tracking | A parallel array marking which positions are already counted |
| Score and history | Tracking guesses, displaying them stacked |

**Read alongside:**
- *Mastermind* (Mordecai Meirowitz / Invicta, 1971) — the toy that named the genre.
- *Bulls and Cows* — the precursor played with pencil and paper.
- Spectrum Mastermind versions — every type-in book of the early 80s had at least one.

**Modern equivalents:**
Deduction puzzles are alive in *Wordle* (the modern viral hit, which uses the same colour-coded marker system as Mastermind), *Inscryption*, *Return of the Obra Dinn*, *The Witness*. The "give the player information, let them reason" design philosophy is in every detective game.

**Polish discipline:**
Mastermind's polish is *the markers*. The exact look of black vs white pegs, the layout of the guess history, the reveal animation when the code is finally guessed, the small celebration of a perfect game (fewer than five guesses) — every polish moment tunes the *clarity* of the information the player is reasoning from.

**Milestone:** The learner can build a deduction puzzle where the depth comes from the player's reasoning, and understands how layered information shapes player skill.

---

### Game 8: Crates

**Volume:** 2 Patterns of State
**Genre:** Sokoban-style push puzzle
**Approx. size:** ~12-18 topics, ~18-28 hours. ~80 lines of BASIC across the topic arc.
**Inspired by:** Sokoban (Hiroyuki Imabayashi / Thinking Rabbit, 1982), Repton's puzzle elements, modern descendants

The warehouse is a grid of walls, floor, crates, and targets. The player can move and push crates. Crates can only be pushed (never pulled) and only one at a time (never two together). Win by getting every crate onto a target. Each level is hand-laid; the puzzle is the layout.

**Headline concept:** The Rule IS the Game — the mechanic is the experience *(industry term: Mechanics as Meaning)*.

**Embedded:** Constraint as gameplay — the no-pulling rule is what makes Sokoban a puzzle rather than a chore. Every push is potentially irreversible; a crate in the wrong corner is permanently stuck. The constraint is the design.

**Design lesson:**
In most games, the mechanics serve the theme: you *fight* monsters, you *drive* cars. In Crates, the mechanic IS the theme. There's no narrative, no character animation, no theme to peel back — just *push, don't pull, never two at once*, applied to spaces designed to make the rule interesting. The player thinks twice before every step. The *constraint* (no pulling) is what gives every move weight: a crate pushed into a corner is permanently stuck. This is *mechanics-as-meaning* — when the system itself is the experience. Tetris, Go, and Chess work the same way.

**Techniques learned:**
- **ATTR for reading the screen as data** — querying the colour of each cell to determine whether it's wall, floor, crate, or target. The screen *is* the database. The learner discovers that they don't need to keep a separate world array if the screen itself can be queried.
- **Grid game level data** — encoding each level as a multi-line DATA block, parsed at runtime into a 2D world. The pattern that drives every level-based game.
- **Move legality checking** — testing whether a move is allowed (wall blocks, crate-against-wall blocks, crate-against-crate blocks) is the heart of the puzzle. A canonical state-machine exercise.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| 2D level grids | Storing the warehouse as a 2D array |
| Multi-line DATA | Each level as a stack of DATA strings |
| `ATTR` | Reading the colour of a character cell — the screen is data |
| Move legality | Wall blocks, crate-on-crate blocks, crate-on-wall blocks |
| Undo via state snapshots | Saving the previous board to enable backtracking |
| Win condition checking | All crates on targets — game complete |

**Read alongside:**
- *Sokoban* (Hiroyuki Imabayashi / Thinking Rabbit, 1982) — the genre's origin.
- *Soko-Ban* on Spectrum — period ports.
- Modern descendants: *Stephen's Sausage Roll* (Stephen Lavelle), *A Monster's Expedition* (Draknek), *Baba Is You* (Hempuli), the entire Stephen Lavelle / PuzzleScript lineage.

**Modern equivalents:**
Mechanics-as-meaning is its own modern indie genre. Stephen Lavelle's PuzzleScript and the *Stephen's Sausage Roll* / *Linelith* / *Bonfire Peaks* lineage all push one rule into deep puzzle space. *Baba Is You* literally makes the rules into the game pieces. *Tetris* and *Go* are the canonical historical examples. The discipline of "the mechanic IS the experience" is a whole school of design.

**Polish discipline:**
Crates' polish is *the thunk*. The satisfying sound of a crate landing on a target, the visual confirmation when a crate is correctly placed, the cleanness of the wall-push refusal, the moment of recognising "I've stuck a crate forever" — every polish moment tunes the *felt rightness* of the puzzle's logic.

**Milestone:** The learner can build a game where the mechanic is the theme, understands that constraints make choices meaningful, and has met `ATTR` as a queryable-screen technique.

---

## Volume 3: Worlds and Rules

The first ambitious work, and the curriculum's pivot from turn-based reasoning to real-time action. Four games construct worlds that tick whether you act or not: snakes that move continuously, balls that bounce by physics, opponents that pursue, caverns that cascade. By Volume 3's end, the learner can construct simulated worlds in BASIC at the scale of magazine-listing classics.

---

### Game 9: Tail Chase

**Volume:** 3 Worlds and Rules
**Genre:** Snake game
**Approx. size:** ~12-16 topics, ~18-24 hours. ~60 lines of BASIC.
**Inspired by:** Classic Snake, magazine type-in listings

A snake moves continuously across the screen. The learner steers — left, right, up, down — but the snake never stops. Each pickup makes the body grow, trailing behind in an array. Hit a wall or your own tail and it's game over.

**Headline concept:** The Game Won't Wait — the world runs whether you act or not *(industry term: Continuous Motion)*.

**Embedded:** Failure as content — hitting a wall or your tail isn't a punishment, it's the game *resolving*. The snake's growing length means longer survival is its own progression *and* its own risk.

**Design lesson:**
The game loop from Touchdown ran continuously, but at BASIC's natural speed — inconsistent and dependent on what's happening on screen. Tail Chase introduces *frame-rate timing*: the game waits for the Spectrum's hardware frame counter (PEEK 23672) before each update, ensuring consistent speed. This is the universal principle of *delta time* — making game behaviour independent of execution speed. Every modern game engine solves this same problem. And the snake's *failure* — colliding with itself — is part of the design, not a bug: the longer the snake survives, the more dangerous it becomes to itself. That is failure as content.

**Techniques learned:**
- **PEEK 23672 for frame-rate timing** — reading the Spectrum's frame counter to pace the game consistently, independent of what BASIC is doing. (First introduced in Reflex; here it paces the world rather than measures reaction.)
- **Circular-array snake body** — storing N positions in a fixed array, moving an index instead of shuffling data. A demoscene-grade technique applied to a beginner's game.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Continuous movement | The snake moves whether the player presses a key or not |
| Collision detection | Same cell = hit (walls, self, pickups) |
| Game states | Playing, game over, level complete |
| Level progression | Harder each time (more hazards, faster speed) |
| Attribute-file POKE (22528+) | Screen transitions — fade to black row by row |
| `SGN` | Direction of movement — `LET dx = SGN(target - current)` |
| `FLASH` for items | Pickups glitter, hazards pulse |

**Read alongside:**
- The "Snake" type-in tradition — magazines reprinted versions of this game for years.
- *Nibbler* and arcade snake ancestry.

**Modern equivalents:**
Delta time and frame-rate independence are core to every modern engine. Unity's `Time.deltaTime`, Godot's `_process(delta)`, every game loop in every browser game — all solving the same problem PEEK 23672 solves here. The circular array is everywhere in modern code: ring buffers, audio sample queues, undo histories.

**Polish discipline:**
Tail Chase's polish is *the feel of the turn*. The exact frames per cell, the visibility of the snake's head versus body, the sound on pickup, the fade-to-black on game-over — every polish moment tunes the moment the player loses control versus the moment they keep it.

**Milestone:** The learner can build a real-time game with consistent timing and understands frame-rate independence.

---

### Game 10: Brick Bash

**Volume:** 3 Worlds and Rules
**Genre:** Breakout-style action game
**Approx. size:** ~12-18 topics, ~18-28 hours. ~80 lines of BASIC.
**Inspired by:** Breakout, Arkanoid, magazine type-in bat-and-ball games

Bricks built from CHR$ block characters fill the top of the screen. A ball bounces around the play area, drawn with CIRCLE, checked with POINT for pixel-level collision. The bat moves smoothly along the bottom. Where the ball hits the bat determines the reflection angle.

**Headline concept:** Physics — objects obey rules that feel right.

**Embedded:** Risk and reward — where you position the bat changes the angle of the next deflection. Aggressive bat-edge hits send the ball at sharper angles, riskier but faster-clearing.

**Design lesson:**
The ball obeys rules — angle of incidence, reflection, momentum. These rules create *emergent gameplay*: the player doesn't control the ball directly, they control the bat, and the physics determines what happens. Simple bouncing (reverse dx or dy) works but feels mechanical. *Angle-based deflection* from the bat position makes the game *controllable* — skilled players can aim. The maths (SIN/COS/ATN) earns its place by making the game feel better. Physics in games isn't about accuracy — it's about *feel*. And the bat-position choice that determines the angle is a *risk/reward* decision the player makes every bounce.

**Techniques learned:**
- **POINT for pixel-level collision** — reading whether a single pixel is set, the bedrock of fine-grained collision in BASIC.
- **SIN/COS/ATN for angle physics** — trigonometry as a game-feel tool. The bat-impact-to-deflection-angle calculation is the technique that lifts Breakout from bouncing-ball-demo to playable game.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CHR$` 128-143 | Block graphic characters — bricks, borders, frame elements |
| `CHR$` / `CODE` | Character codes, converting between numbers and characters |
| `CIRCLE` | Drawing a circle |
| `POINT` | Reading whether a pixel is set |
| `SIN` / `COS` | Converting an angle to dx/dy velocity components |
| `ATN` | Calculating the deflection angle from bat impact position |
| `TAN` | The ratio of SIN to COS — completes the trigonometry family |
| `ASN` / `ACS` | Inverse functions — velocity components back to angle |
| `PI` | The constant needed for angle calculations |

**Read alongside:**
- *Breakout* (Atari, 1976) — the genre's origin.
- *Arkanoid* (Taito, 1986) — the modernised form.
- *Krakout* (Gremlin, 1987) — the Spectrum classic, sideways-orientated Breakout.
- The magazine bat-and-ball type-ins — *Crash*, *Your Sinclair*, *Sinclair User* all published variants.

**Modern equivalents:**
SIN/COS/ATN for angle calculation IS modern physics. Unity's Rigidbody, Godot's KinematicBody, every 2D physics engine — at the maths level, identical. The "feel" pursuit (game-feel, juice) is unchanged: Steve Swink's *Game Feel* opens with Breakout as the seminal example.

**Polish discipline:**
Brick Bash's polish is *the contact*. The exact BEEP per brick type, the bat-impact sound, the ball's apparent weight (frames per pixel), the brick's vanish animation — every polish moment tunes the *felt* physics of the same maths.

**Milestone:** The learner can build physics-driven gameplay with angle-based deflection and understands that feel — not accuracy — is the goal.

---

### Game 11: Night Patrol

**Volume:** 3 Worlds and Rules
**Genre:** Top-down maze chase
**Approx. size:** ~12-18 topics, ~18-28 hours. ~100 lines of BASIC.
**Inspired by:** Magazine chase games, Pac-Man, Mr Wimpy, Cookie

Move through a maze collecting items while enemies chase you. Enemies use simple rules to pursue. Multiple levels with different maze layouts.

**Headline concept:** Opponents — simple rules, emergent challenge *(industry term: AI / Opponent Behaviour)*.

**Embedded:** Apparent vs actual intelligence — the player *believes* the enemies are coordinating, flanking, anticipating. They aren't. The game design exploits the player's instinct to project intelligence onto behaviour.

**Design lesson:**
The enemies in Night Patrol follow simple rules: move toward the player, avoid walls. Two rules. But the emergent behaviour — cornering, flanking, blocking escape routes — feels *intelligent*. This is the core insight of game opponents: *complex-looking behaviour from simple rules*. The enemies don't plan or think. They react. The player's brain fills in the rest, attributing intention where there is only algorithm. Understanding this changes how you think about every game with opponents.

**Techniques learned:**
- **SCREEN$ for reading the character at a position** — querying what's at a given screen cell, the alternative to maintaining a separate map array.
- **OVER 1 for XOR drawing** — drawing without destroying what's underneath. The technique that lets enemies pass over collectables without erasing them.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Map data | String arrays as maze layouts |
| Simple opponent rules | Enemies move toward the player |
| Multiple enemies | Arrays for enemy positions |
| `RESTORE` to specific line | Loading a particular level's data |
| `OVER 1` | XOR mode — move without destroying the background |
| `SCREEN$` | Reading the character at a screen position |
| String arrays | `DIM m$(20)` — a list of strings for level data |

**Read alongside:**
- *Pac-Man* (Namco, 1980) — the canonical pursuit opponent.
- *Mr Wimpy* (Ocean, 1984) — Spectrum Pac-Man variant.
- *Cookie* (Ultimate Play The Game) — pursuit AI in the Ultimate canon.

**Modern equivalents:**
Two-rule emergent opponents are what every modern enemy state machine does at minimum — and most modern enemies are still implemented as state machines with a small number of behaviours, not as planners. Mark Brown's GMTK *AI in Games* video covers exactly this lesson, with Pac-Man's ghosts as the worked example.

**Polish discipline:**
Night Patrol's polish is *the chase*. The enemies' move tempo versus the player's, the audio cue when an enemy is in line-of-sight, the moment of capture — every polish moment tunes the *felt* intelligence the simple rules produce.

**Milestone:** The learner understands that simple rules can produce complex-looking behaviour and can build opponents the player believes are intelligent.

---

### Game 12: Stonefall

**Volume:** 3 Worlds and Rules
**Genre:** Single-screen action-puzzle
**Approx. size:** ~16-24 topics, ~24-36 hours. ~150 lines of BASIC across the topic arc.
**Inspired by:** Boulder Dash, Repton, magazine type-in cavern games

Each screen is a hand-laid cavern. Dig through the earth with the cursor keys, collect gems, and reach the exit — but rocks fall when their support is dug out, and a careless dig becomes a cascade. Walls, earth, gems, stones, the player, and the exit are all hand-designed 8×8 pixel graphics that replace the standard character set.

**Headline concept:** Level Design — hand-laid worlds, readable affordances.

**Embedded:** Signposting (a rock about to fall wobbles for one frame before it does — the cavern *tells the player* what's about to happen if they can read it); Risk and reward (which path to dig is a decision: shorter route through dangerous rock, or longer detour through safe earth).

**Design lesson:**
A custom character set transforms the Spectrum from a text machine into a visual world. Every tile is *designed*, not default. The cavern has its own *visual language* — earth looks different from rock, gems look different from walls, the exit looks like an exit — and the player reads the world instinctively. This is *environmental storytelling through graphics*: the visuals communicate the rules without text. Every commercial game creates its own visual identity. This is where the learner creates theirs. And the *placement* of those tiles — which path is short, which is dangerous, what the player can see — is level design as a separable discipline from the visuals themselves.

**Techniques learned:**
- **Custom character set** (`POKE 23606/23607`) — replacing the entire font with hand-designed 8×8 graphics. The single biggest visual-identity move available in BASIC.
- **Cell-by-cell physics tick** — updating the cavern one cell at a time, in a defined order, so cascades are deterministic and readable. (A form of cellular-automaton update; the modern descendant is *Dwarf Fortress*-style world simulation.)
- **Flood-fill traversal** — when a cascade triggers, the propagation through connected unstable rocks is a flood-fill in disguise. The classic computer-science algorithm applied to a game cascade.
- **Direct attribute POKE** (`22528+`) — writing the attribute file directly to flash a cell, indicate a fall path, or paint the cavern's mood. The technique that makes visual feedback feel instantaneous.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Custom character set | POKE 23606/23607 (CHARS) replaces the entire font |
| Character design | Hand-designed 8×8 pixel graphics |
| Tile-based level design | Each cavern is built from a grid of designed tiles |
| Level data in DATA | Hand-laid screens stored as character strings, loaded at runtime |
| Cell-by-cell physics | Stones fall when unsupported; the world updates one tick at a time |
| Flood-fill propagation | Cascade rocks find unstable neighbours recursively |
| Direct attribute POKE (22528+) | Fast colour-only updates without reprinting |

**Read alongside:**
- *Boulder Dash* (Peter Liepa / Chris Gray, 1984) — the genre's origin, with cell-by-cell physics that became the template.
- *Repton* (Tim Tyler / Superior Software, 1985) — the BBC Micro/Spectrum classic, single-screen-cavern lineage.
- The cavern-puzzle type-ins of the period.

**Modern equivalents:**
Tile-based level design is everywhere modern: *Mario Maker*, *Stardew Valley*, *Celeste*, every retro-aesthetic indie. Custom tilesets and hand-laid screens are the foundation of the indie pixel-art tradition. The cell-by-cell deterministic tick is what *Dwarf Fortress*, *RimWorld*, and every cellular-automata-driven sim does at heart. Flood-fill is the algorithm behind every paint-bucket tool ever shipped.

**Polish discipline:**
Stonefall's polish is *the cascade telegraph*. The single-frame wobble before a rock falls, the sound of earth being dug versus rock falling, the moment of crush versus the moment of safe-passage, the rock-trail attribute flash as a cascade propagates — every polish moment tunes the *readability* of the cavern.

**Milestone:** The learner can design a hand-laid visual world from a custom tileset, understands the difference between visual identity (the tiles) and level design (their arrangement), and has met flood-fill and direct attribute POKE as named techniques.

---

## Volume 4: Stories and Systems

The synthesis. Four games where the systems carry meaning: animated characters with weight, paced escalation, generated worlds, narrative ecology. By Volume 4's end, the learner has met every transferable concept of game design and can build games at the limits of what 48K BASIC supports.

---

### Game 13: Rooftops

**Volume:** 4 Stories and Systems
**Genre:** Single-screen platformer (Miner-mechanical)
**Approx. size:** ~16-24 topics, ~24-36 hours. ~200 lines of BASIC.
**Inspired by:** Manic Miner, Jet Set Willy, magazine type-in platformers

The hero leaps between rooftop arenas — each a single hand-designed screen with chimneys, gargoyles, pigeons on patrol, a key, and an exit. Reach the next rooftop or fall. The character has animation frames — legs moving as they run, a different pose mid-jump. Jump physics give weight and momentum.

**Headline concept:** Character — a sprite that feels alive.

**Embedded:** Animation as state communication — the player reads the hero's pose to know what the system is doing. Standing, walking, jumping, falling, dying — each a recognisable pose, each communicating without text.

**Design lesson:**
A character with two animation frames feels more alive than a static sprite with a hundred colours. *Animation communicates state*: legs cycling means running, a different pose means jumping, no animation means standing still. *Weight and momentum* from jump physics make the character feel physical — they have mass, they obey gravity, they arc through the air. Character is the player's avatar in the game world. Making them feel *right* is the difference between a tech demo and a game people want to play. Rooftops sits in the Miner tradition: single-screen rooftop arenas, each its own contained puzzle, in the lineage of Manic Miner and Jet Set Willy.

**Techniques learned:**
- **UDGs** (`USR`, `BIN`) — User-Defined Graphics, the Spectrum's sprite system. Designing a character glyph-by-glyph from binary patterns. (UDGs appear *after* the custom character set in Stonefall — a deliberate choice. Stonefall's tile-only cavern uses CHARS because no text shares the screen; Rooftops needs a character *plus* score and status text, so UDGs are the right tool. Different scopes, different techniques.)
- **Animation via frame cycling** — alternating between UDG definitions to produce motion. The simplest animation technique and still the canonical one.
- **Jump physics** — gravity, momentum, the arc. The maths that makes a jump feel like a jump.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `USR` | Defining user-defined graphic characters |
| `BIN` | Binary notation for pixel rows |
| UDG design | Graph paper → binary → POKE |
| Animation | Cycling between UDG frame definitions |
| Jump physics | Gravity, momentum, arc |
| Platform collision | ATTR/SCREEN$ to check what's beneath the player |

**Read alongside:**
- *Manic Miner* (Matthew Smith / Bug-Byte, 1983) — the single-screen-platformer canon.
- *Jet Set Willy* (Matthew Smith / Software Projects, 1984) — the sequel and the second Miner-mechanical classic.
- *Saboteur* (Durell, 1985) — rooftop chases and platformer character.

**Modern equivalents:**
Sprite animation as state-communication is unchanged from UDGs to Unreal. A character's pose, gait, and weight communicate what the system is doing. Frame-by-frame animation is still how indie pixel-art games (*Celeste*, *Hollow Knight*) achieve their feel. Jump physics formulas have barely changed — the maths of gravity-and-velocity is the same in BASIC and Unity.

**Polish discipline:**
Rooftops' polish is *the weight*. The animation cycle speed versus run speed, the apex pause at the top of the jump, the landing thud, the death animation — every polish moment tunes the felt physicality of the same sprite.

**Milestone:** The learner can design and animate a character that feels alive, and understands that weight and momentum are made of small frame-level choices.

---

### Game 14: Blockstorm

**Volume:** 4 Stories and Systems
**Genre:** Vertically scrolling shooter
**Approx. size:** ~16-24 topics, ~24-36 hours. ~250 lines of BASIC.
**Inspired by:** Magazine type-in shooters, arcade conversions, Cybernoid

A wave-based vertical shooter with custom UDG sprites. Multiple enemy types, escalating difficulty, score and lives. The game gets harder in deliberate, paced waves — not by accident.

**Headline concept:** Pacing — when to push, how much, what to change.

**Embedded:** Resource management — the *one bullet rule* (only one player bullet on screen at a time) is the central constraint. The player rations every shot. Difficulty curve — the wave design is a curve, not a step function.

**Design lesson:**
A shooter that gets harder at random isn't a game; it's noise. Pacing is the design discipline of *escalating in a curve the player can feel*. Blockstorm teaches it as a first-class concept: each wave introduces *one* new variable (faster enemies, then more of them, then enemies that shoot back, then formations) — the player has time to learn each new threat before the next arrives. The one-bullet rule is the resource constraint that gives every shot weight: the player rations, aims, waits. Performance — the BASIC optimisations that make more enemies on screen possible (short variable names, multi-statement lines, integer arithmetic) — is taught here too, but as a *skill in service of pacing*, not as the headline concept. (The bridge to assembly, where commercial-bar performance lives, is a separate journey in the Spectrum Assembly track.)

**Techniques learned:**
- **Wave data in DATA** — encoding enemy waves as data, READ at runtime. Lets the designer tune pacing without touching code.
- **Multi-statement-line speed tricks** — chaining commands with `:` to reduce BASIC's per-line overhead. A canonical period optimisation.
- **IN 31 for Kempston joystick** — reading the Kempston joystick port, the period-appropriate alternative to keyboard input for action games.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CLEAR` | `CLEAR 59999` — set RAMTOP to protect UDG / graphics data |
| `IN` 31 (Kempston joystick) | Arcade-feel input |
| `INPUT LINE` | Read a full line without quotes |
| Speed optimisation | Short variable names, GO SUB placement, integer tricks |

**Read alongside:**
- *Cybernoid* (Costa Panayi / Hewson, 1988) — the canonical Spectrum vertical shooter, with the legendary difficulty curve.
- *R-Type* (Irem, 1987) — arcade pacing.
- Magazine shooter type-ins of the late 1980s.

**Modern equivalents:**
Pacing is the single most-discussed transferable design concept of the last decade. Mark Brown's GMTK has run videos on it three times. *Roguelike difficulty curves*, *Vampire Survivors*-style wave escalation, *Hades*' Heat system — all the same craft, named, discussed, iterated on by every modern designer.

**Polish discipline:**
Blockstorm's polish is *the wave*. The audio cue announcing each new wave, the brief pause before it starts, the visual difference between enemy types, the death animation of each — every polish moment tunes the *felt* difficulty curve.

**Milestone:** The learner can design a paced experience that escalates in a curve the player can feel, and understands resource constraints as a design tool.

---

### Game 15: Dungeons of Dorin

**Volume:** 4 Stories and Systems
**Genre:** Dungeon crawl RPG
**Approx. size:** ~20-28 topics, ~30-42 hours. ~300 lines of BASIC.
**Inspired by:** Rogue, early CRPGs, Fighting Fantasy

A dungeon crawler with character stats, combat, equipment, and procedural level generation. Simple generation creates a different dungeon each time.

**Headline concept:** Generated Worlds — the computer as co-creator *(industry term: Procedural Generation)*.

**Embedded:** Replayability — the same code produces a different game each session. Risk and reward — descend to a deeper level for better treasure but harder monsters; the player decides when to push their luck.

**Design lesson:**
The wonder moment: something appears on screen that *the learner didn't design*. The code generated it. Generated worlds mean infinite content from finite rules. Every playthrough is different — not because of random chance alone, but because of *systems that create*. This is the principle behind roguelikes, *Minecraft*, and every game that promises "no two plays the same." The learner discovers that code can be *creative* — it can surprise even its author. And the *risk/reward* decision the player faces each floor (push deeper for better loot, or retreat to safer ground) is what makes generated content feel *meaningful* rather than just varied.

**Techniques learned:**
- **DEF FN / FN** — user-defined functions in BASIC. The damage formula, the rarity curve, the distance calculation all become named functions.
- **OUT 254 for screen shake** — writing to the border port to produce rapid colour flicker. A demoscene-grade Spectrum effect achieved with one OUT instruction.
- **SAVE / LOAD / VERIFY** — saving the game state to tape, the period-accurate persistence mechanism.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `DEF FN` / `FN` | User-defined functions — damage formulas, distance calculations |
| `LN` / `EXP` | Logarithmic and exponential functions — rarity curves |
| `SAVE` / `LOAD` / `VERIFY` | Saving game state to tape |
| `OUT` 254 (border port) | Screen shake via rapid border changes |
| `VAL$` | Evaluating a string as an expression |

**Read alongside:**
- *Rogue* (Toy / Wichman / Arnold, 1980) — the genre's origin.
- *Lords of Midnight* (Mike Singleton / Beyond, 1984) — procedural landscape rendering on Spectrum.
- *Sword & Sorcery* (PSS, 1985) — Spectrum dungeon-crawler in the period.
- *Fighting Fantasy* gamebooks — the offline ancestors of dungeon-crawl design.

**Modern equivalents:**
Generated worlds are everywhere modern: *Minecraft*, *Spelunky*, *Hades*, *No Man's Sky*, *Dwarf Fortress*. The seed-based RNG you learn here is the basis. The risk/reward push-your-luck loop is the spine of every modern roguelike — *Slay the Spire*, *Hades*, *Vampire Survivors*.

**Polish discipline:**
Dungeons of Dorin's polish is *the descent*. The stair-down moment, the new-floor reveal, the danger ramp's visible signal, the death scene — every polish moment tunes the *felt* push-your-luck the procedural ruleset creates.

**Milestone:** The learner can build a game where the computer co-creates content and understands that generated systems work because they make every play *different*, not just *random*.

---

### Game 16: Thornwood Manor

**Volume:** 4 Stories and Systems
**Genre:** Parser adventure (text adventure)
**Approx. size:** ~20-30 topics, ~30-45 hours. ~350 lines of BASIC.
**Inspired by:** The Hobbit (Melbourne House, 1982), Mystery of Silver Mountain (Usborne, 1984), Level 9 adventures

The learner's magnum opus and the curriculum's text-tradition closing argument. The player explores Thornwood Manor by typing commands — GO NORTH, EXAMINE PORTRAIT, ASK BUTLER ABOUT KEY, GIVE LOCKET TO GHOST. Rooms have descriptions. Items can be picked up, dropped, used. Characters speak, remember, react. A story unfolds through the player's verbs.

**Headline concept:** Living Worlds — scripted reactivity, narrative ecology.

**Embedded:** Player Agency — the verbs *are* the choices. What the player tries is the game's responsiveness, made concrete. Failure recovery — SAVE and LOAD make mistakes survivable; the design encourages exploration over caution.

**Design lesson:**
The manor doesn't run on its own. NPCs don't move between rooms on schedules; the world is not real-time simulation. Instead, the manor *reacts* — every action the player tries, the game responds to in character. The butler greets the player, then later remembers having greeted them. The ghost answers different questions in different ways. The locked door reveals itself when the player asks about it. This is *narrative ecology*: a world that feels alive because every part of it has been authored to *respond*, not because every part is independently animate. It is The Hobbit's actual achievement — scripted reactivity at scale — which gave Spectrum players the feeling of being inside a story even though the underlying code was a parser plus a table of conditions. *Player agency* is what the player feels: every verb is a choice, every choice is meaningful. *Failure recovery* — the SAVE/LOAD discipline — lets the player experiment without fear.

**Techniques learned:**
- **Verb-noun parser** — splitting an input string into a verb and a noun (and prepositions and objects), then dispatching to a handler. The single most distinctive technique of the parser-adventure tradition.
- **Room data structures** — each room as a record of description, exits, contents, and state flags. The world as data.
- **World-state flags** — boolean (or small-integer) flags that track what the player has done, seen, said. The mechanism by which the manor *remembers*.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| String parsing | Splitting input into verb and noun |
| Dispatch tables | Verb → subroutine via line numbers |
| Synonyms | "GET" = "TAKE" = "PICK UP" |
| Pronouns and context | "EXAMINE IT" |
| Room data in DATA | Description, exits, contents per room |
| State flags | Boolean variables tracking what has happened |
| `SAVE` / `LOAD` for games | The player's save game vs the program |

**Read alongside:**
- *The Hobbit* (Veronika Megler / Philip Mitchell / Melbourne House, 1982) — the canonical parser adventure on Spectrum, with the legendary "you wait for a while" emergent-feel. Read about the Inglish parser language Melbourne House invented for it.
- *Mystery of Silver Mountain* (Les Howarth / Usborne, 1984) — a complete parser-adventure type-in book, the closest direct ancestor of this game.
- Level 9 adventures (*Snowball*, *Return to Eden*, *Worm in Paradise*) — the literate British text-adventure tradition.

**Modern equivalents:**
Verb-noun parsers are NOT obsolete. Inform 7 is the modern descendant; interactive fiction is a thriving small genre. More broadly, *scripted reactivity* — the discipline of authoring response to every action the player might try — is alive in every modern adventure game (*Disco Elysium*, *Pentiment*, *Citizen Sleeper*). The state-flag world-model is the foundation of every dialogue tree, every relationship system, every quest log in modern RPGs.

**Polish discipline:**
Thornwood Manor's polish is *the response*. The prose voice of each room description, the cadence of an NPC's reply, the way the parser handles a misunderstood verb ("I don't know how to PERAMBULATE"), the small acknowledgement when the player tries something the author thought of — every polish moment tunes the *felt* aliveness of the same underlying state machine.

**Milestone:** The learner has built a world that responds, met every transferable concept of game design across 16 games, and is ready to cross over into the Spectrum Assembly track to learn how the legends built games at commercial bar.

---

## Concept progression summary

### Design concepts — by game, when first introduced as headline:

| Concept (player-facing) | Industry term | First game | Reinforced in |
|---------|------|------------|---------------|
| Response | — | 1 | Every game |
| Tension | — | 2 | 9, 14 |
| Pattern | — | 3 | 7, 15 |
| Real-Time Reactivity | Game Loop | 4 | 9, 10, 11, 14 |
| Data-Driven | Content vs Logic | 5 | 11, 15, 16 |
| Progression | — | 6 | 14, 15, 16 |
| Deduction | — | 7 | 8, 15 |
| The Rule IS the Game | Mechanics as Meaning | 8 | (concept stands alone) |
| The Game Won't Wait | Continuous Motion | 9 | 10, 11, 13, 14 |
| Physics | — | 10 | 13 |
| Opponents | AI / Opponent Behaviour | 11 | 16 |
| Level Design | — | 12 | 13, 16 |
| Character | — | 13 | 16 |
| Pacing | — | 14 | 15 |
| Generated Worlds | Procedural Generation | 15 | 16 |
| Living Worlds | — | 16 | (concept stands alone) |

### Embedded concepts — where they appear:

| Embedded concept | Games |
|------------------|-------|
| Juice | 1 |
| Telegraphing | 2, 12 |
| Signposting | 3, 12 |
| Ambient feedback | 4 |
| Difficulty curve | 5, 14 |
| Ratings as social proof | 6 |
| Information layering | 7 |
| Constraint as gameplay | 8 |
| Failure as content | 9 |
| Risk and reward | 10, 12, 15 |
| Apparent vs actual intelligence | 11 |
| Animation as state communication | 13 |
| Resource management | 14 |
| Replayability | 15 |
| Player agency | 16 |
| Failure recovery | 16 |

### Sinclair BASIC concepts — by game, when first introduced:

| Concept group | First game | Reinforced in |
|---------------|-----------|---------------|
| **Language fundamentals** | | |
| PRINT, LET, variables, INPUT, IF/THEN, GO TO, REM | 1 | Every game |
| RND, INT, RANDOMIZE | 1 | 4, 9, 15 |
| LIST, NEW, RUN, STOP, CONTINUE | 1 | — (editor/debug) |
| CLS, PRINT AT, INKEY$, PAUSE, BEEP | 2 | 4, 9, 11, 14 |
| PLOT, DRAW (pixel graphics) | 2 | 3, 4, 10, 13 |
| PEEK 23672 (frame counter) | 2 | 9, 14 |
| FOR/NEXT/STEP, colour model (INK/PAPER/BORDER/BRIGHT) | 3 | 4, 9, 10, 12 |
| Position variables, the game loop, ABS, SQR, ^ | 4 | 9, 10, 15 |
| Strings, DATA/READ, LEN, slicing, STR$, VAL | 5 | 6, 11, 16 |
| GO SUB/RETURN, arrays, RESTORE, AND/OR/NOT, TAB | 6 | 7, 9, 11, 14 |
| **Logic and grids** | | |
| 1D arrays, comparison logic | 7 | 9, 13 |
| `ATTR` (reading the screen as data) | 8 | 12, 13 |
| 2D level grids, multi-line DATA | 8 | 12, 16 |
| **Real-time and hardware access** | | |
| Attribute-file POKE (22528+), SGN, FLASH | 9 | 12, 14 |
| CHR$ 128-143 (block graphic characters), CHR$/CODE | 10 | 13 |
| CIRCLE, POINT (advanced pixel graphics) | 10 | 13 |
| SIN, COS, TAN, ATN, ASN, ACS, PI (trigonometry) | 10 | 15 |
| OVER 1 (XOR drawing), SCREEN$ | 11 | — |
| Custom character sets (POKE CHARS 23606/23607) | 12 | — |
| Cell-by-cell physics ticks | 12 | — |
| Flood-fill traversal | 12 | — |
| Direct attribute POKE (22528+) | 12 | — |
| **Direct control** | | |
| UDGs (USR, BIN), animation | 13 | — |
| CLEAR, INPUT LINE, IN 31 (Kempston joystick) | 14 | — |
| **Systems and persistence** | | |
| DEF FN/FN, LN, EXP, VAL$ | 15 | — |
| OUT 254 (border port) | 15 | — |
| SAVE/LOAD/VERIFY | 15 | 16 |
| String parsing, dispatch tables, world-state flags | 16 | — |

---

## Excluded Sinclair BASIC keywords

The following keywords are not taught (peripheral-specific, no stock 48K use): COPY, LPRINT, LLIST, MERGE, OPEN #, CLOSE #, FORMAT, CAT, ERASE, MOVE. Every other keyword has a game assignment.

Machine code (POKEing Z80 bytes via DATA and `RANDOMIZE USR`) is **not taught in the BASIC track**. The Spectrum Assembly track teaches Z80, the techniques the legends used (raster effects, sprite multiplexing, smooth scrolling, loaders), and commercial-bar craft. The two tracks form one Spectrum curriculum; this is the on-ramp.

---

## Dependencies

The curriculum's *Read alongside* threading depends on vault completeness. Every game's section points at 2-3 vault entries the learner studies alongside their build. **The vault audit is a prerequisite for the spec's launch ship**, not a parallel artefact: a learner clicking through to a stub vault entry breaks the legends-thread promise. Vault gap-fill must happen before or alongside Volume 1's content writing.

Specific high-priority vault entries required for Volume 1 ship:
- Magazine type-in tradition (Crash, Your Sinclair, Sinclair Programs)
- *Computer Spacegames* and *Practise Your BASIC* (Usborne)
- *Lunar Lander* — the DEC original and home-computer descendants
- *Daley Thompson's Decathlon* (Ocean, 1984) — reaction-test heritage
- *Simon* (Milton Bradley, 1978) — toy origin

Volume 2-4 vault entries are scoped per game in their respective sections.

---

## Changelog

- **v6.5 DRAFT (2026-05-25):** **Banner → Story Builder (slot 1).** Banner (a text display program) replaced by Story Builder (a Mad Libs-style fill-in-the-blanks program). Reason: Banner's "Output" concept — PRINT text to screen — doesn't sustain 3+ topics as a standalone game; it's a hello-world, not an interactive program. Story Builder teaches the same concept (Output) but adds INPUT for interactivity and string concatenation for a payoff — the learner's words assembled into a ridiculous story. The program is shareable (show someone the output), gradual (4 topics), and sets up Lucky Number by introducing PRINT and INPUT before Lucky Number adds LET, IF/THEN, and GO TO. **All 8 V1 briefs written** (see `games/{slug}/brief.md` per game). All follow the `specifications/brief-basic-v1.md` lightweight template. **Previous V1 content killed:** Lucky Number, Bright Spark, and Quiz Master MDX units (written under the pre-v6.2 type-in-first pedagogy) deleted; Wire Panic, Hot and Cold, Letter Soup, Minefield (replaced in v6.2 canon-first audit) deleted; Ink War (Spectrum assembly, not fun) and Signal (Amiga assembly) also deleted. **48 topics total across V1** (Story Builder 4, Lucky Number 9, Oracle Stone 5, Reflex 6, Dice Roller 5, Bright Spark 6, Hi-Lo 5, Touchdown 8). BASIC keyword progression refined: PRINT/INPUT arrive in Story Builder (slot 1); LET/IF/GO TO/RND in Lucky Number (slot 2); INKEY$/PLOT/DRAW in Reflex (slot 4); FOR/NEXT in Dice Roller (slot 5); BRIGHT/string-as-sequence in Bright Spark (slot 6). Headline + embedded concept tables updated for slot 1 rename.
- **v6.4 DRAFT (2026-05-19):** Rename pass applying the [inspired-by-not-clones naming convention](../../../../decisions/inspired-by-not-clones-naming.md) (decided same day, from the Spectrum Assembly v0.2/v0.3 brainstorm). **Eleven game renames (Cut A applied — all canonical/trademark/generic-mechanic names, not just active trademarks):** Magic 8-Ball → **Oracle Stone** (slot 3); Hangman → **Cipher** (slot 9); Mastermind → **Locksmith** (slot 11); Battleship → **Sonar** (slot 12); Tic-Tac-Toe → **Three in a Row** (slot 13); Hunt the Wumpus → **The Caverns** (slot 14); Hammurabi → **Yearfall** (slot 15); Pong → **Volley** (slot 18); Asteroids → **Drift** (slot 20); Frogger → **Quickstep** (slot 21); Pac-Man → **The Hungry Maze** (slot 22). All v6.3 structural decisions (32 games, 4 volumes, design concept progression, embedded concepts, BASIC progression shifts, V4 2-deep tour-then-deepen ordering) carry forward unchanged. **Touchdown (slot 8) is NOT renamed** — its dual-name is "Touchdown (Descent — Game Loop)", with the game name staying Touchdown (a generic word, not a trademark) and "Descent" being the player-facing concept name introduced in v6.3. Volume 1 ships at v6.4 names for October 2026 (Banner, Lucky Number, **Oracle Stone**, Reflex, Dice Roller, Bright Spark, Hi-Lo, Touchdown). Existing built V1 games (Lucky Number, Bright Spark) are unchanged. **Pending v6.4 work:** Update headline table (slots 3, 9, 11-15, 18, 20-22) and per-game spec sections (when written) to use v6.4 names. Update [`docs/tracker/revamp.md`](../../../../tracker/revamp.md) tracker. `spectrum-basic-games-progress` memory entry needs update for v6.4 renames. Names are first-draft and may want refinement after living with them.
- **v6.3 DRAFT (2026-05-19):** Structural revision after a three-pass concept-progression brainstorm (design concepts → BASIC programming progression → embedded concepts). The brainstorm started as a sanity check on v6.2 flow and surfaced four concerns: (1) Game Loop taught twice with confusingly similar player-facing names (Touchdown's "Real-Time Reactivity" and Tail Chase's "The Game Won't Wait"); (2) Pacing as a V4 headline at Blockstorm — Pacing is normally embedded, and Blockstorm was a real-time wave shooter stranded among V4's story-system games; (3) Stonefall too engineering-heavy for V3 — Boulder Dash-tradition is V4-sized; (4) Dorin → Thornwood V4 capstone leap (procgen → parser is genre-massive). **Five headline renames:** Touchdown "Real-Time Reactivity" → **"Descent (Game Loop)"**; Blockstorm "Pacing" → **"Escalation (Difficulty Curves)"**; Stonefall "Level Design" → **"Designed Worlds (Level Design)"**; Night Patrol "Opponents" → **"Defence (Multi-Target)"** (Pac-Man now owns Chase AI in V3); Hunt the Wumpus "Hidden Information" → **"Atmosphere (Hidden Information)"** (matching dual-name pattern). **Stonefall/Blockstorm swap:** Blockstorm moves V4→V3 (now V3 capstone); Stonefall moves V3→V4. V3 becomes the real-time arcade arc; V4 becomes the storytelling arc unburdened by a real-time shooter. **32-game restructure:** The trig pile at Brick Bash flagged that the curriculum was missing a genuine trig-using game. Adding Asteroids broke the 4-per-volume lattice. Rather than cut a game (every game post-canon-first audit is canonical) or accept a broken lattice, the curriculum expanded to **8 games per volume = 32 total** — powers-of-2 hold per-volume and total. Honest to the Usborne tradition: *Computer Spacegames* and *Practise Your BASIC* were *many tiny programs*, not 4 medium ones. **V1 grows by 4:** Banner (Output), Magic 8-Ball (Chance), Dice Roller (Accumulation), Hi-Lo (Narrowing) — all small canonical Usborne-tradition programs. **V2 grows by 4:** Battleship (Search), Tic-Tac-Toe (Adversary), Hunt the Wumpus (Atmosphere), Hammurabi (Consequences) — all period-canonical turn-based games. **V3 grows by 4:** Pong (Volley), Asteroids (Momentum) — the trig-canonical game, Frogger (Timing), Pac-Man (Pursuit). **V4 grows by splits:** Rooftops, Stonefall, Dorin, Thornwood each split into Pt 1 and Pt 2 — naming follow-up scheduled (Pt 2 games may earn distinct titles). **V4 ordering: 2-deep tour-then-deepen** — introduce two storytelling forms (Rooftops 1, Stonefall 1), deepen both (Rooftops 2, Stonefall 2), then introduce two more (Dorin 1, Thornwood 1) and deepen both (Dorin 2, Thornwood 2). Volume midpoint at slot 28/29 marks the shift from graphical traditions to narrative traditions. **BASIC progression shifts:** UDGs introduce at Blockstorm (slot 24), not Rooftops — Rooftops Pt 1 deepens with animation. Trig (SIN/COS/PI) moves from Brick Bash to Asteroids (slot 20); TAN/ASN/ACS cut as excluded keywords (no genuine BASIC-game use). FOR/NEXT/STEP introduces at Dice Roller (slot 5), not Bright Spark — Dice Roller's `FOR I = 1 TO 5: LET D = INT(RND*6)+1: NEXT I` is the textbook FOR/NEXT intro. 2D arrays introduce at Battleship (slot 12), not Crates. SAVE/LOAD/VERIFY introduces at Dorin Pt 2 (slot 31), available to Thornwood Pt 2. DATA/READ stays at Hangman (slot 9); Magic 8-Ball (slot 3) uses chained IF and earns its place as a *pattern slot* not a keyword slot — same for Hi-Lo (loop-until-condition pattern). Array overlap ambiguity from v6.2 resolved: string arrays at Quiz Master (slot 10), numeric arrays at Mastermind (slot 11), 2D arrays at Battleship (slot 12). **Embedded concepts grow from 15 to 20:** five new — Anticipation (slots 3, 5, 20, 21), Atmosphere (slots 14, 32 — also Wumpus headline), Trade-offs / delayed consequences (slots 15, 30, 32), Authored experience (slot 28), Emergent stories (slots 29, 31, 32). **Launch impact:** V1 ship doubles from 4 → 8 games for October 2026 — 6 new V1 games to write (vs 2 planned under v6.2), all small (3-6 topics each). Volume 1 launch still achievable in 5 months given game smallness. Post-October curriculum doubles to 32 games, ship through ~2028-29. **Carries forward unchanged from v6.2:** North Star, canon-first audit, dual-name concept pattern, gradual pedagogy, headline-plus-embedded structure, techniques as first-class axis, read-alongside, modern equivalents, polish woven through, BASIC track clean of assembly. **Pending v6.3 work:** 16 new game spec sections still to write (V1: 4 small games; V2: 4 turn-based games; V3: 3 real-time games incl. Asteroids; V4: 4 splits). V4 Pt 2 naming (Rooftops Pt 2, Stonefall Pt 2, Dorin Pt 2, Thornwood Pt 2 may earn distinct names). `docs/tracker/revamp.md` update for v6.3 lineup. Vault audit (prerequisite) scope grows.
- **v6.2 DRAFT (2026-05-18):** Major architectural revision after the canon-first audit, a critical challenge pass, a pedagogy-anchor pass, and a pedagogy-shift pass. The type-it-then-take-apart move (typing a complete 170-line listing in topic 1, then dissecting it across topics 2-9) was abandoned after honest review surfaced it as a romantic homage to a tradition the Usborne books didn't actually follow — and a pedagogical model that costs 90+ minutes of friction before the learner understands anything. Replaced with **fully gradual introduction**: every game starts with the smallest possible working program and adds one concept per topic, producing a working result at every step. Polish weaves through (small *which felt better?* beats at each topic) rather than concentrating at the end. Lucky Number's topic list rewritten as the v6.2 pedagogy exemplar under this gradual shape: topic 1 is `PRINT "Hello"`; topic 9 is the learner's polished game. Spec framing updated throughout: PLOT/DRAW now properly arrive in Game 2 (Reflex), not Game 1; "Graphics from day one" renamed "Pixel graphics from early on"; Volume 1 intro reflects the gradual approach; magazine type-in tradition referenced as historical context, not as pedagogy. Spec opening rewritten to honestly acknowledge that most legendary Spectrum games were written in assembly, not BASIC — the BASIC track teaches the *concepts* the legends used (in vehicles drawn from the broader 80s computing tradition), while the Assembly track teaches the commercial-bar *techniques* the legends actually shipped. Game 4 (was Hot and Cold, constructed) replaced with **Touchdown** — Lunar Lander-alike — completing the canon-first audit so no game in the lineup is constructed-for-curriculum. Rough size estimates added per game and per volume (~190-275 topics total, ~280-460 hours). Vault audit named as a prerequisite dependency for the spec's launch ship. Unit counts replaced with named topics (variable per game). 4 volumes of 4 games introduced (First Programs / Patterns of State / Worlds and Rules / Stories and Systems), each volume with its own thematic identity: V1 = programs that respond (on-ramp), V2 = programs that think (turn-based logic), V3 = programs that act (real-time worlds), V4 = programs that tell stories (synthesis). Four game replacements after canon-first audit: Wire Panic → Reflex (more period-authentic reaction tester), Letter Soup → Hangman (more canonical), Minefield → Mastermind (more canonical, older toy lineage), Ink Spill → Crates (Sokoban-alike, deeply period). Concept names redone with dual-name pattern (player-facing headline + industry subtitle where they differ): Response (was Feedback), Real-Time Reactivity (industry: Game Loop), Data-Driven (industry: Content vs Logic), The Game Won't Wait (industry: Continuous Motion), Deduction (was Information Design), Opponents (industry: AI / Opponent Behaviour), Level Design (was Visual Identity), The Rule IS the Game (industry: Mechanics as Meaning), Pacing (was Pacing and Escalation), Generated Worlds (industry: Procedural Generation), Living Worlds (reframed as narrative ecology). Headline + embedded concepts pattern surfaces 16 concepts at the headline level plus 15+ more as embedded. Techniques surfaced as a first-class axis per game. Read-alongside (legends thread) and Modern equivalents added per game. Polish discipline named as woven-through rather than end-of-game ceremony. Machine code removed from the BASIC track (moved to the Assembly track). Technique reshuffles: ATTR moved from Minefield to Crates; flood-fill and direct attribute POKE moved from Ink Spill to Stonefall. Volume contents reshuffled to clean per-volume identity: Tail Chase moved from V2 to V3 (real-time games together); Crates moved from V3 to V2 (turn-based games together). Game numbers shifted accordingly: Mastermind 8→7, Crates 12→8, Tail Chase 7→9, Brick Bash 9→10, Night Patrol 10→11, Stonefall 11→12. North Star — comprehensive vintage games-development education, drawn from canon where possible — made explicit.
- **v6.1 DRAFT (2026-05-18):** Game 6 design concept reframed from "Structure" to "Progression". Game 11 changed from Tarmac (top-down scrolling racer) to Stonefall (Boulder Dash-alike).
- **v6.0 DRAFT (2026-03-18):** Dual-track curriculum: game design concepts as first-class organising principle alongside BASIC implementation. Each game now teaches a universal game design concept (feedback, tension, pattern, physics, AI, etc.) that transfers to any platform. PLOT/DRAW moved to Game 1 (black box) / Game 2 (formally taught), replacing character-cell block-pixel approach. CIRCLE/POINT/trig remain at Game 9. Game design progression table added. Overview rewritten: the curriculum teaches game design through the medium of Sinclair BASIC, not the other way around.
- **v5.3 DRAFT (2026-03-18):** Complete keyword coverage. Every teachable Sinclair BASIC keyword assigned to a game.
- **v5.2 DRAFT (2026-03-18):** Aligned game names with visual progression document.
- **v5.1 DRAFT (2026-03-16):** Visual progression alignment.
- **v5.0 DRAFT (2026-03-13):** Complete restructure. 16 games, graduated difficulty.
- **v4.0 (2026-03-09):** 4 games × 64 units.
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
