# Tier 2: Building - Detailed Lesson Breakdown

**Overview:** Sprite-based games, deeper hardware understanding, experiencing BASIC's speed limits naturally
**Lessons:** 17-32 (16 lessons)
**End Goal:** Complete sprite-based action game demonstrating VIC-II sprite system, joystick control, collision detection, and game state management
**Key Learning:** Students build real sprite games while naturally encountering BASIC's performance ceiling

---

## Section 1: Sprites Introduced (Lessons 17-22)

### Lesson 17: Hardware Sprites

**Learning Objectives:**
- Understand VIC-II hardware sprite system (8 sprites, 24×21 pixels)
- Differentiate between character graphics and sprite graphics
- Enable first sprite on screen

**Teaching Approach:**
- "Character graphics: good for static screens (like Tier 1)"
- "Sprites: hardware-accelerated moving objects (what you need for action games)"
- "VIC-II has 8 sprite channels - hardware does the drawing"

**Code Pattern (Example 1 - Single Sprite):**
```basic
10 rem enable sprite 0
20 poke 53248,100:poke 53249,100
30 poke 2040,13
40 poke 53269,1
50 get a$:if a$="" then 50
```

**Code Pattern (Example 2 - Sprite with Color):**
```basic
10 rem colored sprite
20 poke 53248,160:poke 53249,120
30 poke 2040,13
40 poke 53287,7:rem sprite 0 color = yellow
50 poke 53269,1:rem enable sprite 0
60 get a$:if a$="" then 60
```

**Hardware Details:**
- $D000/$D001 (53248/53249): Sprite 0 X/Y position
- $D015 (53269): Sprite enable register (bit 0 = sprite 0)
- $D027 (53287): Sprite 0 color
- 2040 (screen RAM + $3F8): Sprite 0 pointer

**Screenshot Requirements:**
- Single sprite visible on black screen
- Sprite positioned center-screen showing hardware rendering

**From the Vault:**
- VIC-II sprite system: Programmer's Reference Guide, pages 400-412
- Sprite positioning: Mapping the Commodore 64, pages 155-158

---

### Lesson 18: Sprite Shapes

**Learning Objectives:**
- Understand sprite data format (24×21 pixels, 63 bytes)
- Design sprite shapes using DATA statements
- Set sprite pointers to custom sprite data

**Teaching Approach:**
- "Default sprite 13 is just data at memory location 832"
- "You can design your own sprites as 63 bytes of data"
- "Each byte represents 8 pixels (1=on, 0=off)"

**Code Pattern (Example 1 - Simple Ship):**
```basic
10 rem custom sprite shape
20 for i=0 to 62:read d:poke 832+i,d:next
30 poke 2040,13:rem point to sprite data at 832
40 poke 53269,1:poke 53287,1
50 poke 53248,160:poke 53249,120
60 data 0,126,0,1,255,128,3,255,192
70 data 7,255,224,15,255,240,31,255,248
80 data ... (continues to 63 bytes)
```

**Code Pattern (Example 2 - Animated Character):**
```basic
10 rem two-frame animation
20 rem frame 1 at 832, frame 2 at 895
30 for i=0 to 62:read d:poke 832+i,d:next
40 for i=0 to 62:read d:poke 895+i,d:next
50 poke 2040,13:rem frame 1
60 poke 53269,1:poke 53287,7
70 poke 53248,160:poke 53249,120
80 data ... (frame 1)
90 data ... (frame 2)
```

**Sprite Design Grid:**
```
Each row = 3 bytes (24 bits/pixels)
21 rows total = 63 bytes
Plus 1 padding byte = 64 bytes per sprite

Example (spaceship nose):
00111100 = 60
01111110 = 126
11111111 = 255
```

**Screenshot Requirements:**
- Custom spaceship sprite
- Recognizable character sprite (showing pixel-perfect design)

**From the Vault:**
- Sprite data format: Programmer's Reference Guide, pages 405-407
- Sprite design tools: SpritePad reference (modern tool using same format)

---

### Lesson 19: Moving Sprites

**Learning Objectives:**
- Update sprite X/Y positions to create movement
- Understand X MSB (most significant bit) for positions > 255
- Create smooth sprite animation with simple loops

**Teaching Approach:**
- "Sprites move by changing their position registers"
- "$D000/$D001 control sprite 0 X and Y"
- "X position needs 9 bits (0-511), so bit 0 of $D010 extends it"

**Code Pattern (Example 1 - Horizontal Movement):**
```basic
10 rem moving sprite across screen
20 poke 2040,13:poke 53269,1:poke 53287,7
30 x=0:y=100
40 poke 53248,x:poke 53249,y
50 for i=1 to 5:next i:rem delay
60 x=x+1:if x>255 then poke 53264,1:rem set MSB
70 if x>320 then x=0:poke 53264,0:rem clear MSB
80 goto 40
```

**Code Pattern (Example 2 - Circular Motion):**
```basic
10 rem circular sprite motion
20 poke 2040,13:poke 53269,1:poke 53287,14
30 a=0
40 x=160+cos(a)*80:y=120+sin(a)*80
50 poke 53248,x:poke 53249,y
60 for i=1 to 10:next i
70 a=a+0.1:if a>6.28 then a=0
80 goto 40
```

**Hardware Details:**
- $D000-$D00F (53248-53263): X/Y positions for sprites 0-7
- $D010 (53264): X MSB for all 8 sprites (bit 0 = sprite 0 MSB, etc.)
- Screen coordinates: X (0-511), Y (0-255 visible region)

**Screenshot Requirements:**
- Sprite at far right of screen (showing X > 255 handling)
- Motion blur effect from continuous movement

**From the Vault:**
- Sprite positioning: Programmer's Reference Guide, pages 402-403
- MSB handling: Mapping the Commodore 64, page 156

---

### Lesson 20: Multiple Sprites

**Learning Objectives:**
- Enable and manage 2-4 sprites simultaneously
- Set individual sprite colors
- Understand sprite register offsets for multiple sprites

**Teaching Approach:**
- "Each sprite has its own X/Y registers, 2 bytes apart"
- "Sprite 0: $D000/$D001, Sprite 1: $D002/$D003, etc."
- "Enable register $D015 uses bits for each sprite"

**Code Pattern (Example 1 - Four Corner Sprites):**
```basic
10 rem four sprites at screen corners
20 for i=0 to 3:poke 2040+i,13:next:rem all use sprite 13
30 poke 53269,15:rem enable sprites 0-3 (bits 0-3)
40 rem sprite 0: top-left
50 poke 53248,24:poke 53249,50
60 rem sprite 1: top-right
70 poke 53250,255:poke 53251,50:poke 53264,2
80 rem sprite 2: bottom-left
90 poke 53252,24:poke 53253,229
100 rem sprite 3: bottom-right
110 poke 53254,255:poke 53255,229:poke 53264,poke(53264) or 8
120 for i=0 to 3:poke 53287+i,i+1:next:rem colors
130 get a$:if a$="" then 130
```

**Code Pattern (Example 2 - Formation Flying):**
```basic
10 rem three sprites in formation
20 for i=0 to 2:poke 2040+i,13:next
30 poke 53269,7:rem enable sprites 0-2
40 x=50:y=100
50 poke 53248,x:poke 53249,y:rem leader
60 poke 53250,x-20:poke 53251,y+15:rem left wing
70 poke 53252,x+20:poke 53253,y+15:rem right wing
80 for i=0 to 2:poke 53287+i,7:next
90 for i=1 to 5:next i
100 x=x+1:if x>255 then poke 53264,1
110 if x>320 then x=0:poke 53264,0
120 goto 50
```

**Hardware Details:**
- Sprite enable ($D015): Bit 0=sprite 0, bit 1=sprite 1, etc.
- Sprite colors ($D027-$D02E): Individual color per sprite
- Memory pointers (2040-2047): Can point to different sprite shapes

**Screenshot Requirements:**
- Four sprites visible simultaneously in different colors
- Formation of 3 sprites showing coordinated movement

**From the Vault:**
- Multiple sprite management: Programmer's Reference Guide, pages 408-410
- Sprite color registers: Mapping the Commodore 64, pages 157-158

---

### Lesson 21: Sprite Collision

**Learning Objectives:**
- Read hardware collision registers
- Detect sprite-sprite collisions
- Detect sprite-background collisions
- Clear collision latches

**Teaching Approach:**
- "VIC-II detects collisions in hardware - you just read the result"
- "$D01E tells you which sprites hit each other"
- "$D01F tells you which sprites hit background graphics"
- "Reading the register clears it (latch mechanism)"

**Code Pattern (Example 1 - Two Sprite Collision):**
```basic
10 rem sprite collision test
20 poke 2040,13:poke 2041,13
30 poke 53269,3:rem enable sprites 0-1
40 x0=50:x1=200:y=100
50 poke 53248,x0:poke 53249,y:poke 53287,7
60 poke 53250,x1:poke 53251,y:poke 53288,2
70 x0=x0+1:x1=x1-1
80 poke 53248,x0:poke 53250,x1
90 c=peek(53278):rem read collision register
100 if c>0 then print "collision!":end
110 for i=1 to 5:next i
120 goto 70
```

**Code Pattern (Example 2 - Background Collision):**
```basic
10 rem sprite hits screen character
20 poke 2040,13:poke 53269,1:poke 53287,7
30 rem draw wall on screen
40 for i=1024 to 1024+39:poke i,160:poke 55296+i,1:next
50 x=0:y=50
60 poke 53248,x:poke 53249,y
70 x=x+1:if x>255 then poke 53264,1
80 poke 53248,x
90 c=peek(53279):rem sprite-background collision
100 if c and 1 then print "hit wall!":end
110 for i=1 to 3:next i
120 goto 70
```

**Hardware Details:**
- $D01E (53278): Sprite-sprite collision (bit per sprite)
- $D01F (53279): Sprite-background collision (bit per sprite)
- Reading register clears latch
- Collision detection happens automatically every frame

**Screenshot Requirements:**
- Two sprites colliding with collision message
- Sprite hitting screen character boundary

**From the Vault:**
- Collision registers: Programmer's Reference Guide, pages 413-414
- Collision timing: Mapping the Commodore 64, page 159

---

### Lesson 22: Sprite Animation

**Learning Objectives:**
- Switch sprite pointers to create animation frames
- Time animation with TI clock or delay loops
- Create walking/flying animation cycles

**Teaching Approach:**
- "Animation = switching between different sprite shapes"
- "Each frame is a separate 63-byte sprite definition"
- "Sprite pointers at 2040-2047 control which shape displays"

**Code Pattern (Example 1 - Two-Frame Walk):**
```basic
10 rem walking animation
20 rem load frame 1 at block 13 (832)
30 for i=0 to 62:read d:poke 832+i,d:next
40 rem load frame 2 at block 14 (896)
50 for i=0 to 62:read d:poke 896+i,d:next
60 poke 53269,1:poke 53287,7
70 x=50:y=100:f=13
80 poke 2040,f:poke 53248,x:poke 53249,y
90 for i=1 to 10:next i:rem animation delay
100 x=x+1:f=13+(f=13):rem toggle 13/14
110 if x>200 then x=50
120 goto 80
130 data ... (frame 1 - left foot forward)
140 data ... (frame 2 - right foot forward)
```

**Code Pattern (Example 2 - Four-Frame Rotation):**
```basic
10 rem rotating sprite (4 frames)
20 for b=13 to 16
30   for i=0 to 62:read d:poke b*64+i,d:next
40 next b
50 poke 53269,1:poke 53287,14
60 x=160:y=120:f=13:la=ti
70 if ti-la<5 then 70:rem wait 1/12 second
80 la=ti:f=f+1:if f>16 then f=13
90 poke 2040,f
100 goto 70
110 data ... (frame 1 - facing up)
120 data ... (frame 2 - facing right)
130 data ... (frame 3 - facing down)
140 data ... (frame 4 - facing left)
```

**Animation Timing:**
- Delay loops: Simple but blocks execution
- TI clock: Non-blocking, allows input during animation
- Frame rate: 10-20 frames/second typical for BASIC

**Screenshot Requirements:**
- Mid-animation frame showing character motion
- Four-frame rotation sequence composite

**From the Vault:**
- Sprite pointers: Programmer's Reference Guide, page 406
- Animation techniques: _Creative Computing_ Sprite Animation article (1984)

---

## Section 2: Sound Deepened (Lessons 23-25)

### Lesson 23: SID Voices

**Learning Objectives:**
- Understand three independent voices
- Program multiple voices simultaneously
- Calculate frequency values for notes

**Teaching Approach:**
- "SID has 3 voices: Voice 1 ($D400), Voice 2 ($D407), Voice 3 ($D40E)"
- "Each voice: independent frequency, waveform, envelope"
- "Chords = programming 3 voices with related frequencies"

**Code Pattern (Example 1 - Three-Note Chord):**
```basic
10 rem c major chord (c-e-g)
20 poke 54296,15:rem volume max
30 rem voice 1: c note (frequency 4291)
40 poke 54272,195:poke 54273,16
50 poke 54277,0:poke 54278,240
60 poke 54276,17:rem gate on, triangle wave
70 rem voice 2: e note (frequency 5423)
80 poke 54279,47:poke 54280,21
90 poke 54284,0:poke 54285,240
100 poke 54283,17:rem gate on, triangle wave
110 rem voice 3: g note (frequency 6436)
120 poke 54286,36:poke 54287,25
130 poke 54291,0:poke 54292,240
140 poke 54290,17:rem gate on, triangle wave
150 get a$:if a$="" then 150
160 poke 54276,16:poke 54283,16:poke 54290,16:rem gates off
```

**Code Pattern (Example 2 - Arpeggio):**
```basic
10 rem arpeggiated chord
20 poke 54296,15:poke 54277,0:poke 54278,240
30 data 4291,5423,6436:rem c,e,g frequencies
40 for i=1 to 10:rem repeat 10 times
50   for j=1 to 3:rem each note
60     read f:poke 54272,f and 255:poke 54273,f/256
70     poke 54276,17:rem gate on
80     for t=1 to 50:next t:rem note duration
90     poke 54276,16:rem gate off
100   next j
110   restore:rem reset data pointer
120 next i
```

**Note Frequency Table (PAL):**
| Note | Frequency | Low Byte | High Byte |
|------|-----------|----------|-----------|
| C-3  | 4291      | 195      | 16        |
| E-3  | 5423      | 47       | 21        |
| G-3  | 6436      | 36       | 25        |
| C-4  | 8581      | 133      | 33        |

**Hardware Details:**
- Voice 1: $D400-$D406 (54272-54278)
- Voice 2: $D407-$D40D (54279-54285)
- Voice 3: $D40E-$D414 (54286-54292)

**From the Vault:**
- SID chip architecture: Programmer's Reference Guide, pages 454-467
- Frequency calculation: SID chip datasheet (MOS Technology)

---

### Lesson 24: ADSR Mastery

**Learning Objectives:**
- Control Attack, Decay, Sustain, Release envelopes
- Shape different instrument sounds
- Understand envelope timing

**Teaching Approach:**
- "ADSR controls volume over time - how notes begin and end"
- "Attack: 0-15 (faster to slower rise)"
- "Decay/Release: 0-15 (faster to slower fall)"
- "Sustain: 0-15 (volume level to hold)"

**Code Pattern (Example 1 - Piano vs Organ):**
```basic
10 rem piano sound (quick attack, decay)
20 poke 54296,15:poke 54272,133:poke 54273,33
30 poke 54277,2:poke 54278,9:rem a=0,d=2,s=0,r=9
40 poke 54276,17:for i=1 to 100:next:poke 54276,16
50 for i=1 to 200:next i
60 rem organ sound (slow attack, sustain)
70 poke 54277,9:poke 54278,244:rem a=9,d=0,s=15,r=4
80 poke 54276,17:for i=1 to 200:next:poke 54276,16
```

**Code Pattern (Example 2 - Sound Effects Library):**
```basic
10 rem sound effect: explosion
20 poke 54296,15:poke 54272,50:poke 54273,0
30 poke 54277,9:poke 54278,0:rem fast attack, instant decay
40 poke 54276,129:rem gate on, noise waveform
50 for i=1 to 50:next i:poke 54276,128
60 end
100 rem sound effect: laser
110 poke 54296,15:poke 54277,0:poke 54278,240
120 f=200:for i=1 to 100
130   poke 54272,f and 255:poke 54273,f/256
140   poke 54276,33:rem sawtooth wave
150   f=f-2:next i
160 poke 54276,32:rem gate off
```

**ADSR Register Format:**
- Attack/Decay: High nibble = attack (0-15), low nibble = decay (0-15)
- Sustain/Release: High nibble = sustain (0-15), low nibble = release (0-15)

**From the Vault:**
- ADSR envelopes: Programmer's Reference Guide, pages 460-462
- Sound synthesis: _Compute!'s Gazette_ SID Programming series (1983-84)

---

### Lesson 25: Simple Music

**Learning Objectives:**
- Sequence notes to create melodies
- Time note durations with TI clock
- Loop background music

**Teaching Approach:**
- "Music = data (notes + durations) + playback loop"
- "DATA statements: note frequency, duration in jiffies"
- "TI timing allows music during gameplay (preview for Tier 2 synthesis)"

**Code Pattern (Example 1 - Simple Melody):**
```basic
10 rem mary had a little lamb
20 poke 54296,15:poke 54277,9:poke 54278,240
30 data 8581,30,7650,30,6811,30,7650,30
40 data 8581,30,8581,30,8581,60,0,30
50 read f,d:if f=0 then 90
60 poke 54272,f and 255:poke 54273,f/256
70 poke 54276,17:la=ti
80 if ti-la<d then 80
90 poke 54276,16:goto 50
```

**Code Pattern (Example 2 - Background Music Loop):**
```basic
10 rem background music + sprite movement
20 poke 54296,15:poke 54277,9:poke 54278,240
30 data 4291,20,5423,20,6436,20,8581,40,-1,0
40 poke 2040,13:poke 53269,1:poke 53287,7
50 x=0:y=100:mi=1:read mf,md:la=ti
60 rem main loop
70 get a$:if a$="a" then x=x-1
80 if a$="d" then x=x+1
90 poke 53248,x:poke 53249,y
100 rem music timing
110 if ti-la<md then 70
120 poke 54276,16:la=ti:read mf,md
130 if mf<0 then restore:read mf,md
140 poke 54272,mf and 255:poke 54273,mf/256
150 poke 54276,17
160 goto 70
```

**Music Data Format:**
```
DATA frequency, duration_in_jiffies
DATA -1, 0  (end marker, triggers RESTORE)
```

**From the Vault:**
- Music programming: _Compute!'s Gazette_ Music Synthesizer (1983)
- Note timing: Programmer's Reference Guide, page 456

---

## Section 3: Joystick Control (Lessons 26-28)

### Lesson 26: Reading the Joystick

**Learning Objectives:**
- Understand CIA chip joystick ports
- Read joystick state via PEEK(56320)
- Decode direction bits and fire button

**Teaching Approach:**
- "Joystick data comes from CIA chip, not VIC-II"
- "Port 2 (most common): PEEK(56320)"
- "Bits: up=0, down=1, left=2, right=3, fire=4"
- "Bit is 0 when pressed (active low logic)"

**Code Pattern (Example 1 - Joystick Tester):**
```basic
10 rem joystick test program
20 print chr$(147);"joystick tester - port 2"
30 j=peek(56320):rem read port 2
40 print chr$(19);:rem home cursor
50 if (j and 1)=0 then print "up    ";
60 if (j and 2)=0 then print "down  ";
70 if (j and 4)=0 then print "left  ";
80 if (j and 8)=0 then print "right ";
90 if (j and 16)=0 then print "fire  ";
100 print "     ":goto 30
```

**Code Pattern (Example 2 - Direction Decoder):**
```basic
10 rem decode all 8 directions
20 j=peek(56320):dx=0:dy=0
30 if (j and 1)=0 then dy=-1:rem up
40 if (j and 2)=0 then dy=1:rem down
50 if (j and 4)=0 then dx=-1:rem left
60 if (j and 8)=0 then dx=1:rem right
70 if dx<>0 or dy<>0 then gosub 200:rem movement
80 if (j and 16)=0 then gosub 300:rem fire
90 goto 20
200 rem movement handler
210 print "dx=";dx;" dy=";dy
220 return
300 rem fire handler
310 print "fire pressed!"
320 return
```

**Joystick Bit Map:**
```
Bit 0 (1):   Up
Bit 1 (2):   Down
Bit 2 (4):   Left
Bit 3 (8):   Right
Bit 4 (16):  Fire button
Bits 5-7:    Unused (always 1)

Value 127 (01111111): Up pressed
Value 111 (01101111): Up + fire pressed
```

**Hardware Details:**
- Port 1: PEEK(56321) - less common, conflicts with keyboard
- Port 2: PEEK(56320) - standard game port
- CIA-1 register $DC00/$DC01

**From the Vault:**
- Joystick interfacing: Programmer's Reference Guide, pages 345-347
- CIA chip: Mapping the Commodore 64, pages 168-170

---

### Lesson 27: Joystick Sprite Movement

**Learning Objectives:**
- Control sprite position with joystick
- Implement movement speed
- Add screen boundary checking

**Teaching Approach:**
- "Same movement logic as keyboard (Tier 1), different input source"
- "Joystick gives direction + magnitude (always max in BASIC)"
- "Boundaries prevent sprite from leaving screen"

**Code Pattern (Example 1 - Basic Joystick Control):**
```basic
10 rem joystick sprite control
20 poke 2040,13:poke 53269,1:poke 53287,7
30 x=160:y=100
40 poke 53248,x:poke 53249,y
50 j=peek(56320)
60 if (j and 1)=0 and y>50 then y=y-2
70 if (j and 2)=0 and y<229 then y=y+2
80 if (j and 4)=0 and x>24 then x=x-2
90 if (j and 8)=0 and x<320 then x=x+2
100 if x>255 then poke 53264,1 else poke 53264,0
110 for i=1 to 3:next i:rem movement speed
120 goto 40
```

**Code Pattern (Example 2 - Variable Speed):**
```basic
10 rem variable speed movement
20 poke 2040,13:poke 53269,1:poke 53287,7
30 x=160:y=100:sp=1
40 poke 53248,x:poke 53249,y
50 j=peek(56320)
60 if (j and 16)=0 then sp=3 else sp=1:rem fire for speed boost
70 if (j and 1)=0 and y>50 then y=y-sp
80 if (j and 2)=0 and y<229 then y=y+sp
90 if (j and 4)=0 and x>24 then x=x-sp
100 if (j and 8)=0 and x<320 then x=x+sp
110 if x>255 then poke 53264,1 else poke 53264,0
120 for i=1 to 2:next i
130 goto 40
```

**Boundary Constants:**
```
X: 24 (left edge) to 344 (right edge, requires MSB)
Y: 50 (top edge) to 229 (bottom edge)
Safe visible: X=24-320, Y=50-229
```

**From the Vault:**
- Sprite control: _Your Commodore_ joystick sprite tutorial (1984)
- Screen boundaries: VIC-II visible region, Programmer's Reference Guide, page 401

---

### Lesson 28: Diagonal Movement

**Learning Objectives:**
- Handle simultaneous direction presses
- Implement smooth 8-way movement
- Understand velocity concepts

**Teaching Approach:**
- "Diagonal = both X and Y change simultaneously"
- "dx/dy velocity variables separate input from position update"
- "Smoother than checking each direction independently"

**Code Pattern (Example 1 - Eight-Way Movement):**
```basic
10 rem smooth 8-way joystick control
20 poke 2040,13:poke 53269,1:poke 53287,14
30 x=160:y=120
40 rem read joystick, calculate velocity
50 j=peek(56320):dx=0:dy=0
60 if (j and 1)=0 then dy=-2:rem up
70 if (j and 2)=0 then dy=2:rem down
80 if (j and 4)=0 then dx=-2:rem left
90 if (j and 8)=0 then dx=2:rem right
100 rem update position
110 x=x+dx:y=y+dy
120 rem boundary checks
130 if x<24 then x=24
140 if x>320 then x=320
150 if y<50 then y=50
160 if y>229 then y=229
170 rem update sprite
180 poke 53248,x:poke 53249,y
190 if x>255 then poke 53264,1 else poke 53264,0
200 for i=1 to 2:next i
210 goto 40
```

**Code Pattern (Example 2 - Normalized Diagonal Speed):**
```basic
10 rem diagonal speed compensation
20 poke 2040,13:poke 53269,1:poke 53287,7
30 x=160:y=120:sp=2
40 j=peek(56320):dx=0:dy=0
50 if (j and 1)=0 then dy=-1
60 if (j and 2)=0 then dy=1
70 if (j and 4)=0 then dx=-1
80 if (j and 8)=0 then dx=1
90 rem scale by speed (simple approximation)
100 if dx<>0 and dy<>0 then s=sp*0.7 else s=sp
110 x=x+dx*s:y=y+dy*s
120 rem boundaries and display
130 if x<24 then x=24
140 if x>320 then x=320
150 if y<50 then y=50
160 if y>229 then y=229
170 poke 53248,x:poke 53249,y
180 if x>255 then poke 53264,1 else poke 53264,0
190 for i=1 to 2:next i
200 goto 40
```

**Movement Patterns:**
```
Cardinal directions (4-way):
  Up:    dx=0,  dy=-1
  Down:  dx=0,  dy=1
  Left:  dx=-1, dy=0
  Right: dx=1,  dy=0

Diagonal directions (8-way):
  Up-Left:     dx=-1, dy=-1
  Up-Right:    dx=1,  dy=-1
  Down-Left:   dx=-1, dy=1
  Down-Right:  dx=1,  dy=1
```

**From the Vault:**
- Velocity-based movement: Game programming pattern, widely documented
- Diagonal speed normalization: sqrt(2) approximation for equal speeds

---

## Section 4: Game Systems (Lessons 29-31)

### Lesson 29: Score Display

**Learning Objectives:**
- Create fixed HUD area for score
- Convert numbers to PETSCII digits
- Update score without screen flicker

**Teaching Approach:**
- "HUD = heads-up display, stays on screen during gameplay"
- "Top or bottom row reserved for score/lives/etc"
- "Screen code arithmetic: digit 0-9 = value + 48"

**Code Pattern (Example 1 - Simple Score):**
```basic
10 rem score display at top of screen
20 print chr$(147):poke 53280,0:poke 53281,0
30 sc=0
40 rem draw score label
50 for i=0 to 4:read d:poke 1024+i,d:poke 55296+i,1:next
60 data 19,3,15,18,5:rem "score"
70 rem game loop
80 sc=sc+1:rem increment score
90 gosub 200:rem update score display
100 for i=1 to 30:next i:rem delay
110 if sc<999 then 80
120 end
200 rem display score subroutine
210 poke 1024+6,sc/100+48:rem hundreds
220 poke 1024+7,(sc mod 100)/10+48:rem tens
230 poke 1024+8,sc mod 10+48:rem ones
240 return
```

**Code Pattern (Example 2 - Zero-Padded Display):**
```basic
10 rem zero-padded 5-digit score
20 print chr$(147):poke 53280,0:poke 53281,0
30 sc=0:rem can go to 99999
40 rem draw hud
50 print "score: 00000"
60 poke 2040,13:poke 53269,1:poke 53287,7
70 x=160:y=120
80 rem game loop (joystick control + score)
90 j=peek(56320)
100 if (j and 16)=0 then sc=sc+10:gosub 300
110 rem sprite movement code...
120 goto 80
300 rem update zero-padded score
310 t=sc
320 for p=4 to 0 step -1
330   poke 1031+p,t mod 10+48
340   t=t/10
350 next p
360 return
```

**Screen Code Conversion:**
```
Numbers 0-9: Screen codes 48-57
Formula: screen_code = number + 48

Example:
Score = 234
Hundreds: 2 + 48 = 50 (screen code '2')
Tens:     3 + 48 = 51 (screen code '3')
Ones:     4 + 48 = 52 (screen code '4')
```

**From the Vault:**
- Screen codes: Programmer's Reference Guide, Appendix C
- HUD design: _Compute!'s Gazette_ game programming articles (1984-1986)

---

### Lesson 30: Lives System

**Learning Objectives:**
- Track player health/lives counter
- Display lives graphically (hearts or icons)
- Implement damage and game over conditions

**Teaching Approach:**
- "Lives = health you can see at a glance"
- "Graphical display: hearts (PETSCII character 83) or sprite icons"
- "Game over when lives reach zero"

**Code Pattern (Example 1 - Heart Display):**
```basic
10 rem lives display with hearts
20 print chr$(147):poke 53280,0:poke 53281,0
30 li=3:rem start with 3 lives
40 rem draw initial hearts
50 for i=0 to li-1:poke 1024+i,83:poke 55296+i,2:next
60 poke 2040,13:poke 53269,1:poke 53287,7
70 x=160:y=120
80 rem game loop
90 j=peek(56320)
100 rem sprite movement...
110 rem collision check (example)
120 if peek(53278)>0 then gosub 300:rem hit something
130 goto 80
300 rem take damage
310 li=li-1:if li<0 then li=0
320 rem redraw hearts
330 for i=0 to 2:poke 1024+i,32:next:rem clear
340 for i=0 to li-1:poke 1024+i,83:poke 55296+i,2:next
350 if li=0 then print chr$(147);"game over!":end
360 rem respawn delay
370 for i=1 to 60:next i
380 return
```

**Code Pattern (Example 2 - Numeric + Icon):**
```basic
10 rem lives: number + icon
20 print chr$(147):poke 53280,0:poke 53281,0
30 li=5:maxli=5
40 rem hud: "lives: 5/5 ♥♥♥♥♥"
50 print "lives:  /";maxli;" ";
60 gosub 200:rem update display
70 rem game loop
80 get a$:if a$="d" then gosub 300:rem debug: take damage
90 if a$="h" then gosub 400:rem debug: heal
100 goto 80
200 rem update lives display
210 poke 1031,li/10+48:poke 1032,li mod 10+48
220 for i=0 to maxli-1:poke 1040+i,32:next:rem clear icons
230 for i=0 to li-1:poke 1040+i,83:poke 55296+40+i,2:next
240 return
300 rem take damage
310 li=li-1:if li<0 then li=0
320 gosub 200
330 if li=0 then print chr$(147);"game over!":end
340 return
400 rem heal
410 li=li+1:if li>maxli then li=maxli
420 gosub 200
430 return
```

**Health Display Patterns:**
- Hearts: PETSCII 83 (♥)
- Boxes: PETSCII 160 (filled box) vs 32 (empty)
- Numeric: "3/5" format
- Combination: Icons + number

**From the Vault:**
- PETSCII graphics characters: Programmer's Reference Guide, Appendix F
- Game state management: _Compute!'s Gazette_ arcade game tutorials

---

### Lesson 31: Game States

**Learning Objectives:**
- Implement state machine pattern
- Handle title, play, and game over states
- Use ON...GOTO for state dispatch

**Teaching Approach:**
- "Games have modes: title screen, playing, game over"
- "STATE variable controls which code runs"
- "ON...GOTO dispatches to state handlers"

**Code Pattern (Example 1 - Three State Game):**
```basic
10 rem state machine game structure
20 st=0:rem 0=title, 1=play, 2=gameover
30 on st+1 goto 100,200,300
100 rem title state
110 print chr$(147);"    my game"
120 print:print "press fire to start"
130 if (peek(56320) and 16)=0 then st=1:goto 30
140 goto 30
200 rem play state
210 print chr$(147);"playing..."
220 poke 53280,0:poke 53281,0
230 sc=0:li=3
240 rem game loop
250 sc=sc+1:if sc>500 then st=2:goto 30
260 rem actual gameplay would go here...
270 for i=1 to 10:next i
280 goto 250
300 rem game over state
310 print chr$(147);"game over!"
320 print:print "score:";sc
330 print:print "press fire to restart"
340 if (peek(56320) and 16)=0 then st=0:goto 30
350 goto 30
```

**Code Pattern (Example 2 - State with Cleanup):**
```basic
10 rem state machine with proper transitions
20 st=0:pst=-1:rem current and previous state
30 if st<>pst then gosub 500:rem state change, initialize
40 pst=st
50 on st+1 goto 100,200,300
100 rem title state
110 print "title: press fire"
120 if (peek(56320) and 16)=0 then st=1
130 goto 30
200 rem play state
210 rem game logic here...
220 rem example: press 'q' to trigger game over
230 get a$:if a$="q" then st=2
240 goto 30
300 rem game over state
310 print "game over: press fire"
320 if (peek(56320) and 16)=0 then st=0
330 goto 30
500 rem state initialization
510 print chr$(147):rem clear screen on state change
520 on st+1 gosub 600,700,800
530 return
600 rem title init
610 poke 53280,6:poke 53281,14:rem light blue
620 return
700 rem play init
710 poke 53280,0:poke 53281,0:rem black
720 sc=0:li=3:rem reset game variables
730 return
800 rem game over init
810 poke 53280,2:poke 53281,8:rem red
820 return
```

**State Machine Pattern:**
```
State 0: Title Screen
  Input: Fire button
  Transition: → Play (state 1)

State 1: Playing
  Input: Gameplay, collisions
  Transition: → Game Over (state 2) on death

State 2: Game Over
  Input: Fire button
  Transition: → Title (state 0) to restart
```

**From the Vault:**
- State machines: Software engineering pattern, widely applicable
- ON...GOTO: BASIC Language Reference, Programmer's Reference Guide, page 157

---

## Lesson 32: SYNTHESIS - Sprite Action Game

**Title:** "Asteroid Runner" - Complete Sprite-Based Game

**Learning Objectives:**
- Combine all Tier 2 skills into complete game
- Experience BASIC's performance limits naturally
- Build shippable game demonstrating sprite mastery

**Game Specification:**
- Player sprite (joystick controlled spaceship)
- 3 enemy sprites (asteroids moving down screen)
- Hardware sprite collision detection
- Score display (points per asteroid dodged)
- Lives system (3 hearts)
- Sound effects (explosion on hit, beep on dodge)
- Title/Play/GameOver states
- Background music during gameplay

**Teaching Approach - The Honest Moment:**
- "Notice sprite movement isn't perfectly smooth"
- "Music sometimes stutters when collision happens"
- "You can only have 3-4 enemies before slowdown"
- "This is BASIC's speed limit - assembly removes it"
- "But you've proven the hardware works, learned the patterns"

**Code Structure (~100-120 lines):**
```basic
10 REM asteroid runner - tier 2 synthesis
20 REM state machine + sprites + joystick + collision + sound
30 st=0:rem 0=title,1=play,2=gameover

100 REM title state
110 print chr$(147);"  asteroid runner"
120 print:print "dodge the asteroids!"
130 print:print "joystick port 2"
140 print:print "press fire to start"
[...]

200 REM play state initialization
210 print chr$(147):poke 53280,0:poke 53281,0
220 sc=0:li=3
230 rem setup player sprite
240 for i=0 to 62:read d:poke 832+i,d:next
250 poke 2040,13:poke 53269,1:poke 53287,7
260 px=160:py=200
270 rem setup 3 asteroid sprites
280 for i=0 to 62:read d:poke 896+i,d:next
290 for i=1 to 3:poke 2040+i,14:next
300 poke 53269,15:rem enable sprites 0-3
[...]

400 REM main game loop
410 rem player movement (joystick)
420 j=peek(56320)
430 if (j and 4)=0 and px>24 then px=px-2
440 if (j and 8)=0 and px<320 then px=px+2
450 poke 53248,px:poke 53249,py
460 rem update asteroids (fall down)
470 for i=1 to 3
480   ay=peek(53249+i*2)+1
490   if ay>250 then ay=50:sc=sc+10:gosub 900:rem dodged!
500   poke 53249+i*2,ay
510 next i
520 rem collision check
530 c=peek(53278):if c>0 then gosub 1000:rem hit!
540 rem music update
550 gosub 1100
560 rem score display
570 gosub 1200
580 goto 410

900 REM dodge sound
910 poke 54296,15:poke 54272,200
920 poke 54276,17:for i=1 to 10:next:poke 54276,16
930 return

1000 REM collision handler
1010 li=li-1:rem lose life
1020 rem explosion sound
1030 poke 54296,15:poke 54276,129
1040 for i=1 to 30:next:poke 54276,128
1050 if li=0 then st=2:return:rem game over
1060 rem respawn
1070 for i=1 to 60:next i
1080 return

1100 REM background music
[simple note sequence with TI timing]
1110 return

1200 REM display HUD
1210 [score + lives hearts]
1220 return

2000 DATA ... (player sprite)
2010 DATA ... (asteroid sprite)
```

**Expected Student Experience:**
1. "Wow, I built a real sprite game!"
2. "The movement feels a bit sluggish compared to commercial games"
3. "When I add more asteroids, everything slows down"
4. "Music hiccups during collision detection"
5. → Natural desire for assembly language

**Screenshot Requirements:**
- Title screen with instructions
- Mid-game action (player + 3 asteroids)
- Game over screen with final score
- HUD showing score + lives clearly

**Challenge Extensions:**
- Add 4th asteroid (demonstrate slowdown)
- Try faster asteroid speeds (show BASIC struggling)
- Add power-ups (demonstrates data-driven design)

**Transition to Tier 3:**
- "You've built something real in BASIC"
- "Next tier: push even harder, understand exactly where BASIC hits its ceiling"
- "Tier 3 introduces techniques that show why assembly matters"

**From the Vault:**
- Complete game structure: _Compute!'s Gazette_ game series
- Performance considerations: _Commodore Power/Play_ optimization articles

---

## Tier 2 Summary

**What Students Built:**
- Understanding of VIC-II sprite system (8 sprites, 24×21 format)
- Complete sprite animation techniques
- Joystick input handling
- Multi-voice SID music programming
- Game state machines
- Complete playable action game

**What Students Experienced:**
- Natural performance limits of BASIC
- Sprite sluggishness with multiple objects
- Music timing challenges during gameplay
- Foundation for understanding why assembly matters

**Transition to Tier 3:**
Students now want to:
- Make sprites move faster
- Add more enemies without slowdown
- Implement smooth scrolling
- Perfect music timing
→ All require assembly language

**Next Steps:**
Tier 3 explicitly attempts advanced techniques (multiplexing, raster effects, scrolling) showing exactly where BASIC fails and previewing assembly solutions.

---

**Last Updated:** 2025-01-19
**Version:** 1.0 - Initial Tier 2 detailed breakdown
