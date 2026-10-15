# Gates and the Adder: assessor notes

Keep answers separate from prompts. Record the learner's first prediction,
trace, explanation and hints before helping. All learner outcomes remain
**not observed**; native/browser checks are not educational validation.

| Task | Expected evidence |
| --- | --- |
| 1 | In order 00,01,10,11: AND 0,0,0,1; OR 0,1,1,1; XOR 0,1,1,0. Row11 distinguishes OR/XOR. NOT0=1 and NOT1=0. Keyboard input states, numeric outputs and row highlights should agree; distinguish prediction from observation. |
| 2 | SUM0,CARRY1 represents 0+2×1=2. OR-for-SUM fails at11, giving sum1/carry1, i.e.3. Any other half-adder input pair hides that particular fault. |
| 3 | Outputs (SUM,COUT) for 000,001,010,011,100,101,110,111: (0,0),(1,0),(1,0),(0,1),(1,0),(0,1),(0,1),(1,1). Maximum total3 needs two bits, not a discarded carry. |
| 4 | Bit0:1+1+0→sum0,carry1; bit1:0+1+1→sum0,carry1; bit2:1+0+1→sum0,carry1. Full result1000=8; low three bits000 with final carry1. Starting carry is an assumption, not a missing input forgotten by arithmetic. |
| 5 | At bit1,0+0+1→sum1,carry0; bit2 stays sum0,carry0. The faulty result is010. The fault changes one higher sum bit but does not propagate a carry beyond it. |
| 6 | A truth table names settled logical results. It does not measure physical voltage/timing conditions. A timing claim needs a named part/configuration, an input change and actual time observations under stated conditions; a browser toggle is not that measurement. |
| 7 | Accept any clear consistent policy with whole inputs0–3. Example1+1=2 gives low10/carry0; 3+1=4 gives low00/carry1. Check low+4×carry=full sum. Saving or displaying the carry preserves the wider result; silently keeping low bits is a different stated policy. No target overflow behaviour is invented. |
| Optional signed comparison | 127+1 can have signed overflow without carry; 5+251 has carry but represents +5 plus−5 under signed interpretation. Do not equate final unsigned carry with every sort of overflow. |
| Optional assembly | The complete first program changes the border colour through a port output. Reading, prediction, running and modification are separate observations. |

The worked ripple uses fixed width and starting carry zero. The schematic is a
static wiring overview, not a complete physical implementation or timed simulation.
A count of logical gate instances is not a universal transistor/cost measurement.
No completion time, pass rate, retention or unaided transfer has been measured.
