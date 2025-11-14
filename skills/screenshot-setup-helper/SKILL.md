---
name: screenshot-setup-helper
description: Use when capturing lesson screenshots - provides platform-specific emulator settings, key bindings, timing, and verification for manual screenshot capture
---

# Screenshot Setup Helper

## Overview

This skill provides comprehensive guidance for manual screenshot capture across all platforms. Screenshots must be captured manually in emulators after code compilation - automated capture is unreliable. Ensures screenshots show actual program output, correct timing, proper filenames, and correct locations.

## When to Use

Use when:
- Creating new lesson with code samples
- Updating existing lesson code (need new screenshots)
- lesson-creation-agent reaches Phase 2 (screenshot verification)
- Screenshot verification fails (wrong output, timing, format)

**Do NOT use when:**
- Lesson has no code samples (text-only)
- Reusing existing screenshots (no code changes)
- Testing/debugging code (not lesson creation)

---

## Why Manual Screenshots?

**The problem with automation:**
- VICE, FCEUX, FUSE, FS-UAE all resist automated capture
- Timing issues (when to capture?)
- Window focus issues
- Emulator-specific quirks

**The solution:**
1. Agent creates loadable code (.prg, .nes, .tap, .adf)
2. User loads in emulator manually
3. User captures screenshot at right moment
4. Agent verifies with READ tool

**Golden rule: As long as the code can be loaded into the emulator, you can capture the screenshot.**

---

## General Screenshot Requirements

### File Format
- **Format:** PNG only
- **Colour depth:** 24-bit RGB (or emulator default)
- **No compression artifacts:** PNG is lossless

### File Naming
```
screenshot-{N}.png
```
- `{N}` = Sequential number starting at 1
- Example: `screenshot-1.png`, `screenshot-2.png`

### File Location
```
/website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/screenshot-{N}.png
```

**Examples:**
- `/website/public/images/commodore-64/phase-0/tier-1/lesson-007/screenshot-1.png`
- `/website/public/images/nintendo-entertainment-system/phase-0/tier-1/lesson-003/screenshot-2.png`
- `/website/public/images/sinclair-zx-spectrum/phase-0/tier-2/lesson-015/screenshot-1.png`
- `/website/public/images/commodore-amiga/phase-0/tier-3/lesson-025/screenshot-1.png`

### What to Capture
- **Complete output:** Show full program result
- **Correct timing:** Capture when output is visible (not mid-frame)
- **No errors:** No error messages, crashes, blank screens
- **Actual output:** Must match code expectations

---

## Platform-Specific Instructions

## Commodore 64 (VICE x64sc)

### Emulator Setup

**Launch command:**
```bash
x64sc -autostart example-1.prg -limitcycles 20000000 -VICIIdsize +sound
```

**Flags explained:**
- `-autostart` = Load and run program automatically
- `-limitcycles` = Run for ~20 seconds (adjust if needed)
- `-VICIIdsize` = Double size window (easier to see)
- `+sound` = Enable audio

**Alternative: Manual load**
```bash
x64sc example-1.prg
# Type LOAD"*",8,1 then RUN in emulator
```

### Settings (Menu → Settings)
- **Video → Double size** = ON (easier to see)
- **Video → VIC-II filters** = OFF (sharp pixels)
- **Video → Fullscreen** = Optional

### Screenshot Capture

**Method 1: Built-in screenshot (RECOMMENDED)**
```
Menu → Snapshot → Save screenshot...
Navigate to: /website/public/images/commodore-64/.../lesson-NNN/
Filename: screenshot-1.png
```

**Method 2: System screenshot**
- **macOS:** Cmd+Shift+4, then Space, click window
- **Linux:** Take screenshot of VICE window
- **Windows:** Win+Shift+S, select region

### Timing
- **BASIC programs:** Capture after READY prompt (program finished)
- **Graphics programs:** Capture when graphics fully drawn
- **Animation:** Capture representative frame (not mid-transition)
- **Input programs:** Capture after expected input shown

### Verification
```bash
# Check screenshot exists
ls /website/public/images/commodore-64/phase-0/tier-1/lesson-007/screenshot-1.png

# View screenshot
open screenshot-1.png  # macOS
# Or use READ tool in Claude Code
```

---

## NES (FCEUX)

### Emulator Setup

**Launch command:**
```bash
fceux example-1.nes
```

**Alternative with config:**
```bash
fceux --loadstate quicksave.fc0 example-1.nes
```

### Settings (Config → Video)
- **Video mode:** SDL
- **Resolution:** Native NES (256×240) or 2x scale
- **Fullscreen:** OFF (easier to capture)
- **OpenGL:** OFF (compatibility)

### Screenshot Capture

**Method 1: Built-in screenshot (RECOMMENDED)**
```
F12 key = Take screenshot
Default location: ~/.fceux/snaps/
Move to: /website/public/images/nintendo-entertainment-system/.../lesson-NNN/screenshot-1.png
```

**Configure screenshot location:**
```
Config → Directories → Snapshots
Set to: /website/public/images/nintendo-entertainment-system/.../lesson-NNN/
```

**Method 2: System screenshot**
- Capture FCEUX window with system screenshot tool

### Timing
- **Boot programs:** Capture after PPU stabilizes (usually 2-3 frames)
- **Graphics programs:** Capture after VBlank when frame complete
- **Animation:** Capture representative frame
- **Input programs:** Capture after expected state

**NES-specific timing issues:**
- Wait for warm-up (2 VBlanks minimum)
- Avoid capturing mid-frame (tearing)
- Sprite 0 hit timing may vary

### Verification
```bash
# Check screenshot
ls /website/public/images/nintendo-entertainment-system/phase-0/tier-1/lesson-003/screenshot-1.png

# View
open screenshot-1.png
```

---

## ZX Spectrum (FUSE)

### Emulator Setup

**Launch command:**
```bash
fuse example-1.tap
```

**Model selection:**
```bash
fuse --machine 48 example-1.tap    # 48K Spectrum (default for Phase 0)
fuse --machine 128 example-1.tap   # 128K Spectrum (if needed)
```

### Settings (Options → General)
- **Emulation speed:** 100% (no turbo)
- **Issue 2 keyboard:** ON (default)
- **Sound:** ON

**Graphics settings (Options → Graphics):**
- **Filter:** None (sharp pixels)
- **Scale:** 2x or 3x (easier to see)

### Screenshot Capture

**Method 1: Built-in screenshot (RECOMMENDED)**
```
F9 key = Save screenshot
Default format: PNG
Default location: Current directory
Move to: /website/public/images/sinclair-zx-spectrum/.../lesson-NNN/screenshot-1.png
```

**Configure screenshot location:**
```
Options → Media → Screenshot directory
Set to: /website/public/images/sinclair-zx-spectrum/.../lesson-NNN/
```

**Method 2: System screenshot**
- Capture FUSE window (Fuse resists automation, manual capture reliable)

### Timing
- **BASIC programs:** Capture after program completes (scroll? prompt)
- **Graphics programs:** Capture when screen fully drawn
- **Border effects:** Ensure border colour visible if relevant
- **BEEP sound:** Capture screen during/after sound (visual confirmation)

**ZX-specific timing notes:**
- Spectrum draws top to bottom (wait for full screen)
- PRINT AT may have scroll delays
- INK/PAPER changes may flash briefly

### Verification
```bash
# Check screenshot
ls /website/public/images/sinclair-zx-spectrum/phase-0/tier-1/lesson-015/screenshot-1.png

# View
open screenshot-1.png
```

---

## Amiga (FS-UAE)

### Emulator Setup

**Launch command:**
```bash
fs-uae --amiga-model=A1200 --hard-drive-0=/code-samples/commodore-amiga/.../lesson-NNN/
```

**Model options:**
- `A500` = OCS (Phase 0-1)
- `A1200` = AGA (Phase 2+)
- `A4000` = Advanced (Phase 3+)

**Alternative: Floppy mount**
```bash
fs-uae --amiga-model=A1200 --floppy-drive-0=example-1.adf
```

### Settings (F12 Menu → Settings)
- **Video → Scale:** 2x or 3x
- **Video → Fullscreen:** OFF
- **Video → Shader:** None (sharp pixels)
- **Audio → Volume:** 100%

### Screenshot Capture

**Method 1: Built-in screenshot (RECOMMENDED)**
```
F12 = Open FS-UAE menu
Screenshot → Save screenshot
Navigate to: /website/public/images/commodore-amiga/.../lesson-NNN/
Filename: screenshot-1.png
```

**Method 2: System screenshot**
- Capture FS-UAE window with system screenshot tool

### Timing
- **AMOS programs:** Capture after screen fully drawn
- **Blitter operations:** Wait for blitter complete
- **Bob animation:** Capture representative frame
- **Copper effects:** Capture when effect visible
- **68K assembly:** Capture after RTS or infinite loop reached

**Amiga-specific timing notes:**
- Workbench load time (wait for desktop)
- CLI programs (wait for prompt after execution)
- Screen mode changes (wait for screen stable)

### Verification
```bash
# Check screenshot
ls /website/public/images/commodore-amiga/phase-0/tier-3/lesson-025/screenshot-1.png

# View
open screenshot-1.png
```

---

## Screenshot Verification Checklist

**After capturing screenshot, verify:**

- [ ] File exists at correct location
- [ ] Filename follows convention (`screenshot-{N}.png`)
- [ ] Format is PNG (not JPG/BMP)
- [ ] Screenshot shows program output (not error/crash/blank)
- [ ] Output matches code expectations
- [ ] Timing correct (not mid-frame, not blank)
- [ ] No emulator UI visible (menu bars, toolbars)
- [ ] Resolution appropriate (native or 2x/3x scale)

**Use READ tool to verify:**
```bash
# In Claude Code
Read(/website/public/images/{platform}/.../lesson-NNN/screenshot-1.png)
# Visually inspect output
```

---

## Common Issues and Fixes

### Issue 1: Screenshot Shows Blank Screen

**Causes:**
- Captured too early (program not started)
- Captured too late (program exited)
- Code has runtime error (crashes before output)

**Fixes:**
1. Check code compiles without errors
2. Run code in emulator manually to verify output
3. Adjust timing (wait longer or capture earlier)
4. Check for runtime errors (BASIC syntax, assembly crashes)

### Issue 2: Screenshot Shows Error Message

**Causes:**
- Code has syntax error (didn't catch in compilation)
- Code has runtime error (divide by zero, illegal quantity)
- Code accesses invalid memory

**Fixes:**
1. Fix code errors first
2. Re-compile and verify
3. Test in emulator before capturing
4. **NEVER capture screenshot of error message**

### Issue 3: Screenshot Shows Partial Output

**Causes:**
- Captured mid-frame (screen drawing)
- Animation captured at wrong moment
- Timing too fast (program still running)

**Fixes:**
1. Wait for complete output
2. Capture after program finishes (READY prompt, prompt, etc.)
3. For animation, choose representative frame
4. Increase `-limitcycles` if needed (VICE)

### Issue 4: Screenshot Has Emulator UI Visible

**Causes:**
- Captured emulator window including menu bar
- Captured with toolbar visible
- Captured with status bar

**Fixes:**
1. Use built-in screenshot feature (crops correctly)
2. Hide emulator UI before system screenshot
3. Crop screenshot to show only output area
4. Use fullscreen mode if available

### Issue 5: Screenshot File Wrong Location

**Causes:**
- Saved to emulator default directory
- Wrong lesson number in path
- Wrong platform name

**Fixes:**
1. Navigate to correct path in save dialog
2. Verify path structure: `/website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`
3. Move file to correct location after capture
4. Update emulator screenshot directory setting

### Issue 6: Screenshot Wrong Format (JPG, BMP)

**Causes:**
- Emulator default format not PNG
- System screenshot tool uses JPG

**Fixes:**
1. Configure emulator to save PNG
2. Convert to PNG if necessary: `convert screenshot.jpg screenshot.png`
3. Always verify format with `file screenshot-1.png`

---

## Anti-Patterns

### 1. Capturing Screenshot of Error Message

**Anti-pattern:**
```
Screenshot shows: "?SYNTAX ERROR IN 10"
```

**Why wrong:** Lesson screenshots must show working code output, not errors.

**Fix:** Fix code first, then capture screenshot of working output.

### 2. Capturing Mid-Frame

**Anti-pattern:**
```
Screenshot shows partial graphics (screen tearing)
```

**Why wrong:** Unprofessional, confusing to learners.

**Fix:** Wait for frame complete, use VBlank timing.

### 3. Including Emulator UI

**Anti-pattern:**
```
Screenshot includes VICE menu bar and toolbar
```

**Why wrong:** Distracting, unprofessional.

**Fix:** Use built-in screenshot feature (crops correctly) or crop manually.

### 4. Wrong Timing (Blank Screen)

**Anti-pattern:**
```
Screenshot captured before BASIC READY prompt (blank screen)
```

**Why wrong:** Doesn't show program output.

**Fix:** Wait for program to complete before capturing.

### 5. JPG Format (Compression Artifacts)

**Anti-pattern:**
```
screenshot-1.jpg with visible compression artifacts
```

**Why wrong:** PNG is lossless, JPG introduces artifacts.

**Fix:** Always use PNG format.

### 6. Wrong Filename

**Anti-pattern:**
```
screenshot_1.png (underscore)
Screen Shot 2025-11-05.png (system default)
example-1-output.png (descriptive but wrong)
```

**Why wrong:** Breaks convention, MDX references won't work.

**Fix:** Always use `screenshot-{N}.png` format.

---

## Integration with Other Skills

**This skill is called by:**

1. **lesson-creation-agent** - Phase 2 (after code creation, before MDX)
2. **Platform-specific skills** - All reference this for screenshot guidance

**After capturing screenshots:**

1. **screenshot-verification** - Verify screenshot content with READ tool
2. **lesson-validation** - Check screenshot references in MDX

---

## Quick Reference

### Screenshot Capture Commands

**C64 (VICE x64sc):**
```bash
x64sc -autostart example-1.prg -limitcycles 20000000 -VICIIdsize
# Menu → Snapshot → Save screenshot...
```

**NES (FCEUX):**
```bash
fceux example-1.nes
# F12 key = screenshot
# Move from ~/.fceux/snaps/ to lesson directory
```

**ZX Spectrum (FUSE):**
```bash
fuse --machine 48 example-1.tap
# F9 key = screenshot
# Move to lesson directory
```

**Amiga (FS-UAE):**
```bash
fs-uae --amiga-model=A1200 --hard-drive-0=/path/to/lesson/
# F12 → Screenshot → Save
```

### File Locations

```
/website/public/images/commodore-64/phase-{N}/tier-{N}/lesson-{NNN}/screenshot-{N}.png
/website/public/images/nintendo-entertainment-system/phase-{N}/tier-{N}/lesson-{NNN}/screenshot-{N}.png
/website/public/images/sinclair-zx-spectrum/phase-{N}/tier-{N}/lesson-{NNN}/screenshot-{N}.png
/website/public/images/commodore-amiga/phase-{N}/tier-{N}/lesson-{NNN}/screenshot-{N}.png
```

### Verification

```bash
# Check exists
ls /website/public/images/{platform}/.../lesson-{NNN}/screenshot-1.png

# View (macOS)
open screenshot-1.png

# View (Claude Code)
Read(/website/public/images/.../screenshot-1.png)
```

---

## The Bottom Line

**Manual screenshot capture ensures authentic output:**
1. Compile code to loadable format (.prg/.nes/.tap/.adf)
2. Launch emulator with compiled code
3. Wait for correct timing (program complete, graphics drawn)
4. Capture with built-in screenshot feature (or system tool)
5. Save to correct location with correct filename
6. Verify with READ tool (check content, not just existence)
7. Fix any issues (errors, timing, format) before proceeding

**Zero tolerance for:**
- Screenshots of error messages (fix code first)
- Blank screenshots (wrong timing)
- Partial output (mid-frame capture)
- JPG format (use PNG always)
- Wrong filenames (must be screenshot-{N}.png)
- Emulator UI visible (crop correctly)
- Unverified screenshots (always READ to verify)

**Automated screenshot capture is unreliable. Manual capture is fast, reliable, and produces authentic results. As long as code loads in emulator, screenshots are straightforward.**
