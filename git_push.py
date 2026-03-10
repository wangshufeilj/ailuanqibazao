#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git 提交并推送到 GitHub
"""

import subprocess
import sys
import os
from pathlib import Path


def find_git():
    """查找 Git 可执行文件"""
    # 检查是否在 PATH 中
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, check=True)
        return "git"
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    
    # 检查常见安装路径
    common_paths = [
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files (x86)\Git\cmd\git.exe",
        r"C:\Program Files\Git\bin\git.exe",
    ]
    
    for git_path in common_paths:
        if os.path.exists(git_path):
            return git_path
    
    return None


def run_command(cmd: list[str], check: bool = True, cwd: Path = None) -> subprocess.CompletedProcess:
    """执行命令并返回结果"""
    print(f"执行: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd, 
            check=check, 
            capture_output=True, 
            text=True,
            cwd=cwd,
            encoding='utf-8',
            errors='replace'
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr and result.returncode != 0:
            print(f"错误: {result.stderr}", file=sys.stderr)
        return result
    except FileNotFoundError as e:
        print(f"错误: 未找到命令 {' '.join(cmd)}", file=sys.stderr)
        print("请确保已安装 Git: https://git-scm.com/download/win", file=sys.stderr)
        sys.exit(1)


def main():
    """主函数"""
    repo_root = Path(__file__).parent.resolve()
    
    # 查找 Git
    git_cmd = find_git()
    if not git_cmd:
        print("错误: 未找到 Git，请先安装 Git: https://git-scm.com/download/win", file=sys.stderr)
        sys.exit(1)
    
    # 替换命令中的 'git' 为实际路径
    def git_command(*args):
        if git_cmd == "git":
            return ["git"] + list(args)
        else:
            return [git_cmd] + list(args)
    
    print("=== 步骤 1: 检查 Git 状态 ===")
    run_command(git_command("status"), check=False, cwd=repo_root)
    
    print("\n=== 步骤 2: 添加所有更改 ===")
    run_command(git_command("add", "."), cwd=repo_root)
    
    print("\n=== 步骤 3: 提交更改 ===")
    commit_message = "Update: 添加新文件和更新索引"
    run_command(git_command("commit", "-m", commit_message), cwd=repo_root)
    
    print("\n=== 步骤 4: 推送到 GitHub ===")
    run_command(git_command("push", "origin", "main"), cwd=repo_root)
    
    print("\n✅ 完成！所有更改已推送到 GitHub")


if __name__ == "__main__":
    main()
