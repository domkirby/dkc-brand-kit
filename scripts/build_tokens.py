#!/usr/bin/env python3
"""Build tokens/tokens.css, tokens/tailwind-theme.css and tokens/tokens.ts from tokens/tokens.json.

tokens.json is the single source of truth. Run after any change:
    python3 scripts/build_tokens.py
Standard library only (Python 3.8+).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tokens" / "tokens.json"
OUT = ROOT / "tokens"
EXT = "com.domkirbycreative"
HEADER = "Dom Kirby Creative tokens. GENERATED from tokens/tokens.json by scripts/build_tokens.py, do not edit by hand."

# Group name in tokens.json -> CSS custom-property prefix (matches the live site's Tailwind names).
CSS_PREFIX = {
    "color": "color", "font": "font", "font-weight": "font-weight", "space": "space",
    "radius": "radius", "border-width": "border-width", "size": "size", "duration": "duration",
}


def tokens_in(group):
    return [(k, v) for k, v in group.items() if not k.startswith("$")]


def css_value(token_type, value):
    if token_type == "fontFamily":
        return ", ".join(f'"{f}"' if " " in f else f for f in value)
    return str(value)


def resolve_ref(ref, data):
    """'{font.heading}' -> (css var, raw value)."""
    m = re.fullmatch(r"\{([^}]+)\}", str(ref))
    if not m:
        return None, ref
    group, name = m.group(1).split(".", 1)
    node = data[group][name]
    return f"var(--{CSS_PREFIX[group]}-{name})", node["$value"]


def main():
    data = json.loads(SRC.read_text())
    css, tw, ts = [], [], {}

    # ---- primitive groups -------------------------------------------------
    for group, prefix in CSS_PREFIX.items():
        gtype = data[group].get("$type")
        ts[group] = {}
        for name, tok in tokens_in(data[group]):
            ttype = tok.get("$type", gtype)
            val = css_value(ttype, tok["$value"])
            css.append(f"  --{prefix}-{name}: {val};")
            ts[group][name] = val
            # Tailwind v4 @theme: colors, fonts, radii, containers. Spacing comes from the default
            # --spacing: .25rem base (p-24 = 96px), weights and breakpoints match Tailwind defaults.
            if group in ("color", "font", "radius"):
                tw.append(f"  --{prefix}-{name}: {val};")
    tw.append(f"  --container-content: {data['size']['container']['$value']};")
    # "narrow", not "prose": Tailwind's built-in max-w-prose (65ch) would shadow --container-prose.
    tw.append(f"  --container-narrow: {data['size']['container-narrow']['$value']};")

    # ---- typography -------------------------------------------------------
    classes = []
    ts["typography"] = {}
    for name, tok in tokens_in(data["typography"]):
        v = tok["$value"]
        ext = tok.get("$extensions", {}).get(EXT, {})
        fam_var, fam_raw = resolve_ref(v["fontFamily"], data)
        size = ext.get("fluid", v["fontSize"])
        ls = ext.get("letterSpacingEm", v["letterSpacing"])
        lh = v["lineHeight"]
        rules = [
            f"font-family: {fam_var};",
            f"font-size: {size};",
            f"font-weight: {v['fontWeight']};",
            f"line-height: {lh};",
            f"letter-spacing: {ls};",
        ]
        if ext.get("textTransform"):
            rules.append(f"text-transform: {ext['textTransform']};")
        if ext.get("color"):
            col_var, _ = resolve_ref(ext["color"], data)
            rules.append(f"color: {col_var};")
        classes.append(f".dkc-text-{name} {{ " + " ".join(rules) + " }")
        tw.append(f"  --text-{name}: {size};")
        tw.append(f"  --text-{name}--line-height: {lh};")
        tw.append(f"  --text-{name}--letter-spacing: {ls};")
        tw.append(f"  --text-{name}--font-weight: {v['fontWeight']};")
        ts["typography"][name] = {
            "fontFamily": css_value("fontFamily", fam_raw),
            "fontSize": v["fontSize"], "fontWeight": v["fontWeight"],
            "lineHeight": lh, "letterSpacing": v["letterSpacing"],
            **({"fluidFontSize": ext["fluid"]} if "fluid" in ext else {}),
            **({"textTransform": ext["textTransform"]} if "textTransform" in ext else {}),
        }

    (OUT / "tokens.css").write_text(
        f"/* {HEADER} */\n\n:root {{\n" + "\n".join(css) + "\n}\n\n"
        "/* Text styles: apply with class=\"dkc-text-<name>\". */\n" + "\n".join(classes) + "\n"
    )
    (OUT / "tailwind-theme.css").write_text(
        f"/* {HEADER}\n"
        "   Tailwind v4: @import \"tailwindcss\"; then @import \"./tailwind-theme.css\";\n"
        "   Gives bg-navy, text-green-deep, font-heading, rounded-panel, text-display-1, max-w-content, max-w-narrow, etc. */\n\n"
        "@theme {\n" + "\n".join(tw) + "\n}\n"
    )
    (OUT / "tokens.ts").write_text(
        f"// {HEADER}\n\nexport const tokens = "
        + json.dumps(ts, indent=2)
        + " as const;\n\nexport type DkcTokens = typeof tokens;\n"
        + "export type DkcColor = keyof typeof tokens.color;\n"
        + "export type DkcTextStyle = keyof typeof tokens.typography;\n"
        + "export default tokens;\n"
    )
    print(f"Built {len(css)} variables and {len(classes)} text styles -> tokens.css, tailwind-theme.css, tokens.ts")


if __name__ == "__main__":
    sys.exit(main())
