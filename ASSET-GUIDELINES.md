# Asset Guidelines - Code Like It's 198x

**Version:** 1.0
**Date:** 2025-10-21
**Purpose:** Guide for creating, contributing, and using C64 game assets

---

## Overview

This curriculum provides **three paths** for handling graphics and sound:

### Path A: Quick Start (Use Provided Assets)
**Best for:** Focus on code, learn quickly
**What you get:** CC0/public domain sprites, characters, and music ready to use
**Time investment:** Zero - just download and go

### Path B: Classic Style (Learn to Create)
**Best for:** Authentic C64 experience, complete mastery
**What you get:** Step-by-step tutorials integrated into lessons
**Time investment:** Part of lesson structure (already included)

### Path C: Go Wild (Create & Share)
**Best for:** Creative expression, community building
**What you get:** Tools, guidelines, and a platform to share your work
**Time investment:** As much as you want

**You can mix all three approaches!** Use provided assets for some games, create your own for others, and share your best work with the community.

---

## Asset Repository Structure

```
/assets/
├── sprites/
│   ├── phase-1/
│   │   ├── lesson-001-pong-paddle.spd
│   │   ├── lesson-001-pong-ball.spd
│   │   └── lesson-001-pong-paddle.png (preview)
│   ├── phase-2/
│   └── common/
│       ├── explosions-8x8.spd
│       ├── bullets-generic.spd
│       └── ui-elements.spd
├── characters/
│   ├── phase-1/
│   │   └── lesson-010-breakout-charset.ctm
│   ├── common/
│   │   ├── retro-font-bold.ctm
│   │   └── retro-font-thin.ctm
├── music/
│   ├── phase-2/
│   │   ├── lesson-200-space-invaders-theme.sid
│   │   └── lesson-200-space-invaders-theme.gt2 (GoatTracker)
│   ├── common/
│   │   ├── game-over-jingle.sid
│   │   └── title-screen-music.sid
└── README.md
```

### File Naming Convention

**Format:** `lesson-XXX-game-asset-description.ext`

**Examples:**
- `lesson-001-pong-paddle.spd` (SpritePad sprite)
- `lesson-042-tetris-blocks.spd` (multiple sprites in one file)
- `lesson-100-breakout-charset.ctm` (CharPad character set)
- `lesson-200-invaders-march.sid` (SID music)
- `lesson-200-invaders-march.gt2` (GoatTracker source)

**Common assets** (reusable across lessons):
- `explosions-8x8.spd`
- `bullets-generic.spd`
- `retro-font-bold.ctm`
- `game-over-jingle.sid`

---

## File Formats

### Sprites
- **Primary:** `.spd` (SpritePad 2.0+ format)
- **Preview:** `.png` (auto-generated or manual screenshot)
- **Tools:** SpritePad (https://csdb.dk/release/?id=132081)

**Sprite constraints:**
- 24×21 pixels (C64 sprite size)
- Single-color or multicolor mode
- Must fit C64 color palette (16 colors)

### Character Sets
- **Primary:** `.ctm` (CharPad 3.0+ format)
- **Preview:** `.png` (charset preview)
- **Tools:** CharPad (https://subchristsoftware.itch.io/charpad-free-edition)

**Character constraints:**
- 8×8 pixels per character
- 256 characters max
- Standard or multicolor mode

### Music & Sound
- **Compiled:** `.sid` (SID music format - playable in VICE)
- **Source:** `.gt2` (GoatTracker 2 source - editable)
- **Tools:** GoatTracker 2 (https://sourceforge.net/projects/goattracker2/)

**Music guidelines:**
- SID chip constraints (3 voices, standard waveforms)
- Consider PAL vs NTSC timing
- File size reasonable for C64 memory

### Palette Files
- **Format:** `.vpl` (VICE palette - if custom palette used)
- **Tools:** Text editor (it's just a text file with RGB values)

---

## Quality Standards

### All Assets Must:

1. **Follow C64 constraints**
   - Sprites: 24×21 pixels, max 16 colors
   - Characters: 8×8 pixels
   - Music: 3 SID voices
   - No "impossible" graphics (modern hi-res, gradients, etc.)

2. **Be readable/usable**
   - Sprites clearly recognizable at C64 resolution
   - Characters legible (if text)
   - Music appropriate for gameplay (not distracting)

3. **Match lesson context**
   - Pong paddle looks like a paddle
   - Space Invaders aliens look retro/alien
   - Music fits game genre (arcade = upbeat, puzzle = calm)

4. **Include preview images**
   - `.png` screenshot showing asset in context
   - Or at least zoomed view of sprite/character

### Good Examples:

✅ **Sprite:** 8×8 pixel ball, white, simple circle
✅ **Character set:** Bold, readable font for scores
✅ **Music:** 30-second looping theme, upbeat, not annoying

### Bad Examples:

❌ **Sprite:** 64×64 pixel detailed spaceship (too big!)
❌ **Character set:** Fancy script font (unreadable at 8×8)
❌ **Music:** 5-minute progressive rock epic (too long, wrong vibe)

---

## Licensing Requirements

**ALL contributed assets MUST be:**

### CC0 (Public Domain Dedication)

By contributing assets, you agree:
- Asset is dedicated to **public domain**
- **No attribution required** (but appreciated!)
- Can be used commercially by students
- Can be modified freely
- No warranties or liability

**Why CC0?** Students create games they can publish and sell. Attribution requirements create legal complexity.

### How to Apply CC0

Include `LICENSE.txt` in your contribution:

```
To the extent possible under law, [Your Name] has waived all copyright
and related or neighboring rights to [Asset Name].

This work is published from: [Your Country]

CC0 1.0 Universal
https://creativecommons.org/publicdomain/zero/1.0/
```

**Or** just state in your pull request: "I dedicate these assets to CC0 public domain."

---

## Contributing Assets

### Option 1: GitHub Pull Request

1. Fork the repository
2. Add assets to appropriate `/assets/` directory
3. Follow naming conventions
4. Include preview images (`.png`)
5. Add entry to `/assets/README.md`
6. Create pull request with:
   - Asset description
   - CC0 dedication statement
   - Your name (for credits, optional)

### Option 2: Community Submissions

If you're not comfortable with Git:

1. Create assets using C64 tools
2. Email to: [curriculum maintainer email]
3. Include:
   - Asset files (`.spd`, `.ctm`, `.sid`)
   - Preview images
   - Description (what lesson/game it's for)
   - CC0 dedication statement
   - Your name for credits (optional)

### What Gets Accepted

**High priority:**
- Assets for specific lessons (Pong paddle, Tetris blocks, etc.)
- Reusable common assets (explosions, bullets, fonts)
- Complete sets (all sprites for a game)

**Medium priority:**
- Alternative versions (different art styles)
- Enhanced versions (more detailed sprites)
- Music variations (different tempo/style)

**Lower priority:**
- Extremely specialized assets (used once)
- Duplicate common assets (we already have 5 explosion sprites)

---

## Credit Attribution

### Contributors Get Credit

Even though assets are CC0 (no attribution required), we credit contributors:

**In `/assets/README.md`:**
```markdown
### Contributors
- **Alice Smith** - Pong sprites, Breakout character set
- **Bob Jones** - Space Invaders music pack
- **Carol Lee** - Generic explosions and bullets
```

**In lesson materials:**
```markdown
## Assets Used
- Sprites: `lesson-001-pong-paddle.spd` (contributed by Alice Smith)
- Music: `common/game-over-jingle.sid` (contributed by Bob Jones)
```

**On project website:** Contributors hall of fame with optional links to portfolios/websites.

### How to Be Credited

Include in your contribution:
- **Name:** How you want to be credited
- **Link:** (optional) Portfolio, website, or social media
- **Bio:** (optional) One sentence about yourself

**Example:**
```
Name: Alice Smith
Link: https://alice-retro-art.com
Bio: Pixel artist and C64 enthusiast since 1985
```

---

## Integrated Tutorials (Path B)

Lessons that teach asset creation include:

### Sprite Creation Lessons
**Phase 1, Tier 1 (Pong):**
- Lesson 5: Introduction to SpritePad
- Lesson 6: Creating paddle sprite (24×21 pixels)
- Lesson 7: Creating ball sprite (8×8 circle)
- Lesson 8: Exporting and using sprites in code

**Phase 2 (Space Invaders):**
- Creating alien sprites (multicolor mode)
- Animation frames (alternate sprites)
- Player ship and bullets

### Character Set Lessons
**Phase 1 (Breakout):**
- Introduction to CharPad
- Designing brick characters (8×8 blocks)
- Creating score display font

### Music Creation Lessons
**Phase 2 (Space Invaders):**
- Introduction to GoatTracker (tracker interface)
- Creating simple march theme (like original game)
- Sound effects (shoot, explosion, UFO)

**Phase 7 (RPG Systems):**
- Creating town theme music
- Battle music
- Sound effect library

### Students Can Skip

All asset creation lessons are **optional**:
- Use provided assets → Skip asset lessons
- Create your own → Follow asset tutorials
- Mix both → Use provided for some, create for others

---

## Tools and Resources

### Essential Tools (All Free)

| Tool | Purpose | Download |
|------|---------|----------|
| **SpritePad** | Sprite editor | https://csdb.dk/release/?id=132081 |
| **CharPad** | Character set editor | https://subchristsoftware.itch.io/charpad-free-edition |
| **GoatTracker 2** | SID music tracker | https://sourceforge.net/projects/goattracker2/ |
| **VICE** | C64 emulator (test assets) | https://vice-emu.sourceforge.io/ |

### Learning Resources

**Sprite Design:**
- "C64 Sprite Tutorial" by Zzap64 (YouTube)
- "Pixel Art for C64" guide (CSDb forums)

**Character Sets:**
- CharPad manual (included with tool)
- "Designing C64 Fonts" tutorial

**Music Creation:**
- GoatTracker manual (comprehensive)
- "SID Chip Basics" video series
- OctaMED users: GoatTracker feels familiar (tracker interface)

### Color Palettes

Use standard C64 palette (16 colors):
```
0: Black       4: Purple      8: Orange      12: Dark Gray
1: White       5: Green       9: Brown       13: Light Green
2: Red         6: Blue       10: Light Red   14: Light Blue
3: Cyan        7: Yellow     11: Dark Gray   15: Light Gray
```

**Tools provide palette pickers** - no need to memorize hex codes.

---

## Asset Integration Process

### How Assets Get Added to Lessons

1. **Contribution received** (via PR or email)
2. **Quality review** (follows C64 constraints? Readable? Appropriate?)
3. **Licensing check** (CC0 dedicated?)
4. **Added to repository** (proper naming, directory structure)
5. **Documented in `/assets/README.md`**
6. **Integrated into lesson** (code examples updated, download links added)
7. **Contributor credited** (name added to credits)

### Using Assets in Lessons

**Download link in lesson:**
```markdown
## Assets Needed
- Paddle sprite: [Download lesson-001-pong-paddle.spd](/assets/sprites/phase-1/lesson-001-pong-paddle.spd)
- Ball sprite: [Download lesson-001-pong-ball.spd](/assets/sprites/phase-1/lesson-001-pong-ball.spd)

**Or create your own** - See Lesson 5: Sprite Creation Tutorial
```

**Code references asset:**
```assembly
; Load sprite data from lesson-001-pong-paddle.spd
; (Export as binary from SpritePad first)

    LDX #$00
LOAD_SPRITE:
    LDA SPRITE_DATA,X
    STA $2000,X     ; Sprite data location
    INX
    CPX #$3F        ; 63 bytes per sprite
    BNE LOAD_SPRITE

SPRITE_DATA:
    INCBIN "lesson-001-pong-paddle.bin"  ; Converted from .spd
```

---

## Frequently Asked Questions

### Q: Do I have to create assets?
**A:** No! Use provided CC0 assets and focus on code.

### Q: Can I use assets from old C64 games?
**A:** **NO!** Those are copyrighted. Only use:
- Your own original creations (CC0)
- Community-contributed CC0 assets
- Public domain assets (confirm licensing!)

### Q: What if I'm terrible at pixel art?
**A:** That's why we provide assets! Or follow tutorials - start simple (Pong paddle is literally a rectangle).

### Q: Can I sell games I make with these assets?
**A:** **YES!** All assets are CC0 public domain. You can use them commercially, modify them, whatever you want.

### Q: I made better sprites than the provided ones. Can I contribute?
**A:** **YES PLEASE!** We love improvements. Submit via PR or email.

### Q: Do I get paid for contributions?
**A:** No, this is a community project. But you get:
- Credit in documentation
- Link to your portfolio/website
- Warm fuzzy feeling of helping learners
- Experience creating C64 assets

### Q: What if my asset doesn't get accepted?
**A:** We'll explain why (usually licensing or technical constraints) and help you fix it if possible.

### Q: Can I contribute music if I don't know GoatTracker?
**A:** Yes! Submit `.sid` files from any SID editor. GoatTracker `.gt2` source files are bonus (helps others learn from your work).

### Q: I have OctaMED experience. Will GoatTracker feel familiar?
**A:** **YES!** Both are tracker-based. Pattern editor, instrument definitions, sequencer - same concepts. You'll pick it up quickly.

---

## Getting Started Checklist

### For Asset Users (Path A):
- [ ] Browse `/assets/` repository
- [ ] Download assets for your lesson
- [ ] Follow lesson code examples for integration
- [ ] Focus on learning assembly and game logic

### For Asset Creators (Path B):
- [ ] Download SpritePad, CharPad, GoatTracker
- [ ] Follow integrated tutorials in lessons
- [ ] Create assets for your games
- [ ] (Optional) Share your best work with community

### For Contributors (Path C):
- [ ] Create C64 assets using proper tools
- [ ] Dedicate to CC0 public domain
- [ ] Follow naming conventions
- [ ] Submit via PR or email
- [ ] Get credited in documentation

---

## Community

### Where to Discuss Assets

- **GitHub Discussions:** General asset talk, requests, showcases
- **Discord:** [Link to Discord] - `#asset-creation` channel
- **CSDb Forums:** Broader C64 community (pixel art, music)

### Asset Requests

**Need an asset that doesn't exist?** Create an issue:
```
Title: [ASSET REQUEST] Pac-Man style ghost sprites
Description: Looking for 4 different ghost sprites (24×21) in multicolor mode
For: Phase 3, Lesson 150 (maze chase game)
Style: Retro, cute, distinct colors
```

**Someone might create it for you!**

---

## Final Notes

**Remember:**
- Assets are **tools to learn code**, not the main goal
- **CC0 licensing** keeps everything simple and legal
- **Three paths** (use, create, share) - pick what works for you
- **Community contributions** make this better for everyone

**Questions?** Open a GitHub discussion or check Discord `#asset-creation` channel.

---

**Version:** 1.0
**Date:** 2025-10-21
**License:** This document is CC0 (public domain)
**Maintained by:** Code Like It's 198x curriculum team
