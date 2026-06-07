#!/usr/bin/env python3
"""
Validate Manim scene files for common issues.

Checks:
  - Scene class compiles (import + parse)
  - Bare wait() calls without explicit duration
  - Off-screen absolute coordinates (hardcoded pixel values)
  - Hardcoded color hex values outside the defined palette

Usage:
    python validate.py scenes/architecture.py
    python validate.py scenes/*.py
"""

import sys
import re
import ast
from pathlib import Path


# ---- Configuration ----

PALETTE_HEX = {
    # Semantic
    "#0066CC",  # primary BLUE_C
    "#7B2D8E",  # secondary PURPLE_C
    "#008A27",  # success GREEN_C
    "#E6A800",  # warning YELLOW_C
    "#CC0000",  # error RED_C
    "#008080",  # info TEAL_C
    "#808080",  # neutral GREY_C
    "#FFFFFF",  # text WHITE
    "#000000",  # background BLACK
    # AWS/GCP/Azure/K8s
    "#FF9900",  # AWS ORANGE
    "#1A56DB",  # GCP BLUE_D
    "#0078D4",  # Azure BLUE_B
    "#1E3A8A",  # K8s BLUE_E
    # Manim built-in hex equivalents (commonly used)
    "#58C4DD",  # BLUE
    "#00BFFF",  # BLUE_A
    "#236B8E",  # BLUE_B
    "#0066CC",  # BLUE_C  (duplicate — keep)
    "#005C99",  # BLUE_D
    "#003366",  # BLUE_E
    "#00FF00",  # GREEN
    "#00CC00",  # GREEN_A
    "#00AA00",  # GREEN_B
    "#008A27",  # GREEN_C
    "#006600",  # GREEN_D
    "#004400",  # GREEN_E
    "#FF0000",  # RED
    "#FF3333",  # RED_A
    "#CC0000",  # RED_C
    "#990000",  # RED_D
    "#660000",  # RED_E
    "#FFFF00",  # YELLOW
    "#FFE135",  # YELLOW_A
    "#FFD700",  # YELLOW_B
    "#E6A800",  # YELLOW_C
    "#CC9900",  # YELLOW_D
    "#B8860B",  # YELLOW_E
    "#AA00FF",  # PURPLE
    "#9B30FF",  # PURPLE_A
    "#8B00FF",  # PURPLE_B
    "#7B2D8E",  # PURPLE_C
    "#5E1A6E",  # PURPLE_D
    "#4A004A",  # PURPLE_E
    "#808080",  # GREY
    "#A0A0A0",  # GREY_A
    "#909090",  # GREY_B
    "#808080",  # GREY_C  (duplicate)
    "#606060",  # GREY_D
    "#404040",  # GREY_E
    "#FF9900",  # ORANGE  (duplicate with AWS)
}

FRAME_WIDTH = 16.0  # manim default
FRAME_HEIGHT = 9.0  # manim default (16:9)


# ---- Checks ----

def check_bare_wait(content: str, path: Path) -> list[str]:
    """Find bare `wait()` calls with no duration argument."""
    import ast
    try:
        tree = ast.parse(content, filename=str(path))
    except SyntaxError:
        return []  # Will be caught by check_compile

    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Name) and call.func.id == "wait":
                if not call.args and not call.keywords:
                    issues.append(f"{path}:{node.lineno} — bare wait() without duration argument")
    return issues


def check_hardcoded_colors(content: str, path: Path) -> list[str]:
    """Find hardcoded hex colors outside the defined palette."""
    issues = []
    # Match hex colors like #RRGGBB or #RGB
    pattern = re.compile(r'#[0-9A-Fa-f]{6}(?:[0-9A-Fa-f]{2})?')
    for match in pattern.finditer(content):
        hex_val = match.group().upper()[:7]
        if hex_val not in PALETTE_HEX:
            line_num = content[:match.start()].count('\n') + 1
            issues.append(f"{path}:{line_num} — hardcoded color {match.group()} outside palette")
    return issues


def check_absolute_coords(content: str, path: Path) -> list[str]:
    """Flag suspiciously large coordinate values that suggest absolute positioning."""
    issues = []
    # Look for numeric literals > 10 that are used as coordinates
    # Exclude numbers that are part of hex colors (#808080)
    large_number_pattern = re.compile(r'(?<!#)(?<!\.)(?:^|(?<=[\s\(\,]))(1[4-9]|[2-9]\d+)(?=[\s\)\,\:]|$)')
    for match in large_number_pattern.finditer(content):
        val = int(match.group())
        # Check approximate context — if it's near shift/move_to/next_to, flag it
        start = max(0, match.start() - 80)
        end = min(len(content), match.end() + 80)
        context = content[start:end]
        if any(kw in context for kw in ['shift(', 'move_to(', 'next_to(', '.x =', '.y =', 'center(']):
            line_num = content[:match.start()].count('\n') + 1
            issues.append(f"{path}:{line_num} — suspicious absolute coordinate {match.group()} (consider using UP/DOWN/LEFT/RIGHT constants)")
    return issues


def check_compile(path: Path) -> list[str]:
    """Try to parse the file as a Python AST. Reports syntax errors."""
    issues = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            ast.parse(f.read(), filename=str(path))
    except SyntaxError as e:
        issues.append(f"{path}:{e.lineno} — syntax error: {e.msg}")
    return issues


def check_scene_imports(content: str, path: Path) -> list[str]:
    """Check that Scene and common manim classes are imported if used."""
    issues = []
    has_class_def = "class " in content
    has_construct = "def construct(self)" in content
    if has_class_def and has_construct:
        # Class with construct() is likely a Scene — check manim import
        if "from manim import" not in content and "from manim import *" not in content:
            # Might use from manim import Scene, etc.
            if "from manim" not in content:
                issues.append(f"{path}:1 — Scene class defined but 'from manim import *' not found")
    return issues


# ---- Main ----

def validate_file(path: Path) -> int:
    """Validate a single Python scene file. Returns issue count."""
    if not path.exists():
        print(f"ERROR: {path} not found")
        return 1

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR: {path} — {e}")
        return 1

    all_issues = []
    all_issues.extend(check_compile(path))
    all_issues.extend(check_bare_wait(content, path))
    all_issues.extend(check_hardcoded_colors(content, path))
    all_issues.extend(check_absolute_coords(content, path))
    all_issues.extend(check_scene_imports(content, path))

    if all_issues:
        print(f"\n{path}:")
        seen = set()
        for issue in all_issues:
            if issue not in seen:
                print(f"  {issue}")
                seen.add(issue)
        return len(seen)
    else:
        print(f"PASS: {path}")
        return 0


def main():
    paths = sys.argv[1:]
    if not paths:
        print("Usage: python validate.py path/to/scene.py [path/to/another.py ...]")
        sys.exit(1)

    total_issues = 0
    for pattern in paths:
        for p in Path(".").glob(pattern):
            total_issues += validate_file(p)

    # Also try literal paths that are not glob patterns
    for p in paths:
        pp = Path(p)
        if pp.exists() and pp.suffix == ".py":
            total_issues += validate_file(pp)

    if total_issues > 0:
        print(f"\nFAIL: {total_issues} issue(s) found across all files")
        sys.exit(1)
    else:
        print(f"\nPASS: All files valid")
        sys.exit(0)


if __name__ == "__main__":
    main()
