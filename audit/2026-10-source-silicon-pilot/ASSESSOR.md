# Assessor notes: source and translation

Keep this separate from the learner tasks. All actual learner outcomes remain
**not observed**. The automated checks below are technical evidence only.

1. Codes 1,1,2,3; displayed result 4. Character codes describe source letters;
   the invented machine expects its own code 1 for INC.
2. Pending progresses [1], [1], [1,2], [1,2,3]. Found is TRUE, FALSE, TRUE,
   TRUE. Valid becomes FALSE at MYSTERY and stays FALSE. Diagnostics name the
   unknown instruction and the failed translation; no program codes are emitted.
3. Every unknown-name case is rejected, including repeats. Empty input is valid
   and emits nothing. Consult diagnostics/validity, not output length alone.
4. New codes 1,2,1,3 show 3. Old codes still show 4. Correct the source, translate
   successfully and hand the resulting codes to the model machine. A failed
   build does not prove that an older output file has been replaced.
5. Accept any program whose two traces agree and whose two shown values differ.
   For example INC, SHOW, DOUBLE, SHOW emits 1,3,2,3 and shows 1 then 2.
6. A snapshot can expose stored tokens and instruction bytes. It does not by
   itself show every instruction fetched or quantify interpreter overhead.
7. Both averages are 10ms. A misses once; B misses none in these four invented
   observations. Further workloads and correctness checks are required.

An optional diagnosis answer should use board-state evidence to test the rule
and rendering evidence to test the picture, without treating either as proof of
both. No new controlled timing comparison is part of this pilot.
