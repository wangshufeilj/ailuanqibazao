---
title: "r/singularity：Claude Mythos「过强不公开发布」Reddit 讨论（双语精读笔记）"
source: Reddit
source_url: ""
platform: reddit
subreddit: r/singularity
op_author: WhyLifeIs4
date: 2026-04-08
created_date: 2026-04-08
category: forum/technology
tags:
  - Anthropic
  - Claude
  - Claude Mythos
  - Mythos Preview
  - OpenBSD
  - FFmpeg
  - Linux kernel
  - Project Glasswing
  - Frontier Red Team
  - Reddit
  - r/singularity
  - cybersecurity
  - 双语笔记
note: 帖内相对时间如「13h ago」为摘录时状态；未附原帖直链。
related_reading_notes:
  - reading/notes/technology/ai-digital/anthropic-claude/030-Assessing-Claude-Mythos-Preview-Cybersecurity-Anthropic-Bilingual-Reading-Notes-2026-04-08.md
  - reading/notes/technology/ai-digital/anthropic-claude/032-Fortune-Anthropic-Mythos-Capybara-Data-Leak-Bilingual-Reading-Notes-2026-04-08.md
  - forum/technology/010-Reddit-r-ClaudeCode-Mythos-Opus-Performance-Bilingual-Forum-Notes-2026-04-08.md
---

# r/singularity：Claude Mythos 讨论（双语精读笔记）

这份精读笔记基于 Anthropic 公司新模型 **Claude Mythos** 的 Reddit 讨论帖。内容设定在 2026 年（基于文中提到的日期和模型版本），讨论了这款因过于强大且具有极高网络攻击风险而被限制发布的模型。

---

### 🟢 帖子主干信息 / Original Post

🔹 **Title: Anthropic's new model, Claude Mythos, is so powerful that it is not releasing it to the public.**  
🔸 **标题：Anthropic 的新模型 Claude Mythos 过于强大，以至于公司不打算向公众发布。**

🔹 **Subreddit: r/singularity | Posted by: WhyLifeIs4 | 13h ago**  
🔸 **版块：r/singularity（技术奇点） | 发布者：WhyLifeIs4 | 13小时前**

🔹 **The Singularity is Near**  
🔸 **奇点临近**

> **[重点词汇解析]**
>
> *   **Singularity (奇点)**: 在技术领域，指人工智能超越人类智能，且技术发展速度快到人类无法预测的转折点。
> *   **Claude Mythos**: 文本中提到的 Anthropic 公司最新（虚拟/未来）模型名称。"Mythos" 在希腊语中意为“神话”或“叙事”。

---

### 💬 评论区深度解析 / Comments & Discussion

#### 👤 Avatar-Nick (13h ago)

🔹 In a post on our Frontier Red Team blog, we provide technical details for a subset of these vulnerabilities that have already been patched and, in some cases, the ways that Mythos Preview found to exploit them.  
🔸 在我们的“前沿红队”（Frontier Red Team）博客文章中，我们提供了一部分已被修复的漏洞的技术细节，以及在某些情况下，Mythos 预览版发现并利用它们的方法。

🔹 It was able to identify nearly all of these vulnerabilities—and develop many related exploits—entirely autonomously, without any human steering.  
🔸 它能够完全自主地识别几乎所有这些漏洞，并开发出许多相关的利用程序（exploits），无需任何人工引导。

🔹 The following are three examples:  
🔸 以下是三个例子：

🔹 1. Mythos Preview found a 27-year-old vulnerability in **OpenBSD**—which has a reputation as one of the most security-hardened operating systems in the world and is used to run firewalls and other critical infrastructure.  
🔸 1. Mythos 预览版在 **OpenBSD** 中发现了一个潜伏 27 年之久的漏洞；OpenBSD 以世界上安全性最强的操作系统之一而闻名，常用于运行防火墙和其他关键基础设施。

🔹 The vulnerability allowed an attacker to remotely crash any machine running the operating system just by connecting to it;  
🔸 该漏洞允许攻击者仅通过连接即可远程崩溃任何运行该操作系统的机器；

🔹 2. It also discovered a 16-year-old vulnerability in **FFmpeg**—which is used by innumerable pieces of software to encode and decode video—in a line of code that automated testing tools had hit five million times without ever catching the problem;  
🔸 2. 它还在 **FFmpeg** 中发现了一个存在 16 年的漏洞。FFmpeg 被无数软件用于音视频编解码，而该漏洞所在的这行代码曾被自动化测试工具运行过 500 万次，却从未被发现有问题；

🔹 3. The model autonomously found and chained together several vulnerabilities in the **Linux kernel**—the software that runs most of the world’s servers—to allow an attacker to escalate from ordinary user access to complete control of the machine.  
🔸 3. 该模型自主发现并串联了 **Linux 内核**（支撑全球大部分服务器的软件）中的多个漏洞，使攻击者能够从普通用户权限提升为对机器的完全控制权。

> **[重点词汇/背景解析]**
>
> *   **Red Team (红队)**: 网络安全术语，指扮演攻击者角色，通过模拟攻击来评估防御系统安全性的团队。
> *   **OpenBSD**: 一种强调安全性的类 Unix 操作系统。
> *   **FFmpeg**: 一个开源的、领先的跨平台多媒体框架，用于处理视频、音频和其他多媒体文件。
> *   **Linux kernel (Linux内核)**: 操作系统的核心部分，负责管理硬件资源。
> *   **Escalate (提权/提升)**: 在安全领域特指 "Privilege Escalation"，即获取超出原定权限的访问级别。

---

#### 👤 BestInDaWrldsBbyFmno (12h ago)

🔹 Cyber security is so fucked.  
🔸 网络安全彻底完蛋了。

---

#### 👤 japie06 (12h ago)

🔹 Anthropic writes they still believe AI will favor the defenders more than the attackers.  
🔸 Anthropic 写道，他们仍然相信 AI 对防御者比对攻击者更有利。

🔹 Gaining practice with using language models for bugfinding is worthwhile, whether it’s with Opus 4.6 or another frontier model.  
🔸 无论是使用 Opus 4.6 还是其他前沿模型，练习使用语言模型寻找漏洞都是值得的。

🔹 We believe that language models will be an important defensive tool, and that Mythos Preview shows the value of understanding how to use them effectively for cyber defense is only going to increase—markedly.  
🔸 我们相信语言模型将成为重要的防御工具，而 Mythos 预览版展示了如何有效利用它们进行网络防御的价值只会显著增加。

🔹 Think beyond vulnerability finding. Frontier models can also accelerate defensive work in many other ways. For example, they can:  
🔸 不要局限于漏洞发现。前沿模型还能以许多其他方式加速防御工作。例如：

🔹 Provide a first-round triage to evaluate the correctness and severity of bug reports.  
🔸 提供第一轮分检（triage），以评估漏洞报告的正确性和严重程度。

🔹 De-duplicate bug reports and otherwise help with the triage processes;  
🔸 对漏洞报告进行去重，并协助分检流程；

🔹 Assist in writing reproduction steps for vulnerability reports;  
🔸 协助编写漏洞报告的复现步骤；

🔹 Write initial patch proposals for bug reports;  
🔸 为漏洞报告撰写初步的补丁建议；

🔹 Analyze cloud environments for misconfigurations;  
🔸 分析云环境是否存在配置错误；

🔹 Aid engineers in reviewing pull requests for security bugs;  
🔸 辅助工程师审查 PR（拉取请求）中的安全漏洞；

🔹 Accelerate migrations from legacy systems to more secure ones;  
🔸 加速从旧系统（legacy systems）向更安全系统的迁移；

> **[重点词汇解析]**
>
> *   **Triage (分检)**: 源自医学，指根据紧急程度对任务或问题进行分类处理。在软件中指对 Bug 的初步筛选。
> *   **Patch (补丁)**: 用于修复软件缺陷的代码。
> *   **Legacy systems (遗产系统/旧系统)**: 指过时但仍在使用的旧计算机系统或应用程序。

---

#### 👤 reefine (10h ago)

🔹 Yeah this basically just means anyone who doesn't adapt and immediately harden their security with the latest models will be left in the dust and wiped out.  
🔸 是的，这基本上意味着任何不适应并立即使用最新模型来加强安全的人都会被抛在后面并被消灭。

🔹 The internet of the past will just be defaced, hacked, and leaked code/websites from human teams that refused to use AI.  
🔸 过去那个互联网将只剩下被污损、被黑、以及由于拒绝使用 AI 的人工团队而导致的泄露代码/网站。

---

#### 👤 uzi_loogies_ (9h ago) & corbanmonoxide (9h ago)

🔹 Fuck, that reminds me of Cyberpunk 2077's internet.  
🔸 该死，这让我想起了《赛博朋克 2077》里的互联网。

🔹 I swear the blackwall is one of the most plausible sci-fi concepts.  
🔸 我发誓“黑墙”（Blackwall）是最合理的科幻概念之一。

---

#### 👤 falsedog11 (7h ago)

🔹 The Net (or Cyberspace) in the Cyberpunk universe is a dangerous, highly immersive 3D digital world heavily used for data theft and surveillance.  
🔸 在《赛博朋克》宇宙中，网络（或赛博空间）是一个危险且高度沉浸的 3D 数字世界，被大量用于数据窃取和监视。

🔹 Following a catastrophic "**DataKrash**" in the 2020s that destroyed the old internet, the current network consists of fragmented, local city intranets and corporate data forts shielded from malicious, untamed rogue AIs by a security system known as the **Blackwall**.  
🔸 在 2020 年代一场摧毁了旧互联网的灾难性“数据崩坏”（DataKrash）之后，现在的网络由破碎的局部城市内网和企业数据堡垒组成，并通过名为“**黑墙**”的安全系统将它们与恶意、不受控制的流氓 AI 隔离开来。

🔹 Prescient.  
🔸 有先见之明。

---

#### 👤 Wickywire (8h ago)

🔹 Okay... So Opus 4.6 turned vulnerabilities found in Firefox's JavaScript engine into working exploits twice out of several hundred attempts. Mythos Preview succeeded 181 times.  
🔸 好吧……也就是说，Opus 4.6 在数百次尝试中，只有两次成功将 Firefox JavaScript 引擎中的漏洞转化为可用的攻击程序。而 Mythos Preview 成功了 181 次。

🔹 I need to sit with this for a moment.  
🔸 我得冷静一下（消化一下这个信息）。

---

#### 👤 qrayons (13h ago)

🔹 My potions are too strong for you, traveler.  
🔸 旅人，我的药水对你来说太强了。

> **[背景解析]**
>
> *   **Potions too strong**: 这是一个经典的互联网梗，源自 YouTube 视频 "Potion Seller"。视频中药剂师拒绝卖药水给旅行者，因为他的药水“太强了”。这里借指模型太强不予发布。

---

#### 👤 jsebrech (12h ago)

🔹 This is a preview of times to come, when us plebs have only access to basic models, and the brains the size of a data center are only available to the powers that be, who will use them to grow ever more powerful.  
🔸 这是未来时代的一个预演：我们这些平民只能接触到基础模型，而数据中心规模的“大脑”仅掌握在权势者手中，他们将利用这些模型变得更加强大。

🔹 If you think the world of today is unfair, you've seen nothing yet.  
🔸 如果你觉得当今世界不公平，那你还什么都没见过呢。

---

#### 👤 BeanHeadedTwat (13h ago)

🔹 They’re not releasing it to the public because it is probably horribly compute expensive and giving public access to it isn’t feasible.  
🔸 他们不向公众发布是因为这玩意的计算成本可能高得吓人，向公众开放是不可行的。

---

#### 👤 ChymChymX (13h ago)

🔹 "Claude what is 2+2?"  
🔸 “Claude，2+2 等于几？”

🔹 Thinking. Synthesizing the history of mathematics.  
🔸 思考中。正在综合数学史。

🔹 "You have reached your 5h usage limit. Please try your request again later or purchase on demand tokens"  
🔸 “您已达到 5 小时使用限制。请稍后重试您的请求或购买按需代币。”

---

#### 👤 nsdjoe (13h ago)

🔹 It's much more expensive per token, but its token efficiency might actually make it cheaper than opus 4.6 for some use cases.  
🔸 每个 Token 的价格要贵得多，但在某些使用场景下，它的 Token 效率实际上可能使它比 Opus 4.6 更便宜。

---

#### 👤 Sky-kunn (13h ago)

🔹 Claude Mythos Preview will be available to participants at $25/$125 per million input/output tokens (participants can access the model on the Claude API, Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry).  
🔸 Claude Mythos 预览版将向参与者开放，价格为每百万输入/输出 Token 25 美元/125 美元（参与者可以通过 Claude API、Amazon Bedrock、Google Cloud 的 Vertex AI 和 Microsoft Foundry 访问该模型）。

🔹 I mean it’s still cheaper than GPT-5.4 Pro at $30.00/$180.00.  
🔸 我是说，这仍然比 GPT-5.4 Pro 的 30.00/180.00 美元要便宜。

🔹 Quick reminder that GPT-4.5 did cost $75/$150, which is just insane.  
🔸 提醒一下，GPT-4.5 当时的价格是 75/150 美元，简直疯了。

---

#### 👤 Hostilis_ (12h ago)

🔹 Regarding the most serious exploit they found:  
🔸 关于他们发现的最严重的攻击利用：

🔹 Across a thousand runs through our scaffold, the total cost was under $20,000 and found several dozen more findings.  
🔸 在我们的脚手架（scaffold）中运行一千次，总成本低于 20,000 美元，并发现了数十项更多发现。

🔹 While the specific run that found the bug above cost under $50, that number only makes sense with full hindsight.  
🔸 虽然发现上述漏洞的单次运行成本低于 50 美元，但这个数字只有在事后看来才有意义。

---

#### 👤 Mundane_Scientist_88 (13h ago)

🔹 This will cook SWEs, pack your bags and let's go home.  
🔸 这会把软件工程师（SWEs）“煮熟”（指失业/被取代），收拾行李回家吧。

---

#### 👤 slowd (13h ago)

🔹 I’m a swe of 20 years and I’m all in.  
🔸 我是一个有 20 年经验的软件工程师，我全力投入。

🔹 My new job is to manage 3 claude sessions running all day long, combined with code review of the vast number of pull requests people generate now.  
🔸 我的新工作是管理整天运行的 3 个 Claude 会话，并结合审查现在人们生成的海量拉取请求（PR）。

🔹 I do things in 15 minutes that would have taken 6 hours in early 2025.  
🔸 我在 15 分钟内完成的事情，在 2025 年初可能需要花 6 个小时。

---

#### 👤 garden_speech (12h ago)

🔹 What the fuck do you guys work on? Cookie cutter JS apps that college students could have put together??  
🔸 你们到底在做什么工作？大学生就能拼凑出来的千篇一律的 JS 应用？？

🔹 I use Opus 4.6 every day at work but it’s painfully obvious when using it that the benchmark scores for SWE-Bench, which are atomic, bite sized self-contained tasks in Python repos, do not translate to the kind of month long projects actual devs take on in large complex repos.  
🔸 我每天在工作中使用 Opus 4.6，但很明显，SWE-Bench（软件工程师基准测试）的那些原子化、小块的、在 Python 仓库中的独立任务，并不能转化为真实开发人员在大型复杂代码库中进行的月度项目。

---

#### 👤 Si3rra6ix (12h ago)

🔹 I recall very precisely that the same was said of o3 about a year ago, that OAI would probably not ever release the full version to the public due to it being so powerful.  
🔸 我非常清楚地记得，大约一年前对 o3 也是这么说的：由于它太强大，OpenAI 可能永远不会向公众发布完整版本。

🔹 It’s all smoke and mirrors. Mythos will be released, have its 6 months span in the spotlight and we’ll go for another round of bait and switch.  
🔸 这全是烟雾弹（花招）。Mythos 会发布的，在聚光灯下待个 6 个月，然后我们再进行下一轮“挂羊头卖狗肉”（诱导转向）。

---

#### 👤 fxvv (13h ago)

🔹 Anyone with a background in cybersecurity knows how brittle most software is.  
🔸 任何有网络安全背景的人都知道大多数软件有多么脆弱（brittle）。

🔹 Securing critical vulnerabilities before they can be widely exploited is a responsible use of generative AI tooling, and restricting Mythos’ availability makes sense from a cyber defense perspective if it’s as powerful as claimed.  
🔸 在关键漏洞被广泛利用之前对其进行修复，是生成式 AI 工具的一种负责任用途；如果 Mythos 真的像声称的那样强大，那么从网络防御的角度限制其可用性是有意义的。

---

#### 👤 marlinspike (13h ago)

🔹 Holy crap. Acceleration is hockey stick now.  
🔸 额滴神。加速现在呈“曲棍球棒”（指数级）增长了。

🔹 “We formed Project Glasswing because of capabilities we’ve observed in a new frontier model... AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.”  
🔸 “我们组建 Project Glasswing（玻璃翼计划）是因为我们在一个新前沿模型中观察到的能力……AI 模型已经达到了这样一种编程能力水平：在寻找和利用软件漏洞方面，它们可以超越除最顶尖人类之外的所有人。”

---

#### 👤 CatalyticDragon (7h ago)

🔹 I'm getting distinct "the PS3 is so powerful we need export controls or adversaries will use it to simulate nuclear weapons" vibes here.  
🔸 我在这里感受到了一种明显的“PS3 太强大了，我们需要出口管制，否则对手会用它模拟核武器”的氛围。

> **[背景解析]**
>
> *   **PS3 Export Controls**: 这是一个历史轶事。索尼 PlayStation 3 发布时，由于其使用的 Cell 处理器性能强劲，曾传出其受美国出口管制限制，担心被用于军事超级计算。

---

### 📝 术语与注释 (Annotations)

1.  **Anthropic**: 一家由前 OpenAI 高管创立的 AI 安全和研究公司，以开发 Claude 系列模型闻名。
2.  **r/singularity**: Reddit 上的一个热门讨论版块，专注于“技术奇点”，即 AI 超过人类智能的时刻。
3.  **Project Glasswing**: 文中提到的 Anthropic 内部项目名。Glasswing 指“玻璃翼蝴蝶”，可能象征透明或脆弱的防御。
4.  **Zero-day (零日漏洞)**: 指在软件开发者意识到漏洞并发布补丁之前就被发现的安全漏洞。
5.  **Jevons Paradox (杰文斯悖论)**: 文中提到的一种经济学现象，即技术进步提高了资源利用效率，反而会导致该资源的总消耗量增加。
6.  **SWE-Bench**: 衡量 AI 模型解决现实世界软件工程问题能力的基准测试。
7.  **Amazon Bedrock / Vertex AI / Microsoft Foundry**: 分别是亚马逊、谷歌和微软提供的云端 AI 模型托管平台。
8.  **Stuxnet (震网)**: 一种极其复杂的蠕虫病毒，曾被用于攻击伊朗的核设施。评论中提到的 Leopold Aschenbrenner 是一位著名的 AI 趋势分析师。
