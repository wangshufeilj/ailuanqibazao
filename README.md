# AI 驱动整理项目

AI 驱动的多格式内容分类与整理工作区。对来自互联网的各类文件（文章、新闻、图片、视频、数据等）按主题（LCC 分类法）进行分类、存储与索引。

## 目录结构

采用 12 类顶层目录，每类下按主题（LCC）或格式分册。完整结构见 [.cursor/rules/file-classification.mdc](.cursor/rules/file-classification.mdc)。

主要目录：

- `inbox/` — 待分类入口
- `articles/`、`news/`、`research/`、`tutorials/`、`reference/` — 文本类
- `reading/notes/` — 精读笔记
- `images/`、`videos/`、`audio/`、`data/` — 多媒体与数据
- `generated/summaries/` — AI 生成的多媒体摘要
- `INDEX.md` — 主索引

## 大文件仅存条目

本仓库**不存储**图片、视频、PDF、音频、表格等大文件，仅保留其**条目**（路径、标题、类型、日期、摘要链接）。详见 [LARGE_FILES_MANIFEST.md](LARGE_FILES_MANIFEST.md)。实际文件需在本地保有。

## 使用流程

1. 将待分类内容放入 `inbox/`
2. 按内容语义判断主题与类别，存入对应目录
3. 多媒体生成摘要至 `generated/summaries/`
4. 更新 `INDEX.md` 与（如有大文件）`LARGE_FILES_MANIFEST.md`
