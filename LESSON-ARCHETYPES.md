# Lesson Archetypes Guide

**Last Updated:** 2025-01-17
**Philosophy:** Teach concepts authentically. Avoid formulas. Trust the hardware to be compelling.

---

## The Four Archetypes

| Archetype | Marker | When to Use |
|-----------|--------|-------------|
| **Discovery** | None | Teaching a new concept (most lessons) |
| **Challenge** | Lightning bolt | Learner solves problem with recent skills |
| **Synthesis** | Link icon | Combine concepts into complete program |
| **Deep Dive** | Microscope | Hardware internals (optional advanced) |

**Note:** Reference material (color tables, memory maps, register references) belongs in [The Vault](/vault), not lessons.

**Important:** These are patterns, not rigid templates. Adapt them. Break them when it serves the lesson.

---

## 1. Discovery (Standard Teaching Lesson)

**Purpose:** Introduce a concept, show how it works, invite experimentation.

**Most lessons are Discovery lessons.** No icon needed.

### Typical Structure

```markdown
## [Clear Title - What This Teaches]

[Brief opening - what this does, why it matters]

## Try This First

[5-10 line simple demonstration]

Type this in and RUN it.

## The Full Program

[20-40 line impressive result]

![Screenshot](/images/lessons/commodore-64/phase-0/tier-2/lesson-023.png)

[Brief note on BASIC speed if relevant]

## How It Works

[Explain the hardware/concept using chip names and addresses]

## Experiment

Try changing [specific thing]. What happens?
```

### What to Include

- What the hardware is doing
- Memory addresses and chip names
- Parameters to experiment with
- Honest assessment of BASIC speed where relevant

### What to Avoid

- Forcing historical game references every lesson
- Repeating "you're controlling hardware..." constantly
- Claiming BASIC techniques match assembly speed
- Using the same opening formula repeatedly

### When to Reference Games/History

**Good reasons:**
- Specific programmer solved an interesting problem
- Game pioneered a clever technique
- Constraint led to creative solution
- Illuminates why hardware works this way

**Example of genuine connection:**
```markdown
Andrew Braybrook discovered you could reuse sprites mid-screen by timing
writes to VIC-II registers. *Uridium* showed 20+ sprites using only the
8 hardware sprites available.

(We'll build this in assembly - BASIC is too slow for the precise timing.)
```

**Example of forced connection:**
```markdown
This is the same sprite enable register every C64 game used!
[Adds nothing meaningful - delete this]
```

### Modern Relevance (Light Touch)

Mention occasionally, not every lesson:
- "Same principle as polling input in game engines"
- "Direct hardware access - like GPU programming"
- "Raster timing - similar to vsync in modern graphics"

**Frequency:** Maybe once per tier. Trust learners to see patterns themselves.

---

## 2. Challenge (Problem-Solving Exercise)

**Purpose:** Let learners apply recent concepts independently before showing solution.

**Mark clearly:** ⚡ in title

### Structure

```markdown
---
title: "⚡ Challenge: Make a Sprite Bounce"
---

## The Challenge

Make a sprite bounce off screen edges.

**You've learned:**
- Sprite positioning (Lesson 18)
- Variables and loops (Lessons 5-7)
- IF statements (Lesson 12)

Try solving this yourself before looking at the hints.

## Hints

<details>
<summary>Hint 1: Direction Variables</summary>

Use DX and DY to track direction (1 or -1).

</details>

<details>
<summary>Hint 2: Edge Detection</summary>

```basic
IF X<=0 OR X>=320 THEN DX=-DX
```

</details>

## Solution

[Complete working program]

[Explanation of approach]

## Take It Further

- Add a second sprite bouncing differently
- Change speed (DX=2, DY=2)
- Make it change color when hitting edges
```

### Key Points

- Clearly marked with lightning bolt in title
- Prerequisites stated explicitly
- Solvable with recent lessons
- Progressive hints (collapsible)
- Solution at bottom
- Extension suggestions

**Frequency:** Maybe 1-2 per tier. Optional detours for engaged learners.

---

## 3. Synthesis (Combining Concepts)

**Purpose:** Build something substantial using multiple recent concepts.

**Mark clearly:** 🔗 in title

**When:** After 8-12 related lessons accumulate

### Structure

```markdown
---
title: "🔗 Synthesis: Interactive Game Foundation"
---

## What We're Building

A complete game combining everything from Tier 2:
- Sprites (Lessons 18-19)
- Joystick (Lesson 20)
- Collisions (Lesson 21)
- Sound (Lesson 22)
- Scoring (Lesson 23)

You'll create "Dodge the Asteroids" - control ship, avoid obstacles, score points.

## Prerequisites Check

Comfortable with:
- [x] Sprite positioning
- [x] Reading joystick input
- [x] Detecting collisions
- [x] Playing sounds
- [x] Displaying numbers

If any feel shaky, review those lessons first.

## Building Step By Step

### Step 1: Setup (Lines 10-50)
[Initialization code]

### Step 2: Player Control (Lines 60-100)
[Joystick input code]

### Step 3: Obstacles (Lines 110-150)
[Enemy sprite movement]

### Step 4: Collision & Score (Lines 160-200)
[Detection and points]

## The Complete Program

[Full 60-80 line program]

![Complete game running](/images/lessons/commodore-64/phase-0/tier-2/lesson-032.png)

This is BASIC speed - slower than assembly, but the concepts are identical.
Assembly lessons will show how to build this at full speed.

## What You've Proven

You can:
- Build complete interactive programs
- Manage multiple hardware systems simultaneously
- Create engaging real-time experiences

This is the foundation. Assembly will add speed.
```

### Key Points

- Marked with link icon in title
- Lists prerequisites
- Creates complete, substantial program
- Step-by-step construction
- Honest about BASIC vs assembly
- Emphasizes learner accomplishment

**Avoid claiming:** "Same as professionals did" (they used assembly)
**Instead emphasize:** "Same hardware, same principles, foundation for assembly"

**Frequency:** Every 8-12 lessons when concepts naturally accumulate.

---

## 4. Deep Dive (Hardware Internals)

**Purpose:** Explain WHY hardware works this way (optional, for curious learners).

**Mark clearly:** 🔬 in title

**State upfront:** "You don't need this to USE the feature"

### Structure

```markdown
---
title: "🔬 Deep Dive: Inside the VIC-II Sprite System"
---

## You Don't Need This

Lesson 18 shows you how to use sprites. This explains what's happening
inside the VIC-II chip when you POKE sprite registers.

## The VIC-II Architecture

The VIC-II is a separate processor running alongside the 6510 CPU.
While your BASIC program runs, VIC-II constantly:

1. Reads sprite data from RAM
2. Checks sprite enable register ($D015)
3. Fetches X/Y coordinates
4. Draws sprites onto electron beam

50 times per second (PAL), independent of your program.

## Why Sprite Pointers Live at $07F8

[Hardware constraint explanation]

## The Multiplexing Trick

VIC-II can only display 8 sprites. But games like *Mayhem in Monsterland*
show 20+. How?

Raster interrupts. When the electron beam finishes drawing sprites at top
of screen:
1. Reposition those same 8 sprites to middle
2. VIC-II draws them again
3. Repeat for bottom

Result: 8 hardware sprites × 3 positions = 24 visible sprites.

(Assembly only - BASIC is too slow for the precise timing required.)

## See Also

- [VIC-II Chip](/vault/vic-ii) - Complete register reference
- Lesson 18: Using sprites (practical)
- Phase 3, Lesson 145: Sprite multiplexing in assembly
```

### Key Points

- Marked with microscope icon in title
- "You don't need this" upfront
- Explains WHY, not just HOW
- Hardware constraints as context
- Links to Vault for reference material
- Links to practical lessons

**Frequency:** 5-10% of lessons. Always optional. Never blocks progress.

---

## Reference Material: Lessons vs Vault

### **Belongs in Vault:**

- Color code tables → [VIC-II](/vault/vic-ii)
- Complete memory maps → [Commodore 64](/vault/commodore-64)
- SID register reference → [SID Chip](/vault/sid-chip)
- BASIC command syntax → [Commodore 64 BASIC](/vault/commodore-64-basic)
- Complete chip documentation
- Historical game information
- Programmer biographies

### **Belongs in Lessons (Inline):**

- Quick syntax for THIS lesson's concept
- Memory addresses relevant to THIS technique
- Brief register explanations specific to THIS code

### **Example of Good Inline Reference:**

```markdown
## Quick Reference

**Sprite positioning:**
- X position: POKE 53248 + (sprite# × 2), X
- Y position: POKE 53249 + (sprite# × 2), Y
- Enable: POKE 53269, bitmask (1=sprite 0, 2=sprite 1, etc.)

See [VIC-II](/vault/vic-ii) for complete register documentation.
```

**Don't:** Recreate entire VIC-II register table in every sprite lesson.
**Do:** Show the specific registers THIS lesson uses, link to Vault for complete reference.

---

## Avoiding Formula

### Toxic When Overused

- "You're controlling the same hardware as..."
- "This technique powered [famous game]..."
- "Modern engines use this principle..."
- "You're programming [chip name] directly..."

**Use these sparingly.** Once per tier, not every lesson.

### Fresh Approaches

- Let the screenshot speak
- Start with the concept directly
- Focus on what the hardware does
- Trust the idea is interesting
- Vary your openings completely

### Example Variety

**Lesson 18 opening:**
```markdown
## Enabling Sprites

The VIC-II can display 8 hardware sprites. POKE 53269 to enable them.
```

**Lesson 20 opening:**
```markdown
## Reading the Joystick

Port $DC00 gives you direct hardware access. No operating system layer.
```

**Lesson 22 opening:**
```markdown
## First Sounds

The SID chip at $D400 has three oscillators. Program them directly.
```

**All different. All clear. No formula.**

---

## Phase 0 Honesty

BASIC is slow. Assembly is fast. Be clear about this.

### Phase 0 Framing

Good approaches:
- "BASIC proves the concept"
- "Assembly lessons will show full-speed techniques"
- "Slower, but you can see what's happening"
- "Foundation for assembly mastery"

### Avoid

- Pretending BASIC matches assembly speed
- Claiming BASIC games were professional quality
- Apologizing for BASIC

### Do

- Respect BASIC for what it is
- Acknowledge speed honestly
- Show it teaches real concepts
- Point toward assembly as next step

---

## Quality Over Formula

The Magic Test (from LESSON-WORKFLOW.md) focuses on intrinsic qualities:

1. **Immediacy** - Something happens fast
2. **Hardware connection** - Metal is visible
3. **Experimentation** - Safe to tinker
4. **Clarity** - Focus is obvious
5. **Authenticity** - Honest about what this is

**Not required:**
- Historical game reference
- Modern relevance mention
- "You're controlling hardware" phrase
- Specific opening formula

**Variety matters more than formula.**

---

## Choosing the Right Archetype

```
What are you teaching?

├─ New concept/technique → Discovery (no icon)
│
├─ Consolidating recent skills
│  ├─ Problem to solve → Challenge (⚡)
│  └─ Build something substantial → Synthesis (🔗)
│
└─ How hardware works internally → Deep Dive (🔬)
```

**Reference material?** → Create Vault entry, link from lesson

---

## See Also

- [LESSON-WORKFLOW.md](LESSON-WORKFLOW.md) - Complete authoring guide
- [CLAUDE.md](../CLAUDE.md) - Project standards
- [README.md](../README.md) - Project philosophy
- [The Vault](/vault) - Reference material and history

---

**Final thought:** If you're asking "should I mention [famous game]?" - you probably shouldn't. If the connection is obvious and illuminating, you won't need to ask.
