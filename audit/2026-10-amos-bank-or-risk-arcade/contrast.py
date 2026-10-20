"""Check the actual RGB12 palette's text roles against their drawn backgrounds."""

from __future__ import annotations

import json

PALETTE = ["112", "FFE", "4FF", "F6B", "FE4", "224", "7F9", "BAD"]


def rgb(value: str) -> tuple[int, int, int]:
    return tuple(int(c, 16) * 17 for c in value)


def luminance(value: str) -> float:
    channels = [c / 255 for c in rgb(value)]
    channels = [
        c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels
    ]
    return sum(a * b for a, b in zip(channels, [0.2126, 0.7152, 0.0722], strict=True))


def checks() -> dict:
    result = {}
    pairs = (
        [(i, 0) for i in [1, 2, 3, 4, 6, 7]]
        + [(i, 5) for i in [1, 2, 3, 4, 7]]
        + [(0, 1)]
    )
    for foreground, background in pairs:
        a, b = sorted([luminance(PALETTE[foreground]), luminance(PALETTE[background])])
        contrast = (b + 0.05) / (a + 0.05)
        assert contrast >= 4.5, (foreground, background, contrast)
        result[f"{foreground}-on-{background}"] = {
            "foreground": rgb(PALETTE[foreground]),
            "background": rgb(PALETTE[background]),
            "contrast": contrast,
        }
    return {"palette_rgb12": PALETTE, "text_pair_minimum": 4.5, "pairs": result}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
