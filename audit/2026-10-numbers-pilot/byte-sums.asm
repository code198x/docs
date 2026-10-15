; Audit fixture: retain A and F after each actual ADD. No injected results.
org 32768
start:
    di
    ld a,255
    add a,1
    push af
    pop hl
    ld ($9000),hl
    ld a,127
    add a,1
    push af
    pop hl
    ld ($9002),hl
    ld a,5
    add a,251
    push af
    pop hl
    ld ($9004),hl
hold:
    jr hold
end start
