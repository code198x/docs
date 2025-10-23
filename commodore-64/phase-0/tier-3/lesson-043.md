# Lesson 043: Turn-Based Combat

**Arc:** Adventure/RPG
**Position:** Lesson 4 of 6 in arc
**Type:** Standard
**Estimated Completion:** 120 lines of code

## Learning Objectives

- Implement turn-based combat system
- Create player and enemy stats (HP, attack, defense)
- Build combat actions (attack, defend, item, flee)
- Design enemy AI for combat decisions
- Balance combat difficulty and player progression

## Prerequisites

**From Previous Lessons:**
- Inventory system for combat items (L41)
- Dialogue system for combat initiation (L42)
- Random number generation (RND function)

**BASIC Knowledge:**
- Turn-based game loops
- Combat math (damage calculation)
- AI decision making

## Key Concepts Introduced

### Combat Stats
Player and enemy have HP (health points), ATK (attack power), DEF (defense). Damage = ATK - DEF with randomness.

### Turn Structure
Player chooses action → action resolves → enemy chooses action → action resolves → check win/lose → repeat until combat ends.

### Combat Actions
**Attack:** Deal damage to opponent. **Defend:** Reduce incoming damage. **Item:** Use healing/buff item. **Flee:** Attempt to escape (chance-based).

### Enemy AI
Simple AI: If HP<30% → heal/defend, else → attack. More complex: Weighted random choices based on situation.

## Code Pattern

```basic
10 REM Turn-based combat system
20 REM Player stats
30 PHP=100:PMAXHP=100:PATK=15:PDEF=5
40 REM Enemy stats (dragon example)
50 EHP=80:EMAXHP=80:EATK=12:EDEF=3:ENAME$="DRAGON"
60 DEFENDING=0:REM Player defending this turn
70 REM Combat loop
80 GOSUB 1000:REM Display combat status
90 REM Player turn
100 GOSUB 2000:REM Player action
110 IF EHP<=0 THEN GOSUB 4000:RETURN:REM Victory
120 REM Enemy turn
130 GOSUB 3000:REM Enemy action
140 IF PHP<=0 THEN GOSUB 5000:RETURN:REM Defeat
150 GOTO 80:REM Next turn
1000 REM Display combat status
1010 PRINT CHR$(147)
1020 PRINT STRING$(40,"=")
1030 PRINT "BATTLE: YOU VS ";ENAME$
1040 PRINT STRING$(40,"=")
1050 PRINT
1060 PRINT "YOUR HP: ";PHP;"/";PMAXHP
1070 PRINT "YOUR ATK: ";PATK;" DEF: ";PDEF
1080 PRINT
1090 PRINT ENAME$;" HP: ";EHP;"/";EMAXHP
1100 PRINT ENAME$;" ATK: ";EATK;" DEF: ";EDEF
1110 PRINT
1120 PRINT STRING$(40,"-")
1130 RETURN
2000 REM Player action
2010 PRINT "YOUR TURN"
2020 PRINT "1. ATTACK"
2030 PRINT "2. DEFEND"
2040 PRINT "3. USE ITEM"
2050 PRINT "4. FLEE"
2060 PRINT:INPUT "CHOICE";CH
2070 IF CH<1 OR CH>4 THEN PRINT "INVALID!":GOTO 2010
2080 IF CH=1 THEN GOSUB 2100:RETURN:REM Attack
2090 IF CH=2 THEN GOSUB 2200:RETURN:REM Defend
2100 IF CH=3 THEN GOSUB 2300:RETURN:REM Item
2110 IF CH=4 THEN GOSUB 2400:RETURN:REM Flee
2100 REM Player attacks
2110 DMG=PATK-EDEF+INT(RND(1)*6)-3:REM Random -3 to +3
2120 IF DMG<1 THEN DMG=1:REM Minimum 1 damage
2130 EHP=EHP-DMG
2140 PRINT:PRINT "YOU ATTACK! DEAL ";DMG;" DAMAGE!"
2150 FOR I=1 TO 100:NEXT I:REM Pause
2160 DEFENDING=0:REM Reset defend flag
2170 RETURN
2200 REM Player defends
2210 DEFENDING=1
2220 PRINT:PRINT "YOU BRACE FOR THE NEXT ATTACK!"
2230 PRINT "DEFENSE DOUBLED FOR THIS TURN."
2240 FOR I=1 TO 100:NEXT I
2250 RETURN
2300 REM Player uses item
2310 PRINT:PRINT "USE WHICH ITEM?"
2320 PRINT "1. HEALTH POTION (+30 HP)"
2330 PRINT "2. ATTACK POTION (+5 ATK FOR 3 TURNS)"
2340 PRINT "3. [CANCEL]"
2350 INPUT IT
2360 IF IT=1 THEN GOSUB 2370:RETURN
2370 IF IT=2 THEN GOSUB 2410:RETURN
2380 PRINT "CANCELLED.":RETURN
2370 REM Use health potion
2380 REM Check if player has potion (inventory check)
2390 HASPOTION=0:REM [Check INV$ from L41]
2400 IF HASPOTION=0 THEN PRINT "YOU DON'T HAVE THAT!":GOTO 2010
2410 PHP=PHP+30:IF PHP>PMAXHP THEN PHP=PMAXHP
2420 PRINT:PRINT "YOU DRINK THE POTION. +30 HP!"
2430 FOR I=1 TO 100:NEXT I
2440 REM Remove potion from inventory
2450 DEFENDING=0
2460 RETURN
2410 REM Use attack potion
2420 PRINT:PRINT "YOU DRINK THE ATTACK POTION!"
2430 PRINT "ATTACK +5 FOR 3 TURNS!"
2440 PATK=PATK+5:BUFF_TURNS=3
2450 FOR I=1 TO 100:NEXT I
2460 DEFENDING=0
2470 RETURN
2400 REM Attempt to flee
2410 FLEE_CHANCE=INT(RND(1)*100)
2420 IF FLEE_CHANCE<40 THEN
2430 PRINT:PRINT "YOU ESCAPED!"
2440 FOR I=1 TO 100:NEXT I
2450 RETURN:REM Exit combat
2460 PRINT:PRINT "COULDN'T ESCAPE!"
2470 FOR I=1 TO 100:NEXT I
2480 DEFENDING=0
2490 RETURN
3000 REM Enemy action (AI)
3010 PRINT:PRINT ENAME$;"'S TURN..."
3020 FOR I=1 TO 50:NEXT I
3030 REM Simple AI logic
3040 IF EHP<EMAXHP*0.3 THEN GOSUB 3100:RETURN:REM Heal if low HP
3050 IF INT(RND(1)*100)<80 THEN GOSUB 3200:RETURN:REM 80% attack
3060 GOSUB 3300:RETURN:REM 20% defend
3100 REM Enemy heals
3110 HEAL=INT(RND(1)*15)+10:REM 10-25 HP
3120 EHP=EHP+HEAL:IF EHP>EMAXHP THEN EHP=EMAXHP
3130 PRINT ENAME$;" HEALS FOR ";HEAL;" HP!"
3140 FOR I=1 TO 100:NEXT I
3150 RETURN
3200 REM Enemy attacks
3210 DEF=PDEF:IF DEFENDING=1 THEN DEF=PDEF*2
3220 DMG=EATK-DEF+INT(RND(1)*6)-3
3230 IF DMG<1 THEN DMG=1
3240 PHP=PHP-DMG
3250 PRINT ENAME$;" ATTACKS! YOU TAKE ";DMG;" DAMAGE!"
3260 IF DEFENDING=1 THEN PRINT "(DEFENSE WAS DOUBLED)"
3270 FOR I=1 TO 100:NEXT I
3280 DEFENDING=0:REM Reset defend
3290 RETURN
3300 REM Enemy defends
3310 PRINT ENAME$;" PREPARES A DEFENSE!"
3320 EDEF=EDEF+3:REM Temporary DEF boost
3330 FOR I=1 TO 100:NEXT I
3340 RETURN
4000 REM Victory
4010 PRINT CHR$(147)
4020 PRINT:PRINT:PRINT
4030 PRINT TAB(10);"VICTORY!"
4040 PRINT:PRINT
4050 PRINT "YOU DEFEATED THE ";ENAME$;"!"
4060 EXP=50:GOLD=100:REM Rewards
4070 PRINT "EARNED: ";EXP;" EXP, ";GOLD;" GOLD"
4080 PRINT:PRINT "PRESS ANY KEY";
4090 GET K$:IF K$="" THEN 4090
4100 RETURN
5000 REM Defeat
5010 PRINT CHR$(147)
5020 PRINT:PRINT:PRINT
5030 PRINT TAB(10);"DEFEATED..."
5040 PRINT:PRINT
5050 PRINT "THE ";ENAME$;" HAS BESTED YOU."
5060 PRINT:PRINT "GAME OVER"
5070 PRINT:PRINT "PRESS ANY KEY TO RESTART";
5080 GET K$:IF K$="" THEN 5080
5090 RUN:REM Restart game
```

## Hardware Interaction

**Chips Involved:**
- None (text-based, turn-based)

**Memory Addresses:**
- Screen memory for combat display
- TI register for RND seed (randomness)

## Common Pitfalls

1. **No damage variance:** Static damage feels robotic (add randomness)
2. **Healing above max:** Not capping HP at MAXHP
3. **Negative damage:** Forgetting to set minimum 1 damage
4. **Instant death:** Damage calculation bug one-shots player
5. **AI too predictable:** Always same action becomes boring

## Extension Ideas

- Add multiple enemy types with different stats/AI
- Add player leveling system (gain ATK/DEF on level up)
- Add status effects (poison, stun, burn)
- Add multi-enemy battles (fight 2-3 enemies)
- Add special attacks (consume MP/stamina)
- Add combo system (chain attacks for bonus)
- Add critical hits (random chance for 2× damage)

## Builds Toward

**In This Tier:**
- L44: Save/load preserves combat stats and progress
- L45: Complete RPG with multiple combat encounters throughout adventure

## Quick Reference

**Combat Math:**
```basic
REM Damage calculation
DMG = ATTACKER_ATK - DEFENDER_DEF + RANDOM(-3 to +3)
IF DMG < 1 THEN DMG = 1 (minimum damage)

REM Healing
HP = HP + HEAL_AMOUNT
IF HP > MAXHP THEN HP = MAXHP

REM Critical hit (10% chance, 2× damage)
IF RND(1) < 0.1 THEN DMG = DMG * 2
```

**Turn Structure:**
```
1. Display status (HP, stats)
2. Player chooses action
3. Execute player action
4. Check if enemy defeated → Victory
5. Enemy chooses action (AI)
6. Execute enemy action
7. Check if player defeated → Defeat
8. Go to step 1 (next turn)
```

**AI Decision Tree:**
```basic
10 IF ENEMY_HP < 30% THEN [heal/defend]
20 IF PLAYER_HP < 25% THEN [aggressive attack]
30 IF RANDOM(1-100) < 80 THEN [attack]
40 ELSE [defend or special]
```

**Combat Balance Tips:**
- **Early enemies:** Low HP (30-50), low ATK (8-12)
- **Mid enemies:** Medium HP (60-80), medium ATK (12-16)
- **Boss enemies:** High HP (100-150), high ATK (16-20)
- **Player progression:** Start 100 HP, 15 ATK, 5 DEF; level up +10 HP, +2 ATK, +1 DEF

**Action Types:**
- **Attack:** Reliable damage, use most turns
- **Defend:** Reduce next hit, use when low HP
- **Item:** Heal or buff, limited by inventory
- **Flee:** Escape unfavorable battle, ~40% success
- **Special:** Cost resource (MP), higher risk/reward

**Status Display:**
```
========================================
BATTLE: YOU VS DRAGON
========================================

YOUR HP: 75/100
YOUR ATK: 15 DEF: 5

DRAGON HP: 45/80
DRAGON ATK: 12 DEF: 3

----------------------------------------
YOUR TURN
1. ATTACK
2. DEFEND
3. USE ITEM
4. FLEE
CHOICE?
```

**Performance Note:**
"Turn-based combat has zero speed pressure. Player reads stats, thinks, chooses action—BASIC handles this perfectly. Combat calculation (damage math, AI decisions) completes instantly. Complex combat systems with multiple enemies, status effects, and deep AI work flawlessly. This is BASIC's sweet spot: turn-based gameplay."
