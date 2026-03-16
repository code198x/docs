# Game 16: The Cursed Manor

**Track:** Spectrum BASIC
**Genre:** Graphical text adventure with autonomous NPCs
**Units:** 64 (4 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~500
**Save/load:** Optional stretch goal

---

## Premise

You arrive at Thornbury Manor for Lady Ashworth's autumn gathering. The invitation was unexpected — you've never met her — but curiosity won. The front door swings open at your touch. Inside, the hall is lit, drinks are poured, a fire crackles. But every guest stands frozen mid-gesture: a man reaching for a glass, a woman mid-laugh, a butler carrying a tray. None of them move. None of them breathe.

The front door has locked behind you.

The manor is yours to explore. Somewhere in its rooms is the answer to what happened — and the means to undo it. Find the source of the curse, break it room by room, and escape. As the curse lifts, the guests unfreeze — and begin to act on their own. The butler follows you, offering help. Mrs Pembury wanders the drawing room muttering about the sherry. Colonel Barwick stalks the billiard room, suspicious of everyone. The manor fills with life, conversation, and complication.

The Hobbit (Melbourne House, 1982) shipped with every Spectrum+. It had autonomous characters who moved through the world, picked up items, fought each other, and acted whether or not the player was watching. Thorin sang about gold. Gandalf wandered off. The world felt alive. The Cursed Manor is the learner's own version of that miracle — built from scratch in 500 lines of Sinclair BASIC, using every skill from 15 previous games and 272 units of learning.

This is the magnum opus.

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
- A **location illustration** for key rooms (PLOT/DRAW graphics, displayed above the text)

Rooms should feel distinct. The library smells of leather and pipe smoke. The kitchen has a half-prepared meal going cold. The conservatory's glass panels show a moonlit garden. Each room tells a micro-story about the moment the curse struck.

### Frozen Guests

8 frozen guests throughout the manor, each frozen mid-action:

| Guest | Location | Frozen pose | Clue | Personality when unfrozen |
|-------|----------|-------------|------|---------------------------|
| Colonel Barwick | Billiard room | Leaning over a shot | Chalk mark on the green baize spells a word | Suspicious, territorial — stays near the billiard room, questions the player |
| Mrs Pembury | Drawing room | Reaching for a sherry glass | Her brooch is unusual — an eye motif | Anxious gossip — wanders between the drawing room and dining room, mutters clues |
| Dr Harlan | Library | Book open in hand | The open page describes a binding ritual | Helpful scholar — stays in the library, will answer questions about the ritual |
| Ivy (the maid) | Kitchen | Pouring from a kettle | Steam frozen mid-air; her apron pocket holds a note | Nervous but brave — follows the player, offers to carry items |
| Mr Oakes | Dining room | Carving knife raised over a roast | Place cards on the table spell something when read in order | Stoic and practical — stays near the dining room, keeps the fire lit |
| Miss Calder | Conservatory | Tending orchids | One orchid has a silver key wired to its stem | Quiet observer — moves slowly through the grounds, notices things others miss |
| Rev. Whitmore | Entrance hall | Mid-stride toward the door | His bible is open to a marked passage | Frightened — paces the entrance hall, wants to leave |
| Lady Ashworth | Tower study | Hands on an open grimoire | Only reachable late; the grimoire IS the curse | Remorseful — once freed, explains what happened and helps with the final ritual |

EXAMINEing a frozen guest reveals their pose and the clue. Once unfrozen, the same guest becomes a living character with a personality, a location, and goals.

### Map Structure

The manor is mostly open — the player can explore freely from the start. Gated areas:
- **Upper floor**: accessible from entrance hall (grand staircase)
- **Cellar**: accessible from kitchen (stairs down)
- **Tower**: locked door on the upper floor — requires the silver key (from conservatory orchid)
- **Sealed chamber** (cellar): requires solving a combination puzzle
- **Rooftop**: accessible from observatory (trapdoor, requires rope)

The progression is: explore freely, find the silver key, reach the tower, discover the grimoire, gather the components to break the curse, perform the ritual, escape.

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

**The Sealed Chamber** (medium): The dining room place cards, read in seat order, spell a four-digit combination. EXAMINE CARDS in the dining room reveals the numbers. Go to the sealed chamber in the cellar and ENTER CODE (or USE CARDS or similar).

**The True Name** (hard, multi-step): Each frozen guest holds a fragment of the name. Colonel Barwick's chalk marks, Ivy's note, Dr Harlan's book, the Reverend's bible passage — each reveals a syllable or letter. The player must EXAMINE multiple guests, note the fragments, and assemble them. The game does not assemble the name automatically — the player must SAY [NAME] with the correct word. After guests unfreeze, some offer additional hints through conversation if the player asks.

**Cold Fire** (medium): The blue candle from the chapel must be lit with the tinderbox from the study. LIGHT CANDLE or USE TINDERBOX ON CANDLE. The candle burns with a blue flame — "cold fire" as described in the grimoire.

**The Amulet** (medium): Inside the sealed chamber. Once the combination is entered, the chamber opens and the amulet can be taken.

### Red Herrings

A few items and details exist purely for atmosphere and misdirection:
- A grandfather clock stopped at 11:47 (the moment of the curse — atmospheric, not a puzzle)
- A cat (the only living thing besides the player — wanders between rooms, purely decorative early on)
- Wine bottles in the cellar (EXAMINEable, flavour text only)
- A portrait of Lady Ashworth in the entrance hall (foreshadowing, not a puzzle)

---

## Parser Design

### Command Structure

The parser accepts:
- **VERB** alone: LOOK, INVENTORY, HELP, QUIT, SCORE
- **VERB NOUN**: GET KEY, EXAMINE GUEST, OPEN DOOR
- **VERB NOUN NOUN**: USE KEY ON DOOR, PUT CANDLE IN HOLDER
- **SAY TO [character]**: SAY TO BUTLER OPEN CELLAR (NPC commands, Phase 4 stretch)
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
| SAY | SPEAK | Say a word (for the true name puzzle) or speak to a character |
| TALK | ASK | Talk to an unfrozen character |
| GIVE | OFFER | Give an item to a character |
| LOOK | L | Redisplay room description |
| INVENTORY | I | Show carried items |
| HELP | | Show available commands |
| QUIT | Q | End the game |
| SCORE | | Show current score |

### Parser Implementation

The parser is ~60-80 lines:
1. INPUT the command string
2. Split on first space to get verb$ and noun$ (and optionally second noun after ON/IN/WITH/TO)
3. Match verb$ against synonym table (DATA/READ loop)
4. Dispatch to appropriate GO SUB handler
5. Handler checks noun$ against current room contents, inventory, scenery, and present characters

Unrecognised verbs: "I don't understand that."
Recognised verb, invalid noun: "I can't see that here."
Valid combination with no effect: "Nothing happens."
NPC not present: "There is nobody here by that name."

### Synonyms via DATA

```basic
1000 DATA "GET","GET","TAKE","GET","GRAB","GET"
1010 DATA "LOOK","LOOK","L","LOOK"
1020 DATA "EXAMINE","EXAMINE","X","EXAMINE","CHECK","EXAMINE","INSPECT","EXAMINE"
1030 DATA "TALK","TALK","ASK","TALK"
```

READ through the pairs; if input matches the first element, replace with the second.

---

## Autonomous NPCs

This is what makes The Cursed Manor a capstone. The Hobbit's autonomous characters were revolutionary in 1982. Building the same kind of system — characters who act on their own, who move through the world, who make decisions — is the culmination of everything the learner has built across 15 games.

### How It Works

Each guest has a state record stored in parallel arrays:

```
Guest number, Name$, Current room, Frozen flag, Goal, Mood, Timer
```

- **Frozen flag**: 1 = still frozen, 0 = unfrozen and active
- **Goal**: a number representing the guest's current intention (0 = idle, 1 = go to a specific room, 2 = follow the player, 3 = find an item, 4 = talk to another guest)
- **Mood**: affects dialogue and behaviour (0 = neutral, 1 = helpful, 2 = nervous, 3 = suspicious)
- **Timer**: counts turns until the next action (prevents guests from acting every single turn)

### The NPC Turn

After the player enters a command and it is processed, every unfrozen guest takes a turn. The NPC turn runs as a GO SUB that loops through all guests:

```
FOR g = 1 TO 8
  IF frozen(g) = 0 THEN GO SUB 6000
NEXT g
```

The NPC handler at line 6000 checks the guest's goal and timer:

1. **Decrement timer.** If timer > 0, do nothing this turn (the guest is resting, thinking, or mid-action).
2. **Check goal.** If the guest has a goal, attempt to fulfil it:
   - Goal 1 (go to room): move one room toward the target, using the exit that brings them closer. If already there, set goal to 0.
   - Goal 2 (follow player): move toward the player's current room.
   - Goal 3 (find item): move toward the room containing the item. If in the same room, pick it up.
   - Goal 4 (talk to guest): move toward the other guest. If in the same room, deliver a line of dialogue.
3. **If no goal**: choose a new one based on personality. The butler's default is to follow the player. Mrs Pembury's default is to wander between the drawing room and dining room. Dr Harlan stays in the library. Each guest has a home room they gravitate toward.
4. **Set a new timer** (2-4 turns) so the guest does not act every single turn.

### What the Player Sees

The player only sees NPC actions that happen in their current room or in adjacent rooms:

- **Same room**: "Ivy enters from the north." / "The butler says, 'Shall I try the cellar, sir?'" / "Mrs Pembury picks up the sherry glass."
- **Adjacent room**: "You hear footsteps above you." / "A door opens somewhere nearby." / "Muffled voices come from the drawing room."
- **Distant**: Nothing. Events happen silently. The player discovers the effects later ("The rope is no longer in the stable yard — someone has moved it").

This creates the feeling of a living world. Things happen whether or not the player is watching. The manor is not a static puzzle box — it breathes.

### NPC Personalities

Each unfrozen guest has distinct behaviour:

| Guest | Default behaviour | Special actions |
|-------|-------------------|-----------------|
| Colonel Barwick | Patrols the billiard room and study. Suspicious. | Questions the player if they meet. "What are you doing in here?" |
| Mrs Pembury | Wanders drawing room and dining room. Nervous. | Mutters clue fragments. "The eye sees all, you know..." |
| Dr Harlan | Stays in the library. Helpful. | Will explain ritual details if the player talks to him. |
| Ivy | Follows the player. Nervous but willing. | Can carry one item for the player. "Shall I hold that for you, miss?" |
| Mr Oakes | Stays near the dining room and kitchen. Practical. | Keeps the fire going. Will mention if he has seen something unusual. |
| Miss Calder | Wanders the grounds slowly. Observant. | Notices things: "I saw something glinting in the greenhouse." |
| Rev. Whitmore | Paces the entrance hall. Frightened. | Wants to leave. Quotes scripture. Will not enter the cellar. |
| Lady Ashworth | Stays in the tower study. Remorseful. | Explains the curse. Helps with the final ritual if asked. |

### NPC Pathfinding

Guests move one room per action, choosing the exit that reduces their distance to the target room. Distance is calculated as the number of rooms in the shortest path — but since BASIC cannot afford a proper pathfinding algorithm, a simpler approach works: each room stores a "zone" value (ground = 1, upper = 2, cellar = 3, tower = 4, grounds = 5). To reach a room in a different zone, the guest first moves toward the connection point (stairs, garden door). Within a zone, the guest picks a random valid exit that is in the correct zone. This produces believable movement without expensive computation.

### Unfreezing Order

Guests unfreeze as the curse is broken. The curse does not lift all at once — it weakens in stages as the player completes puzzles:

| Event | Who unfreezes |
|-------|--------------|
| Unlock the tower door | Ivy (the maid) |
| Open the sealed chamber | Mr Oakes, Rev. Whitmore |
| Light the candle with cold fire | Mrs Pembury, Miss Calder |
| Assemble the true name | Colonel Barwick, Dr Harlan |
| Complete the ritual | Lady Ashworth (the last to wake) |

Each unfreezing is a dramatic moment. The frozen figure gasps, stumbles, looks around in confusion. The player witnesses it. From that point on, the guest is alive in the world.

---

## Location Graphics

Key rooms have illustrations drawn with PLOT and DRAW — atmospheric line art displayed in the top portion of the screen before the room description text. Not every room needs graphics. 10 rooms get illustrations, chosen for visual distinctiveness and narrative weight.

### Illustrated Rooms

| Room | Subject | Drawing approach |
|------|---------|-----------------|
| Entrance hall | Grand doorway, chandelier, frozen Reverend mid-stride | Arched doorway with DRAW lines, chandelier as CIRCLE + hanging lines |
| Library | Bookshelves, reading chair, Dr Harlan's silhouette | Horizontal shelf lines, vertical book spines, seated figure outline |
| Conservatory | Glass panels, orchids, moonlight through panes | Diagonal DRAW lines for glass panes, small CIRCLE shapes for flowers |
| Billiard room | Table outline, cue and balls, Colonel leaning | Rectangle for table, CIRCLE for balls, angled line for cue |
| Tower study | Grimoire on a lectern, Lady Ashworth's silhouette, candles | Lectern shape, open book, small flame shapes |
| Chapel | Arched window, pews, blue candle on altar | Pointed arch, horizontal pew lines, single candle shape |
| Wine cellar | Barrels, stone arch, descending stairs | CIRCLE halves for barrel ends, arch with DRAW, stepped line |
| Sealed chamber | Heavy door (closed) / dark void (open) | Thick rectangle outline with rivets (closed), empty black space (open) |
| Walled garden | Wall outline, bare tree, moonlit path | Horizontal wall, branching tree with DRAW, path as two lines |
| Observatory | Telescope, round window showing stars | Angled tube shape, CIRCLE for window, PLOT dots for stars |

### Drawing Approach

Each illustration is a GO SUB that draws into the top 64 pixels of the screen (rows 0-63 in pixel coordinates, which corresponds to character rows 0-7). Room text begins at row 9, leaving row 8 as a gap. The drawing area is cleared with a PAPER/INK combination appropriate to the room's mood before drawing begins.

Drawings use:
- **PLOT** for individual points (stars, rivets, small details)
- **DRAW** for straight lines and outlines (walls, furniture, architecture)
- **CIRCLE** for round objects (chandelier, billiard balls, barrel ends, window)
- **INK** changes within drawings for emphasis (the candle flame in yellow, moonlight in cyan)

Each illustration is 15-25 lines of BASIC — compact enough to fit within the 500-line budget when shared across 10 rooms. The drawings are simple but atmospheric: silhouettes and outlines rather than filled detail. The Spectrum's high-resolution mode (256x176) gives clean lines, and the limited palette forces a graphic style that suits the Gothic mood.

### When Graphics Display

The room illustration draws when:
- The player enters a room with graphics for the first time
- The player types LOOK in a room with graphics
- An NPC event triggers a visual change (the sealed chamber opening)

Rooms without illustrations show text only, starting at the top of the screen. The learner decides which rooms get graphics based on narrative importance and visual potential — not every room needs a picture, and restraint is part of the design.

---

## Atmosphere

### Colour

- **Default text**: white INK on black PAPER (dark, atmospheric)
- **Room descriptions**: cyan INK (distinct from commands and responses)
- **Item/clue reveals**: yellow INK (draws attention)
- **NPC dialogue**: green INK (characters stand out from narration)
- **Scary moments**: red INK + BEEP (finding the grimoire, the sealed chamber opening)
- **Victory**: green INK, BRIGHT 1
- **Location graphics**: room-specific INK on black PAPER (cyan for moonlit rooms, yellow for firelit rooms, white for neutral)

### Sound

- **Door opening**: low BEEP (short, resonant)
- **Picking up items**: rising two-note BEEP
- **Wrong command**: flat buzz BEEP
- **Finding a clue**: three ascending notes
- **Entering the tower**: descending ominous tone
- **Guest unfreezing**: a sharp gasp — high note then silence
- **NPC enters room**: soft footstep — short low BEEP
- **NPC speaks**: brief attention tone before dialogue
- **Breaking the curse**: ascending scale, triumphant
- **The cat**: occasional soft BEEP when it appears in a room

### Text Effects

- **FLASH 1** on the grimoire text when first examined
- **INVERSE 1** for frozen guests' descriptions (they stand out from the room)
- **BRIGHT 1** for unfrozen guest dialogue (alive, vivid)
- **PAUSE** for dramatic timing (the sealed chamber door grinds open... PAUSE 50... revealing darkness beyond)
- **PAUSE** after NPC actions in the player's room (gives each event a moment to land)

---

## Score System

Points awarded for progress. Maximum score: 100.

| Action | Points |
|--------|--------|
| Exploring a new room (first visit) | 1 each (35-40 total) |
| Examining a frozen guest | 2 each (16 total) |
| Finding the silver key | 3 |
| Reaching the tower | 3 |
| Opening the sealed chamber | 3 |
| Finding the amulet | 3 |
| Lighting the candle | 3 |
| Assembling the true name | 5 |
| Unfreezing a guest | 2 each (16 total) |
| Breaking the curse | 5 |
| Escaping the manor | 5 |

Displayed on SCORE command and at game end.

---

## Data Architecture

### Room Data

Each room is stored in DATA statements:

```
Room number, Name$, Description$, N exit, S exit, E exit, W exit, U exit, D exit, Zone, HasGraphics flag
```

Exit values: room number (1-40) or 0 (no exit) or -1 (locked, requires key/condition). Zone values: 1=ground, 2=upper, 3=cellar, 4=tower, 5=grounds. HasGraphics: 0 or 1.

### Item Data

```
Item number, Name$, Description$, Start room (0 = not placed yet, -1 = in inventory)
```

### Guest Data

```
Guest number, Name$, Start room, Pose$, Clue$, Frozen flag, Home room, Default goal, Mood
```

### State

- Current room number
- Inventory array (max 8 items)
- Room visited flags (for score and "first visit" descriptions)
- Guest examined flags
- Guest state arrays: location, frozen flag, goal, mood, timer
- Puzzle state flags (key found, tower unlocked, chamber opened, candle lit, name known, curse broken)
- Turn counter (for NPC timing)

---

## Phase Breakdown

### Phase 1: The Empty Manor (Units 1-16)

The player can move between rooms and read descriptions. No items, no puzzles, no parser beyond movement. The focus is on world-building with DATA-driven rooms, atmospheric text, and the first location illustrations. By the end, the manor is a complete, explorable place.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | The Gothic Font | Design a custom character set for the manor — gothic, atmospheric, manor-appropriate. POKE to CHARS (23606/23607) to install it. The entire game has its own typeface. Title screen: "THE CURSED MANOR" in the custom font, large PRINT AT text with colour. Atmospheric BEEP. "You arrive at Thornbury Manor..." Opening narration in cyan INK on black PAPER. | Custom character set via POKE CHARS, character design, atmospheric title |
| 2 | The Entrance Hall | First room. Display room name in BRIGHT 1 and description in cyan. A simple INPUT loop — the player types a command, but only LOOK works (redisplays the room). Everything else gets "I don't understand that." | INPUT, IF/THEN, string comparison, the command loop |
| 3 | North and South | Two rooms: entrance hall and drawing room. GO NORTH moves to the drawing room, GO SOUTH returns. Room number variable `r` tracks position. The screen clears and the new room displays. | LET for state, CLS between rooms, simple movement |
| 4 | Four Directions | Expand to four exits per room. Parse N, S, E, W as shortcuts for GO NORTH etc. Add the dining room (east of drawing room) and library (west). Four rooms, four directions. | String comparison for directions, multiple IF chains |
| 5 | Room Data | Move room names and descriptions into DATA statements. READ into string arrays at startup. The main loop looks up `r$(r)` and `d$(r)` instead of using hardcoded IF chains. The room data is separate from the logic. | DATA, READ, RESTORE, string arrays |
| 6 | The Ground Floor | All 12 ground floor rooms defined in DATA. DIM arrays for names, descriptions, and exits. A FOR/NEXT loop reads everything at startup. The player can explore the entire ground floor. | DIM, FOR/NEXT, 2D exit array `e(r,6)`, larger DATA blocks |
| 7 | The Upper Floor | Add 8 upper floor rooms. The grand staircase connects floors via UP and DOWN (exit indices 5 and 6). Parse U and D alongside compass directions. Two floors, 20 rooms. | U/D direction handling, expanding arrays and DATA |
| 8 | Atmosphere Through Colour | Add cellar rooms and grounds. 30+ rooms. Each area has a colour mood set via attribute POKE: frozen rooms are blue and cyan PAPER, cellar rooms are dim with low BRIGHT, grounds use dark blue PAPER for moonlight. The colour palette tells the story — the manor feels frozen, cold, cursed. | Attribute-based mood, PAPER/INK as atmosphere, conditional descriptions |
| 9 | Locked Doors | The tower door on the upper floor is locked — exit value -1. "The door is locked." when the player tries to go through. The sealed chamber in the cellar is also blocked. Two locked doors, two different messages. | Negative exit values as flags, gated progression |
| 10 | First Visit Text | Rooms show a longer description on first visit, a shorter one on return. A `v()` array tracks visited rooms. First visit: full atmospheric description. Return: room name and exit list only. | Boolean array, conditional text length |
| 11 | LOOK Command | LOOK (or L) redisplays the current room's full description, even if already visited. Begin separating the display logic into a GO SUB — the room display routine that will be called from multiple places. | GO SUB/RETURN, separating display from logic |
| 12 | The Wandering Cat | A grey cat appears randomly in rooms. Each turn, there is a 1-in-6 chance the cat is in the player's room. "A grey cat watches you from the shadows." The cat cannot be interacted with — purely atmospheric. This is the prototype for NPC movement. | RND for random events, atmospheric flavour, proto-NPC |
| 13 | The First Drawing | Draw the entrance hall illustration using PLOT and DRAW. An arched doorway, a chandelier (CIRCLE + hanging lines), stone floor lines. The drawing appears in the top 64 pixels when the player enters or types LOOK. Room text starts below. | PLOT, DRAW, CIRCLE, screen layout (graphics area + text area) |
| 14 | More Drawings | Add illustrations for the library (bookshelves, reading chair) and the conservatory (glass panes, moonlight, orchids). Each is a GO SUB called from the room display routine when `hg(r)=1`. Three illustrated rooms. | Multiple drawing subroutines, conditional GO SUB dispatch |
| 15 | Sound and Mood | Add BEEP to room transitions (a short tone when moving). Room-specific ambient details via random text: "A clock ticks somewhere." "The fire crackles." "Wind rattles a window pane." 1-in-4 chance each turn. | BEEP with pitch/duration, random atmospheric text |
| 16 | The Full Map | All 35-40 rooms in place. Every exit checked — north from room 3 leads to room 7, and south from room 7 leads back to room 3. Walk every path. Fix mismatched exits. Polish descriptions. The manor is complete and explorable. | Integration testing, data validation, play testing |

**Milestone:** A complete explorable manor with atmosphere, colour, sound, location illustrations, and a wandering cat. No items or puzzles yet — but it feels like a real place. The learner has built a world.

### Phase 2: Things and People (Units 17-32)

Items can be picked up and dropped. Frozen guests can be examined. The inventory system and a proper two-word parser take shape. By the end, the player can interact with everything in the manor.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | The Silver Key | One item in one room. The conservatory contains a silver key. "There is a silver key here." GET KEY picks it up. A single variable tracks whether the key is carried. | Item state variable, simple GET verb |
| 18 | Carrying Things | Expand to a proper inventory. An array `il()` tracks every item's location: a room number if it is on the floor, -1 if the player carries it, 0 if it has been consumed. GET moves an item from the room to inventory. | Array search and update, item location tracking |
| 19 | Dropping Things | DROP removes an item from inventory and places it in the current room. The item reappears in the room description. Items can be picked up and dropped repeatedly — they persist in the world. | Array removal, room state update |
| 20 | Inventory Command | I or INVENTORY lists everything the player carries. "You are carrying: a silver key, a blue candle." If carrying nothing: "You are empty-handed." | Array iteration, string building for display |
| 21 | Item Descriptions | EXAMINE [item] shows a detailed description. The silver key: "A small silver key, tarnished with age. It is cold to the touch." Each item has an examine-text stored in DATA alongside its name. | Item lookup by name, EXAMINE verb dispatch |
| 22 | All the Items | Add every game item: silver key, blue candle, tinderbox, rope, note (from Ivy's pocket), and the amulet (not yet accessible — in the sealed chamber). Item DATA statements define name, description, and starting room. | Expanding DATA structures, multiple items |
| 23 | Item Limits | Maximum 8 items carried. "You can't carry any more." If the inventory is full, the player must DROP something before picking up something new. | Array bounds checking, user feedback |
| 24 | The Frozen Guests | Guests appear in room descriptions. "Colonel Barwick stands frozen here, leaning over the billiard table." Guest data is stored in arrays: name, room, pose description. Guests are part of the room, not the floor — they cannot be taken. | Guest data arrays, room contents listing |
| 25 | Examining Guests | EXAMINE COLONEL (or BARWICK — match on either word) shows the frozen pose and reveals the clue. Yellow INK for clue text. "His chalk marks on the green baize spell... THORN." A flag records that this guest has been examined. | Partial name matching, INK colour changes, examined flags |
| 26 | All the Clues | Every guest's clue is in place. Dr Harlan's book describes a binding ritual. Ivy's note is a warning. The Reverend's bible passage references "the eye that watches." Each clue makes partial sense alone and full sense together. | Multiple clue texts, multi-source puzzle design |
| 27 | Synonym Table | GET, TAKE, GRAB, and PICK all work the same. The parser looks up every input verb against a synonym DATA table before dispatching. EXAMINE, X, CHECK, INSPECT all map to EXAMINE. Sixteen verbs, many synonyms. | Synonym DATA, lookup loop, verb normalisation |
| 28 | Better Errors | Three tiers of error message: (1) "I don't understand that" for unknown verbs, (2) "I can't see that here" for valid verbs with invalid nouns, (3) "Nothing happens" for valid combinations with no effect. The parser validates in order: verb first, then noun against room contents. | Error hierarchy, validation order, defensive parsing |
| 29 | Scenery | Rooms have fixed scenery that can be EXAMINEd but not taken. The library has bookshelves and a fireplace. The billiard room has the table. "You can't take that." Scenery data is stored per room — a string of keywords that the EXAMINE handler checks. | Scenery keywords, "You can't take that" response |
| 30 | Room Contents | The room description now ends with a dynamic list: items on the floor, frozen guests present, and scenery mentions. "You can see: a candle. Colonel Barwick stands frozen nearby." Built from arrays each time the room displays. | Dynamic description assembly, combining multiple data sources |
| 31 | HELP Command | HELP (or H) prints available verbs in a clean two-column layout. "Commands: GO, GET, DROP, EXAMINE, USE, OPEN, LIGHT, SAY, LOOK, INVENTORY, HELP, SCORE, QUIT." Brief and useful. | Help text, user-facing documentation |
| 32 | The Parser | Refactor the entire input handling into a clean GO SUB architecture. INPUT at line 100. Synonym lookup at line 200. Verb dispatch at line 250 (a chain of IF v$="GET" THEN GO SUB 300, etc.). Each verb handler is its own GO SUB. Clean, readable, maintainable. | GO SUB architecture, string splitting, refactoring for clarity |

**Milestone:** A fully interactive manor. Pick up items, examine everything, examine frozen guests and find their clues, get useful error messages, and navigate with synonyms and shortcuts. The parser is solid. The world responds.

### Phase 3: Puzzles and Awakening (Units 33-48)

The puzzles become solvable. Guests unfreeze as the curse weakens. The autonomous NPC system comes to life. By the end, the manor is a living world with characters who move and act on their own.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | The Locked Door | USE KEY ON DOOR (or UNLOCK DOOR, with key in inventory) opens the tower. The exit value changes from -1 to the tower staircase room number. The key remains in inventory — it might be needed again. | USE verb with two nouns, modifying exit data at runtime |
| 34 | The Tower | Tower rooms become accessible: spiral staircase, observatory, Lady Ashworth's study. Add illustrations for the tower study (grimoire on lectern) and observatory (telescope, star-filled window). Four new rooms with unique atmosphere. | Unlocking gated content, new room DATA and illustrations |
| 35 | The Grimoire | EXAMINE GRIMOIRE in the tower study reveals the ritual requirements in dramatic fashion. FLASH 1 text. Red INK. Descending BEEP. "To break the binding, three things must be brought together..." The three requirements are stated clearly. | Dramatic presentation, FLASH, multi-line reveal, pacing with PAUSE |
| 36 | The Combination | EXAMINE CARDS in the dining room reveals the place card numbers. The learner implements a clue that maps to a four-digit code — readable if the player pays attention, not obvious if they rush. | Clue design, mapping narrative to game state |
| 37 | The Sealed Chamber | At the sealed chamber door, the game prompts for a code. Enter the correct four digits and the door grinds open — BEEP, PAUSE 50, new room accessible. Wrong code: "Nothing happens." The chamber is now open permanently. | Input validation, code entry, dramatic reveal, state change |
| 38 | The Amulet | The amulet sits inside the sealed chamber. "The Eye of Thornbury — a heavy gold amulet set with a dark stone that seems to drink the light." GET AMULET. This also triggers the first unfreezing: Mr Oakes and Rev. Whitmore gasp back to life. | Item in locked area, triggered NPC unfreezing |
| 39 | Cold Fire | LIGHT CANDLE (with tinderbox in inventory) produces a blue flame. The candle's state changes — it is now "a candle burning with cold blue fire." This triggers Mrs Pembury and Miss Calder unfreezing. | Item combination, state transformation, triggered events |
| 40 | The True Name | Fragments from the guests assemble into a name. The player must SAY [NAME] with the correct word. Wrong name: "The word echoes and fades. Nothing happens." Correct name: Colonel Barwick and Dr Harlan unfreeze. | String comparison, multi-source puzzle, SAY verb |
| 41 | NPC State Arrays | Set up the parallel arrays for autonomous NPCs: `gl()` for guest location, `gf()` for frozen flag, `gg()` for goal, `gm()` for mood, `gt()` for timer. Initialise all guests as frozen. When a guest unfreezes, their flag changes and they gain a starting goal. | Parallel arrays for entity state, initialisation |
| 42 | The NPC Turn | After every player command, a GO SUB loops through all guests. Unfrozen guests with timer=0 attempt their current goal. Timer decrements each turn. The butler (Ivy) starts following the player. Test with one NPC first. | NPC update loop, timer-based action pacing |
| 43 | NPC Movement | Guests can move between rooms. Each turn, an active guest with a movement goal picks an exit that brings them closer to their target room (zone-based pathfinding). "Ivy enters from the south." The player sees arrivals and departures in their room. | Zone-based pathfinding, NPC movement, contextual messages |
| 44 | NPC Actions | Beyond movement, NPCs can: pick up an item (Ivy carries things for the player), speak a line of dialogue, react to the player's presence. Each personality drives different actions. Mrs Pembury mutters. Dr Harlan offers advice. | NPC action dispatch, personality-driven behaviour |
| 45 | Distant Events | If an NPC acts in an adjacent room, the player hears it: "You hear footsteps above you." "A door opens somewhere nearby." If an NPC moves an item, the player discovers it later. The world has depth beyond the current room. | Adjacent-room awareness, off-screen event messages |
| 46 | The Curse Breaks | In the tower study with amulet, lit candle, and name spoken: the curse breaks. Lady Ashworth unfreezes — the last guest. The final visual moment: colour floods back room by room via cascading attribute POKE (22528+). Frozen rooms were blue and cyan; as the curse lifts, they warm through yellow to white. The manor transforms from cold to alive. Ascending BEEP scale. | Multi-condition check, cascading attribute POKE, colour as narrative, dramatic climax |
| 47 | Escape | The front door unlocks. GO SOUTH from the entrance hall. The unfrozen guests gather to say goodbye. Rev. Whitmore practically runs out. The colonel nods stiffly. Victory text and final score. | End-game state, NPC farewell sequence, score display |
| 48 | Score and State | Score system fully implemented. Points for exploration, examination, puzzle completion, and unfreezing guests. SCORE command works throughout. Edge cases: what if the player SAYs the name before finding the grimoire? What if they USE items in wrong rooms? Graceful handling for every combination. | Score tracking, defensive programming, state validation |

**Milestone:** The game is completable. All puzzles work. Guests unfreeze and act on their own — moving, speaking, helping. The manor is alive. The NPC system produces emergent moments the learner did not explicitly script.

### Phase 4: Graphics and Polish (Units 49-64)

The game works — now make it sing. More illustrations, richer NPC interactions, a proper title sequence, and relentless polish. The final 16 units are about craftsmanship.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Sequence | A proper title screen: "THE CURSED MANOR" centred in BRIGHT white on black. Below it, a PLOT/DRAW illustration of the manor's front facade — peaked roof, windows, heavy door. "Press any key." A slow, low BEEP tone sets the mood. | Title design, illustration as branding, first impressions |
| 50 | Instructions | A "HOW TO PLAY" screen accessible from the title. Lists commands, explains the premise ("You are a guest at Thornbury Manor. Something has gone terribly wrong."), and reassures the player: "EXAMINE everything. Talk to people. There is no way to die." | Onboarding, user documentation, accessibility |
| 51 | Remaining Illustrations | Add the remaining location illustrations: billiard room, chapel, wine cellar, sealed chamber (both closed and open states), walled garden. Each is a GO SUB, 15-25 lines of PLOT/DRAW/CIRCLE. All 10 illustrated rooms now have graphics. | Multiple drawing subroutines, visual consistency |
| 52 | Room Descriptions Rewrite | Revisit every room description. Tighten prose — cut adjectives that do not earn their place. Add sensory details: the library smells of pipe smoke, the cellar is cold enough to see your breath, the conservatory glass is misted with condensation. | Writing craft, concise atmospheric prose |
| 53 | Guest Descriptions Rewrite | Revisit every frozen guest description and every unfrozen dialogue line. Make each pose vivid: not "standing" but "frozen mid-reach, fingers inches from the glass." Ensure clues are fair but not obvious. Ensure dialogue sounds like a real person. | Character voice, clue fairness, prose polish |
| 54 | TALK TO | TALK TO [character] when the character is unfrozen and in the same room. Each character has 2-3 dialogue lines that cycle. Dr Harlan explains the ritual. Ivy asks if she can help. The colonel demands to know what is going on. Talking advances the NPC's dialogue index. | TALK verb, per-character dialogue arrays, cycling responses |
| 55 | GIVE TO | GIVE [item] TO [character]. Some characters react usefully: give the note to Dr Harlan and he interprets it. Give the candle to Ivy and she carries it. Others refuse: "The colonel is not interested." This opens alternative puzzle approaches. | GIVE verb, item transfer between player and NPC |
| 56 | Darkness | Cellar rooms without the lit candle show "It is pitch dark. You can see nothing." Cannot EXAMINE anything. Movement still works (the player can stumble through). The candle is the light source — must be lit and carried. | Light source mechanic, conditional room display |
| 57 | Ambient Events | Random atmospheric text triggered each turn (1-in-4 chance): "A floorboard creaks somewhere above you." "The grandfather clock strikes once, though the hands have not moved." "The fire pops and sends up sparks." Separate pool for each area of the manor. | Random text events, area-specific atmosphere pools |
| 58 | The Cat Revisited | The cat now reacts to events. Before any guests unfreeze, it hisses in rooms near frozen guests. After guests unfreeze, it follows Ivy. When the curse breaks, it purrs. A small detail that rewards attention — the cat was an NPC all along. | State-aware NPC behaviour, environmental storytelling |
| 59 | Response Variety | Replace "OK" responses with contextual text. GET KEY: "You take the silver key. It is cold to the touch." DROP CANDLE: "You set the candle down carefully." Each item has pickup and drop messages stored in DATA. | Varied response text, personality in feedback |
| 60 | Abbreviations | N/S/E/W/U/D already work. Add X for EXAMINE, I for INVENTORY, L for LOOK, H for HELP, Q for QUIT. Pre-process single-character input before the synonym table. Quality-of-life for experienced players. | Input preprocessing, shorthand expansion |
| 61 | Machine Code and Speed | Machine code helpers for fast screen operations: a fast attribute fill routine (for the colour-flooding curse-break sequence), stored in DATA, POKEd into RAM, called via RANDOMIZE USR. Move frequently-called GO SUBs earlier in the listing. Use short variable names. Test that the NPC turn does not cause a noticeable pause. | Machine code helpers (DATA/POKE/USR), BASIC interpreter performance |
| 62 | Bug Sweep | Systematic testing: try every verb with every noun in every room. Move every NPC through every path. Pick up and drop every item in every room. Test puzzle completion in different orders. Fix every broken combination. | Systematic QA, edge case testing |
| 63 | Final Line Count | Review the program line by line. Are we under 500 lines? If over, tighten: combine related statements with colons, shorten DATA strings, remove redundant checks. Every line must earn its place. The constraint is part of the art. | Code review, economy, editing under constraint |
| 64 | The Finished Game | The complete Cursed Manor. Title screen, instructions, 35-40 rooms, 10 location illustrations, 8 autonomous NPCs, a multi-step puzzle chain, atmospheric colour and sound, a living world, and a satisfying conclusion. Run it. Play it. It is yours. | Completion |

**Milestone:** A polished, complete graphical text adventure with autonomous NPCs, a custom gothic character set, attribute-based mood that tells the curse's story through colour, and a final moment where the curse breaks and warmth floods back room by room. 35-40 rooms, 10 location illustrations drawn with PLOT and DRAW, 8 characters who move and act on their own, machine code helpers, and a world that breathes. Under 500 lines of Sinclair BASIC. The learner who typed in a magazine listing in Game 1 has built The Hobbit.

---

## Technical Notes

### Memory

The Spectrum 48K has limited memory for BASIC programs. Approximate budget:
- Program text: ~12-15 KB (500 lines averaging 25-30 characters)
- Variables and arrays: ~4-5 KB (room data, items, guest state, NPC arrays)
- Screen memory: fixed at $4000-$5AFF
- Available: ~25 KB after system and BASIC overhead

This should be comfortable. The NPC arrays add roughly 1 KB over a non-NPC version. If memory becomes tight, room descriptions can be shortened or drawing subroutines can share common shapes.

### Line Numbering

Use a consistent scheme:
- 1-99: Initialisation, DIM, DATA reading
- 100-199: Main game loop and INPUT
- 200-299: Parser, synonym lookup, and dispatch
- 300-499: Verb handlers (GET, DROP, EXAMINE, USE, OPEN, LIGHT, SAY, TALK, GIVE)
- 500-699: Puzzle logic (locked door, sealed chamber, ritual, unfreezing)
- 700-799: Room display routines (text, contents list, graphics dispatch)
- 800-899: Location illustration subroutines (PLOT/DRAW)
- 900-999: NPC update loop, movement, actions, dialogue
- 1000-1099: Atmosphere (sound, random events, cat)
- 1100-1199: Title screen, instructions, endgame
- 1200+: DATA statements (rooms, items, guests, synonyms, dialogue)

### Key Variables

```
r       - current room number
r$()    - room names
d$()    - room descriptions (first visit)
e()     - exits array (6 per room: N,S,E,W,U,D)
z()     - room zone (1-5)
hg()    - room has graphics flag
v()     - room visited flags
i$()    - item names
id$()   - item descriptions
il()    - item locations (room number, -1 = carried, 0 = consumed)
g$()    - guest names
gl()    - guest current room
gf()    - guest frozen flag (1=frozen, 0=active)
gg()    - guest current goal
gm()    - guest mood
gt()    - guest timer (turns until next action)
gh()    - guest home room
ge()    - guest examined flag
sc      - score
v$      - parsed verb
n$      - parsed noun
n2$     - parsed second noun (after ON/IN/WITH/TO)
tn      - turn counter
```

Short variable names for interpreter speed. The naming convention — `g` prefix for guest arrays, `i` prefix for item arrays — keeps related data grouped.

### NPC Performance

The NPC update loop runs after every player command. With 8 guests and simple logic per guest, this adds a fraction of a second per turn — imperceptible in a text adventure where the player is reading and thinking. If performance becomes noticeable:
- Skip frozen guests early (the IF check is fast)
- Only run the full pathfinding logic when timer reaches 0 (most turns, the guest just decrements timer and returns)
- Limit adjacent-room messages to one per turn (even if multiple NPCs acted nearby)

### No ELSE

Sinclair BASIC on the 48K has no ELSE keyword. All branching uses IF/THEN with GO TO to skip the alternative. The NPC goal dispatch — which would naturally be an IF/ELSE IF chain — becomes a sequence of IF/THEN GO TO checks:

```basic
6010 IF gg(g)=0 THEN GO TO 6100
6020 IF gg(g)=1 THEN GO SUB 6200: GO TO 6100
6030 IF gg(g)=2 THEN GO SUB 6300: GO TO 6100
6040 IF gg(g)=3 THEN GO SUB 6400: GO TO 6100
```

This is verbose but clear. Each goal has its own handler subroutine.

### Drawing Budget

Ten illustrated rooms at 15-25 lines each = 150-250 lines of drawing code. This is significant within a 500-line budget. Strategies to stay within limits:
- Share common shapes (a generic "arched doorway" subroutine called by multiple rooms)
- Use relative DRAW (lines relative to previous position) to reduce PLOT calls
- Keep illustrations simple — silhouettes and outlines, not filled detail
- Consider storing drawing data in DATA statements and using a generic "draw from data" loop

### The 500-Line Challenge

500 lines is tight for a game with 35-40 rooms, 10 illustrations, a parser, inventory, puzzles, and autonomous NPCs. The learner will need every optimisation trick from 15 previous games:
- Multiple statements per line (colon-separated)
- Short variable names
- DATA-driven content (rooms, items, guests, dialogue) rather than hardcoded IF chains
- Shared subroutines for common operations
- Ruthless editing of descriptions and dialogue

The constraint is not a limitation — it is the point. Fitting this much ambition into 500 lines of BASIC teaches economy, prioritisation, and craft. Every line earns its place or it goes.

---

## Walkthrough (Spoilers)

For testing purposes only. Not published with the game.

1. Explore the ground floor. EXAMINE guests as you find them. Note clue fragments.
2. Go to the conservatory. EXAMINE ORCHIDS. GET KEY.
3. Go upstairs. USE KEY ON DOOR (tower door). Go up to Lady Ashworth's study. Ivy unfreezes.
4. EXAMINE GRIMOIRE. Note the three requirements.
5. Go to the dining room. EXAMINE CARDS. Note the combination.
6. Go to the cellar. Go to the sealed chamber. ENTER [combination]. Mr Oakes and Rev. Whitmore unfreeze.
7. GET AMULET from the sealed chamber.
8. Go to the chapel (grounds). GET CANDLE.
9. Go to the study (ground floor). GET TINDERBOX.
10. LIGHT CANDLE. Mrs Pembury and Miss Calder unfreeze.
11. Assemble the true name from guest clues: [name TBD during writing].
12. SAY [true name]. Colonel Barwick and Dr Harlan unfreeze.
13. Return to the tower study with amulet and lit candle.
14. USE AMULET. SAY [true name]. The curse breaks. Lady Ashworth unfreezes.
15. Go downstairs. GO SOUTH from entrance hall. The guests gather. Victory.

---

## Changelog

- **v1.1 (2026-03-16):** Added custom gothic character set (Unit 1), attribute-based mood (Unit 8), cascading colour-flood curse-break moment (Unit 46), machine code helpers (Unit 61). Per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum. Replaces Game 1 version (text-only, no NPCs) with the full capstone: autonomous NPCs, location graphics, advanced parser, 64 units across 4 phases. Content reused from the Game 1 outline where appropriate (premise, manor layout, puzzles, parser, atmosphere, score system).
