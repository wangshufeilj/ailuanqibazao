---
title: "The New Stack：Anthropic’s Claude Mythos 已推出，但并不面向你（中英对照精读）"
source: The New Stack (TNS)
source_url: https://thenewstack.io/anthropic-claude-mythos-cybersecurity/
author: Frederic Lardinois
date: 2026-04-08
created_date: 2026-04-08
category: reading/notes/technology/ai-digital/anthropic-claude
tags:
  - The New Stack
  - TNS
  - Frederic Lardinois
  - Anthropic
  - Claude Mythos
  - Claude Mythos Preview
  - Project Glasswing
  - CyberGym
  - CrowdStrike
  - Elia Zaitsev
  - Linux Foundation
  - Jim Zemlin
  - OpenBSD
  - 零日漏洞
  - 网络安全
  - 双语精读
  - AI 安全
  - 代理编码
---

# 英语精读笔记：The New Stack — Claude Mythos 已推出，但并不面向你

### 一、来源与元信息

- **来源**：The New Stack (TNS)
- **题目**：Anthropic’s Claude Mythos is now available, but not for you
- **作者**：Frederic Lardinois（资深科技记者，曾任 TechCrunch 企业版编辑，长期关注云计算、AI 及量子计算领域）
- **原文链接**：[Anthropic’s Claude Mythos is now available, but not for you](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)

---

### 二、前情提要 | Contextual Summary

#### 1. 整体结构 (Overall Structure)

本文报道了 AI 巨头 Anthropic 发布其最新、最强大的模型级次——Claude Mythos Preview。文章从泄密事件背景切入，详细介绍了「翠凤蝶计划」（Project Glasswing）的运作方式、首批合作伙伴、该模型在网络安全防御方面的卓越性能，以及行业专家对 AI 安全攻防平衡的见解。

#### 2. 段落层次 (Paragraph Level)

- **段落 1–2**：背景引入。由早前 CMS 配置错误导致的泄密，引出 Claude Mythos 的定位：比 Opus 更大、更强的非公开模型。
- **段落 3–4**：「翠凤蝶计划」详情。列举了包括微软、亚马逊在内的顶级科技合作伙伴，明确该预览版目前仅用于系统防御和开源工具安全扫描。
- **段落 5–6**：性能评估。通过 CyberGym 基准测试，对比 Mythos 与 Opus 4.6 的评分差异，强调其强大的逻辑推理与代理编码能力。
- **段落 7–9**：安全立场与行业警告。引用 CrowdStrike CTO 的观点，讨论 AI 如何缩短漏洞从发现到被利用的时间窗口，强调「防御者必须跑得更快」。
- **段落 10–14**：实战成果与开源支持。披露 Mythos 已发现数千个漏洞（含 27 年之久的陈年漏洞），并重点讨论该技术如何赋能资源匮乏的开源维护者（Linux 基金会视角）。
- **段落 15**：结语与未来展望。提到未来的商业化计划及 Anthropic 对开源安全组织的资金支持。

#### 3. 段落内部层次 (Intra-paragraph Level)

- **核心逻辑**：[发布新产品] → [限制访问权限] → [解释安全风险] → [展示实战数据] → [行业社会价值]。

---

### 三、逐句精读

🔹 **Anthropic’s Claude Mythos / is / now available, / but not for you.**  
🔸 **Anthropic 的 Claude Mythos / 现已 / 推向市场，/ 但并不针对普通用户。**

> [!NOTE]
> **Anthropic**: 一家总部位于旧金山的美国人工智能初创公司，由 OpenAI 前高管创办，强调 AI 安全性（Safety）与对齐（Alignment）。  
> **Claude Mythos**: Anthropic 旗下的最新模型系列名称，「Mythos」意为「神话」或「神话体系」。  
> 1. **Available**: [adj.] 可获得的，可购得的。在雅思中常用于描述资源或服务的供给。  
> 2. **Not for you**: [phrase] 这里的语气带有一种神秘感或排他性，暗示该产品目前仅限特定群体。

🔹 **Anthropic / launches / Claude Mythos Preview / through Project Glasswing, / giving / select partners / access / to its most capable model / for cybersecurity defense.**  
🔸 **Anthropic / 通过「翠凤蝶计划」 / 推出了 / Claude Mythos 预览版，/ 为 / 精选合作伙伴 / 提供了 / 访问其最强模型的权限，/ 以用于网络安全防御。**

> 1. **Launch**: [v.] 发布，投放（市场）。写作中常用于描述新产品、新政策的实施。  
> 2. **Project Glasswing**: 翠凤蝶计划。Glasswing 是一种翅膀透明的蝴蝶，象征着该计划可能涉及的透明度与防御性。  
> 3. **Capable**: [adj.] 有能力的，功能强大的。常用于评价 AI 模型的逻辑与性能。  
> 4. **Cybersecurity**: [n.] 网络安全。复合词，cyber-（网络的）+ security（安全）。  
> 5. **Access**: [n./v.] 进入权，使用权。常用搭配 `have access to sth.`。

🔹 **In late March, / a misconfiguration / in Anthropic’s content management system / revealed / that the company / was working on / Claude Mythos, / a new tier of models / larger and more capable / than its current flagship, Opus.**  
🔸 **3 月下旬，/ Anthropic 内容管理系统中的 / 一次配置错误 / 泄露了 / 该公司 / 正在研发 / Claude Mythos 的消息，/ 这是一个 / 比其目前旗舰模型 Opus / 体量更大、能力更强的 / 全新模型层级。**

> 1. **Misconfiguration**: [n.] 错误配置。由 prefix `mis-`（错误）+ `configuration` 组成。  
> 2. **Reveal**: [v.] 揭露，显示。常用于雅思阅读中描述研究结果或秘密被发现。  
> 3. **Tier**: [n.] 等级，层级。在技术领域常指代产品线的不同级别（如 Entry-tier, High-tier）。  
> 4. **Flagship**: [n.] 旗舰，最重要的一员。原指舰队的旗舰，现引申为公司最核心的产品。  
> 5. **Opus**: Anthropic 之前最顶尖的模型型号，属于 Claude 3/3.5 系列。

🔹 **That unpublished announcement / also noted / that Anthropic / would take / a more deliberate approach / to launching the model / to mitigate / “potential near-term risks / in the realm of cybersecurity.”**  
🔸 **那份未公开的公告 / 还提到，/ Anthropic / 将采取 / 一种更为审慎的方式 / 来发布该模型，/ 以缓解 / 「网络安全领域 / 潜在的短期风险」。**

> 1. **Deliberate**: [adj.] 深思熟虑的，谨慎的。在雅思写作中可替代 `careful` 以提升词汇深度。  
> 2. **Mitigate**: [v.] 缓解，减轻。高频雅思/考研词汇，常用于讨论解决环境、经济或安全问题。  
> 3. **Potential**: [adj./n.] 潜在的；潜力。  
> 4. **Realm**: [n.] 领域，范围。比 `field` 或 `area` 更正式。  
> 5. **Near-term**: [adj.] 短期的。反义词为 `long-term`。

🔹 **That’s exactly / what Anthropic / is doing / now.**  
🔸 **这正是 / Anthropic / 目前 / 正在做的事情。**

> 1. **Exactly**: [adv.] 确切地，完全地。用于加强语气，对应前文的预告。

🔹 **Claude Mythos Preview, / which the company / described / on Tuesday / as a “general-purpose, unreleased frontier model,” / will not be / publicly available / — at least not yet / and not in its current form.**  
🔸 **Claude Mythos 预览版，/ 该公司 / 在周二 / 将其描述为 / 「通用的、未发布的尖端模型」，/ 将不会 / 公开发售 / —— 至少目前不会，/ 也不会以当前的形式发布。**

> 1. **General-purpose**: [adj.] 通用的。在 AI 领域指能处理多种任务而非单一任务的模型。  
> 2. **Unreleased**: [adj.] 未发布的。  
> 3. **Frontier model**: [n.] 前沿模型，尖端模型。指目前技术水平最高、规模最大的 AI 模型。  
> 4. **Publicly**: [adv.] 公开地。  
> 5. **Form**: [n.] 形式，形态。

🔹 **Instead, / Anthropic / will make it available / to a few select partners / through / what it calls / Project Glasswing.**  
🔸 **相反，/ Anthropic / 将通过 / 所谓的 / 「翠凤蝶计划」，/ 向少数精选合作伙伴 / 开放该模型。**

> 1. **Instead**: [adv.] 相反。逻辑连接词，用于表示对比。  
> 2. **Select**: [adj.] 精选的，优选的。  
> 3. **What it calls**: [phrase] 所谓的。引入特定术语或名称。

🔹 **Claude Mythos Preview / won’t be public / — only select partners / get access.**  
🔸 **Claude Mythos 预览版 / 将不会公开 / —— 只有精选合作伙伴 / 拥有访问权。**

> 1. **Public**: [adj.] 公众的，公开的。

🔹 **Amazon, Apple, Broadcom, Cisco, CrowdStrike, the Linux Foundation, Microsoft, and Palo Alto Networks / are / the launch partners / for this project.**  
🔸 **亚马逊、苹果、博通、思科、CrowdStrike、Linux 基金会、微软以及帕罗奥图网络 / 是 / 该项目的 / 首批合作伙伴。**

> [!NOTE]
> **Amazon/Apple/Microsoft**: 全球顶级科技巨头。  
> **Broadcom/Cisco**: 半导体与网络设备巨头。  
> **CrowdStrike/Palo Alto Networks**: 领先的网络安全公司。  
> **The Linux Foundation**: 非营利性联盟，支持 Linux 内核及开源项目的发展。  
> 1. **Partner**: [n.] 合作伙伴。

🔹 **They / and about 40 additional organizations / will get access / to the preview version / of Claude Mythos / for defensive security work / so they can use it / to scan and secure / their own systems / and open-source tools.**  
🔸 **他们 / 以及大约 40 个其他机构 / 将获得 / Claude Mythos 预览版 / 的访问权限，/ 用于防御性安全工作，/ 以便利用该模型 / 扫描并保护 / 自身的系统 / 和开源工具。**

> 1. **Additional**: [adj.] 额外的，附加的。  
> 2. **Defensive**: [adj.] 防御性的。  
> 3. **Scan**: [v.] 扫描。  
> 4. **Secure**: [v.] 使安全，保卫。此处作为动词使用，在雅思阅读中很常见。  
> 5. **Open-source**: [adj.] 开源的。指源代码公开，任何人都可以查看、修改和分发的软件模式。

🔹 **While / Mythos / wasn’t specifically designed / for cybersecurity tasks, / Anthropic / notes / that the model / performs strongly / in agentic coding and reasoning.**  
🔸 **尽管 / Mythos / 并非专门 / 为网络安全任务设计，/ 但 Anthropic / 指出，/ 该模型 / 在代理编码和推理方面 / 表现强劲。**

> 1. **Specifically**: [adv.] 专门地，明确地。  
> 2. **Perform**: [v.] 表现。  
> 3. **Agentic**: [adj.] 代理性的。在 AI 语境中指模型能够像「代理人」一样自主规划并执行复杂任务。  
> 4. **Coding**: [n.] 编程，编写代码。  
> 5. **Reasoning**: [n.] 推理，逻辑思考。雅思阅读中常涉及的高级认知能力词汇。

🔹 **On the CyberGym benchmark, / which / evaluates / AI agents / on vulnerability analysis tasks, / Claude Mythos / scores 83.1%.**  
🔸 **在 CyberGym 基准测试中，/ 该测试 / 评估 / AI 代理 / 在漏洞分析任务上的表现，/ Claude Mythos / 的得分为 83.1%。**

> [!NOTE]
> **Benchmark**: [n.] 基准测试。衡量计算机硬件或软件性能的标准程序。  
> 1. **Evaluate**: [v.] 评估，评价。写作高频词。  
> 2. **Vulnerability**: [n.] 漏洞，脆弱性。网络安全核心词汇，原义指身体或情感上的脆弱。  
> 3. **Analysis**: [n.] 分析。复数形式为 `analyses`。

🔹 **Opus 4.6, / which / until now / led the rankings / on this benchmark, / scored 66.6%.**  
🔸 **此前 / 在该基准测试排名中 / 居首的 / Opus 4.6，/ 得分为 66.6%。**

> 1. **Lead the rankings**: [phrase] 排名领先。  
> 2. **Score**: [v.] 得分。

🔹 **Anthropic, / which, / after all, / was founded / as an AI-safety-focused alternative / to OpenAI, / seems to believe / that launching a model / with these capabilities / should be done / cautiously.**  
🔸 **毕竟，/ 成立初衷 / 是作为 OpenAI 的一个 / 专注于 AI 安全的替代方案 / 的 Anthropic，/ 似乎认为，/ 发布一个 / 具备此类能力的模型 / 应当 / 谨慎行事。**

> [!NOTE]
> **OpenAI**: ChatGPT 的开发公司。Anthropic 的创始人因对 OpenAI 的商业化路径和安全理念产生分歧而离职创业。  
> 1. **After all**: [phrase] 毕竟。  
> 2. **Safety-focused**: [adj.] 聚焦安全的。  
> 3. **Alternative**: [n.] 替代方案，另一种选择。  
> 4. **Cautiously**: [adv.] 谨慎地。

🔹 **To give / defenders / time / to batten down the hatches / before / attackers / gain access / to it, too.**  
🔸 **为了给 / 防御者 / 留出 / 严阵以待的时间，/ 赶在 / 攻击者 / 也获得 / 访问权之前。**

> 1. **Batten down the hatches**: [idiom] 严阵以待，做好准备应对困难。原指在暴风雨来临前封好船舱盖。  
> 2. **Defender**: [n.] 防御者。  
> 3. **Attacker**: [n.] 攻击者（黑客）。

🔹 **Cynics / may argue / that playing up these dangers / also / helps position these models / as especially capable / — and hence desirable / — in the public eye.**  
🔸 **愤世嫉俗者 / 可能会争辩说，/ 渲染这些危险 / 也有助于 / 将这些模型定位为 / 异常强大的 / —— 从而在公众眼中 / 变得更具吸引力。**

> 1. **Cynic**: [n.] 愤世嫉俗的人，怀疑论者。  
> 2. **Play up**: [v. phr.] 夸大，强调。雅思听力/阅读中常出现。  
> 3. **Position**: [v.] 定位。在市场营销中指塑造品牌形象。  
> 4. **Hence**: [adv.] 因此，从而。逻辑词。  
> 5. **Desirable**: [adj.] 值得拥有的，合意的。

🔹 **But / as CrowdStrike CTO Elia Zaitsev / notes, / there is / a real danger / here.**  
🔸 **但 / 正如 CrowdStrike 首席技术官 Elia Zaitsev / 所指出的，/ 这里确实存在 / 真正的危险。**

> [!NOTE]
> **CrowdStrike**: 美国著名的终端安全和威胁情报服务提供商，曾因 2024 年大规模蓝屏事件而广为人知。  
> **CTO**: Chief Technology Officer，首席技术官。

🔹 **“The window / between a vulnerability being discovered / and being exploited / by an adversary / has collapsed / – what once took months / now happens in minutes / with AI,” / he / says / in a statement.**  
🔸 **「漏洞从被发现 / 到被对手 / 利用的 / 时间窗口 / 已经坍塌 / —— 有了 AI，/ 曾经需要数月时间的过程 / 现在只需几分钟就能完成，」 / 他 / 在一份声明中 / 说道。**

> 1. **Exploit**: [v.] 利用（带有贬义，如剥削、利用漏洞）。  
> 2. **Adversary**: [n.] 对手，敌人。比 `enemy` 更正式，常用于军事或技术对抗。  
> 3. **Collapse**: [v.] 崩塌，瓦解。  
> 4. **Statement**: [n.] 声明，陈述。

🔹 **“Claude Mythos Preview / demonstrates / what is now possible / for defenders / at scale, / and adversaries / will inevitably look / to exploit the same capabilities.”**  
🔸 **「Claude Mythos 预览版 / 展示了 / 防御者 / 现在可以实现的大规模能力，/ 而对手 / 也将不可避免地寻求 / 利用这些相同的能力。」**

> 1. **Demonstrate**: [v.] 证明，展示。写作高频词。  
> 2. **At scale**: [phrase] 大规模地。科技行业常用表达。  
> 3. **Inevitably**: [adv.] 不可避免地。

🔹 **“That / is not / a reason to slow down; / it’s a reason / to move together, faster.”**  
🔸 **「这 / 并不是 / 放慢速度的理由；/ 相反，这是 / 大家团结一致、加快行动的理由。」**

> 1. **Slow down**: [v. phr.] 减速。

🔹 **“If you / want / to deploy AI, / you / need / security.”**  
🔸 **「如果你 / 想要 / 部署 AI，/ 你就 / 需要 / 安全。」**

> 1. **Deploy**: [v.] 部署，配置。常用于技术实施或军事调动。

🔹 **Already, / Anthropic / has used / Mythos Preview / to find / what it describes as / “thousands of zero-day vulnerabilities, / many of them critical.”**  
🔸 **目前，/ Anthropic / 已经利用 / Mythos 预览版 / 发现了 / 其所描述的 / 「数千个零日漏洞，/ 其中许多是致命的」。**

> [!NOTE]
> **Zero-day vulnerability**: 零日漏洞。指已被发现但在开发者发布补丁之前就被攻击者利用的漏洞。  
> 1. **Critical**: [adj.] 关键的，严重的（在安全语境下指极其危险）。

🔹 **Often, / these / were very old, / with the oldest / being a bug / in OpenBSD / that remained unknown and unpatched / for 27 years.**  
🔸 **通常情况下，/ 这些漏洞 / 都非常久远，/ 最古老的一个 / 是 OpenBSD 系统中的 / 一个漏洞，/ 该漏洞已经 27 年 / 未被发现且未修复。**

> [!NOTE]
> **OpenBSD**: 一个以安全著称的类 Unix 操作系统。  
> 1. **Unpatched**: [adj.] 未打补丁的，未修复的。  
> 2. **Unknown**: [adj.] 未知的。

🔹 **The model / also managed to / chain together / several vulnerabilities / in the Linux kernel / to gain / superuser access.**  
🔸 **该模型 / 还成功地 / 将 Linux 内核中的 / 几个漏洞 / 串联起来，/ 以获取 / 超级用户权限。**

> [!NOTE]
> **Linux kernel**: Linux 内核，操作系统的核心部分。  
> **Superuser access**: 超级用户权限（Root 权限），拥有对系统的绝对控制权。  
> 1. **Chain together**: [phrase] 链锁，串联。  
> 2. **Manage to do**: [phrase] 设法完成（强调成功克服困难）。

🔹 **Security research / like this / is / especially important / for open-source projects.**  
🔸 **像这样的 / 安全研究 / 对于开源项目 / 尤其重要。**

> 1. **Especially**: [adv.] 尤其地。

🔹 **Linux Foundation Executive Director Jim Zemlin / said / security expertise / was historically something / large enterprises / could afford / but remained out of reach / for smaller companies / and open-source projects.**  
🔸 **Linux 基金会执行董事 Jim Zemlin / 表示，/ 安全专业知识 / 在历史上 / 只有大型企业 / 才能负担得起，/ 而对于规模较小的公司 / 和开源项目来说，/ 依然是遥不可及的。**

> 1. **Executive Director**: [n.] 执行董事。  
> 2. **Expertise**: [n.] 专业知识，专长。不可数名词。  
> 3. **Afford**: [v.] 负担得起。  
> 4. **Out of reach**: [phrase] 够不着，遥不可及。

🔹 **“Open source maintainers / — whose software underpins / much of the world’s critical infrastructure / — have historically been left / to figure out security / on their own,” / he / says.**  
🔸 **「开源维护者 / —— 他们的软件支撑着 / 全球大部分关键基础设施 / —— 在历史上一直不得不 / 依靠自己 / 来解决安全问题，」 / 他 / 说道。**

> 1. **Maintainer**: [n.] 维护者。  
> 2. **Underpin**: [v.] 支撑，巩固。写作中描述基础结构的高级词汇。  
> 3. **Infrastructure**: [n.] 基础设施。  
> 4. **Figure out**: [v. phr.] 弄清楚，解决。

🔹 **“By giving / the maintainers / of these critical open source codebases / access / to a new generation / of AI models / that can proactively identify and fix / vulnerabilities / at scale, / Project Glasswing / offers / a credible path / to changing that equation.”**  
🔸 **「通过让 / 这些关键开源代码库 / 的维护者 / 获得 / 能够大规模 / 主动识别并修复 / 漏洞的 / 新一代 AI 模型，/ 『翠凤蝶计划』 / 提供了一条 / 改变这一现状的 / 可信路径。」**

> 1. **Codebase**: [n.] 代码库。  
> 2. **Proactively**: [adv.] 主动地。雅思写作中推荐使用的正面品质词汇。  
> 3. **Identify**: [v.] 识别。  
> 4. **Credible**: [adj.] 可信的，可靠的。  
> 5. **Equation**: [n.] 方程式。此处比喻「形势」或「利益平衡」。

🔹 **“This / is how / AI-augmented security / can become / a trusted sidekick / for every maintainer, / not just those / who can afford / expensive security teams.”**  
🔸 **「这就是 / AI 增强型安全 / 如何成为 / 每一位维护者的 / 得力助手，/ 而不仅仅是那些 / 能够雇佣 / 昂贵安全团队的 / 人的专利。」**

> 1. **Augmented**: [adj.] 增强的，扩张的。  
> 2. **Trusted**: [adj.] 值得信赖的。  
> 3. **Sidekick**: [n.] 助手，搭档（非正式语境下常带有一种幽默色彩）。

🔹 **Eventually, / Anthropic / plans to / launch / Mythos-class models / to its users, / but / for now, / it’s restricted / to Project Glasswing participants only.**  
🔸 **最终，/ Anthropic / 计划 / 向其用户 / 推送 / Mythos 级别的模型，/ 但 / 目前，/ 它仅限于 / 『翠凤蝶计划』的参与者。**

> 1. **Eventually**: [adv.] 最终。  
> 2. **Restricted**: [adj.] 受限制的。  
> 3. **Participant**: [n.] 参与者。

🔹 **Anthropic / is making / $100 million / in usage credits / available / to the participating companies, / as well as / $4 million / in direct donations / to open-source security organizations.**  
🔸 **Anthropic / 正在为 / 参与公司 / 提供 / 价值 1 亿美元 / 的使用额度，/ 并向 / 开源安全组织 / 直接捐赠 / 400 万美元。**

> 1. **Usage credits**: [n.] 使用额度（抵扣费用的点数）。  
> 2. **Donation**: [n.] 捐赠。  
> 3. **Organization**: [n.] 组织，机构。

---

### 四、参考与链接

- [Anthropic’s Claude Mythos is now available, but not for you](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)（The New Stack，Frederic Lardinois）
