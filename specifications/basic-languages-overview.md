# BASIC Languages: Gateway to Game Development

**Purpose:** Document BASIC variants across platforms, their capabilities for game development, and curriculum tracks for BASIC-based learning.

**Last Updated:** 2026-01-18

---

## Why BASIC Matters

BASIC was:
1. **First language for millions** - Accessible entry point
2. **Built into machines** - Available immediately
3. **Capable of real games** - Especially enhanced BASICs
4. **Gateway to assembly** - Natural progression
5. **Still relevant** - Modern retro development

Some BASICs (AMOS, Blitz, BBC BASIC) produced **commercial games**.

---

## Part 1: BASIC Variants Overview

### The BASIC Family Tree

| Era | Development |
|-----|-------------|
| **1964** | Dartmouth BASIC (Kemeny & Kurtz) |
| **1975** | Microsoft BASIC (Gates & Allen) |
| **1977** | Apple Integer BASIC, Commodore BASIC |
| **1981** | BBC BASIC (Acorn) |
| **1982** | Sinclair BASIC |
| **1987** | AMOS (Amiga) |
| **1991** | Blitz Basic (Amiga) |

### Capability Tiers

| Tier | Characteristics | Examples |
|------|-----------------|----------|
| **Basic** | Slow, limited graphics | C64 BASIC V2, early MS-BASIC |
| **Enhanced** | Better graphics/sound commands | Simons' BASIC, Laser BASIC |
| **Structured** | Procedures, local variables | BBC BASIC |
| **Game-oriented** | Sprites, screens, game commands | AMOS, Blitz Basic, STOS |
| **Compiled** | Fast execution | Blitz Basic, PureBasic |

### Platform Comparison

| Platform | Built-in BASIC | Game Capability | Better Options |
|----------|---------------|-----------------|----------------|
| **C64** | BASIC V2 (limited) | Poor | Simons' BASIC, BASIC Boss |
| **Spectrum** | Sinclair BASIC | Moderate | Beta BASIC, Laser BASIC |
| **BBC Micro** | BBC BASIC | Excellent | Built-in is great |
| **Amstrad CPC** | Locomotive BASIC | Good | Built-in is capable |
| **MSX** | MSX-BASIC | Moderate | MSX-BASIC 2.0+ |
| **Amiga** | AmigaBASIC | Poor | AMOS, Blitz Basic |
| **Atari ST** | ST BASIC | Poor | STOS, GFA BASIC |
| **Atari 8-bit** | Atari BASIC | Moderate | Turbo-BASIC XL |

**Vault entries:**
- `basic-history` - Culture entry
- `microsoft-basic` - Software entry
- `dartmouth-basic` - Culture entry

---

## Part 2: C64 BASIC

### BASIC V2 Limitations

| Problem | Impact |
|---------|--------|
| **No sprite commands** | Must POKE everything |
| **No sound commands** | Must POKE SID directly |
| **No graphics commands** | Must POKE VIC-II |
| **Slow** | Interpreted, inefficient |
| **No structured programming** | GOTO spaghetti |

### Why C64 BASIC Was Bad

Commodore used the same BASIC from the PET (1977):
- No knowledge of VIC-II chip
- No knowledge of SID chip
- Designed before C64 existed

```basic
10 REM SPRITE EXAMPLE - TEDIOUS!
20 V=53248:POKE V+21,1
30 POKE 2040,13:POKE V,100:POKE V+1,100
40 FOR I=0 TO 62:READ A:POKE 832+I,A:NEXT
```

Compare to BBC BASIC or AMOS - night and day.

### Enhanced C64 BASICs

| Extension | Features |
|-----------|----------|
| **Simons' BASIC** | Graphics, sound, sprites |
| **BASIC Boss** | Compiled, faster |
| **Laser BASIC** | Extended commands |
| **Super Expander 64** | Cartridge, graphics |
| **Graphics BASIC** | Drawing commands |

### Simons' BASIC

| Aspect | Notes |
|--------|-------|
| **Creator** | David Simons |
| **Publisher** | Commodore |
| **Features** | 114 new commands |
| **Sprites** | SPRITE, MOB commands |
| **Sound** | ENVELOPE, VOL |
| **Graphics** | CIRCLE, LINE, PAINT |

Made C64 BASIC actually usable for games.

### Commercial C64 BASIC Games

Despite limitations, some games were written in BASIC:
- Type-in games from magazines
- Simple arcade games
- Text adventures
- Educational software

**Vault entries:**
- `c64-basic-v2` - Software entry
- `simons-basic` - Software entry

---

## Part 3: BBC BASIC

### Why BBC BASIC Was Excellent

| Feature | Benefit |
|---------|---------|
| **Procedures (PROC)** | Structured code |
| **Functions (FN)** | Reusable code |
| **Local variables** | No conflicts |
| **Named procedures** | Readable code |
| **Built-in assembler** | Inline assembly |
| **Good speed** | Reasonably fast |
| **Graphics commands** | DRAW, PLOT, GCOL |
| **Sound commands** | SOUND, ENVELOPE |

### BBC BASIC Example

```basic
10 MODE 2
20 PROCSETUP
30 REPEAT
40   PROCMOVEPADDLE
50   PROCMOVEBALL
60   PROCCHECKCOLLISION
70   PROCDRAW
80 UNTIL gameover%
90 END
100
110 DEF PROCSETUP
120   paddle% = 640
130   ballx% = 500 : bally% = 500
140 ENDPROC
```

This looks like a real programming language!

### Built-in Assembler

```basic
10 DIM code% 100
20 FOR pass% = 0 TO 2 STEP 2
30 P% = code%
40 [OPT pass%
50 LDA #65
60 JSR &FFEE
70 RTS
80 ]
90 NEXT
100 CALL code%
```

You could mix BASIC and assembly seamlessly.

### Commercial BBC BASIC Games

Many BBC games were written in BASIC:
- Educational titles
- Adventure games
- Arcade games (with assembly for speed)
- Simulations

BBC BASIC was genuinely suitable for game development.

**Vault entries:**
- `bbc-basic` - Software entry (major)
- `acorn-basic-assembler` - Technique entry

---

## Part 4: Spectrum BASIC

### Sinclair BASIC Characteristics

| Feature | Notes |
|---------|-------|
| **Keyword entry** | Single keypress per keyword |
| **Line editor** | Edit by line |
| **Reasonable speed** | Faster than C64 BASIC |
| **Graphics** | PLOT, DRAW, CIRCLE |
| **Sound** | BEEP (limited) |
| **Attributes** | INK, PAPER, BRIGHT, FLASH |

### Spectrum BASIC Example

```basic
10 FOR n=0 TO 255
20 PLOT n,88+80*SIN(n/20)
30 NEXT n
```

Graphics commands built-in - much better than C64.

### Enhanced Spectrum BASICs

| Extension | Features |
|-----------|----------|
| **Beta BASIC** | Procedures, toolkit |
| **Laser BASIC** | Sprites, scrolling |
| **SAM BASIC** | (SAM Coupé) Enhanced |

### Commercial Spectrum BASIC Games

Many Spectrum games used BASIC:
- Text adventures (common)
- Puzzle games
- Educational titles
- Early arcade games

Speed limitations meant action games usually needed assembly.

**Vault entries:**
- `sinclair-basic` - Software entry
- `beta-basic` - Software entry

---

## Part 5: AMOS (Amiga)

### What Made AMOS Special

| Feature | Capability |
|---------|------------|
| **Sprites** | Full Amiga sprite support |
| **Bobs** | Blitter objects |
| **Screens** | Multiple screens, scrolling |
| **Sound** | Samples, tracker music |
| **Compiled** | Compiler available |
| **Game-focused** | Designed for games |

### AMOS Creator

| Aspect | Notes |
|--------|-------|
| **Creator** | François Lionet |
| **Publisher** | Europress (later Clickteam) |
| **Released** | 1990 |
| **Versions** | AMOS, Easy AMOS, AMOS Pro |

François Lionet also created STOS for Atari ST.

### AMOS Example

```basic
' AMOS sprite example - SO much easier than C64!
Load "sprites.abk",1
Screen Open 0,320,256,32,Lowres
Flash Off : Curs Off : Cls 0

Sprite 1,160,128,1
Do
  Add X,2
  If X>300 Then X=0
  Sprite 1,X,128,
  Wait Vbl
Loop
```

Compare this to the C64 POKE nightmare!

### AMOS Professional

| Feature | Notes |
|---------|-------|
| **Released** | 1992 |
| **Improvements** | Better editor, more commands |
| **Compiler** | Faster execution |
| **Interface** | New development environment |

### Commercial AMOS Games

Real commercial games made in AMOS:

| Game | Developer | Notes |
|------|-----------|-------|
| **Ultimate Soccer Manager** | Impressions | Management sim |
| **Guardian** | Acid Software | Defender clone |
| **Scorched Tanks** | | Worms precursor |
| **Minskies** | | Puzzle game |
| **Numerous PD/shareware** | Various | Huge library |

AMOS proved BASIC could make real games.

### AMOS Extensions

| Extension | Purpose |
|-----------|---------|
| **AMOS 3D** | 3D graphics |
| **AMOS Music** | Tracker support |
| **AMOS Compiler** | Faster execution |
| **Various user extensions** | Community-created |

**Vault entries:**
- `amos` - Software entry (major)
- `francois-lionet` - People entry
- `amos-professional` - Software entry

---

## Part 6: Blitz Basic (Amiga)

### Blitz Basic Characteristics

| Feature | Capability |
|---------|------------|
| **Compiled** | True compiler, fast execution |
| **Structured** | Proper programming constructs |
| **Low-level access** | Peek/Poke, direct hardware |
| **Type system** | Proper data types |
| **Objects** | Blitz objects system |

### Blitz vs AMOS

| Aspect | AMOS | Blitz Basic |
|--------|------|-------------|
| **Speed** | Interpreted (compiler available) | Always compiled |
| **Learning curve** | Easier | Steeper |
| **Power** | Game-focused | More general |
| **Commercial use** | Some | More |

### Blitz Basic 2

| Feature | Notes |
|---------|-------|
| **Released** | 1993 |
| **Company** | Acid Software |
| **Features** | Full Amiga access, fast |

### Commercial Blitz Basic Games

| Game | Developer | Notes |
|------|-----------|-------|
| **Skidmarks** | Acid Software | Racing game |
| **Worms** | Team17 | Original version |
| **Super Skidmarks** | Acid Software | Sequel |
| **Various commercial** | Multiple | Real releases |

**Worms** was written in Blitz Basic - one of the most successful games ever.

### The Team17 Connection

Team17 used Blitz Basic extensively:
- Rapid prototyping
- Full game development
- Worms franchise began in Blitz

### Blitz Legacy

| Successor | Platform |
|-----------|----------|
| **Blitz Basic** | PC |
| **BlitzMax** | Cross-platform |
| **Blitz3D** | 3D games |
| **Monkey X** | Modern cross-platform |

The Blitz family continues today.

**Vault entries:**
- `blitz-basic` - Software entry (major)
- `acid-software` - Company entry
- `worms-blitz` - Culture entry

---

## Part 7: STOS (Atari ST)

### STOS Basics

| Aspect | Notes |
|--------|-------|
| **Creator** | François Lionet (same as AMOS) |
| **Publisher** | Mandarin Software |
| **Released** | 1988 |
| **Platform** | Atari ST |

STOS was AMOS's predecessor/sibling.

### STOS Features

| Feature | Capability |
|---------|------------|
| **Sprites** | ST sprite handling |
| **Sound** | ST sound chip |
| **Screens** | Screen management |
| **Game commands** | Joystick, collision |

### STOS Games

| Game | Notes |
|------|-------|
| **Numerous PD titles** | Active community |
| **Magazine type-ins** | ST Format etc. |
| **Some commercial** | Smaller scale than AMOS |

**Vault entry:**
- `stos` - Software entry

---

## Part 8: Other Notable BASICs

### GFA BASIC (Atari ST)

| Aspect | Notes |
|--------|-------|
| **Type** | Structured BASIC |
| **Speed** | Fast, compiled |
| **Use** | Utilities, games, applications |

GFA BASIC was powerful but less game-focused than STOS.

### Locomotive BASIC (Amstrad CPC)

| Feature | Notes |
|---------|-------|
| **Built-in** | Standard CPC BASIC |
| **Quality** | Better than C64 BASIC |
| **Graphics** | Good commands |
| **Sound** | AY chip access |

Locomotive BASIC was reasonably capable for games.

### MSX-BASIC

| Version | Features |
|---------|----------|
| **MSX-BASIC 1.0** | Basic features |
| **MSX-BASIC 2.0** | Improved graphics |
| **MSX-BASIC 3.0** | MSX2+ features |

### Turbo-BASIC XL (Atari 8-bit)

| Feature | Notes |
|---------|-------|
| **Type** | Enhanced Atari BASIC |
| **Speed** | Much faster |
| **Structured** | Procedures |

### Applesoft BASIC (Apple II)

| Feature | Notes |
|---------|-------|
| **Built-in** | Standard Apple II BASIC |
| **Graphics** | HGR, HGR2 commands |
| **Limitations** | Slow, limited |

### Dragon BASIC

| Feature | Notes |
|---------|-------|
| **Type** | Microsoft BASIC variant |
| **Quality** | Reasonable |
| **Graphics** | PMODE commands |

**Vault entries:**
- `gfa-basic` - Software entry
- `locomotive-basic` - Software entry
- `turbo-basic-xl` - Software entry

---

## Part 9: BASIC Game Design Patterns

### What BASIC Games Could Do Well

| Genre | Suitability | Examples |
|-------|-------------|----------|
| **Text adventures** | Excellent | Many classics |
| **Puzzle games** | Good | Logic games |
| **Turn-based strategy** | Good | Wargames |
| **Simple arcade** | Moderate | With enhanced BASIC |
| **Management sims** | Good | Football Manager origins |
| **Educational** | Excellent | Many titles |

### What BASIC Struggled With

| Requirement | Problem |
|-------------|---------|
| **Fast action** | Interpretation overhead |
| **Many sprites** | Speed limitations |
| **Smooth scrolling** | Difficult in BASIC |
| **Complex AI** | Speed issues |

### The Hybrid Approach

Many games used:
- BASIC for game logic
- Assembly for speed-critical parts
- BASIC for development speed
- Assembly routines for graphics/sound

BBC BASIC excelled at this with its built-in assembler.

---

## Part 10: Curriculum Tracks

### Why BASIC Tracks Matter

| Reason | Benefit |
|--------|---------|
| **Lower barrier** | Easier than assembly |
| **Faster iteration** | Quick testing |
| **Focus on logic** | Less hardware detail |
| **Historical accuracy** | Many learned this way |
| **Progression** | Gateway to assembly |

### Proposed BASIC Curricula

| Platform | Track | Games | Notes |
|----------|-------|-------|-------|
| **C64** | BASIC Gateway | 8 | Stock BASIC V2 + PEEK/POKE |
| **Amiga** | AMOS Track | 8 | Full game development |
| **Amiga** | Blitz Track | 8 | More advanced |
| **BBC Micro** | BBC BASIC | 8-16 | Full curriculum possible |
| **Spectrum** | Sinclair BASIC | 4-8 | Gateway track |

### BASIC to Assembly Progression

| Stage | Focus |
|-------|-------|
| **1. Pure BASIC** | Logic, game design |
| **2. BASIC + peek/poke** | Understanding memory |
| **3. BASIC + assembly routines** | Speed-critical code |
| **4. Full assembly** | Complete control |

---

## Summary: New Vault Entries

| Category | Entries |
|----------|---------|
| **Software** | AMOS, Blitz, STOS, various BASICs | 15 |
| **People** | François Lionet | 1 |
| **Companies** | Acid Software | 1 |
| **Culture** | BASIC history, commercial BASIC games | 5 |

**Total new entries: ~22**

---

## Running Vault Total

| Previous | This Document | New Total |
|----------|---------------|-----------|
| ~1570 | +22 | **~1592 entries** |
