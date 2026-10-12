# Dom Kirby Creative brand kit — agent guide

This repository is the brand and design-token source for **Dom Kirby Creative (DKC)**: fast, secure, static (Astro) websites for B2B small businesses, with a specialty in MSPs. Use it whenever you write DKC copy or build or review DKC UI.

In a project that installed this kit, everything below lives under `dkc-brand/`. Paths here are relative to the kit root.

## Read in this order
1. `.specify/memory/constitution.md` — the non-negotiables (8 principles). Check every spec, plan, change and line of copy against it.
2. `brand/voice.md` — how DKC writes, with real lines to model.
3. `brand/visual.md` — color, type, spacing, shape and imagery rules with every value.
4. `brand/components.md` — Button, Eyebrow, Process step, Pricing strip, Lead form, Site header, Footer.
5. `brand/open-decisions.md` — unresolved questions and known issues. Don't copy the listed defects into new work, and don't "fix" brand values on your own; raise them.

## Hard rules (summary — the constitution is authoritative)
- Use tokens, never raw values. CSS: `var(--color-navy)`. Tailwind v4: `bg-navy`, `text-green-deep`, `font-heading`, `rounded-panel`, `text-display-1`. TS/JS: `tokens.color.navy`.
- `color.green` (#5fbf46) is a fill, never text on light grounds; green text is `color.green-deep`. Text on green is navy.
- `color.logo-*` is for the logo artwork only.
- Poppins for headings, numerals and prices; Raleway for everything else. Only the named text styles.
- No shadows, gradients, emoji, exclamation marks or extra accent colors.
- Prices appear in full with units: Audit $500 one-time · Redesign $1,500 one-time (Simplify included) · Manage $49.95/mo.
- Hero headlines use "Built for X. Not Y." — once per page.
- WCAG 2.2 AA for new work, including visible focus states.

## Files
| Path | What |
|---|---|
| `tokens/tokens.json` | Source of truth (W3C design-token structure). Edit here only. |
| `tokens/tokens.css` | Generated CSS custom properties + `.dkc-text-*` text-style classes |
| `tokens/tailwind-theme.css` | Generated Tailwind v4 `@theme` block (same names as the live site) |
| `tokens/tokens.ts` | Generated typed export for TS/JS (Vue, React, Astro, Node) |
| `components/dkc.css` | Reference component classes (`.dkc-*`) built on the tokens |
| `components/previews/index.html` | Open in a browser to see every component |
| `assets/logos/` | Official logo files — use as supplied, never redraw |
| `scripts/build_tokens.py` | Regenerates the three token outputs after editing `tokens.json` |
| `scripts/install.sh` | Installs the kit into another project |

## Using the tokens
- **Tailwind v4 / Astro** (the live site's stack): `@import "tailwindcss"; @import "../dkc-brand/tokens/tailwind-theme.css";`
- **Plain CSS / Laravel Blade / WordPress theme**: link `tokens/tokens.css` (and `components/dkc.css` for ready-made components).
- **Vue / TS**: `import { tokens } from "../dkc-brand/tokens/tokens";`
- Fonts: `https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Raleway:wght@400..800&display=swap`, or `@fontsource/poppins` + `@fontsource-variable/raleway`.

## Changing the brand
Edit `tokens/tokens.json` and/or the `brand/` docs, run `python3 scripts/build_tokens.py`, and amend the constitution's version and Sync Impact Report in the same change.
