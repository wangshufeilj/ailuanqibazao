# -*- coding: utf-8 -*-
"""Mythos 双语稿：章节空行、重点术语加粗（跳过 fenced code 与行内 `code`）。"""
from __future__ import annotations

import re
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / (
    "reading/notes/technology/ai-digital/anthropic-claude/"
    "030-Assessing-Claude-Mythos-Preview-Cybersecurity-Anthropic-Bilingual-Reading-Notes-2026-04-08.md"
)


def add_section_spacing(text: str) -> str:
    text = re.sub(r"([^\n])\n(### 🔹)", r"\1\n\n\2", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def bold_plain_segment(chunk: str) -> str:
    """对一段不含围栏代码的文本加粗术语；保留行内反引号块不改动。"""
    pieces = re.split(r"(`[^`]*`)", chunk)
    out: list[str] = []
    for i, p in enumerate(pieces):
        if i % 2 == 1:
            out.append(p)
            continue
        s = p
        # 英文（顺序：长短语优先）
        subs_en = [
            (r"(?<!\*)\bClaude Mythos Preview\b(?!\*)", "**Claude Mythos Preview**"),
            (r"(?<!\*)\bProject Glasswing\b(?!\*)", "**Project Glasswing**"),
            (r"(?<!\*)\bOpus 4\.6\b(?!\*)", "**Opus 4.6**"),
            (r"(?<!\*)\bSonnet 4\.6\b(?!\*)", "**Sonnet 4.6**"),
            (r"(?<!\*)\bCVE-\d{4}-\d+\b(?!\*)", lambda m: f"**{m.group(0)}**"),
            (r"(?<![*`/])\bzero-day\b(?![*`])", "**zero-day**"),
            (r"(?<![*`/])\bN-day\b(?![*`])", "**N-day**"),
            (r"(?<!Claude )(?<!\*)\bMythos Preview\b(?!\*)", "**Mythos Preview**"),
        ]
        for pat, repl in subs_en:
            if callable(repl):
                s = re.sub(pat, repl, s)
            else:
                s = re.sub(pat, repl, s)
        zh_pairs = [
            ("分水岭时刻", "**分水岭时刻**"),
            ("大规模协调防御行动", "**大规模协调防御行动**"),
            ("协调漏洞披露", "**协调漏洞披露**"),
            ("零日漏洞", "**零日漏洞**"),
            ("N 日漏洞", "**N 日漏洞**"),
        ]
        for old, new in zh_pairs:
            if old in s and new not in s:
                s = s.replace(old, new)
        out.append(s)
    return "".join(out)


def process_fenced(text: str) -> str:
    parts = re.split(r"(```[\s\S]*?```)", text)
    out: list[str] = []
    for i, p in enumerate(parts):
        if p.startswith("```") and len(p) >= 3 and p.strip().endswith("```"):
            out.append(p)
        else:
            out.append(bold_plain_segment(p))
    return "".join(out)


def split_frontmatter(raw: str) -> tuple[str, str]:
    if not raw.startswith("---\n"):
        return "", raw
    idx = raw.find("\n---\n", 4)
    if idx == -1:
        return "", raw
    return raw[: idx + 5], raw[idx + 5 :]


def main() -> None:
    raw = PATH.read_text(encoding="utf-8")
    fm, body = split_frontmatter(raw)
    body = add_section_spacing(body)
    body = process_fenced(body)
    PATH.write_text(fm + body, encoding="utf-8")
    print("OK:", PATH)


if __name__ == "__main__":
    main()
