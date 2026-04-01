# 工具：给 Markdown 某几行或整段套上“护眼炫彩字体”

适用场景：你已经有一个现成的 Markdown 文件，想把其中 **几行连续句子**或**整段内容**做成**字体炫彩**，而不是背景高亮；重点是 **好看 + 看得清**，适合阅读笔记里的对照句、结论段、案例段。

脚本入口：`scripts/apply_eye_friendly_gradient_text.py`

---

## 一、效果说明

**修改前（Before）**：普通 Markdown 行，例如：

```text
🔻 **С 2019 года ...**
🔹 **Since 2019, ...**
🔸 **自2019年以来，...**
```

**修改后（After）**：脚本会把它替换成一个小型 HTML 容器，使用 **文字渐变色**，不加背景底色，例如：

```html
<div data-toolbox-gradient-text="readable" ...>
<p style="...">🔻 С 2019 года ...</p>
<p style="...">🔹 Since 2019, ...</p>
<p style="...">🔸 自2019年以来，...</p>
</div>
```

说明：

- 这是 **字体颜色渐变**，不是背景渐变。
- 默认 `readable` 调色板偏 **蓝 / 青 / 紫 / 粉**，比高饱和彩虹更清楚。
- 适合 **Cursor / VS Code 本地 Markdown 预览**；GitHub 网页端可能弱化或忽略部分样式。

---

## 二、推荐用法

### 1. 最常见：从某一行开始，连续处理 3 行

```bash
python scripts/apply_eye_friendly_gradient_text.py "reading/notes/social-sciences/015-Russian-Newsprint-Crisis-Kommersant-Gazeta-Terpit-Reading-Notes-2026-03-26.md" --contains "С 2019 года" --line-count 3 --palette readable
```

适合：

- 俄 / 英 / 中三行对照
- 某个局部案例句
- 某个结论段的连续几行

### 2. 整段模式：从命中的这一行，一直处理到下一个空行

```bash
python scripts/apply_eye_friendly_gradient_text.py "目标文件.md" --contains "关键词" --until-blank --palette readable
```

适合：

- 超过 3 行但仍想整体炫彩
- 一整个段落都想统一做字体渐变
- 不想手工数行数

### 3. 如果同一句在文件里出现多次

```bash
python scripts/apply_eye_friendly_gradient_text.py "目标文件.md" --contains "关键词" --line-count 3 --match-index 2
```

这里的 `--match-index 2` 表示取**第二处**匹配。

### 4. 想更柔和或更鲜艳

```bash
python scripts/apply_eye_friendly_gradient_text.py "目标文件.md" --contains "关键词" --line-count 3 --palette soft
python scripts/apply_eye_friendly_gradient_text.py "目标文件.md" --contains "关键词" --line-count 3 --palette vivid
```

可选调色板：

- `readable`：默认，最清楚，优先推荐
- `soft`：更柔和
- `vivid`：更亮更抓眼

---

## 三、参数说明

| 参数 | 必填 | 说明 |
|------|------|------|
| `file` | 是 | 要修改的 Markdown 文件 |
| `--contains` | 是 | 用于定位目标起始行的唯一文本 |
| `--line-count` | 否 | 从起始行开始连续处理多少行，默认 `1` |
| `--until-blank` | 否 | 从起始行一直处理到下一个空行，适合整段模式 |
| `--match-index` | 否 | 第几处匹配，默认 `1` |
| `--palette` | 否 | `readable / soft / vivid`，默认 `readable` |
| `--font-weight` | 否 | 字重，默认 `700` |

---

## 四、适用边界

适合：

- 连续几行句子高亮
- 阅读笔记中的双语 / 三语对照句
- 想对一个完整段落做统一炫彩字体
- 想保留原文件主体结构，只局部加效果

不太适合：

- 超长整段正文大面积上色
- 代码块内文本
- 已经是同类 HTML 炫彩块的内容再次重复处理

---

## 五、注意事项

1. 脚本会**原地修改文件**。
2. 它会把目标几行替换成 HTML `<div><p>...</p></div>`，因此不再保留原来的 `**加粗语法**`，而是由 HTML 的 `font-weight` 接管。
3. 定位文本 `--contains` 尽量写得**足够独特**，避免误替换。
4. 若使用 `--line-count`，目标块中含空行时脚本会拒绝处理，避免误包裹半段内容。
5. 若使用 `--until-blank`，脚本会从命中行一直处理到下一个空行为止。

---

## 六、给 Agent 的一句话口令

如果以后想直接调用这个储备工具，可以这样说：

```text
按 toolbox/workflows/apply-eye-friendly-gradient-text.md 工具执行：
- 文件：贴相对路径
- 定位词：贴一句独特文本
- 模式：连续行数 / 整段直到空行
- 连续行数：可选，任意 >= 1
- 配色：readable
```

例如：

```text
按 toolbox/workflows/apply-eye-friendly-gradient-text.md 工具执行：
- 文件：reading/notes/social-sciences/015-Russian-Newsprint-Crisis-Kommersant-Gazeta-Terpit-Reading-Notes-2026-03-26.md
- 定位词：С 2019 года
- 模式：整段直到空行
- 配色：readable
```
