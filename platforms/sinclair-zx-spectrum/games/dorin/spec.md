# Game 15: Dungeons of Dorin

**Track:** Spectrum BASIC
**Genre:** Dungeon crawl RPG
**Units:** 32 (2 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~450
**Save/load:** Yes — SAVE/LOAD game state to tape

---

## Premise

The dwarven city of Dorin fell centuries ago. Its halls — once filled with light and song — now twist downward through ten floors of darkness, each deeper than the last. Monsters roam the corridors. Treasure lies in forgotten chambers. At the bottom, the Heart of Dorin still pulses with ancient power. Reach it, and the city can be restored.

Dungeons of Dorin is a turn-based dungeon crawler inspired by Rogue, early CRPGs, and the Fighting Fantasy gamebooks that filled every Spectrum owner's bookshelf. The player creates a character with three stats (HP, attack, defence), descends through procedurally generated dungeon floors, fights monsters in turn-based combat, collects equipment that modifies stats, and manages limited resources. Each run is different because the dungeon layout is generated fresh from RND and a set of placement rules.

This is the most complex game the learner has built. Previous games had one or two interacting systems — movement plus collision, or a board plus rules. Dungeons of Dorin has five: movement, combat, inventory, procedural generation, and persistence. The learner must manage many variables, multiple arrays, and several subroutines that all depend on shared state. It is the proving ground for Game 16's autonomous NPCs and rich world simulation.

---

## Core Mechanics

### The Character

The player has three core stats:

| Stat | Starting value | Purpose |
|------|---------------|---------|
| HP | 20 | Hit points — reach 0 and the game ends |
| Attack | 3 | Added to a random roll when dealing damage |
| Defence | 2 | Subtracted from incoming damage (minimum 1 damage taken) |

Stats are modified by equipment. The player also tracks: current floor, gold collected, monsters slain, and turns survived.

### The Dungeon

Each floor is a 16×16 grid stored in a 2D array. Cells are walls, corridors, rooms, stairs down, or special features (treasure chests, monster lairs, healing fountains). The player sees only the area around their current position — a 7×7 viewport centred on the character, displayed with PRINT AT using UDG characters for walls, floor, doors, stairs, and items.

Floors get harder as the player descends. More monsters, fewer potions, tighter corridors. Floor 10 is the final level, containing the Heart of Dorin.

### Procedural Generation

Each floor is generated at runtime using RND and a set of rules:

1. Fill the grid with walls
2. Place 3-5 rooms (random position and size, 3×3 to 6×6)
3. Connect rooms with corridors (horizontal then vertical, or vice versa)
4. Place the stairs down in the room furthest from the stairs up
5. Scatter treasure chests, monsters, and potions according to floor difficulty
6. Place the player at the stairs-up position

The result is different every time, but always solvable — every room is connected, and stairs are always reachable.

### Movement

Turn-based, not real-time. The player presses Q/A/O/P (up/down/left/right) to move one cell. Each move is a turn. Monsters act after the player moves. The viewport scrolls to keep the player centred.

| Control | Key |
|---------|-----|
| Up | Q |
| Down | A |
| Left | O |
| Right | P |
| Inventory | I |
| Use potion | H |
| Save game | S (from inventory screen) |
| Load game | L (from title screen) |

### Combat

Walking into a monster triggers combat. Combat is turn-based and runs in a loop until one side is dead or the player flees:

1. **Player attacks:** Roll `INT(RND*6)+1 + attack`. Subtract monster defence. Deal remaining damage (minimum 1).
2. **Monster attacks:** Roll `INT(RND*6)+1 + monster_attack`. Subtract player defence. Deal remaining damage (minimum 1).
3. **Flee option:** Each turn, the player can attempt to flee. Success chance is 50% (adjusted by floor depth). Failure means the monster gets a free attack.

Combat uses the bottom portion of the screen — a text panel below the viewport showing attack rolls, damage dealt, and HP remaining.

### Monster Types

| Monster | HP | Attack | Defence | Floors | Gold |
|---------|-----|--------|---------|--------|------|
| Rat | 4 | 1 | 0 | 1-3 | 2 |
| Goblin | 8 | 2 | 1 | 2-5 | 5 |
| Skeleton | 12 | 3 | 2 | 3-7 | 8 |
| Troll | 18 | 4 | 2 | 5-8 | 12 |
| Wraith | 15 | 5 | 1 | 6-9 | 15 |
| Dragon | 30 | 6 | 4 | 10 | 50 |

Monsters are placed during generation. Each floor has 2-5 monsters chosen from the types available at that depth.

### Equipment

Equipment is found in treasure chests or dropped by defeated monsters. Each item modifies a stat:

| Item | Effect | Where found |
|------|--------|-------------|
| Rusty Sword | Attack +1 | Floors 1-3 |
| Steel Sword | Attack +2 | Floors 3-6 |
| Enchanted Blade | Attack +4 | Floors 7-10 |
| Leather Armour | Defence +1 | Floors 1-4 |
| Chain Mail | Defence +2 | Floors 4-7 |
| Plate Armour | Defence +3 | Floors 7-10 |
| Health Potion | Restore 10 HP | Any floor |
| Max HP Potion | Max HP +5 | Floors 5-10 |

The player can carry one weapon, one armour, and up to 3 potions. Finding a better weapon or armour replaces the current one (the old item is lost). Potions are consumed on use.

### Exploration and Discovery

The dungeon starts hidden. As the player moves, explored cells are marked as "seen" in a visibility array. Seen cells remain visible on the map even when the player moves away (drawn dimmer, without INK BRIGHT). Unseen cells show as solid black. This fog-of-war effect encourages exploration and creates tension — the player never knows what is around the next corner.

### Save and Load

From the inventory screen, the player can save the game state to tape. The save writes: character stats, current equipment, inventory, floor number, and the current floor layout. On the title screen, the player can load a saved game and resume from where they left off.

This teaches persistence — the idea that a program's state can survive beyond a single session.

### Winning and Losing

**Win:** Reach the Heart of Dorin on floor 10. A victory screen displays stats: floors cleared, monsters slain, gold collected, turns taken.

**Lose:** HP reaches 0. A death screen shows how far the player got and offers to start a new game.

---

## Phase Breakdown

### Phase 1: The Descent (Units 1-16)

Build the dungeon, move through it, and fight monsters. By the end of this phase, the game is playable: procedurally generated floors, fog of war, turn-based combat, and multiple monster types.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | The Hero | Title screen with game name and "Press any key". Define character stats as variables: `hp`, `at` (attack), `df` (defence), `mh` (max HP). Display stats on screen. | Character stats as variables, RPG stat model |
| 2 | The Empty Grid | Create a 16×16 2D array `d(16,16)` filled with walls (value 1). Display the full grid using PRINT AT — walls as UDG blocks, empty space as dots. | 2D array as game world, grid constants for cell types |
| 3 | Carving Rooms | Write a subroutine that places a room at a random position. A room is a rectangle of floor cells (value 0) inside the wall grid. Place 3 rooms. Display the result. | Procedural room placement, RND for position and size |
| 4 | Connecting Rooms | Write a corridor-carving subroutine. Given two points, carve a horizontal corridor then a vertical one (or vice versa, chosen randomly). Connect every room to the next. | Corridor generation, L-shaped paths |
| 5 | The Dungeon Generator | Combine rooms and corridors into a single `generate_floor` subroutine. Call it, display the result. Run it several times — each dungeon is different. | Procedural generation as a complete system |
| 6 | Placing the Player | Put the player in the first room. Display the player as a UDG character (a simple figure). Track position with `px`, `py`. | Player placement, UDG for the player character |
| 7 | Movement | Q/A/O/P moves the player. Check the target cell — if it is a wall, the move is blocked. Erase old position, draw new. The dungeon responds to input. | Turn-based movement, wall collision |
| 8 | The Viewport | Instead of showing the full 16×16 grid, display a 7×7 window centred on the player. The viewport scrolls as the player moves. Walls beyond the grid edge show as solid. | Viewport rendering, offset calculation, clipping |
| 9 | Fog of War | Add a visibility array `v(16,16)`. Cells start unseen (0). When the player is adjacent to a cell, mark it seen (1). Only draw seen cells. Unseen cells are black. | Fog of war, visibility tracking, dual-array state |
| 10 | The Status Panel | Below the viewport, display a status panel: HP, attack, defence, current floor, gold. Use PRINT AT with INK colours to make stats readable. | HUD design, formatted stat display |
| 11 | Stairs Down | Place stairs (cell value 2) in the room furthest from the player's starting room. Walking onto stairs generates a new floor and increments the floor counter. | Stairs placement, floor transitions, distance calculation |
| 12 | Placing Monsters | After generating a floor, scatter monsters in rooms. Each monster is stored in arrays: `mx()`, `my()` for position, `mt()` for type, `mh()` for HP. Draw monsters as coloured UDG characters. | Monster placement, parallel arrays for entity state |
| 13 | Starting a Fight | Walk into a monster's cell to trigger combat. Display the combat panel: monster name, monster HP, player HP. The player chooses "Attack" or "Flee". For now, attack always deals 1 damage. | Combat trigger, mode switch (exploration to combat) |
| 14 | Real Combat | Implement the full combat formula. Player rolls `INT(RND*6)+1 + at - monster_df`. Monster rolls `INT(RND*6)+1 + monster_at - df`. Display each roll and the damage dealt. Loop until one side falls. | Stat-based combat, random rolls, combat loop |
| 15 | Flee and Die | Implement flee (50% chance, failure means a free monster attack). Implement death: HP reaches 0, show "You have fallen" with stats, offer a new game. Remove defeated monsters from the map. | Flee mechanic, death handling, entity removal |
| 16 | Ten Floors | Wire up all 10 floors. Each floor generates harder content: more monsters, tougher types (use the monster table). Floor 10 places the Dragon. Reaching the Heart of Dorin shows a victory message. | Difficulty scaling, win condition, complete game loop |

**Milestone:** A playable dungeon crawler with procedural generation, fog of war, turn-based combat with stats and dice rolls, 6 monster types across 10 floors, and win/lose conditions. The core game works.

### Phase 2: Riches and Ruin (Units 17-32)

Add equipment, inventory, potions, save/load, and polish. By the end, the game is complete: a full RPG with interacting systems, persistence, and replayability.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 17 | Treasure Chests | Place treasure chests (cell value 3) during generation. Walking onto a chest reveals its contents — for now, always gold (a random amount). Add gold to the player's total. | Chest placement, loot tables, gold tracking |
| 18 | Health Potions | Chests can now contain potions. Add a potion inventory: `pi` counts potions carried (max 3). Pressing H during exploration uses a potion, restoring 10 HP (capped at max HP). | Consumable items, inventory count, HP restoration |
| 19 | Weapons | Chests can contain weapons. The player carries one weapon tracked by `wp` (0=fists, 1=rusty, 2=steel, 3=enchanted). Each weapon adds to attack. Finding a better weapon replaces the current one. | Equipment slots, stat modifiers, upgrade logic |
| 20 | Armour | Same system for armour: `ar` tracks current armour (0=none, 1=leather, 2=chain, 3=plate). Each adds to defence. Better armour replaces current. | Parallel equipment system, defence modifiers |
| 21 | The Inventory Screen | Press I to open the inventory: a full-screen display showing current weapon, armour, potions, gold, and stats (including equipment bonuses). Press any key to return to the dungeon. | Inventory UI, mode switching, derived stat display |
| 22 | Monster Drops | Defeated monsters can drop items. Rats drop nothing. Goblins occasionally drop gold. Tougher monsters drop better equipment. Use RND to determine drops. | Loot from combat, probability tables |
| 23 | Healing Fountains | A new dungeon feature: fountains (cell value 4) restore HP to maximum when used. Each fountain works once. Placed rarely — one per floor at most, and not on every floor. | Single-use features, world state flags |
| 24 | Combat Drama | Combat messages with visual weight: "The rat bites you for 3 damage", "You strike the troll for 5 damage". Screen shake via rapid `OUT 254` (the border port) — three fast border colour changes make the screen feel like it shakes on heavy hits. Health bars drain through attribute colour (POKE to the attribute file). Colour-code damage (red for player, green for monster). | `OUT` 254 (border port), screen shake, attribute-based health display |
| 25 | Atmospheric Depth | Deeper floors get darker PAPER, lower BRIGHT. Floor 1 is well-lit. Floor 5 is dim. Floor 10 is almost black. The dungeon *feels* dangerous as you descend. Difficulty curves match the visuals: floors 1-3 are gentle, floors 7-9 are brutal, floor 10 is the gauntlet. | Atmosphere through colour, BRIGHT as depth indicator, difficulty curves |
| 26 | Machine Code Helpers | Store machine code routines in DATA, POKE into RAM, call via RANDOMIZE USR — just like Game 14, but for different purposes. A fast room redraw that clears and redraws the viewport in one go. A richer sound effect routine that produces sounds BEEP can't. The game runs smoother than pure BASIC. | Machine code helpers (DATA/POKE/USR), fast redraw, richer audio |
| 27 | Map Memory | When the player descends to a new floor, the old floor is lost — regenerating it on return would produce a different layout. Accept this limitation but show the player a "You descend deeper..." message. The one-way descent is part of the tension. | Design constraints, one-way progression |
| 28 | Save Game | From the inventory screen, press S to save. Use SAVE with a DATA block: write `hp`, `mh`, `at`, `df`, `wp`, `ar`, `pi`, gold, floor number, and the current `d()` array to tape. | SAVE command, serialising game state |
| 29 | Load Game | On the title screen, press L to load. READ the saved values back into variables and arrays. Resume play on the saved floor with the saved stats. Handle the case where no save exists (error trapping). | LOAD command, deserialising state, error handling |
| 30 | Title Screen | A proper title screen: "DUNGEONS OF DORIN" in large text, a UDG illustration (a doorway or dungeon entrance), and options: "N - New Game", "L - Load Game". Set the mood with colour — dark PAPER, dim INK. | Title design, atmospheric presentation |
| 31 | Victory and Stats | Reaching the Heart of Dorin triggers a victory sequence: congratulations text, then a full stat summary — floors cleared, monsters slain, gold collected, turns taken, equipment found. A proper ending. | End-game summary, stat tracking across the full run |
| 32 | The Complete Dungeon | Final integration. Playtest all 10 floors. Verify save/load works. Check combat balance. Confirm every system interacts correctly: equipment modifies combat, potions save lives, generation creates fair floors, fog of war creates tension. The game is complete. | System integration, final QA, interacting systems |

**Milestone:** A complete dungeon crawl RPG with procedural generation, fog of war, turn-based combat, equipment, consumables, save/load, and 10 floors of escalating difficulty. The learner has built a game with five interacting systems — movement, generation, combat, inventory, and persistence — and is ready for the capstone.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `hp` | Current hit points |
| `mh` | Maximum hit points |
| `at` | Base attack |
| `df` | Base defence |
| `wp` | Weapon equipped (0-3) |
| `ar` | Armour equipped (0-3) |
| `pi` | Potions carried (0-3) |
| `gd` | Gold collected |
| `fl` | Current floor (1-10) |
| `px`, `py` | Player position on the grid |
| `tn` | Turn counter |
| `kl` | Monsters slain |

### Arrays

| Array | Size | Purpose |
|-------|------|---------|
| `d(16,16)` | 256 cells | Dungeon grid (0=floor, 1=wall, 2=stairs, 3=chest, 4=fountain) |
| `v(16,16)` | 256 cells | Visibility (0=unseen, 1=seen) |
| `mx(5)` | 5 entries | Monster X positions |
| `my(5)` | 5 entries | Monster Y positions |
| `mt(5)` | 5 entries | Monster type (1-6) |
| `mz(5)` | 5 entries | Monster current HP |

### Monster DATA

Monster stats are stored in DATA and read into lookup arrays at startup:

```basic
100 REM MONSTER DATA: NAME$, HP, ATTACK, DEFENCE, GOLD
110 DATA "Rat",4,1,0,2
120 DATA "Goblin",8,2,1,5
130 DATA "Skeleton",12,3,2,8
140 DATA "Troll",18,4,2,12
150 DATA "Wraith",15,5,1,15
160 DATA "Dragon",30,6,4,50
```

### UDG Allocation

| UDG | Character | Purpose |
|-----|-----------|---------|
| A | Wall | Solid block — dark, heavy |
| B | Floor | Light dot pattern |
| C | Player | Simple humanoid figure |
| D | Stairs | Downward arrow or steps |
| E | Chest | Small box shape |
| F | Fountain | Water drop or basin |
| G | Rat | Small, low |
| H | Goblin | Armed figure |
| I | Skeleton | Skull or bones |
| J | Troll | Large, heavy |
| K | Wraith | Ghostly shape |
| L | Dragon | Winged beast |
| M | Sword | Weapon icon (for inventory) |
| N | Shield | Armour icon (for inventory) |
| O | Potion | Bottle shape |
| P | Heart | HP indicator |

### Line Numbering

- 1-49: Initialisation, UDG definitions, monster DATA
- 50-99: Title screen, new game, load game
- 100-199: Dungeon generation (rooms, corridors, placement)
- 200-299: Main exploration loop (input, movement, viewport drawing)
- 300-349: Viewport rendering
- 350-399: Fog of war update
- 400-499: Combat loop (attack, defend, flee, death)
- 500-549: Inventory screen
- 550-599: Equipment and potion handling
- 600-649: Floor transition (stairs, generation, difficulty scaling)
- 650-699: Save and load
- 700-749: Victory and game over screens
- 750-799: Sound effects
- 800-899: DATA (monster stats, equipment names, loot tables)
- 900-999: UDG DATA

### Memory Budget

- Game logic: ~8-10 KB
- Arrays (dungeon + visibility + monsters): ~2 KB
- UDG DATA: ~0.5 KB
- Monster and equipment DATA: ~0.5 KB
- Total: ~11-13 KB — comfortable on 48K

### No ELSE

The Spectrum 48K has no ELSE keyword. All branching uses IF/THEN with GO TO to skip the alternative path. Combat and loot logic — which would naturally use IF/ELSE chains — must be structured as a sequence of IF/THEN checks with GO TO jumps past each branch.

### Turn-Based Advantage

Because the game is turn-based, there is no frame rate pressure. The interpreter can take as long as it needs to process a turn — the player waits for input, the game processes, and the result is displayed. This is a deliberate contrast with Blockstorm's real-time performance ceiling. Complex systems are viable in BASIC when you remove the clock.

---

## Changelog

- **v1.1 (2026-03-16):** Added OUT 254 screen shake (Unit 24), atmospheric depth via BRIGHT/PAPER (Unit 25), machine code helpers (Unit 26). Per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
