# -*- coding: utf-8 -*-
"""为 Mythos 双语稿添加 🔹 英文 / 🔸 中文，并将符号置于 # / 列表 / 脚注标号之后（不破坏 Markdown）。"""
from __future__ import annotations

import re
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / (
    "reading/notes/technology/ai-digital/anthropic-claude/"
    "030-Assessing-Claude-Mythos-Preview-Cybersecurity-Anthropic-Bilingual-Reading-Notes-2026-04-08.md"
)

# 当前 🔹🔸；兼容旧版 🔴🔵 以便去重后重跑
EMOJI_LEAD = re.compile(
    r"^(\s*)([\U0001F534\U0001F535\U0001F538\U0001F539\U0001F53B])\s+"
)


def strip_lead_emoji(line: str) -> str:
    m = EMOJI_LEAD.match(line)
    if m:
        return m.group(1) + line[m.end() :]
    return line


def apply_markers(lines: list[str]) -> list[str]:
    out: list[str] = []
    in_frontmatter = False
    frontmatter_done = False
    in_code = False
    prev_was_english = False

    for raw in lines:
        if not frontmatter_done:
            if raw.startswith("---"):
                if in_frontmatter:
                    frontmatter_done = True
                    in_frontmatter = False
                    out.append(raw)
                    prev_was_english = False
                    continue
                in_frontmatter = True
            if not frontmatter_done:
                out.append(raw)
                prev_was_english = False
                continue

        stripped = raw.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            out.append(raw)
            prev_was_english = False
            continue

        if in_code:
            out.append(raw)
            prev_was_english = False
            continue

        body = strip_lead_emoji(raw)
        no_nl = body.rstrip("\n\r")
        is_empty = no_nl.strip() == ""

        if is_empty:
            out.append(body)
            prev_was_english = False
            continue

        ends_hardbreak = len(no_nl) >= 2 and no_nl.endswith("  ")

        if ends_hardbreak:
            if not no_nl.lstrip().startswith(("🔹", "🔸", "🔴", "🔵")):
                prefix = body[: len(body) - len(body.lstrip())]
                rest = body[len(prefix) :]
                out.append(f"{prefix}🔹 {rest}")
            else:
                out.append(body)
            prev_was_english = True
            continue

        if prev_was_english:
            if not no_nl.lstrip().startswith(("🔹", "🔸", "🔴", "🔵")):
                prefix = body[: len(body) - len(body.lstrip())]
                rest = body[len(prefix) :]
                out.append(f"{prefix}🔸 {rest}")
            else:
                out.append(body)
            prev_was_english = False
            continue

        out.append(body)
        prev_was_english = False

    return out


def reorder_markdown_syntax(text: str) -> str:
    t = text
    t = re.sub(r"^🔹 (#+\s)", r"\1🔹 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔸 (#+\s)", r"\1🔸 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔹 (\d+\.\s)", r"\1🔹 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔸 (\d+\.\s)", r"\1🔸 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔹 (\*\s)", r"\1🔹 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔸 (\*\s)", r"\1🔸 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔹 (\[\d+\]\s)", r"\1🔹 ", t, flags=re.MULTILINE)
    t = re.sub(r"^🔸 (\[\d+\]\s)", r"\1🔸 ", t, flags=re.MULTILINE)
    return t


def main() -> None:
    raw_lines = PATH.read_text(encoding="utf-8").splitlines(keepends=True)
    out_lines = apply_markers(raw_lines)
    new_text = "".join(out_lines)
    new_text = reorder_markdown_syntax(new_text)
    PATH.write_text(new_text, encoding="utf-8")
    print("OK:", PATH)


if __name__ == "__main__":
    main()
