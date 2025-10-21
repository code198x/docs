# Tier 4 Section 1: Data Systems (Lessons 49-52)

**Section Theme:** "Organizing Complexity"
**Core Skill:** Managing game data beyond simple variables

---

## Section 1 Overview

After Tier 3's performance lessons, students return to what BASIC does well: **data management and logic**. This section teaches professional data organization techniques used in commercial BASIC games.

**Why This Matters:**
- RPGs, adventures, and strategy games are data-heavy
- Save systems require structured data
- High scores need persistent storage
- These patterns work in ANY language

**Reality Check:** The file I/O and data structures you learn here are MORE relevant to modern game development than raster bars. Every game needs save systems and leaderboards.

---

## Lesson 49: Arrays & Data Structures

**Concept:** Multi-dimensional arrays, parallel arrays, data organization
**WOW Moment:** RPG inventory system with items, quantities, and prices
**Difficulty:** ⭐⭐⭐ (introduces multi-array coordination)

### The Problem

Variables don't scale:
```basic
100 I1$="SWORD":Q1=1:P1=50
110 I2$="POTION":Q2=3:P2=10
120 I3$="SHIELD":Q3=1:P3=75
```

What if you have 50 items? **Arrays solve this.**

### Technical Details

**Parallel Arrays Pattern:**
```basic
100 REM Inventory system with parallel arrays
110 DIM I$(10): REM Item names
120 DIM Q(10): REM Quantities
130 DIM P(10): REM Prices
140 REM
150 REM Load inventory data
160 FOR N=1 TO 5
170 READ I$(N),Q(N),P(N)
180 NEXT
190 REM
200 DATA "SWORD",1,50
210 DATA "POTION",3,10
220 DATA "SHIELD",1,75
230 DATA "KEY",2,0
240 DATA "MAP",1,100
```

**Why This Works:**
- Same index across arrays = related data
- `I$(3)`, `Q(3)`, `P(3)` = complete item #3
- Easy to add/remove items
- Can search, sort, display

### Extended Example: 2D Array for Level Map

```basic
100 REM Tile-based level map
110 DIM M(10,10): REM 11x11 grid (0-10)
120 REM
130 REM Load level data
140 FOR Y=0 TO 10
150 FOR X=0 TO 10
160 READ M(X,Y)
170 NEXT X
180 NEXT Y
190 REM
200 REM Tile types: 0=floor, 1=wall, 2=door, 3=treasure
210 DATA 1,1,1,1,1,1,1,1,1,1,1
220 DATA 1,0,0,0,0,0,0,0,0,0,1
230 DATA 1,0,1,1,1,0,1,1,1,0,1
240 DATA 1,0,1,3,0,0,0,3,1,0,1
250 DATA 1,0,1,1,1,0,1,1,1,0,1
260 DATA 1,0,0,0,0,0,0,0,0,0,1
270 DATA 1,0,1,1,2,1,1,1,1,0,1
280 DATA 1,0,0,0,0,0,0,0,0,0,1
290 DATA 1,1,1,1,1,1,1,1,1,1,1
300 REM
310 REM Display map
320 FOR Y=0 TO 10
330 FOR X=0 TO 10
340 T=M(X,Y)
350 IF T=0 THEN PRINT ".";
360 IF T=1 THEN PRINT CHR$(160);: REM Solid block
370 IF T=2 THEN PRINT "D";
380 IF T=3 THEN PRINT "*";
390 NEXT X
400 PRINT
410 NEXT Y
```

### Example 3: High Score Table (Sorted Array)

```basic
100 REM High score table
110 DIM HS(10): REM High scores
120 DIM N$(10): REM Player names
130 REM
140 REM Initialize with dummy data
150 FOR I=1 TO 10
160 HS(I)=(11-I)*1000
170 N$(I)="CPU"
180 NEXT
190 REM
200 REM Display current table
210 PRINT "HIGH SCORES"
220 PRINT "============"
230 FOR I=1 TO 10
240 PRINT I;". ";N$(I);TAB(15);HS(I)
250 NEXT
260 REM
270 REM Try to insert new score
280 INPUT "YOUR NAME";NM$
290 INPUT "YOUR SCORE";SC
300 GOSUB 1000: REM Insert score subroutine
310 REM
320 REM Display updated table
330 PRINT:PRINT "UPDATED HIGH SCORES"
340 PRINT "==================="
350 FOR I=1 TO 10
360 PRINT I;". ";N$(I);TAB(15);HS(I)
370 NEXT
380 END
390 REM
1000 REM ══════════════════════════════════════
1010 REM Insert score into sorted table
1020 REM ══════════════════════════════════════
1030 FOR I=1 TO 10
1040 IF SC>HS(I) THEN 1060
1050 NEXT I:RETURN: REM Score too low
1060 REM Found position, shift down
1070 FOR J=10 TO I+1 STEP -1
1080 HS(J)=HS(J-1)
1090 N$(J)=N$(J-1)
1100 NEXT J
1110 REM Insert new score
1120 HS(I)=SC
1130 N$(I)=NM$
1140 RETURN
```

### Common Mistakes to Address

**Mistake 1: Forgetting DIM before use**
```basic
100 I$(1)="SWORD": REM ERROR! Array not dimensioned
```
**Fix:** Always DIM arrays at program start.

**Mistake 2: Off-by-one errors with 2D arrays**
```basic
100 DIM M(10,10): REM Allocates 11x11 (indices 0-10)
110 FOR Y=1 TO 11: REM WRONG! Will crash at Y=11
```
**Fix:** Remember arrays start at 0, or use 1-based and DIM one larger.

**Mistake 3: Parallel array index mismatch**
```basic
100 DIM I$(10),Q(10),P(10)
110 I$(1)="SWORD":Q(2)=1:P(1)=50: REM Q(2) should be Q(1)!
```
**Fix:** Use same loop variable for all parallel arrays.

**Mistake 4: String array without dimension**
```basic
100 DIM N$(10): REM Only allocates pointers
110 N$(1)="CHRISTOPHER": REM ERROR! Default string length too short
```
**Fix:** C64 BASIC V2 strings are dynamic, but initialize with empty strings if needed.

### Game Context: How Professionals Used This

**The Bard's Tale (1985):**
- Parallel arrays for party members: names, HP, MP, stats
- 2D arrays for dungeon maps (22x22 grids)
- Item arrays with properties (type, damage, armor class)

**Ultima IV (1985):**
- Character arrays for 8-party system
- Inventory arrays per character
- World map as massive array (256x256 tiles compressed)

**Why It Works in BASIC:**
- Arrays don't require pointers or memory management
- READ/DATA makes initialization clean
- Simple index math for lookups

### Progression Notes

**Builds on:**
- L5: Variables (single values)
- L6: FOR loops (iteration)
- L10: Arrays basics (if introduced)

**Leads to:**
- L50: Saving arrays to disk
- L51: Complex data serialization
- L52: Persistent high scores

### Why It Matters

**Short-term:** You can now build inventory systems, level editors, and data-driven games.

**Long-term:** Every language uses arrays/lists. The parallel array pattern translates directly to structs/objects in other languages:

```c
// Same concept in C
struct Item {
    char name[20];
    int quantity;
    int price;
};
struct Item inventory[10];
```

### Reality Check

**What BASIC Does Well:**
- Simple array syntax (no pointers!)
- Automatic bounds checking (crashes instead of corruption)
- Easy to debug with PRINT statements

**What BASIC Struggles With:**
- No dynamic resizing (must DIM max size upfront)
- No structs/records (thus parallel arrays)
- Limited string handling in arrays

**Assembly won't make data structures easier.** This is where BASIC shines.

---

## Lesson 50: File I/O Basics

**Concept:** OPEN, CLOSE, PRINT#, INPUT#, GET#
**WOW Moment:** Save game progress to disk, load it back
**Difficulty:** ⭐⭐⭐⭐ (disk I/O can fail in mysterious ways)

### The Problem

```basic
100 SCORE=1500:LEVEL=3:LIVES=5
```

**What happens when you turn off the computer?** Data vanishes.

**Solution:** Write to disk, read from disk.

### Technical Details: C64 File Operations

**Sequential File Write:**
```basic
100 REM Save game state
110 OPEN 1,8,2,"SAVEGAME,SEQ,W"
120 PRINT#1,SCORE
130 PRINT#1,LEVEL
140 PRINT#1,LIVES
150 CLOSE 1
160 PRINT "GAME SAVED!"
```

**Sequential File Read:**
```basic
200 REM Load game state
210 OPEN 1,8,2,"SAVEGAME,SEQ,R"
220 INPUT#1,SCORE
230 INPUT#1,LEVEL
240 INPUT#1,LIVES
250 CLOSE 1
260 PRINT "GAME LOADED!"
270 PRINT "SCORE:";SCORE
280 PRINT "LEVEL:";LEVEL
290 PRINT "LIVES:";LIVES
```

### C64 File I/O Syntax Breakdown

**OPEN syntax:**
```
OPEN logical_file, device, secondary_address, "filename,type,mode"
```

- **Logical file (1-255):** Your handle for this file
- **Device (8):** Disk drive (8 = first drive, 9 = second drive)
- **Secondary address (2-14):** Channel number (usually 2 for data files)
- **Filename:** Up to 16 characters
- **Type:** SEQ (sequential), PRG (program), REL (relative - advanced)
- **Mode:** R (read), W (write), A (append)

### Extended Example: Save with Error Checking

```basic
100 REM Save game with error checking
110 PRINT "SAVING GAME..."
120 REM
130 REM Clear error channel
140 OPEN 15,8,15
150 INPUT#15,EN,EM$,ET,ES: REM Error number, message, track, sector
160 IF EN<>0 THEN PRINT "DISK ERROR:";EM$:CLOSE 15:END
170 REM
180 REM Open save file
190 OPEN 1,8,2,"SAVEGAME,SEQ,W"
200 REM Check for error after OPEN
210 INPUT#15,EN,EM$
220 IF EN<>0 THEN PRINT "SAVE FAILED:";EM$:CLOSE 1:CLOSE 15:END
230 REM
240 REM Write data
250 PRINT#1,SCORE
260 PRINT#1,LEVEL
270 PRINT#1,LIVES
280 PRINT#1,PX: REM Player X position
290 PRINT#1,PY: REM Player Y position
300 REM
310 REM Close files
320 CLOSE 1
330 CLOSE 15
340 PRINT "GAME SAVED SUCCESSFULLY!"
```

### Example 3: Load with Validation

```basic
400 REM Load game with validation
410 PRINT "LOADING GAME..."
420 REM
430 REM Check if file exists
440 OPEN 15,8,15
450 OPEN 1,8,2,"SAVEGAME,SEQ,R"
460 INPUT#15,EN,EM$
470 IF EN=62 THEN PRINT "NO SAVE FILE FOUND":CLOSE 1:CLOSE 15:GOTO 600
480 IF EN<>0 THEN PRINT "LOAD ERROR:";EM$:CLOSE 1:CLOSE 15:END
490 REM
500 REM Read data
510 INPUT#1,SCORE
520 INPUT#1,LEVEL
530 INPUT#1,LIVES
540 INPUT#1,PX
550 INPUT#1,PY
560 REM
570 REM Validate data
580 IF LEVEL<1 OR LEVEL>10 THEN PRINT "CORRUPT SAVE FILE":CLOSE 1:CLOSE 15:END
590 IF LIVES<0 OR LIVES>9 THEN PRINT "CORRUPT SAVE FILE":CLOSE 1:CLOSE 15:END
595 REM
600 CLOSE 1
610 CLOSE 15
620 PRINT "GAME LOADED!"
630 PRINT "SCORE:";SCORE;" LEVEL:";LEVEL;" LIVES:";LIVES
```

### Common Mistakes to Address

**Mistake 1: Forgetting to CLOSE files**
```basic
100 OPEN 1,8,2,"DATA,SEQ,W"
110 PRINT#1,"HELLO"
120 END: REM WRONG! File not closed, data may not be written
```
**Fix:** Always CLOSE before END. Data buffers may not flush otherwise.

**Mistake 2: Reusing logical file numbers**
```basic
100 OPEN 1,8,2,"FILE1,SEQ,W"
110 PRINT#1,"DATA"
120 CLOSE 1
130 OPEN 1,8,2,"FILE2,SEQ,W": REM OK, but error-prone
```
**Fix:** Use different logical file numbers for clarity, or always CLOSE before reopen.

**Mistake 3: Not checking disk errors**
```basic
100 OPEN 1,8,2,"SAVE,SEQ,W"
110 PRINT#1,DATA: REM What if disk is full? Write-protected? Missing?
```
**Fix:** Always check error channel 15.

**Mistake 4: INPUT# reads strings incorrectly**
```basic
100 PRINT#1,"HELLO WORLD": REM Writes: HELLO WORLD
110 INPUT#1,A$: REM Reads: "HELLO" (stops at space!)
```
**Fix:** Use GET# for character-by-character reading, or avoid spaces in strings.

### Game Context: How Professionals Used This

**Ultima IV (1985):**
- Save file contains: character stats, party composition, inventory, quest flags
- Single sequential file, loads quickly
- Checksum validation to detect corruption

**The Bard's Tale (1985):**
- Separate save file per character
- Dungeon progress saved independently
- "Save Roster" before entering dangerous areas

**Pirates! (1987):**
- Career progression saved to disk
- Multiple save slots for different pirate careers
- Save includes: wealth, reputation, family, fleet

### Progression Notes

**Builds on:**
- L49: Arrays (saving structured data)
- L5: Variables (basic data types)

**Leads to:**
- L51: Multi-slot save system
- L52: High score persistence
- L56: Save/load UI

### Why It Matters

**Short-term:** Your games can now remember progress across sessions. HUGE upgrade in perceived professionalism.

**Long-term:** Every platform has file I/O. The concepts (open, write, close, error handling) are universal.

### Reality Check

**What BASIC Does Well:**
- Sequential file I/O is simple and reliable
- Error channel provides good feedback
- No complex file handles or streams

**What BASIC Struggles With:**
- Slow! Disk access takes ~1 second per operation
- No random access (well, REL files exist but are complex)
- Limited error recovery options

**C64 Disk Quirks:**
- Error 62 = File not found (most common)
- Error 63 = File exists (trying to write existing file without @0:)
- Error 65 = No device present (drive off or disconnected)
- Error 72 = Disk full

**Assembly won't make disk I/O faster.** It's the 1541 drive's speed that's the bottleneck. Use BASIC for save systems.

---

## Lesson 51: Save/Load Systems

**Concept:** Complete save system with validation and multiple slots
**WOW Moment:** Professional three-slot save system like commercial games
**Difficulty:** ⭐⭐⭐⭐⭐ (complex state management and validation)

### The Problem

Lesson 50 taught file I/O basics. But real games need:
- **Multiple save slots** (3 is standard)
- **Metadata** (when saved, which level, character name)
- **Validation** (detect corrupted saves)
- **Overwrite protection** (confirm before deleting progress)

### Save File Format Design

**Good save files are self-describing:**

```
Line 1: Version number (e.g., "V1.0")
Line 2: Timestamp (e.g., "2024-01-15")
Line 3: Player name
Line 4: Score
Line 5: Level
Line 6: Lives
Line 7: Player X position
Line 8: Player Y position
Line 9: Inventory data (encoded string)
Line 10: Checksum (sum of all data mod 65536)
```

**Why this format?**
- Version number lets you detect old saves if you update the game
- Timestamp shown in load menu
- Checksum catches disk errors or manual editing

### Complete Three-Slot Save System

```basic
10 REM ═══════════════════════════════════════
20 REM Three-Slot Save System
30 REM ═══════════════════════════════════════
40 REM
100 REM Initialize game variables
110 SCORE=0:LEVEL=1:LIVES=3
120 PX=10:PY=10
130 NM$="PLAYER"
140 INV$="": REM Inventory string
150 REM
200 REM Main menu
210 PRINT CHR$(147): REM Clear screen
220 PRINT "GAME MAIN MENU"
230 PRINT "=============="
240 PRINT
250 PRINT "1. NEW GAME"
260 PRINT "2. LOAD GAME"
270 PRINT "3. SAVE GAME"
280 PRINT "4. QUIT"
290 PRINT
300 INPUT "CHOICE";C$
310 IF C$="1" THEN GOSUB 1000: REM New game
320 IF C$="2" THEN GOSUB 2000: REM Load game
330 IF C$="3" THEN GOSUB 3000: REM Save game
340 IF C$="4" THEN END
350 GOTO 200
360 REM
1000 REM ═══════════════════════════════════════
1010 REM New game
1020 REM ═══════════════════════════════════════
1030 PRINT CHR$(147)
1040 INPUT "ENTER YOUR NAME";NM$
1050 SCORE=0:LEVEL=1:LIVES=3
1060 PX=10:PY=10:INV$=""
1070 PRINT "GOOD LUCK, ";NM$;"!"
1080 FOR I=1 TO 1000:NEXT: REM Pause
1090 RETURN
1100 REM
2000 REM ═══════════════════════════════════════
2010 REM Load game (slot selection)
2020 REM ═══════════════════════════════════════
2030 PRINT CHR$(147)
2040 PRINT "LOAD GAME"
2050 PRINT "========="
2060 PRINT
2070 REM Display slot metadata
2080 FOR SL=1 TO 3
2090 PRINT SL;". ";
2100 GOSUB 5000: REM Check if slot exists
2110 IF EX=1 THEN GOSUB 5500: REM Display metadata
2120 IF EX=0 THEN PRINT "EMPTY SLOT"
2130 NEXT SL
2140 PRINT
2150 INPUT "LOAD SLOT (1-3, 0=CANCEL)";SL
2160 IF SL=0 THEN RETURN
2170 IF SL<1 OR SL>3 THEN PRINT "INVALID SLOT":GOTO 2150
2180 GOSUB 6000: REM Load from slot
2190 RETURN
2200 REM
3000 REM ═══════════════════════════════════════
3010 REM Save game (slot selection)
3020 REM ═══════════════════════════════════════
3030 PRINT CHR$(147)
3040 PRINT "SAVE GAME"
3050 PRINT "========="
3060 PRINT
3070 REM Display slot metadata
3080 FOR SL=1 TO 3
3090 PRINT SL;". ";
3100 GOSUB 5000: REM Check if slot exists
3110 IF EX=1 THEN GOSUB 5500: REM Display metadata
3120 IF EX=0 THEN PRINT "EMPTY SLOT"
3130 NEXT SL
3140 PRINT
3150 INPUT "SAVE TO SLOT (1-3, 0=CANCEL)";SL
3160 IF SL=0 THEN RETURN
3170 IF SL<1 OR SL>3 THEN PRINT "INVALID SLOT":GOTO 3150
3180 REM Confirm overwrite if slot occupied
3190 GOSUB 5000: REM Check if slot exists
3200 IF EX=1 THEN INPUT "OVERWRITE EXISTING SAVE (Y/N)";A$:IF A$<>"Y" THEN RETURN
3210 GOSUB 7000: REM Save to slot
3220 RETURN
3300 REM
5000 REM ═══════════════════════════════════════
5010 REM Check if save slot exists
5020 REM Input: SL (slot number 1-3)
5030 REM Output: EX (1=exists, 0=empty)
5040 REM ═══════════════════════════════════════
5050 FN$="SAVE"+STR$(SL)+",SEQ,R"
5060 OPEN 15,8,15
5070 OPEN 1,8,2,FN$
5080 INPUT#15,EN,EM$
5090 IF EN=62 THEN EX=0: REM File not found
5100 IF EN=0 THEN EX=1: REM File exists
5110 CLOSE 1
5120 CLOSE 15
5130 RETURN
5200 REM
5500 REM ═══════════════════════════════════════
5510 REM Display save slot metadata
5520 REM Input: SL (slot number)
5530 REM ═══════════════════════════════════════
5540 FN$="SAVE"+STR$(SL)+",SEQ,R"
5550 OPEN 1,8,2,FN$
5560 INPUT#1,VER$: REM Version
5570 INPUT#1,DT$: REM Date
5580 INPUT#1,SNM$: REM Saved player name
5590 INPUT#1,SSC: REM Saved score
5600 INPUT#1,SLV: REM Saved level
5610 CLOSE 1
5620 PRINT SNM$;" - LV";SLV;" - ";SSC;" PTS - ";DT$
5630 RETURN
5700 REM
6000 REM ═══════════════════════════════════════
6010 REM Load game from slot
6020 REM Input: SL (slot number)
6030 REM ═══════════════════════════════════════
6040 FN$="SAVE"+STR$(SL)+",SEQ,R"
6050 PRINT "LOADING SLOT";SL;"..."
6060 OPEN 1,8,2,FN$
6070 REM Read all data
6080 INPUT#1,VER$
6090 INPUT#1,DT$
6100 INPUT#1,NM$
6110 INPUT#1,SCORE
6120 INPUT#1,LEVEL
6130 INPUT#1,LIVES
6140 INPUT#1,PX
6150 INPUT#1,PY
6160 INPUT#1,INV$
6170 INPUT#1,CHK: REM Checksum
6180 CLOSE 1
6190 REM Validate checksum
6200 GOSUB 8000: REM Calculate checksum
6210 IF CHK<>CK THEN PRINT "CORRUPT SAVE FILE!":RETURN
6220 PRINT "LOADED SUCCESSFULLY!"
6230 PRINT "WELCOME BACK, ";NM$;"!"
6240 FOR I=1 TO 1000:NEXT
6250 RETURN
6300 REM
7000 REM ═══════════════════════════════════════
7010 REM Save game to slot
7020 REM Input: SL (slot number)
7030 REM ═══════════════════════════════════════
7040 FN$="@0:SAVE"+STR$(SL)+",SEQ,W": REM @0: overwrites existing
7050 PRINT "SAVING TO SLOT";SL;"..."
7060 OPEN 1,8,2,FN$
7070 REM Write header
7080 PRINT#1,"V1.0": REM Version
7090 REM Create simple timestamp
7100 DT$="2024-01-15": REM In real game, get from TOD$ or user input
7110 PRINT#1,DT$
7120 REM Write game state
7130 PRINT#1,NM$
7140 PRINT#1,SCORE
7150 PRINT#1,LEVEL
7160 PRINT#1,LIVES
7170 PRINT#1,PX
7180 PRINT#1,PY
7190 PRINT#1,INV$
7200 REM Calculate and write checksum
7210 GOSUB 8000: REM Calculate checksum
7220 PRINT#1,CK
7230 CLOSE 1
7240 PRINT "SAVED SUCCESSFULLY!"
7250 FOR I=1 TO 1000:NEXT
7260 RETURN
7300 REM
8000 REM ═══════════════════════════════════════
8010 REM Calculate checksum
8020 REM Output: CK (checksum)
8030 REM ═══════════════════════════════════════
8040 CK=SCORE+LEVEL+LIVES+PX+PY
8050 REM Add string lengths as proxy
8060 CK=CK+LEN(NM$)+LEN(INV$)
8070 REM Keep in valid range
8080 CK=CK AND 65535: REM 16-bit checksum
8090 RETURN
```

### Common Mistakes to Address

**Mistake 1: Not using @0: prefix for overwrite**
```basic
100 OPEN 1,8,2,"SAVE1,SEQ,W": REM Error 63 if file exists!
```
**Fix:** Use `"@0:SAVE1,SEQ,W"` to allow overwrite.

**Mistake 2: Forgetting to validate loaded data**
```basic
100 INPUT#1,LEVEL: REM What if LEVEL=999 due to corruption?
110 FOR I=1 TO LEVEL: REM Crashes or hangs!
```
**Fix:** Always check loaded values are in valid ranges.

**Mistake 3: Weak checksums**
```basic
100 CK=SCORE+LEVEL: REM Too simple, many collisions
```
**Fix:** Include more data in checksum, use modulo to prevent overflow.

**Mistake 4: No user feedback during save/load**
```basic
100 GOSUB 7000: REM Long pause with no indication...
```
**Fix:** Print "SAVING..." and "SAVED!" messages.

### Game Context: How Professionals Used This

**Ultima V (1988):**
- Single save slot (to increase difficulty!)
- Save only at inns (strategic decision)
- Checksum validation plus magic number check

**Might and Magic (1987):**
- Save party roster separately from world state
- Can copy character files between disks
- "Write-protect your save disk" advice in manual

**Wizardry (1981):**
- Permanent death: deleted save file when character died
- Backup saves encouraged in manual
- Created tension: "Do I risk this dungeon?"

### Progression Notes

**Builds on:**
- L50: Basic file I/O
- L49: Arrays (saving complex data)
- L55: Menu systems (UI for slot selection)

**Leads to:**
- L56: Save/Load UI (visual slot browser)
- L64: Complete game with saves

### Why It Matters

**Short-term:** Your games now have professional-grade save systems that rival commercial titles.

**Long-term:** Save system design teaches you about:
- Data serialization (JSON/XML in modern games)
- Version compatibility (V1.0 vs V1.1 saves)
- Data validation and integrity
- User experience (confirmation dialogs, metadata display)

These concepts appear in EVERY game engine and application framework.

### Reality Check

**What BASIC Does Well:**
- Sequential file format is human-readable (for debugging)
- Simple to implement with PRINT#/INPUT#
- Error channel provides clear feedback

**What BASIC Struggles With:**
- Disk access is SLOW (~3-5 seconds for 3-slot scan)
- No compression (save files use more disk space)
- Limited string handling makes complex data awkward

**Could Assembly Help?**
- **Slightly:** Direct disk access can be faster
- **Mostly No:** The 1541 drive itself is the bottleneck
- **Verdict:** Stick with BASIC for save systems. Faster code doesn't help when waiting for disk drive.

---

## Lesson 52: High Score Table

**Concept:** Persistent leaderboard with sorted insertion
**WOW Moment:** Top 10 scores survive across play sessions, just like arcade games
**Difficulty:** ⭐⭐⭐⭐ (sorting algorithm + disk persistence)

### The Problem

Variables and arrays lose data when you turn off the computer. But **high scores should be permanent**, creating competition across sessions.

### The Arcade Standard

Arcade games (Pac-Man, Donkey Kong) have persistent high scores because they use battery-backed RAM or EEPROM. Home computers use disk files instead.

**Key Requirements:**
- Top 10 (or top 5) scores
- Player initials/name
- Sorted highest-to-lowest
- Persist across sessions
- Insert new score in correct position (no full re-sort)

### Complete High Score System

```basic
10 REM ═══════════════════════════════════════
20 REM High Score Table System
30 REM ═══════════════════════════════════════
40 REM
100 REM Initialize arrays
110 DIM HS(10): REM High scores
120 DIM N$(10): REM Player names
130 REM
140 REM Load high scores from disk
150 GOSUB 5000
160 REM
200 REM Main menu
210 PRINT CHR$(147)
220 PRINT "HIGH SCORE DEMO"
230 PRINT "==============="
240 PRINT
250 PRINT "1. VIEW HIGH SCORES"
260 PRINT "2. ENTER SCORE"
270 PRINT "3. RESET HIGH SCORES"
280 PRINT "4. QUIT"
290 PRINT
300 INPUT "CHOICE";C$
310 IF C$="1" THEN GOSUB 1000: REM View scores
320 IF C$="2" THEN GOSUB 2000: REM Enter new score
330 IF C$="3" THEN GOSUB 4000: REM Reset scores
340 IF C$="4" THEN END
350 GOTO 200
360 REM
1000 REM ═══════════════════════════════════════
1010 REM Display high score table
1020 REM ═══════════════════════════════════════
1030 PRINT CHR$(147)
1040 PRINT "╔═══════════════════════════════════╗"
1050 PRINT "║       HIGH SCORE TABLE            ║"
1060 PRINT "╠═══════════════════════════════════╣"
1070 FOR I=1 TO 10
1080 PRINT "║";
1090 IF I<10 THEN PRINT " ";
1100 PRINT I;". ";
1110 PRINT N$(I);
1120 REM Pad name to 10 characters
1130 FOR P=LEN(N$(I))+1 TO 10:PRINT " ";:NEXT P
1140 REM Right-align score
1150 SC$=STR$(HS(I))
1160 FOR P=LEN(SC$) TO 8:PRINT " ";:NEXT P
1170 PRINT SC$;"║"
1180 NEXT I
1190 PRINT "╚═══════════════════════════════════╝"
1200 PRINT
1210 INPUT "PRESS RETURN";A$
1220 RETURN
1300 REM
2000 REM ═══════════════════════════════════════
2010 REM Enter new score
2020 REM ═══════════════════════════════════════
2030 PRINT CHR$(147)
2040 INPUT "ENTER YOUR NAME";NM$
2050 IF LEN(NM$)>10 THEN NM$=LEFT$(NM$,10): REM Truncate
2060 INPUT "ENTER YOUR SCORE";SC
2070 IF SC<1 THEN PRINT "INVALID SCORE":RETURN
2080 REM
2090 REM Check if score qualifies
2100 IF SC<=HS(10) THEN PRINT "SORRY, SCORE TOO LOW!":FOR I=1 TO 1000:NEXT:RETURN
2110 REM
2120 REM Insert score into table
2130 GOSUB 3000
2140 REM
2150 REM Save updated table
2160 GOSUB 6000
2170 REM
2180 REM Show updated table
2190 GOSUB 1000
2200 RETURN
2300 REM
3000 REM ═══════════════════════════════════════
3010 REM Insert score into sorted table
3020 REM Input: NM$ (name), SC (score)
3030 REM ═══════════════════════════════════════
3040 REM Find insertion position
3050 POS=0
3060 FOR I=1 TO 10
3070 IF SC>HS(I) THEN POS=I:I=10: REM Found position, exit loop
3080 NEXT I
3090 REM
3100 IF POS=0 THEN RETURN: REM Score didn't make table
3110 REM
3120 REM Shift scores down from position
3130 FOR J=10 TO POS+1 STEP -1
3140 HS(J)=HS(J-1)
3150 N$(J)=N$(J-1)
3160 NEXT J
3170 REM
3180 REM Insert new score
3190 HS(POS)=SC
3200 N$(POS)=NM$
3210 REM
3220 REM Check if new high score
3230 IF POS=1 THEN PRINT:PRINT "*** NEW HIGH SCORE! ***":FOR I=1 TO 2000:NEXT
3240 RETURN
3300 REM
4000 REM ═══════════════════════════════════════
4010 REM Reset high scores to defaults
4020 REM ═══════════════════════════════════════
4030 INPUT "ARE YOU SURE (Y/N)";A$
4040 IF A$<>"Y" THEN RETURN
4050 FOR I=1 TO 10
4060 HS(I)=(11-I)*1000: REM 10000, 9000, ..., 1000
4070 N$(I)="CPU"
4080 NEXT I
4090 GOSUB 6000: REM Save to disk
4100 PRINT "HIGH SCORES RESET!"
4110 FOR I=1 TO 1000:NEXT
4120 RETURN
4200 REM
5000 REM ═══════════════════════════════════════
5010 REM Load high scores from disk
5020 REM ═══════════════════════════════════════
5030 PRINT "LOADING HIGH SCORES..."
5040 OPEN 15,8,15
5050 OPEN 1,8,2,"HISCORES,SEQ,R"
5060 INPUT#15,EN,EM$
5070 IF EN=62 THEN PRINT "NO HIGH SCORES FOUND, INITIALIZING...":CLOSE 1:CLOSE 15:GOSUB 4050:RETURN
5080 IF EN<>0 THEN PRINT "DISK ERROR:";EM$:CLOSE 1:CLOSE 15:END
5090 REM
5100 REM Read scores from file
5110 FOR I=1 TO 10
5120 INPUT#1,N$(I),HS(I)
5130 NEXT I
5140 CLOSE 1
5150 CLOSE 15
5160 PRINT "HIGH SCORES LOADED!"
5170 RETURN
5200 REM
6000 REM ═══════════════════════════════════════
6010 REM Save high scores to disk
6020 REM ═══════════════════════════════════════
6030 PRINT "SAVING HIGH SCORES..."
6040 OPEN 1,8,2,"@0:HISCORES,SEQ,W"
6050 REM Write all scores
6060 FOR I=1 TO 10
6070 PRINT#1,N$(I),HS(I)
6080 NEXT I
6090 CLOSE 1
6100 PRINT "HIGH SCORES SAVED!"
6110 RETURN
```

### Algorithm Deep Dive: Sorted Insertion

The key algorithm is **sorted insertion** (lines 3000-3240):

**Step 1:** Find where new score belongs
```basic
3050 POS=0
3060 FOR I=1 TO 10
3070 IF SC>HS(I) THEN POS=I:I=10
3080 NEXT I
```
This finds the first position where `SC > HS(I)`. The `I=10` trick exits the loop early once found.

**Step 2:** Shift everything below down one position
```basic
3130 FOR J=10 TO POS+1 STEP -1
3140 HS(J)=HS(J-1)
3150 N$(J)=N$(J-1)
3160 NEXT J
```
**Why backwards?** If you go forwards, you'd overwrite data before copying it:
```
WRONG: HS(2)=HS(1), HS(3)=HS(2) → HS(3) now has HS(1)'s value!
RIGHT: HS(10)=HS(9), ..., HS(3)=HS(2) → Each copy preserves data
```

**Step 3:** Insert new score in gap
```basic
3190 HS(POS)=SC
3200 N$(POS)=NM$
```

### Extended Example: High Scores with Date

```basic
100 DIM HS(10),N$(10),DT$(10): REM Add date array
...
3200 N$(POS)=NM$
3210 DT$(POS)=TI$: REM Store time (HHMMSS format)
...
5110 FOR I=1 TO 10
5120 INPUT#1,N$(I),HS(I),DT$(I): REM Load date too
5130 NEXT I
...
6060 FOR I=1 TO 10
6070 PRINT#1,N$(I),HS(I),DT$(I): REM Save date too
6080 NEXT I
```

### Common Mistakes to Address

**Mistake 1: Forward shift overwrites data**
```basic
FOR J=POS TO 9: REM WRONG! Copies forward
HS(J+1)=HS(J)
NEXT J
```
**Result:** All entries become copies of POS. Data lost!

**Mistake 2: Not checking if score qualifies**
```basic
INPUT "SCORE";SC
GOSUB 3000: REM Insert score (even if it's 0!)
```
**Fix:** Check `IF SC<=HS(10)` before attempting insert.

**Mistake 3: Initializing with zero scores**
```basic
FOR I=1 TO 10:HS(I)=0:N$(I)="---":NEXT
```
**Problem:** Any score makes the table! Start with reasonable defaults (1000, 2000, etc.).

**Mistake 4: Not handling file-not-found gracefully**
```basic
OPEN 1,8,2,"HISCORES,SEQ,R"
INPUT#1,N$(I),HS(I): REM Crashes if file doesn't exist!
```
**Fix:** Check error channel 15 for error 62, initialize defaults if missing.

### Game Context: How Professionals Used This

**Boulder Dash (1984):**
- Top 5 scores per cave set
- Scores saved to separate file on disk
- "Hall of Fame" screen accessible from menu

**Pac-Man (1983 C64 port):**
- Top 10 scores
- Three-letter initials (like arcade)
- Scores persist across loads

**Impossible Mission (1984):**
- Best times instead of scores
- Separate leaderboards for different difficulty levels

### Progression Notes

**Builds on:**
- L49: Arrays (sorted data structures)
- L50: File I/O (persistence)
- L51: Save systems (validation patterns)

**Leads to:**
- L54: Game state machines (when to check for high score)
- L64: Complete game (high score integration)

### Why It Matters

**Short-term:** High score tables add massive replay value. Players compete with themselves and friends.

**Long-term:** Sorted insertion is a fundamental algorithm you'll use in every language:
- Leaderboards in web apps
- Priority queues
- Keeping sorted lists (cheaper than full re-sort)

The persistence patterns (load on start, save on update) apply to all data-driven apps.

### Reality Check

**What BASIC Does Well:**
- Parallel arrays make this algorithm clean
- Sequential files are perfect for small tables (10-100 entries)
- Easy to debug: just print the arrays

**What BASIC Struggles With:**
- Large leaderboards (1000+ entries) are slow to search
- No binary search (arrays aren't random-access-efficient in BASIC)
- String sorting is awkward (no built-in comparison)

**Could Assembly Help?**
- **Yes, for search:** Binary search in assembly is faster
- **No, for disk:** Still limited by 1541 drive speed
- **Verdict:** For top-10 tables, BASIC is perfect. For MMO-scale leaderboards, you'd need a database anyway.

---

## Section 1 Summary: Data Systems

**Lessons 49-52 taught you:**
- ✅ Organizing complex data with arrays (L49)
- ✅ Reading and writing files (L50)
- ✅ Complete save/load systems with validation (L51)
- ✅ Persistent high score tables with sorting (L52)

**These aren't "toy" features.** They're the foundation of:
- RPGs (character sheets, inventory, world state)
- Adventures (puzzles solved, items collected)
- Strategy games (campaign progress, unit rosters)
- ANY game that lasts more than one sitting

**What's Next:**
Section 2 (L53-56) covers **Screen Systems**: title screens, state machines, menus, and UI. You'll learn how to structure complete games with professional presentation.

---

**End of Section 1: Data Systems**
