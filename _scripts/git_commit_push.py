#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Git 提交和推送脚本
"""
import subprocess
import sys
import os
from pathlib import Path

def find_git_executable():
    """查找 git 可执行文件"""
    possible_paths = [
        'git',  # 在 PATH 中
        r'C:\Program Files\Git\cmd\git.exe',
        r'C:\Program Files (x86)\Git\cmd\git.exe',
        os.path.expanduser(r'~\AppData\Local\Programs\Git\cmd\git.exe'),
        r'C:\Program Files\Git\bin\git.exe',
    ]
    
    for git_path in possible_paths:
        try:
            # 测试 git 是否可用
            result = subprocess.run(
                [git_path, '--version'],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                return git_path
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    return None

def run_git_command(cmd, cwd=None):
    """执行 git 命令"""
    git_exe = find_git_executable()
    if not git_exe:
        print("错误: 未找到 git 命令，请确保已安装 Git", file=sys.stderr)
        return False
    
    try:
        result = subprocess.run(
            [git_exe] + cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"错误: 执行 git 命令失败: {e}", file=sys.stderr)
        return False

def main():
    repo_path = Path(__file__).parent.parent
    
    print("=" * 60)
    print("Git 提交和推送")
    print("=" * 60)
    
    # 1. 检查状态
    print("\n1. 检查当前状态...")
    run_git_command(['status'], cwd=repo_path)
    
    # 2. 添加所有更改
    print("\n2. 添加所有更改...")
    if not run_git_command(['add', '-A'], cwd=repo_path):
        print("错误: 添加文件失败", file=sys.stderr)
        return False
    
    # 3. 提交
    print("\n3. 提交更改...")
    commit_message = "更新: 添加新文件和修改现有文件"
    if not run_git_command(['commit', '-m', commit_message], cwd=repo_path):
        print("错误: 提交失败", file=sys.stderr)
        return False
    
    # 4. 推送到远程
    print("\n4. 推送到 GitHub...")
    if not run_git_command(['push'], cwd=repo_path):
        print("错误: 推送失败", file=sys.stderr)
        return False
    
    print("\n" + "=" * 60)
    print("完成！所有更改已提交并推送到 GitHub")
    print("=" * 60)
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
