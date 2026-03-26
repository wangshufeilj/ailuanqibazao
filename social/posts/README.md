# social/posts 目录说明

新归档的**社交平台帖子**统一使用路径：

`social/posts/{platform}/{主题}/`

- `{platform}`：来源平台目录名（如 `reddit`、`xiaohongshu`），与 `.cursor/rules/file-classification.mdc` 中「social/posts 平台细分」一致。
- `{主题}`：按 LCC 与 `articles/`、`reading/notes/` 相同的主题目录名（如 `education`、`technology`）。
- 各 `social/posts/{platform}/{主题}/` 目录内**独立**流水编号 `001`、`002`…

历史说明：此前曾有 `social/posts/education/` 等「无平台层」路径，已逐步迁入带 `{platform}` 的子目录；新内容请勿再放回旧结构。
