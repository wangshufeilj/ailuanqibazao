# -*- coding: utf-8 -*-
"""从 026 双语 Markdown 生成约 20% 关键词七彩炫彩 HTML（预设 A）。"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reading/notes/technology/ai-digital/026-Lex-Fridman-447-Cursor-Team-Bilingual-Transcript-2026-04-05.md"
OUT = ROOT / "reading/notes/technology/ai-digital/026-Lex-Fridman-447-Cursor-Team-Bilingual-Transcript-rainbow-2026-04-05.html"

TARGET_RATIO = 0.20

EN_KEYWORDS = sorted(
    {
        "speculative edits",
        "speculative decoding",
        "Shadow Workspace",
        "language server protocol",
        "language server",
        "process reward model",
        "outcome reward model",
        "formal verification",
        "homomorphic encryption",
        "test time compute",
        "scaling laws",
        "GitHub Copilot",
        "Cursor Tab",
        "multi-query attention",
        "multi-head attention",
        "multi-latent",
        "approximate nearest neighbors",
        "write-ahead log",
        "KV cache",
        "TTFT",
        "SWE-Bench",
        "Merkle tree",
        "PlanetScale",
        "RLAIF",
        "RLHF",
        "Anthropic",
        "OpenAI",
        "DeepSeek",
        "VS Code",
        "code base",
        "codebase",
        "embeddings",
        "embedding",
        "inference",
        "pre-training",
        "post-training",
        "fine-tuning",
        "distillation",
        "transformer",
        "attention heads",
        "attention",
        "benchmark",
        "benchmarks",
        "frontier model",
        "frontier models",
        "language model",
        "language models",
        "chain of thought",
        "agentic",
        "programming",
        "programmer",
        "iteration",
        "latency",
        "bandwidth",
        "parallelism",
        "CUDA",
        "GPU",
        "GPUs",
        "tokens",
        "prompt",
        "retrieval",
        "rerank",
        "Apply",
        "Copilot",
        "Cursor",
        "Sonnet",
        "Claude",
        "o1",
        "IMO",
        "AGI",
        "LSP",
        "MOE",
        "MQA",
        "GQA",
        "MLA",
        "SSM",
        "Chinchilla",
        "Gemma",
        "Vim",
        "Neovim",
        "TypeScript",
        "Rust",
        "Node.js",
        "Jupyter",
        "Stripe",
        "AWS",
        "Linux",
        "YouTube",
        "Reddit",
        "Perplexity",
    },
    key=len,
    reverse=True,
)

ZH_KEYWORDS = sorted(
    {
        "混合专家",
        "键值缓存",
        "语言服务器",
        "形式化验证",
        "全同态加密",
        "测试时算力",
        "推理时算力",
        "缩放定律",
        "人类反馈",
        "强化学习",
        "合成数据",
        "知识蒸馏",
        "代码库",
        "上下文",
        "嵌入向量",
        "向量数据库",
        "近似最近邻",
        "预训练",
        "后训练",
        "指令微调",
        "思维链",
        "智能体",
        "基准测试",
        "前沿模型",
        "大语言模型",
        "语言模型",
        "程序员",
        "编程",
        "迭代",
        "延迟",
        "带宽",
        "并行",
        "令牌",
        "提示词",
        "检索",
        "注意力",
        "变换器",
        "人机协作",
        "人机系统",
        "低熵击键",
        "推测解码",
        "后台运行",
        "分支数据库",
        "菲尔兹奖",
        "缩放",
        "蒸馏",
        "推理",
        "对齐",
        "沙箱",
        "默克尔",
        "差分",
        "迁移",
        "调试",
        "规约",
        "算力",
        "参数",
        "编辑器",
        "扩展",
    },
    key=len,
    reverse=True,
)


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) >= 3:
        return parts[2].lstrip("\n")
    return text


def strip_markdown_links(text: str) -> str:
    """[锚文本](任意网址) → 仅保留锚文本。"""
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: m.group(1), text)


def strip_bare_http_urls(text: str) -> str:
    """删除裸露的 http(s)://…（不含 Markdown 括号包裹）。"""

    def bare_repl(_m: re.Match[str]) -> str:
        return ""

    t = re.sub(r"https?://[^\s\]\)]+", bare_repl, text)
    return re.sub(r" {2,}", " ", t)


def strip_plain_urls(text: str) -> str:
    """正文用：去掉 Markdown 链接与裸露网址。"""
    return strip_bare_http_urls(strip_markdown_links(text)).strip()


def md_link_html(label: str, url: str) -> str:
    """不输出任何超链接，仅保留锚文本（与 strip_plain_urls 一致）。"""
    return html.escape(label)


def is_english_dialogue(line: str) -> bool:
    return bool(
        re.match(
            r"^(?:(?:Lex|Aman|Arvid|Michael|Sualeh) \[\([^)]+\)\]\([^)]+\)|\[\([^)]+\)\]\([^)]+\))\s+",
            line,
        )
    )


def is_chinese_dialogue(line: str) -> bool:
    if "（" not in line[:60]:
        return False
    return bool(re.search(r"[\u4e00-\u9fff]", line))


def dialogue_plain_len(line: str) -> int:
    t = re.sub(
        r"^((?:Lex|Aman|Arvid|Michael|Sualeh) \[\([^)]+\)\]\([^)]+\)|\[\([^)]+\)\]\([^)]+\))\s+",
        "",
        line,
    )
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return len(t)


def split_prefix_body(line: str) -> tuple[str | None, str]:
    m = re.match(
        r"^((?:Lex|Aman|Arvid|Michael|Sualeh) \[\([^)]+\)\]\([^)]+\)|\[\([^)]+\)\]\([^)]+\))\s+(.*)$",
        line,
        re.DOTALL,
    )
    if m:
        return m.group(1), m.group(2)
    return None, line


def intervals_overlap(intervals: list[tuple[int, int]], start: int, end: int) -> bool:
    for a, b in intervals:
        if not (end <= a or start >= b):
            return True
    return False


def merge_intervals(iv: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not iv:
        return []
    iv = sorted(iv)
    out: list[tuple[int, int]] = [iv[0]]
    for s, e in iv[1:]:
        ps, pe = out[-1]
        if s <= pe:
            out[-1] = (ps, max(pe, e))
        else:
            out.append((s, e))
    return out


def gap_ranges(n: int, merged: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not merged:
        return [(0, n)] if n > 0 else []
    gaps: list[tuple[int, int]] = []
    pos = 0
    for s, e in merged:
        if pos < s:
            gaps.append((pos, s))
        pos = max(pos, e)
    if pos < n:
        gaps.append((pos, n))
    return gaps


def _fallback_spans(seg: str, blocked: list[tuple[int, int]], budget: int, used: int) -> list[tuple[int, int]]:
    """在未被关键词覆盖的间隙内，用较长英文词、中文词块补足高亮预算。"""
    merged = merge_intervals(blocked)
    cands: list[tuple[int, int, int]] = []
    for gs, ge in gap_ranges(len(seg), merged):
        sub = seg[gs:ge]
        for m in re.finditer(r"[A-Za-z]{5,}", sub):
            cands.append((m.end() - m.start(), gs + m.start(), gs + m.end()))
        for m in re.finditer(r"[\u4e00-\u9fff]{2,}", sub):
            cands.append((m.end() - m.start(), gs + m.start(), gs + m.end()))
    cands.sort(key=lambda x: -x[0])
    extra: list[tuple[int, int]] = []
    cur = list(blocked)
    u = used
    for _ln, s, e in cands:
        if u >= budget:
            break
        ln = e - s
        if ln <= 0 or u + ln > budget:
            continue
        if intervals_overlap(cur, s, e):
            continue
        cur.append((s, e))
        extra.append((s, e))
        u += ln
    return extra


def highlight_plain_segments(plain: str, keywords: list[str], budget: int, color_idx: int) -> tuple[str, int, int]:
    """plain 可含 [text](url)；仅在非链接片段内匹配关键词。返回 (html, 高亮字符数, 下一个颜色索引)。"""
    plain = strip_plain_urls(plain)
    if budget <= 0 or not plain.strip():
        return _md_to_html(plain), 0, color_idx

    pieces: list[str] = []
    last = 0
    used = 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", plain):
        if m.start() > last:
            seg = plain[last : m.start()]
            h, u, color_idx = _highlight_segment(seg, keywords, budget - used, color_idx)
            pieces.append(h)
            used += u
        pieces.append(md_link_html(m.group(1), m.group(2)))
        last = m.end()
    if last < len(plain):
        h, u, color_idx = _highlight_segment(plain[last:], keywords, budget - used, color_idx)
        pieces.append(h)
        used += u
    return "".join(pieces), used, color_idx


def _highlight_segment(seg: str, keywords: list[str], budget: int, color_idx: int) -> tuple[str, int, int]:
    if budget <= 0 or not seg:
        return html.escape(seg), 0, color_idx
    intervals: list[tuple[int, int]] = []
    picked: list[tuple[int, int]] = []
    used = 0
    for kw in keywords:
        if used >= budget:
            break
        for m in re.finditer(re.escape(kw), seg, flags=re.IGNORECASE):
            s, e = m.span()
            ln = e - s
            if ln <= 0 or intervals_overlap(intervals, s, e):
                continue
            if used + ln > budget:
                continue
            intervals.append((s, e))
            picked.append((s, e))
            used += ln
    if used < budget:
        for s, e in _fallback_spans(seg, picked, budget, used):
            picked.append((s, e))
            intervals.append((s, e))
            used += e - s
            if used >= budget:
                break
    if not picked:
        return html.escape(seg), 0, color_idx
    picked.sort(key=lambda x: x[0])
    total = sum(e - s for s, e in picked)
    out: list[str] = []
    pos = 0
    for s, e in picked:
        if pos < s:
            out.append(html.escape(seg[pos:s]))
        out.append(f'<span class="kw kw-{color_idx % 7}">{html.escape(seg[s:e])}</span>')
        color_idx += 1
        pos = e
    if pos < len(seg):
        out.append(html.escape(seg[pos:]))
    return "".join(out), total, color_idx


def _md_to_html(s: str) -> str:
    """无链接时的转义。"""

    def repl(m: re.Match[str]) -> str:
        return md_link_html(m.group(1), m.group(2))

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, html.escape(s))


def collect_pairs(body: str) -> tuple[list[tuple[str, str | None]], int]:
    lines = body.splitlines()
    pairs: list[tuple[str, str | None]] = []
    total = 0
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## ") or not ln.strip():
            i += 1
            continue
        if is_english_dialogue(ln):
            total += dialogue_plain_len(ln)
            zh: str | None = None
            if i + 1 < len(lines) and is_chinese_dialogue(lines[i + 1]):
                zh = lines[i + 1]
                total += dialogue_plain_len(zh)
                i += 2
            else:
                i += 1
            pairs.append((ln, zh))
            continue
        i += 1
    return pairs, total


def render_one_pair(
    en_line: str,
    zh_line: str | None,
    pair_budget: int,
    color_idx: int,
) -> tuple[str, int, int]:
    """返回 (pair 的 div HTML, 本对高亮字符数, 下一个颜色索引)。"""
    pref, en_body = split_prefix_body(en_line)
    zplain = re.sub(
        r"^(?:Lex|Aman|Arvid|Michael|Sualeh)?（[0-9:：]+）\s*",
        "",
        zh_line or "",
    )
    elen = max(1, len(en_body))
    zlen = max(1, len(zplain))
    en_share = elen / (elen + zlen)
    en_budget = int(pair_budget * en_share)
    zh_budget = pair_budget - en_budget

    en_html, u1, color_idx = highlight_plain_segments(en_body, EN_KEYWORDS, en_budget, color_idx)
    if pref:
        pref_vis = strip_plain_urls(pref)
        en_full = f'<span class="prefix">{html.escape(pref_vis)}</span> {en_html}'
    else:
        en_full = en_html

    zh_full = ""
    u2 = 0
    if zh_line:
        zh_html, u2, color_idx = highlight_plain_segments(zplain, ZH_KEYWORDS, zh_budget, color_idx)
        zh_full = zh_html

    parts = ['<div class="pair">\n', f'<p class="tri-en">{en_full}</p>\n']
    if zh_full:
        parts.append(f'<p class="tri-zh">{zh_full}</p>\n')
    parts.append("</div>\n")
    return "".join(parts), u1 + u2, color_idx


def build_html() -> str:
    raw = SRC.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)
    pairs, total_plain = collect_pairs(body)
    global_budget = max(1, int(total_plain * TARGET_RATIO))

    chunks: list[str] = []
    chunks.append("<!DOCTYPE html>\n<html lang=\"zh-Hans\">\n<head>\n")
    chunks.append('<meta charset="utf-8">\n')
    chunks.append("<title>Lex #447 · 中英双语重点炫彩（约20%）</title>\n")
    chunks.append(
        """<style>
body{font-family:system-ui,Segoe UI,Roboto,\"Noto Sans SC\",sans-serif;background:#f3f6f7;color:#5a6570;margin:0;padding:24px;line-height:1.55;max-width:920px;margin-left:auto;margin-right:auto;}
h1{font-size:1.35rem;margin-bottom:8px;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,\"Liberation Mono\",\"Courier New\",monospace;background:#e0e5e9;padding:2px 6px;border-radius:4px;font-size:0.85em;word-break:break-all;}
.note{font-size:0.9rem;color:#546e7a;margin-bottom:20px;line-height:1.8;}
.pair{border-left:3px solid #cfd8dc;padding-left:12px;margin:14px 0;}
.tri-en,.tri-zh{color:#5a6570;margin:6px 0;}
.prefix{white-space:nowrap;font-weight:600;color:#5a6570;}
h2{color:#37474f;font-size:1.05rem;margin-top:28px;margin-bottom:12px;border-bottom:1px solid #eceff1;padding-bottom:4px;}
.kw{font-weight:700;}
.kw-0{color:#d32f2f;}
.kw-1{color:#e65100;}
.kw-2{color:#f57f17;}
.kw-3{color:#2e7d32;}
.kw-4{color:#00838f;}
.kw-5{color:#1565c0;}
.kw-6{color:#6a1b9a;}
a{color:#1565c0;}
.stats{font-size:0.85rem;color:#78909c;margin-top:24px;padding:12px;background:#eceff1;border-radius:8px;}
</style>\n</head>\n<body>\n"""
    )

    chunks.append(
        "<h1>Lex Fridman #447 — Cursor 团队（中英对照 · 约20%重点 · 单词轮换色）</h1>\n"
    )
    chunks.append(
        '<p class="note">重点词按<strong>红→橙→黄→绿→青→蓝→紫</strong>顺序逐个单色轮换。'
        ' 思路参考 <code>toolbox/workflows/full-trilingual-keyword-rainbow-on-white.md</code>。'
        " 源稿：Lex Fridman 官网文字稿；同目录 <code>026-Lex-Fridman-447-Cursor-Team-Bilingual-Transcript-2026-04-05.md</code>。</p>\n"
    )

    pair_lens: list[int] = []
    for en_line, zh_line in pairs:
        pl = dialogue_plain_len(en_line)
        if zh_line:
            pl += dialogue_plain_len(zh_line)
        pair_lens.append(max(1, pl))

    pair_chunks: list[str] = []
    spent = 0
    color_idx = 0
    for (en_line, zh_line), plen in zip(pairs, pair_lens):
        pair_budget = max(0, int(global_budget * plen / total_plain))
        html_block, u, color_idx = render_one_pair(en_line, zh_line, pair_budget, color_idx)
        spent += u
        pair_chunks.append(html_block)

    lines = body.splitlines()
    p_idx = 0
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## ") and "Table of Contents" not in ln:
            chunks.append(f"<h2>{html.escape(ln[3:].strip())}</h2>\n")
            i += 1
            continue
        if not ln.strip():
            i += 1
            continue
        if is_english_dialogue(ln):
            if p_idx >= len(pair_chunks):
                i += 1
                continue
            _en, zh_line = pairs[p_idx]
            chunks.append(pair_chunks[p_idx])
            p_idx += 1
            i += 1
            if zh_line and i < len(lines) and lines[i] == zh_line:
                i += 1
            continue
        i += 1

    if p_idx < len(pair_chunks):
        for j in range(p_idx, len(pair_chunks)):
            chunks.append(pair_chunks[j])

    ratio = (spent / total_plain * 100) if total_plain else 0
    chunks.append(
        f'<p class="stats">可见字符总计约 <strong>{total_plain}</strong>；'
        f'炫彩覆盖约 <strong>{spent}</strong> 字（<strong>{ratio:.1f}%</strong>），目标约 <strong>{TARGET_RATIO:.0%}</strong>。</p>\n'
    )
    chunks.append("</body>\n</html>\n")
    return "".join(chunks)


def main() -> None:
    s = build_html()
    OUT.write_text(s, encoding="utf-8")
    print(f"OK {OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()
