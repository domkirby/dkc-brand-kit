# Components

Reference implementations are in `components/dkc.css` (classes prefixed `.dkc-`, reading `tokens/tokens.css`). Open `components/previews/index.html` in a browser to see each one. Values were measured from the live site.

## Button
- **Primary** `.dkc-btn.dkc-btn-primary` — `color.green` fill, `color.navy` label, `button` text style, `radius.pill`, padding `space.4` × `space.7-5` (form submit: 16px × 34px). One per view.
- **Secondary** `.dkc-btn.dkc-btn-secondary` — no fill, navy label, 2px navy underline, padding `space.4` × `space.3`. Always beside a primary.
- Consumer provides: label, href. Labels sentence case, no icons.
- The live site defines no hover or focus style. New implementations must add a visible focus state (constitution VIII).

## Eyebrow
- `.dkc-eyebrow` — `eyebrow` text in `color.green-deep` on `color.paper-2`, 1px `color.line` border, `radius.pill`, padding `space.1-5` × `space.3-5`.
- One per page, directly above the h1. Names an audience ("For B2B small businesses").
- As built it is 3.1:1 — below AA for 12px. See open-decisions.md.

## Process step
- `.dkc-step` — `numeral` in green-deep, `title-sm` in ink, `body-sm` in muted.
- Always two-digit (01–04), in order, four across on desktop. Descriptions start with "We…".

## Pricing strip
- `ol.dkc-pricing > li.dkc-price-cell` — three `color.surface` cells, padding `space.8` × `space.9`, dashed 1px `color.line` dividers, square corners, no shadow.
- Cell: `numeral-sm` (green-deep) + `stage-label` (muted) → `price` (navy) + `price-unit` → `caption` description → ✓ checklist in `body-sm` (green-deep ticks, ink text).
- Cells after the first have a 24px green disc with a navy "→" on the left edge: stages are a sequence, not tiers.
- Consumer provides: number, stage name, price, unit, description, 3–4 checklist lines.

## Lead form
- `.dkc-form` — navy panel, `radius.panel`, padding `space.16`; `form-title` heading in on-navy; intro in on-navy-body.
- Underline-only fields: transparent, 2px green bottom border, on-navy 15px/600 text, `label` style labels in on-navy-muted. Two columns on desktop.
- Fields in order: First name, Last name, Email, Company or brand name, Timeline (First availability / 3–6 months / Just exploring), Industry (MSP, Professional Services, Retail, Healthcare, Technology, Other), State (US), project description. Submit: primary button "Send it over".
- Inputs on the live site remove the focus outline without replacement; add one.

## Site header
- Utility bar: navy, `utility` text in on-navy-soft — email left, "Client Support →" right.
- Header: paper, 1px line below, logo at `size.logo-height`, `nav` links in navy; current page gets a 2px green underline (`aria-current`).
- Nav order: Home, MSP Websites, Web Hosting, Why Static, Get in Touch.

## Footer
- Navy background, padding 56px 32px 32px; links in on-navy-link (14px); social links as single glyphs in round `color.on-navy-fill` buttons. (Not separately previewed.)
