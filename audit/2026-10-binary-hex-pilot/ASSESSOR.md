# Binary and hex: assessor notes

Keep this separate from the learner prompts. Record the original prediction,
calculation, explanation and any hint before offering help. Every actual learner
outcome is **not observed**; technical evidence is not a learner result.

| Task | Evidence to look for |
| --- | --- |
| 1 | Places 128,64,32,16,8,4,2,1; selected64+16+8+2=90. Groups0101/1010 give hex 5A, and 5×16+10=90. |
| 2 | 64+16+8+4+1=93; binary 01011101, hex 5D. Check both the weighted bits and 5×16+13. |
| 3 | Group from the right: 0001 1011 gives hex 1B and decimal 27. Right-padding changed the value to 216. A leading zero preserves value; moving digits into higher places does not. |
| 4 | Hex 10=16 and hex 100=256. Only the first fits unsigned 0–255. Leading zeros change the numeral's width, not its value or a chosen field's capacity. No wrap/reject rule is inferred for an unspecified target. |
| 5 | All name one numeric value, five. None alone allocates storage or establishes how a real program stores it. Need a target, representation, chosen field and range rule. The switch drawing models a bit; it is not a measurement or universal circuit-current model. |
| 6 | Hex AA=binary 10101010=170, from hex A5=165. The high nibble 1010 is unchanged; low nibble changes 0101→1010. Difference+5 follows from low-nibble place values. |
| 7 | Accept any value in range with consistent conversions. Flipping position k changes the unsigned value by +2^k for 0→1 or -2^k for 1→0. An independent weighted sum and high×16+low check should agree; a repeated copied answer is insufficient. |
| Optional pixel lesson | % marks binary and $ marks hex in that assembler. A 1 selects ink and 0 selects paper for the described display. Explain that these are target syntax/display rules, not changes to numeric value. Reading, running and modifying are separate observations. |
| Optional wider value | Sixteen bits give 65536 patterns and unsigned maximum 65535; a numbered address range does not establish installed RAM. |

The answers use unsigned whole-number interpretation and explicitly chosen widths.
Do not treat “255 is the maximum” as a claim about every meaning of eight bits.
Distinguish unaided work, prompted correction and an observer-supplied solution.
No completion time, pass rate, retention or independent transfer has been measured.
