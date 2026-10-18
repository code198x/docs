"""Draw original explanatory vectors, not a reconstruction of game frames.

Run with Python 3.13+; standard library only. SVG coordinates count downwards.
"""

from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).parent
INK = "#25231f"
BLUE = "#165b96"
ORANGE = "#a54412"
GREEN = "#126650"


def arrow(
    x: int, y: int, dx: int, dy: int, colour: str, marker: str, dashed: bool = False
) -> str:
    dash = ' stroke-dasharray="5 5"' if dashed else ""
    return f'<path d="M{x} {y} l{dx} {dy}" fill="none" stroke="{colour}" stroke-width="3" marker-end="url(#{marker})"{dash}/>'


def label(x: int, y: int, text: str, colour: str = INK, anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" fill="{colour}" text-anchor="{anchor}">{text}</text>'


def write(name: str, title: str, description: str, content: str) -> None:
    markers = "".join(
        f'<marker id="{name}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="{colour}"/></marker>'
        for name, colour in [
            ("blue", BLUE),
            ("orange", ORANGE),
            ("green", GREEN),
            ("neutral", INK),
        ]
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="320" viewBox="0 0 360 320" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{description}</desc>
<rect width="360" height="320" fill="#f7f5ef"/>
<defs>{markers}</defs><g font-family="system-ui, sans-serif" font-size="18">{content}</g></svg>\n"""
    (ROOT / f"{name}.svg").write_text(svg, encoding="utf-8")


# Coasting: four positions at equal intervals, each separated by 85 units.
positions = [45, 130, 215, 300]
assert len({b - a for a, b in pairwise(positions)}) == 1
ships = "".join(
    f'<path d="M{x} 130 l-10 27 10-6 10 6 Z" fill="none" stroke="{INK}" stroke-width="2"/>'
    + label(x, 190, f"{i} s", anchor="middle")
    for i, x in enumerate(positions)
)
write(
    "coast",
    "Coast: facing up, moving right",
    "With thrust and gravity absent, a ship facing upwards moves equal distances right in equal time intervals. Its heading and velocity are different directions.",
    label(24, 35, "Coast")
    + label(24, 69, "Engine off · gravity left out")
    + ships
    + arrow(45, 230, 255, 0, BLUE, "blue")
    + label(180, 277, "Same velocity throughout", BLUE, "middle"),
)

# Velocity addition: v=(210,0), delta-v=(0,-140), result=(210,-140).
v = (210, 0)
dv = (0, -140)
result = tuple(a + b for a, b in zip(v, dv))
assert result == (210, -140)
write(
    "thrust",
    "Thrust adds an upward change to a rightward velocity",
    "The old velocity points right. An upward change from thrust is added at its tip. The resulting velocity points up and right from the same starting point.",
    label(24, 35, "Add thrust")
    + label(34, 76, "After: up + right", GREEN)
    + arrow(65, 235, *v, BLUE, "blue")
    + arrow(275, 235, *dv, ORANGE, "orange")
    + arrow(65, 235, *result, GREEN, "green")
    + label(75, 275, "Before: right", BLUE)
    + label(175, 187, "Thrust", ORANGE)
    + label(175, 210, "change", ORANGE),
)

# One illustrative gravity update: the acceleration direction points to the star.
origin = (60, 110)
star = (260, 250)
dv = (80, 56)
v = (150, 0)
assert dv[0] * (star[1] - origin[1]) == dv[1] * (star[0] - origin[0])
result = tuple(a + b for a, b in zip(v, dv))
assert result == (230, 56)
write(
    "gravity",
    "Gravity changes velocity towards the star",
    "The ship has a rightward velocity. Gravity adds a down-right change pointing towards the star. The resulting velocity is down and right. These arrows show one velocity update, not the flight path.",
    label(24, 35, "Add gravity")
    + arrow(*origin, *v, BLUE, "blue")
    + arrow(*origin, *dv, ORANGE, "orange")
    + arrow(origin[0] + v[0], origin[1] + v[1], *dv, ORANGE, "orange", True)
    + arrow(*origin, *result, GREEN, "green")
    + label(78, 86, "Before", BLUE)
    + label(24, 200, "Gravity change", ORANGE)
    + label(216, 200, "After", GREEN)
    + '<circle cx="260" cy="250" r="17" fill="#a54412"/><circle cx="60" cy="110" r="4" fill="#25231f"/>'
    + label(260, 294, "Star", anchor="middle"),
)


write(
    "control-response",
    "From a held thrust control to a moving ship",
    "Holding thrust applies acceleration. Acceleration changes velocity; velocity changes position. Releasing thrust ends its acceleration contribution, not the motion already acquired. Gravity may still act.",
    label(180, 35, "Hold the thrust control", anchor="middle")
    + arrow(180, 47, 0, 35, INK, "neutral")
    + label(180, 105, "Acceleration while held", anchor="middle")
    + arrow(180, 117, 0, 35, INK, "neutral")
    + label(180, 175, "Velocity changes", anchor="middle")
    + arrow(180, 187, 0, 35, INK, "neutral")
    + label(180, 245, "Position changes", anchor="middle")
    + label(180, 294, "Release thrust ≠ stop motion", anchor="middle"),
)

print(
    "Wrote four diagrams; equal-spacing, vector-sum and radial-direction checks pass."
)
