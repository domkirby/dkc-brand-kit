# Dom Kirby Creative brand

This repository is the DKC brand kit. Follow `AGENTS.md` and the constitution at `.specify/memory/constitution.md` for any copy, UI or styling work.

- Use tokens, never raw values: `tokens/tokens.css` (`var(--color-navy)`), `tokens/tailwind-theme.css` (`bg-navy`, `font-heading`) or `tokens/tokens.ts`.
- `color.green` is a fill, never text on light grounds; green text is `color.green-deep`; text on green is navy.
- Poppins for headings, numerals and prices; Raleway for everything else.
- No shadows, gradients, emoji or exclamation marks. Prices in full with units.
- Logos only from `assets/logos/`.
- Edit tokens in `tokens/tokens.json`, then run `python3 scripts/build_tokens.py`.
