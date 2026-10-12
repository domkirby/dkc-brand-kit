#!/usr/bin/env bash
#
# install.sh — add the Dom Kirby Creative brand kit to another project.
#
# Usage:  ./scripts/install.sh /path/to/project
#
# What it does (safe to re-run; it never overwrites files you wrote):
#   1. Copies the kit into <project>/dkc-brand/ (replacing any previous copy of the kit only).
#   2. Installs the Claude Code skill and /brand-check command into <project>/.claude/.
#   3. Adds a short, marked pointer block to <project>/AGENTS.md and <project>/CLAUDE.md
#      (creating them if missing).
#   4. Adds the Cursor rule, and a pointer block in .github/copilot-instructions.md if that file exists.
#   5. Spec Kit: if <project>/.specify/ exists, links the brand constitution into
#      .specify/memory/constitution.md (copies it if there is none, otherwise appends a marked
#      section that points at dkc-brand/.specify/memory/constitution.md).
#
set -euo pipefail

KIT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-}"
if [[ -z "$TARGET" || ! -d "$TARGET" ]]; then
    echo "Usage: $0 /path/to/existing/project" >&2
    exit 1
fi
TARGET="$(cd "$TARGET" && pwd)"
if [[ "$TARGET" == "$KIT" ]]; then
    echo "Error: target is the kit itself." >&2
    exit 1
fi

DEST="$TARGET/dkc-brand"
START="<!-- dkc-brand:start -->"
END="<!-- dkc-brand:end -->"

POINTER="$START
## Dom Kirby Creative brand
All copy and UI in this project follows the DKC brand kit in \`dkc-brand/\`.
Read \`dkc-brand/AGENTS.md\`, then \`dkc-brand/.specify/memory/constitution.md\` (authoritative).
Use tokens, never raw values: \`dkc-brand/tokens/tailwind-theme.css\`, \`tokens.css\` or \`tokens.ts\`.
$END"

# add_block FILE — append the pointer block once; leave an existing block untouched.
add_block() {
    local file="$1"
    mkdir -p "$(dirname "$file")"
    if [[ -f "$file" ]] && grep -qF "$START" "$file"; then
        echo "    = $file (already linked)"
        return
    fi
    if [[ -s "$file" ]]; then printf '\n%s\n' "$POINTER" >> "$file"; else printf '%s\n' "$POINTER" > "$file"; fi
    echo "    + $file"
}

echo "==> Copying kit to $DEST"
rm -rf "$DEST"
mkdir -p "$DEST"
for item in AGENTS.md README.md .specify brand tokens components assets scripts; do
    cp -R "$KIT/$item" "$DEST/"
done

echo "==> Claude Code skill and command"
mkdir -p "$TARGET/.claude/skills/dkc-brand" "$TARGET/.claude/commands"
cp "$KIT/.claude/skills/dkc-brand/SKILL.md" "$TARGET/.claude/skills/dkc-brand/SKILL.md"
cp "$KIT/.claude/commands/brand-check.md" "$TARGET/.claude/commands/brand-check.md"
echo "    + .claude/skills/dkc-brand/SKILL.md, .claude/commands/brand-check.md"

echo "==> Agent entry points"
add_block "$TARGET/AGENTS.md"
add_block "$TARGET/CLAUDE.md"
mkdir -p "$TARGET/.cursor/rules"
cp "$KIT/.cursor/rules/dkc-brand.mdc" "$TARGET/.cursor/rules/dkc-brand.mdc"
echo "    + .cursor/rules/dkc-brand.mdc"
if [[ -f "$TARGET/.github/copilot-instructions.md" ]]; then
    add_block "$TARGET/.github/copilot-instructions.md"
fi

if [[ -d "$TARGET/.specify" ]]; then
    echo "==> Spec Kit"
    CONST="$TARGET/.specify/memory/constitution.md"
    if [[ ! -f "$CONST" ]]; then
        mkdir -p "$(dirname "$CONST")"
        cp "$KIT/.specify/memory/constitution.md" "$CONST"
        echo "    + $CONST (brand constitution)"
    elif grep -qF "$START" "$CONST"; then
        echo "    = $CONST (already linked)"
    else
        cat >> "$CONST" <<EOF

$START
## Brand Constraints (Dom Kirby Creative)
All user-facing copy and UI MUST comply with the Dom Kirby Creative Brand Constitution at
\`dkc-brand/.specify/memory/constitution.md\` (principles I–VIII). Where the two conflict on a
brand matter (voice, visual design, pricing presentation, logo use), the brand constitution wins.
$END
EOF
        echo "    + $CONST (brand section appended)"
    fi
else
    echo "==> No .specify/ here — skipping Spec Kit. Re-run after 'specify init' to link the constitution."
fi

cat <<DONE

Done. Next:
  - Tailwind v4:  @import "../dkc-brand/tokens/tailwind-theme.css";   (adjust the relative path)
  - Plain CSS:    <link rel="stylesheet" href="/dkc-brand/tokens/tokens.css">
  - Claude Code:  /brand-check to review changes against the brand
To update later, pull the kit and run this script again.
DONE
