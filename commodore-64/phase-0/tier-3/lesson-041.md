# Lesson 041: Inventory System

**Arc:** Adventure/RPG
**Position:** Lesson 2 of 6 in arc
**Type:** Standard
**Estimated Completion:** 90 lines of code

## Learning Objectives

- Implement player inventory with multiple items
- Create item collection and usage mechanics
- Build item inspection and management commands
- Design item-based puzzle solving

## Prerequisites

**From Previous Lessons:**
- Room navigation system (L40)
- Data-driven design (L6, L35)
- Array management

**BASIC Knowledge:**
- Dynamic arrays for inventory
- Item properties (name, description, usable)
- Command parsing for item actions

## Key Concepts Introduced

### Inventory Array
Track items player carries using arrays: IID$(slot)=item name, IHAVE(itemID)=count. Support multiple copies of items.

### Item Placement
Place items in rooms using RIT$(room)=item name. When player enters room, show item. TAKE command adds to inventory.

### Item Usage
USE command with item name. Check if player has item, apply effects (unlock door, heal, light torch). Remove consumable items.

### Inventory Limit
Maximum carrying capacity (e.g., 10 items). Must drop items to pick up new ones if at limit.

## Code Pattern

```basic
10 REM Inventory system
20 MAXITEMS=10:INVCOUNT=0
30 DIM INV$(10):REM Inventory slots
40 DIM IIT$(10):REM Items in rooms (room → item name)
50 DIM IDESC$(20):REM Item descriptions (item ID → description)
60 DIM INAME$(20):REM Item names (item ID → name)
70 REM Game state
80 CR=1:HASKEY=0:HASTORCH=0:TORCHLIT=0
90 REM Initialize
100 GOSUB 1000:REM Load item data
110 GOSUB 2000:REM Place items in rooms
120 REM Main loop
130 GOSUB 3000:REM Display room (with items)
140 PRINT:PRINT "COMMAND (N/S/E/W/TAKE/USE/INV/LOOK/QUIT)";
150 INPUT C$
160 REM Navigation commands
170 IF C$="N" OR C$="S" OR C$="E" OR C$="W" THEN GOSUB 4000
180 REM Inventory commands
190 IF C$="TAKE" THEN GOSUB 5000
200 IF C$="USE" THEN GOSUB 6000
210 IF C$="INV" OR C$="I" THEN GOSUB 7000
220 IF C$="LOOK" THEN GOSUB 3000
230 IF C$="QUIT" THEN PRINT "GOODBYE!":END
240 GOTO 130
1000 REM Load item data
1010 REM Item 1: Rusty Key
1020 INAME$(1)="RUSTY KEY"
1030 IDESC$(1)="AN OLD RUSTY KEY. IT MIGHT UNLOCK SOMETHING."
1040 REM Item 2: Torch
1050 INAME$(2)="TORCH"
1060 IDESC$(2)="A WOODEN TORCH. USE IT TO LIGHT DARK AREAS."
1070 REM Item 3: Health Potion
1080 INAME$(3)="HEALTH POTION"
1090 IDESC$(3)="A RED POTION. RESTORES 20 HP WHEN USED."
1100 REM Item 4: Ancient Scroll
1110 INAME$(4)="ANCIENT SCROLL"
1120 IDESC$(4)="A YELLOWED SCROLL WITH ARCANE WRITING."
1130 REM Item 5: Gold Coin
1140 INAME$(5)="GOLD COIN"
1150 IDESC$(5)="A SHINY GOLD COIN. MIGHT BE VALUABLE."
1160 REM Item 6: Silver Key
1170 INAME$(6)="SILVER KEY"
1180 IDESC$(6)="AN ORNATE SILVER KEY."
1190 RETURN
2000 REM Place items in rooms
2010 IIT$(1)="":REM Room 1 (entrance) - no item
2020 IIT$(2)="TORCH":REM Room 2 - torch
2030 IIT$(3)="RUSTY KEY":REM Room 3 - key
2040 IIT$(4)="":REM Room 4 - empty
2050 IIT$(5)="HEALTH POTION":REM Room 5 - potion
2060 IIT$(6)="ANCIENT SCROLL":REM Room 6 - scroll
2070 IIT$(7)="GOLD COIN":REM Room 7 - coin
2080 IIT$(8)="":REM Room 8 - empty
2090 IIT$(9)="SILVER KEY":REM Room 9 - silver key
2100 IIT$(10)="":REM Room 10 - empty
2110 RETURN
3000 REM Display room with items
3010 PRINT CHR$(147)
3020 PRINT "ROOM ";CR
3030 PRINT STRING$(40,"-")
3040 REM Room description (from L40)
3050 PRINT "[ROOM DESCRIPTION HERE]"
3060 PRINT STRING$(40,"-")
3070 REM Show item if present
3080 IF IIT$(CR)<>"" THEN
3090 PRINT:PRINT "YOU SEE: ";IIT$(CR)
3100 RETURN
4000 REM Navigation (simplified from L40)
4010 REM [Handle N/S/E/W movement]
4020 RETURN
5000 REM Take item
5010 IF IIT$(CR)="" THEN PRINT "THERE'S NOTHING TO TAKE.":RETURN
5020 IF INVCOUNT>=MAXITEMS THEN PRINT "INVENTORY FULL!":RETURN
5030 REM Add to inventory
5040 INVCOUNT=INVCOUNT+1
5050 INV$(INVCOUNT)=IIT$(CR)
5060 PRINT "YOU TAKE THE ";IIT$(CR);"."
5070 IIT$(CR)="":REM Remove from room
5080 RETURN
6000 REM Use item
6010 PRINT "USE WHAT";
6020 INPUT IT$
6030 REM Check if player has item
6040 HASITEM=0
6050 FOR I=1 TO INVCOUNT
6060 IF INV$(I)=IT$ THEN HASITEM=I
6070 NEXT I
6080 IF HASITEM=0 THEN PRINT "YOU DON'T HAVE THAT.":RETURN
6090 REM Apply item effects
6100 IF IT$="RUSTY KEY" THEN GOSUB 8000:RETURN
6110 IF IT$="TORCH" THEN GOSUB 8100:RETURN
6120 IF IT$="HEALTH POTION" THEN GOSUB 8200:RETURN
6130 IF IT$="ANCIENT SCROLL" THEN GOSUB 8300:RETURN
6140 IF IT$="SILVER KEY" THEN GOSUB 8400:RETURN
6150 PRINT "YOU CAN'T USE THAT HERE."
6160 RETURN
7000 REM Show inventory
7010 PRINT CHR$(147)
7020 PRINT "INVENTORY (";INVCOUNT;"/";MAXITEMS;" ITEMS)"
7030 PRINT STRING$(40,"-")
7040 IF INVCOUNT=0 THEN PRINT "EMPTY":GOTO 7080
7050 FOR I=1 TO INVCOUNT
7060 PRINT I;". ";INV$(I)
7070 NEXT I
7080 PRINT STRING$(40,"-")
7090 PRINT:PRINT "PRESS ANY KEY";
7100 GET K$:IF K$="" THEN 7100
7110 RETURN
8000 REM Use rusty key
8010 IF CR=4 THEN PRINT "YOU UNLOCK THE TOWER DOOR!":HASKEY=1:RETURN
8020 PRINT "THE KEY DOESN'T FIT ANY LOCK HERE."
8030 RETURN
8100 REM Use torch
8110 IF TORCHLIT=1 THEN PRINT "THE TORCH IS ALREADY LIT.":RETURN
8120 PRINT "YOU LIGHT THE TORCH. THE DARKNESS RECEDES."
8130 TORCHLIT=1
8140 RETURN
8200 REM Use health potion
8210 PRINT "YOU DRINK THE POTION. YOU FEEL BETTER! (+20 HP)"
8220 HP=HP+20:IF HP>MAXHP THEN HP=MAXHP
8230 REM Remove potion from inventory (consumable)
8240 FOR I=HASITEM TO INVCOUNT-1
8250 INV$(I)=INV$(I+1)
8260 NEXT I
8270 INVCOUNT=INVCOUNT-1
8280 RETURN
8300 REM Use ancient scroll
8310 PRINT "THE SCROLL READS: 'THE SILVER KEY OPENS"
8320 PRINT "THE TREASURE VAULT. SEEK IT IN THE EAST.'"
8330 RETURN
8400 REM Use silver key
8410 IF CR=9 THEN PRINT "THE VAULT OPENS!":VAULTOPEN=1:RETURN
8420 PRINT "NO LOCK HERE FOR THIS KEY."
8430 RETURN
```

## Hardware Interaction

**Chips Involved:**
- None (text-based)

**Memory Addresses:**
- Screen memory for text display
- Keyboard for INPUT/GET

## Common Pitfalls

1. **Items disappear:** Not checking if slot is empty before displaying
2. **Duplicate items:** Taking same item twice without removing from room
3. **Can't drop items:** No DROP command to free inventory space
4. **Consumables persist:** Potions/scrolls not removed after use
5. **Case sensitivity:** "Torch" vs "TORCH" vs "torch" not matching

## Extension Ideas

- Add DROP command to remove items from inventory
- Add EXAMINE command for detailed item descriptions
- Add item combinations (USE X WITH Y)
- Add quest items that trigger events
- Add weight system (heavy items take multiple slots)
- Add item durability (weapons break after use)
- Add container items (bag holds more items)

## Builds Toward

**In This Tier:**
- L42: NPCs who want specific items (trading)
- L43: Combat items (weapons, armor, potions)
- L44: Save/load preserves inventory
- L45: Complete RPG with item-driven puzzles

## Quick Reference

**Inventory Data Structure:**
```basic
INV$(slot) = Item name in slot (1 to INVCOUNT)
INVCOUNT = Number of items currently held
MAXITEMS = Maximum carrying capacity
IIT$(room) = Item present in room (empty string = none)
```

**Take Item Pattern:**
```basic
10 IF NO_ITEM_IN_ROOM THEN [message]:RETURN
20 IF INVENTORY_FULL THEN [message]:RETURN
30 ADD_TO_INVENTORY(ITEM)
40 REMOVE_FROM_ROOM
```

**Use Item Pattern:**
```basic
10 INPUT ITEM_NAME$
20 FIND_IN_INVENTORY(ITEM_NAME$)
30 IF NOT_FOUND THEN [message]:RETURN
40 IF ITEM_NAME$="X" THEN GOSUB [use_X]
50 IF CONSUMABLE THEN REMOVE_FROM_INVENTORY
```

**Item Effect Types:**
- **Key items:** Unlock doors/areas (persist after use)
- **Consumables:** Heal/boost (removed after use)
- **Quest items:** Trigger events (persist)
- **Information:** Provide clues (persist)
- **Tools:** Enable actions (persist)

**Inventory Management:**
```basic
REM Add item
10 INVCOUNT=INVCOUNT+1
20 INV$(INVCOUNT)=ITEM_NAME$

REM Remove item from slot N
10 FOR I=N TO INVCOUNT-1
20 INV$(I)=INV$(I+1)
30 NEXT I
40 INVCOUNT=INVCOUNT-1

REM Check if player has item
10 FOR I=1 TO INVCOUNT
20 IF INV$(I)=SEARCH_ITEM$ THEN FOUND=I
30 NEXT I
```

**Command Parsing Tips:**
- Accept abbreviations: "I" for "INV", "T" for "TAKE"
- Case insensitive: Convert to uppercase with `C$=LEFT$(C$,1)`
- Full words: "TAKE TORCH" vs just "TAKE" then prompt
- Error messages: Clear feedback for invalid commands

**Item Placement Strategy:**
- **Tutorial area:** Obvious items (torch in plain sight)
- **Exploration reward:** Hidden items (search to find)
- **Puzzle solution:** Items needed for specific obstacles
- **Optional:** Power-ups not required to finish game

**Performance Note:**
"Inventory system adds negligible overhead—string array lookups are fast. Text-based interaction means zero speed pressure. Player reads descriptions, types commands—BASIC handles this perfectly. Turn-based gameplay is where BASIC shines."
