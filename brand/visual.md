# Visual foundations

Every value here is a token in `tokens/tokens.json`. CSS custom properties use the same names as the live site's Tailwind theme (`--color-navy`, `--font-heading`, …).

## Color
| Token | Value | Use |
|---|---|---|
| `color.paper` | #fbf9f3 | Page ground |
| `color.paper-2` | #f3f0e7 | Alternate section band, eyebrow fill |
| `color.surface` | #ffffff | Pricing cells and other raised panels |
| `color.ink` | #171717 | h2/h3, nav, default text |
| `color.muted` | #68655f | Paragraphs, leads, stage labels |
| `color.navy` | #0d1440 | h1, prices, CTA label; utility bar, form panel, footer |
| `color.green` | #5fbf46 | Fills only: CTA, underlines, arrow discs |
| `color.green-deep` | #3e9a2c | Green text: numerals, ✓, heading period, eyebrow |
| `color.line` | #17140f1f | Hairlines, dashed dividers |
| `color.on-navy*` | white at 100/80/78/72/60/10% | Text and fills on navy |
| `color.logo-*` | #1025a1 / #0b1970 / #7ed957 | Logo artwork only |

Contrast (WCAG 2): ink/paper 17.0 · navy/paper 16.7 · muted/paper 5.5 · muted/surface 5.8 · navy-on-green 7.6 · white/navy 17.6 · green-deep/paper 3.4 · green-deep/paper-2 3.1 · green/paper 2.2.

Rules: green is never text on light grounds; text on green is navy; no gradients; no shadows; no extra accent hues. There is no dark theme.

## Typography
- **Poppins** (`font.heading`, 600/700/800): headings, numerals, prices, stage labels.
- **Raleway** (`font.sans`; served as Raleway Variable via Fontsource on the site): everything else.
- Load: `https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Raleway:wght@400..800&display=swap` or `@fontsource-variable/raleway` + `@fontsource/poppins`.

| Style | Spec | Where |
|---|---|---|
| `display-1` | Poppins 700, 68px / 1.03, −0.025em; fluid clamp(40px, 5.2vw, 68px) | Hero h1, navy, one per page |
| `display-2` | Poppins 700, 40/50, −0.025em; clamp(28px, 3.4vw, 40px) | Section h2, ink |
| `form-title` | Poppins 700, 36/54, −0.9px | Lead-form heading |
| `numeral` | Poppins 800, 38px | Process steps 01–04 |
| `price` | Poppins 800, 32px | Prices |
| `numeral-sm` | Poppins 800, 28/28 | Pricing stage numbers |
| `title-sm` | Poppins 700, 15.5/23.25 | Stage titles (h3) |
| `stage-label` | Poppins 700, 14/20, .35px, uppercase | Pricing stage names |
| `price-unit` | Poppins 600, 14/21 | "one-time", "per month" |
| `lead` | Raleway 400, 19/31 | Hero subhead, intros |
| `body` | Raleway 400, 16/24 | Default |
| `body-sm` | Raleway 400, 14/22.75 | Step descriptions, checklists |
| `caption` | Raleway 400, 13.5/21.94 | Pricing descriptions |
| `nav` | Raleway 600, 15px | Header nav |
| `button` | Raleway 700, 15.5px | CTAs |
| `label` | Raleway 600, 13px | Form labels |
| `utility` | Raleway 400, 13px | Utility bar |
| `eyebrow` | Raleway 700, 12px, .3px, uppercase | Audience badge |

## Space and layout
- Base 4px (Tailwind `--spacing: .25rem`). Sections: `space.24` (96px) top/bottom, `space.8` (32px) sides.
- Grid max `size.container` (1240px); prose `size.container-narrow` (660px).
- Single-column narrative; two columns (text + image) from `size.breakpoint-md` (48rem).

## Shape and borders
- `radius.pill` — CTAs, eyebrow, icon buttons, arrow discs.
- `radius.panel` (26px) — form panel. `radius.image` (22px) / `radius.image-sm` (20px) — photography.
- Pricing cells are square.
- `border-width.hairline` in `color.line` (dashed between pricing cells); `border-width.underline` (2px) for nav, inputs, secondary button.
- Motion: `duration.default` (150ms, cubic-bezier(.4,0,.2,1)) where anything transitions. Nothing animates on its own.

## Imagery and icons
- Real-feeling photography of people and workspaces, corners `radius.image`. One illustrated editorial image appears in the philosophy section.
- No icon library. Checkmarks are "✓" in `color.green-deep` at 800 weight; arrows are "→" in navy inside a 24px `color.green` disc.

## Logos
See `assets/logos/README.md`. Horizontal logo on light grounds at `size.logo-height` (36px); the mark alone for square placements. No reversed version exists for navy.
