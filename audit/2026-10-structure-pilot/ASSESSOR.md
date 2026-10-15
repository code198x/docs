# Structure: assessor notes

Keep answers separate from the learner sheet. Record the learner's original
prediction, explanation, trace and any hint before giving help. Every learner
outcome is **not observed**; technical checks do not supply learner results.

| Task | Expected evidence |
| --- | --- |
| 1 | Initially only 1 is valid; after append, 1 and 2. Zero remains invalid. Empty length is zero with no valid indices; the loop body displays nothing. Invalid access has no invented default value. |
| 2 | (1,1),(1,2),(1,3),(2,1),(2,2),(2,3), six lines. Exchanging the loops yields (1,1),(2,1),(1,2),(2,2),(1,3),(2,3) when each pair is written (row,column). The inner-loop quantity changes fastest; the count remains six. |
| 3 | All three change. A separate job or a parameter that distinguishes the particular call can meet the narrower request; accept a justified small design rather than one mandatory abstraction. |
| 4 | First call: caller n stays4; local4→8, returned8 stored in result. Second: local4→8, returned8 then assigned to caller n, which becomes8. Printing is an effect and does not provide the expression result required by assignment. |
| 5 | Broken final2 versus intended13. Replace assignment with total=total+price. Empty gives0; one item gives that item in both versions and therefore cannot distinguish them. The original case must pass after repair. |
| 6 | A valid contract accepts a number, returns input+3 and has no display/caller mutation. For example inputs0 and-4 return3 and-1. A trace must keep the original caller value separate from its result; other clear names and negative values are acceptable. |
| Optional BASIC | Calls at50/89 resume at60/92 respectively. GO SUB records a return point; ordinary variables remain shared. RETURN resumes execution and supplies no expression value. Do not infer that a named pseudocode parameter is a hardware register or BASIC local variable. |
| Optional debugger | Accept a specific recorded observation before the repair, such as the inspected comparison/branch or tracked value. Distinguish finding and explaining the observation from stepping a machine. |

The list tasks assume a fixed list size during iteration. The copied-parameter
task uses numbers; it does not define real-language list aliasing or deep-copy
rules. Separate unaided work, prompted correction and an observer-supplied answer.
No completion time, pass rate, retention or independent transfer has been measured.
