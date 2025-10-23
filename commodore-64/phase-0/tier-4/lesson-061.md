# Lesson 061: Optimisation Marathon

**Arc:** Complexity Limit - System Depth
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 180 lines

## Learning Objectives
- Apply every BASIC optimization technique
- Measure performance gains (~40% improvement)
- Confirm optimizations insufficient (still too slow)
- Document optimization ceiling

## Key Concepts
- **Integer Variables:** I%=5 faster than I=5
- **Computed GOTO:** ON X GOTO faster than IF chains
- **Variable Caching:** Store PEEK results
- **Loop Reduction:** Minimize FOR/NEXT
- **Line Number Optimization:** Lower numbers = faster lookup
- **Result:** 40% faster, still 6× too slow

## Code Pattern
```basic
10 REM Optimized version (all techniques)
20 REM Integer variables (%)
30 FC%=0:FPS%=0:PX%=160:PY%=220
40 REM Cached registers
50 J%=0:R%=0:REM Joystick, raster
60 REM Main loop (lowest line numbers for speed)
70 FC%=FC%+1
80 REM Cache PEEK values
90 J%=PEEK(56320):R%=PEEK(53266)
100 REM Computed GOTO instead of IF chains
110 ON ((J% AND 4)=0)+1 GOTO 120,130
120 PX%=PX%-3:REM Left
130 ON ((J% AND 8)=0)+1 GOTO 140,150
140 PX%=PX%+3:REM Right
150 REM Integer math only
160 EX%=EX%+2:EY%=EY%+1
170 REM Optimized collision (early exit)
180 DX%=ABS(EX%-PX%):IF DX%>20 THEN 200
190 DY%=ABS(EY%-PY%):IF DY%>18 THEN 200
195 GOSUB 1000:REM Hit
200 REM ... continue
```

## Performance Measurement
**Optimization Results:**
```
Before optimization: 5-6 fps
After all optimizations: 7-9 fps
Improvement: ~40% faster
Target: 50-60 fps
Gap: Still 6-7× too slow
```

## Optimization Techniques Applied
1. Integer variables (I% vs I): ~15% faster
2. Computed GOTO: ~10% faster
3. PEEK caching: ~8% faster
4. Loop reduction: ~5% faster
5. Line number optimization: ~2% faster
**Combined: ~40% improvement**

## Limit Confirmed
**Optimizations Help But Don't Solve Problem**

"Every optimization technique applied: **40% faster (7-9 fps from 5-6 fps).**

But we need 50-60 fps. Still **6-7× too slow.**

**Why optimizations insufficient:**
- Integer math: 15% faster, but still interpreted
- Cached PEEKs: Saves lookups, but still parsed
- Computed GOTO: Faster branches, but still line-number lookup

**Root problem:** 70-80% of CPU time is interpreter overhead. Optimizing the 20-30% actual logic gives 40% overall gain. **Not enough.**

**Assembly removes the 70-80% interpreter overhead** → 5-7× speedup achievable."

## Quick Reference
**Optimization Techniques:**
```
1. Integer variables: A%=5 (16-bit) vs A=5 (float)
2. ON GOTO: ON X GOTO 100,200,300
3. PEEK caching: J=PEEK(56320) once per frame
4. Early exit: Check cheap conditions first
5. Low line numbers: Faster lookup
```

**Performance Note:**
"All optimizations applied yield **40% improvement** (5-6 → 7-9 fps). Still **6-7× slower than needed**. Interpreter overhead (70-80% CPU time) is the bottleneck. **Optimizations polish the 20-30% logic** but can't eliminate interpreter."
