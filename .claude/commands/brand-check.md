---
description: Review changes or a file against the Dom Kirby Creative brand constitution
argument-hint: "[file or path — defaults to uncommitted changes]"
---

Review $ARGUMENTS (if empty: the current uncommitted git changes) against the Dom Kirby Creative brand.

Load the `dkc-brand` skill, then read the kit's `.specify/memory/constitution.md`, `brand/voice.md`, `brand/visual.md` and `brand/open-decisions.md`.

Check:
1. **Tokens** — any hardcoded color, font size, radius or spacing that should be a token; any `color.logo-*` used in UI; green used as text on a light ground; white text on green.
2. **Type** — only Poppins/Raleway and the named text styles; at most one `display-1`.
3. **Shape and depth** — no shadows, gradients or extra accent colors; radii from the scale.
4. **Copy** — "we"/"you", sentence case, no exclamation marks or emoji, none of the rejected words, prices in full with units, "Built for X. Not Y." at most once per page.
5. **Accessibility** — contrast (4.5:1 text, 3:1 large text and UI), visible focus states, labelled inputs, alt text on logos and images.

Report a table: severity (must / should), file:line, principle, problem, exact fix. Then a one-line verdict. Do not edit files unless asked.
