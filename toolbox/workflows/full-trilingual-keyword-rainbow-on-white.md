# 工作流：全文三语对照 + 30%关键词动态炫彩（白底护眼）

适用场景：  
你需要把一篇**长实录/长新闻**做成**俄/英/中（或其他三语）全文对照**，并且在白底阅读环境下实现：

- 全文可读（非整段炫彩）
- 仅部分关键词炫彩（可选 20% / 30% / 35% 覆盖）
- 炫彩为**字本身**，不是背景块
- 保留动态流动效果（动画）

---

## 一、这次沉淀出的核心原则（通用）

1. **先保证结构正确，再谈样式**  
   先做“全文三语对齐”，再做“关键词炫彩密度控制”。

2. **整行文本必须保持普通可读色**  
   防止“满屏炫彩”影响阅读；白底建议使用深灰正文色。

3. **炫彩只给关键词，不给背景底色**  
   `background-clip: text` + `color: transparent` 用在关键词 span 上；不要给关键词底色块。

4. **炫彩密度按比例控制（推荐 20% 或 30%）**  
   用“字符覆盖率”或“词项数量比例”控制，不靠主观手调。

5. **大文本翻译必须分块**  
   全文逐句请求易卡住；使用“分块 + 重试 + 回退”的批处理更稳。

6. **分类先定规则再落库**  
   官方会议实录优先归 `news/politics`，不要误放 `reading/notes/*`。

---

## 二、标准流程（建议照此执行）

### 阶段 A：内容获取与清洗

1. 获取原文 HTML（官方来源优先）。  
2. 提取正文容器（如 `articleBody`）。  
3. 去掉视频容器、推荐卡片、站点尾部导航。  
4. 保留段落级文本（`<p>`）并解码 HTML 实体。

### 阶段 B：三语生成（全文）

1. 以段落为单位建立主序列（如俄文段落列表）。  
2. 英文/中文翻译使用**分块翻译**：
   - 每块控制长度（例如 2k~3k 字符）
   - 失败重试（指数退避）
   - 缺失段落回退到单段翻译
3. 统一输出为三语段块：
   - `🔻` 原文
   - `🔹` 英文
   - `🔸` 中文

### 阶段 C：样式与炫彩策略

1. 容器样式：白底、适度内边距、圆角。  
2. 全文行样式（`tri-line`）固定普通深色。  
3. 关键词样式（`kw`）使用动态彩虹渐变：
   - `background-clip:text`
   - `-webkit-text-fill-color: transparent`
   - `animation: kwFlow ... infinite`
4. 密度控制：仅约 20% / 30% / 35% 词项/字符上色。

### 阶段 D：分类与元信息

1. 路径放到合适目录（如 `news/politics`）。  
2. frontmatter 的 `category` 与路径一致。  
3. `source_url` 指向官方原文；`tags` 标记“三语/全文/炫彩字体”等。

### 阶段 E：验收

最少检查这 5 条：

1. 不是整行炫彩（正文依旧深色）。  
2. 关键词是“字本身炫彩”，无背景高亮块。  
3. 动画仍在（关键词有流动变化）。  
4. 炫彩覆盖大约 20% / 30% / 35%（不是满屏）。  
5. 分类路径与 frontmatter 一致。

---

## 三、样式预设（可直接复用）

### 预设 A（推荐默认）

- 关键词“字本身”动态炫彩
- 其余正文保持黑/深灰可读
- 适合长时间阅读

### 预设 B（视觉更强）

- 黑色字体 + 字后七彩动态背景
- 其余正文保持黑/深灰可读
- 适合强调感更强的展示场景

---

## 四、推荐 CSS 基线（可直接复用）

```css
.tri-line,.tri-ru,.tri-en,.tri-zh{
  color:#263238 !important;
  background:none !important;
  background-image:none !important;
  -webkit-background-clip:initial !important;
  background-clip:initial !important;
  -webkit-text-fill-color:#263238 !important;
}

.kw{
  font-weight:760;
  background-size:260% 100%;
  -webkit-background-clip:text !important;
  background-clip:text !important;
  color:transparent !important;
  -webkit-text-fill-color:transparent !important;
  animation:kwFlow 6.8s linear infinite;
}

@keyframes kwFlow{
  0%{background-position:0% 50%;}
  50%{background-position:100% 50%;}
  100%{background-position:0% 50%;}
}
```

说明：  
`tri-line` 与 `kw` 必须职责分离：前者负责可读，后者负责炫彩。

---

## 五、常见坑与修复

### 1) 预览仍显示“全文炫彩”

原因：旧样式残留或优先级不够。  
修复：

- 在 `tri-line/tri-ru/tri-en/tri-zh` 上加 `!important`
- 显式关闭 `background-image` 与 `animation`
- 确认旧 `triGlow` 不再被引用

### 2) 关键词出现“背景高亮块”

原因：`.kw-*` 里配置了 `background` 色块。  
修复：仅保留文字渐变背景（用于 clip），移除可见底色。

### 3) 彩色覆盖过密/过稀

修复：把密度参数化：

- `0.20`：最克制，长文阅读舒适优先
- `0.30`：平衡（默认）
- `0.35`：更明显

### 4) 中文高亮不自然（单字碎片化）

修复：中文建议最小 2 字分块；必要时引入词典分词做词级高亮。

### 5) 翻译任务卡住

修复：不要逐段请求；用分块批处理 + 超时重试 + 失败回退。

---

## 六、给 Agent 的一句话口令（通用）

```text
按 toolbox/workflows/full-trilingual-keyword-rainbow-on-white.md 执行：
- 目标：全文三语对照
- 分类：按内容放正确目录（默认 news/politics）
- 样式：白底护眼，整行普通字色
- 炫彩：仅关键词，字本身动态炫彩（预设A）
- 密度：20% / 30% / 35%（默认 30%）
```

如需黑字+七彩背景版本（预设B）：

```text
按 toolbox/workflows/full-trilingual-keyword-rainbow-on-white.md 执行：
- 目标：全文三语对照
- 分类：按内容放正确目录（默认 news/politics）
- 样式：白底护眼，整行普通字色
- 炫彩：仅关键词，黑字+字后七彩动态背景（预设B）
- 密度：20% / 30% / 35%（默认 30%）
```

---

## 七、适用边界

适合：

- 官方会议实录、长新闻、长访谈的三语对照版
- 本地阅读优先（Cursor/VS Code 预览）

不适合：

- 需要严格法律级译文一致性的场景（机器翻译仍需人工校对）
- 不支持内联样式的渲染环境
