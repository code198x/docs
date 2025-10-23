# Presentation Images - Ready to Use

## Location

All images prepared at:
```
/Users/stevehill/Projects/Code198x/docs/workspace/presentation-images/
```

---

## Available Images

### **1. Slide 9: System Scope Montage** ✅ READY

**File**: `slide-9-systems-montage.jpg`
- **Dimensions**: 7200 × 1400 pixels (5:1 aspect ratio)
- **Size**: 2.6 MB
- **Format**: JPEG, sRGB
- **License**: Public Domain (Vanamo Online Game Museum)

**Systems included** (left to right):
1. **Atari 2600** (1977) - Wood-panel classic, "dawn of home computing"
2. **Commodore 64** (1982) - Your origin story machine
3. **Game Boy** (1989) - Handheld revolution
4. **Dreamcast** (1999) - Late 90s innovation
5. **PlayStation 2** (2000) - "PS2 era" endpoint

**Usage**: Insert on slide 9 after text "71 systems. From the dawn of home computing to the PS2 era."

---

### **2. Slide 27: Lesson Screenshot** ✅ READY

**File**: `lesson-screenshot.png`
- **Dimensions**: 384 × 272 pixels (native C64 screenshot)
- **Size**: 1.3 KB
- **Format**: PNG
- **License**: Your own content

**Content**: Commodore 64 BASIC lesson showing hardware interaction (lesson-008/example-2)

**Usage**: Insert on slide 27 as proof the curriculum exists. Position after text showing "what you get."

---

## Individual System Images (Also Available)

If you prefer to use individual system images instead of the montage:

### **Commodore 64**
- **File**: `commodore-64.jpg`
- **Dimensions**: 4600 × 2600 pixels
- **Size**: 3.1 MB
- **Source**: Commodore-64-Computer-FL.jpg (Wikimedia Commons)

### **Atari 2600**
- **File**: `atari-2600.jpg`
- **Dimensions**: 3940 × 2300 pixels
- **Size**: 2.5 MB
- **Source**: Atari-2600-Wood-4Sw-Set.jpg (Wikimedia Commons)

### **Game Boy**
- **File**: `game-boy.jpg`
- **Dimensions**: 2820 × 3420 pixels (portrait)
- **Size**: 2.3 MB
- **Source**: Game-Boy-FL.jpg (Wikimedia Commons)

### **Dreamcast**
- **File**: `dreamcast.jpg`
- **Dimensions**: 3720 × 2730 pixels
- **Size**: 1.1 MB
- **Source**: Sega-Dreamcast-Console-FL.jpg (Wikimedia Commons)

### **PlayStation 2**
- **File**: `playstation-2.jpg`
- **Dimensions**: 2720 × 3300 pixels (portrait)
- **Size**: 1.8 MB
- **Source**: PS2-Fat-Console-Set.jpg (Wikimedia Commons)

All individual images are public domain from the Vanamo Online Game Museum (Evan Amos).

---

## How to Insert into Presentation

### **Method 1: PowerPoint (macOS)**

1. Open `/Users/stevehill/Desktop/Code Like It's 198x - Updated.pptx`

2. **For Slide 9 (Systems Montage)**:
   - Navigate to Slide 9 (currently shows just text)
   - Insert → Picture → Picture from File
   - Select `slide-9-systems-montage.jpg`
   - Resize to fill slide width (~10" wide)
   - Position below or above text (your choice)

3. **For Slide 27 (Lesson Screenshot)**:
   - Navigate to Slide 27 (transition slide before "What You Get")
   - Insert → Picture → Picture from File
   - Select `lesson-screenshot.png`
   - Keep small (~3-4" wide) and center
   - Position prominently (C64 screenshot is iconic)

### **Method 2: Keynote (macOS)**

1. Open PPTX in Keynote (it will convert)

2. **Insert images**:
   - Drag and drop image files directly onto slides
   - Use Format → Arrange → Send to Back (if text overlaps)
   - Resize with corner handles (hold Shift to maintain aspect ratio)

---

## Design Recommendations

### **Slide 9 Layout Options**

**Option A: Image Above Text** (Recommended)
```
┌─────────────────────────────┐
│                             │
│  [System Montage Image]     │
│                             │
├─────────────────────────────┤
│  71 systems.                │
│  From the dawn of home      │
│  computing to the PS2 era.  │
│  8-bit, 16-bit, 32-bit,     │
│  64-bit.                    │
└─────────────────────────────┘
```

**Option B: Image Below Text**
```
┌─────────────────────────────┐
│  71 systems.                │
│  From the dawn of home      │
│  computing to the PS2 era.  │
│  8-bit, 16-bit, 32-bit,     │
│  64-bit.                    │
├─────────────────────────────┤
│                             │
│  [System Montage Image]     │
│                             │
└─────────────────────────────┘
```

**Option C: Image Only** (Bold choice)
- Remove text entirely from Slide 9
- Let the montage speak for itself
- Text on Slide 10 provides context

### **Slide 27 Layout**

Since this is currently a transition slide (blank or minimal), center the screenshot:

```
┌─────────────────────────────┐
│                             │
│                             │
│    ┌───────────────┐        │
│    │               │        │
│    │  C64 Screen   │        │
│    │  Screenshot   │        │
│    │               │        │
│    └───────────────┘        │
│                             │
│  Optional caption:          │
│  "One of 8,256 lessons"     │
│                             │
└─────────────────────────────┘
```

---

## Color Consistency Check

Your presentation uses:
- **Purple-gray**: #5D5B7A (main text)
- **Blue**: #01A9F5 (accent)
- **Cream**: #FEFCF8 (backgrounds)

The Vanamo images have:
- **Neutral gray backgrounds** - Compatible with your design
- **Natural hardware colors** - Won't clash
- **Clean professional photography** - Matches your aesthetic

No color adjustments needed. The images will integrate seamlessly.

---

## File Size Impact

**Current presentation**: 2.1 MB

**After adding images**:
- Slide 9 montage: +2.6 MB
- Slide 27 screenshot: +1.3 KB (negligible)

**New total**: ~4.7 MB (still reasonable for email/web)

If file size is a concern, images can be compressed:
```bash
# Reduce montage to 80% quality (saves ~40%)
magick slide-9-systems-montage.jpg -quality 80 slide-9-systems-montage-compressed.jpg
```

---

## Attribution (Optional but Recommended)

While the images are public domain (no attribution required), you could add a final slide or note:

```
Hardware photography by Evan Amos
Vanamo Online Game Museum
commons.wikimedia.org/wiki/User:Evan-Amos
Public Domain
```

This adds credibility and supports the photographer's work.

---

## Alternative Montage Layouts

If the 5-system horizontal montage feels too wide or cramped, alternative arrangements:

### **2-3 Layout** (Compact)
```
[ Atari ]  [ C64 ]  [ Game Boy ]
[ Dreamcast ]    [ PS2 ]
```
Command:
```bash
magick \( \( atari-2600.jpg -resize x800 \) \( commodore-64.jpg -resize x800 \) \( game-boy.jpg -resize x800 \) +append \) \
  \( \( dreamcast.jpg -resize x800 \) \( playstation-2.jpg -resize x800 \) +append -gravity center -extent 2600x800 \) \
  -append -gravity center -background white -extent 2600x1800 slide-9-compact.jpg
```

### **Arc Layout** (Artistic)
Arrange systems in a gentle arc to suggest timeline progression. Requires more complex ImageMagick distortion.

### **Spotlight Layout** (Minimalist)
Show only 3 key systems:
- Atari 2600 ("Dawn")
- Commodore 64 ("Your story")
- PlayStation 2 ("PS2 era")

Command:
```bash
magick \( atari-2600.jpg -resize x1000 \) \
  \( commodore-64.jpg -resize x1000 \) \
  \( playstation-2.jpg -resize x1000 \) \
  +append -background white -gravity center -extent 5000x1200 slide-9-spotlight.jpg
```

---

## Next Steps

1. ✅ **Images are ready** - All files prepared and available
2. ⏳ **Open presentation** - Load the updated PPTX
3. ⏳ **Insert Slide 9 image** - Systems montage
4. ⏳ **Insert Slide 27 image** - Lesson screenshot
5. ⏳ **Review and adjust** - Resize/position as needed
6. ⏳ **Save as new version** - Keep original as backup

---

## Troubleshooting

### **Images look pixelated**
- All images are high-resolution (2720×2600 or larger)
- PowerPoint/Keynote may preview at lower quality
- Export to PDF to verify final quality

### **File size too large**
- Compress montage with `-quality 80` or `-quality 70`
- Consider using fewer systems (3 instead of 5)
- Convert to optimized PNG: `magick input.jpg -strip output.png`

### **Images clash with design**
- All images have neutral backgrounds (white/gray)
- Can add border matching your colors:
  ```bash
  magick slide-9-systems-montage.jpg -bordercolor "#5D5B7A" -border 10 slide-9-bordered.jpg
  ```

### **Aspect ratio doesn't fit slide**
- Current montage is 5:1 (very wide)
- Can adjust with `-extent` parameter
- Or use 2-row layout (see alternative layouts above)

---

## Summary

**What's ready**:
- ✅ 5-system chronological montage (1977→2000)
- ✅ Lesson screenshot showing curriculum substance
- ✅ All individual system images (if you want alternatives)
- ✅ Public domain licensing (zero restrictions)

**What you need to do**:
1. Open presentation in PowerPoint or Keynote
2. Insert 2 images (Slide 9 and Slide 27)
3. Resize and position to taste
4. Save updated presentation

**Estimated time**: 5-10 minutes

The images are production-ready and will significantly strengthen your presentation's visual impact while maintaining your clean, professional design aesthetic.
