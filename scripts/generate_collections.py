#!/usr/bin/env python3
"""
收藏条目同步脚本：扫描含 starred: true 的 Markdown 文件，
在顶层 collections/ 目录下生成/更新引用条目，保护用户手写的「收藏理由」段落。
"""

from pathlib import Path
import re
from datetime import date

# 项目根目录（脚本所在目录的上一级）
PROJECT_ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS_DIR = PROJECT_ROOT / "collections"

# 需要扫描的顶层目录（含 starred 的文件所在位置）
SCAN_DIRS = [
    "articles",
    "news",
    "research",
    "tutorials",
    "reference",
    "chinese-documents",
    "social",
    "reading",
    "creative",
]

# 跳过的目录名
SKIP_DIRS = {".git", ".cursor", "node_modules", "collections", "generated", "inbox", "images", "videos", "data", "audio"}


def slugify(text: str, max_len: int = 30) -> str:
    """将文本转为可用作文件名的短标识。"""
    if not text or not text.strip():
        return "untitled"
    # 取括号前部分（如「新华社 (Xinhua)」→「新华社」）
    text = re.split(r"\s*[(\（]\s*", text.strip())[0]
    # 替换非法字符为连字符
    text = re.sub(r'[<>:"/\\|?*\s]+', "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_len] if len(text) > max_len else text or "untitled"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """解析 YAML frontmatter，返回 (frontmatter_dict, body)。"""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return {}, content
    fm_str, body = match.groups()
    fm = {}
    for line in fm_str.split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            key, _, val = line.partition(":")
            fm[key.strip().lower()] = val.strip().strip("'\"").strip('"')
    return fm, body


def get_frontmatter_str(fm: dict) -> str:
    """将字典转回 frontmatter 字符串。"""
    lines = []
    for k, v in fm.items():
        if v is not None and v != "":
            lines.append(f"{k}: {v}")
    return "\n".join(lines)


def extract_starred_files() -> list[tuple[Path, dict]]:
    """扫描项目内所有含 starred: true 的 .md 文件。"""
    starred = []
    for dir_name in SCAN_DIRS:
        base = PROJECT_ROOT / dir_name
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            # 跳过在 skip 目录中的
            if any(part in SKIP_DIRS for part in path.relative_to(PROJECT_ROOT).parts):
                continue
            try:
                text = path.read_text(encoding="utf-8")
                fm, _ = parse_frontmatter(text)
                if fm.get("starred") in ("true", True):
                    starred.append((path, fm))
            except Exception:
                continue
    return starred


def get_existing_entries() -> dict[str, Path]:
    """获取 collections/ 中已有条目：source_path -> 条目路径。"""
    mapping = {}
    if not COLLECTIONS_DIR.exists():
        return mapping
    for path in COLLECTIONS_DIR.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(text)
            sp = fm.get("source_path")
            if sp:
                # source_path 可能为相对路径，统一用正斜杠
                key = Path(sp).as_posix()
                mapping[key] = path
        except Exception:
            continue
    return mapping


def get_next_sequence() -> int:
    """获取 collections 目录下下一个序号。"""
    if not COLLECTIONS_DIR.exists():
        return 1
    max_seq = 0
    for path in COLLECTIONS_DIR.glob("*.md"):
        m = re.match(r"^(\d{3})-", path.name)
        if m:
            max_seq = max(max_seq, int(m.group(1)))
    return max_seq + 1


def create_or_update_entry(
    source_path: Path,
    fm: dict,
    existing_path: Path | None,
    next_seq: int,
) -> Path:
    """
    创建或更新收藏条目。仅更新 frontmatter，保留用户手写的正文（收藏理由）。
    """
    rel_path = source_path.relative_to(PROJECT_ROOT)
    source_path_key = rel_path.as_posix()

    title = fm.get("title") or source_path.stem
    source = fm.get("source") or ""
    starred_date = fm.get("starred_date") or date.today().isoformat()
    category = fm.get("category") or ""

    title_slug = slugify(title)
    source_slug = slugify(source, 15)

    if existing_path:
        try:
            content = existing_path.read_text(encoding="utf-8")
            _, body = parse_frontmatter(content)
        except Exception:
            body = ""
        entry_path = existing_path
    else:
        body = "\n\n## 收藏理由 / 个人备注\n\n"
        filename = f"{next_seq:03d}-{title_slug}-{source_slug}-{starred_date}.md"
        entry_path = COLLECTIONS_DIR / filename

    new_fm = {
        "title": f"{title}（精选）",
        "source_path": source_path_key,
        "source": source,
        "starred_date": starred_date,
        "category": category,
    }

    new_content = f"---\n{get_frontmatter_str(new_fm)}\n---\n{body}"
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(new_content, encoding="utf-8")
    return entry_path


def main() -> None:
    COLLECTIONS_DIR.mkdir(parents=True, exist_ok=True)

    starred_list = extract_starred_files()
    existing = get_existing_entries()

    # 用于生成新条目的序号
    next_seq = get_next_sequence()

    # 当前 starred 对应的 source_path
    current_source_paths = set()

    for source_path, fm in starred_list:
        rel = source_path.relative_to(PROJECT_ROOT)
        key = rel.as_posix()
        current_source_paths.add(key)

        existing_path = existing.get(key)
        create_or_update_entry(source_path, fm, existing_path, next_seq)
        if not existing_path:
            next_seq += 1

    # 移除已取消收藏的条目
    for sp, entry_path in list(existing.items()):
        if sp not in current_source_paths:
            try:
                entry_path.unlink()
            except Exception:
                pass


if __name__ == "__main__":
    main()
