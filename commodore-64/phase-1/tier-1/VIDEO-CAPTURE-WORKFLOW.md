# Audio Capture Workflow for Phase 1 Lessons

## Overview

Phase 1 lessons require audio demonstration of SID chip functionality. Audio can be captured automatically with VICE. Video is optional and can be added later if needed.

**Primary deliverable:** Audio-only WAV files demonstrating SID output

## Automated Audio Capture

VICE x64sc can automatically capture audio to WAV:

```bash
cd /path/to/lesson/code

x64sc -autostart example-1.prg \
      -limitcycles 5400000 \
      -sound \
      -soundrate 44100 \
      -soundrecdev wav \
      -soundrecarg /path/to/output.wav
```

**Parameters:**
- `-limitcycles 5400000` - ~90 seconds at 60Hz (adjust for desired duration)
- `-soundrate 44100` - 44.1kHz sample rate
- `-soundrecdev wav` - Output to WAV format
- `-soundrecarg <path>` - Output file path

**Result:** Audio-only WAV file with SID output

## Quick Capture Script

For efficient batch processing of all lessons:

```bash
#!/bin/bash
# capture-audio.sh <lesson-number>

LESSON=$1
CODE_DIR="/Users/stevehill/Projects/Code198x/code-samples/commodore-64/phase-1/tier-1/lesson-$(printf '%03d' $LESSON)"
OUTPUT_DIR="/Users/stevehill/Projects/Code198x/website/public/audio/commodore-64/phase-1/tier-1"

mkdir -p "$OUTPUT_DIR"

cd "$CODE_DIR"

# Capture example-1 (90 seconds)
x64sc -autostart example-1.prg \
      -limitcycles 5400000 \
      -sound \
      -soundrate 44100 \
      -soundrecdev wav \
      -soundrecarg "$OUTPUT_DIR/lesson-$(printf '%03d' $LESSON)-example-1.wav"

echo "Captured: lesson-$(printf '%03d' $LESSON)-example-1.wav"

# Capture example-2 if it exists (90 seconds)
if [ -f "example-2.prg" ]; then
    x64sc -autostart example-2.prg \
          -limitcycles 5400000 \
          -sound \
          -soundrate 44100 \
          -soundrecdev wav \
          -soundrecarg "$OUTPUT_DIR/lesson-$(printf '%03d' $LESSON)-example-2.wav"

    echo "Captured: lesson-$(printf '%03d' $LESSON)-example-2.wav"
fi
```

**Usage:**
```bash
chmod +x capture-audio.sh
./capture-audio.sh 1    # Captures lesson 001 audio
./capture-audio.sh 6    # Captures lesson 006 audio
```

## Manual Video Capture (Optional)

Video capture requires screen recording software due to VICE GUI limitations.

### macOS: QuickTime Player

1. **Start VICE with GUI:**
   ```bash
   x64sc -autostart example-1.prg -sound
   ```

2. **Start QuickTime Screen Recording:**
   - Open QuickTime Player
   - File → New Screen Recording
   - Click Options → set Microphone to "None" (we want SID audio, not mic)
   - Select recording area (just the VICE window)
   - Click Record button

3. **Demonstrate the lesson:**
   - Show C64 boot → READY prompt
   - Show program auto-loading
   - Let SID play for 15-20 seconds
   - Press RUN/STOP+RESTORE to exit
   - Total duration: 60-90 seconds

4. **Stop recording:**
   - Click Stop in menu bar
   - File → Save (to `/website/public/video/...`)

### macOS: ffmpeg with Screen Capture

```bash
# List available devices
ffmpeg -f avfoundation -list_devices true -i ""

# Capture screen + audio (device numbers may vary)
ffmpeg -f avfoundation \
       -i "1:0" \
       -t 90 \
       -c:v libx264 \
       -preset fast \
       -crf 23 \
       -c:a aac \
       -b:a 128k \
       output.mp4
```

### Linux: ffmpeg with X11

```bash
ffmpeg -video_size 720x568 \
       -framerate 60 \
       -f x11grab \
       -i :0.0+100,100 \
       -f pulse \
       -i default \
       -t 90 \
       output.mp4
```

### OBS Studio (All Platforms)

1. Add "Window Capture" source → select VICE window
2. Add "Audio Output Capture" → system audio
3. Start Recording
4. Run VICE demonstration
5. Stop Recording
6. File is saved to configured output directory

## Capture Scenario Checklist

Every Phase 1 lesson video should show:

- [ ] C64 boot screen (2-3 seconds)
- [ ] READY prompt
- [ ] Program loading (if applicable)
- [ ] READY after load
- [ ] RUN command (if applicable)
- [ ] Program execution showing SID output
- [ ] Audio playing clearly (15-20 seconds minimum)
- [ ] RUN/STOP+RESTORE to exit (if applicable)
- [ ] Return to READY prompt

**Total duration:** 60-90 seconds

## Post-Processing

### Trim Video

```bash
ffmpeg -i input.mp4 \
       -ss 00:00:02 \
       -t 00:01:30 \
       -c copy \
       output.mp4
```

### Add Text Overlays (Optional)

```bash
ffmpeg -i input.mp4 \
       -vf "drawtext=fontfile=/path/to/font.ttf:text='Lesson 001\: Your First Note':fontcolor=white:fontsize=24:x=10:y=10" \
       output.mp4
```

### Verify Audio Sync

```bash
ffprobe -v error \
        -select_streams a:0 \
        -show_entries stream=sample_rate,channels \
        -of default=noprint_wrappers=1 \
        output.mp4
```

Expected: `sample_rate=44100`, `channels=1` or `channels=2`

## File Naming Convention

**Audio files (primary):**
```
/website/public/audio/commodore-64/phase-1/tier-1/lesson-NNN-example-N.wav
```

Examples:
- `lesson-001-example-1.wav` (triangle wave)
- `lesson-001-example-2.wav` (sawtooth with ADSR)
- `lesson-002-example-1.wav`
- `lesson-006-example-1.wav`

**Video files (optional):**
```
/website/public/video/commodore-64/phase-1/tier-1/lesson-NNN-demonstration.mp4
```

## Quality Guidelines

**Video:**
- Resolution: 720x568 (native C64 display) or higher
- Frame rate: 60fps preferred (matches C64 output)
- Codec: H.264 (MP4 container)
- Bitrate: 2-5 Mbps (good quality without excessive file size)

**Audio:**
- Sample rate: 44.1kHz
- Codec: AAC or PCM
- Bitrate: 128-192 kbps
- Ensure SID output is clearly audible

**Duration:**
- Minimum: 60 seconds
- Target: 60-90 seconds
- Maximum: 120 seconds (keep lessons focused)

## Automation Script (Future Enhancement)

For complete automation, consider:
1. VICE monitor scripting to control playback
2. Xvfb (Linux) for headless X server
3. ffmpeg screen capture of virtual display
4. Combine with automated audio capture

This would enable fully scripted video generation but requires significant setup.

## Current Recommendation

**For Phase 1 Tier 1 lessons:**
- Use manual screen recording (QuickTime/OBS)
- Capture during lesson creation workflow
- Verify audio is clear and synchronized
- Total time: ~5-10 minutes per lesson video

This balances quality, effort, and workflow integration.
