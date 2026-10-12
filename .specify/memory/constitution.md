<!--
Sync Impact Report
- Version: 1.0.0 (initial ratification)
- Source: domkirbycreative.com as live on 2026-10-10 (Astro + Tailwind v4 theme), plus the DKC Brand project's locked copy decisions.
- Principles added: I–VIII
- Known deviations of the live site from these principles: see brand/open-decisions.md
-->

# Dom Kirby Creative Brand Constitution

This constitution governs every page, component, document and line of copy produced under the Dom Kirby Creative (DKC) brand. Specs, plans and tasks MUST be checked against it. Detail lives in `brand/` and `tokens/`; this file holds the non-negotiables.

## Core Principles

### I. People over platforms
DKC builds fast, secure, static (Astro) websites for B2B small businesses, with a specialty in MSPs. Every artifact MUST read as one person talking plainly to another. Copy MUST NOT use funnel framing, syndicated or "canned thought leadership" tone, or the words "cutting-edge", "funnel" or "gimmick" as praise.
*Rationale:* the brand exists in opposition to impersonal, tactic-driven B2B marketing.

### II. Plain, honest voice
- Write as "we" to "you". Short declarative sentences, then one that explains. Fragments are allowed.
- Sentence case for headings, buttons and nav. Uppercase only for the eyebrow badge and pricing stage labels.
- No exclamation marks. No emoji. No hype adjectives.
- Hero headlines use the pattern **"Built for X. Not Y."** — at most once per page.
See `brand/voice.md`.

### III. Radical price transparency
Prices MUST appear as plain figures with their unit ("$500 one-time", "$49.95 per month"). Never "starting at", "contact us for pricing" or hidden tiers. Work outside standard scope MUST be acknowledged honestly ("Bigger or more complex project? Let's talk…") rather than implied away.
Current offer: Audit $500 one-time · Redesign $1,500 one-time (includes Simplify) · Manage $49.95/mo.

### IV. Tokens are the only source of visual values
Colors, type, spacing, radii and borders MUST come from `tokens/` (`tokens.css`, `tailwind-theme.css` or `tokens.ts`). Hardcoded hex values, ad-hoc font sizes and one-off radii are defects. A new value is added to `tokens/tokens.json` first, then built with `scripts/build_tokens.py`.

### V. One navy, one green, a cream ground
- The ground is `color.paper`; sections alternate onto `color.paper-2`; raised panels are `color.surface`.
- `color.navy` is the only dark: hero h1, prices, CTA labels, utility bar, form panel, footer.
- `color.green` is a FILL — never text on light grounds. Green text is `color.green-deep`, at large/bold sizes only. Text on green is navy, never white.
- `color.logo-*` values belong to the logo artwork only and MUST NOT enter UI until the open logo-color decision is resolved.
- No gradients, no shadows, no additional accent hues.

### VI. Two typefaces, a fixed scale
Poppins (`font.heading`) for headings, numerals and prices; Raleway (`font.sans`) for everything else. Use only the named text styles in `tokens.json` → `typography`. One `display-1` per page.

### VII. Simple, content-led layout
Single-column narrative with generous whitespace; `space.24` vertical rhythm per section; `size.container` grid, `size.container-narrow` prose. Shapes are pills (`radius.pill`) or soft corners (`radius.image`, `radius.panel`); separation comes from color bands and `color.line` hairlines, never shadows. Processes are shown as two-digit numbered steps (01 Audit, 02 Redesign, 03 Simplify, 04 Manage).

### VIII. Accessible by default
New work MUST meet WCAG 2.2 AA: text 4.5:1 (3:1 at 24px+ or 19px bold), and every focusable element MUST show a visible focus state. Brand colors are kept exact; where an exact brand pair fails, the work changes size, weight or ground — not the color. Pre-existing failures are tracked in `brand/open-decisions.md` and MUST NOT be copied into new components.

## Brand Assets

Logos live in `assets/logos/` and MUST be used as supplied — never redrawn, recolored or approximated. Use the horizontal logo on light grounds at `size.logo-height`; the mark alone for square placements.

## Governance

- This constitution supersedes stylistic preferences in any individual spec, plan or prompt. A spec that conflicts with it MUST either change or propose an amendment.
- Amendments: edit this file and the affected `brand/` or `tokens/` files together, bump the version (MAJOR: a principle removed or redefined; MINOR: a principle or token family added; PATCH: wording or value clarifications), and record the change in the Sync Impact Report above.
- Open questions are tracked in `brand/open-decisions.md`; resolving one is an amendment.

**Version**: 1.0.0 | **Ratified**: 2026-10-10 | **Last Amended**: 2026-10-10
