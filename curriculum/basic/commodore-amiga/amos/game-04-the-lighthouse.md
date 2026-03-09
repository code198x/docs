# AMOS Game 04: The Lighthouse

**Track:** AMOS
**Genre:** Point-and-click adventure
**Units:** 64 (4 phases × 16 units)
**Language:** AMOS Professional
**Max lines:** ~500

---

## Premise

A storm drives your boat onto rocks. You wash ashore at the base of a lighthouse on a small island. The lighthouse is dark — its lamp hasn't burned in years. The keeper is gone. The radio in the keeper's cottage is dead. Another storm is coming.

You need to repair the lighthouse lamp to signal for rescue before the second storm hits. The island is small — six screens — but every location holds something you need: tools, parts, fuel, knowledge. The puzzles are logical, the atmosphere is maritime and melancholic, and the Amiga's hand-drawn aesthetic makes every screen feel like a painting.

This is THE Amiga genre. Monkey Island, Beneath a Steel Sky, Simon the Sorcerer — the point-and-click adventure defined the platform. The Lighthouse brings it to AMOS at a scale that fits 500 lines.

---

## The Island

### Six Screens

| Screen | Location | Atmosphere | Key items/puzzles |
|--------|----------|------------|-------------------|
| 1 | The Shore | Wreckage, grey waves, wind. Your boat in pieces. | Rope (from boat), glass lens (in rockpool) |
| 2 | The Path | Overgrown coastal path, wildflowers, cliff edge. | Wildflowers (decorative), rusty gate (needs oil) |
| 3 | The Cottage | Keeper's home, dusty, abandoned. Fireplace, desk, shelves. | Matches (desk drawer), journal (clues), oil can (shelf) |
| 4 | The Shed | Workshop. Tools, workbench, broken generator. | Wrench (workbench), fuel can (empty), fuse (box) |
| 5 | The Lighthouse Base | Heavy door, spiral staircase, machinery room. | Generator connection, fuse box, fuel intake |
| 6 | The Lamp Room | The lamp assembly, cracked lens housing, signal apparatus. | Lens housing (needs lens), lamp mechanism (needs power) |

### Navigation

Click screen edges to move between adjacent locations:
- Shore ↔ Path ↔ Cottage
- Path ↔ Shed
- Path ↔ Lighthouse Base ↔ Lamp Room (up stairs)

No maze, no dead ends. The island is small and fully explorable from the start. The challenge is figuring out what to do, not finding where to go.

---

## Puzzle Chain

### The Goal

Repair the lighthouse lamp to signal a passing ship.

### Requirements

The lamp needs three things:
1. **Power** — the generator must run (needs fuel + fuse + wrench to connect)
2. **A lens** — the lamp housing's lens is cracked (replace with the lens from the rockpool)
3. **A signal** — the lamp must be aimed at the shipping lane (clue in the keeper's journal)

### Puzzle Flow

```
Explore freely — all 6 screens accessible
  → Find the keeper's journal in the cottage (explains what the lamp needs)
  → FUEL: find the empty fuel can in the shed
    → Use fuel can on the boat wreckage (shore) to siphon fuel
    → Use fuel can on generator fuel intake (lighthouse base)
  → FUSE: find the fuse in the shed fuse box
    → Use fuse on the fuse box in the lighthouse base
  → CONNECTION: find the wrench in the shed
    → Use wrench on the generator coupling (lighthouse base)
    → Generator starts! Power restored.
  → LENS: find the glass lens in the rockpool (shore)
    → Use oil can on the rusty gate (path) to reach the shed shortcut
    → Use lens on the lamp housing (lamp room)
  → SIGNAL: read the journal for the compass bearing
    → Use signal apparatus in the lamp room to aim the lamp
  → Lamp lights → ship spotted → rescue
```

### Puzzle Design Principles

- **Every puzzle is logical.** No "use rubber chicken with pulley" absurdity. Fuel goes in the generator. The wrench connects pipes. The lens fits the housing.
- **Items are visible.** No pixel hunts. Clickable objects are clearly drawn and highlighted on hover.
- **The journal is the hint system.** It describes what the lamp needs in the keeper's own words. A player who reads it knows the goal; the puzzles are about finding and combining the components.
- **No deaths, no fail states.** The storm is atmospheric pressure, not a timer. The player explores at their own pace.

---

## Interface

### Verb System

Simple verb bar at the bottom of the screen:

```
[LOOK]  [USE]  [TAKE]  [TALK]  [INVENTORY]
```

- **LOOK**: Click LOOK, then click an object → description text
- **USE**: Click USE, click an inventory item, click a target → attempt combination
- **TAKE**: Click TAKE, then click an object → add to inventory (if takeable)
- **TALK**: Unused in this game (no NPCs) — but the infrastructure teaches the pattern
- **INVENTORY**: Shows carried items as icons. Click an item to select it for USE.

### Cursor

The mouse cursor changes based on context:
- **Arrow**: default movement
- **Eye**: hovering over an examinable object (after clicking LOOK)
- **Hand**: hovering over a takeable object (after clicking TAKE)
- **Gear**: hovering over a usable target (after clicking USE with item selected)

AMOS's sprite system handles the cursor — a hardware sprite that follows X Mouse, Y Mouse with different images per mode.

### Text Display

Descriptions and responses appear in a text area at the bottom of the screen (below the verb bar). 2-3 lines maximum. Text fades in, persists for 3 seconds or until the player clicks, then fades out.

---

## Visual Design

### Screen Rendering

Each screen is a hand-drawn background image loaded from disk. AMOS's Load Iff command loads IFF images directly. The backgrounds should look painterly — not pixel-perfect, but atmospheric. Muted colours, weather-beaten textures, a sense of isolation.

Interactive objects are BOBs layered over the background. This allows:
- Hover highlighting (BOB image swap to brighter version)
- Removal when taken (Bob Off)
- Animation (flickering fireplace, swaying rope, rotating lamp)

### Copper Effects

Each screen has a Copper gradient background visible through windows or sky areas:
- Shore: grey-to-dark-blue sky, white-capped wave colour cycling
- Path: grey sky with distant lightning flash (brief palette change)
- Cottage interior: warm amber from fireplace (colour cycling in fire area)
- Lamp room: dark until power restored → golden glow floods the room

### MOD Music

Each screen has a short ambient MOD loop:
- Shore: wind and waves (minimal, atmospheric)
- Cottage: creaking wood, ticking clock
- Lighthouse base: machinery hum (after power restored)
- Lamp room: triumphant theme when lamp lights

Music crossfades between screens (Track Stop on old, brief silence, Track Play new).

---

## Phase Breakdown

### Phase 1: Screens and Navigation (Units 1-16)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Loading a Picture | Load Iff loads a background image. The shore appears — waves, rocks, wreckage. | Load Iff, screen display |
| 2 | The Mouse Cursor | Hardware sprite follows X Mouse, Y Mouse. Custom arrow image. | Sprite, X Mouse, Y Mouse |
| 3 | Screen Edges | Click near the left edge → move to previous screen. Right edge → next. Navigation between two screens. | Click zones, screen transitions |
| 4 | Six Screens | All six backgrounds loaded (or loaded on demand). Click edges to navigate the island. | Multi-screen navigation, Load on demand |
| 5 | Transition Effect | Screen doesn't just snap — brief fade to black (palette manipulation), load new screen, fade in. | Palette fading, Fade command |
| 6 | Hotspot Zones | Define clickable areas per screen using AMOS Zone command. Shore: rockpool zone, boat zone, path-exit zone. | Zone, zone detection |
| 7 | Cursor Changes | Cursor sprite changes image when hovering over a hotspot. Eye icon for examinable, hand for takeable. | Conditional cursor, Zone detection |
| 8 | The Verb Bar | Five buttons at the bottom: LOOK, USE, TAKE, TALK, INVENTORY. Click to select current verb. | UI buttons, mode selection |
| 9 | LOOK Command | Select LOOK, click a hotspot → text description appears in the text area. "The boat is splintered beyond repair. But there's rope tangled in the rigging." | Verb + target dispatch, text display |
| 10 | Text Area | Text fades in at the bottom of the screen. Persists until click or 3 seconds. Fades out. | Timed text, fade effect |
| 11 | Object Descriptions | Every hotspot on every screen has a LOOK description. Data-driven: screen number + zone number → text string. | DATA-driven descriptions |
| 12 | Ambient Sound | Shore: wave MOD loop. Cottage: creaking MOD loop. Music changes with screen. | Track Load/Play per screen |
| 13 | Copper Sky | Copper gradient behind the sky area on the shore screen. Grey-to-blue gradient. | AMOS Copper commands |
| 14 | Animated BOBs | Fireplace flicker in the cottage (BOB alternates between 2 images). Rope sways on the shore. | Timer-based BOB animation |
| 15 | Atmosphere Pass | Every screen has: background, hotspots, descriptions, ambient music, at least one animated element. | Holistic screen design |
| 16 | Navigation Polish | Moving between screens feels smooth. Fades are the right speed. Music transitions cleanly. The island feels like a place. | Integration, atmosphere |

**Milestone:** Six explorable screens with hand-drawn backgrounds, Copper effects, ambient MOD music, animated objects, and text descriptions. No puzzles yet — but the island feels real.

### Phase 2: Items and Inventory (Units 17-32)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Taking an Item | Select TAKE, click the rope → rope disappears from screen (Bob Off), appears in inventory. | Item acquisition, BOB removal |
| 18 | The Inventory | Click INVENTORY → overlay shows carried items as icons (small BOBs). Click an item to select it. | Inventory display, item selection |
| 19 | Inventory Icons | Each item has a small icon sprite. Drawn in a grid on the inventory panel. Click to select for USE. | Icon rendering, grid layout |
| 20 | USE Command | Select USE, click inventory item (it's selected), click a hotspot target. Game checks if the combination is valid. | Two-phase input, combination checking |
| 21 | Valid Combinations | Data table: item X + target Y = result. "fuel_can + boat_wreckage = fuel_can_full". Lookup and execute. | Combination DATA, lookup table |
| 22 | Invalid Combinations | "That doesn't work." / "I can't use the rope on the wildflowers." Context-sensitive rejection messages. | Failure feedback, per-combination messages |
| 23 | Item Transformation | Using the fuel can on the boat wreckage transforms it into a full fuel can (different icon, different item ID). | Item state change, icon swap |
| 24 | All Items | Implement all takeable items: rope, lens, matches, oil can, wrench, fuel can, fuse, journal. | Full item set |
| 25 | The Journal | Taking the journal → a special LOOK that shows the keeper's notes. Multi-page text. Clue to the puzzle solution. | Special item, multi-page text |
| 26 | Oil on the Gate | USE oil can on rusty gate → gate opens with a creak (sound effect). New path accessible (shortcut). | Environment modification, gate state |
| 27 | Generator Repair | USE wrench on coupling, USE fuse on fuse box, USE fuel can on fuel intake. Three-step repair. Order doesn't matter. | Multi-step puzzle, state tracking |
| 28 | Power Restored | All three generator steps complete → machinery starts (sound effect, screen change — lights flicker on in lighthouse base). | Multi-condition trigger, environmental change |
| 29 | Lens Installation | USE lens on lamp housing → lens clicks into place. Visual change in lamp room. | Item placement, screen update |
| 30 | Signal Aiming | USE signal apparatus → brief interactive moment: click to aim the lamp toward the compass bearing from the journal. | Mini-interaction, directional input |
| 31 | The Lamp Lights | All conditions met → lamp ignites. Golden Copper gradient floods the lamp room. Triumphant MOD theme plays. | Victory trigger, multi-condition check |
| 32 | Rescue | Ship spotted → rescue sequence. Fade to dawn. "RESCUED." Final text. Credits. | End sequence, narrative conclusion |

**Milestone:** All puzzles work. The lighthouse can be repaired. The game is completable from start to finish.

### Phase 3: Atmosphere and Polish (Units 33-48)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Weather Effects | Rain on the shore (animated dots falling via BOBs or Ink). Intensifies in later screens. | Particle-like weather |
| 34 | Lightning | Occasional lightning flash on the path screen (palette snap to white, then back). Thunder BEEP. | Palette flash, timed event |
| 35 | Colour Cycling | Waves on the shore use colour cycling (rotating palette entries). Water appears to move. | Colour cycling, palette rotation |
| 36 | Fire Animation | Cottage fireplace: 3-frame BOB animation + colour cycling in the hearth area. Warm and alive. | Multi-technique animation |
| 37 | Generator Sound | After power is restored: low hum MOD loop in the lighthouse base. Machinery feels alive. | State-dependent audio |
| 38 | Text Personality | Rewrite all descriptions for voice and character. The player character has a dry, practical tone. Not Guybrush — more lighthouse engineer. | Writing craft, consistent voice |
| 39 | Examine Everything | Every hotspot has a detailed LOOK response. Furniture, paintings, tools, the view from the lamp room. The world rewards curiosity. | Content depth, description writing |
| 40 | Cursor Feedback | Clicking non-interactive areas: "Nothing interesting there." Clicking a taken item's spot: "I already took that." | Comprehensive feedback |
| 41 | Item Descriptions | LOOK at inventory items: detailed text. The journal is especially rich — backstory about the keeper and why they left. | Inventory LOOK, narrative depth |
| 42 | Sound Effects | Door creak, item pickup, oil pouring, wrench tightening, generator coughing to life, lens clicking into place. Sample Play for each. | Per-action audio |
| 43 | Title Screen | "THE LIGHTHOUSE" with an image of the lighthouse silhouette against a stormy sky. MOD title theme. | Title design |
| 44 | Introduction | Opening sequence: boat at sea, storm hits, crash, fade to black, fade up on the shore. Sets the scene. | Narrative opening, sequenced screens |
| 45 | Ending Polish | Rescue sequence: lamp sweeps the sea (animated), ship horn sounds, dawn breaks (palette shift), closing text, credits. | Multi-stage ending |
| 46 | Hint Sensitivity | If the player has been on the same screen for 60 seconds without progress, subtly highlight an unexamined hotspot. Gentle, not intrusive. | Adaptive hints, timed help |
| 47 | Testing | Play from start to finish with fresh eyes. Every combination, every description, every transition. | Full playthrough QA |
| 48 | Atmosphere Review | Play with headphones. Is the wind convincing? Does the cottage feel warm? Does the lamp lighting feel triumphant? | Emotional QA |

### Phase 4: Production (Units 49-64)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Screen Loading | Screens load from disk on demand (not all at startup). Loading is masked by the fade transition. | On-demand loading, masked load times |
| 50 | Save Game | Write game state to disk: current screen, inventory, puzzle flags. Load on startup if save exists. | File I/O, state serialisation |
| 51 | Multiple Save Slots | 3 save slots. Save/load menu accessible via function key. | Multi-slot save system |
| 52 | AMOS Compiler | Compile to standalone executable. Test that it runs without the AMOS environment. | AMOS compilation |
| 53 | Bootable ADF | Create a bootable ADF disk image. Game starts automatically on boot. | ADF creation, autoboot |
| 54-60 | Polish passes: text, sound, transitions, edge cases, performance | Various | Multiple techniques |
| 61 | The AMOS Showcase | Review: this game uses BOBs (Ricochet), mouse (Conduit), scrolling/MOD (Sidewinder), and adds IFF loading, Copper, save/load, compilation. Everything AMOS can do. | Cumulative skill review |
| 62 | What Assembly Would Do | Discussion: faster Copper lists, direct blitter control for screen transitions, interrupt-driven music for seamless audio. The adventure genre doesn't demand assembly — but the techniques transfer. | Bridge to assembly |
| 63 | Line Count | Under 500 lines? IFF loading and screen management are compact. Puzzle logic is data-driven. Should fit — but save/load might push it to a documented extension. | Scope check |
| 64 | The Finished Game | A complete point-and-click adventure. Six screens, hand-drawn backgrounds, inventory puzzles, Copper effects, MOD music, save/load, bootable ADF. The AMOS track's peak — and a genuine Amiga experience. | Completion |

---

## Technical Notes

### Screen Management

```basic
' Load and display a screen
Procedure LOAD_SCREEN[NUM]
  Fade 5 : Wait 35          ' Fade current screen to black
  Load Iff "screen"+Str$(NUM)+".iff", 0
  ' Set up zones for this screen
  SETUP_ZONES[NUM]
  ' Place interactive BOBs
  SETUP_BOBS[NUM]
  ' Start ambient music
  Track Load "ambient"+Str$(NUM)+".mod", 1
  Track Play 1
  Fade 5 To -1               ' Fade in to full palette
  Wait 35
End Proc
```

### Puzzle State

```basic
' Flags for puzzle progress
Dim FLAGS(20)
' 0=not done, 1=done
' FLAGS(1) = rope taken
' FLAGS(2) = lens taken
' FLAGS(3) = gate oiled
' FLAGS(4) = fuel siphoned
' FLAGS(5) = fuse installed
' FLAGS(6) = wrench connected
' FLAGS(7) = fuel poured
' FLAGS(8) = lens installed
' FLAGS(9) = lamp aimed
' FLAGS(10) = lamp lit
```

### Combination Table

```basic
' USE item X on target Y = result
' item_id, target_screen, target_zone, result_flag, result_text$
DATA 4, 1, 3, 4, "You siphon fuel from the boat's tank."
DATA 6, 5, 2, 5, "The fuse clicks into place."
DATA 5, 5, 3, 6, "You tighten the coupling with the wrench."
DATA 4, 5, 4, 7, "Fuel glugs into the generator tank."
DATA 3, 6, 1, 8, "The lens fits the housing perfectly."
```

### Memory

- IFF backgrounds: ~32 KB each × 6 = ~192 KB (loaded one at a time, not all in memory)
- Sprite bank: ~10-20 KB (item icons, cursors, animated objects)
- MOD files: ~20-50 KB each (loaded one at a time)
- Program: ~12-15 KB
- Total in memory at any time: ~80-100 KB — fits in 512 KB chip RAM

---

## Design Notes

### Why Point-and-Click

The point-and-click adventure is the Amiga's defining genre. More than shooters, more than platformers — the Amiga was THE adventure game machine. Monkey Island, Beneath a Steel Sky, Simon the Sorcerer, Lure of the Temptress. Teaching AMOS without building an adventure game would be like teaching C64 BASIC without touching the SID.

### Six Screens, Not Sixty

Commercial adventures had hundreds of screens. The Lighthouse has six. This is deliberate: 500 lines can't hold a LucasArts epic. But six screens with rich interaction, atmospheric audio, and logical puzzles can create a complete, satisfying experience. Every screen earns its place.

### The Keeper's Journal

The journal is the narrative heart. It explains the puzzle (what the lamp needs) but also tells a story: why the keeper left, what the lighthouse meant, why it matters. The player pieces together two stories simultaneously — the practical (repair the lamp) and the personal (understand the keeper). This is what adventure games do best.

### The AMOS Arc

1. **Ricochet**: action, BOBs, joystick — AMOS's immediacy
2. **Conduit**: puzzle, mouse, drawing — AMOS's interaction model
3. **Sidewinder**: scrolling, shooting, MOD — AMOS's hardware access
4. **The Lighthouse**: adventure, everything combined — AMOS's soul

The Amiga was an adventure game machine. The AMOS track ends where the platform's heart is.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. AMOS Game 4 in the restructured Amiga BASIC track. Point-and-click adventure in the Amiga tradition.
