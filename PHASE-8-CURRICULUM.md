# Phase 8: Adventure Games (Lessons 4481-4992)

**Total:** 512 lessons across 8 tiers (64 lessons per tier)

**Phase Goal:** Master narrative-driven adventure games. Learn inventory puzzles, dialogue systems, parser mechanics, story branching, and environmental storytelling.

**Prerequisites:** Phases 1-7 complete (all foundational systems, especially save systems from Phase 7)

**Phase Philosophy:**
- Story = primary driver
- Inventory puzzles = logic challenges
- Dialogue systems = branching narratives
- Parser mechanics = text interaction
- Environmental storytelling
- Save/load critical (large state spaces)
- 64 lessons sufficient for each style
- Complete games with full stories

**Game Progression:**
- **Tier 1:** Maniac Mansion - Room-based, character switching, object puzzles
- **Tier 2:** Monkey Island - Verb interface, dialogue trees, inventory combos
- **Tier 3:** King's Quest - Parser + graphics, fairy tale, death states
- **Tier 4:** Police Quest - Procedural realism, sequence-sensitive puzzles
- **Tier 5:** Uninvited - Horror atmosphere, limited inventory, MacVenture
- **Tier 6:** Shadowgate - Death traps, light mechanics, fantasy dungeon
- **Tier 7:** Déjà Vu - Noir detective, amnesia narrative, time pressure
- **Tier 8:** The Hobbit - Text parser excellence, NPC AI, Tolkien adaptation

**What Students Master:**
- Inventory systems (object interaction, combinations)
- Dialogue trees (branching conversations, flags)
- Parser systems (text command interpretation)
- Verb interfaces (SCUMM-style)
- Object interaction (use X on Y)
- Puzzle dependency chains (A required for B required for C)
- Story state management (flags, progression tracking)
- Character switching (multiple protagonists)
- Death states and failure conditions
- Save/load for complex state spaces
- Environmental storytelling (room descriptions, examine text)
- NPC schedules and AI
- Time-based puzzles
- Light/darkness mechanics

---

## Phase 8 Overview

| Tier | Game | Sub-genre | Deliverable | Key Skills |
|------|------|-----------|-------------|------------|
| 1 | Maniac Mansion | Room-based | Multi-character, object puzzles, cutscenes | Character switching, room states, objects |
| 2 | Monkey Island | SCUMM Adventure | Verb interface, dialogue, inventory | Verbs, dialogue trees, no-death design |
| 3 | King's Quest | Parser + Graphics | Text parser, graphics, fairy tale | Parser, Sierra-style, death states |
| 4 | Police Quest | Procedural Adventure | Realism, sequence puzzles, police work | Procedure tracking, realistic puzzles |
| 5 | Uninvited | MacVenture Horror | Point-and-click, horror, death traps | MacVenture UI, atmosphere, tension |
| 6 | Shadowgate | MacVenture Fantasy | First-person, torch mechanics, fantasy | Resource management, death traps, torch |
| 7 | Déjà Vu | MacVenture Noir | Detective, amnesia, time limit | Detective mechanics, noir, time pressure |
| 8 | The Hobbit | Text Parser | Advanced parser, NPC AI, Tolkien | Parser excellence, NPC schedules, adaptation |

**Technical Progression:**
- Tiers 1-2: Modern adventure (verb interface, no-death)
- Tiers 3-4: Parser-based (text commands, realism)
- Tiers 5-7: MacVenture (point-and-click, horror/fantasy/noir)
- Tier 8: Text excellence (parser mastery, NPC AI)

---

## Tier 1: Maniac Mansion (Lessons 4481-4544)

**Goal:** Build Maniac Mansion with character switching, object puzzles, and cutscenes.

**Why this game:** LucasArts foundation. Multiple characters with different abilities. Object-based puzzles. Cutscenes and narrative.

**Game Requirements:**
- Choose 3 characters from 7 (Dave + 6 kids)
- Each character has unique ability (fix phone, develop film, play music, etc.)
- 20+ rooms (mansion layout)
- Object-based puzzles (use key on door, put hamster in microwave)
- Character switching (switch between your 3 characters)
- Cutscenes (triggered by events)
- Multiple solutions (different character combos = different paths)
- Multiple endings
- No death (characters get captured, can be rescued)
- Save/load system

**Skills Introduced:**
- Character switching (manage 3 protagonists)
- Character-specific abilities (puzzle gating by character)
- Object interaction system (use X on Y)
- Room-based world (screen-by-screen navigation)
- Cutscene system (triggered narrative)
- Multiple solutions (player choice affects path)
- Capture/rescue mechanics (no death, but failure states)

### Lesson Structure

**Lessons 4481-4488: Room System**
- L4481-4482: Room data structure (connections, objects, state)
- L4483-4484: Room rendering (background graphics)
- L4485-4486: Room navigation (exits, connections)
- L4487-4488: Room state persistence (doors locked, items taken)

**Lessons 4489-4496: Character System**
- L4489-4490: 7 characters (stats, abilities)
- L4491-4492: Character selection (choose 3)
- L4493-4494: Character switching (cycle between active 3)
- L4495-4496: Character abilities (unique puzzle solutions)

**Lessons 4497-4504: Inventory & Objects**
- L4497-4498: Inventory system (character-specific, 4-item limit)
- L4499-4500: Object pickup/drop
- L4501-4502: Object examination (descriptions)
- L4503-4504: Inventory UI (show current character's items)

**Lessons 4505-4512: Object Interaction**
- L4505-4506: "Use X on Y" system
- L4507-4508: Object combination (batteries + flashlight)
- L4509-4510: Object-environment interaction (key + door)
- L4511-4512: Interaction results (state changes, text feedback)

**Lessons 4513-4520: Puzzle System**
- L4513-4514: Puzzle dependency chains (need A to get B)
- L4515-4516: Character-gated puzzles (only Syd can fix phone)
- L4517-4518: Multiple solutions (different paths to same goal)
- L4519-4520: Puzzle state tracking (flags)

**Lessons 4521-4528: Cutscenes**
- L4521-4522: Cutscene triggers (event-based)
- L4523-4524: Cutscene rendering (animations, text)
- L4525-4526: Cutscene scripts (sequence of events)
- L4527-4528: Return to gameplay after cutscene

**Lessons 4529-4536: Capture/Rescue**
- L4529-4530: Character capture (failure condition)
- L4531-4532: Captured state (removed from active party)
- L4533-4534: Rescue mechanic (free captured characters)
- L4535-4536: Game over (all characters captured)

**Lessons 4537-4544: Story & Completion**
- L4537-4538: Story flags (progression tracking)
- L4539-4540: Multiple endings (based on choices)
- L4541-4542: Save/load system (full game state)
- L4543-4544: Polish and final integration

---

## Tier 2: Monkey Island (Lessons 4545-4608)

**Goal:** Build Monkey Island with SCUMM verb interface and dialogue trees.

**Why this game:** Defines modern adventure games. Verb interface. Dialogue trees. No-death design. Comedy writing.

**Game Requirements:**
- SCUMM verb interface (9 verbs: Open, Close, Push, Pull, Walk to, Pick up, Talk to, Give, Use, Look at)
- Click verb, then click object/character
- Inventory (collect items, combine items)
- Dialogue trees (choose responses, branching conversations)
- No death (impossible to die or get stuck)
- 3 acts (Melee Island, ship, Monkey Island)
- Insult sword fighting (match wits, not reflexes)
- Multiple islands (boat travel)
- Save/load

**Skills Introduced:**
- SCUMM verb interface (9-verb system)
- Dialogue trees (branching conversations with choices)
- No-death design (remove failure states)
- Insult combat (word matching as puzzle)
- Island navigation (world map)
- Comedy timing (text pacing, jokes)

---

## Tier 3: King's Quest (Lessons 4609-4672)

**Goal:** Build King's Quest with parser + graphics and Sierra-style design.

**Why this game:** Parser commands with graphics. Death states. Fairy tale setting. Sierra adventure template.

**Game Requirements:**
- Text parser (type commands: "get key", "open door", "talk to guard")
- Parser vocabulary (200+ recognized words)
- Synonyms (take = get, speak = talk)
- Graphics (Sierra AGI-style)
- Character movement (walk with arrow keys or click)
- Death states (fall off cliff, eaten by dragon)
- Score system (points for puzzle solutions)
- Fairy tale setting (Daventry, fantasy creatures)
- Save/load (death is frequent)

**Skills Introduced:**
- Text parser (command interpretation)
- Parser vocabulary (word recognition, synonyms)
- Death states (Sierra-style failure)
- Score tracking (puzzle completion points)
- AGI-style graphics (320×200-ish aesthetic on C64)
- Fairy tale narrative

---

## Tier 4: Police Quest (Lessons 4673-4736)

**Goal:** Build Police Quest with procedural realism and sequence-sensitive puzzles.

**Why this game:** Realism over fantasy. Procedures matter. Sequence-sensitive (do steps in order). Educational game design.

**Game Requirements:**
- Police procedures (check car before shift, use radio correctly)
- Sequence-sensitive puzzles (must do A, then B, then C)
- Instant death if you skip procedures (shot if you don't draw gun)
- Traffic stops (realistic police work)
- DUI arrest (breathalyzer, paperwork)
- Crime investigation (collect evidence)
- Final confrontation (The Death Angel)
- Score based on procedure adherence
- Sierra parser + graphics

**Skills Introduced:**
- Procedural puzzles (correct order required)
- Realism as game design (vs fantasy)
- Instant failure for mistakes (unforgiving)
- Educational game techniques (teach police procedure)
- Investigation mechanics (evidence collection)

---

## Tier 5: Uninvited (Lessons 4737-4800)

**Goal:** Build MacVenture-style horror adventure with atmospheric tension.

**Why this game:** MacVenture interface. Horror atmosphere. Limited inventory. First-person point-and-click.

**Game Requirements:**
- MacVenture interface (windows: room view, inventory, text, exits)
- First-person perspective (see room from your eyes)
- Point-and-click (click on objects to examine/take)
- Horror setting (haunted mansion)
- Limited inventory (weight/space restrictions)
- Death traps (ghosts, demons, bad choices)
- Atmospheric text (detailed descriptions)
- Survival horror (limited resources)
- Save/load

**Skills Introduced:**
- MacVenture interface (windowed UI)
- First-person perspective (vs third-person)
- Horror atmosphere (tension via text/graphics)
- Limited inventory (resource management)
- Survival horror mechanics

---

## Tier 6: Shadowgate (Lessons 4801-4864)

**Goal:** Build Shadowgate with torch mechanics and death traps.

**Why this game:** MacVenture fantasy. Torch resource management. Death everywhere. First-person dungeon.

**Game Requirements:**
- MacVenture interface (same as Uninvited)
- Fantasy dungeon (castle Shadowgate)
- Torch mechanics (need light to see, torches burn out)
- Death traps EVERYWHERE (open door → arrow trap)
- Trial and error gameplay (save often)
- Magic items (wand, staff, sphere)
- Warlock MacFadden (final boss)
- Dark rooms (need torch or die)
- Time pressure (torch countdown)

**Skills Introduced:**
- Resource management (torch as consumable)
- Time pressure (torch timer)
- Death trap design (punish exploration)
- Trial and error gameplay loop
- Dark room mechanics

---

## Tier 7: Déjà Vu (Lessons 4865-4928)

**Goal:** Build noir detective adventure with amnesia narrative.

**Why this game:** MacVenture noir. Detective mechanics. Time pressure (police raid). Amnesia story.

**Game Requirements:**
- MacVenture interface
- Noir detective setting (1940s Chicago)
- Amnesia opening (wake up in bathroom, don't remember anything)
- Detective mechanics (examine clues, piece together story)
- Time limit (police raid the bar after X minutes)
- Inventory puzzles (noir items: gun, flask, badge)
- Story revelation (discover your identity)
- Multiple endings (caught by police, escape, solve case)

**Skills Introduced:**
- Amnesia narrative (discover story as you play)
- Detective mechanics (clue examination)
- Time pressure (deadline to escape)
- Noir atmosphere (1940s aesthetic, cynical tone)
- Identity revelation (story through gameplay)

---

## Tier 8: The Hobbit (Lessons 4929-4992)

**Goal:** Build advanced text parser with NPC AI and Tolkien adaptation.

**Why this game:** Best text parser on C64. NPCs act independently. Tolkien license. Synthesis of Phase 8.

**Game Requirements:**
- Advanced text parser (complex commands: "ask Gandalf about ring")
- NPC AI (Thorin, Gandalf, Gollum act independently)
- NPC schedules (NPCs move around, pursue goals)
- Combat system (text-based)
- Tolkien narrative (follow the book)
- Day/night cycle
- Weather system
- Animals (Wargs, Eagles act autonomously)
- Inventory management
- Complete Hobbit story (Bag End to Lonely Mountain)

**Skills Introduced:**
- Advanced parser (complex sentence structure)
- NPC AI (characters act independently, not just respond)
- NPC schedules (Thorin might wander off, Gandalf might leave)
- Autonomous world (things happen without player action)
- License adaptation (book → game)
- Everything from Phase 8 synthesized

### Lesson Structure

**Lessons 4929-4936: Advanced Parser**
- L4929-4930: Complex grammar (subject-verb-object-preposition)
- L4931-4932: Parser engine (tokenize, parse tree)
- L4933-4934: Synonym handling (extensive vocabulary)
- L4935-4936: Ambiguity resolution ("which door?")

**Lessons 4937-4944: NPC AI Foundation**
- L4937-4938: NPC data structures (stats, inventory, goals)
- L4939-4940: NPC movement (autonomous pathfinding)
- L4941-4942: NPC goals (Thorin wants treasure, Gollum wants ring)
- L4943-4944: NPC decision making (simple goal-oriented AI)

**Lessons 4945-4952: NPC Interaction**
- L4945-4946: Conversation system (ask X about Y)
- L4947-4948: NPC responses (based on state, relationship)
- L4949-4950: NPC trading (give/take items)
- L4951-4952: NPC following (companions)

**Lessons 4953-4960: World Simulation**
- L4953-4954: Day/night cycle
- L4955-4956: Weather system (affects travel)
- L4957-4958: Animal AI (Wargs hunt, Eagles rescue)
- L4959-4960: World state updates (things change over time)

**Lessons 4961-4968: Combat & Danger**
- L4961-4962: Text-based combat (attack, defend, flee)
- L4963-4964: Combat resolution (stats, randomness)
- L4965-4966: NPC combat (Thorin fights alongside you)
- L4967-4968: Death and injury

**Lessons 4969-4976: Tolkien Narrative**
- L4969-4970: Story structure (chapters, locations)
- L4971-4972: Key events (riddles in dark, barrel escape)
- L4973-4974: Treasure quest (dragon, Arkenstone)
- L4975-4976: Narrative progression (story flags)

**Lessons 4977-4984: World & Locations**
- L4977-4978: Middle-earth map (Shire to Lonely Mountain)
- L4979-4980: Location descriptions (rich text)
- L4981-4982: Travel system (paths, obstacles)
- L4983-4984: Hidden areas and secrets

**Lessons 4985-4992: Polish & Completion**
- L4985-4986: Save/load (complex state)
- L4987-4988: Text pacing and readability
- L4989-4990: Balance (difficulty, NPC behavior)
- L4991-4992: Final polish and testing

---

## Phase 8 Outcome

Students have built **8 complete adventure games** and mastered:

**Inventory Systems:**
- Object pickup/drop
- Inventory UI (text, graphical, windowed)
- Item examination
- Object combinations
- Weight/space limits
- Character-specific inventories

**Puzzle Systems:**
- Object interaction (use X on Y)
- Dependency chains (need A for B for C)
- Character-gated puzzles (unique abilities)
- Sequence-sensitive puzzles (correct order)
- Multiple solutions (player choice)
- Environmental puzzles (room states)

**Dialogue Systems:**
- Dialogue trees (branching conversations)
- Conversation choices (affect outcome)
- NPC conversations (ask about topics)
- Story revelation through dialogue

**Parser Systems:**
- Simple parser (2-word commands)
- Advanced parser (complex grammar)
- Vocabulary and synonyms
- Ambiguity handling
- Command interpretation

**Interface Types:**
- SCUMM verbs (9-verb interface)
- MacVenture (windowed, point-and-click)
- Sierra AGI (parser + graphics)
- Text parser (The Hobbit)

**Narrative Techniques:**
- Story flags (progression tracking)
- Cutscenes (triggered events)
- Multiple endings (choice-based)
- Environmental storytelling (examine text)
- Amnesia narrative (gradual revelation)
- License adaptation (book → game)

**NPC Systems:**
- Character switching (multiple protagonists)
- NPC AI (autonomous behavior)
- NPC schedules (movement, goals)
- Companion mechanics (following, helping)
- NPC trading and interaction

**Game Design:**
- No-death design (Monkey Island)
- Death-trap design (Shadowgate)
- Procedural realism (Police Quest)
- Horror atmosphere (Uninvited)
- Comedy timing (Monkey Island)

**Technical Systems:**
- Save/load (complex state spaces)
- Room-based worlds
- First-person perspective
- Third-person perspective
- Time pressure systems
- Resource management (torches, time)

**Ready for Phase 9:** Students transition from narrative-driven adventures to strategic thinking with real-time and turn-based strategy games.

---

**Version:** 3.0
**Date:** 2025-10-21
**Status:** Complete restructure for 512-lesson phase
**Focus:** 8 adventure games spanning all sub-genres - narrative and puzzle mastery
