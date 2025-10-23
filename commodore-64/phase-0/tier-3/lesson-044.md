# Lesson 044: Save/Load System

**Arc:** Adventure/RPG
**Position:** Lesson 5 of 6 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Implement save game to disk
- Create load game from disk
- Serialize game state (position, inventory, flags)
- Handle disk errors gracefully
- Build save/load menu system

## Prerequisites

**From Previous Lessons:**
- Complete RPG systems (L40-43)
- File I/O concepts
- Sequential file access

**BASIC Knowledge:**
- OPEN/CLOSE file operations
- PRINT# and INPUT# for file I/O
- Error handling for disk operations

## Key Concepts Introduced

### Game State Serialization
Identify all variables that define game progress: player position, inventory, quest flags, stats. Write these to sequential file.

### Sequential File Format
Save data line-by-line: room number, HP, gold, inventory items, quest flags. Load in same order.

### Save Slot System
Multiple save files (SAVE1.DAT, SAVE2.DAT, SAVE3.DAT). Player chooses slot to save/load.

### Error Handling
Check for disk errors (no disk, file not found, disk full). Provide clear error messages, don't crash.

## Code Pattern

```basic
10 REM Save/Load system
20 REM Game state variables
30 CR=1:PHP=100:PMAXHP=100:PATK=15:PDEF=5
40 GOLD=0:EXP=0:LEVEL=1
50 DIM INV$(10):INVCOUNT=0
60 DIM QUESTMET(5):QUESTDONE(5)
70 HASKEY=0:HASTORCH=0:TORCHLIT=0
80 REM Save filename
90 SAVEFILE$="SAVEGAME.DAT"
100 REM Main game loop
110 GOSUB 1000:REM Game logic
120 REM Save/Load commands
130 IF C$="SAVE" THEN GOSUB 2000
140 IF C$="LOAD" THEN GOSUB 3000
150 GOTO 110
1000 REM Game logic
1010 REM [Main game code here]
1020 RETURN
2000 REM Save game
2010 PRINT CHR$(147)
2020 PRINT "SAVE GAME"
2030 PRINT STRING$(40,"-")
2040 PRINT:PRINT "SAVING TO DISK..."
2050 REM Open file for writing
2060 OPEN 1,8,2,SAVEFILE$+",S,W"
2070 REM Check for disk error
2080 ST_VAL=ST:IF ST_VAL<>0 THEN GOSUB 4000:RETURN
2090 REM Write player position
2100 PRINT#1,CR
2110 REM Write player stats
2120 PRINT#1,PHP;",";PMAXHP;",";PATK;",";PDEF
2130 PRINT#1,GOLD;",";EXP;",";LEVEL
2140 REM Write inventory
2150 PRINT#1,INVCOUNT
2160 FOR I=1 TO INVCOUNT
2170 PRINT#1,INV$(I)
2180 NEXT I
2190 REM Write quest flags
2200 FOR I=1 TO 5
2210 PRINT#1,QUESTMET(I);",";QUESTDONE(I)
2220 NEXT I
2230 REM Write misc flags
2240 PRINT#1,HASKEY;",";HASTORCH;",";TORCHLIT
2250 REM Close file
2260 CLOSE 1
2270 PRINT:PRINT "GAME SAVED!"
2280 FOR I=1 TO 100:NEXT I
2290 RETURN
3000 REM Load game
3010 PRINT CHR$(147)
3020 PRINT "LOAD GAME"
3030 PRINT STRING$(40,"-")
3040 PRINT:PRINT "LOADING FROM DISK..."
3050 REM Open file for reading
3060 OPEN 1,8,2,SAVEFILE$+",S,R"
3070 REM Check for disk error
3080 ST_VAL=ST:IF ST_VAL<>0 THEN GOSUB 4100:RETURN
3090 REM Read player position
3100 INPUT#1,CR
3110 REM Read player stats
3120 INPUT#1,PHP,PMAXHP,PATK,PDEF
3130 INPUT#1,GOLD,EXP,LEVEL
3140 REM Read inventory
3150 INPUT#1,INVCOUNT
3160 FOR I=1 TO INVCOUNT
3170 INPUT#1,INV$(I)
3180 NEXT I
3190 REM Read quest flags
3200 FOR I=1 TO 5
3210 INPUT#1,QUESTMET(I),QUESTDONE(I)
3220 NEXT I
3230 REM Read misc flags
3240 INPUT#1,HASKEY,HASTORCH,TORCHLIT
3250 REM Close file
3260 CLOSE 1
3270 PRINT:PRINT "GAME LOADED!"
3280 FOR I=1 TO 100:NEXT I
3290 RETURN
4000 REM Save error handler
4010 PRINT:PRINT "ERROR: CANNOT SAVE!"
4020 PRINT "CHECK DISK AND TRY AGAIN."
4030 CLOSE 1:REM Ensure file closed
4040 FOR I=1 TO 150:NEXT I
4050 RETURN
4100 REM Load error handler
4110 PRINT:PRINT "ERROR: NO SAVE FILE FOUND!"
4120 PRINT "START A NEW GAME."
4130 CLOSE 1
4140 FOR I=1 TO 150:NEXT I
4150 RETURN
5000 REM Save slot menu
5010 PRINT CHR$(147)
5020 PRINT "SAVE GAME"
5030 PRINT STRING$(40,"-")
5040 PRINT:PRINT "SELECT SAVE SLOT:"
5050 PRINT "1. SLOT 1"
5060 PRINT "2. SLOT 2"
5070 PRINT "3. SLOT 3"
5080 PRINT "4. [CANCEL]"
5090 INPUT SLOT
5100 IF SLOT<1 OR SLOT>3 THEN RETURN
5110 SAVEFILE$="SAVE"+STR$(SLOT)+".DAT"
5120 GOSUB 2000:REM Save to selected slot
5130 RETURN
5200 REM Load slot menu
5210 PRINT CHR$(147)
5220 PRINT "LOAD GAME"
5230 PRINT STRING$(40,"-")
5240 PRINT:PRINT "SELECT SAVE SLOT:"
5250 PRINT "1. SLOT 1"
5260 PRINT "2. SLOT 2"
5270 PRINT "3. SLOT 3"
5280 PRINT "4. [CANCEL]"
5290 INPUT SLOT
5300 IF SLOT<1 OR SLOT>3 THEN RETURN
5310 SAVEFILE$="SAVE"+STR$(SLOT)+".DAT"
5320 GOSUB 3000:REM Load from selected slot
5330 RETURN
6000 REM Auto-save feature
6010 REM Called automatically after major events
6020 SAVEFILE$="AUTOSAVE.DAT"
6030 GOSUB 2000
6040 PRINT "(AUTO-SAVED)"
6050 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **Disk Drive (1541)** - File I/O operations

**Memory Addresses:**
- None directly (uses KERNAL routines)

**Disk Operations:**
- OPEN channel to disk drive (device 8)
- PRINT# writes data to file
- INPUT# reads data from file
- CLOSE closes file channel
- ST status variable checks for errors

## Common Pitfalls

1. **No error checking:** Disk errors crash program instead of graceful message
2. **Write/read mismatch:** Saving 5 values but loading 6 causes data corruption
3. **String truncation:** Long strings split across lines when reading
4. **File not closed:** CLOSE 1 not called, disk drive left in bad state
5. **Overwriting autosave:** Losing progress by accidentally overwriting save

## Extension Ideas

- Add save file preview (show level, location, time saved)
- Add quicksave/quickload (F1/F3 keys)
- Add multiple save slots (3-5 slots)
- Add autosave on level completion
- Add save file validation (checksum to detect corruption)
- Add compress save data (reduce disk space)

## Builds Toward

**In This Tier:**
- L45: Complete RPG with save/load integrated into full game loop

## Quick Reference

**File I/O Commands:**
```basic
REM Open file for writing
OPEN 1,8,2,"FILENAME,S,W"

REM Write data
PRINT#1,VALUE
PRINT#1,STRING$

REM Close file
CLOSE 1

REM Open file for reading
OPEN 1,8,2,"FILENAME,S,R"

REM Read data
INPUT#1,VARIABLE
INPUT#1,STRING_VAR$

REM Check for error
IF ST<>0 THEN [error handler]
```

**Save File Structure:**
```
Line 1: Current room number
Line 2: HP, MAXHP, ATK, DEF (comma-separated)
Line 3: Gold, EXP, Level
Line 4: Inventory count
Lines 5-14: Inventory items (one per line)
Lines 15-19: Quest flags (QUESTMET, QUESTDONE pairs)
Line 20: Misc flags (HASKEY, HASTORCH, etc.)
```

**Serialization Pattern:**
```basic
REM Identify all game state:
- Player position (room/coordinates)
- Player stats (HP, ATK, DEF, Level, EXP, Gold)
- Inventory (items array + count)
- Quest progress (flags array)
- World state (doors unlocked, enemies defeated, etc.)
- Misc flags (keys, torches, etc.)

REM Save order = Load order (critical!)
```

**Error Handling:**
```basic
10 OPEN 1,8,2,FILENAME$+",S,W"
20 IF ST<>0 THEN PRINT "DISK ERROR!":CLOSE 1:RETURN
30 REM Proceed with file operations
40 CLOSE 1
```

**Multiple Save Slots:**
```
SAVE1.DAT - Slot 1
SAVE2.DAT - Slot 2
SAVE3.DAT - Slot 3
AUTOSAVE.DAT - Auto-save (overwritten regularly)
```

**Best Practices:**
- **Save often:** Allow save at any time (not just checkpoints)
- **Autosave:** Save automatically after major events
- **Feedback:** Show "Saving..." and "Saved!" messages
- **Error recovery:** Don't crash on disk error, show message
- **Test thoroughly:** Load old saves to verify compatibility

**Disk Status (ST) Values:**
```
0 = OK
64 = End of file
-128 = Time out (no disk)
Other values = Various disk errors
```

**Save File Size Estimation:**
```
Typical RPG save: 50-200 bytes
- Room number: 1-2 bytes
- Stats: 20-30 bytes
- Inventory: 50-100 bytes
- Flags: 10-20 bytes
- Strings: Variable (item names, etc.)

1541 disk capacity: ~170KB (plenty of space!)
```

**Performance Note:**
"Save/load operations take 1-3 seconds (disk I/O speed). This is acceptable for turn-based RPGs—player saves between actions. No impact on gameplay performance. Disk errors (no disk, file not found) must be handled gracefully with clear messages."
