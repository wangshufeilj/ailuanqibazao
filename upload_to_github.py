#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 上传辅助脚本
帮助用户将文件提交并推送到 GitHub
"""

import subprocess
import sys
import os
from pathlib import Path

def find_git():
    """尝试找到 git 可执行文件"""
    # 常见的 Git 安装位置（Windows）
    common_paths = [
        r'C:\Program Files\Git\cmd\git.exe',
        r'C:\Program Files (x86)\Git\cmd\git.exe',
        r'C:\Program Files\Git\bin\git.exe',
        r'C:\Program Files (x86)\Git\bin\git.exe',
    ]
    
    # 首先尝试直接使用 git（如果在 PATH 中）
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, timeout=5)
        if result.returncode == 0:
            return 'git'
    except:
        pass
    
    # 尝试常见路径
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    return None

def run_git_command(cmd, check=True):
    """执行 git 命令"""
    git_exe = find_git()
    if not git_exe:
        return None
    
    try:
        result = subprocess.run(
            [git_exe] + cmd,
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=30
        )
        if result.returncode != 0 and check:
            return None
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        return None

def check_git_status():
    """检查 git 状态"""
    print("=" * 60)
    print("检查 Git 状态...")
    print("=" * 60)
    
    status = run_git_command(['status'], check=False)
    if status:
        print(status)
        return True
    return False

def check_remote():
    """检查远程仓库配置"""
    print("\n" + "=" * 60)
    print("检查远程仓库配置...")
    print("=" * 60)
    
    remote = run_git_command(['remote', '-v'])
    if remote:
        print(remote)
        return True
    else:
        print("未配置远程仓库")
        return False

def get_current_branch():
    """获取当前分支名"""
    branch = run_git_command(['branch', '--show-current'])
    return branch if branch else 'main'

def main():
    """主函数"""
    repo_path = Path(__file__).parent
    
    print("=" * 60)
    print("GitHub 上传辅助工具")
    print("=" * 60)
    print(f"\n工作目录: {repo_path}\n")
    
    # 设置输出编码
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    # 检查 git 是否可用
    git_exe = find_git()
    if not git_exe:
        print("[X] 未找到 Git。请确保：")
        print("1. 已安装 Git（https://git-scm.com/download/win）")
        print("2. Git 已添加到系统 PATH")
        print("\n或者您可以手动执行命令，参考 GITHUB_UPLOAD_GUIDE.md")
        return
    
    print(f"[OK] 找到 Git: {git_exe}\n")
    
    # 检查 git 状态
    print("=" * 60)
    print("当前 Git 状态")
    print("=" * 60)
    status = run_git_command(['status'], check=False)
    if status:
        print(status)
    else:
        print("无法获取状态")
        return
    
    # 检查远程仓库
    print("\n" + "=" * 60)
    print("远程仓库配置")
    print("=" * 60)
    remote = run_git_command(['remote', '-v'])
    has_remote = bool(remote)
    
    if remote:
        print(remote)
    else:
        print("[!] 未配置远程仓库")
    
    # 获取当前分支
    current_branch = get_current_branch()
    print(f"\n当前分支: {current_branch}")
    
    # 提供操作指南
    print("\n" + "=" * 60)
    print("操作指南")
    print("=" * 60)
    
    if not has_remote:
        print("\n📝 第一步：配置远程仓库")
        print("1. 在 GitHub 上创建新仓库（如果还没有）")
        print("2. 添加远程仓库：")
        print("   git remote add origin https://github.com/你的用户名/仓库名.git")
        print("   或使用 SSH：")
        print("   git remote add origin git@github.com:你的用户名/仓库名.git")
        print("\n然后重新运行此脚本继续。")
        return
    
    # 如果有远程仓库，提供快速操作选项
    print("\n[OK] 远程仓库已配置")
    print("\n可以执行以下命令完成上传：")
    print("\n1. 添加所有更改：")
    print("   git add .")
    print("\n2. 提交更改：")
    print("   git commit -m \"添加新的笔记和规则文件\"")
    print("\n3. 推送到 GitHub：")
    print(f"   git push -u origin {current_branch}")
    print("\n" + "=" * 60)
    print("提示")
    print("=" * 60)
    print("- 首次推送可能需要认证（使用 Personal Access Token 或 SSH）")
    print("- 大文件（图片、视频等）建议不上传到 Git")
    print("- 详细说明请查看 GITHUB_UPLOAD_GUIDE.md")

if __name__ == '__main__':
    main()
