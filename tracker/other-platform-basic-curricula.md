# Other Platform BASIC Curricula

**Purpose:** Define BASIC curriculum tracks for BBC Micro, Spectrum, and other platforms with capable BASIC implementations.

**Last Updated:** 2026-01-18

---

## Part 1: BBC BASIC Track

### Why BBC BASIC Deserves a Full Track

BBC BASIC is arguably **the best 8-bit BASIC**:

| Feature | Benefit |
|---------|---------|
| **Structured** | PROC/FN, local variables |
| **Fast** | Well-optimised interpreter |
| **Graphics** | Comprehensive commands |
| **Sound** | ENVELOPE system |
| **Assembler** | Built-in inline assembly |

### Track Overview

| Aspect | Details |
|--------|---------|
| **Language** | BBC BASIC (standard) |
| **Platform** | BBC Micro / Master |
| **Games** | 8-16 |
| **Prerequisite** | None |
| **Unique value** | Best BASIC, educational heritage |

### Potential Game Sequence (8 games)

#### Game 1: Guess the Number
**"Mind Reader"**

| Concepts | Variables, input, conditionals |
|----------|-------------------------------|
| **Mode** | MODE 7 (teletext) |
| **Skills** | INPUT, IF/THEN/ELSE, PRINT |

#### Game 2: Hangman
**"Word Master"**

| Concepts | Strings, arrays, graphics |
|----------|---------------------------|
| **Mode** | MODE 4 or 7 |
| **Skills** | String handling, DRAW |

#### Game 3: Snake
**"Serpent"**

| Concepts | Movement, collision, game loop |
|----------|-------------------------------|
| **Mode** | MODE 5 (4 colours) |
| **Skills** | PLOT, POINT, INKEY$ |

#### Game 4: Breakout
**"Brick Basher"**

| Concepts | Physics, arrays, animation |
|----------|----------------------------|
| **Mode** | MODE 2 (8 colours) |
| **Skills** | Ball physics, MOVE/DRAW |

#### Game 5: Space Invaders
**"Alien Attack"**

| Concepts | Enemies, shooting, waves |
|----------|-------------------------|
| **Mode** | MODE 1 or 2 |
| **Skills** | VDU codes, user-defined characters |

**Note:** BBC BASIC can use VDU 23 to define custom characters.

#### Game 6: Platformer
**"Cave Jump"**

| Concepts | Gravity, platforms, scrolling |
|----------|------------------------------|
| **Mode** | MODE 2 or 5 |
| **Skills** | PROC/FN for organisation |

#### Game 7: Racing Game
**"Road Race"**

| Concepts | Pseudo-3D, obstacles, speed |
|----------|---------------------------|
| **Mode** | MODE 2 |
| **Skills** | Scaling, Mode 7 text overlays |

#### Game 8: Adventure
**"Quest"**

| Concepts | Rooms, inventory, puzzles |
|----------|--------------------------|
| **Mode** | Mixed modes |
| **Skills** | Complex state, save/load |

### BBC BASIC Code Example

```basic
10 REM SPACE INVADERS - BBC BASIC
20 MODE 2
30 VDU 23,224,24,24,60,126,255,90,36,0
40 PROCsetup
50 REPEAT
60   PROCmovePlayer
70   PROCmoveAliens
80   PROCmoveBullet
90   PROCcheckCollision
100  PROCdraw
110 UNTIL gameOver%
120 END
130
140 DEF PROCsetup
150   playerX%=640 : playerY%=950
160   LOCAL I%
170   DIM alienX%(10), alienY%(10)
180   FOR I%=1 TO 10
190     alienX%(I%)=I%*100 : alienY%(I%)=100
200   NEXT
210   gameOver%=FALSE
220 ENDPROC
```

Notice: **structured programming**, local variables, meaningful names.

### BBC BASIC to Assembly Bridge

BBC BASIC has a built-in assembler:

```basic
10 DIM code% 100
20 FOR pass%=0 TO 2 STEP 2
30   P%=code%
40   [OPT pass%
50   LDA #65
60   JSR &FFEE
70   RTS
80   ]
90 NEXT
100 CALL code%
```

Students can **mix BASIC and assembly** naturally.

### Unique Teaching Opportunities

| Feature | Teaching Value |
|---------|----------------|
| **MODE system** | Memory/colour tradeoffs |
| **ENVELOPE** | Sound synthesis |
| **Built-in assembler** | Gradual transition |
| **Teletext (MODE 7)** | Character-based graphics |
| **Structured syntax** | Good habits |

---

## Part 2: Spectrum BASIC Track

### Track Overview

| Aspect | Details |
|--------|---------|
| **Language** | Sinclair BASIC (+ Beta BASIC optional) |
| **Platform** | ZX Spectrum |
| **Games** | 8 |
| **Prerequisite** | None |
| **Purpose** | Complete game development curriculum |

### Why Spectrum BASIC Deserves 8 Games

| Reason | Notes |
|--------|-------|
| **Historical importance** | THE UK home computer |
| **Massive type-in culture** | Sinclair Programs, magazines full of BASIC |
| **Capable built-in commands** | PLOT, DRAW, CIRCLE, attributes |
| **Text adventure heritage** | Perfect for the genre |
| **Parity with C64** | Same gateway importance |
| **Faster than C64 BASIC** | Reasonably performant |

### Sinclair BASIC Features

| Strength | Notes |
|----------|-------|
| **Graphics commands** | PLOT, DRAW, CIRCLE built-in |
| **Attribute system** | INK, PAPER, BRIGHT, FLASH |
| **Reasonable speed** | Faster than C64 BASIC |
| **Huge library** | Hundreds of type-in games |
| **UDGs** | User Defined Graphics for sprites |

| Limitation | Notes |
|------------|-------|
| **No procedures** | Subroutines only (GOSUB) |
| **Limited sound** | BEEP command only |
| **Attribute clash** | Colour limitations (but teachable!) |

### Game Sequence (8 games)

#### Game 1: Number Guess
**"Think of a Number"**

| Aspect | Details |
|--------|---------|
| **Units** | 4 |
| **Concepts** | Variables, input, conditionals, loops |
| **Skills** | INPUT, PRINT, IF/THEN, RND |

#### Game 2: Text Adventure
**"The Cursed Manor"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Concepts** | Strings, arrays, DATA, parsing |
| **Skills** | String handling, room structure |

Text adventures were HUGE on Spectrum - this is historically authentic.

#### Game 3: Maze Game
**"Lost in the Labyrinth"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Concepts** | Movement, screen drawing, collision |
| **Skills** | PLOT, DRAW, INKEY$, ATTR |

#### Game 4: Breakout
**"Block Breaker"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Concepts** | Physics, arrays, animation |
| **Skills** | Ball movement, brick arrays |

#### Game 5: Snake
**"Spectrum Serpent"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Concepts** | Growth, collision, speed |
| **Skills** | PRINT AT, screen reading |

#### Game 6: Space Shooter
**"Starfire"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Concepts** | UDGs, shooting, waves |
| **Skills** | User-defined graphics, collision |

**UDG Introduction:** This game teaches custom character graphics.

#### Game 7: Platform Game
**"Miner Mick"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Concepts** | Gravity, platforms, collectibles |
| **Skills** | Physics, level design |

Homage to Manic Miner - which defined Spectrum gaming.

#### Game 8: Puzzle Adventure
**"The Crystal Quest"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Concepts** | Inventory, puzzles, multiple screens |
| **Skills** | State management, complex logic |

**Capstone:** Combines everything - text, graphics, logic, state.

### Spectrum BASIC Code Example

```basic
10 REM SIMPLE SHOOTER
20 LET px=128: LET py=170
30 FOR n=0 TO 7: READ a: POKE USR "a"+n,a: NEXT n
40 DATA 24,60,126,255,255,90,36,102

100 REM MAIN LOOP
110 LET k$=INKEY$
120 IF k$="o" AND px>8 THEN LET px=px-4
130 IF k$="p" AND px<248 THEN LET px=px+4
140 PRINT AT 21,px/8; CHR$ 144
150 GO TO 110
```

### User Defined Graphics (UDGs)

Spectrum BASIC can redefine characters:
```basic
FOR n=0 TO 7
  READ a
  POKE USR "a"+n,a
NEXT n
DATA 24,60,126,255,255,90,36,102
```

This creates simple "sprites" - essential for Spectrum BASIC games.

### Enhanced Spectrum BASIC

| Extension | Features |
|-----------|----------|
| **Beta BASIC** | Procedures, toolkit |
| **Laser BASIC** | Sprites, scrolling |

Consider allowing Beta BASIC for more advanced games.

---

## Part 3: Amstrad CPC Locomotive BASIC

### Track Overview

| Aspect | Details |
|--------|---------|
| **Language** | Locomotive BASIC |
| **Platform** | Amstrad CPC |
| **Games** | 4-8 |
| **Unique value** | Better than C64, good graphics |

### Locomotive BASIC Features

| Feature | Capability |
|---------|------------|
| **Graphics** | MODE 0/1/2, PLOT, DRAW |
| **Sound** | SOUND command (AY chip) |
| **Sprites** | TAG, SYMBOL AFTER |
| **Speed** | Reasonable |

### Code Example

```basic
10 MODE 1
20 INK 0,0:INK 1,26:INK 2,6:INK 3,18
30 BORDER 0
40 SYMBOL AFTER 240
50 SYMBOL 240,24,60,126,255,255,90,36,102
60 x=160:y=100
70 WHILE 1
80   IF INKEY(8)=0 AND x>10 THEN x=x-2
90   IF INKEY(1)=0 AND x<300 THEN x=x+2
100  TAG
110  MOVE x,y:PRINT CHR$(240);
120  TAGOFF
130  CALL &BD19:REM Wait vsync
140 WEND
```

### Potential Games

Similar progression to Spectrum:
1. Number guess
2. Maze/adventure
3. Breakout
4. Shooter

---

## Part 4: STOS (Atari ST)

### Track Overview

| Aspect | Details |
|--------|---------|
| **Language** | STOS Basic |
| **Platform** | Atari ST |
| **Games** | 8 |
| **Creator** | François Lionet (same as AMOS) |

### STOS Features

| Feature | Capability |
|---------|------------|
| **Sprites** | ST sprite handling |
| **Sound** | YM2149 chip |
| **Screens** | Multiple screens |
| **Game commands** | Collision, joystick |

### STOS vs AMOS

| Aspect | STOS | AMOS |
|--------|------|------|
| **Platform** | Atari ST | Amiga |
| **Sprites** | Software | Hardware + bobs |
| **Sound** | YM chip | Paula samples |
| **Community** | Smaller | Larger |

### Potential STOS Curriculum

Mirror the AMOS track with ST-specific adaptations:
1. Target practice
2. Maze game
3. Breakout
4. Shooter
5. Platformer
6. Puzzle
7. Racing
8. Adventure

---

## Part 5: Other Capable BASICs

### GFA BASIC (Atari ST)

| Aspect | Notes |
|--------|-------|
| **Type** | Structured, compiled |
| **Use** | Applications and games |
| **Speed** | Fast |
| **Best for** | Programmers wanting structure |

Not as game-focused as STOS, but more powerful.

### MSX-BASIC

| Version | Features |
|---------|----------|
| **MSX-BASIC 1.0** | Basic features, sprites |
| **MSX-BASIC 2.0** | Better graphics, improved |

MSX has hardware sprites accessible from BASIC:
```basic
10 SCREEN 2
20 SPRITE$(0)="..." ' Define sprite pattern
30 PUT SPRITE 0,(100,100),15,0
```

### Turbo-BASIC XL (Atari 8-bit)

| Feature | Notes |
|---------|-------|
| **Speed** | Much faster than Atari BASIC |
| **Structured** | Procedures, REPEAT/UNTIL |
| **Graphics** | Good Atari graphics access |

---

## Part 6: Curriculum Summary

### Full BASIC Tracks Recommended

| Platform | Language | Games | Priority |
|----------|----------|-------|----------|
| **C64** | Stock BASIC V2 | 8 | High (gateway) |
| **Spectrum** | Sinclair BASIC | 8 | High (UK heritage) |
| **Amiga** | AMOS | 8 | High |
| **Amiga** | Blitz Basic | 8 | High |
| **BBC Micro** | BBC BASIC | 8-16 | High (best BASIC) |

### Gateway BASIC Tracks

| Platform | Language | Games | Priority |
|----------|----------|-------|----------|
| **Spectrum** | Sinclair BASIC | 8 | High |
| **Amstrad CPC** | Locomotive BASIC | 4-8 | Medium |
| **Atari ST** | STOS | 8 | Medium |
| **MSX** | MSX-BASIC | 4-8 | Medium |

### BASIC Quality Ranking

| Tier | Languages |
|------|-----------|
| **Excellent** | BBC BASIC, AMOS, Blitz Basic |
| **Good** | STOS, Locomotive BASIC, Turbo-BASIC XL |
| **Adequate** | Sinclair BASIC, MSX-BASIC |
| **Poor** | C64 BASIC V2, AmigaBASIC |

---

## Part 7: Teaching Philosophy

### BASIC as Complete Curriculum

BASIC tracks are **not** stepping stones to assembly - they are complete curricula in their own right.

| Evidence | Details |
|----------|---------|
| **Worms** | Made in Blitz Basic - one of gaming's biggest franchises |
| **Ultimate Soccer Manager** | Commercial AMOS release |
| **Skidmarks** | Commercial Blitz Basic release |
| **Countless BBC games** | Professional releases in BBC BASIC |
| **Magazine libraries** | Thousands of playable BASIC games |

### Why BASIC?

| Reason | Benefit |
|--------|---------|
| **Immediate results** | Type and run |
| **Focus on logic** | Game design, not hardware registers |
| **Rapid iteration** | Quick testing cycle |
| **Historical authenticity** | This is how people learned |
| **Commercially proven** | Real games shipped in BASIC |
| **Complete solution** | No need to "graduate" to assembly |

### BASIC vs Assembly: Different Goals

| BASIC Track | Assembly Track |
|-------------|----------------|
| Game design focus | Hardware mastery |
| Faster development | Maximum performance |
| Higher-level thinking | Low-level understanding |
| Equally valid | Equally valid |

**Neither is "better" - they serve different goals.**

### Optional Assembly Transition

Some students may *choose* to explore assembly:
- Curiosity about hardware
- Performance requirements
- Interest in low-level programming
- Want to understand "how it really works"

This is optional, not required. A complete BASIC curriculum produces real games.

---

## Summary

### BASIC is Legitimate

BASIC tracks aren't "lesser" - they're:
- **Historical** - How people actually learned
- **Practical** - Real games were made
- **Educational** - Focus on concepts
- **Accessible** - Lower barrier
- **Sufficient** - AMOS/Blitz prove commercial viability

### Recommended Implementation

1. **C64 BASIC Gateway** - 8 games before assembly
2. **AMOS Track** - Full Amiga curriculum in BASIC
3. **Blitz Track** - Performance-focused Amiga
4. **BBC BASIC Track** - Best 8-bit BASIC, full curriculum
5. **Gateway tracks** - Spectrum, CPC, others (4 games each)

---

## Vault Entries

| Entry | Type |
|-------|------|
| `bbc-basic-curriculum` | Curriculum |
| `spectrum-basic-curriculum` | Curriculum |
| `locomotive-basic` | Software |
| `stos-curriculum` | Curriculum |
| `basic-curricula` | Culture |

**New entries: 5**
