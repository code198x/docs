; Audit-only unsigned 16-bit scaled addition and whole-part extraction.
org 32768
start:
    di
    ld hl,384
    ld de,128
    add hl,de
    ld ($9000),hl
    ld hl,384
    ld a,h
    ld ($9002),a
    ld hl,65535
    ld de,1
    add hl,de
    ld ($9003),hl
    push af
    pop hl
    ld ($9005),hl
hold:
    jr hold
end start
