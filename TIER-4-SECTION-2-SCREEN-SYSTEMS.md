# Tier 4 Section 2: Screen Systems (Lessons 53-56)

**Section Theme:** "Professional Presentation"
**Core Skill:** Game flow and user interface

---

## Section 2 Overview

Data systems (Section 1) manage game state. Screen systems manage how players **experience** that state. This section teaches the structure of professional games: title screens, state machines, menus, and UI.

**Why This Matters:**
- First impressions matter (title screens)
- Game flow prevents spaghetti code (state machines)
- Players need interfaces (menus, save/load UI)
- Polish separates amateur from professional

**Reality Check:** Modern game engines (Unity, Unreal) use the EXACT same concepts: scenes, state machines, UI systems. Learning this in BASIC gives you the vocabulary for any platform.

---

## Lesson 53: Title Screen

**Concept:** Attract mode with logo, animation, music
**WOW Moment:** Professional-looking title screen that rivals commercial games
**Difficulty:** ⭐⭐⭐ (coordinates graphics, sound, input

)

### The Problem

Amateur games:
```basic
100 PRINT CHR$(147);"SUPER GAME"
110 PRINT"PRESS FIRE TO START"
120 IF JOY<>16 THEN 120
130 GOSUB 1000: REM Start game
```

**This works, but it's boring.** Commercial games have:
- Large logo (custom graphics)
- Animated elements (sprites, colors)
- Background music
- "Press FIRE" blinking prompt
- Copyright/credits
- Timeout to attract mode or instructions

### Technical Details: Title Screen Architecture

**Components:**
1. **Logo display** (character graphics or sprites)
2. **Animation loop** (sprites bouncing, colors cycling)
3. **Music playback** (SID background music)
4. **Input detection** (fire button with debounce)
5. **Attract mode** (timeout to demo or instructions)

### Example 1: Static Title with Custom Charset

```basic
10 REM ═══════════════════════════════════════
20 REM Static Title Screen
30 REM ═══════════════════════════════════════
40 REM
100 REM Setup screen
110 POKE 53280,0: REM Black border
120 POKE 53281,0: REM Black background
130 REM
140 REM Load custom character set (if available)
150 REM This example uses built-in charset
160 REM
200 REM Draw title using block graphics
210 PRINT CHR$(147): REM Clear screen
220 PRINT TAB(10);"╔═══════════════╗"
230 PRINT TAB(10);"║               ║"
240 PRINT TAB(10);"║  SUPER QUEST  ║"
250 PRINT TAB(10);"║               ║"
260 PRINT TAB(10);"╚═══════════════╝"
270 REM
300 REM Display menu
310 FOR I=1 TO 5:PRINT:NEXT: REM Spacing
320 PRINT TAB(12);"PRESS FIRE"
330 PRINT
340 PRINT TAB(12);"TO START"
350 REM
400 REM Copyright
410 PRINT:PRINT TAB(8);"© 2024 YOUR NAME"
420 REM
500 REM Wait for fire button
510 JOY=PEEK(56320): REM Read joystick port 2
520 IF (JOY AND 16)=0 THEN 600: REM Fire pressed
530 FOR I=1 TO 10:NEXT: REM Short delay
540 GOTO 510
550 REM
600 REM Start game
610 PRINT CHR$(147);"STARTING..."
620 FOR I=1 TO 500:NEXT
630 RETURN: REM Would jump to game
```

### Example 2: Animated Title with Sprites

```basic
10 REM ═══════════════════════════════════════
20 REM Animated Title Screen with Sprites
30 REM ═══════════════════════════════════════
40 REM
100 REM Setup screen
110 POKE 53280,6: REM Blue border
120 POKE 53281,14: REM Light blue background
130 REM
140 REM Load sprite data
150 FOR I=0 TO 62
160 READ B:POKE 832+I,B
170 NEXT
180 REM
200 REM Setup 2 sprites
210 POKE 2040,13:POKE 2041,13: REM Sprite pointers
220 POKE 53287,7:POKE 53288,10: REM Colors (yellow, red)
230 POKE 53269,3: REM Enable sprites 0 and 1
240 REM
250 REM Initial positions and velocities
260 X1=100:Y1=100:VX1=2:VY1=1
270 X2=200:Y2=150:VX2=-2:VY2=-1
280 REM
300 REM Display title text
310 PRINT CHR$(147)
320 FOR I=1 TO 5:PRINT:NEXT
330 PRINT TAB(8);"═══════════════════"
340 PRINT TAB(8);"   CRYSTAL QUEST   "
350 PRINT TAB(8);"═══════════════════"
360 REM
400 REM Blinking "PRESS FIRE" flag
410 BL=0:BT=0
420 REM
500 REM ═══════════════════════════════════════
510 REM Main title loop
520 REM ═══════════════════════════════════════
530 REM Update sprite 1
540 X1=X1+VX1:Y1=Y1+VY1
550 IF X1<24 OR X1>320 THEN VX1=-VX1:X1=X1+VX1
560 IF Y1<50 OR Y1>230 THEN VY1=-VY1:Y1=Y1+VY1
570 POKE 53248,X1:POKE 53249,Y1
580 REM
590 REM Update sprite 2
600 X2=X2+VX2:Y2=Y2+VY2
610 IF X2<24 OR X2>320 THEN VX2=-VX2:X2=X2+VX2
620 IF Y2<50 OR Y2>230 THEN VY2=-VY2:Y2=Y2+VY2
630 POKE 53250,X2:POKE 53251,Y2
640 REM
650 REM Blinking text
660 BT=BT+1
670 IF BT>20 THEN BL=1-BL:BT=0: REM Toggle every 20 frames
680 IF BL=1 THEN POKE 1024+880,32: REM Clear text (space)
690 IF BL=0 THEN PRINT TAB(13);"PRESS FIRE";: REM Show text
700 REM
710 REM Check for fire button
720 JOY=PEEK(56320)
730 IF (JOY AND 16)=0 THEN 800: REM Fire pressed
740 REM
750 REM Small delay
760 FOR D=1 TO 10:NEXT D
770 GOTO 530: REM Loop
780 REM
800 REM Start game
810 POKE 53269,0: REM Disable sprites
820 PRINT CHR$(147);"LOADING..."
830 FOR I=1 TO 1000:NEXT
840 RETURN
850 REM
1000 REM Sprite data (star/crystal shape)
1010 DATA 0,24,0,0,60,0,0,126,0
1020 DATA 0,255,0,1,255,128,3,255,192
1030 DATA 7,255,224,15,255,240,31,255,248
1040 DATA 3,255,192,3,255,192,3,255,192
1050 DATA 3,255,192,3,255,192,3,255,192
1060 DATA 1,255,128,0,255,0,0,126,0
1070 DATA 0,60,0,0,24,0,0,0,0
```

### Example 3: Title with Attract Mode Timeout

```basic
10 REM ═══════════════════════════════════════
20 REM Title Screen with Attract Mode
30 REM ═══════════════════════════════════════
40 REM
100 REM Setup
110 POKE 53280,0:POKE 53281,0
120 TM=0: REM Timeout counter
130 REM
200 REM Display title
210 PRINT CHR$(147)
220 FOR I=1 TO 6:PRINT:NEXT
230 PRINT TAB(10);"╔═══════════════╗"
240 PRINT TAB(10);"║  SPACE RAID   ║"
250 PRINT TAB(10);"╚═══════════════╝"
260 PRINT:PRINT TAB(12);"PRESS FIRE"
270 REM
500 REM Main loop
510 JOY=PEEK(56320)
520 IF (JOY AND 16)=0 THEN 700: REM Fire pressed → start game
530 REM
540 REM Increment timeout
550 TM=TM+1
560 IF TM>300 THEN 800: REM ~5 seconds (60 fps) → attract mode
570 REM
580 REM Small delay
590 FOR D=1 TO 10:NEXT D
600 GOTO 510
610 REM
700 REM Start game
710 PRINT CHR$(147);"STARTING GAME..."
720 FOR I=1 TO 1000:NEXT
730 RETURN
740 REM
800 REM Attract mode (show instructions or demo)
810 PRINT CHR$(147)
820 PRINT "HOW TO PLAY"
830 PRINT "==========="
840 PRINT
850 PRINT "USE JOYSTICK TO MOVE"
860 PRINT "FIRE TO SHOOT"
870 PRINT
880 PRINT "PRESS FIRE TO START"
890 REM
900 REM Wait for fire
910 JOY=PEEK(56320)
920 IF (JOY AND 16)=0 THEN 700
930 FOR D=1 TO 10:NEXT D
940 GOTO 910
```

### Common Mistakes to Address

**Mistake 1: No debounce on fire button**
```basic
500 IF PEEK(56320) AND 16=0 THEN GOSUB 1000: REM Starts game immediately!
510 GOTO 500: REM Player can't release button in time → multiple starts
```
**Fix:** Wait for button release before accepting next press, or add delay after press.

**Mistake 2: Tight loop blocks music**
```basic
100 IF PEEK(56320) AND 16=0 THEN 200: REM Tight check
110 GOTO 100: REM Music can't play (no cycles for SID updates)
```
**Fix:** Add delay in loop (`FOR I=1 TO 10:NEXT`) to give SID time to generate sound.

**Mistake 3: Forgetting to disable sprites after title**
```basic
100 POKE 53269,3: REM Enable sprites for title
...
200 REM Start game without disabling sprites
210 GOSUB 5000: REM Game code → sprites still visible from title!
```
**Fix:** `POKE 53269,0` before exiting title screen.

**Mistake 4: Hardcoded screen positions break on PETSC

II**
```basic
100 PRINT TAB(10);"TITLE": REM Looks good with one font
110 REM But if you change charset, TAB positions shift!
```
**Fix:** Calculate center positions based on screen width (40 columns).

### Game Context: How Professionals Used This

**Impossible Mission (1984):**
- Voice sample plays on title: "Another visitor! Stay a while..."
- Logo fills screen with custom graphics
- No music, but dramatic voice sets tone
- "Press fire" prompt after voice finishes

**The Last Ninja (1987):**
- Stunning title screen with large ninja sprite
- Custom font for title text
- SID music plays immediately (iconic tune)
- Animated stars/particles in background
- Fade transition to menu

**Bubble Bobble (1987 C64 port):**
- Cute animated logo with bouncing letters
- Characters demo the gameplay
- High score displayed on title
- Coin-op style "Insert Coin" prompt (adapted to "Press Fire")

### Progression Notes

**Builds on:**
- L18-19: Sprites (animated elements)
- L23: SID music (background audio)
- L7-8: Colors and screen control

**Leads to:**
- L54: Game states (title is state #1)
- L55: Menu system (next screen after title)
- L57: Transitions (fade from title to game)

### Why It Matters

**Short-term:** Your game now has a professional presentation. Players take it seriously.

**Long-term:** Title screens teach you about:
- Sequencing (load assets → display → wait for input → transition)
- Animation loops (update, render, repeat)
- Event handling (input detection)
- Attention to detail (blinking text, attract modes)

These concepts scale up: web page splash screens, app launch screens, game main menus.

### Reality Check

**What BASIC Does Well:**
- Simple text-based titles are easy
- PETSCII graphics can look retro-cool
- Sprite animation is straightforward
- Fire button detection is one PEEK

**What BASIC Struggles With:**
- Custom fonts require charset switching (complex)
- Smooth fades require timing (hard to get right)
- Complex animations slow down music playback
- Large graphics eat memory

**Assembly Advantage:**
- Can load compressed title graphics
- Raster interrupt for stable music during animation
- Smooth fades with precise timing
- Can pack more into memory

**Verdict:** For simple/medium titles, BASIC is fine. For magazine-cover stunning titles (The Last Ninja), you need assembly.

---

## Lesson 54: Game States

**Concept:** State machine for game flow control
**WOW Moment:** Clean architecture that handles title → menu → game → pause → game over flow
**Difficulty:** ⭐⭐⭐⭐ (introduces fundamental CS concept)

### The Problem

Spaghetti code without state management:
```basic
100 GOSUB 1000: REM Title
110 GOSUB 2000: REM Game
120 IF LIVES=0 THEN GOSUB 3000: REM Game over
130 IF PAUSED=1 THEN GOSUB 4000: REM Pause
140 GOTO 110: REM Chaos!
```

**Problems:**
- Hard to read flow
- Easy to introduce bugs (what if pause happens during game over?)
- Can't easily add new screens
- No clear "which screen am I on?"

### The Solution: State Machine

**A state machine has:**
- Current state variable (S)
- States are numbered (1=TITLE, 2=MENU, 3=GAME, etc.)
- Main loop dispatches to state handler
- States transition cleanly (S=2 changes state)

**Benefits:**
- Clear flow (always know current state)
- Easy to add states (just add handler)
- Prevents invalid combinations (can't be in title AND game simultaneously)
- Professional architecture

### Complete State Machine Example

```basic
10 REM ═══════════════════════════════════════
20 REM Game State Machine
30 REM ═══════════════════════════════════════
40 REM
50 REM States:
60 REM 1 = Title screen
70 REM 2 = Main menu
80 REM 3 = Playing game
90 REM 4 = Paused
100 REM 5 = Game over
110 REM 6 = High score entry
120 REM
200 REM Initialize game variables
210 SCORE=0:LIVES=3:LEVEL=1
220 REM
300 REM Set initial state
310 S=1: REM Start at title
320 REM
400 REM ═══════════════════════════════════════
410 REM Main state machine loop
420 REM ═══════════════════════════════════════
430 ON S GOSUB 1000,2000,3000,4000,5000,6000
440 GOTO 430: REM Loop forever
450 REM
1000 REM ═══════════════════════════════════════
1010 REM State 1: Title screen
1020 REM ═══════════════════════════════════════
1030 PRINT CHR$(147)
1040 PRINT:PRINT TAB(12);"SUPER QUEST"
1050 PRINT:PRINT TAB(12);"PRESS FIRE"
1060 REM
1070 JOY=PEEK(56320)
1080 IF (JOY AND 16)=0 THEN S=2: REM Fire → go to menu
1090 FOR D=1 TO 10:NEXT D
1100 RETURN
1110 REM
2000 REM ═══════════════════════════════════════
2010 REM State 2: Main menu
2020 REM ═══════════════════════════════════════
2030 PRINT CHR$(147)
2040 PRINT "MAIN MENU"
2050 PRINT "========="
2060 PRINT
2070 PRINT "1. START GAME"
2080 PRINT "2. HIGH SCORES"
2090 PRINT "3. QUIT"
2100 PRINT
2110 GET K$:IF K$="" THEN 2110
2120 IF K$="1" THEN S=3: REM Start game
2130 IF K$="2" THEN PRINT "HIGH SCORES...":FOR I=1 TO 1000:NEXT:REM Stay in menu
2140 IF K$="3" THEN END
2150 RETURN
2160 REM
3000 REM ═══════════════════════════════════════
3010 REM State 3: Playing game
3020 REM ═══════════════════════════════════════
3030 PRINT CHR$(147)
3040 PRINT "LEVEL:";LEVEL;" SCORE:";SCORE;" LIVES:";LIVES
3050 PRINT
3060 PRINT "GAME IS RUNNING..."
3070 PRINT "(PRESS P TO PAUSE, Q TO QUIT)"
3080 REM
3090 REM Simulate gameplay
3100 SCORE=SCORE+10
3110 REM
3120 REM Check for pause
3130 GET K$
3140 IF K$="P" THEN S=4:RETURN: REM Go to pause state
3150 IF K$="Q" THEN S=2:RETURN: REM Quit to menu
3160 REM
3170 REM Check for game over condition
3180 IF SCORE>1000 THEN LIVES=LIVES-1: REM Lose life after 1000 pts (demo)
3190 IF LIVES<=0 THEN S=5:RETURN: REM Go to game over
3200 REM
3210 FOR D=1 TO 50:NEXT D: REM Slow down game loop
3220 RETURN
3230 REM
4000 REM ═══════════════════════════════════════
4010 REM State 4: Paused
4020 REM ═══════════════════════════════════════
4030 PRINT CHR$(147)
4040 PRINT:PRINT TAB(14);"PAUSED"
4050 PRINT:PRINT TAB(10);"PRESS P TO RESUME"
4060 REM
4070 GET K$
4080 IF K$="P" THEN S=3: REM Resume game
4090 FOR D=1 TO 10:NEXT D
4100 RETURN
4110 REM
5000 REM ═══════════════════════════════════════
5010 REM State 5: Game over
5020 REM ═══════════════════════════════════════
5030 PRINT CHR$(147)
5040 PRINT:PRINT TAB(12);"GAME OVER"
5050 PRINT:PRINT TAB(10);"FINAL SCORE:";SCORE
5060 PRINT:PRINT TAB(9);"PRESS FIRE TO CONTINUE"
5070 REM
5080 JOY=PEEK(56320)
5090 IF (JOY AND 16)=0 THEN S=6: REM Fire → high score entry
5100 FOR D=1 TO 10:NEXT D
5110 RETURN
5120 REM
6000 REM ═══════════════════════════════════════
6010 REM State 6: High score entry
6020 REM ═══════════════════════════════════════
6030 PRINT CHR$(147)
6040 PRINT "HIGH SCORE ENTRY"
6050 PRINT "================"
6060 PRINT
6070 INPUT "ENTER YOUR NAME";NM$
6080 PRINT "SAVING SCORE..."
6090 FOR I=1 TO 1000:NEXT
6100 REM
6110 REM Return to menu
6120 S=2
6130 RETURN
```

### State Transition Diagram

```
[TITLE] → (fire) → [MENU]
                       ↓
         (1)──→ [GAME] ←──(resume)── [PAUSE]
                  ↓                      ↑
              (p press)                  │
                  └──────────────────────┘
                  ↓
             (lives=0)
                  ↓
            [GAME OVER] → (fire) → [HIGH SCORE] → [MENU]
```

### Extended Example: State Machine with Entry/Exit Actions

```basic
400 REM Main loop with entry/exit actions
410 REM
420 REM Check if state changed
430 IF S<>OS THEN GOSUB 9000: REM State changed, handle transition
440 REM
450 REM Execute current state
460 ON S GOSUB 1000,2000,3000,4000,5000,6000
470 REM
480 GOTO 420
...
9000 REM ═══════════════════════════════════════
9010 REM Handle state transitions
9020 REM OS = old state, S = new state
9030 REM ═══════════════════════════════════════
9040 REM Exit old state
9050 IF OS=3 THEN GOSUB 9500: REM Exiting game state
9060 REM
9070 REM Enter new state
9080 IF S=3 THEN GOSUB 9700: REM Entering game state
9090 REM
9100 REM Update old state
9110 OS=S
9120 RETURN
9130 REM
9500 REM Exit game state (cleanup)
9510 POKE 53269,0: REM Disable sprites
9520 POKE 54296,0: REM Silence SID
9530 RETURN
9540 REM
9700 REM Enter game state (setup)
9710 GOSUB 8000: REM Load sprites
9720 GOSUB 8100: REM Start music
9730 RETURN
```

### Common Mistakes to Address

**Mistake 1: Modifying state inside state handler without RETURN**
```basic
3000 REM Game state
3010 IF LIVES=0 THEN S=5: REM Change to game over
3020 SCORE=SCORE+10: REM Still executing game code! Bug!
3030 RETURN
```
**Fix:** RETURN immediately after changing state:
```basic
3010 IF LIVES=0 THEN S=5:RETURN
```

**Mistake 2: Forgetting to handle all states in ON...GOSUB**
```basic
100 ON S GOSUB 1000,2000,3000: REM Only 3 states
110 S=4: REM Oops! No handler for state 4 → crashes
```
**Fix:** Always have handler for each state, even if it's empty.

**Mistake 3: States doing too much**
```basic
3000 REM Game state
3010 REM ... 500 lines of game logic ...
3510 RETURN
```
**Fix:** State handlers should be **dispatch points**, not implementations. Call subroutines:
```basic
3000 REM Game state
3010 GOSUB 7000: REM Update player
3020 GOSUB 7100: REM Update enemies
3030 GOSUB 7200: REM Check collisions
3040 GOSUB 7300: REM Render
3050 RETURN
```

**Mistake 4: No way to exit infinite loop**
```basic
400 ON S GOSUB 1000,2000,3000
410 GOTO 400: REM Loops forever, no END state
```
**Fix:** Add exit state (S=0 → END) or allow states to set flag.

### Game Context: How Professionals Used This

**Archon (1984):**
- States: Title, Character Select, Board View, Battle Mode, Game Over
- Clean transitions between board game and arcade battle
- Each state has distinct controls and graphics

**M.U.L.E. (1983):**
- States: Setup, Land Auction, Production, Store, Results
- Turn-based state machine
- Each phase has timer and specific UI

**Elite (1984 C64 port):**
- States: Title, Ship View, Planet View, Market, Equipment, Combat
- Seamless transitions between states
- Each state loads different graphics/data

### Progression Notes

**Builds on:**
- L53: Title screen (first state)
- L6: GOSUB/RETURN (state dispatch)
- L5: Variables (state tracking)

**Leads to:**
- L55: Menu system (menu state handler)
- L56: Save/Load UI (additional states)
- L64: Complete game (full state machine)

### Why It Matters

**Short-term:** Your code is now maintainable and extensible. Adding features is straightforward.

**Long-term:** State machines are EVERYWHERE:
- Game engines (Unity: SceneManager, Unreal: Level Streaming)
- UI frameworks (React: component state, finite state machines)
- Network protocols (TCP states: LISTEN, SYN_SENT, ESTABLISHED, etc.)
- Hardware (CPU instruction states, USB device states)

Understanding state machines makes you a better programmer in ANY language.

### Reality Check

**What BASIC Does Well:**
- `ON...GOSUB` is perfect for state dispatch
- Simple integer state IDs
- Easy to visualize flow

**What BASIC Struggles With:**
- No enums (must use magic numbers: 1, 2, 3...)
- No function pointers (can't have state tables)
- Complex state transitions require manual management

**Assembly Advantage:**
- Jump tables for faster dispatch
- More states (BASIC's ON...GOSUB limited to ~15)

**Verdict:** For typical games (5-10 states), BASIC state machines are perfect. The concept matters more than the implementation speed.

---

*[Continuing with Lessons 55-56 in the same detailed style...]*

## Lesson 55: Menu System

**Concept:** Navigable menus with cursor and selection
**WOW Moment:** Professional menu system with joystick/keyboard navigation
**Difficulty:** ⭐⭐⭐⭐ (cursor movement, input handling, nested menus)

### The Problem

Simple text menus require typing:
```basic
100 PRINT "1. START"
110 PRINT "2. OPTIONS"
120 INPUT "CHOICE";C$
```

**Problems:**
- Must type number (error-prone)
- No visual feedback
- Can't use joystick
- Doesn't feel like a game

**Solution:** Cursor-based menu with directional navigation.

### Technical Details: Menu System Architecture

**Components:**
1. **Menu items array** (`M$()` - option strings)
2. **Cursor position** (`C` - which item is selected)
3. **Input handler** (joystick up/down, fire to select)
4. **Display routine** (draw menu with highlight)
5. **Action dispatcher** (execute selected option)

### Complete Menu System

```basic
10 REM ═══════════════════════════════════════
20 REM Menu System with Cursor
30 REM ═══════════════════════════════════════
40 REM
100 REM Define menu options
110 DIM M$(5): REM 5 menu items
120 M$(1)="START GAME"
130 M$(2)="LOAD GAME"
140 M$(3)="OPTIONS"
150 M$(4)="HIGH SCORES"
160 M$(5)="QUIT"
170 MI=5: REM Menu item count
180 REM
200 REM Initialize cursor position
210 C=1: REM Start at first item
220 REM
300 REM ═══════════════════════════════════════
310 REM Main menu loop
320 REM ═══════════════════════════════════════
330 GOSUB 1000: REM Display menu
340 GOSUB 2000: REM Handle input
350 IF SEL=1 THEN GOSUB 3000: REM Execute selection
360 GOTO 330: REM Loop
370 REM
1000 REM ═══════════════════════════════════════
1010 REM Display menu
1020 REM ═══════════════════════════════════════
1030 PRINT CHR$(147): REM Clear screen
1040 PRINT:PRINT TAB(12);"MAIN MENU"
1050 PRINT TAB(12);"========="
1060 PRINT
1070 REM
1080 REM Draw menu items
1090 FOR I=1 TO MI
1100 PRINT TAB(10);
1110 REM Highlight current selection
1120 IF I=C THEN PRINT CHR$(18);: REM Reverse on
1130 PRINT M$(I);
1140 IF I=C THEN PRINT CHR$(146);: REM Reverse off
1150 PRINT
1160 NEXT I
1170 RETURN
1180 REM
2000 REM ═══════════════════════════════════════
2010 REM Handle input
2020 REM Output: SEL=1 if selection made
2030 REM ═══════════════════════════════════════
2040 SEL=0: REM No selection yet
2050 REM
2060 REM Read joystick
2070 JOY=PEEK(56320)
2080 REM
2090 REM Check up (bit 0)
2100 IF (JOY AND 1)=0 THEN C=C-1:IF C<1 THEN C=MI:REM Wrap to bottom
2110 REM
2120 REM Check down (bit 1)
2130 IF (JOY AND 2)=0 THEN C=C+1:IF C>MI THEN C=1:REM Wrap to top
2140 REM
2150 REM Check fire (bit 4)
2160 IF (JOY AND 16)=0 THEN SEL=1: REM Selection made
2170 REM
2180 REM Delay to prevent rapid scrolling
2190 FOR D=1 TO 100:NEXT D
2200 RETURN
2210 REM
3000 REM ═══════════════════════════════════════
3010 REM Execute selection
3020 REM ═══════════════════════════════════════
3030 PRINT CHR$(147)
3040 ON C GOSUB 3100,3200,3300,3400,3500
3050 REM Wait before returning to menu
3060 PRINT:PRINT "PRESS FIRE TO CONTINUE"
3070 JOY=PEEK(56320)
3080 IF (JOY AND 16)=0 THEN RETURN
3090 GOTO 3070
3100 REM START GAME
3110 PRINT "STARTING GAME..."
3120 FOR I=1 TO 1000:NEXT
3130 RETURN
3140 REM
3200 REM LOAD GAME
3210 PRINT "LOAD GAME SELECTED"
3220 FOR I=1 TO 1000:NEXT
3230 RETURN
3240 REM
3300 REM OPTIONS
3310 PRINT "OPTIONS MENU"
3320 FOR I=1 TO 1000:NEXT
3330 RETURN
3340 REM
3400 REM HIGH SCORES
3410 PRINT "HIGH SCORES"
3420 FOR I=1 TO 1000:NEXT
3430 RETURN
3440 REM
3500 REM QUIT
3510 PRINT "GOODBYE!"
3520 FOR I=1 TO 1000:NEXT
3530 END
```

### Extended Example: Nested Menus

```basic
10 REM Nested menu system
20 REM ML = Menu Level (1=main, 2=submenu)
30 REM
100 ML=1: REM Start at main menu
110 REM
200 REM Main loop
210 IF ML=1 THEN GOSUB 1000: REM Main menu
220 IF ML=2 THEN GOSUB 2000: REM Submenu
230 GOTO 210
...
2000 REM ═══════════════════════════════════════
2010 REM Options submenu
2020 REM ═══════════════════════════════════════
2030 DIM SM$(4)
2040 SM$(1)="DIFFICULTY: EASY"
2050 SM$(2)="MUSIC: ON"
2060 SM$(3)="SOUND FX: ON"
2070 SM$(4)="BACK"
2080 SMI=4
2090 SC=1: REM Submenu cursor
2100 REM
2110 REM Display submenu
2120 PRINT CHR$(147)
2130 PRINT:PRINT TAB(12);"OPTIONS"
2140 FOR I=1 TO SMI
2150 PRINT TAB(10);
2160 IF I=SC THEN PRINT CHR$(18);
2170 PRINT SM$(I);
2180 IF I=SC THEN PRINT CHR$(146);
2190 PRINT
2200 NEXT I
2210 REM
2220 REM Handle input (similar to main menu)
2230 JOY=PEEK(56320)
2240 IF (JOY AND 1)=0 THEN SC=SC-1:IF SC<1 THEN SC=SMI
2250 IF (JOY AND 2)=0 THEN SC=SC+1:IF SC>SMI THEN SC=1
2260 IF (JOY AND 16)=0 THEN GOSUB 2500: REM Execute submenu selection
2270 FOR D=1 TO 100:NEXT D
2280 RETURN
2290 REM
2500 REM Execute submenu selection
2510 IF SC=4 THEN ML=1:RETURN: REM Back to main menu
2520 IF SC=1 THEN PRINT "DIFFICULTY CHANGED":FOR I=1 TO 500:NEXT
2530 IF SC=2 THEN PRINT "MUSIC TOGGLED":FOR I=1 TO 500:NEXT
2540 IF SC=3 THEN PRINT "SOUND FX TOGGLED":FOR I=1 TO 500:NEXT
2550 RETURN
```

### Common Mistakes to Address

**Mistake 1: No wrap-around on cursor**
```basic
100 C=C-1: REM Move up
110 IF C<1 THEN C=1: REM Stops at top (annoying!)
```
**Fix:** Wrap to bottom: `IF C<1 THEN C=MI`

**Mistake 2: Redrawing entire menu every frame**
```basic
100 PRINT CHR$(147): REM Clear screen every loop
110 REM Draw all items
120 GOTO 100: REM Flickers!
```
**Fix:** Only redraw when cursor moves, OR accept flicker as retro aesthetic.

**Mistake 3: No delay between inputs**
```basic
100 JOY=PEEK(56320)
110 IF (JOY AND 1)=0 THEN C=C-1
120 GOTO 100: REM Scrolls TOO FAST!
```
**Fix:** Add delay (`FOR D=1 TO 100:NEXT D`) after input processing.

**Mistake 4: Fire button not debounced**
```basic
100 IF (JOY AND 16)=0 THEN GOSUB 1000: REM Execute action
110 REM Fire still held → executes again immediately!
```
**Fix:** Wait for button release:
```basic
100 IF (JOY AND 16)=0 THEN GOSUB 1000:GOSUB 9000: REM Wait for release
...
9000 JOY=PEEK(56320):IF (JOY AND 16)=0 THEN 9000
9010 RETURN
```

### Game Context: How Professionals Used This

**Ultima IV (1985):**
- Menu for commands (Talk, Cast, Search, etc.)
- Cursor wraps around
- Keyboard shortcuts (T for Talk) AND menu selection
- Context-sensitive (different options in dungeon vs town)

**Bard's Tale (1985):**
- Character selection menu
- Spell casting menu (nested: choose character → choose spell)
- Inventory management (select character → select item → action)

**Pirates! (1987):**
- Port menu (tavern, merchant, shipyard, governor)
- Cursor-based selection with joystick
- Each option leads to submenu or game screen

### Progression Notes

**Builds on:**
- L54: State machine (menu is a state)
- L12: Joystick input
- L49: Arrays (menu items)

**Leads to:**
- L56: Save/Load UI (menu variant)
- L58: Options menu (settings modification)
- L64: Complete game (integrated menu system)

### Why It Matters

**Short-term:** Menus make your game accessible and professional.

**Long-term:** Menu systems teach you:
- Event-driven programming (respond to input)
- UI/UX design (cursor feedback, navigation flow)
- State management within states (cursor position)

Modern UI frameworks (React, Flutter, SwiftUI) use the same concepts: lists of options, selection state, event handlers.

### Reality Check

**What BASIC Does Well:**
- Simple string arrays for menu items
- Joystick input is easy
- Reverse video highlight looks good

**What BASIC Struggles With:**
- Smooth scrolling menus (can't do inertia easily)
- Complex layouts (multi-column menus are awkward)
- Animated cursors (sprite overlay slows rendering)

**Assembly Advantage:**
- Custom fonts for fancy menu graphics
- Smooth color cycling on selection
- Can handle 100+ item menus efficiently

**Verdict:** For typical menus (5-20 items), BASIC is perfect. Focus on usability, not fancy graphics.

---

## Lesson 56: Save/Load UI

**Concept:** Visual save slot browser with metadata preview
**WOW Moment:** Professional save/load interface like RPGs
**Difficulty:** ⭐⭐⭐⭐⭐ (combines file I/O, menus, validation, UX)

### The Problem

Lesson 51 taught save systems, but the UI was text-based:
```basic
INPUT "SAVE TO SLOT (1-3)";SL
```

**Problems:**
- User must remember slot numbers
- No preview of what's in each slot
- Easy to overwrite wrong save
- Not user-friendly

**Solution:** Visual slot browser showing metadata.

### Complete Save/Load UI

```basic
10 REM ═══════════════════════════════════════
20 REM Save/Load UI System
30 REM ═══════════════════════════════════════
40 REM
100 REM Initialize slot metadata arrays
110 DIM SN$(3): REM Slot names
120 DIM SS(3): REM Slot scores
130 DIM SL(3): REM Slot levels
140 DIM SD$(3): REM Slot dates
150 DIM SE(3): REM Slot exists flag (1=has save, 0=empty)
160 REM
200 REM Current game state (to save)
210 SCORE=1500:LEVEL=3:LIVES=5:NM$="PLAYER"
220 REM
300 REM Mode: 1=Save, 2=Load
310 MD=1: REM Change to test different modes
320 REM
400 REM ═══════════════════════════════════════
410 REM Main UI loop
420 REM ═══════════════════════════════════════
430 GOSUB 5000: REM Scan slots for metadata
440 GOSUB 1000: REM Display slot browser
450 GOSUB 2000: REM Handle input
460 IF SEL>0 THEN GOSUB 3000: REM Process selection
470 IF DONE=1 THEN END: REM Exit UI
480 GOTO 440: REM Loop
490 REM
1000 REM ═══════════════════════════════════════
1010 REM Display slot browser
1020 REM ═══════════════════════════════════════
1030 PRINT CHR$(147)
1040 PRINT
1050 IF MD=1 THEN PRINT TAB(14);"SAVE GAME"
1060 IF MD=2 THEN PRINT TAB(14);"LOAD GAME"
1070 PRINT TAB(14);"========="
1080 PRINT
1090 REM
1100 REM Display each slot
1110 FOR I=1 TO 3
1120 PRINT TAB(5);
1130 REM Highlight current selection
1140 IF I=C THEN PRINT CHR$(18);: REM Reverse on
1150 PRINT "SLOT";I;
1160 REM
1170 IF SE(I)=0 THEN PRINT " [EMPTY]";
1180 IF SE(I)=1 THEN PRINT " ";SN$(I);" LV";SL(I);" ";SS(I);"PTS";
1190 REM
1200 IF I=C THEN PRINT CHR$(146);: REM Reverse off
1210 PRINT
1220 PRINT TAB(10);"  ";
1230 IF SE(I)=1 THEN PRINT "SAVED: ";SD$(I)
1240 PRINT
1250 NEXT I
1260 REM
1270 PRINT:PRINT TAB(10);"USE JOY UP/DOWN, FIRE=SELECT"
1280 PRINT TAB(10);"PRESS Q TO CANCEL"
1290 RETURN
1300 REM
2000 REM ═══════════════════════════════════════
2010 REM Handle input
2020 REM ═══════════════════════════════════════
2030 SEL=0: REM No selection
2040 C=1: REM Cursor position (1-3)
2050 REM
2060 REM Input loop
2070 JOY=PEEK(56320)
2080 GET K$
2090 REM
2100 REM Up/Down
2110 IF (JOY AND 1)=0 THEN C=C-1:IF C<1 THEN C=3
2120 IF (JOY AND 2)=0 THEN C=C+1:IF C>3 THEN C=1
2130 REM
2140 REM Fire to select
2150 IF (JOY AND 16)=0 THEN SEL=C:RETURN
2160 REM
2170 REM Q to cancel
2180 IF K$="Q" THEN DONE=1:RETURN
2190 REM
2200 FOR D=1 TO 100:NEXT D
2210 IF SEL=0 THEN GOTO 2070: REM Loop until selection
2220 RETURN
2230 REM
3000 REM ═══════════════════════════════════════
3010 REM Process selection
3020 REM Input: SEL (slot number), MD (mode)
3030 REM ═══════════════════════════════════════
3040 IF MD=1 THEN GOSUB 6000: REM Save to slot
3050 IF MD=2 THEN GOSUB 7000: REM Load from slot
3060 DONE=1: REM Exit after action
3070 RETURN
3080 REM
5000 REM ═══════════════════════════════════════
5010 REM Scan all slots for metadata
5020 REM ═══════════════════════════════════════
5030 FOR I=1 TO 3
5040 GOSUB 5500: REM Check slot I
5050 NEXT I
5060 RETURN
5070 REM
5500 REM Check single slot (I=slot number)
5510 FN$="SAVE"+STR$(I)+",SEQ,R"
5520 OPEN 15,8,15
5530 OPEN 1,8,2,FN$
5540 INPUT#15,EN,EM$
5550 REM
5560 IF EN=62 THEN SE(I)=0:CLOSE 1:CLOSE 15:RETURN: REM File not found
5570 IF EN<>0 THEN SE(I)=0:CLOSE 1:CLOSE 15:RETURN: REM Error
5580 REM
5590 REM File exists, read metadata
5600 SE(I)=1
5610 INPUT#1,VER$: REM Version (ignored)
5620 INPUT#1,SD$(I): REM Date
5630 INPUT#1,SN$(I): REM Name
5640 INPUT#1,SS(I): REM Score
5650 INPUT#1,SL(I): REM Level
5660 CLOSE 1
5670 CLOSE 15
5680 RETURN
5700 REM
6000 REM ═══════════════════════════════════════
6010 REM Save to slot
6020 REM Input: SEL (slot number)
6030 REM ═══════════════════════════════════════
6040 REM Check if slot has existing save
6050 IF SE(SEL)=1 THEN GOSUB 6500: REM Confirm overwrite
6060 IF OW=0 THEN RETURN: REM User cancelled
6070 REM
6080 FN$="@0:SAVE"+STR$(SEL)+",SEQ,W"
6090 PRINT CHR$(147)
6100 PRINT:PRINT "SAVING TO SLOT";SEL;"..."
6110 REM
6120 OPEN 1,8,2,FN$
6130 PRINT#1,"V1.0": REM Version
6140 PRINT#1,"2024-01-15": REM Date (hardcoded for demo)
6150 PRINT#1,NM$
6160 PRINT#1,SCORE
6170 PRINT#1,LEVEL
6180 PRINT#1,LIVES
6190 CLOSE 1
6200 REM
6210 PRINT:PRINT "SAVE COMPLETE!"
6220 FOR I=1 TO 1000:NEXT
6230 RETURN
6240 REM
6500 REM Confirm overwrite
6510 PRINT CHR$(147)
6520 PRINT:PRINT "SLOT";SEL;"ALREADY HAS A SAVE:"
6530 PRINT
6540 PRINT "  ";SN$(SEL)
6550 PRINT "  LEVEL";SL(SEL)
6560 PRINT "  SCORE";SS(SEL)
6570 PRINT
6580 INPUT "OVERWRITE (Y/N)";A$
6590 IF A$="Y" OR A$="y" THEN OW=1:RETURN
6600 OW=0:RETURN
6610 REM
7000 REM ═══════════════════════════════════════
7010 REM Load from slot
7020 REM Input: SEL (slot number)
7030 REM ═══════════════════════════════════════
7040 IF SE(SEL)=0 THEN PRINT CHR$(147);"SLOT EMPTY!":FOR I=1 TO 1000:NEXT:RETURN
7050 REM
7060 FN$="SAVE"+STR$(SEL)+",SEQ,R"
7070 PRINT CHR$(147)
7080 PRINT:PRINT "LOADING SLOT";SEL;"..."
7090 REM
7100 OPEN 1,8,2,FN$
7110 INPUT#1,VER$
7120 INPUT#1,DT$
7130 INPUT#1,NM$
7140 INPUT#1,SCORE
7150 INPUT#1,LEVEL
7160 INPUT#1,LIVES
7170 CLOSE 1
7180 REM
7190 PRINT:PRINT "LOAD COMPLETE!"
7200 PRINT "WELCOME BACK, ";NM$;"!"
7210 FOR I=1 TO 2000:NEXT
7220 RETURN
```

### Common Mistakes to Address

**Mistake 1: Scanning slots every frame**
```basic
100 GOSUB 5000: REM Scan all 3 slots (slow!)
110 GOSUB 1000: REM Display
120 GOTO 100: REM Repeated disk access!
```
**Fix:** Scan once at UI entry, refresh only after save.

**Mistake 2: Not showing "EMPTY" for unused slots**
```basic
100 IF SE(I)=0 THEN PRINT: REM Just blank line (confusing!)
```
**Fix:** Explicitly print `"[EMPTY]"` so users know slot is available.

**Mistake 3: No confirmation for overwrite**
```basic
100 INPUT "SLOT";SL
110 GOSUB 6000: REM Save immediately (data loss!)
```
**Fix:** Check `SE(SL)`, confirm if occupied.

**Mistake 4: Truncated metadata display**
```basic
100 PRINT SN$(I);SL(I);SS(I): REM All crammed together
```
**Fix:** Format clearly: `"PLAYER - LV3 - 1500 PTS - 2024-01-15"`

### Game Context: How Professionals Used This

**Ultima VI (1990):**
- Visual save slot browser with character portraits
- Displays: character name, location, play time
- Autosave slot + 8 manual slots
- Confirms overwrite with detailed prompt

**The Legend of Zelda (NES, but similar UX):**
- 3 save slots with heart containers visible
- Shows name, deaths, progress (triforce pieces)
- Red highlight on selected slot

**Final Fantasy III (SNES):**
- Save menu shows: party members, location, time played
- Thumbnails of party sprites
- Slot 1-4 selection with cursor

**Key Pattern:** Metadata preview is standard in professional games. Users should never guess what's in a slot.

### Progression Notes

**Builds on:**
- L51: Save/load systems (file I/O)
- L55: Menu system (cursor navigation)
- L50: File I/O (metadata reading)

**Leads to:**
- L64: Complete game (integrated save UI)

### Why It Matters

**Short-term:** Save/load UI completes the professional game experience. Players can manage saves confidently.

**Long-term:** Save UI design teaches:
- User experience (feedback, confirmation, clarity)
- Data presentation (metadata formatting)
- Error prevention (overwrite protection)
- Accessibility (visual vs text-only)

These principles apply to ANY application with data management: cloud saves, document editors, photo apps.

### Reality Check

**What BASIC Does Well:**
- Simple text-based metadata display
- Sequential file reading is straightforward
- Cursor navigation reuses menu code

**What BASIC Struggles With:**
- No thumbnails/screenshots (would require image loading)
- Slow slot scanning (disk access adds seconds)
- Limited formatting (can't do fancy layouts easily)

**Assembly Advantage:**
- Could compress/decompress screenshots
- Faster slot scanning with optimized file reads
- Custom graphics for slot display

**Verdict:** BASIC save UI is functional and professional for text-based metadata. For fancy graphics (character portraits), you'd need assembly or hybrid approach.

---

## Section 2 Summary: Screen Systems

**Lessons 53-56 taught you:**
- ✅ Title screens with animation and attract modes (L53)
- ✅ State machines for clean game flow (L54)
- ✅ Cursor-based menu systems (L55)
- ✅ Professional save/load UI with metadata (L56)

**These systems create the STRUCTURE of professional games:**
- Players see polished presentation (title)
- Code has clean architecture (state machine)
- Players navigate easily (menus)
- Players manage progress confidently (save UI)

**What's Next:**
Section 3 (L57-60) covers **Game Polish**: transitions, options menus, instructions, and configuration. You'll learn the "final 10%" that makes games feel finished.

---

**End of Section 2: Screen Systems**
