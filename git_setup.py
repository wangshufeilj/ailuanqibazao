#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 驱动整理项目 - Git 初始化与 GitHub 推送脚本
使用前请确保已安装 Git: https://git-scm.com/download/win
若使用 GitHub CLI (gh)，可跳过方式 A 的手动创建步骤
"""

import subprocess
import sys
from pathlib import Path
from typing import Optional


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """执行命令并返回结果"""
    print(f"执行: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    return result


def main():
    """主函数"""
    repo_root = Path(__file__).parent.resolve()
    
    print("=== 步骤 1: 初始化 Git ===")
    try:
        run_command(["git", "init"], check=False)
    except FileNotFoundError:
        print("错误: 未找到 Git，请先安装 Git: https://git-scm.com/download/win")
        sys.exit(1)
    
    print("\n=== 步骤 2: 添加文件 ===")
    run_command(["git", "add", "."])
    run_command(["git", "status"], check=False)
    
    print("\n=== 步骤 3: 首次提交 ===")
    commit_message = "Initial commit: AI 驱动整理项目（大文件仅存条目，见 LARGE_FILES_MANIFEST.md）"
    run_command(["git", "commit", "-m", commit_message])
    
    print("\n=== 步骤 4: 推送到 GitHub ===")
    print("请选择方式：")
    print("  [A] 已手动创建 GitHub 仓库，请设置 <用户名> 和 <仓库名> 后执行：")
    print("      git remote add origin https://github.com/<用户名>/<仓库名>.git")
    print("      git branch -M main")
    print("      git push -u origin main")
    print("")
    print("  [B] 若已安装 gh，可执行：")
    print("      gh auth login")
    print("      gh repo create ai-content-organizer --private --source=. --remote=origin --push")
    print("")


if __name__ == "__main__":
    main()
