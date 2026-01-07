# SID Symphony: 64-Unit Outline

**Game:** C64 Game 1: SID Symphony
**Units:** 64
**Concept:** Rhythm game - notes scroll across three tracks, hit the correct key when notes reach the hit zone. Guitar Hero on the C64.

**Commercial Quality Target:** A game that could have sold for £9.99 on cassette in 1986. Polished, replayable, impressive to show friends.

---

## The Finished Game

Before detailing the units, here's what the learner builds:

### Core Gameplay
- Three note tracks (high, mid, low) corresponding to three SID voices
- Notes scroll right-to-left toward a hit zone
- Player presses Z/X/C (or joystick positions) to hit notes
- Timing matters: Perfect, Good, Miss ratings
- Combo system rewards consecutive hits
- Health/performance meter - too many misses ends the song

### Content
- 5 complete songs of varying difficulty
- 3 difficulty levels per song (Easy/Normal/Hard)
- Practice mode (slow speed, no fail)
- Career mode (unlock songs by completing previous)
- Endless mode (procedurally generated patterns)

### Audio
- Full SID music (not just beeps - actual composed tracks)
- Note sounds match the music when hit correctly
- Miss sounds (dissonant buzz)
- Voice synthesis for "Perfect!" "Miss!" callouts
- Sound effects layered on top of music

### Visuals
- Custom character set for notes, tracks, UI
- Animated hit zone (pulsing to beat)
- Screen flash on perfect hits
- Sprite-based effects for combos
- Colour cycling backgrounds
- Smooth note scrolling

### Polish
- Title screen with animated logo
- Attract mode (demo playback)
- High score table with name entry
- Options screen (difficulty, sound test)
- Pause functionality
- Credits sequence

---

## Phase 1: Foundation (Units 1-16)

*Goal: A working rhythm game with one song. Playable from start to finish.*

*By the end of this phase, the learner has built a complete, if simple, game. They understand the SID chip fundamentals, basic 6510 assembly, and the core game loop pattern. The game is playable and winnable/losable.*

---

### Unit 1: First Sound

**Learning Objectives:**
- Understand the BASIC stub that launches machine code
- Know the SID chip's memory location ($D400-$D41C)
- Write to SID registers to produce a tone
- Create a working assembly program that runs on the C64

**Concepts Introduced:**
- Memory-mapped I/O
- The SID's three voices
- Frequency registers (low/high byte pairs)
- Gate bit (turning sound on/off)

**Code Written:**
```
- BASIC stub (10 SYS 2064)
- Set SID frequency registers for voice 1
- Set waveform (pulse wave)
- Set gate bit to trigger sound
- Infinite loop to keep program running
```

**What the Learner Sees:**
A blank screen, but a continuous tone plays from the SID. Changing values changes the pitch. First contact with the SID chip.

**Technical Details:**
- SID base: $D400
- Voice 1 frequency: $D400-$D401
- Voice 1 control: $D404
- Gate bit is bit 0 of control register

---

### Unit 2: The Three Voices

**Learning Objectives:**
- Configure all three SID voices independently
- Understand waveform selection (triangle, sawtooth, pulse, noise)
- Hear the characteristic sound of each waveform
- Play a chord (three simultaneous notes)

**Concepts Introduced:**
- Voice register offsets (+7 per voice)
- Waveform bits in control register
- Pulse width for pulse wave
- How voices sum together

**Code Written:**
```
- Configure voice 1: triangle wave, middle C
- Configure voice 2: sawtooth wave, E above middle C
- Configure voice 3: pulse wave, G above middle C
- Gate all three simultaneously
```

**What the Learner Sees:**
A C major chord plays continuously. The learner experiments with different waveforms and hears how triangle sounds flute-like, sawtooth sounds brassy, pulse sounds hollow, and noise sounds like static.

**Technical Details:**
- Waveform bits: triangle=$11, sawtooth=$21, pulse=$41, noise=$81
- Voice offsets: voice 1=$D400, voice 2=$D407, voice 3=$D40E
- Pulse width: $D402-$D403 (12-bit value)

---

### Unit 3: ADSR Envelopes

**Learning Objectives:**
- Understand Attack, Decay, Sustain, Release
- Shape sounds from harsh stabs to soft pads
- Create distinct timbres for each voice
- Hear how envelope affects musical expression

**Concepts Introduced:**
- ADSR register layout (4 bits each)
- Time values for each stage
- How sustain level affects volume
- Why release matters for musical sounds

**Code Written:**
```
- Voice 1: fast attack, no decay, full sustain (organ-like)
- Voice 2: slow attack, medium decay, low sustain (string-like)
- Voice 3: instant attack, fast decay, no sustain (pluck-like)
- Play chord, release after 1 second to hear release phase
```

**What the Learner Sees:**
Three very different sounding notes despite same waveforms. The pluck fades quickly, the string swells in, the organ sustains. First taste of sound design.

**Technical Details:**
- Attack/Decay register: $D405 (voice 1), +7 for others
- Sustain/Release register: $D406 (voice 1), +7 for others
- Values 0-15 for each parameter
- Attack 0 = 2ms, Attack 15 = 8 seconds

---

### Unit 4: Playing a Scale

**Learning Objectives:**
- Calculate frequency values for musical notes
- Build a note table for one octave
- Play notes in sequence with timing
- Introduce the concept of a frame-based timer

**Concepts Introduced:**
- Frequency = (note_value * clock) / 16777216
- Lookup tables for efficiency
- Frame counting for timing
- Raster wait for consistent speed

**Code Written:**
```
- Note frequency table (C4 through B4, 12 notes)
- Play routine: load note, set frequency, gate on
- Simple delay loop (wait N frames)
- Scale plays automatically on startup
```

**What the Learner Sees:**
A musical scale plays: C-D-E-F-G-A-B-C, one note per beat. First recognisable melody from their code.

**Technical Details:**
- C4 = $1168 (4456 decimal)
- Each semitone multiplies by 2^(1/12) ≈ 1.0595
- 50 frames = 1 second on PAL C64
- Raster register: $D012

---

### Unit 5: Screen Layout

**Learning Objectives:**
- Clear the screen efficiently
- Set border and background colours
- Use PETSCII characters for basic graphics
- Plan screen layout for the game

**Concepts Introduced:**
- Screen memory at $0400
- Colour RAM at $D800
- Border ($D020) and background ($D021)
- Screen dimensions: 40x25 characters

**Code Written:**
```
- Clear screen routine (fill $0400-$07E7 with spaces)
- Set all colour RAM to chosen colour
- Draw three horizontal lines for tracks (rows 8, 12, 16)
- Draw hit zone column (column 4)
- Reserve top row for score display
```

**What the Learner Sees:**
Three horizontal tracks across the screen with a vertical hit zone on the left. Score area at top. The skeleton of the game screen.

**Layout:**
```
SCORE: 000000              HI: 000000
________________________________________
        [============================]  <- Track 1
        |
        [============================]  <- Track 2
        |
        [============================]  <- Track 3
        |
        Hit Zone
________________________________________
HEALTH: ████████
```

---

### Unit 6: Custom Characters

**Learning Objectives:**
- Understand character ROM and RAM
- Design custom characters for notes
- Copy character set to RAM for modification
- Switch VIC-II to use custom characters

**Concepts Introduced:**
- Character memory pointer (VIC $D018)
- 8 bytes per character definition
- Designing on 8x8 grid
- Bank selection basics

**Code Written:**
```
- Copy ROM character set to $3000
- Define note character (filled circle or arrow)
- Define track characters (horizontal line variants)
- Define hit zone characters
- Point VIC to new character set
```

**What the Learner Sees:**
The same layout as Unit 5, but now with custom graphics. Notes will be distinctive shapes, tracks have custom line graphics, hit zone has a unique marker.

**Character Designs:**
- Note: solid circle or chevron pointing left
- Track: thin horizontal line
- Hit zone: vertical bar with glow effect
- Perfect/Good/Miss indicators

---

### Unit 7: The Game Loop

**Learning Objectives:**
- Structure code as initialisation + main loop
- Synchronise to raster for consistent timing
- Count frames for game speed control
- Handle clean program exit

**Concepts Introduced:**
- Init-once vs every-frame code
- Raster synchronisation techniques
- Frame counter variable
- Beat timing (frames per beat)

**Code Written:**
```
- init: subroutine for one-time setup
- main_loop: the repeating game code
- wait_raster: sync to specific raster line
- frame_counter: increments each frame
- beat_counter: triggers every N frames
- Check for Q key to exit
```

**What the Learner Sees:**
The game screen sits stable with no flickering. A counter (displayed for debugging) increments smoothly. The foundation for all game logic.

**Technical Details:**
- Wait for raster 255 before processing
- BPM to frames: 120 BPM = 25 frames per beat (PAL)
- Use zero page for frequently accessed variables

---

### Unit 8: Note Data Structure

**Learning Objectives:**
- Design a data format for song notes
- Understand the trade-offs in data representation
- Create a simple test song
- Calculate memory requirements

**Concepts Introduced:**
- Parallel arrays vs structs
- Beat-relative timing
- Track assignment (1, 2, or 3)
- End-of-song marker

**Code Written:**
```
- song_beats: array of beat numbers when notes appear
- song_tracks: array of which track (1-3)
- song_notes: array of SID note values
- song_length: total beats in song
- Test song: 32 beats, 16 notes, simple pattern
```

**Data Format:**
```
; Beat 0: note on track 2
; Beat 4: note on track 1
; Beat 8: note on track 3
; etc.

song_data:
    !byte 0, 2, $24    ; beat, track, note
    !byte 4, 1, $30    ; beat, track, note
    !byte 8, 3, $18    ; beat, track, note
    ...
    !byte $FF          ; end marker
```

**What the Learner Sees:**
No visual change yet - data structures are invisible. But the song is defined and ready to drive the game.

---

### Unit 9: Spawning Notes

**Learning Objectives:**
- Read song data at the right time
- Create visual notes on screen
- Track active notes in memory
- Limit simultaneous notes for performance

**Concepts Introduced:**
- Song playhead (current beat position)
- Active note array
- Spawning at right edge of screen
- Finding free slots in arrays

**Code Written:**
```
- song_position: current beat in song
- active_notes: array of 8 note structures
- spawn_note: create new note from song data
- Check song data each beat
- Place note character at right edge of correct track
```

**What the Learner Sees:**
Notes appear at the right edge of the screen on the correct track, synchronised to the beat. They don't move yet - just pop into existence.

**Technical Details:**
- Maximum 8 active notes (one per possible screen column in hit zone)
- Note structure: x_position, track, note_value, active_flag
- Spawn at x=39 (rightmost column)

---

### Unit 10: Moving Notes

**Learning Objectives:**
- Animate notes across the screen
- Calculate timing so notes hit the zone on beat
- Remove notes that pass the hit zone
- Handle smooth visual movement

**Concepts Introduced:**
- Per-frame position updates
- Pixels vs characters for movement
- Character position calculation
- Off-screen cleanup

**Code Written:**
```
- update_notes: move all active notes left
- Calculate scroll speed from BPM and distance
- Erase old position, draw new position
- Deactivate notes that pass x=0
- Sync so note reaches hit zone on its beat
```

**What the Learner Sees:**
Notes scroll smoothly from right to left across their tracks, reaching the hit zone exactly on the beat. The game is starting to look like a rhythm game.

**Technical Details:**
- Hit zone at column 4
- Columns to travel: 35
- At 120 BPM, 25 frames per beat
- Multiple notes can be on screen simultaneously

---

### Unit 11: Keyboard Input

**Learning Objectives:**
- Read the C64 keyboard matrix
- Detect specific key presses (Z, X, C)
- Debounce to avoid repeated triggers
- Provide visual feedback for input

**Concepts Introduced:**
- CIA keyboard scanning ($DC00-$DC01)
- Matrix row and column selection
- Key state vs key transition
- Input visualization

**Code Written:**
```
- scan_keyboard: read key matrix
- check_z, check_x, check_c: specific key routines
- key_state: previous frame's key status
- key_pressed: newly pressed this frame
- Flash hit zone row when key pressed
```

**What the Learner Sees:**
Pressing Z, X, or C causes the corresponding track's hit zone to flash. The game responds to input. Notes still scroll past without interaction.

**Technical Details:**
- Z = row 1, col 4
- X = row 2, col 7
- C = row 2, col 4
- Store previous state to detect edges

---

### Unit 12: Hit Detection

**Learning Objectives:**
- Detect when a key press coincides with a note
- Implement timing windows for accuracy
- Trigger correct SID note on successful hit
- Remove hit notes from play

**Concepts Introduced:**
- Timing windows (frames of tolerance)
- Perfect vs Good vs Miss thresholds
- Playing the correct note on hit
- Note consumption (one input, one note)

**Code Written:**
```
- check_hits: run when key pressed
- Find notes in hit zone on that track
- Calculate timing difference from perfect
- If within window: play note, remove from screen
- If outside window: it's a miss
```

**What the Learner Sees:**
Pressing the right key when a note is in the hit zone plays the note and removes it from screen. Wrong timing or wrong track does nothing (yet). The core gameplay works.

**Technical Details:**
- Perfect: ±2 frames
- Good: ±4 frames
- Miss: note still there, key wasted
- Only one note consumed per key press

---

### Unit 13: Scoring Basics

**Learning Objectives:**
- Implement a score counter
- Award points based on hit quality
- Display score on screen efficiently
- Handle large numbers (16-bit)

**Concepts Introduced:**
- 16-bit arithmetic on 8-bit CPU
- Binary to decimal conversion
- Efficient screen updates (only changed digits)
- Score constants

**Code Written:**
```
- score_lo, score_hi: 16-bit score
- add_score: add N points to score
- display_score: convert to decimal, show on screen
- Point values: Perfect=100, Good=50
- Update display only when score changes
```

**What the Learner Sees:**
Score display at top of screen increases when notes are hit. Perfect hits score more than good hits. The numbers feel satisfying.

**Technical Details:**
- Max score: 65535 (enough for one song)
- Display as 6 digits with leading zeros
- Use BCD mode or division for conversion

---

### Unit 14: Miss Handling

**Learning Objectives:**
- Detect notes that weren't hit in time
- Provide feedback for misses
- Track miss count
- Play dissonant sound for misses

**Concepts Introduced:**
- Implicit misses (note left hit zone)
- Explicit misses (key pressed, nothing there)
- Negative feedback design
- Dissonance in SID

**Code Written:**
```
- check_missed_notes: notes past hit zone
- mark_miss: increment miss counter, play sound
- miss_sound: brief noise burst or wrong note
- Flash track red on miss
- Display miss count (debug, remove later)
```

**What the Learner Sees:**
Notes that scroll past unhit cause a harsh buzz and the track flashes briefly. Pressing a key with no note also triggers feedback. The game now punishes mistakes.

**Technical Details:**
- Miss sound: noise waveform, fast decay
- Track flash: change colour RAM briefly
- Miss counter separate from score

---

### Unit 15: Health Meter

**Learning Objectives:**
- Implement a performance meter
- Increase health on hits, decrease on misses
- Display health as a bar graph
- End song when health depletes

**Concepts Introduced:**
- Clamped values (min/max bounds)
- Bar graph display with custom characters
- Game over state
- Health as "second chance" pool

**Code Written:**
```
- health: value 0-64
- modify_health: add or subtract, clamp
- display_health: show as 8-character bar
- check_game_over: health==0 ends song
- Custom characters for full/partial/empty bar segments
```

**What the Learner Sees:**
Health bar at bottom of screen grows with hits, shrinks with misses. If it empties completely, the song ends in failure. Stakes are real now.

**Technical Details:**
- Start at 32/64 (half full)
- Perfect: +4, Good: +2, Miss: -8
- Display: 8 characters × 8 pixels = 64 levels
- Game over triggers immediately when health hits 0

---

### Unit 16: Complete Playthrough

**Learning Objectives:**
- Detect end of song
- Display results screen
- Calculate and show statistics
- Allow replay or return to start

**Concepts Introduced:**
- Game states (playing, results, menu)
- End-of-song detection
- Statistics calculation
- Simple menu navigation

**Code Written:**
```
- check_song_end: all beats processed, all notes resolved
- show_results: clear screen, display stats
- Results: score, perfects, goods, misses, max combo
- Wait for key press
- Return to song start for replay
```

**What the Learner Sees:**
After the song ends (success or failure), a results screen shows score and breakdown. Press a key to play again. A complete game loop.

**Phase 1 Checkpoint:**
The learner has built a working rhythm game. One song, basic graphics, functional scoring, health system, win/lose conditions. It's simple but complete. Everything from here builds on this foundation.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Multiple songs, difficulty levels, game modes. A game with real content and variety.*

*By the end of this phase, the game has 5 songs, 3 difficulty levels, career mode, practice mode, endless mode, and a combo system. It's a game people would actually want to play multiple times.*

---

### Unit 17: Song Selection Screen

**Learning Objectives:**
- Create a menu system
- Display list of available songs
- Handle cursor movement
- Transition between game states

**Concepts Introduced:**
- Menu state management
- Cursor position tracking
- Key repeat delay
- State machine pattern

**Code Written:**
```
- menu_state: which menu screen is active
- song_list: array of song metadata
- draw_menu: display song names with cursor
- menu_input: up/down to move, fire to select
- transition_to_game: load selected song, switch state
```

**What the Learner Sees:**
A song selection screen lists available songs (currently just one). Cursor highlights selection. Press fire to play. The game has structure beyond just playing.

---

### Unit 18: Song 2 - Composing for SID

**Learning Objectives:**
- Understand basic music composition for games
- Create a song with different character than Song 1
- Use different SID voices effectively
- Balance difficulty with musicality

**Concepts Introduced:**
- Musical keys and scales
- Tempo and feel
- Voice assignment for melody/harmony/bass
- Note density for difficulty

**Code Written:**
```
- Song 2 data: ~40 notes, different tempo
- Distinct melodic feel (major key, upbeat)
- Use different waveform combinations
- Add to song_list array
```

**What the Learner Sees:**
Song selection now shows two songs. Song 2 plays noticeably differently - different music, different feel, similar difficulty.

**Composition Notes:**
- Song 1: 120 BPM, minor key, steady
- Song 2: 130 BPM, major key, bouncy
- Both introduce mechanics gently

---

### Unit 19: Difficulty Levels

**Learning Objectives:**
- Implement difficulty selection
- Modify game parameters based on difficulty
- Understand difficulty as content multiplier
- Add difficulty to UI

**Concepts Introduced:**
- Difficulty parameters (timing window, note density)
- Easy: wider windows, fewer notes
- Hard: tight windows, more notes
- UI for difficulty selection

**Code Written:**
```
- difficulty: 0=Easy, 1=Normal, 2=Hard
- timing_window: varies by difficulty
- Difficulty selection on song menu
- Display selected difficulty
```

**What the Learner Sees:**
Each song now shows Easy/Normal/Hard options. Easy gives more time to hit notes and is more forgiving. Hard punishes sloppy timing.

**Difficulty Parameters:**
| Parameter | Easy | Normal | Hard |
|-----------|------|--------|------|
| Perfect window | ±4 frames | ±2 frames | ±1 frame |
| Good window | ±8 frames | ±4 frames | ±2 frames |
| Health loss | -4 | -8 | -12 |

---

### Unit 20: Note Patterns for Difficulty

**Learning Objectives:**
- Generate difficulty variants from base song
- Thin notes for Easy, densify for Hard
- Keep musical integrity across difficulties
- Store variants efficiently

**Concepts Introduced:**
- Algorithmic pattern modification
- Note filtering (keep every Nth note)
- Note insertion (add off-beats)
- Variant storage strategies

**Code Written:**
```
- generate_easy: remove notes on weak beats
- generate_hard: add notes on off-beats
- Store as separate data or generate on load
- Maintain base pattern as Normal
```

**What the Learner Sees:**
Playing the same song on Easy has noticeably fewer notes. Hard has notes filling in gaps. The song remains recognisable but challenge varies dramatically.

---

### Unit 21: Song 3 - Faster Tempo

**Learning Objectives:**
- Handle faster scroll speeds
- Ensure hit detection works at high speed
- Compose for speed while remaining playable
- Test difficulty scaling at tempo

**Concepts Introduced:**
- Tempo ceiling (human reaction limits)
- Note anticipation at high speed
- Visual clarity at fast scroll
- Frame-rate concerns

**Code Written:**
```
- Song 3 data: 150 BPM, energetic
- Adjust scroll calculation for speed
- Verify hit detection at 1-frame windows
- Balance note density for playability
```

**What the Learner Sees:**
Song 3 scrolls faster, demands quicker reactions. The game tests speed now, not just rhythm accuracy. Easy mode on Song 3 ≈ Normal mode on Song 1.

---

### Unit 22: Combo System

**Learning Objectives:**
- Track consecutive successful hits
- Implement score multiplier
- Break combo on any miss
- Display combo prominently

**Concepts Introduced:**
- Combo counter variable
- Multiplier tiers (10, 25, 50 hits)
- Combo break feedback
- Risk/reward design

**Code Written:**
```
- combo: current consecutive hits
- max_combo: best combo this song
- multiplier: 1x, 2x, 3x, 4x based on combo
- Multiply score by multiplier
- Reset combo to 0 on miss
```

**What the Learner Sees:**
A combo counter appears, climbing with each hit. Score multiplier increases at thresholds. Missing breaks the combo and feels devastating. High scores now require consistency.

**Multiplier Tiers:**
- 0-9 hits: 1x
- 10-24 hits: 2x
- 25-49 hits: 3x
- 50+ hits: 4x

---

### Unit 23: Combo Visuals

**Learning Objectives:**
- Provide visual feedback for combo status
- Create escalating visual intensity
- Use colour and sprites for emphasis
- Reward streaks viscerally

**Concepts Introduced:**
- Colour cycling tied to game state
- Hardware sprites for effects
- Border colour as feedback
- Escalating visual feedback

**Code Written:**
```
- Border colour shifts with combo tier
- Large combo number display
- Sprite explosion on multiplier increase
- "Fire" effect sprite at high combos
- All effects disable on combo break
```

**What the Learner Sees:**
As combo builds, the border shifts through colours, numbers grow large, sprites add visual flair. Breaking a 50+ combo is visually devastating as all the effects disappear. The combo feels important.

---

### Unit 24: Practice Mode

**Learning Objectives:**
- Implement alternate game mode
- Allow failure-free play for learning
- Provide speed adjustment
- Section loop for difficult parts

**Concepts Introduced:**
- Game mode as parameter
- Speed scaling (0.5x, 0.75x, 1x)
- Section markers in song data
- No-fail flag

**Code Written:**
```
- practice_mode: boolean flag
- speed_multiplier: affects scroll rate
- If practice_mode: health never depletes
- Speed selection in menu
- Can restart from last section marker
```

**What the Learner Sees:**
Practice mode in menu. Songs play slower and don't end on empty health. Learners can work through difficult sections without frustration.

---

### Unit 25: Song 4 - Syncopation

**Learning Objectives:**
- Compose with off-beat emphasis
- Challenge assumed rhythm patterns
- Provide visual cues for syncopation
- Test rhythm reading skills

**Concepts Introduced:**
- Syncopation in music
- Off-beat note placement
- Visual beat indicators
- Rhythm complexity

**Code Written:**
```
- Song 4 data: emphasis on off-beats
- Add beat marker visual (pulse on downbeat)
- Note patterns that contradict visual beat
- Test syncopation across difficulties
```

**What the Learner Sees:**
Song 4 feels different - notes land between expected beats. The visual beat marker helps but hands want to follow eyes, not ears. A new kind of challenge.

---

### Unit 26: Career Mode Structure

**Learning Objectives:**
- Implement progression system
- Lock content behind achievement
- Save and display progress
- Create sense of advancement

**Concepts Introduced:**
- Unlock conditions
- Progress persistence (in memory for now)
- Achievement thresholds
- Career menu UI

**Code Written:**
```
- song_unlocked: array of booleans
- unlock_condition: minimum score or completion
- Song 1 always unlocked
- Check unlock after results
- Career menu shows locked/unlocked status
```

**What the Learner Sees:**
Career mode shows songs 2-5 locked initially. Completing Song 1 unlocks Song 2. Progress creates motivation to continue. A reason to play beyond high scores.

---

### Unit 27: Song 5 - The Challenge

**Learning Objectives:**
- Compose a demanding finale song
- Use all SID capabilities learned so far
- Create memorable musical moments
- Balance difficulty with fairness

**Concepts Introduced:**
- Extended song length
- Dynamic difficulty within song
- Climactic sections
- Reward for mastery

**Code Written:**
```
- Song 5 data: 2+ minutes, 100+ notes
- Uses all three voices prominently
- Difficulty ramps within song
- Climactic ending section
```

**What the Learner Sees:**
Song 5 is clearly the boss. Longer, denser, more demanding. Completing it on Hard is a real achievement. The SID output is impressive.

---

### Unit 28: Joystick Support

**Learning Objectives:**
- Read joystick input
- Map joystick to three-track input
- Let player choose control scheme
- Handle both simultaneously

**Concepts Introduced:**
- CIA joystick reading
- Direction to track mapping
- Input method selection
- Control scheme UI

**Code Written:**
```
- read_joystick: check directions
- Map: up=track1, fire=track2, down=track3
- control_scheme: keyboard or joystick
- Selection in options
- Both can work simultaneously
```

**What the Learner Sees:**
Options menu includes control scheme. Joystick works as alternative to keyboard. Some players prefer one or the other.

**Joystick Mapping:**
- Up: Track 1 (high voice)
- Fire: Track 2 (mid voice)
- Down: Track 3 (low voice)

---

### Unit 29: Endless Mode - Procedural Generation

**Learning Objectives:**
- Generate note patterns algorithmically
- Follow musical rules for coherent patterns
- Create unlimited content
- Balance randomness with playability

**Concepts Introduced:**
- Procedural generation basics
- Beat grid constraints
- Probability distributions
- Seed-based randomness

**Code Written:**
```
- generate_note: decide if note appears on beat
- Probability increases with level
- Notes placed on beat grid
- Track selection weighted
- Infinite loop mode (no song end)
```

**What the Learner Sees:**
Endless mode generates notes forever. Patterns feel musical (mostly on beats) but unpredictable. High score is only goal.

---

### Unit 30: Endless Mode - Difficulty Curve

**Learning Objectives:**
- Implement dynamic difficulty
- Increase challenge over time
- Track level/progress in endless
- Balance for long sessions

**Concepts Introduced:**
- Dynamic difficulty adjustment
- Level as time survived
- Speed increase over time
- Density increase over time

**Code Written:**
```
- endless_level: increases with time
- Speed scales with level
- Note density scales with level
- Display current level
- Level up fanfare
```

**What the Learner Sees:**
Endless mode starts easy, gets progressively harder. Level number tracks progress. Eventually becomes impossible but that's the point. Competing for how long you survive.

---

### Unit 31: Statistics Tracking

**Learning Objectives:**
- Track persistent statistics
- Display lifetime achievements
- Create long-term goals
- Show progression over time

**Concepts Introduced:**
- Aggregate statistics
- 32-bit counters for large values
- Statistics display screen
- Progress visualisation

**Code Written:**
```
- total_notes_hit: lifetime counter
- total_perfects: lifetime counter
- best_combo: highest ever achieved
- games_played: session counter
- stats_screen: display all statistics
```

**What the Learner Sees:**
Statistics screen shows lifetime totals: notes hit, perfects, best combo, songs completed. A sense of overall progress beyond individual songs.

---

### Unit 32: Content Complete Review

**Learning Objectives:**
- Playtest complete content
- Balance difficulty curve across songs
- Verify all modes integrate properly
- Fix integration bugs

**Concepts Introduced:**
- System integration testing
- Balance tuning
- Player experience flow
- Bug prioritisation

**Code Written:**
```
- Playtest session with notes
- Adjust note patterns for balance
- Verify career unlock flow
- Fix any issues found
- Document known issues
```

**What the Learner Sees:**
The complete game with all content. Everything works together. Five songs, three difficulties, multiple modes. Ready for polish.

**Phase 2 Checkpoint:**
The game now has substantial content: 5 songs × 3 difficulties = 15 distinct challenges, plus endless mode for infinite play. Career mode provides progression. Practice mode helps learning. The game is feature-complete but not yet polished.

---

## Phase 3: Polish (Units 33-48)

*Goal: Make it feel professional. Visual effects, sound design, and user experience polish.*

*By the end of this phase, the game looks and sounds professional. Every interaction has feedback. The experience is cohesive and polished.*

---

### Unit 33: Title Screen Design

**Learning Objectives:**
- Design an impactful title screen
- Create logo with custom characters
- Establish visual identity
- Plan menu navigation

**Concepts Introduced:**
- Logo design on character grid
- Colour palette selection
- Visual hierarchy
- Brand identity

**Code Written:**
```
- Title screen character layout
- "SID SYMPHONY" logo in custom chars
- Menu options: Start, Options, High Scores
- Colour scheme matching game aesthetic
```

**What the Learner Sees:**
A proper title screen with large logo, clear menu options, cohesive colours. Looks like a commercial game.

---

### Unit 34: Title Screen Animation

**Learning Objectives:**
- Animate static elements
- Create visual interest
- Loop animations smoothly
- Add title music

**Concepts Introduced:**
- Frame-based animation
- Colour cycling techniques
- Music loop structure
- Attention management

**Code Written:**
```
- Logo shimmer animation
- Background colour cycling
- Pulsing menu cursor
- Short music loop on title
- Transition effects to menu
```

**What the Learner Sees:**
The title screen moves and breathes. Logo shimmers, colours cycle, music plays. The game feels alive even before playing.

---

### Unit 35: Attract Mode

**Learning Objectives:**
- Implement auto-play demonstration
- Record or script gameplay
- Return to title on input
- Showcase game features

**Concepts Introduced:**
- Demo playback system
- Attract mode timing
- Input interrupt
- Feature showcase

**Code Written:**
```
- attract_mode: plays Song 1 automatically
- Scripted or perfect-play input
- Timer to cycle through songs
- Any key returns to title
- Cycle: Title → Attract → Title
```

**What the Learner Sees:**
Leave the game idle and it plays itself, showing off gameplay. Perfect for shop displays or impressing friends. Commercial quality feature.

---

### Unit 36: Hit Zone Animation

**Learning Objectives:**
- Animate the hit zone to the beat
- Provide rhythmic visual feedback
- Enhance timing feel
- Create urgency

**Concepts Introduced:**
- Beat-synced animation
- Expansion/contraction effect
- Colour pulse
- Visual metronome

**Code Written:**
```
- hit_zone_anim: pulse on each beat
- Expand slightly on downbeat
- Colour intensity follows beat
- Performance indicator (changes with health)
```

**What the Learner Sees:**
The hit zone pulses in time with the music, expanding on each beat. It helps feel the rhythm and provides a visual metronome.

---

### Unit 37: Perfect Hit Effects

**Learning Objectives:**
- Create satisfying hit feedback
- Layer multiple effect types
- Make perfects feel special
- Reward accuracy dramatically

**Concepts Introduced:**
- Screen flash technique
- Sprite burst effects
- Sound punctuation
- Feedback layering

**Code Written:**
```
- perfect_hit_effect: all effects combined
- Border flash (white, 2 frames)
- Sprite starburst at note position
- Sound "punch" (quick noise burst)
- Score popup animation
```

**What the Learner Sees:**
A perfect hit triggers a cascade of feedback: flash, sparkle, sound, animated score. It feels amazing. Perfects become the goal.

---

### Unit 38: Good Hit Effects

**Learning Objectives:**
- Differentiate feedback tiers
- Make good feel okay, not great
- Motivate improvement
- Maintain consistency

**Concepts Introduced:**
- Tiered feedback design
- Subtle vs dramatic effects
- Positive but lesser reward
- Comparison feedback

**Code Written:**
```
- good_hit_effect: subset of perfect
- Smaller sprite effect
- No screen flash
- Softer sound
- Score popup (smaller)
```

**What the Learner Sees:**
Good hits still get feedback, but noticeably less than perfect. The difference motivates chasing perfects without punishing goods.

---

### Unit 39: Miss Effects

**Learning Objectives:**
- Provide negative feedback appropriately
- Make misses feel bad (not annoying)
- Don't over-punish
- Reset expectations

**Concepts Introduced:**
- Negative feedback design
- Brevity of punishment
- Screen shake technique
- Sound dissonance

**Code Written:**
```
- miss_effect: brief negative feedback
- Track "crack" sprite
- Screen shake (1-2 frames)
- Dissonant sound burst
- Combo counter breaks visually
```

**What the Learner Sees:**
Misses feel like mistakes - brief shake, harsh sound, combo breaks. But it's over quickly and doesn't dwell. Punishment is immediate and brief.

---

### Unit 40: Background Visuals

**Learning Objectives:**
- Add dynamic background
- Use raster effects for colour
- Keep performance stable
- Enhance atmosphere

**Concepts Introduced:**
- Raster splits for backgrounds
- Colour cycling patterns
- Performance budgeting
- Atmosphere through visuals

**Code Written:**
```
- background_anim: colour cycling pattern
- Raster interrupt for colour splits
- Simple starfield or gradient
- Intensity follows music/combo
- Performance monitoring
```

**What the Learner Sees:**
The background isn't static black anymore. Colour shifts and patterns add depth. At high combos, background intensifies.

---

### Unit 41: Voice Callouts

**Learning Objectives:**
- Implement SID voice synthesis
- Create short speech samples
- Trigger appropriately
- Mix with music

**Concepts Introduced:**
- SID vocal synthesis basics
- Sample triggering
- Volume mixing
- Appropriate frequency

**Code Written:**
```
- say_perfect: synthesize "PERFECT"
- say_miss: synthesize "MISS"
- Trigger on notable events
- Only on milestones (not every hit)
- Mix level below music
```

**What the Learner Sees:**
On significant events (first perfect, combo milestone, miss after long streak), a robotic voice announces it. Adds personality.

---

### Unit 42: Advanced SID - Filters

**Learning Objectives:**
- Understand SID filter architecture
- Use filter for sound design
- Create sweep effects
- Tie filter to gameplay

**Concepts Introduced:**
- Low-pass, band-pass, high-pass
- Filter cutoff and resonance
- Sweep automation
- Filter as expression

**Code Written:**
```
- Configure SID filter
- Filter sweep on perfect hits
- Filter linked to combo (brighter at high combo)
- Muffled sound when health low
```

**What the Learner Sees:**
Sound becomes richer. Perfects have a sweep effect. High combos sound brighter. Low health sounds muffled. The SID is more expressive.

---

### Unit 43: Sound Effects Layer

**Learning Objectives:**
- Design complete SFX set
- Mix effects with music
- Cover all interactions
- Consistent audio design

**Concepts Introduced:**
- SFX inventory
- Voice allocation for SFX
- Mix balance
- Audio feedback completeness

**Code Written:**
```
- Menu sounds (select, confirm, back)
- UI sounds (pause, unpause)
- Feedback sounds (all refined)
- Victory/failure jingles
- All sounds balanced in mix
```

**What the Learner Sees:**
Every interaction has appropriate sound. Menus blip, confirmations click, victory plays a fanfare. Complete audio experience.

---

### Unit 44: Results Screen Polish

**Learning Objectives:**
- Create satisfying results display
- Animate score reveal
- Show achievements
- Celebrate success

**Concepts Introduced:**
- Score count-up animation
- Star rating system
- New high score celebration
- Detailed breakdown

**Code Written:**
```
- Animated score count (ticks up)
- Star rating (1-5 based on performance)
- "NEW HIGH SCORE" flash
- Detailed stats breakdown
- Continue options clear
```

**What the Learner Sees:**
Results screen is an event - score ticks up, stars appear, new records celebrated. It feels like an achievement even on modest scores.

---

### Unit 45: High Score Table

**Learning Objectives:**
- Implement persistent high scores
- Create name entry system
- Display leaderboard
- Rank scores correctly

**Concepts Introduced:**
- High score data structure
- Name entry UI
- Score insertion/sorting
- Display formatting

**Code Written:**
```
- high_scores: array of 10 entries
- Name entry: letter selection system
- Insert new score in sorted position
- Display formatted table
- Highlight new entry
```

**What the Learner Sees:**
High score table shows top 10 with names. Beating a score prompts name entry. New entries highlighted. A reason to replay.

---

### Unit 46: Options Screen

**Learning Objectives:**
- Create options menu
- Implement configurable settings
- Save preferences
- Sound test feature

**Concepts Introduced:**
- Settings persistence
- Toggle and slider UI
- Sound test mode
- User preferences

**Code Written:**
```
- Options menu structure
- Difficulty default setting
- Sound/music volume controls
- Control scheme selection
- Sound test (preview all songs)
```

**What the Learner Sees:**
Options screen allows customisation: difficulty, volume, controls. Sound test lets players preview songs. Player has control.

---

### Unit 47: Pause Functionality

**Learning Objectives:**
- Implement mid-game pause
- Handle pause state correctly
- Provide pause menu
- Resume cleanly

**Concepts Introduced:**
- Game state preservation
- Pause overlay
- Music pause/resume
- Countdown resume

**Code Written:**
```
- Pause on P key or fire (configurable)
- Pause menu: Resume, Restart, Quit
- Music pauses (not stops)
- 3-2-1 countdown on resume
- Full state preserved
```

**What the Learner Sees:**
Pressing pause freezes game with overlay. Menu offers options. Resuming has countdown to prepare. Professional pause system.

---

### Unit 48: Polish Pass

**Learning Objectives:**
- Playtest complete game
- Fix visual inconsistencies
- Tune final balance
- Document polish notes

**Concepts Introduced:**
- Polish playtest methodology
- Detail attention
- Final tuning
- Quality bar

**Code Written:**
```
- Fix any visual glitches found
- Tighten timing feel
- Adjust colours for CRT
- Final difficulty balance
- Performance verification
```

**What the Learner Sees:**
Subtle improvements throughout. Everything feels slightly tighter, cleaner, more polished. The 90% to 100% quality jump.

**Phase 3 Checkpoint:**
The game looks and sounds professional. Every interaction has feedback. Menus are polished, effects are satisfying, audio is complete. It feels like a commercial product.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Commercial quality finish. Optimisation, advanced techniques, and professional packaging.*

*By the end of this phase, the game is truly complete: optimised, feature-rich, and ready for distribution. The learner has skills matching professional C64 developers.*

---

### Unit 49: Code Review and Architecture

**Learning Objectives:**
- Review complete codebase
- Identify architectural improvements
- Document code structure
- Plan optimisation targets

**Concepts Introduced:**
- Code review practices
- Technical debt identification
- Documentation standards
- Optimisation planning

**Code Written:**
```
- Full code review with notes
- Document memory map
- Identify hot paths for optimisation
- Clean up naming inconsistencies
- Add code comments where needed
```

**What the Learner Sees:**
No visible change, but codebase is cleaner. Comments explain complex sections. Architecture documented.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce memory footprint
- Compress data efficiently
- Remove redundant code
- Free RAM for future use

**Concepts Introduced:**
- Data compression techniques
- Dead code elimination
- Memory layout optimisation
- RAM budgeting

**Code Written:**
```
- Compress song data
- Optimize character set (remove unused)
- Eliminate dead code paths
- Consolidate redundant routines
- Document final memory map
```

**What the Learner Sees:**
Same game, smaller size. More RAM free. Important for distribution.

---

### Unit 51: CPU Optimisation - Hot Paths

**Learning Objectives:**
- Profile code performance
- Optimise critical loops
- Reduce cycle counts
- Maintain headroom

**Concepts Introduced:**
- Profiling techniques
- Cycle counting
- Loop unrolling
- Lookup tables vs calculation

**Code Written:**
```
- Identify hot loops (note update, hit detection)
- Unroll critical loops
- Replace calculations with lookups
- Verify cycle counts
- Document performance budget
```

**What the Learner Sees:**
Game feels slightly smoother. More room for effects. Professional optimisation practice.

---

### Unit 52: Stable Raster Timing

**Learning Objectives:**
- Achieve perfect raster stability
- Handle worst-case scenarios
- Eliminate all tearing
- Professional visual quality

**Concepts Introduced:**
- Double-buffering concepts
- Raster timing edge cases
- Worst-case budgeting
- Visual polish standard

**Code Written:**
```
- Verify raster sync under load
- Handle many-note scenarios
- Test all songs at all difficulties
- Fix any remaining tearing
- Document timing budget
```

**What the Learner Sees:**
Rock-solid visuals. No tearing ever, even at peak note density. Professional quality.

---

### Unit 53: Advanced SID - Multi-Speed

**Learning Objectives:**
- Update SID faster than frame rate
- Create richer sound
- Implement per-frame effects
- Professional audio quality

**Concepts Introduced:**
- Multi-speed SID updates
- Timer interrupt for audio
- Sub-frame sound changes
- Professional sound design

**Code Written:**
```
- Timer interrupt for SID (2x per frame)
- More detailed envelope shapes
- Vibrato effect (pitch wobble)
- Pitch slides between notes
- Professional SID sound quality
```

**What the Learner Sees:**
Music sounds noticeably richer. Notes have subtle life. Professional SID audio.

---

### Unit 54: Advanced SID - Ring Modulation

**Learning Objectives:**
- Understand ring modulation
- Create metallic and bell tones
- Use oscillator sync
- Expand sonic palette

**Concepts Introduced:**
- Ring modulation theory
- Sync oscillators
- Bell and metallic sounds
- Creative sound design

**Code Written:**
```
- Ring mod for bell sounds
- Sync for hard-edged tones
- Use in specific songs (Song 5)
- New SFX using ring mod
- Full SID capability demonstrated
```

**What the Learner Sees:**
New sounds not possible before. Metallic hits, bell tones, complex timbres. The SID's full potential.

---

### Unit 55: Sprite Multiplexing Introduction

**Learning Objectives:**
- Understand why 8 sprites isn't enough
- Implement basic multiplexing
- More visual effects possible
- Professional effect quality

**Concepts Introduced:**
- Sprite multiplexing concept
- Raster interrupt for sprites
- Sorted sprite lists
- More than 8 sprites on screen

**Code Written:**
```
- Basic sprite multiplexer
- More simultaneous effect sprites
- Perfect hit creates multiple bursts
- Combo effects more elaborate
- Up to 16 sprites visible
```

**What the Learner Sees:**
More visual effects than seemed possible. Multiple simultaneous explosions. Professional effect density.

---

### Unit 56: Loading Screen

**Learning Objectives:**
- Create professional load experience
- Design loading screen
- Loading music/animation
- Set expectations

**Concepts Introduced:**
- Load-time experience
- Loading screen design
- Progress indication
- First impression

**Code Written:**
```
- Loading screen image
- Loading music (short loop)
- Simple animation during load
- Progress bar if possible
- Professional first impression
```

**What the Learner Sees:**
Loading isn't blank screen anymore. Art, music, animation. Professional presentation.

---

### Unit 57: Tape/Disk Optimisation

**Learning Objectives:**
- Understand storage media
- Optimise load time
- Implement save functionality
- Professional distribution

**Concepts Introduced:**
- Disk vs tape trade-offs
- File organisation
- Save routines
- Distribution formats

**Code Written:**
```
- Optimise file layout for disk
- Implement high score save/load
- Test on real hardware (if possible)
- Create distribution files
- Professional save system
```

**What the Learner Sees:**
High scores persist across sessions. Loads faster. Ready for real distribution.

---

### Unit 58: Two Player Mode

**Learning Objectives:**
- Design two player experience
- Handle dual input
- Create competitive mode
- Expand replayability

**Concepts Introduced:**
- Multiplayer design
- Input mapping for two
- Screen sharing strategies
- Competitive balance

**Code Written:**
```
- Two player mode option
- Split input (keyboard + joystick)
- Shared screen, dual tracks
- Competitive scoring
- Winner determination
```

**What the Learner Sees:**
Two players can compete on same song. Adds social dimension. Significant replay value.

---

### Unit 59: Two Player Polish

**Learning Objectives:**
- Complete two player experience
- Balance for fairness
- Polish multiplayer presentation
- Multiplayer attract mode

**Concepts Introduced:**
- Multiplayer balance
- Winner/loser presentation
- Fairness considerations
- Multiplayer polish

**Code Written:**
```
- Winner celebration
- Loser commiseration
- Balanced scoring for two
- Two player attract mode
- Complete multiplayer experience
```

**What the Learner Sees:**
Two player mode feels complete. Clear winner/loser, fair competition, polished presentation.

---

### Unit 60: Final Song - The Showcase

**Learning Objectives:**
- Compose ultimate demonstration
- Use every SID technique
- Create memorable finale
- Reward completion

**Concepts Introduced:**
- Showcase composition
- All techniques combined
- Hidden content reward
- Memorable experience

**Code Written:**
```
- Song 6: hidden final song
- Unlocked by completing all songs on Hard
- 3+ minutes, uses all SID features
- Most challenging and rewarding
- Technical showcase
```

**What the Learner Sees:**
Completing the game on Hard unlocks a secret final song. It's the ultimate challenge and uses every technique. A reward for mastery.

---

### Unit 61: Credits Sequence

**Learning Objectives:**
- Create professional credits
- Acknowledge work done
- Provide closure
- Original credit music

**Concepts Introduced:**
- Credits scroll technique
- Attribution standards
- Closure experience
- Credit music

**Code Written:**
```
- Scrolling credits screen
- Attribution (learner's name!)
- Original credits music
- Unlocked after any completion
- Professional ending
```

**What the Learner Sees:**
Completing the game shows proper credits. The learner's name is in a game they built. Satisfying closure.

---

### Unit 62: Bug Hunt and Edge Cases

**Learning Objectives:**
- Systematic bug testing
- Edge case handling
- Defensive programming
- Quality assurance

**Concepts Introduced:**
- Bug hunt methodology
- Edge case identification
- Defensive code practices
- QA process

**Code Written:**
```
- Test all paths systematically
- Fix edge cases (key mashing, etc.)
- Add defensive checks
- Memory boundary verification
- Document all issues found/fixed
```

**What the Learner Sees:**
No visible change if bugs were minor. Confidence in stability. Professional quality.

---

### Unit 63: Final Playtest

**Learning Objectives:**
- Fresh perspective playtest
- Final tuning opportunity
- Help text if needed
- Release candidate

**Concepts Introduced:**
- Release candidate concept
- Fresh eyes testing
- Final adjustments
- Sign-off process

**Code Written:**
```
- External playtest if possible
- Tutorial/help if needed
- Final difficulty tweaks
- Any last polish
- Declare release candidate
```

**What the Learner Sees:**
Final version. Everything works. Ready for release.

---

### Unit 64: Packaging and Distribution

**Learning Objectives:**
- Create distribution package
- Document the game
- Archive final build
- Prepare for release

**Concepts Introduced:**
- Distribution formats (D64, TAP, PRG)
- Documentation writing
- Archive practices
- Release process

**Code Written:**
```
- Create D64 disk image
- Create TAP tape image
- Write instruction card
- Box art concept (description)
- Final archive of all source
```

**What the Learner Sees:**
Distributable game files ready to share. Documentation explains how to play. A complete commercial-quality product.

**Phase 4 Checkpoint:**
The game is complete. Optimised, polished, feature-rich, and professionally packaged. It could have sold for £9.99 in 1986. The learner has built a commercial-quality game and learned skills matching professional C64 developers.

---

## Skills Mastery Summary

By completing all 64 units, learners have demonstrated mastery of:

### SID Chip
- All three voices and waveforms
- ADSR envelopes
- Filters (low/band/high pass)
- Ring modulation and sync
- Multi-speed playback
- Voice synthesis

### 6510 Assembly
- Memory architecture
- Raster timing and interrupts
- Keyboard and joystick input
- Data structures
- Optimisation techniques
- Clean code organisation

### Game Development
- Game loop structure
- State machine patterns
- Collision detection
- Scoring and progression systems
- Save/load functionality
- Two player implementation

### Professional Skills
- Playtesting methodology
- Polish and juice design
- Performance optimisation
- Distribution packaging
- Quality assurance

---

## Comparison: 16 Units vs 64 Units

| Aspect | 16-Unit Version | 64-Unit Version |
|--------|-----------------|-----------------|
| Songs | 1 | 6 (5 + secret) + endless |
| Difficulties | 1 | 3 + practice mode |
| Modes | Play only | Career, Practice, Endless, 2P |
| SID Usage | Basic voices | Full: filters, ring mod, multi-speed |
| Visuals | Static | Animated, effects, raster tricks |
| Polish | Minimal | Title, attract, credits, options |
| Save | None | High scores persist |
| Distribution | PRG file | Full package with docs |
| Commercial viable? | No | Yes |
| Time investment | 16-32 hours | 64-128 hours |

---

## Version History

- **1.0 (2025-01-07):** Initial 64-unit outline
