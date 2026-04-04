#!/usr/bin/env python3
"""修复仓库内指向旧路径的链接引用"""

from pathlib import Path
import re

REPO_ROOT = Path("d:/AI驱动整理乱七八糟")

def parse_migration_report(report_path: Path) -> dict:
    """解析迁移报告，返回 old_name -> new_path 映射（使用正斜杠）"""
    text = report_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    name_to_new = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and not line.startswith('->') and not line.startswith('旧路径'):
            old = line.replace('\\', '/')
            if i + 1 < len(lines) and lines[i+1].strip().startswith('->'):
                new = lines[i+1].strip()[3:].strip().replace('\\', '/')
                # 提取旧文件名（用于匹配时）
                old_name = old.split('/')[-1]
                # 获取不含序号前缀的文件名（用于匹配重编号后的情况）
                # 实际上我们用完整旧路径进行匹配替换
                name_to_new[old] = new
                i += 2
                continue
        i += 1
    return name_to_new


def fix_links_in_file(file_path: Path, path_map: dict) -> int:
    """替换文件中的旧路径，返回替换次数"""
    try:
        text = file_path.read_text(encoding='utf-8')
    except Exception:
        return 0

    original = text
    count = 0
    for old, new in path_map.items():
        if old in text:
            text = text.replace(old, new)
            count += text.count(new) - original.count(new)  # crude
    
    # More reliable count
    count = sum(text.count(new) - original.count(new)
                for old, new in path_map.items()
                if old in original)

    if text != original:
        file_path.write_text(text, encoding='utf-8')
        return max(count, 1)
    return 0


def main():
    report_path = REPO_ROOT / "generated/migration-report-2026-04-04.txt"
    path_map = parse_migration_report(report_path)
    print(f"映射条目: {len(path_map)}")

    fixed_files = 0
    total_replacements = 0
    skipped = []

    for md in sorted(REPO_ROOT.rglob("*.md")):
        # 跳过脚本目录和迁移报告本身
        if 'scripts' in md.parts:
            continue
        try:
            text = md.read_text(encoding='utf-8')
        except Exception:
            continue
        
        needs_fix = any(old in text for old in path_map)
        if not needs_fix:
            continue

        original = text
        for old, new in path_map.items():
            if old in text:
                text = text.replace(old, new)
        
        if text != original:
            md.write_text(text, encoding='utf-8')
            fixed_files += 1
            print(f"  已修复: {md.relative_to(REPO_ROOT)}")

    print(f"\n链接修复完成: {fixed_files} 个文件已更新")


if __name__ == "__main__":
    main()
