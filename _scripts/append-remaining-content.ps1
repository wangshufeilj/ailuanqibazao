# append-remaining-content.ps1
# 用途：将精读笔记的剩余内容追加到 002-Dollar-Dominance-US-Tariff-Populism-RT-2026-03-08.md
# 使用：主代理先将完整剩余内容写入 content-to-append.txt，然后运行本脚本

$targetFile = "d:\AI驱动整理乱七八糟\reading\notes\social-sciences\002-Dollar-Dominance-US-Tariff-Populism-RT-2026-03-08.md"
$contentFile = "d:\AI驱动整理乱七八糟\_scripts\content-to-append.txt"

if (-not (Test-Path $contentFile)) {
    Write-Error "请先将待追加内容写入: $contentFile"
    exit 1
}

$content = Get-Content $contentFile -Raw -Encoding UTF8
Add-Content -Path $targetFile -Value $content -Encoding UTF8
Write-Host "已成功追加内容到: $targetFile"
