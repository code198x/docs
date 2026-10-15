# Contrast follow-up

The three incomplete Structure colour-contrast checks concern long pseudocode
lines clipped by their horizontal scroll containers at width 390. Axe reports
`elmPartiallyObscured`: it cannot determine the complete element's background.
Its reported contrastRatio of zero is a placeholder for that failed calculation,
not a measured text/background ratio.

The [raw axe record](before-axe.json) identifies the elements. The independent
[rendered-colour check](before-colours.json) reads the foreground and first opaque
background, checks ancestor opacity/background images, and computes relative
luminance and contrast. All three use foreground rgb(27,26,23) on background
rgb(252,251,248), giving **16.8168:1**, above axe's required 4.5:1. All three scroll
containers accept keyboard focus; End moves their horizontal scroll positions
by 76, 230 and 57 pixels respectively. The visible text was inspected in viewport
captures after that keyboard action.

This resolves the contrast question for those particular text elements. It does
not establish that every colour on the site passes or provide screen-reader or
learner evidence. The original pilot records correctly retain their incomplete
status; this follow-up supplements them rather than rewriting prior results.
The initial arithmetic contrast warning did not recur in this settled live check.

The approved arithmetic and Structure merges change no files under website
`src/styles/` or `src/components/`; the code-block styling measured here is
unchanged by those merges. These observations were made on the live pages before
the new deployment finished, rather than presented as a full post-deployment sweep.
