"""Add two trailing spaces after **🔹...** lines when followed by **🔹...** (markdown hard break)."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def _is_english_fire_line(line: str) -> bool:
    """Match **🔹...** or **N 🔹...** (numbered segment in Roholl notes)."""
    t = line.strip()
    if not t.startswith("**") or "🔹" not in t:
        return False
    return t.endswith("**")


def process(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    for i, line in enumerate(lines):
        stripped_next = lines[i + 1].lstrip() if i + 1 < len(lines) else ""
        if (
            _is_english_fire_line(line)
            and stripped_next.startswith("**🔸")
            and not line.rstrip("\r\n").rstrip().endswith("  ")
        ):
            nl = "\r\n" if line.endswith("\r\n") else ("\n" if line.endswith("\n") else "")
            core = line.rstrip("\r\n").rstrip()
            line = core + "  " + nl
        out.append(line)
    return "".join(out)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("path", type=Path)
    args = p.parse_args()
    path: Path = args.path
    raw = path.read_text(encoding="utf-8")
    path.write_text(process(raw), encoding="utf-8")


if __name__ == "__main__":
    main()
