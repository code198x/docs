# Game 01: The Cursed Manor

**Track:** Spectrum BASIC
**Genre:** Text Adventure
**Units:** 64 (4 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~500
**Save/load:** No — completable in one sitting once puzzles are known

---

## Premise

You arrive at Thornbury Manor for Lady Ashworth's autumn gathering. The invitation was unexpected — you've never met her — but curiosity won. The front door swings open at your touch. Inside, the hall is lit, drinks are poured, a fire crackles. But every guest stands frozen mid-gesture: a man reaching for a glass, a woman mid-laugh, a butler carrying a tray. None of them move. None of them breathe.

The front door has locked behind you.

The manor is yours to explore. Somewhere in its rooms is the answer to what happened — and the means to undo it. Find the source of the curse, break it, and escape.

---

## The Manor

### Scale

35-40 rooms across five areas:

- **Ground floor** (~12 rooms): Entrance hall, drawing room, dining room, kitchen, pantry, library, conservatory, billiard room, study, servants' corridor, wine cellar stairs, garden door
- **Upper floor** (~8 rooms): Grand staircase landing, master bedroom, guest bedrooms (3), bathroom, linen closet, locked tower stairs
- **Cellar** (~5 rooms): Wine cellar, cold store, coal cellar, old passage, sealed chamber
- **Tower** (~4 rooms): Spiral staircase, observatory, Lady Ashworth's private study, rooftop
- **Grounds** (~5 rooms): Front drive, walled garden, greenhouse, stable yard, family chapel

### Room Design Principles

Each room has:
- A **description** (2-4 lines of atmospheric text)
- **Exits** (compass directions + UP/DOWN where appropriate)
- **Fixed scenery** that can be EXAMINEd (furniture, paintings, windows)
- **Frozen guests** in some rooms (EXAMINEable, each holding a clue)
- **Items** in some rooms (takeable objects)

Rooms should feel distinct. The library smells of leather and pipe smoke. The kitchen has a half-prepared meal going cold. The conservatory's glass panels show a moonlit garden. Each room tells a micro-story about the moment the curse struck.

### Frozen Guests

8-10 frozen guests throughout the manor, each frozen mid-action:

| Guest | Location | Frozen pose | Clue |
|-------|----------|-------------|------|
| Colonel Barwick | Billiard room | Leaning over a shot | Chalk mark on the green baize spells a word |
| Mrs Pembury | Drawing room | Reaching for a sherry glass | Her brooch is unusual — an eye motif |
| Dr Harlan | Library | Book open in hand | The open page describes a binding ritual |
| Ivy (maid) | Kitchen | Pouring from a kettle | Steam frozen mid-air; her apron pocket holds a note |
| Mr Oakes | Dining room | Carving knife raised over a roast | Place cards on the table spell something when read in order |
| Miss Calder | Conservatory | Tending orchids | One orchid has a silver key wired to its stem |
| Rev. Whitmore | Entrance hall | Mid-stride toward the door | His bible is open to a marked passage |
| Lady Ashworth | Tower study | Hands on an open grimoire | Only reachable late; the grimoire IS the curse |

EXAMINEing guests reveals their pose and the clue. Some clues are immediately useful; others make sense only in combination.

### Map Structure

The manor is mostly open — the player can explore freely from the start. Gated areas:
- **Upper floor**: accessible from entrance hall (grand staircase)
- **Cellar**: accessible from kitchen (stairs down)
- **Tower**: locked door on the upper floor — requires the silver key (from conservatory orchid)
- **Sealed chamber** (cellar): requires solving a combination puzzle
- **Rooftop**: accessible from observatory (trapdoor, requires rope)

The progression is: explore freely → find the silver key → reach the tower → discover the grimoire → gather the components to break the curse → perform the ritual → escape.

---

## Puzzles

### Puzzle Flow

```
Explore ground floor and upper floor freely
  → Find silver key (conservatory orchid, visible on EXAMINE)
  → Unlock tower door
  → Reach Lady Ashworth's study
  → EXAMINE grimoire: describes the binding ritual and how to reverse it
  → Reversal requires three components:
      1. The Eye of Thornbury (an amulet — in the sealed chamber)
      2. A candle lit with "cold fire" (blue candle + tinderbox)
      3. The true name of the curse-caster (assembled from guest clues)
  → Sealed chamber combination: from place cards in dining room
  → Blue candle: found in the chapel
  → Tinderbox: found in the study desk
  → True name: assembled from clues across multiple frozen guests
  → Return to tower study with all three components
  → USE AMULET, LIGHT CANDLE, SAY NAME
  → Curse breaks, guests unfreeze, front door unlocks
  → Walk out the front door to win
```

### Puzzle Details

**The Silver Key** (easy, early): EXAMINE the orchids in the conservatory. "One orchid has a silver key wired to its stem." GET KEY. USE KEY ON DOOR (upper floor tower door).

**The Sealed Chamber** (medium): The dining room place cards, read in seat order, spell a four-digit combination. EXAMINE CARDS in the dining room reveals the numbers. GO to the sealed chamber in the cellar and ENTER CODE (or USE CARDS or similar).

**The True Name** (hard, multi-step): Each frozen guest holds a fragment of the name. Colonel Barwick's chalk marks, Ivy's note, Dr Harlan's book, the Reverend's bible passage — each reveals a syllable or letter. The player must EXAMINE multiple guests, note the fragments, and assemble them. The game doesn't assemble the name automatically — the player must SAY [NAME] with the correct word.

**Cold Fire** (medium): The blue candle from the chapel must be lit with the tinderbox from the study. LIGHT CANDLE or USE TINDERBOX ON CANDLE. The candle burns with a blue flame — "cold fire" as described in the grimoire.

**The Amulet** (medium): Inside the sealed chamber. Once the combination is entered, the chamber opens and the amulet can be taken.

### Red Herrings

A few items and details exist purely for atmosphere and misdirection:
- A grandfather clock stopped at 11:47 (the moment of the curse — atmospheric, not a puzzle)
- A cat (the only living thing besides the player — wanders between rooms, purely decorative)
- Wine bottles in the cellar (EXAMINEable, flavour text only)
- A portrait of Lady Ashworth in the entrance hall (foreshadowing, not a puzzle)

---

## Parser Design

### Command Structure

The parser accepts:
- **VERB** alone: LOOK, INVENTORY, HELP, QUIT, SCORE
- **VERB NOUN**: GET KEY, EXAMINE GUEST, OPEN DOOR
- **VERB NOUN NOUN**: USE KEY ON DOOR, PUT CANDLE IN HOLDER (stretch goal — implement if line budget allows)
- **Direction shortcuts**: N, S, E, W, U, D (expand to GO NORTH etc.)

### Verb Table

| Verb | Synonyms | Action |
|------|----------|--------|
| GO | WALK, MOVE | Move in a direction |
| GET | TAKE, GRAB, PICK | Pick up an item |
| DROP | PUT, LEAVE | Drop an item |
| EXAMINE | LOOK AT, CHECK, INSPECT, X | Describe an item, guest, or scenery |
| USE | | Use an item (context-dependent) |
| OPEN | UNLOCK | Open a door or container |
| LIGHT | | Light the candle |
| SAY | SPEAK | Say a word (for the true name puzzle) |
| LOOK | L | Redisplay room description |
| INVENTORY | I | Show carried items |
| HELP | | Show available commands |
| QUIT | Q | End the game |
| SCORE | | Show current score |

### Parser Implementation

The parser is ~60-80 lines:
1. INPUT the command string
2. Split on first space → verb$ and noun$ (and optionally second noun after ON/IN/WITH)
3. Match verb$ against synonym table (DATA/READ loop or IF chain)
4. Dispatch to appropriate GOSUB handler
5. Handler checks noun$ against current room contents, inventory, and scenery

Unrecognised verbs: "I don't understand that."
Recognised verb, invalid noun: "I can't see that here."
Valid combination with no effect: "Nothing happens."

### Synonyms via DATA

```basic
1000 DATA "GET","GET","TAKE","GET","GRAB","GET"
1010 DATA "LOOK","LOOK","L","LOOK"
1020 DATA "EXAMINE","EXAMINE","X","EXAMINE","CHECK","EXAMINE","INSPECT","EXAMINE"
```

READ through the pairs; if input matches the first element, replace with the second.

---

## Atmosphere

### Colour

- **Default text**: white INK on black PAPER (dark, atmospheric)
- **Room descriptions**: cyan INK (distinct from commands and responses)
- **Item/clue reveals**: yellow INK (draws attention)
- **Scary moments**: red INK + BEEP (finding the grimoire, the sealed chamber opening)
- **Victory**: green INK, BRIGHT 1

### Sound

- **Door opening**: low BEEP (short, resonant)
- **Picking up items**: rising two-note BEEP
- **Wrong command**: flat buzz BEEP
- **Finding a clue**: three ascending notes
- **Entering the tower**: descending ominous tone
- **Breaking the curse**: ascending scale, triumphant
- **The cat**: occasional soft BEEP when it appears in a room

### Text Effects

- **FLASH 1** on the grimoire text when first examined
- **INVERSE 1** for the frozen guests' descriptions (they stand out from the room)
- **PAUSE** for dramatic timing (the sealed chamber door grinds open... PAUSE 50... revealing darkness beyond)

---

## Score System

Points awarded for progress. Maximum score: 100.

| Action | Points |
|--------|--------|
| Exploring a new room (first visit) | 1 each (35-40 total) |
| Examining a frozen guest | 2 each (16-20 total) |
| Finding the silver key | 5 |
| Reaching the tower | 5 |
| Opening the sealed chamber | 5 |
| Finding the amulet | 5 |
| Lighting the candle | 5 |
| Assembling the true name | 10 |
| Breaking the curse | 10 |

Displayed on SCORE command and at game end.

---

## Data Architecture

### Room Data

Each room is stored in DATA statements:

```
Room number, Name$, Description$, N exit, S exit, E exit, W exit, U exit, D exit
```

Exit values: room number (1-40) or 0 (no exit) or -1 (locked, requires key/condition).

### Item Data

```
Item number, Name$, Description$, Start room (0 = not placed yet, -1 = in inventory)
```

### Guest Data

```
Guest number, Name$, Room, Pose$, Clue$, Examined flag
```

### State

- Current room number
- Inventory array (max 8 items)
- Room visited flags (for score and "first visit" descriptions)
- Guest examined flags
- Puzzle state flags (key found, tower unlocked, chamber opened, candle lit, name known, curse broken)

---

## Phase Breakdown

### Phase 1: The Empty Manor (Units 1-16)

The player can move between rooms and read descriptions. No items, no puzzles, no parser beyond movement. The focus is on world-building and core BASIC skills.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Arrival | Title screen with colour and BEEP. "You arrive at Thornbury Manor..." Opening text and prompt. | PRINT, INK, PAPER, BORDER, CLS, BEEP |
| 2 | The Entrance Hall | First room description. Display room name and text. Simple INPUT loop ("Press ENTER to continue"). | Variables, INPUT, strings |
| 3 | North and South | Two rooms connected by GO NORTH / GO SOUTH. Room number variable tracks position. | IF/THEN, LET, simple state |
| 4 | Four Directions | Expand to four exits per room. Direction parsing (N/S/E/W). | String comparison, multiple IF |
| 5 | Room Data | Move room descriptions into DATA statements. READ into variables. | DATA, READ, RESTORE |
| 6 | The Ground Floor | 8 rooms with DATA. Loop reads all rooms at startup into arrays. | DIM, FOR/NEXT, arrays |
| 7 | Room Descriptions | Display multi-line descriptions with colour. Cyan for room text, white for prompt. | INK within PRINT, string formatting |
| 8 | Locked Doors | Some exits are blocked. "The door is locked." Message when exit = -1. | Negative values as flags, conditional messages |
| 9 | The Upper Floor | Add 8 more rooms. Grand staircase connects floors via UP/DOWN. | U/D directions, larger arrays |
| 10 | The Cellar | Add cellar rooms. Kitchen stairs lead down. Dark rooms print "It is dark." | Conditional descriptions, room flags |
| 11 | LOOK Command | LOOK redisplays current room. Separate from movement. Begin two-word parsing. | GOSUB/RETURN, command dispatch |
| 12 | The Grounds | Add outdoor rooms. Different atmosphere text (moonlight, cold air). | Expanding DATA, atmospheric writing |
| 13 | First Visit Text | Rooms show a longer description on first visit, shorter on return. Visited() array. | Boolean arrays, conditional text |
| 14 | The Wandering Cat | A cat appears randomly in rooms. Purely atmospheric. "A grey cat watches you from the shadows." | RND, random events, flavour text |
| 15 | Sound and Mood | Add BEEP to door transitions, room-specific atmosphere (clock ticking, fire crackling). | BEEP with pitch/duration, atmospheric design |
| 16 | The Full Map | All 35-40 rooms in place. Player can walk everywhere except tower (locked) and sealed chamber. Test and polish. | Integration testing, debugging DATA, play testing |

**Milestone:** A complete explorable manor with atmosphere, colour, sound, and a wandering cat. No items or puzzles yet — but it feels like a real place.

### Phase 2: Things and People (Units 17-32)

Items can be picked up and dropped. Frozen guests can be examined. The inventory system and a proper parser take shape.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | The Silver Key | One item in one room. "There is a silver key here." GET KEY picks it up. | Item state variable, simple GET |
| 18 | Carrying Things | Inventory array. GET adds to inventory, item disappears from room. | Array search, insertion |
| 19 | Dropping Things | DROP removes from inventory, places in current room. | Array removal, room state update |
| 20 | Inventory Command | I or INVENTORY lists carried items. "You are carrying: a silver key, a candle." | Array iteration, string building |
| 21 | Item Descriptions | EXAMINE [item] shows a detailed description. Different from room description. | Item lookup, EXAMINE dispatch |
| 22 | More Items | Add all game items (key, candle, tinderbox, amulet, note, grimoire reference). Item DATA statements. | Expanding data structures, DATA for items |
| 23 | Item Limits | Maximum 8 items carried. "You can't carry any more." DROP something first. | Array bounds, user feedback |
| 24 | The Frozen Guests | Guests in rooms. "Colonel Barwick stands frozen, leaning over the billiard table." | Guest data, room contents |
| 25 | Examining Guests | EXAMINE COLONEL (or BARWICK) shows pose and clue text. Yellow INK for clues. | String matching, partial names, INK changes |
| 26 | Guest Clues | Each guest reveals a fragment. Dr Harlan's book, Ivy's note, the Reverend's bible. | Multiple clue texts, state tracking |
| 27 | Synonym Table | GET/TAKE/GRAB all work. Parser looks up synonyms via DATA before dispatch. | Synonym data, lookup loop |
| 28 | Better Errors | "I can't see that here" vs "I don't understand that" vs "Nothing happens." Context-sensitive errors. | Error hierarchy, validation order |
| 29 | Scenery | Rooms have fixed scenery (paintings, furniture, windows) that can be EXAMINEd but not taken. | Scenery data, "You can't take that" |
| 30 | Room Contents List | Room description ends with item list and guest list. "You can see: a candle. Colonel Barwick stands frozen nearby." | Dynamic description building |
| 31 | HELP Command | HELP prints available verbs. Lists commands clearly. | Help text, user-friendly design |
| 32 | The Parser | Full two-word parser with synonyms, verb dispatch, noun validation. Refactor into clean GOSUB structure. | GOSUB architecture, string splitting, refactoring |

**Milestone:** A fully interactive manor. Pick up items, examine everything, talk to (well, examine) frozen guests, get useful error messages. The parser handles synonyms and provides helpful feedback.

### Phase 3: Puzzles and Peril (Units 33-48)

The game becomes solvable. Puzzles are implemented, clues lead to solutions, and the curse can be broken.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | The Locked Door | USE KEY ON DOOR (or UNLOCK DOOR) opens the tower. Key is consumed or stays in inventory. | USE verb, item+target interaction |
| 34 | The Tower | Tower rooms become accessible. Spiral staircase, observatory, Lady Ashworth's study. | Unlocking exits, state change |
| 35 | The Grimoire | EXAMINE GRIMOIRE in the tower study reveals the ritual requirements. FLASH 1 text. Red INK. Dramatic BEEP. | Atmosphere climax, FLASH, dramatic pacing |
| 36 | The Combination | Dining room place cards spell a number. EXAMINE CARDS reveals it. | Clue-to-solution mapping |
| 37 | The Sealed Chamber | Enter the combination at the sealed chamber door. Chamber opens with sound and drama. | Input validation, code entry |
| 38 | The Amulet | Amulet found inside the sealed chamber. "The Eye of Thornbury — a heavy gold amulet set with a dark stone." | Item in locked area, gated access |
| 39 | Cold Fire | LIGHT CANDLE (with tinderbox in inventory) produces blue flame. Candle state changes. | Item combination, state flags |
| 40 | The True Name | Fragments from guests assemble into a name. Player must SAY [NAME]. | String comparison, multi-source puzzle |
| 41 | SAY Command | SAY verb added. SAY [wrong word] = "Nothing happens." SAY [correct name] = progress. | New verb, secret word mechanic |
| 42 | The Ritual | In the tower study with amulet + lit candle + name spoken: the curse breaks. Multi-step sequence. | Multi-condition check, sequence validation |
| 43 | Breaking the Curse | Atmospheric sequence: the air shimmers, guests gasp, warmth returns. Green INK. Ascending BEEP scale. | Victory sequence, dramatic text, celebration |
| 44 | Escape | Front door unlocks. GO SOUTH from entrance hall. Victory text and final score. | End game state, score display |
| 45 | Score System | Points for exploration, examination, puzzle completion. SCORE command works throughout. | Score tracking, point allocation |
| 46 | Edge Cases | What if you SAY the name before finding the grimoire? What if you USE items in wrong rooms? Graceful handling. | Defensive programming, state validation |
| 47 | Red Herrings | Add atmospheric-only details: the stopped clock, wine bottles, the portrait. EXAMINEable but not puzzles. | Flavour content, misdirection |
| 48 | Puzzle Balance | Playtest the full puzzle chain. Are clues clear enough? Too obvious? Adjust hint levels. | Playtesting, difficulty tuning |

**Milestone:** The game is completable. All puzzles work, the curse can be broken, and the player can escape. Score tracks progress.

### Phase 4: Polish and Presentation (Units 49-64)

The game is done — now make it good. Title screen, better text, pacing, testing, and the final polished version.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "THE CURSED MANOR" in large letters (UDG or PRINT AT positioning). Atmospheric colour and sound. | Title design, PRINT AT, presentation |
| 50 | Instructions | Brief "HOW TO PLAY" screen. List commands, explain the premise. Accessible to newcomers. | User documentation, onboarding |
| 51 | Room Descriptions Rewrite | Revisit every room description. Tighten prose. Add sensory details. Make each room feel distinct. | Writing craft, concise prose |
| 52 | Guest Descriptions Rewrite | Revisit frozen guest descriptions. Make each pose vivid and specific. Ensure clues are fair but not obvious. | Clue design, fair play |
| 53 | Darkness | Cellar rooms without the lit candle show "It is pitch dark." Can't EXAMINE anything. Candle required. | Light source mechanic, conditional access |
| 54 | Ambient Events | Random atmospheric events: "A floorboard creaks somewhere above you." "The fire pops and sends up a shower of sparks." | Random text events, atmosphere |
| 55 | The Cat Returns | The cat now reacts to events. After the curse breaks, it purrs. Before, it hisses in certain rooms. | Dynamic NPC behaviour, state-aware text |
| 56 | Death? | Optional: can the player die? A wrong action in the sealed chamber, or staying too long? Adds tension. Consider carefully. | Fail states, game over, design choice |
| 57 | Abbreviations | N/S/E/W/U/D, I for INVENTORY, L for LOOK, X for EXAMINE. Quality-of-life. | Input preprocessing, shorthand expansion |
| 58 | Response Variety | "OK" is boring. Varied pickup messages: "You take the silver key. It's cold to the touch." | Response variation, personality |
| 59 | Optimisation | Program speed. Move frequently-accessed GOSUBs earlier in the listing. Use integer variables where possible. | BASIC performance, interpreter behaviour |
| 60 | Bug Sweep | Systematic testing: try every verb with every noun in every room. Fix broken combinations. | Testing methodology, systematic QA |
| 61 | Map Consistency | Walk every path. Check all exits match both ways. Verify locked doors work correctly. | Spatial consistency, data validation |
| 62 | Clue Fairness | Can a first-time player solve it without a walkthrough? Are all clues accessible before they're needed? Test with fresh eyes. | Puzzle design, fairness, accessibility |
| 63 | Final Line Count | Review the program. Are we under 500 lines? If over, what can be tightened? Every line must earn its place. | Code review, economy, editing |
| 64 | The Finished Game | Clean listing, title screen, full playthrough, final score. The complete game. | Completion, pride, accomplishment |

**Milestone:** A polished, complete text adventure. 35-40 rooms, 8-10 frozen guests, a multi-step puzzle chain, atmospheric colour and sound, a satisfying conclusion. Under 500 lines of Sinclair BASIC.

---

## Technical Notes

### Memory

The Spectrum 48K has limited memory for BASIC programs. Approximate budget:
- Program text: ~12-15 KB (500 lines averaging 25-30 characters)
- Variables and arrays: ~3-4 KB (room data, items, flags)
- Screen memory: fixed at $4000-$5AFF
- Available: ~25 KB after system and BASIC overhead

This should be comfortable. If memory becomes tight, room descriptions can be shortened or stored more compactly.

### Line Numbering

Use a consistent scheme:
- 1-99: Initialisation
- 100-199: Main game loop and input
- 200-299: Parser and dispatch
- 300-499: Verb handlers (GET, DROP, EXAMINE, USE, etc.)
- 500-699: Puzzle logic
- 700-799: Display routines (room, inventory, score)
- 800-899: Atmosphere (sound, colour, random events)
- 900-999: Title screen and endgame
- 1000+: DATA statements (rooms, items, guests, synonyms)

### Key Variables

```
r       - current room number
r$()    - room names
d$()    - room descriptions (first visit)
e()     - exits array (6 per room: N,S,E,W,U,D)
v()     - visited flags
i()     - inventory (item numbers, 0 = empty slot)
il()    - item locations (room number, -1 = carried, 0 = gone)
sc      - score
v$      - parsed verb
n$      - parsed noun
```

Short variable names for interpreter speed. Comments explain meaning.

---

## Walkthrough (Spoilers)

For testing purposes only. Not published with the game.

1. Explore the ground floor. EXAMINE guests as you find them. Note clue fragments.
2. Go to the conservatory. EXAMINE ORCHIDS. GET KEY.
3. Go upstairs. USE KEY ON DOOR (tower door). Go up to Lady Ashworth's study.
4. EXAMINE GRIMOIRE. Note the three requirements.
5. Go to the dining room. EXAMINE CARDS. Note the combination.
6. Go to the cellar. Go to the sealed chamber. ENTER [combination].
7. GET AMULET from the sealed chamber.
8. Go to the chapel (grounds). GET CANDLE.
9. Go to the study (ground floor). GET TINDERBOX.
10. LIGHT CANDLE (tinderbox must be carried).
11. Assemble the true name from guest clues: [name TBD during writing].
12. Return to the tower study.
13. USE AMULET. (Place it on the grimoire.)
14. SAY [true name].
15. The curse breaks. Go downstairs. GO SOUTH from entrance hall. Victory.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old Game 2 (The Cursed Manor, 16 units) with expanded 64-unit version as Game 1 of the restructured BASIC track.
