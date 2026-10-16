# Amiga unit-4 decisions and repetition

Both unit-4 lessons now have bounded prediction, change and debugging tasks. The Blitz parity exercise had a reproducible bug: with the default Quick type, `x/2*2=x` was true for every counter from 0 through 9. `x MOD 2` produced alternating remainders. The maintained listing also now waits before entering BLITZ mode, matching the qualified setup route.

Tracked by [website #773](https://github.com/code198x/website/issues/773), under [Amiga audit #116](https://github.com/stevehill1981/198x/issues/116). Source identities are in `source.json`; media/archive hashes are in `inputs.json`. No ROMs or runtime binaries are included.

## Native execution

`observations.json` records the named A1200 PAL configuration and the observed results. AMOS Professional 2.00 loaded the exact maintained `branch.amos` through Merge ASCII (right-Amiga+Shift+M), then ran with F1. Editing the assignment to 1, 0 and -1 selected the expected branches. The final lives line appeared in every case. At zero lives, changing `>0` to `>=0` ran successfully but selected the wrong branch. Restoring `>0` rejected zero and accepted one. A key ended `Wait Key`; Return dismissed the end requester.

AmiBlitz 3.13.0b compiled the retained `.ab3` files through its CLI, with `RuntimeDebug = 0`, then ran each standalone executable. `parity.txt` is actual guest output, not a host-language simulation. The graphical baseline showed ten bars with only the sixth purple. The MOD variant alternated purple and pink. Moving the colour reset outside the loop made the sixth through tenth bars purple. Recompiling and rerunning the baseline restored the single purple bar. All four retained compilation logs report zero errors. This qualifies these program results; it does not repeat the earlier PED editor qualification.

The `.ab3` header is followed by the maintained sample verbatim in `bars.ab3`. `stripes.ab3` changes only the If expression. `colourbug.ab3` moves only the colour reset. The capture JSON has the exact maintained sample payload, but its older editor-control sequence is not a newly qualified PED automation route.

## Delivery checks

The production build passed (2,459 pages), using the changed code-samples checkout. `npm run check:content` passed (25,972 Vault references). `verify.py` checked source hashes, capture payload equality, native output, generated questions and local Amiga links. Its intentionally reversed wait-order fixture was rejected. Run without Python optimisation, since the verifier uses assertions:

```sh
python3 audit/2026-10-amiga-decisions/verify.py --website /path/to/website --samples /path/to/code-samples
```

Native Chrome review used the local production build at 390×844 and 1440×900. Both lessons were styled and readable, code blocks stayed within their containers, and the new explanation disclosures worked. The Blitz parity disclosure also toggled with Return. Dimensions are responsive emulation, not a physical phone test.

## Limits and setup failures

No learner trial, VoiceOver check or performance benchmark was performed. The new timing wording is a sourced explanation, not a measured frame-rate claim. These two pages do not clear every outstanding first-session check in #766/#767.

The first sandboxed emulator launch aborted before a configured test window. A later Workbench command was truncated by fast synthetic input and returned object-not-found (return code 10); no compiler result is claimed for it. Short command aliases and checking the complete command before Return allowed the recorded runs. Two attempted host key combinations produced the wrong guest character during the boundary edit; they were removed before execution, then literal text input produced the inspected `>=0` condition.

The LHA extractor exited 1 on an accented catalogue-folder name (`fran?ais`). The compiler and required core files were present, their identities checked, and the retained programs actually compiled and ran; full archive extraction is not claimed. The first local HTTP port was occupied (`OSError: [Errno 48] Address already in use`); a task-owned server used an allocated port instead. An artifact check started during the final rebuild failed with `AssertionError: /systems/commodore-amiga/amos/meet-amos` because that route had not yet been emitted. It passed after the build completed; verification is sequenced after generation. Build warnings concerned existing large chunks and deprecated Pagefind UI; no dependencies changed.

Primary references: the [pinned AmiBlitz guide](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Docs/Amiblitz3.guide), sections 2.2.1 and 3.1.5, and the [Blitz BASIC 2.1 manual](https://daemonbite.com/files/linked/BB21Manual.pdf), printed pages 47 and 98 (PDF pages 58 and 109). The official AMOS repository was pinned at `533b4b1f5acd604814513f78e02c7b4796cb0531`.
