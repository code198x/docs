# SimCity — evidence and review boundaries

This is an unreviewed draft. It extends the existing whole-game composition, not a new curriculum implementation or a claim to have reviewed every version.

## Sources

The bibliography distinguishes original manuals, contemporary criticism, creator interviews, participant writing, source code and later publisher accounts. The 1989 Amiga manual is a text transcription; the 1992 DUX/HyperLook manual belongs to a different version. Its workstation requirements, pie menus and concurrent zoom views are not attributed to the Amiga. The July 1999 Palm OS manual returned by a search labelled “1989” was rejected as evidence for original interface behaviour.

CGW 59 pp16–17 was downloaded and read; p16 was rendered and visually inspected. It establishes the review's own experiences, not independently validated urban realism. Its Brøderbund/scenario and Lem accounts are attributed. CGW 214 p65 (PDF page69) was rendered, OCRed and visually inspected: the text reports Wright's research leading towards Conway and Forrester; it does not establish that all of either scientist's work entered the simulation. No broad “first city game” claim.

The licensed Prima retrospective contradicts itself about early release and 2000's year. These dates are not adopted. EA's own timeline independently supplies 1989/1993/1997/1999/2003. CHM's exhibit has inconsistent game/fire dates; those were not adopted. The complete Gingold book has not been read; the publisher's catalogue supports its further-reading listing only, not detailed historical claims.

Hopkins' interface account explicitly mixes Wright's talks with his own elaboration. The article says so and contains no reconstructed verbatim quotation. The single short Wright quotation in the 1995 interview is paraphrased in the draft; no more than 25 words quoted from an individual source.

Micropolis source was inspected at c98f6b08519887b450d9be198bfca5237aab6d0c: traffic.cpp/tryDrive performs bounded route attempts; simulate.cpp divides work into phases. This later C++ descendant is not presented as the original Amiga binary. No source-code excerpt or third-party diagram copied. The budget and feedback illustrations are our own, with invented numbers explicitly labelled. 2000/3000/4/2013/Skylines are documentary comparisons, not games played in this session.

## Images and play

Own headless MAME Amiga captures use a held disk image and verified firmware set. Inputs are ordinary mouse/keyboard operations through MAME's Lua input API. The capture harness selects Mouse using the configuration field's user_value; set_value on that configuration field does not select its enum. The mistaken configuration was a harness problem, not evidence of an emulator/game defect.

Full native frames, media hashes, exact tool/configuration and input schedules are recorded in captures/manifest.json. No ROMs, disk images, firmware, save states, memory dumps or private collection paths are published. Working media and any temporary emulator checkpoint stay private and are removed during cleanup. No gameplay code patch or memory write is used. A temporary checkpoint can shorten later observation; the full boot/build input script remains reproducible.

These observations are an early building experiment, not a scenario victory, long-term balanced city or complete tour. Captions distinguish actual game output from the original imagined header and explanatory diagrams. Sound was disabled in the headless run: no claim to have listened to or measured audio. The manual's sound option is documented, not evidence that all editions sound alike. People/advertising imagery remains absent rather than borrowed without a rights record.

## Publication

Canonical prose remains separate from the concise game entry. Human historical and voice review is pending; reviewed stays false and the study is excluded from sitemap/search indexing. Future practical work and any Pattern Library restructuring need their own agreed design. See the existing Craft/Pattern proposal rather than treating these themes as published lessons.

## Static validation

Six figure paths and seventeen numbered bibliography sources resolve. All four native capture hashes/dimensions checked, all four original SVGs parsed, and the two invented budget balances recomputed. The CSV has 2,887 records, unique stable IDs and fifteen new needs-triage rows. Open and closed issue title audit returned 281 issues, with no matching new subjects. Website rendering and browser evidence are recorded with its integration PR.
