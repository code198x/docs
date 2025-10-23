# Lesson 027: Sound Effects Library

**Arc:** Sound & Music Mastery
**Position:** Lesson 4 of 5 in arc
**Type:** Standard
**Estimated Completion:** 45 lines of code

## Learning Objectives

- Create comprehensive game sound effects library (10-12 effects)
- Learn sound design principles for different game events
- Implement sound priority system (effects vs music)
- Build reusable SFX subroutines

## Prerequisites

**From Previous Lessons:**
- Basic sound effects (L11)
- Multi-voice SID (L24)
- Non-blocking music (L26)

**BASIC Knowledge:**
- SID programming
- Subroutines (GOSUB/RETURN)
- Voice allocation

## Key Concepts Introduced

### Comprehensive SFX Categories
UI sounds (menu, select), combat sounds (hit, explosion), movement sounds (jump, land), collection sounds (coin, powerup), ambient sounds (door, switch).

### Sound Priority
When music playing, temporarily use voice for effect then return to music. Or dedicate voice 2 for effects, voice 3 for music.

### SFX Design Principles
Short duration (<0.5 sec), distinctive tones, appropriate waveforms, clear purpose. Player should instantly recognize what happened.

### Effect Layering
Some effects use 2 voices simultaneously for richer sound (explosion = noise + falling tone).

## Code Pattern

```basic
10 REM Sound Effects Library - Call via GOSUB
1000 REM Jump sound
1010 POKE 54296,15:POKE 54279,0:POKE 54280,10
1020 FOR F=100 TO 200 STEP 10
1030 POKE 54279,F:POKE 54283,17:FOR D=1 TO 5:NEXT D:NEXT F
1040 POKE 54283,16:RETURN
1100 REM Coin collect
1110 POKE 54279,100:POKE 54280,40:POKE 54283,65
1120 FOR D=1 TO 50:NEXT D:POKE 54279,150:POKE 54280,50
1130 FOR D=1 TO 50:NEXT D:POKE 54283,64:RETURN
1200 REM Explosion (uses 2 voices)
1210 POKE 54283,129:POKE 54290,129:REM Noise on V2+V3
1220 FOR D=1 TO 150:NEXT D
1230 POKE 54283,128:POKE 54290,128:RETURN
1300 REM Laser shoot
1310 FOR F=200 TO 50 STEP -10
1320 POKE 54279,F:POKE 54283,33:FOR D=1 TO 3:NEXT D:NEXT F
1330 POKE 54283,32:RETURN
1400 REM Menu select
1410 POKE 54279,100:POKE 54280,20:POKE 54283,65
1420 FOR D=1 TO 30:NEXT D:POKE 54283,64:RETURN
```

## Hardware Interaction

**Chips Involved:**
- **SID** - Voices 1-3 for various effects

**Memory Addresses:**
- All SID voice registers
- Voice 2 (54279+) recommended for effects during music

## Common Pitfalls

1. **Effects too long:** >0.5 sec feels sluggish, player waiting for feedback
2. **Effects interrupt music badly:** Need quick restore or dedicated voice
3. **Similar sounds:** Jump and bounce should sound different
4. **Volume inconsistency:** All effects should be similar volume
5. **Blocking gameplay:** Effect playback shouldn't freeze game

## Extension Ideas

- Add stereo panning (voice 1=left, voice 3=right feel)
- Add reverb/echo effects
- Randomize pitch slightly per effect (variety)
- Add effect variations (hit1, hit2, hit3)
- Create ambient loops (background sound)
- Add volume control (quiet mode)

## Builds Toward

**In This Tier:**
- L28: Integrate all sound with 3-voice music

## Quick Reference

**Effect Categories:**

**UI Sounds:**
- Menu select: Short beep (100ms)
- Menu move: Quiet tick
- Confirm: Rising tone
- Cancel: Falling tone

**Combat Sounds:**
- Player shoot: Descending sawtooth
- Enemy shoot: Ascending sawtooth
- Hit: Short noise burst
- Explosion: Long noise + falling pitch
- Death: Complex descending sequence

**Movement Sounds:**
- Jump: Rising triangle
- Land: Short pulse thud
- Walk: Quiet pulse ticks
- Dash: Whoosh (fast sweep)

**Collection Sounds:**
- Coin: Two-note rising pulse
- Powerup: Ascending arpeggio
- Extra life: Jingle melody
- Key/item: Distinctive chime

**Ambient Sounds:**
- Door open: Rising noise
- Switch: Click pulse
- Alarm: Alternating tones
- Warp: Whooshing sweep

**Sound Design Formula:**
```
Duration: 50-300ms (target)
Waveform: Match event type
Frequency: Distinctive per category
Envelope: Quick attack/release
```

**Voice Allocation Strategy:**
```
Voice 1: Critical player feedback
Voice 2: Effects during music
Voice 3: Background music
```

See previous SFX lessons (L11) for basic patterns
