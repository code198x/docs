# Signal: 64-Unit Outline

**Game:** 1 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Frogger-style lane crosser. Cross roads, ride logs, reach safety. A timing game that naturally exercises the entire custom chipset.

---

## Why This Game First?

Signal introduces the Amiga chipset symphony:

1. **68000 fundamentals** - Registers, addressing modes, instructions
2. **Display setup** - Bitplanes, Copper lists, screen structure
3. **Hardware sprites** - Player character
4. **Blitter basics** - BOBs for obstacles
5. **Paula sound** - Sample playback

Learners touch every custom chip without going deep on any.

---

## Phase 1: 68000 and Display (Units 1-16)
*Assembly fundamentals and screen setup.*

### Units 1-4: 68000 Basics
- **Unit 1:** 68000 architecture - registers (D0-D7, A0-A7)
- **Unit 2:** Addressing modes - immediate, register, memory
- **Unit 3:** Data movement - MOVE, LEA, MOVEM
- **Unit 4:** Arithmetic - ADD, SUB, MULU, DIVU

### Units 5-8: System Setup
- **Unit 5:** Amiga memory map - chip RAM, custom chips
- **Unit 6:** Taking over the system - disable OS
- **Unit 7:** Custom chip registers - address map
- **Unit 8:** VBlank interrupt - timing

### Units 9-12: Display Basics
- **Unit 9:** Bitplanes - how Amiga display works
- **Unit 10:** Display setup - DIWSTRT, DIWSTOP, DDFSTRT, DDFSTOP
- **Unit 11:** Bitplane pointers - BPL1PTH/L
- **Unit 12:** First display - coloured screen

### Units 13-16: Copper Introduction
- **Unit 13:** Copper concept - display list coprocessor
- **Unit 14:** Copper instructions - WAIT, MOVE
- **Unit 15:** Basic Copper list - display setup
- **Unit 16:** Copper colour splits - background bands

**Phase Goal:** Coloured display with Copper.

---

## Phase 2: Sprites and Player (Units 17-32)
*Hardware sprites for the player.*

### Units 17-20: Hardware Sprites
- **Unit 17:** Sprite structure - control words, data
- **Unit 18:** Sprite DMA - SPRxPTH/L
- **Unit 19:** Sprite colours - SPRxCOL
- **Unit 20:** First sprite - on screen

### Units 21-24: Player Character
- **Unit 21:** Frog sprite - design
- **Unit 22:** Sprite positioning - SPRPOS, SPRCTL
- **Unit 23:** Joystick input - CIA port reading
- **Unit 24:** Player movement - grid-based

### Units 25-28: Player Animation
- **Unit 25:** Animation frames - multiple images
- **Unit 26:** Direction facing - sprite flip
- **Unit 27:** Animation timing - frame rate
- **Unit 28:** Death animation - squash sequence

### Units 29-32: Player Mechanics
- **Unit 29:** Movement grid - lane alignment
- **Unit 30:** Movement timing - hop speed
- **Unit 31:** Screen boundaries - keep in bounds
- **Unit 32:** Player demo - moving frog

**Phase Goal:** Controllable animated player.

---

## Phase 3: Obstacles and Blitter (Units 33-48)
*BOBs for cars and logs.*

### Units 33-36: Blitter Basics
- **Unit 33:** Blitter concept - DMA graphics engine
- **Unit 34:** Blitter registers - BLTCON0/1, pointers
- **Unit 35:** Simple copy - A to D channel
- **Unit 36:** Blitter wait - BLTBUSY

### Units 37-40: Blitter Objects (BOBs)
- **Unit 37:** BOB concept - vs hardware sprites
- **Unit 38:** Cookie-cut mode - masking
- **Unit 39:** BOB drawing - to bitplanes
- **Unit 40:** Multiple BOBs - cars, logs

### Units 41-44: Lane Objects
- **Unit 41:** Car sprites - different types
- **Unit 42:** Log sprites - rideable platforms
- **Unit 43:** Lane movement - objects scroll
- **Unit 44:** Lane speeds - different per lane

### Units 45-48: Collision Detection
- **Unit 45:** Bounding box - rectangle collision
- **Unit 46:** Car collision - death
- **Unit 47:** Log collision - riding
- **Unit 48:** Water collision - death if no log

**Phase Goal:** Moving obstacles with collision.

---

## Phase 4: Game Completion (Units 49-64)
*Audio, scoring, polish.*

### Units 49-52: Paula Audio
- **Unit 49:** Paula overview - 4 channels, DMA
- **Unit 50:** Sample format - 8-bit signed
- **Unit 51:** Channel setup - AUDxLCH/L, AUDxLEN, AUDxPER
- **Unit 52:** Sound effects - hop, splash, death

### Units 53-56: Game Logic
- **Unit 53:** Safe zones - home bases
- **Unit 54:** Level completion - fill all homes
- **Unit 55:** Lives system - 3 lives
- **Unit 56:** Score tracking - points per hop

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Score display - Blitter text
- **Unit 59:** Lives display - remaining
- **Unit 60:** Game over screen

### Units 61-64: Polish
- **Unit 61:** Level progression - faster lanes
- **Unit 62:** Difficulty curve - speed increase
- **Unit 63:** Full testing
- **Unit 64:** Release build - bootable ADF

**Phase Goal:** Complete Frogger clone.

---

## Summary

**Signal** teaches Amiga hardware fundamentals.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes (32 colours)
- **Player:** Hardware sprite, 3 colours
- **Obstacles:** Blitter objects (BOBs)
- **Audio:** Paula sample playback
- **Copper:** Display setup, colour splits
- **Input:** Joystick via CIA
- **Distribution:** Bootable ADF

### Skills for Next Game

- 68000 assembly proficiency
- Copper list construction
- Hardware sprite control
- Basic Blitter operations
- Paula sample playback
- Interrupt-driven game loop
