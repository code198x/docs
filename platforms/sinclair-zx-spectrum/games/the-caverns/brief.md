# The Caverns — Brief

**Title (working):** The Caverns
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 6 of 8 (slot 14)
**Headline concept:** Atmosphere — fear of the unseen
**Embedded concept:** Spatial reasoning — building a mental map from fragments
**Topics:** 10 topics, ~10–14 hours
**Constraint position:** period-faithful

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach that hidden state and partial information create tension — and that the player's imagination fills the gaps — so the learner arrives at Yearfall understanding that what the game *withholds* matters as much as what it shows.

---

## 2. Classic Ancestors

- **Hunt the Wumpus** (Gregory Yob, 1973) — the cave-exploration game. Move through connected rooms, sense nearby hazards ("I smell a Wumpus"), choose to move or shoot. The mechanic: a hidden map explored through proximity clues.
- **Colossal Cave Adventure** (Crowther & Woods, 1976) — the text adventure tradition of navigating by description, not by sight.

---

## 3. Core Experience

You are in a cave. Tunnels lead in several directions. You cannot see what is in the next room — but you can sense things: a draft (a pit is nearby), a smell (the creature is close), a glint (treasure). Move carefully, collect treasure, avoid the pit, evade the creature. The cave is dark; your imagination lights it.

---

## 4. Visual Direction

- **Deliberate restraint.** The darkness is the design. No map, no illustrations of rooms, no graphics in the play area. The player's imagination fills the gaps.
- Blue theme (BORDER 1, PAPER 1, INK 7) from unit 1. Minimal, atmospheric.
- INVERSE header bar: room number as navigation header.
- BRIGHT 1 on sensory clue text (draft, smell, glint) to make warnings more visible against the blue.
- Subtle compass rose using block graphics in the corner — four CHR$ characters showing N/S/E/W with available exits highlighted.
- DRAW torch on title screen (handle + flame outline in INK 6, ~6 DRAW commands). Adds identity without breaking the text-first design.

---

## 5. Audio Direction

- **Draft warning.** A low breathy tone (BEEP with very low pitch, short duration).
- **Creature warning.** A higher, more urgent tone.
- **Treasure found.** Ascending chime.
- **Falling into pit.** Descending tone — game over.
- **Silence between rooms.** The quiet is the atmosphere.

---

## 6. Level Design Direction

- **Content source:** The cave is a network of connected rooms stored in arrays. Each room has a list of exits (north/south/east/west) pointing to other room numbers. Hazards (pit, creature) and treasure placed randomly at game start.
- **Map shape.** 20 rooms, irregularly connected. Not a grid — some rooms have 2 exits, some have 4. The irregular connections create the feeling of a real cave, not a spreadsheet.
- **Difficulty curve.** The creature moves randomly each turn. The longer the player explores, the higher the chance of encountering it. Treasure is scattered — collecting all of it requires thorough exploration.
- **Scale:** 20 rooms, 1 pit, 1 creature, 3 treasures. One session: 10–20 minutes.
- **Onboarding.** The starting room has no hazards nearby. The first few moves are safe — the player learns the interface (compass directions, sensory clues) before encountering danger.

---

## 7. Anti-goals

- No combat — the player evades the creature, does not fight it. Combat systems arrive in V4 (Dungeons of Dorin).
- No weapons — no "shoot the Wumpus" option. The design focuses on exploration and evasion.
- No visible map — the atmosphere depends on not knowing the layout. A map would reduce the game to a path-finding exercise.
- No graphics — this is a text game. Visual atmosphere comes from words, colour, and sound.
- Maximum ~70 lines of BASIC.

---

## 8. Topic Progression

1. **A room.** Print a room description. List the exits: "Tunnels lead NORTH and EAST." INPUT a direction. **New:** room descriptions as text, compass-direction input. **Program:** ~8 lines.

2. **Connected rooms.** DIM arrays for room connections: `DIM n(20), s(20), e(20), w(20)`. Each array holds the room number reached by going that direction (0 = no exit). Move the player by following the connection. **New:** arrays as a graph structure (rooms connected by edges). **Program:** ~16 lines.

3. **Many rooms.** DATA statements hold room descriptions and connections. Read all DATA into arrays at start. The player navigates a 20-room cave. **New:** DATA-driven map loading, combining DATA/READ with arrays. **Program:** ~24 lines + DATA.

4. **Sensory clues.** Before printing the room description, check adjacent rooms. If the pit is one room away, print "You feel a cold draft..." If the creature is adjacent, print "A terrible smell fills the air..." **New:** adjacency checking (scan exit arrays for hazard room numbers). **Program:** ~32 lines + DATA.

5. **The pit.** If the player enters the pit room, they fall — game over. The draft warning gives them one room of advance notice. The decision: go toward the draft (risky) or away (safe but unexplored). **New:** lethal hidden state, consequence of ignoring warnings. **Program:** ~36 lines + DATA.

6. **The creature.** The creature occupies one room and moves randomly each turn (to a random adjacent room). If the player enters the creature's room, game over. The smell warning gives advance notice. Unlike the pit, the threat moves — the player cannot simply avoid a fixed location. **New:** NPC movement (random walk on the room graph), moving hidden state. **Program:** ~42 lines + DATA.

7. **Treasure.** Three rooms contain treasure. When the player enters, they collect it automatically — "You found a golden chalice!" Track collected treasures. Finding all three wins the game. **New:** collectible items, inventory as a counter. **Program:** ~48 lines + DATA.

8. **Atmosphere.** Refine the room descriptions — each room gets a unique flavour text. Add colour: warnings in yellow/red, treasure in green, normal text in white. Add sound: different tones for each sensory clue. The cave *feels* different with atmosphere layered on, even though the mechanics are unchanged. **New:** colour and sound as atmosphere (reinforces Oracle Stone's mood design). **Program:** ~55 lines + DATA.

9. **The mental map.** Add a "look" command that re-displays the current room. Add a move counter. The player navigates by memory and reasoning — which direction was the draft? Did the smell move? The design lesson: the game withholds the map so the player's brain becomes the map. That is **Atmosphere** — fear of the unseen. **New:** none (design reflection). **Program:** ~60 lines + DATA.

10. **Make it yours.** Title screen. Write your own room descriptions — make the cave yours. Adjust the room count, treasure count, creature behaviour. Add a "flee" mechanic — when the creature is adjacent, the player can choose to run in a random direction. The cave is now a complete game — and a gateway to the text adventure tradition. **New:** flee mechanic (random escape). **Program:** ~70 lines + DATA.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] Room connections form a navigable graph (no dead ends, no disconnected rooms)
- [ ] Sensory clues correctly identify adjacent hazards
- [ ] Creature moves randomly each turn and the smell updates accordingly
- [ ] Pit is lethal when entered
- [ ] All three treasures are collectable and the win condition fires
- [ ] Player cannot move through non-existent exits
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **framework** — room graph: arrays of exit connections representing a navigable map. The pattern behind every text adventure, dungeon crawler, and multi-screen game. Cross-platform.
- **ai** — random walk NPC: a creature that moves to a random adjacent room each turn. The simplest mobile hazard pattern.
- **framework** — adjacency-based clues: checking neighbouring nodes for hazards before the player moves. The pattern behind fog-of-war, proximity warnings, and radar.

---

## 11. Vault Tie-ins

- **Hunt the Wumpus** (Gregory Yob, 1973) — cave exploration with proximity clues as direct ancestor.
- **Colossal Cave Adventure** (Crowther & Woods, 1976) — the text adventure tradition.
- **Hidden information in game design** — the principle that what the game withholds creates tension, imagination, and atmosphere.
