# -*- coding: utf-8 -*-
"""Generate inline-HTML '炫彩' variant of a reading note (local MD preview). Skips ``` fences."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BOLD_COLORS = [
    "#0d9488",
    "#c2410c",
    "#7c3aed",
    "#2563eb",
    "#db2777",
    "#0891b2",
    "#ca8a04",
]
H2_COLORS = ["#c2410c", "#7c3aed", "#0d9488", "#2563eb", "#be185d", "#0369a1"]


def split_frontmatter(raw: str) -> tuple[str, str]:
    if not raw.startswith("---"):
        return "", raw
    end = raw.find("\n---\n", 4)
    if end < 0:
        return "", raw
    fm_block = raw[4:end]
    body = raw[end + 5 :]
    return fm_block, body


def fm_to_dict(fm_block: str) -> dict[str, str]:
    fm: dict[str, str] = {}
    for line in fm_block.splitlines():
        if line.startswith("tags:") or line.startswith("  - "):
            continue
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm


def collect_chapter_titles(lines: list[str]) -> list[str]:
    inf = False
    out: list[str] = []
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            inf = not inf
            continue
        if inf:
            continue
        if line.startswith("# ") and not line.startswith("## "):
            out.append(line[2:].strip())
    return out


def slug_chapter(i: int) -> str:
    return f"ch-{i}"


def colorize_bolds_line(line: str, idx: list[int]) -> str:
    if "<strong style=" in line:
        return line

    def repl(m: re.Match[str]) -> str:
        inner = m.group(1)
        c = BOLD_COLORS[idx[0] % len(BOLD_COLORS)]
        idx[0] += 1
        inner_esc = (
            inner.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )
        return f'<strong style="color:{c};font-weight:600">{inner_esc}</strong>'

    return re.sub(r"\*\*([^*]+)\*\*", repl, line)


def process_body(body: str, bold_idx: list[int]) -> str:
    lines = body.splitlines()
    ch_idx = [0]
    h2_sub = [0]
    inf = False
    out: list[str] = []

    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            inf = not inf
            out.append(line)
            continue
        if inf:
            out.append(line)
            continue

        if line.startswith("# ") and not line.startswith("## "):
            ch_idx[0] += 1
            title = line[2:].strip()
            hid = slug_chapter(ch_idx[0])
            c = H2_COLORS[(ch_idx[0] - 1) % len(H2_COLORS)]
            title_esc = (
                title.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            out.append(
                f'<h2 id="{hid}" style="color:{c};font-weight:700;margin:1.35em 0 0.5em;'
                f'font-size:1.28em;line-height:1.3;padding-bottom:0.15em;'
                f'border-bottom:2px solid {c}33">{title_esc}</h2>'
            )
            continue

        if line.startswith("## ") and not line.startswith("### "):
            h2_sub[0] += 1
            title = line[3:].strip()
            hid = f"sub-{h2_sub[0]}"
            title_esc = (
                title.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            out.append(
                f'<h3 id="{hid}" style="color:#0c4a6e;font-weight:650;margin:1.05em 0 0.4em;'
                f'font-size:1.08em">{title_esc}</h3>'
            )
            continue

        if line.startswith("### "):
            title = line[4:].strip()
            title_esc = (
                title.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            out.append(
                '<h4 style="color:#334155;font-weight:600;margin:0.95em 0 0.35em;'
                'font-size:1.02em;border-left:4px solid #38bdf8;padding-left:0.55em">'
                f"{title_esc}</h4>"
            )
            continue

        out.append(colorize_bolds_line(line, bold_idx))

    return "\n".join(out)


def hero_html(fm: dict[str, str], chapters: list[str]) -> str:
    title = fm.get("title", "Reading notes")
    title_esc = (
        title.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    src = fm.get("source", "")
    url = fm.get("source_url", "")
    date = fm.get("date", "")
    plain = fm.get("companion_plain", "")

    src_html = (
        f'<a href="{url}" style="color:#4f46e5;font-weight:600">{src}</a>'
        if url
        else f'<span style="color:#4338ca">{src}</span>'
    )

    toc_items = []
    for i, t in enumerate(chapters, start=1):
        c = H2_COLORS[(i - 1) % len(H2_COLORS)]
        tid = slug_chapter(i)
        esc = (
            t.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
        toc_items.append(
            f'<li style="margin:0.25em 0"><a href="#{tid}" style="color:{c};font-weight:600;'
            f'text-decoration:none;border-bottom:1px dotted {c}88">{esc}</a></li>'
        )
    toc = (
        '<h2 id="contents" style="color:#0369a1;font-weight:700;margin:1em 0 0.35em;font-size:1.22em">'
        "目录 · Contents</h2>\n<ul style=\"margin:0.2em 0 1.1em;padding-left:1.2em;line-height:1.75;color:#334155\">"
        + "\n".join(toc_items)
        + "</ul>"
    )

    plain_note = ""
    if plain:
        plain_note = (
            f'<p style="margin:0.6em 0 0;font-size:0.88em;color:#64748b">'
            f"纯 Markdown 原版：<code style=\"background:#f1f5f9;padding:2px 6px;border-radius:4px\">{plain}</code></p>"
        )

    return f"""<h1 style="color:#0f766e;font-weight:700;font-size:1.6em;margin:0.4em 0 0.35em;padding-bottom:0.2em;border-bottom:3px solid #2dd4bf;line-height:1.25">{title_esc}</h1>

<blockquote style="margin:0.65em 0 0.85em;padding:12px 16px;border-left:5px solid #6366f1;background:linear-gradient(90deg,#ecfdf5 0%,#f8fafc 60%);color:#134e4a;border-radius:0 10px 10px 0"><p style="margin:0;line-height:1.55"><strong>Source:</strong> {src_html} · <strong>Date:</strong> <span style="color:#0e7490">{date}</span></p></blockquote>

<p style="margin:0 0 0.85em;font-size:0.9em;color:#64748b;line-height:1.5"><span style="color:#f59e0b">●</span> <span style="color:#475569">章节标题分色；<code>**加粗**</code> 已轮换为青绿 / 琥珀 / 紫 / 蓝 / 玫红 / cyan / 金（代码块内除外）。</span></p>
{plain_note}
{toc}
<hr style="border:none;border-top:1px solid #e2e8f0;margin:1.2em 0" />
"""


def inject_yaml_fields(fm_block: str, companion_plain: str) -> str:
    if "colored_html:" in fm_block:
        return fm_block
    add = f"""colored_html: 2026-03-21
companion_plain: {companion_plain}
archived_note: 炫彩 HTML 内联样式版（本地 MD 预览友好）；GitHub 网页可能弱化样式。
"""
    return fm_block.rstrip() + "\n" + add


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument(
        "--companion-name",
        required=True,
        help="Plain-note filename for hero link",
    )
    args = p.parse_args()
    raw = args.input.read_text(encoding="utf-8")
    fm_block, body = split_frontmatter(raw)
    if not fm_block:
        print("No YAML frontmatter", file=sys.stderr)
        sys.exit(1)
    fm_block2 = inject_yaml_fields(fm_block, args.companion_name)
    fm = fm_to_dict(fm_block2)
    fm["companion_plain"] = args.companion_name

    chapters = collect_chapter_titles(body.splitlines())
    hero = hero_html(fm, chapters)
    bold_idx = [0]
    processed = process_body(body, bold_idx)

    out = f"---\n{fm_block2}\n---\n{hero}{processed}\n"
    args.output.write_text(out, encoding="utf-8")
    print(f"Wrote {args.output} ({len(out)} chars)", file=sys.stderr)


if __name__ == "__main__":
    main()
