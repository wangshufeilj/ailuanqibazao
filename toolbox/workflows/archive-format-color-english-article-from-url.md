# 工作流：从 URL 存档英文长文（抓取 → 排版 → 加粗 → 炫彩 HTML）

本文档固化一次完整闭环：**用户提供原文链接** → **正文入库** → **版式美化** → **重点加粗** → **（可选）HTML 炫彩**。  
成功案例：[SiliconSnark《The Complete Guide to Tech Marketing Buzzwords (1995–2025)》](https://www.siliconsnark.com/the-complete-guide-to-tech-marketing-buzzwords-1995-2025/)，仓库内成品见 [📄 002 英文存档](../../articles/technology/002-The-Complete-Guide-to-Tech-Marketing-Buzzwords-1995-2025-2025-06-01.md) 与 [📄 025/026 精读笔记](../../reading/notes/technology/ai-digital/009-The-Complete-Guide-to-Tech-Marketing-Buzzwords-1995-2025-Reading-Notes-2026-03-20.md)。

---

## 一、适用条件

- 原文为**英文**（或以外文为主）、体裁为**长文 / 评论 / 指南**。
- 目标：**全文存档**归入 `articles/{LCC主题}/`，与 `reading/notes/` 中的精读笔记**分工**（笔记可拆分多文件，存档保持一篇完整英文正文）。
- 需要 **Markdown** 为主格式；炫彩依赖 **HTML 内联样式**（本地预览友好，GitHub 网页可能弱化样式）。

---

## 二、阶段总览

```mermaid
flowchart LR
  A[1 抓取正文] --> B[2 定路径与 frontmatter]
  B --> C[3 写入 articles]
  C --> D[4 Reflow 排版]
  D --> E[5 重点加粗]
  E --> F[6 炫彩 HTML 可选]
  F --> G[7 笔记侧互链与元数据]
```

---

## 三、阶段 1：抓取正文（通用方案）

**目标**：得到干净、可分段落的正文（通常为 Markdown 或接近 Markdown 的纯文本）。

1. 使用可用的网页抓取工具，传入完整文章 URL。  
2. 保存或缓存返回结果（常为 `title` + `content` 结构；`content` 可能带 YAML 块缩进）。  
3. 若抓取失败：换网络/重试；仍失败则记录原因并请用户粘贴正文或更换链接。

**注意**：不要在未授权站点上绕过付费墙；遵守站点条款与版权边界。

---

## 四、阶段 2：分类、命名与 frontmatter

**修改前（Before）**：仅有 URL 或零散笔记，无固定库内路径。  
**修改后（After）**：路径与文件名符合仓库规范，frontmatter 可检索。

1. **顶层类别**：外文长文优先 `articles/`，按 LCC 选子目录（例：科技营销 → `articles/technology/`）。  
2. **流水号**：在目标子目录内取下一个 `00x`。  
3. **文件名**：`{序号}-{英文短标题}-{原文日期YYYY-MM-DD}.md`（原文日不明时用抓取日或站点标注日）。  
4. **frontmatter 建议字段**（英文存档）：

| 字段 | 说明 |
|------|------|
| `title` | 与原文标题一致 |
| `source` | 站点/品牌名 |
| `source_url` | **完整文章 URL**（勿只写根域名） |
| `author` | 作者 |
| `date` | **原文发布日**（若可知） |
| `language` | `en` |
| `category` | 如 `articles/technology` |
| `tags` | 主题词，便于检索 |
| `archived_note` | 抓取方式、后续排版/加粗/HTML 处理摘要 |

精读笔记另存 `reading/notes/...`，`source_url` 与 `date` 应与存档对齐，并在文首增加指向 **全文英文存档** 的 Markdown 链接。

---

## 五、阶段 3：写入 `articles`（初稿）

**修改前（Before）**：抓取导出多为**短行 + 硬换行**、章节为 `### **...**`**。  
**修改后（After）**：同一文件内已是连贯段落 + 标准 `##` 标题（见阶段 4）；初稿也可先落盘再 reflow。

1. 从抓取导出中剥离 `content`，去掉行首 YAML 缩进，合并误断行（若先写初稿，阶段 4 统一做也可）。  
2. 正文前保留 frontmatter，正文以 `# 标题` 起笔。  
3. 文末站点运营句（如打赏提示）可保留；后续可用 `---` + 引用块与正文区分。

---

## 六、阶段 4：Reflow 排版（强烈建议）

**修改前（Before）**：段落被切成固定列宽短行，段间多空行；章节标题为 `### **标题**` 且偶有**跨行标题**。  
**修改后（After）**：

- 以**空段**（`\n\n+`）为界拆成块；块内单行合并为**一段**（空格拼接，压缩多余空白）。  
- `### **...**` → `## ...`（去掉冗余 `**`），跨行标题先拼成一行再转 `##`。  
- 文首增加**来源引用块**（`Source` / `Author` / `Published`）。  
- 增加 **Contents**：链接到各 `##` 的锚点（slug 与所用预览器一致即可；不一致时可在 HTML `h2` 上显式 `id`）。  
- 文末运营句：`---` + `blockquote`（或保留 Markdown blockquote）。

**幂等性**：对已 reflow 的文件再跑同一逻辑时，需识别现有 `##`，避免把正文误判为标题块。建议脚本带「输入形态检测」或保留「仅执行一次」的说明。

---

## 七、阶段 5：重点加粗

**修改前（Before）**：全文同一字重，扫读困难。  
**修改后（After）**：对**定义句、时代主题词、结论句、关键案例名**等加 `**...**`，控制密度，避免句句加粗。

**原则**（可写进 Agent 提示）：

- 每段优先 **1～3 处**高信号加粗，而非术语全标。  
- 媒体名可用 *斜体* 与加粗区分层次。  
- 更新 `archived_note` 说明「关键句与术语已加粗」。

---

## 八、阶段 6：炫彩 HTML（可选）

**修改前（Before）**：仅 Markdown 加粗，无颜色。  
**修改后（After）**：

- **H1 / H2**：改为带 `style` 的 `<h1>` / `<h2 id="...">`（标题色分章，与目录锚点一致）。  
- **来源区**：`<blockquote style="...">` + 渐变背景 + 彩色链接/作者/日期。  
- **目录**：`<ul><li><a style="color:...">` 与各章颜色呼应。  
- **原 `**...**`**：批量替换为 `<strong style="color:...;font-weight:600">...</strong>`，在**有限调色板**（如 6～7 色）上**轮换**，避免彩虹失控。  
- **页脚**：`<hr>` + 淡色 `blockquote`。

**兼容性**：Cursor / VS Code 等本地 Markdown 预览通常可渲染内联样式；**GitHub 网页可能过滤部分样式**，属正常现象。  
**常见坑**：`colored_html` 等字段必须写在 **frontmatter 闭合 `---` 之前**，勿落在正文开头。

**幂等性**：对已含 `<strong style=` 的文件**禁止**再次执行同一替换，否则嵌套或重复标签。脚本应检测特征或单独备份「无炫彩版」。

---

## 九、阶段 7：笔记与存档互链

**修改前（Before）**：笔记与全文存档互不引用。  
**修改后（After）**：

- 在 `reading/notes/...` 文首或「同系列」处增加：  
  `[📄 英文全文存档](../../articles/technology/00x-....md)`  
- 存档 `source_url` 保持**canonical 文章链接**。  
- `date` = 原文日，`created_date` / `formatted` / `colored_html` = 处理日期（按需）。

---

## 十、质量检查清单（提交前）

- [ ] `source_url` 指向**单篇**文章，非仅首页。  
- [ ] 目录锚点能跳到对应章节（在主要预览环境中点测）。  
- [ ] frontmatter YAML 语法有效（`---` 成对、`colored_html` 位置正确）。  
- [ ] 炫彩脚本未对已是 HTML 的版本重复执行。  
- [ ] `archived_note` 与当前形态（reflow / bold / color）一致。  

---

## 十一、扩展与变体

| 变体 | 说明 |
|------|------|
| **不要炫彩** | 完成到阶段 5 即可；保留纯 MD + `**`**，GitHub 兼容性最佳。 |
| **中文长文** | 路径改 `chinese-documents/` 或 `articles/` 下对应主题；frontmatter 可中英混排。 |
| **自动化** | 可将阶段 4～6 逻辑收敛为可幂等的 `scripts/*.py`，本工作流只维护步骤与参数约定。 |

---

## 十二、本仓库中的参考成品

- [📄 英文全文（炫彩版）](../../articles/technology/002-The-Complete-Guide-to-Tech-Marketing-Buzzwords-1995-2025-2025-06-01.md)  
- [📄 精读笔记 025](../../reading/notes/technology/ai-digital/009-The-Complete-Guide-to-Tech-Marketing-Buzzwords-1995-2025-Reading-Notes-2026-03-20.md)  
- [📄 精读笔记 026](../../reading/notes/technology/ai-digital/010-2000s-Tech-Marketing-Buzzwords-Early-Late-IELTS-Reading-Notes-2026-03-20.md)  

---

*工作流文档版本：随仓库维护；与具体脚本实现解耦。*
