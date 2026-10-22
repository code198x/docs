# Amiga opening claims: bounded corrections

The proposed opening lessons explain numeric storage and OS access without
ranking languages by unsupported speed or safety claims. The graphics sample
also moves its disk-settling wait before `BLITZ`. These changes are ready for
source review; fresh runtime and desktop/phone visual checks remain blocked.
This is work on [website #767](https://github.com/code198x/website/issues/767)
under umbrella #116.

## Scope and evidence

We read both module introductions and units 1–3 at website
`e98bcf78e5dd359d4b4a0bf7698efec663a5905a`. Five pages need edits; AMOS’s
introduction and both first lessons remain unchanged. The previous merged
[first-greeting qualification](../2026-10-amiga-greetings/REPORT.md) establishes
only its named greetings, edits and error recovery. It does not qualify these
later numeric or graphics examples.

[Source identities](source.json) record the website/sample baselines and exact
changed-file hashes. The [plan](../../plans/2026-10-16-amiga-opening-claims.md)
records the agreed boundary. There is no track rewrite, new game or dependency.

## Claims and corrections

| Location | Exact former text | Proposed explanation |
| --- | --- | --- |
| Blitz overview description | “It looks like BASIC and runs like C.” | Describes the compile loop and subjects without a language-wide timing comparison. |
| Blitz overview | “Blitz hands you faster, lower-level tools and compiles them to the metal.” | Distinguishes the interpreter/editor loop from ahead-of-run compilation; a speed comparison needs a workload and machine. |
| AMOS 3 | “AMOS has two kinds: a plain name holds a **number**” | This example uses an integer and a string; real-number names end in `#`. Numeric ranges and precision are finite. |
| Blitz 3 | “the language quietly uses a big, safe box for everything” | Removes the AMOS safety/ranking claim. Explains value storage, range and optional overflow checking. |
| Blitz 3 | “Roomy, but uses the most memory.” | States the one/two/four-byte integer value storage; does not rank all types or whole-program memory. |
| Blitz 2 | “That's the bargain every Amiga game struck: give up the safety net, gain the speed.” | Explains which services are available in each mode; removes the universal historical claim and speed guarantee. |
| Blitz 2 | “VWait 100 … waits about two seconds for the display to settle” | Places the wait before the mode switch, for disk activity, following the manual. A fixed delay does not establish that a drive has finished. |
| Blitz 2–3 | “Type the program into Ted and press **right-Amiga + X**.” | Uses the established PED `.ab3` import route and Compile & Run / right-Amiga+#. |

The earlier audit’s unit-1 “compiled code runs many times faster” sentence was
already removed by the merged greeting work. We do not claim to remove it again.

The word exercise now also asks readers to change its fixed printed labels:
changing the variable’s type cannot change those quoted strings. AMOS units 2–3
carry forward the qualified Return step after the end-of-program requester.

## Primary sources and their limits

- **AMOS Professional User Guide**, §5.1, “Types of variables”, and §5.3, floating
  point: [variable types](https://amospromanual.dev/05-01-the-bare-bones.html#types-of-variables)
  and [maths](https://amospromanual.dev/05-03-maths.html).
  The manual distinguishes integer, real and string variables. The public §5.1
  transcription has a suspect integer-range numeral; we do not reproduce it or
  introduce a new AMOS boundary claim from it.
- **AmiBlitz3 guide**, pinned revision
  `5dd815f880d72c5285b380ef3ddebfa5766d0626`,
  [§2.5 Primitive Types](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Docs/Amiblitz3.guide#L1176)
  and [file format](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Docs/Amiblitz3.guide#L147).
  The signed integer widths/ranges and named XTRA fields are documented contracts;
  reading them is not a new compiler execution.
- **Blitz BASIC 2.1 manual**, chapter 3, printed pp. 21–23 (PDF pp. 32–34),
  [numeric overflow](https://daemonbite.com/files/linked/BB21Manual.pdf#page=34);
  chapter 7, printed pp. 47–51 (PDF pp. 58–62),
  [mode switching](https://daemonbite.com/files/linked/BB21Manual.pdf#page=58).
  It documents optional overflow checking and the pre-mode-switch delay. Its
  historical performance assertions are not used as a measured comparison.

The `VWait` finding is an ordering defect established from source and manual:
the maintained wait followed `BLITZ`, so it could not delay entry into that mode.
We have not reproduced a disk corruption or crash, and do not claim one. The
sample change moves that existing wait and updates its comment; all drawing
commands, dimensions and colours remain the same. Its capture driver’s complete
typing payload is updated to match. The driver’s existing controls remain a
historical capture route, not a newly qualified PED automation.

## Runtime probes and blocker

The already authorised official v3.13.0b archive was fetched again. Its SHA-256
is `e728b213f9e45cb2a2098dd41c9d3ea7d4810ff363725f9a75810bd09e788b3e`;
its compiler binary matches the greeting trial
(`b85caf464f00f6a6f7e4783ea4f9dadf5f61299772a2e78607c9df643fc749e6`).
Extraction reported `Failed to create parent directory` for an accented catalogue
path and exited 1. No complete installation or successful runtime is inferred.
No dependency was added.

Computer use then returned **“Sky Computer Use native pipe startup failed”**.
Browser selection returned **“Browser is not available: chrome”**; the surface
inventory contained no apps or browsers and repeated the native-pipe error.
No emulator session, program execution, new screenshot or visual review occurred.
The earlier runtime observations and browser timeouts remain separate evidence.

[Prepared probes](probes/) retain reproducible plain-text inputs:

| Probe | Expected observation to check later | Current result |
| --- | --- | --- |
| `types.ab3` | Maintained byte listing; with RuntimeDebug=0 and OverflowCheck=0, inspect 1000000, 100 and −106 before clicking | Not run |
| `word.ab3` | Change only the byte type and corresponding labels; inspect the final 150 | Not run |
| `blitzmode.ab3` | Corrected maintained sample; inspect both shapes, left-click and return to PED | Not run |

Use the existing named A1200/PAL, 2 MB chip + 8 MB fast, Kickstart 3.1 /
Workbench 3.1 configuration from the greeting report. Load these files into PED
using that report’s route. The changed `OverflowCheck` setting and graphics
sample still need this execution check. Do not infer a pass from host arithmetic,
a compiler exit, the old screenshots or a source match. Overflow-check-on
behaviour is documented, but no new runtime diagnostic was observed.

## Validation and remaining review

`validation.json` records actual build/content/artifact results. The verifier
checks changed-source identities, exact capture typing, pre-BLITZ wait order,
ten built routes, linked header styles and Amiga internal link targets. Its
wrong-order control must fail. These checks do not measure layout or interaction.

Before treating #767 as complete, run the retained numeric/graphics probes and
review the final rendered desktop and phone routes, including the previously
outstanding setup/first-greeting clickthrough in #766. Keep the three coordinated
PRs as drafts pending those checks or an explicit owner decision accepting the
limits. Merge the sample correction before the website, so its CodeFromFile
listing resolves to the intended source. No benchmark or learner trial was
performed; neither performance nor educational effectiveness is validated here.
