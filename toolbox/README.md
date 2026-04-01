# 工具箱 | Toolbox

存放**可复用的工作流说明**（Markdown），便于日后按相同套路处理同类任务。  
执行时由人或 Agent 对照步骤操作；不强制附带脚本（脚本可随仓库迭代单独维护）。

## 工作流索引

| 文档 | 适用场景 |
|------|----------|
| [从 URL 存档英文长文：抓取 → 排版 → 加粗 → 炫彩 HTML](workflows/archive-format-color-english-article-from-url.md) | 外站长文、SiliconSnark 类博客；需要本地精读存档 + 可选炫彩预览 |
| [给 Markdown 某几行或整段套上护眼炫彩字体](workflows/apply-eye-friendly-gradient-text.md) | 已有 Markdown 文件；想把几行句子或整段内容做成“字体炫彩、背景不变、优先清晰度”的局部高亮 |
| [全文三语对照 + 30%关键词动态炫彩（白底护眼）](workflows/full-trilingual-keyword-rainbow-on-white.md) | 官方实录/长新闻的全文三语对照；要求“整行可读 + 仅关键词动态炫彩 + 白底护眼”，并可控炫彩密度（30%/35%） |

## 快速调用（推荐）

在 **Cursor** 里不必每次手抄流程，用下面任一方式即可。

### 方式 A：`@` 引用工作流（最省事）

1. 在聊天输入框输入 **`@`**。  
2. 选中 **[📄 英文长文存档工作流](workflows/archive-format-color-english-article-from-url.md)**（或搜索 `archive-format-color`）。  
3. 同一句话里附上 **文章 URL**，并说明要不要炫彩，例如：  
   - `按此工作流抓取并入库，要炫彩`  
   - `按此工作流，只要排版加粗不要 HTML 颜色`

Agent 会把该文件当作执行清单，按阶段做。

### 方式 B：复制一句「口令」（不 `@` 也行）

把下面整段复制进对话框，把 URL 和选项改掉即可：

```text
请按 toolbox/workflows/archive-format-color-english-article-from-url.md 工作流执行：
- 文章 URL：粘贴这里
- 炫彩 HTML：要 / 不要
- 精读笔记：要另写 / 已有文件只互链 / 本次不做
```

局部炫彩字体则可复制这段：

```text
请按 toolbox/workflows/apply-eye-friendly-gradient-text.md 工具执行：
- 文件：贴相对路径
- 定位词：贴一句独特文本
- 模式：连续行数 / 整段直到空行
- 连续行数：可选，任意 >= 1
- 配色：readable / soft / vivid
```

全文三语 + 关键词动态炫彩则可复制这段：

```text
请按 toolbox/workflows/full-trilingual-keyword-rainbow-on-white.md 执行：
- 目标：全文三语对照
- 分类：按内容放正确目录（默认 news/politics）
- 样式：白底护眼，整行普通字色
- 炫彩：仅关键词，字本身动态炫彩
- 密度：20% / 30% / 35%（默认 30%）
```

如果要黑字 + 字后七彩动态背景（预设B），可用这段：

```text
请按 toolbox/workflows/full-trilingual-keyword-rainbow-on-white.md 执行：
- 目标：全文三语对照
- 分类：按内容放正确目录（默认 news/politics）
- 样式：白底护眼，整行普通字色
- 炫彩：仅关键词，黑字+字后七彩动态背景（预设B）
- 密度：20% / 30% / 35%（默认 30%）
```

### 方式 C：自己记一个短口令（口语）

你可以自己约定一句，例如：**「走工具箱英文存档流程」**，并在同一条消息里贴上 **URL** 与 **要不要炫彩**。  
为减少歧义，**第一次**仍建议同时 `@` 上述工作流文件一次，之后 Agent 会结合仓库里的文档理解「工具箱英文存档」指什么。

---

## 使用说明

1. 打开对应 `workflows/*.md`，按**阶段**执行。  
2. 涉及网页抓取时，按任务需求选择可用抓取方案。  
3. 涉及入库路径与命名时，遵循 **file-classification**（见 `.cursor/rules/file-classification.mdc`）。
