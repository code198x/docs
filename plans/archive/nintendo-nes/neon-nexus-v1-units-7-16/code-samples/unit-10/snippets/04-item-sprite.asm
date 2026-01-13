;──────────────────────────────────────────────────────────────
; UPDATE ITEM SPRITE
;──────────────────────────────────────────────────────────────
; Write item position to shadow OAM.
; Uses sprite slot 5 (after player and 4 enemies).

.proc update_item_sprite
    lda item_y
    sta $0200 + 20          ; Sprite 5: Y position
    lda #4                  ; Item tile (diamond shape)
    sta $0200 + 21          ; Sprite 5: tile index
    lda #%00000010          ; Palette 2 (green)
    sta $0200 + 22          ; Sprite 5: attributes
    lda item_x
    sta $0200 + 23          ; Sprite 5: X position
    rts
.endproc

; Shadow OAM layout:
; $0200-$0203: Player (sprite 0)
; $0204-$0213: Enemies (sprites 1-4)
; $0214-$0217: Item (sprite 5)
;
; Each sprite uses 4 bytes: Y, tile, attributes, X
