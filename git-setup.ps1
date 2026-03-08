# AI 驱动整理项目 - Git 初始化与 GitHub 推送脚本
# 使用前请确保已安装 Git: https://git-scm.com/download/win
# 若使用 GitHub CLI (gh)，可跳过方式 A 的手动创建步骤

$ErrorActionPreference = "Stop"
$repoRoot = $PSScriptRoot

Write-Host "=== 步骤 1: 初始化 Git ===" -ForegroundColor Cyan
Set-Location $repoRoot
git init

Write-Host "`n=== 步骤 2: 添加文件 ===" -ForegroundColor Cyan
git add .
git status

Write-Host "`n=== 步骤 3: 首次提交 ===" -ForegroundColor Cyan
git commit -m "Initial commit: AI 驱动整理项目（大文件仅存条目，见 LARGE_FILES_MANIFEST.md）"

Write-Host "`n=== 步骤 4: 推送到 GitHub ===" -ForegroundColor Cyan
Write-Host "请选择方式：" -ForegroundColor Yellow
Write-Host "  [A] 已手动创建 GitHub 仓库，请设置 <用户名> 和 <仓库名> 后执行："
Write-Host "      git remote add origin https://github.com/<用户名>/<仓库名>.git"
Write-Host "      git branch -M main"
Write-Host "      git push -u origin main"
Write-Host ""
Write-Host "  [B] 若已安装 gh，可执行："
Write-Host "      gh auth login"
Write-Host "      gh repo create ai-content-organizer --private --source=. --remote=origin --push"
Write-Host ""
