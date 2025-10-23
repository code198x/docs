# Lesson 042: Dialogue System

**Arc:** Adventure/RPG
**Position:** Lesson 3 of 6 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Implement NPC characters with dialogue
- Create branching conversation trees
- Build quest tracking through dialogue
- Design character interactions and story progression

## Prerequisites

**From Previous Lessons:**
- Room navigation (L40)
- Inventory system (L41)
- Data-driven design (L6, L35)

**BASIC Knowledge:**
- Multi-line dialogue storage
- Choice-based branching
- Quest flag tracking

## Key Concepts Introduced

### NPC Placement
Place NPCs in rooms using RNPC$(room)=NPC name. TALK command initiates conversation with NPC in current room.

### Dialogue Trees
Store conversation as numbered nodes. Each node has text and 2-3 choices. Choices lead to different nodes or end conversation.

### Quest Flags
Track conversation progress with flags: QUESTMET(npc)=has met, QUESTDONE(npc)=quest complete. Dialogue changes based on flags.

### Conditional Responses
NPC responses depend on inventory items, quest status, or game state. Same NPC has different dialogue at different times.

## Code Pattern

```basic
10 REM Dialogue system
20 DIM RNPC$(10):REM NPC in each room
30 DIM NPCNAME$(5):REM NPC names
40 DIM QUESTMET(5):REM Has met NPC
50 DIM QUESTDONE(5):REM Quest completed
60 REM Game state
70 CR=1:HASKEY=0:HASMESSAGE=0
80 REM Initialize
90 GOSUB 1000:REM Place NPCs
100 GOSUB 2000:REM Load NPC data
110 REM Main loop
120 GOSUB 3000:REM Display room (with NPC)
130 PRINT:PRINT "COMMAND (N/S/E/W/TALK/INV/LOOK)";
140 INPUT C$
150 IF C$="TALK" OR C$="T" THEN GOSUB 4000
160 REM Other commands (navigation, inventory, etc.)
170 GOTO 120
1000 REM Place NPCs in rooms
1010 RNPC$(1)="":REM Room 1 - no NPC
1020 RNPC$(2)="OLD WIZARD":REM Room 2 - wizard
1030 RNPC$(3)="":REM Room 3 - empty
1040 RNPC$(4)="KNIGHT":REM Room 4 - knight
1050 RNPC$(5)="MERCHANT":REM Room 5 - merchant
1060 RNPC$(6)="":REM Room 6 - empty
1070 RNPC$(7)="HERMIT":REM Room 7 - hermit
1080 RNPC$(8)="":REM Room 8 - empty
1090 RNPC$(9)="DRAGON":REM Room 9 - dragon (boss)
1100 RNPC$(10)="":REM Room 10 - empty
1110 RETURN
2000 REM Load NPC data
2010 NPCNAME$(1)="OLD WIZARD"
2020 NPCNAME$(2)="KNIGHT"
2030 NPCNAME$(3)="MERCHANT"
2040 NPCNAME$(4)="HERMIT"
2050 NPCNAME$(5)="DRAGON"
2060 REM Initialize quest flags
2070 FOR I=1 TO 5
2080 QUESTMET(I)=0:QUESTDONE(I)=0
2090 NEXT I
2100 RETURN
3000 REM Display room with NPC
3010 PRINT CHR$(147)
3020 PRINT "ROOM ";CR
3030 PRINT STRING$(40,"-")
3040 PRINT "[ROOM DESCRIPTION]"
3050 IF RNPC$(CR)<>"" THEN
3060 PRINT:PRINT "YOU SEE: ";RNPC$(CR)
3070 RETURN
4000 REM Talk to NPC
4010 IF RNPC$(CR)="" THEN PRINT "THERE'S NO ONE HERE.":RETURN
4020 REM Identify which NPC
4030 NPCID=0
4040 FOR I=1 TO 5
4050 IF RNPC$(CR)=NPCNAME$(I) THEN NPCID=I
4060 NEXT I
4070 REM Start conversation with specific NPC
4080 IF NPCID=1 THEN GOSUB 5000:RETURN:REM Wizard
4090 IF NPCID=2 THEN GOSUB 6000:RETURN:REM Knight
4100 IF NPCID=3 THEN GOSUB 7000:RETURN:REM Merchant
4110 IF NPCID=4 THEN GOSUB 8000:RETURN:REM Hermit
4120 IF NPCID=5 THEN GOSUB 9000:RETURN:REM Dragon
4130 RETURN
5000 REM Wizard dialogue
5010 PRINT CHR$(147)
5020 PRINT "OLD WIZARD:"
5030 PRINT STRING$(40,"-")
5040 IF QUESTMET(1)=0 THEN GOSUB 5500:RETURN:REM First meeting
5050 IF QUESTDONE(1)=0 THEN GOSUB 5600:RETURN:REM Quest active
5060 GOSUB 5700:RETURN:REM Quest complete
5500 REM Wizard: First meeting
5510 PRINT "GREETINGS, YOUNG TRAVELLER. I AM"
5520 PRINT "ZARGON THE WISE. I SENSE YOU SEEK"
5530 PRINT "THE ANCIENT ARTIFACT."
5540 PRINT
5550 PRINT "1. 'YES, CAN YOU HELP ME?'"
5560 PRINT "2. 'WHO ARE YOU?'"
5570 PRINT "3. [LEAVE]"
5580 PRINT:INPUT "CHOICE";CH
5590 IF CH=1 THEN GOSUB 5800:RETURN
5600 IF CH=2 THEN GOSUB 5900:RETURN
5610 PRINT "THE WIZARD NODS AND RETURNS TO HIS STUDIES."
5620 RETURN
5600 REM Wizard: Quest active
5610 IF HASKEY=1 THEN GOSUB 5650:RETURN:REM Has key
5620 PRINT "HAVE YOU FOUND THE RUSTY KEY YET?"
5630 PRINT "IT'S IN THE LIBRARY TO THE EAST."
5640 RETURN
5650 REM Wizard: Player has key
5660 PRINT "AH! YOU FOUND IT! THIS KEY OPENS THE"
5670 PRINT "TOWER DOOR. BEWARE WHAT LIES WITHIN."
5680 QUESTDONE(1)=1:HASMESSAGE=1
5690 RETURN
5700 REM Wizard: Quest complete
5710 PRINT "YOU'VE DONE WELL. THE PATH IS OPEN."
5720 PRINT "MAY FORTUNE FAVOR YOU."
5730 RETURN
5800 REM Wizard: Accept quest
5810 PRINT:PRINT "EXCELLENT. FIRST, YOU MUST FIND THE"
5820 PRINT "RUSTY KEY. IT'S HIDDEN IN THE LIBRARY."
5830 PRINT "BRING IT TO ME."
5840 QUESTMET(1)=1
5850 RETURN
5900 REM Wizard: Explain backstory
5910 PRINT:PRINT "I AM THE KEEPER OF ANCIENT KNOWLEDGE."
5920 PRINT "MANY SEEK THE ARTIFACT, BUT FEW ARE"
5930 PRINT "WORTHY. PROVE YOURSELF, AND I SHALL AID YOU."
5940 QUESTMET(1)=1
5950 RETURN
6000 REM Knight dialogue
6010 PRINT CHR$(147)
6020 PRINT "KNIGHT:"
6030 PRINT STRING$(40,"-")
6040 IF QUESTMET(2)=0 THEN
6050 PRINT "HALT! I GUARD THIS PASSAGE. NONE SHALL"
6060 PRINT "PASS WITHOUT THE WIZARD'S BLESSING."
6070 PRINT
6080 IF HASMESSAGE=1 THEN
6090 PRINT "AH, YOU BEAR THE WIZARD'S MARK. YOU MAY"
6100 PRINT "PROCEED. BEWARE THE DRAGON AHEAD."
6110 QUESTMET(2)=1
6120 RETURN
6130 PRINT "RETURN WHEN YOU HAVE PROVEN YOURSELF."
6140 RETURN
6150 PRINT "THE PATH IS CLEAR. GO FORTH, BRAVE ONE."
6160 RETURN
7000 REM Merchant dialogue
7010 PRINT CHR$(147)
7020 PRINT "MERCHANT:"
7030 PRINT STRING$(40,"-")
7040 PRINT "LOOKING TO BUY OR SELL?"
7050 PRINT
7060 PRINT "1. 'WHAT DO YOU HAVE?'"
7070 PRINT "2. 'I'D LIKE TO SELL.'"
7080 PRINT "3. [LEAVE]"
7090 PRINT:INPUT "CHOICE";CH
7100 IF CH=1 THEN GOSUB 7200:RETURN
7110 IF CH=2 THEN GOSUB 7300:RETURN
7120 PRINT "COME BACK ANYTIME!"
7130 RETURN
7200 REM Merchant: Show wares
7210 PRINT:PRINT "I HAVE:"
7220 PRINT "  HEALTH POTION - 50 GOLD"
7230 PRINT "  SILVER KEY - 100 GOLD"
7240 PRINT "  TORCH - 20 GOLD"
7250 PRINT:PRINT "[TRADE SYSTEM NOT YET IMPLEMENTED]"
7260 RETURN
7300 REM Merchant: Buy from player
7310 PRINT:PRINT "I'LL BUY GOLD COINS FOR 10 GOLD EACH."
7320 PRINT "[TRADE SYSTEM NOT YET IMPLEMENTED]"
7330 RETURN
8000 REM Hermit dialogue
8010 PRINT CHR$(147)
8020 PRINT "HERMIT:"
8030 PRINT STRING$(40,"-")
8040 PRINT "THE DRAGON HOARDS THE ARTIFACT YOU SEEK."
8050 PRINT "ONLY THE SILVER KEY OPENS THE VAULT."
8060 PRINT "SEEK THE MERCHANT IN THE EAST."
8070 RETURN
9000 REM Dragon dialogue
9010 PRINT CHR$(147)
9020 PRINT "DRAGON:"
9030 PRINT STRING$(40,"-")
9040 PRINT "SSSSO... ANOTHER FOOLISH MORTAL COMESSS"
9050 PRINT "FOR MY TREASSSURE. PREPARE FOR BATTLE!"
9060 PRINT:PRINT "[COMBAT BEGINS]"
9070 REM Transition to combat (L43)
9080 RETURN
```

## Hardware Interaction

**Chips Involved:**
- None (text-based)

**Memory Addresses:**
- Screen memory for dialogue display
- Keyboard for INPUT

## Common Pitfalls

1. **Dialogue repeats:** Not tracking conversation state (always shows first meeting)
2. **No NPC check:** Trying to talk when no NPC present
3. **Quest logic errors:** Can complete quest without meeting requirements
4. **Infinite loops:** Dialogue choices that loop back to same node forever
5. **Text too fast:** No pause between dialogue pages

## Extension Ideas

- Add multiple dialogue trees per NPC (different topics)
- Add reputation system (NPC friendliness based on actions)
- Add dialogue skill checks (persuasion, intimidation)
- Add time-based dialogue (NPCs say different things at different times)
- Add NPC memory (reference previous conversations)
- Add party members who join through dialogue

## Builds Toward

**In This Tier:**
- L43: Combat initiated through NPC dialogue (boss fights)
- L44: Save/load preserves quest flags and NPC states
- L45: Complete RPG with story-driven NPC interactions

## Quick Reference

**Dialogue Tree Structure:**
```basic
REM Node: Display text + choices
100 PRINT "NPC SAYS: [text]"
110 PRINT "1. [CHOICE A]"
120 PRINT "2. [CHOICE B]"
130 PRINT "3. [CHOICE C]"
140 INPUT CH
150 IF CH=1 THEN GOSUB [node A]
160 IF CH=2 THEN GOSUB [node B]
170 IF CH=3 THEN GOSUB [node C]
```

**Quest Flag Pattern:**
```basic
QUESTMET(npc) = 0/1 (haven't met / have met)
QUESTDONE(npc) = 0/1 (quest active / complete)

REM Dialogue changes based on flags:
IF QUESTMET=0 THEN [first meeting dialogue]
IF QUESTMET=1 AND QUESTDONE=0 THEN [quest active dialogue]
IF QUESTDONE=1 THEN [quest complete dialogue]
```

**Conditional Dialogue:**
```basic
10 IF PLAYER_HAS_ITEM THEN [special dialogue]
20 IF QUEST_FLAG_SET THEN [updated dialogue]
30 IF REPUTATION>10 THEN [friendly dialogue]
40 ELSE [default dialogue]
```

**Dialogue Design Tips:**
- **Short paragraphs:** 2-3 sentences per text block
- **Clear choices:** Label what each option represents
- **Exit option:** Always allow player to leave conversation
- **Feedback:** Confirm player choices ("You agree to help...")
- **Progression:** Dialogue should advance story/quests

**NPC Personality Through Dialogue:**
- **Formal:** "Greetings, traveller. State your business."
- **Friendly:** "Hey there! What brings you by?"
- **Mysterious:** "You seek answers... but are you ready for truth?"
- **Hostile:** "Leave before I make you leave."

**Dialogue State Management:**
```
First meeting → Quest given → Quest active → Quest complete
               ↓
         Alternate paths (reject quest, ask questions)
```

**Branching Patterns:**
- **Linear:** A→B→C→End (tutorial)
- **Branching:** A→B or C→End (player choice matters)
- **Looping:** A→B→back to A (ask multiple questions)
- **Gated:** Must meet condition to access dialogue branch

**Performance Note:**
"Dialogue system is pure text with player INPUT—zero performance impact. Turn-based interaction is BASIC's strength. Complex branching trees with multiple NPCs and quest tracking work flawlessly. No speed pressure whatsoever."
