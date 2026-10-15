# Working It Out: assessor notes

Keep this separate from the learner sheet. Let the learner predict before
showing an answer. Record their words, trace, mistakes and hints. Technical
checks below are not learner observations; every learner outcome is **not observed**.

| Task | Evidence to look for |
| --- | --- |
| 1 | 12 versus 3; 9 versus 15. Equal-priority multiplication/division and addition/subtraction work left to right in this notation; brackets change grouping. |
| 2 | 4 → 10 → 16. Resetting to 4 before the second update gives 10 instead. The right-hand side reads the current value before assignment. |
| 3 | Naive trace ends a=8, b=12, c=8. Old a=3 was lost. Save old a before changing it, then assign a=b, b=c, c=spare, giving 8,12,3. A different correct trace-preserving repair is acceptable. |
| 4 | 3.25, 3, 1 and 3. Complete rows use floor, not nearest as a general rule. 3×4+1=13 accounts for every tile; nearest happens to match here. Ask for a total where they differ, such as 15. |
| 5 | (q,r) pairs (0,0), (0,3), (1,0), (1,1). Each satisfies 4q+r=n and 0≤r<4. Zero group size is undefined; reject it before division. Floor(-4.5)=-5; dropping the fraction gives -4 and moves upwards. |
| 6 | Testing equality produces a truth value, not the column. Use the remainder itself: 18 remainder16=2; 16 remainder16=0. This introductory contract has not defined negative remainder inputs; a negative-coordinate convention must be chosen before use. |
| 7 | Example length7 leaves17 spare: floor(17/2)=8 left,9 right. To put the extra on the left use 17-floor(17/2)=9, or another justified ceiling calculation. State whole text lengths 0–24 and an explicit overlong-text policy; any consistent choice with a trace is acceptable. |
| Optional BASIC | INT applies to the scaled non-negative random value, then +1 shifts 0–9 to 1–10. Do not imply removing brackets or moving +1 always changes a mathematically equivalent bounded expression; ask the learner to explain the operation sequence and range. |
| Optional Pattern | The illustrative listing falls back to column zero for full-width/overlong text. The Pattern carries its own code-status limit; following the link is not proof that its assembly ran. |

Distinguish a correct number from an explanation of why it follows. Record
independent work, a prompted correction and an observer-supplied answer separately.
No pass rate, completion time, retention or unaided transfer has been measured.
