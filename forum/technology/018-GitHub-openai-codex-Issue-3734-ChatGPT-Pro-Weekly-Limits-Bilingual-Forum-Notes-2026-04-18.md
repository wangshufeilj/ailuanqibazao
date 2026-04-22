---
title: "GitHub openai/codex #3734：ChatGPT Pro 方案迅速触达每周额度 — 双语论坛精读笔记"
source: GitHub
source_url: "https://github.com/openai/codex/issues/3734"
platform: github
repository: openai/codex
issue: 3734
issue_status: closed
labels:
  - bug
  - rate-limits
op_author: Alfredo-Sandoval
date: 2026-03-18
created_date: 2026-04-18
category: forum/technology
tags:
  - OpenAI
  - Codex
  - ChatGPT Pro
  - usage limits
  - rate limits
  - gpt-5-codex
  - gpt-5 high
  - Claude Code
  - cached tokens
  - GitHub Issues
  - 双语笔记
language_pair: en-zh
note: 议题状态、官方回复以 GitHub 页面为准；文内用量数字为报告者自述。
---

# GitHub Issue 精读笔记：Rapidly hitting weekly limits on ChatGPT Pro plan

### 📁 项目信息与 Issue 概览

**Repository:** openai / codex  
**Issue ID:** #3734  
**Title:** Rapidly hitting weekly limits on ChatGPT Pro plan  
**Status:** Closed  
**Labels:** `bug`, `rate-limits`

---

### 📝 主题内容详情 (Issue Description)

👤 **Alfredo-Sandoval** (Opened on March 18, 2026)

🔹 **What version of Codex is running?**  
🔸 **运行的 Codex 版本是什么？**  
🔹 `codex-cli 0.36.0`  
🔸 `codex-cli 0.36.0`

🔹 **Which model were you using?**  
🔸 **你使用的是哪个模型？**  
🔹 `gpt-5-codex high`  
🔸 `gpt-5-codex high`

🔹 **What platform is your computer?**  
🔸 **你的计算机平台是什么？**  
🔹 `Linux 6.14.0-29-generic x86_64`  
🔸 `Linux 6.14.0-29-generic x86_64`

🔹 **What steps can reproduce the bug?**  
🔸 **哪些步骤可以复现这个 Bug？**  
🔹 Use **codex** as your primary coding **agent**.  
🔸 将 **Codex** 作为你的主要编程**智能体**使用。

🔹 **What is the expected behavior?**  
🔸 **预期行为是什么？**  
🔹 Usage **parity** with **Claude code**. Codex usage limits are substantially lower than CC.  
🔸 与 **Claude code** 的使用**对等性**。Codex 的使用限制远低于 Claude Code。

🔹 **What do you see instead?**  
🔸 **你实际看到了什么？**  
🔹 **Incentive** to not spend on ChatGPT Pro.  
🔸 让人失去了购买 ChatGPT Pro 的**动力**。

🔹 **Additional information**  
🔸 **补充信息**  
🔹 It is **caching** a tremendous amount of tokens per chat.  
🔸 每次对话都会**缓存**大量的 Token。  
🔹 Token usage: total=748,177 input=693,709 (+ 9,781,504 **cached**) output=54,468 (reasoning 33,216).  
🔸 Token 使用量：总量 748,177，输入 693,709（另有 9,781,504 **缓存**），输出 54,468（推理 33,216）。  
🔹 Maybe this is why?  
🔸 或许这就是原因？

> **[词汇与专有名词解析]**  
> * **Agent（智能体）**：在 AI 领域指能够自主理解任务、规划并执行操作的程序，Codex 常被集成在开发者工具中作为此类角色。  
> * **Parity（对等/平等）**：此处指用户希望 OpenAI 的产品在额度上能与竞争对手 Anthropic 的 Claude Code 持平。  
> * **Incentive（动机/动力）**：原意为激励。作者讽刺糟糕的额度体验反而「激励」用户不要订阅。  
> * **Cached Tokens（缓存的 Token）**：OpenAI 的一种机制，对于重复出现的上下文，系统会通过缓存来减少计算压力。但在 Prompt 极长的情况下，缓存量也会非常惊人。

---

### 💬 讨论区 (Discussions)

👤 **ariawisp**

🔹 `gpt-5-codex high` seems to consume **insane** amounts of usage compared to `gpt-5 high`.  
🔸 与 `gpt-5 high` 相比，`gpt-5-codex high` 的消耗量似乎达到了**疯狂**的程度。  
🔹 I had been using `gpt-5 high` with 4-6 agents for 8+ hours a day on my Pro plan without ever hitting usage limits.  
🔸 我之前在 Pro 方案上每天使用 4-6 个智能体运行 `gpt-5 high` 超过 8 小时，从未达到过使用限制。  
🔹 Then I tried `gpt-5-codex high` when it released yesterday and hit the 5-day usage limit after only 30 minutes of running 2 agents.  
🔸 结果昨天新模型发布后，我尝试运行 2 个智能体，仅 30 分钟就达到了 5 天的使用上限。  
🔹 Very frustrating.  
🔸 非常令人沮丧。

---

👤 **aehlke**

🔹 Since it released they heavily recommend using **medium**.  
🔸 自发布以来，官方强烈建议使用 **medium（中等推理）** 模式。  
🔹 It's more **dynamic** than before - using fewer tokens for thought when it identifies "easy" problems, and using more tokens (like high) for "hard" ones.  
🔸 它比以前更加**动态**——当识别到「简单」问题时，它会减少思考消耗的 Token；遇到「难题」时则会增加（类似 high 模式）。  
🔹 Btw how many tokens did it report were used in those 30 minutes?  
🔸 顺便问下，那 30 分钟里报告的使用量是多少？

> **[解析]**  
> * **Dynamic（动态的）**：指模型能够根据任务复杂度自动调整资源投入，是 GPT-5 系列的核心特性之一。

---

👤 **ariawisp**

🔹 If I recall, it was around the same **magnitude** shown by @Alfredo-Sandoval - around 10 million cached tokens.  
🔸 如果我没记错，其**量级**与作者提到的差不多——大约 1000 万缓存 Token。

---

👤 **aehlke**

🔹 Sounds like something is going wrong then. I used around 10 million un-cached tokens yesterday, on my first day of Pro usage.  
🔸 听起来确实出问题了。我昨天第一天使用 Pro，大约用了 1000 万非缓存 Token。  
🔹 From my largest session: Token usage: total=8,755,957 input=8,537,903 (+ 30,605,824 cached) output=218,054 (reasoning 122,496).  
🔸 在我最大的一个会话中：Token 总量约 875 万，缓存了 3000 多万。

---

👤 **Alfredo-Sandoval** (Author)

🔹 Had the weekly limit **lifted** for a few messages and its back now.  
🔸 限制曾短暂**解除**了一会儿，发了几条消息后又回来了。  
🔹 Can't help but think its related to the usage spike from people coming over to codex.  
🔸 我不禁在想，这是否与大量用户涌向 Codex 导致的使用高峰有关。

---

👤 **TrevorLoucks**

🔹 I just hit limit on Pro plan using `gpt-5-codex-medium` with 2.5 days till reset, something is off.  
🔸 我刚在 Pro 方案上用 `gpt-5-codex-medium` 达到了限制，离重置还有 2.5 天，肯定有什么地方不对劲。  
🔹 And the limit message is also telling me to upgrade to Pro to increase my limits.  
🔸 而且限制消息居然还在告诉我「升级到 Pro 以提高额度」，但我已经是 Pro 了。

---

👤 **ariawisp** (Compiled Tweets/Feedback)

🔹 "The Codex GPT-5-Codex model should be cautious to use (for plus users), as it quickly reaches its limit."  
🔸 「Plus 用户在使用 GPT-5-Codex 时应保持谨慎，因为它会迅速达到上限。」  
🔹 "Guys, don't try gpt-5-codex if you want do anything. Wasting limit in simple 4 prompts at medium reasoning."  
🔸 「伙计们，如果你想干正事就别碰这个模型。在 medium 模式下才 4 个提示词就耗尽了额度。」  
🔹 "I hit my Codex **quota** limit so now I have to wait 2 days. How am I supposed to code now? In an IDE like some kind of **savage**? 😤"  
🔸 「我的 Codex **配额**用完了，得等 2 天。现在让我怎么写代码？像**野人**一样直接在 IDE 里写吗？」  
🔹 "Claude 5hr window more reasonable."  
🔸 「Claude 的 5 小时窗口期更为合理。」  
🔹 "I just asked it to fix a test file and suddenly it burned 200K tokens. Bug?"  
🔸 「我只是让它修复一个测试文件，它突然烧掉了 20 万 Token。Bug 吗？」

> **[词汇解析]**  
> * **Quota（配额/限额）**：系统分配给用户的特定使用量。  
> * **Savage（野人/原始人）**：此处是开发者的自嘲，意指离开 AI 辅助后，手动写代码变得像原始时代一样低效。

---

👤 **omggga**

🔹 Could you please publish the **concrete** weekly limits and reset rules?  
🔸 能否公布**具体的**每周限制额度和重置规则？  
🔹 Hitting the limit after half a day of normal work on a Pro plan is pretty unreasonable without clear guidance.  
🔸 在 Pro 方案上正常工作半天就达到上限，在没有明确指引的情况下是非常不合理的。

---

👤 **rockyicer** (Bilingual comment provided)

🔸 与 GPT-5 High 相比，GPT-5-Codex High 似乎消耗了大量的使用量。  
🔹 gpt-5-codex high seems to consume insane amounts of usage...  
🔸 仅 30 分钟就达到了 5 天的使用限制。非常令人沮丧。

---

👤 **ariawisp**

🔹 I've just gone back to `gpt-5 high` and having no issues with limits there so far.  
🔸 我刚切回到 `gpt-5 high`，目前还没遇到额度问题。  
🔹 `gpt-5-codex` spent 30 minutes working and ultimately **reverted** everything it did because it wasn't sure how to solve the issues.  
🔸 `gpt-5-codex` 花了 30 分钟干活，最后却因为不确定如何解决问题而**撤销**了所有更改。

---

👤 **whoschek**

🔹 In my experience `gpt-5-codex high` also turns out to be far worse than `gpt-5 high`, at least for a complex **codebase**.  
🔸 根据我的经验，至少在复杂的**代码库**中，`gpt-5-codex high` 表现得远不如 `gpt-5 high`。  
🔹 It comes across as a shallow **drama queen** that claims to find bugs where there actually aren't any.  
🔸 它给人的感觉就像一个肤浅的**戏精**，在没有 Bug 的地方声称发现了 Bug。  
🔹 The model ends up spending little reasoning time on things that are actually subtle and hard issues.  
🔸 模型最终在真正微妙且困难的问题上花费的推理时间极少。  
🔹 OpenAI should drop the "**auto-mode**", and instead add a radio group UI widget where users can choose between think time: 1sec, 10secs, 100secs, 1000secs.  
🔸 OpenAI 应该放弃「**自动模式**」，增加一个 UI 组件让用户自己选择思考时间：1 秒、10 秒、100 秒或 1000 秒。

> **[词汇解析]**  
> * **Codebase（代码库）**：项目所有源代码的集合。  
> * **Drama queen（戏精/小题大做的人）**：形象地描述模型由于误解代码逻辑而产生大量无谓的、错误的纠错反应。

---

👤 **jovkon123**

🔹 Just tried first run of `gpt-5-codex medium` and it spent 45 minutes running powershell cmds changing 2 files and then ultimately reverting them.  
🔸 刚试了一下 `gpt-5-codex medium`，它花了 45 分钟运行 PowerShell 命令修改了 2 个文件，结果最后又给撤销了。  
🔹 Token Usage: Input 267k (+ 17M cached), Output 117k.  
🔸 Token 使用情况：输入 267k（另有 1700 万缓存），输出 117k。

---

👤 **tekn0x**

🔹 $200 a month is cutting it very close at that rate for a 5-6 day work week.  
🔸 按照这个速度，每月 200 美元的价格对于每周 5-6 天的工作量来说太吃紧了。  
🔹 At least Claude Code never had the weekly cut off, just the 5 hour cool down.  
🔸 至少 Claude Code 从没有过每周封禁，只有 5 小时的冷却期。

---

👤 **neo0oen619**

🔹 5 hours of coding and I get limited for 5 days .... that's **absurd**.  
🔸 编了 5 小时代码就被封了 5 天……这太**荒唐**了。

---

👤 **etraut-openai** (Collaborator)

🔹 We've recently introduced some changes that help you extend your available usage.  
🔸 我们最近引入了一些更改，旨在帮助您延长可用额度。  
🔹 (Issue marked as **Closed**)  
🔸 （此议题被标记为**已关闭**。）

---

👤 **mateususa** (Final comment)

🔹 Introducing a less capable model does not fix the issue.  
🔸 引入一个能力较弱的模型并不能解决问题。  
🔹 Our most recent models already **dynamically** adjust their reasoning level based on the specified task.  
🔸 （引述官方观点）我们最新的模型已经能够根据特定任务**动态**调整其推理水平。  
🔹 If you are hitting usage limits, you have the option of upgrading to a less **restrictive** plan, buying additional credits, or switching to **metered** API key pricing.  
🔸 如果你达到了使用限制，你可以选择升级到限制较少的方案、购买额外积分，或者转向**按量计费**的 API Key 模式。

> **[解析]**  
> * **Restrictive（限制性的）**：指额度更宽松的套餐。  
> * **Metered pricing（按量计费）**：类似水电费，用多少 Token 付多少钱，没有每周或每 5 小时的硬性上限，但对于高强度用户来说可能极其昂贵。

---

### 📌 小结（笔记整理者）

- 讨论焦点：**gpt-5-codex** 系列在 Codex / Pro 语境下的**额度消耗速度**、**缓存 Token 统计**与用户感知的**公平性/透明度**（相对 Claude Code 等）。  
- 官方协作账号 **etraut-openai** 表示已推出有助于延长可用额度的变更，议题随后 **Closed**；具体数字与规则仍以 [Issue #3734](https://github.com/openai/codex/issues/3734) 及当时产品说明为准。
