#!/usr/bin/env python3
"""
Validate .drawio files for common issues.

Checks:
  - Overlapping vertex geometries
  - Orphan connectors (missing source or target)
  - Font sizes below minimum 11pt
  - Color compliance with defined palette
  - Floating elements (cells without a container)

Usage:
    python validate.py path/to/diagram.drawio
    python validate.py *.drawio
"""

import sys
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from io import BytesIO


# ---- Configuration ----

MIN_FONT_SIZE = 11
CONNECTOR_LABEL_MIN = 10

PALETTE = {
    # Semantic
    "#3B82F6", "#60A5FA",  # primary
    "#8B5CF6", "#A78BFA",  # secondary
    "#22C55E", "#4ADE80",  # success
    "#F59E0B", "#FBBF24",  # warning
    "#EF4444", "#F87171",  # error
    "#06B6D4", "#22D3EE",  # info
    "#F3F4F6", "#D1D5DB",  # neutral light
    "#1F2937", "#4B5563",  # neutral dark
    "#111827",             # text light
    "#F9FAFB",             # text dark
    "#FFFFFF",             # background light
    # Cloud providers
    "#FF9900",             # AWS
    "#4285F4",             # GCP
    "#0078D4",             # Azure
    "#326CE5",             # K8s
    "#6B7280",             # generic service
    # Stroke defaults
    "#000000",
    "#333333",
}

NS = {"drawio": "http://www.w3.org/1999/xhtml"}


# ---- Helpers ----

def parse_drawio(path: Path) -> ET.Element:
    """Parse .drawio XML and return the root of the inner diagram file."""
    raw = ET.parse(path).getroot()
    # The mxfile wraps a compressed or plain mxGraphModel
    mxfile = raw
    # Find the inner diagram content
    diagram_el = mxfile.find(".//diagram")
    if diagram_el is not None and diagram_el.text:
        # Content may be in CDATA
        text = diagram_el.text.strip()
        if text.startswith("<"):
            return ET.fromstring(text)
        # Try base64-decompressed (standard drawio compression)
        try:
            import base64, gzip
            decoded = base64.b64decode(text)
            decompressed = gzip.decompress(decoded)
            return ET.fromstring(decompressed)
        except Exception:
            pass
    # Fallback: direct model children
    model = raw.find(".//mxGraphModel") or raw.find(".//{*}mxGraphModel")
    if model is not None:
        return model
    return raw


def get_cells(root: ET.Element) -> list[ET.Element]:
    """Return all mxCell elements in the tree."""
    return root.findall(".//{*}mxCell") or root.findall(".//mxCell")


def rect_from_geo(mxgeo: ET.Element | None) -> tuple[float, float, float, float] | None:
    """Extract (x, y, w, h) from an mxGeometry element."""
    if mxgeo is None:
        return None
    x = float(mxgeo.get("x", 0))
    y = float(mxgeo.get("y", 0))
    w = float(mxgeo.get("width", 0))
    h = float(mxgeo.get("height", 0))
    if w == 0 and h == 0:
        return None
    return (x, y, x + w, y + h)


def rects_overlap(a: tuple, b: tuple) -> bool:
    """Check if two rectangles overlap."""
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def parse_style(style_str: str) -> dict:
    """Parse drawio style string into a dict."""
    parts = style_str.split(";")
    result = {}
    for p in parts:
        p = p.strip()
        if "=" in p:
            k, v = p.split("=", 1)
            result[k] = v
        elif p:
            result[p] = True
    return result


def extract_colors(style: dict) -> set[str]:
    """Extract hex color values from a style dict."""
    colors = set()
    for key in ("fillColor", "strokeColor", "fontColor", "gradientColor"):
        val = style.get(key, "").strip().lower()
        if val and val.startswith("#"):
            colors.add(val.upper())
    return colors


def is_within_palette(hex_color: str) -> bool:
    """Check if a hex color is in the approved palette (case-insensitive)."""
    return hex_color.upper() in PALETTE


def extract_font_size(style: dict) -> float | None:
    """Return font size from style dict, or None."""
    val = style.get("fontSize")
    if val:
        try:
            return float(val)
        except ValueError:
            pass
    return None


# ---- Validation Functions ----

def check_overlaps(cells: list[ET.Element]) -> list[str]:
    """Find overlapping vertex geometries."""
    issues = []
    vertices: list[tuple[str, tuple[float, float, float, float]]] = []
    for cell in cells:
        if cell.get("vertex") == "1" or cell.get("vertex") == "true":
            geo = cell.find("{*}mxGeometry") or cell.find("mxGeometry")
            r = rect_from_geo(geo)
            if r:
                cid = cell.get("id", "?")
                vertices.append((cid, r))
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            id_a, ra = vertices[i]
            id_b, rb = vertices[j]
            if rects_overlap(ra, rb):
                issues.append(f"OVERLAP: cell '{id_a}' overlaps cell '{id_b}'")
    return issues


def check_orphan_connectors(cells: list[ET.Element]) -> list[str]:
    """Find edges with missing source or target."""
    issues = []
    all_ids = {cell.get("id") for cell in cells}
    for cell in cells:
        if cell.get("edge") == "1" or cell.get("edge") == "true":
            src = cell.get("source")
            tgt = cell.get("target")
            if src and src not in all_ids:
                issues.append(f"ORPHAN: edge '{cell.get('id')}' has source '{src}' which does not exist")
            if tgt and tgt not in all_ids:
                issues.append(f"ORPHAN: edge '{cell.get('id')}' has target '{tgt}' which does not exist")
    return issues


def check_font_sizes(cells: list[ET.Element]) -> list[str]:
    """Find text elements with font size below minimum."""
    issues = []
    for cell in cells:
        style = parse_style(cell.get("style", ""))
        is_edge = cell.get("edge") == "1" or cell.get("edge") == "true"
        threshold = CONNECTOR_LABEL_MIN if is_edge else MIN_FONT_SIZE
        size = extract_font_size(style)
        if size is not None and size < threshold:
            cid = cell.get("id", "?")
            label = (cell.get("value") or "")[:30]
            issues.append(f"FONT: cell '{cid}' font size {size}pt is below minimum {threshold}pt ('{label}')")
    return issues


def check_color_compliance(cells: list[ET.Element]) -> list[str]:
    """Find colors outside the approved palette."""
    issues = []
    for cell in cells:
        style = parse_style(cell.get("style", ""))
        colors = extract_colors(style)
        for c in colors:
            if not is_within_palette(c):
                cid = cell.get("id", "?")
                issues.append(f"COLOR: cell '{cid}' uses non-palette color {c}")
    return issues


def check_floating_elements(cells: list[ET.Element]) -> list[str]:
    """Find vertex cells that have no parent container."""
    issues = []
    all_ids = {cell.get("id") for cell in cells}
    for cell in cells:
        if cell.get("vertex") == "1" or cell.get("vertex") == "true":
            parent = cell.get("parent")
            if parent and parent in all_ids:
                parent_cell = next((c for c in cells if c.get("id") == parent), None)
                if parent_cell:
                    # If parent is the root (id="0") or the diagram layer (id="1"), skip
                    if parent in ("0", "1"):
                        continue
                    # Check if parent has geometry (i.e., is a container)
                    pgeo = parent_cell.find("{*}mxGeometry") or parent_cell.find("mxGeometry")
                    if pgeo is None:
                        issues.append(f"FLOATING: cell '{cell.get('id')}' has parent '{parent}' which has no geometry (not a container)")
            elif parent not in ("0", "1"):
                issues.append(f"FLOATING: cell '{cell.get('id')}' has unknown parent '{parent}'")
    return issues


# ---- Main ----

def validate_file(path: Path) -> int:
    """Validate a single .drawio file. Returns issue count."""
    try:
        root = parse_drawio(path)
    except Exception as e:
        print(f"PARSE ERROR: {path} — {e}")
        return 1

    cells = get_cells(root)
    if not cells:
        print(f"WARNING: {path} — no mxCell elements found")
        return 0

    all_issues = []
    all_issues.extend(check_overlaps(cells))
    all_issues.extend(check_orphan_connectors(cells))
    all_issues.extend(check_font_sizes(cells))
    all_issues.extend(check_color_compliance(cells))
    all_issues.extend(check_floating_elements(cells))

    if all_issues:
        print(f"\n{path}:")
        for issue in all_issues:
            print(f"  [{issue.split(':')[0]}] {issue}")
        return len(all_issues)
    else:
        print(f"PASS: {path}")
        return 0


def main():
    paths = sys.argv[1:]
    if not paths:
        print("Usage: python validate.py path/to/diagram.drawio [path/to/another.drawio ...]")
        sys.exit(1)

    total_issues = 0
    for pattern in paths:
        for p in Path(".").glob(pattern):
            total_issues += validate_file(p)
        # Also try literal file path
        for p in paths:
            pp = Path(p)
            if pp.exists() and pp.suffix == ".drawio":
                total_issues += validate_file(pp)

    if total_issues > 0:
        print(f"\nFAIL: {total_issues} issue(s) found across all files")
        sys.exit(1)
    else:
        print(f"\nPASS: All files valid")
        sys.exit(0)


if __name__ == "__main__":
    main()
