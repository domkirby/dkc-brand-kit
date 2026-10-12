---
name: dkc-brand
description: Dom Kirby Creative brand rules, design tokens and components. Use whenever writing DKC copy (site pages, emails, proposals, posts) or building, styling or reviewing any DKC or MSPSite.io page, component, slide or graphic.
---

# Dom Kirby Creative brand

1. Find the kit root: `dkc-brand/` in an installed project, otherwise the repository root (where `tokens/tokens.json` lives).
2. Read `<kit>/.specify/memory/constitution.md` first. It is authoritative.
3. Then read only what the task needs:
   - Copy → `<kit>/brand/voice.md`
   - UI, styling, graphics → `<kit>/brand/visual.md` and `<kit>/brand/components.md`
   - Anything touching colors, logo or accessibility → also `<kit>/brand/open-decisions.md`
4. Build with tokens, never raw values:
   - Tailwind v4: import `<kit>/tokens/tailwind-theme.css` → `bg-navy`, `text-green-deep`, `font-heading`, `rounded-panel`, `text-display-1`
   - CSS: `<kit>/tokens/tokens.css` → `var(--color-navy)`, `.dkc-text-lead`; components in `<kit>/components/dkc.css`
   - TS/JS: `import { tokens } from "<kit>/tokens/tokens"`
5. Logos come from `<kit>/assets/logos/` only. Never draw or approximate the mark.
6. Before finishing, check the work against each constitution principle. Name any principle you could not satisfy and why.

Never edit the kit's tokens or constitution as a side effect of other work. Brand changes are explicit amendments (see the constitution's Governance section).
