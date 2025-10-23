# Demoscene Comparison - Licensing Challenge

## Problem

Finding **freely licensed** C64 game and demo screenshots is difficult:
- Most commercial game screenshots are copyrighted
- Most demoscene screenshots are copyrighted by their creators
- Fair use applies for criticism/education, but unclear for commercial presentations
- MobyGames, CSDb screenshots: unclear licensing

## Options

### **Option A: Create Our Own Screenshots** ✅ SAFEST
**Approach**: Use C64 emulator (VICE) to capture our own screenshots

**For "1985 commercial game" side:**
1. Download public domain C64 game from Lemon64 or Internet Archive
2. Run in VICE emulator (x64sc)
3. Capture screenshot showing typical 1980s graphics
4. We own the screenshot (even if game is public domain)

**For "2024 demoscene" side:**
1. Download recent demo from CSDb (e.g., Fairlight's "13:37" or "The Demo Coder")
2. Run in VICE
3. Capture screenshot at impressive effect moment
4. Fair use argument stronger (educational, transformative)

**Time needed**: 30-60 minutes
**Legal risk**: Minimal (fair use + educational context)

### **Option B: Use Descriptive Text Instead** ✅ SAFE
**Approach**: Don't use actual screenshots—use text description

**Slide 18 could say:**
```
Beyond 1980s games.
Demoscene tricks.
Modern techniques discovered since.

From simple sprites and backgrounds...
...to multicolor raster effects,
software FLI modes, and
real-time 3D vector objects.

All on the same 1982 hardware.
```

**Pros**: Zero licensing issues, emphasizes achievement
**Cons**: Less visceral impact than visual proof

### **Option C: Stylized Representation** ✅ CREATIVE
**Approach**: Create artistic representation, not actual screenshots

**Left side**: Simple colored blocks representing sprites
**Right side**: Complex gradient/effect pattern
**Caption**: "1985 → 2024: Same Hardware, Different Techniques"

**Pros**: Avoids copyright, creative, professional
**Cons**: Less authentic than real screenshots

### **Option D: Request Permission** ⚠️ SLOW
**Approach**: Email demoscene group for permission

Example: Contact Fairlight via CSDb, explain educational use, request screenshot permission

**Pros**: Proper licensing if granted
**Cons**: Could take weeks, might be denied

### **Option E: Fair Use Assertion** ⚠️ MODERATE RISK
**Approach**: Use screenshots under fair use doctrine

**Fair use factors favor you:**
- ✅ Educational/non-profit purpose
- ✅ Transformative (teaching, not entertainment)
- ✅ Small portion (1 screenshot from 1000s of frames)
- ✅ No market harm (promotes retro gaming)

**BUT:**
- ⚠️ Not a legal certainty
- ⚠️ Depends on jurisdiction
- ⚠️ Commercial presentation context matters

## My Recommendation

**Go with Option A: Create Our Own Screenshots**

### Implementation Plan

1. **Download public domain C64 game** (5 min)
   - Visit Lemon64: https://www.lemon64.com/games/list.php?list_company=public-domain
   - Choose simple game from mid-1980s (platformer, shooter, puzzle)
   - Download .d64 or .prg file

2. **Capture "commercial game" screenshot** (10 min)
   - Open VICE (x64sc -autoload game.d64)
   - Play until typical gameplay visible
   - Press Alt+Shift+P (screenshot) or use File → Screenshot
   - Save as "commercial-1985.png"

3. **Download modern demo** (5 min)
   - Visit CSDb: https://csdb.dk/release/?id=242855 (Fairlight "13:37")
   - Download .d64 file
   - License: Demos are typically more permissive for educational use

4. **Capture "demoscene" screenshot** (10 min)
   - Open VICE (x64sc -autoload demo.d64)
   - Let demo run until impressive effect appears
   - Capture moment with raster bars, FLI graphics, or 3D vectors
   - Save as "demoscene-2024.png"

5. **Create comparison** (10 min)
   - Use ImageMagick to create side-by-side:
   ```bash
   magick \( commercial-1985.png -resize 800x600 \) \
     \( demoscene-2024.png -resize 800x600 \) \
     +append -background white \
     -gravity south -splice 0x50 \
     -pointsize 36 -annotate +200+10 "1985 Commercial" \
     -annotate +1000+10 "2024 Demoscene" \
     slide-18-comparison.jpg
   ```

6. **Insert into presentation** (5 min)
   - Same process as before (unpack, insert, pack)

**Total time**: ~45 minutes
**Legal risk**: Minimal (public domain + fair use)
**Visual impact**: HIGH

## Alternative: Just Skip It

Given the complexity and time investment, you could also:
- **Stick with 2 images** (current state)
- **Add text to Slide 18** emphasizing techniques without visual proof
- **Trust that your target audience** (software engineers) understands the technical achievement

Your presentation is already strong with the systems montage and lesson screenshot. The demoscene comparison is "nice to have" but not essential if licensing concerns or time investment feel excessive.

## Your Call

Which option feels right to you?
- **Option A** (DIY screenshots): Most authentic, 45 min investment
- **Option B** (Text only): Safest, quickest
- **Option C** (Stylized): Creative middle ground
- **Skip it**: Current 2 images are sufficient

I'm ready to implement whichever you choose!
