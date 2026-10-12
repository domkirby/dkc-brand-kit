# Dom Kirby Creative — Brand Kit

The brand rules, design tokens, components and logos for Dom Kirby Creative, packaged so people and coding agents (Claude Code, Copilot, Cursor, Codex, Spec Kit) can all reference the same source.

Captured from domkirbycreative.com on 2026-10-10. Values are recorded exactly as the live site uses them; known issues are listed in `brand/open-decisions.md`, not silently fixed.

## What's inside
```
.specify/memory/constitution.md   Brand constitution (Spec Kit format) — the non-negotiables
AGENTS.md / CLAUDE.md              Entry points for coding agents
brand/                             voice, visual foundations, components, open decisions
tokens/tokens.json                 Source of truth (W3C design-token structure)
tokens/tokens.css                  Generated CSS variables + text-style classes
tokens/tailwind-theme.css          Generated Tailwind v4 @theme
tokens/tokens.ts                   Generated typed tokens for TS/JS
components/dkc.css                 Reference components (.dkc-*)
components/previews/index.html     Visual reference — open in a browser
assets/logos/                      Official logo files
.claude/  .cursor/  .github/       Claude Code skill + /brand-check, Cursor rule, Copilot instructions
scripts/build_tokens.py            Rebuild token outputs after editing tokens.json
scripts/install.sh                 Install into another project
```

## Use it in a project
```bash
./scripts/install.sh ~/code/my-astro-site
```
That vendors the kit into `my-astro-site/dkc-brand/`, adds the Claude Code skill and `/brand-check` command, links the brand from `AGENTS.md` and `CLAUDE.md`, adds the Cursor rule, and — if the project uses Spec Kit — links the brand constitution into `.specify/memory/constitution.md`. Re-running it is safe.

Or reference it without installing: add the kit as a git submodule, or start Claude Code with `--add-dir /path/to/dkc-brand-kit`.

## Change the brand
1. Edit `tokens/tokens.json` and/or `brand/*.md`.
2. `python3 scripts/build_tokens.py`
3. Bump the version and Sync Impact Report in `.specify/memory/constitution.md`.
