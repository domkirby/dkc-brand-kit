# Open decisions and known issues

Captured 2026-10-10. Nothing here has been changed in the tokens; values are recorded exactly as the live site uses them. Resolving any item is a constitution amendment.

## Decisions
1. **Logo colors vs. UI colors.** The logo uses #1025a1 / #0b1970 / #7ed957; the UI uses navy #0d1440 and green #5fbf46. Options: tighten the UI to the logo, re-export the logo in the UI colors, or keep both and document the logo palette as artwork-only (current state).
2. **Reversed logo.** There is no logo version for navy grounds (footer, form panel, utility bar).
3. **Manage and hosting.** Whether $49.95/mo includes hosting for every client, and what happens to legacy hosting-only clients on $19.95/$39.95 plans.
4. **MSP page FAQ.** Real questions and answers still need writing.

## Accessibility (live site)
| Issue | Where | Measured | Target |
|---|---|---|---|
| Eyebrow text contrast | green-deep #3e9a2c on paper-2 #f3f0e7, 12px bold | 3.1:1 | 4.5:1 |
| No input focus style | Lead-form inputs set `outline: none` | — | Visible focus (WCAG 2.4.7) |
| No button hover/focus style | Primary and secondary CTAs | — | Visible focus |

## Performance (live site)
| Asset | Size | Note |
|---|---|---|
| `horiz-logo-dkc-dark.svg` | ~636 KB | Traced outlines, ~1,860 paths, loaded on every page |
| `favicon.svg` | ~279 KB | Traced outlines, ~2,350 paths |
These undercut the "fast" positioning. A clean vector export of the mark and wordmark would likely be a few KB.
