#!/usr/bin/env python3
"""Apply readable gradient-text HTML to a fixed line block or whole paragraph."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


PALETTES: dict[str, str] = {
    "readable": (
        "linear-gradient(90deg, #2563eb 0%, #0891b2 28%, "
        "#7c3aed 58%, #db2777 82%, #2563eb 100%)"
    ),
    "soft": (
        "linear-gradient(90deg, #3b82f6 0%, #14b8a6 30%, "
        "#8b5cf6 62%, #ec4899 86%, #3b82f6 100%)"
    ),
    "vivid": (
        "linear-gradient(90deg, #1d4ed8 0%, #0ea5e9 24%, "
        "#7c3aed 54%, #e11d48 80%, #1d4ed8 100%)"
    ),
}


def strip_markdown_emphasis(text: str) -> str:
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text)


def block_already_wrapped(lines: list[str], idx: int) -> bool:
    current = lines[idx].lstrip()
    if current.startswith("<p ") or current.startswith("<div "):
        return True

    for back in range(max(0, idx - 2), idx):
        if 'data-toolbox-gradient-text="' in lines[back]:
            return True
    return False


def find_candidate_indexes(lines: list[str], needle: str) -> list[int]:
    hits: list[int] = []
    for idx, line in enumerate(lines):
        if needle in line and not block_already_wrapped(lines, idx):
            hits.append(idx)
    return hits


def build_gradient_block(
    raw_lines: list[str],
    *,
    palette_name: str,
    font_weight: int,
) -> list[str]:
    gradient = PALETTES[palette_name]
    out = [
        (
            f'<div data-toolbox-gradient-text="{palette_name}" '
            'style="margin: 0.5em 0; line-height: 1.7;">'
        )
    ]

    for raw in raw_lines:
        clean = html.escape(strip_markdown_emphasis(raw.strip()))
        out.append(
            '<p style="margin: 0.18em 0; '
            f'font-weight: {font_weight}; '
            f"background: {gradient}; "
            '-webkit-background-clip: text; '
            'background-clip: text; '
            'color: transparent; '
            '-webkit-text-fill-color: transparent;">'
            f"{clean}</p>"
        )

    out.append("</div>")
    return out


def detect_block_end(lines: list[str], start: int, line_count: int, until_blank: bool) -> int:
    if until_blank:
        end = start
        while end < len(lines) and lines[end].strip():
            end += 1
        return end
    return start + line_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Wrap matching lines in a Markdown file with eye-friendly gradient text HTML."
        )
    )
    parser.add_argument("file", type=Path, help="Markdown file to edit in place.")
    parser.add_argument(
        "--contains",
        required=True,
        help="Unique text used to locate the first target line.",
    )
    parser.add_argument(
        "--line-count",
        type=int,
        default=1,
        help="Number of consecutive lines to wrap starting from the matched line.",
    )
    parser.add_argument(
        "--until-blank",
        action="store_true",
        help="Wrap from the matched line until the next blank line.",
    )
    parser.add_argument(
        "--match-index",
        type=int,
        default=1,
        help="1-based index if the --contains text appears multiple times.",
    )
    parser.add_argument(
        "--palette",
        choices=sorted(PALETTES.keys()),
        default="readable",
        help="Gradient palette to apply.",
    )
    parser.add_argument(
        "--font-weight",
        type=int,
        default=700,
        help="CSS font-weight for the generated paragraph lines.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.line_count < 1:
        print("--line-count must be >= 1", file=sys.stderr)
        sys.exit(1)

    if args.match_index < 1:
        print("--match-index must be >= 1", file=sys.stderr)
        sys.exit(1)

    if not args.file.exists():
        print(f"File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    raw = args.file.read_text(encoding="utf-8")
    lines = raw.splitlines()
    hits = find_candidate_indexes(lines, args.contains)

    if not hits:
        print("No unwrapped match found for --contains text.", file=sys.stderr)
        sys.exit(1)

    if args.match_index > len(hits):
        print(
            f"--match-index {args.match_index} exceeds available matches ({len(hits)}).",
            file=sys.stderr,
        )
        sys.exit(1)

    start = hits[args.match_index - 1]
    end = detect_block_end(lines, start, args.line_count, args.until_blank)

    if end > len(lines):
        print("Target block exceeds file length.", file=sys.stderr)
        sys.exit(1)

    block = lines[start:end]
    if not block:
        print("Resolved target block is empty.", file=sys.stderr)
        sys.exit(1)

    if any(not line.strip() for line in block):
        print("Target block contains blank lines; narrow the match or line count.", file=sys.stderr)
        sys.exit(1)

    replacement = build_gradient_block(
        block,
        palette_name=args.palette,
        font_weight=args.font_weight,
    )

    new_lines = lines[:start] + replacement + lines[end:]
    output = "\n".join(new_lines)
    if raw.endswith("\n"):
        output += "\n"

    args.file.write_text(output, encoding="utf-8")
    print(
        f"Updated {args.file} at line {start + 1} "
        f"with palette={args.palette} "
        f"{'until_blank' if args.until_blank else f'line_count={args.line_count}'}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
