# Tier 2: Building (Lessons 17-32)

**Philosophy:** Technical depth with sprite mastery, sound, and physics
**Arc Length:** Balanced (4-7 lessons)
**Games Built:** 4 complete games
**Code Range:** 25-150 lines
**Hardware Mastered:** VIC-II sprites, 3-voice SID, joystick control

## Goals

- Master the complete C64 sprite system (8 sprites, hardware collision)
- Learn multi-voice music composition and non-blocking sound
- Understand physics simulation (momentum, acceleration, friction)
- Build progressively complex games that push BASIC further
- **Natural performance awareness:** Students begin experiencing frame rate drops (12-15 fps) with complex games
- Develop professional game programming patterns

## Arcs Overview

### Arc 1: Space Shooter Evolution (L17-23)
**Game:** Galactic Defender (complete shooter, ~150 lines)
**Concepts:** Sprites, joystick, collision detection, AI patterns, animation
**Hardware:** VIC-II sprite system, CIA joystick ports

- **L17:** First Sprite - Single sprite appears and moves
- **L18:** Player Control - Joystick-controlled spaceship
- **L19:** Shooting Gallery - Bullets + collision with targets
- **L20:** Enemy Movement - AI patterns, enemy bullets
- **L21:** Sprite Animation - Multi-frame animated enemies (2-4 frames)
- **L22:** Power-Up System - Collectibles, weapon upgrades, shields
- **L23:** **SYNTHESIS** - Galactic Defender (complete shooter, ~150 lines)

### Arc 2: Sound & Music Mastery (L24-28)
**Tool:** Music Studio with sound effects library
**Concepts:** Multi-voice SID programming, non-blocking music, waveforms, ADSR
**Hardware:** Complete SID chip control (all 3 voices, filters)

- **L24:** Three Voice Player - Chords on all 3 SID voices
- **L25:** Melody Sequencer - 16-step note sequencer
- **L26:** Background Music Player - Non-blocking music during gameplay
- **L27:** Sound Effects Library - 10-12 different game sound effects
- **L28:** Multi-Voice Game Music - 3-voice composition (melody, bass, drums)

### Arc 3: Physics & Movement (L29-32)
**Game:** Asteroids Complete (physics game, ~130 lines)
**Concepts:** Smooth movement, momentum, acceleration, friction, rotation, bounce
**Discovery:** Physics calculations work great in BASIC for this complexity level

- **L29:** Smooth Movement - Perfect 8-way joystick control
- **L30:** Physics Simulation - Momentum, acceleration, friction, bounce
- **L31:** Asteroid Clone Part 1 - Rotation, momentum-based movement
- **L32:** **SYNTHESIS** - Asteroids Complete (physics game, ~130 lines)

## Learning Outcomes

By completing Tier 2, you will have:

- Built **4 complete games** including a full space shooter and Asteroids clone
- Mastered the VIC-II sprite system (positioning, animation, hardware collision)
- Learned joystick control programming (CIA chip reading)
- Composed multi-voice music and integrated it with gameplay
- Implemented physics simulations (momentum, acceleration, rotation)
- Written programs up to 150 lines with complex state management
- **Experienced performance limits naturally** (12-15 fps with many sprites/enemies)
- Developed professional game patterns (non-blocking music, AI, power-ups)

## Prerequisites

**Tier 1 completion required:**
- All BASIC V2 fundamentals
- Basic hardware control (VIC-II colours, screen memory, SID basics)
- GET command and keyboard input
- Simple game loop structure

## Builds Toward

**Tier 3:** Mastery (L33-48) - Professional-quality games (platformer, RPG, puzzle)
**Next Concepts:** Advanced animation, level design, inventory systems, save/load

## Performance Discovery

**Important pedagogical moment:** Tier 2 is where students naturally discover BASIC's speed limits:

- **L17-20:** Simple shooter works fine
- **L21-22:** Adding animation + multiple enemies → slowdown begins
- **L23:** Complete shooter with all features → 12-15 fps (noticeable but playable)
- **L32:** Asteroids clone runs smoothly (fewer moving objects)

**This is intentional.** Students aren't told "BASIC is slow" - they discover it through building increasingly ambitious games. This creates organic motivation for Phase 1 (assembly language).

## Key Mastery Moments

Throughout Tier 2, you'll experience several breakthrough realizations:

1. **L17:** "Sprites are hardware-accelerated - I can move them smoothly!"
2. **L18:** "Joystick control feels like a real arcade game"
3. **L21:** "Animation brings everything to life"
4. **L23:** "I built a complete shooter that could have been sold in the 1980s!"
5. **L26:** "Music during gameplay - now it feels professional"
6. **L30:** "Physics makes movement feel natural and satisfying"
7. **L32:** "Complex games are possible in BASIC - but I'm noticing slowdowns..."

## Teaching Notes

**Arc Structure:**
- **Longer arcs (4-7 lessons):** Build complexity gradually
- **Each arc ends with synthesis:** Complete game using all arc concepts
- **Performance awareness emerges naturally:** Don't preach about speed limits

**Progression Pattern:**
- Arc 1 (L17-23): Foundation gameplay systems (sprites, collision, AI)
- Arc 2 (L24-28): Polish and production value (sound, music)
- Arc 3 (L29-32): Advanced techniques (physics, smooth movement)

**Important:** Frame rate discussion should be observational, not prescriptive. When students notice slowdowns in L23, acknowledge it as a discovery: "Yes, with 7 animated enemies, BASIC manages about 12-15 fps. Still playable, but you've found the limit. Later, we'll learn assembly language which can hit 50/60 fps."

**Games vs Tools:**
- L17-23: Complete game (shooter)
- L24-28: Music tool + library (can be used in any game)
- L29-32: Complete game (Asteroids)

This balance teaches both game development and reusable component creation.
