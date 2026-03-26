---
title: Cursorの「自社開発モデル」は他社製だった―Composer 2とKimi K2.5
source: kkm-mako.com
author: kkm (Horikawa)
date: 2026-03-21
created_date: 2026-03-21
category: reading/notes/technology
tags:
  - Cursor
  - Composer 2
  - Kimi K2.5
  - Moonshot AI
  - 月之暗面
  - Anysphere
  - AI编程工具
  - 开放权重
  - Modified MIT License
  - 署名义务
  - 派生作品
  - 强化学习
  - compaction-in-the-loop
  - Hacker News
  - Fynn
  - Yulun Du
  - 估值
  - ARR
  - 行业伦理
  - 日语精读
  - 英语词汇
  - kkm
---

### 文章信息 (Article Information)

*   **题目 (Title):** Cursorの「自社開発モデル」は他社製だった―Composer 2とKimi K2.5 / Cursor's "In-house Model" was Third-party: Composer 2 and Kimi K2.5 / Cursor的“自研模型”竟是他家产品：Composer 2 与 Kimi K2.5
*   **来源 (Source):** kkm-mako.com
*   **作者 (Author):** **kkm (Horikawa)**。背景：**后端工程师** (Backend Engineer)，擅长 **AWS** 与 **Django** 开发。其内容通常关注 AI 编程工具、云基础设施及开发效率。
*   **发布日期 (Date):** 2026年3月21日

---

### 前情提要 (Overview & Structure)

```markdown
# 文章结构纵览 (Article Structure Overview)

## 1. 整体架构 (Global Structure)
本文是一篇科技深度报道与评论，探讨了知名AI编程编辑器 Cursor 在发布其“自研”模型 Composer 2 时引发的争议。文章从技术发现、产品背景、授权协议冲突、各方反应及行业伦理五个维度展开，旨在揭示 AI 行业中“自研”标签下的真实技术生态。
- **Core Theme**: The controversy surrounding Cursor's rebranding of Moonshot AI's Kimi K2.5 as its own "in-house" model.

## 2. 段落逻辑 (Paragraph-level Logic)
- **Introduction**: 揭露 Composer 2 的真实身份（Moonshot AI 的 Kimi K2.5），指出引发争议的根源。
- **The Discovery**: 详述开发者 Fynn 如何通过 API 接口模型 ID 发现真相。
- **Technical Analysis**: 解释 Composer 2 的技术特征（RL 强化学习）及其所谓创新的实质。
- **Product Context**: 介绍 Kimi K2.5 及其背后的 Moonshot AI 及其开源/开放权重政策。
- **Legal & License Conflict**: 核心部分。解析 Modified MIT License 协议，指出 Cursor 违反了署名义务（Attribution Requirement）。
- **Reactions & Business Strategy**: 描述 Moonshot AI 的内部反应、Cursor 的沉默及其背后的高估值资本压力。
- **Community Sentiment**: 梳理 Hacker News 等技术社区的三种代表性观点。
- **Conclusion**: 总结 AI 工具透明度的缺失问题，并对未来行业信誉提出警示。

## 3. 段落内部细节 (Intra-paragraph Details)
- **ID Dissection**: 将 `kimi-k2p5-rl-0317-s515-fast` 拆解为厂商、型号、技术手段、时间、版本和速度模式。
- **License Thresholds**: 明确指出月活 1 亿或月营收 2000 万美元的门槛，对比 Cursor 远超此标准的营收规模（20亿美金 ARR）。
- **Analogy**: 使用“电影导演剥夺代笔编剧署名权”来类比 AI 模型的版权争议。
```

---

### 全文精读笔记 (Full-Text Intensive Reading Notes)

🔹 **Cursorの「自社開発モデル」は他社製だった―Composer 2とKimi K2.5**
🔸 **Cursor's "in-house model"** / **was third-party** / — **Composer 2 and Kimi K2.5**
🔻 **Cursor 的“自研模型”竟是他家产品——Composer 2 与 Kimi K2.5**

> - **In-house** [ˌɪnˈhaʊs] `adj.` Done or existing within an organization. (公司内部的；自研的)
>   - *Collocation:* **In-house development** (内部开发), **in-house team** (内部团队).
>   - *IELTS Note:* 常用于描述公司不外包而自主完成的工作。
> - **Third-party** [ˌθɜːrd ˈpɑːrti] `adj.` Relating to a person or group besides the two primarily involved. (第三方的；他家的)
>   - *Note:* 在科技领域常指非原生或外部提供的服务。

---

🔹 **Cursorが自社開発と謳ったComposer 2の正体はMoonshot AIのKimi K2.5+RLだった。**
🔸 **The true identity of Composer 2**, / **which Cursor claimed was / an in-house development**, / **was Moonshot AI's Kimi K2.5 + RL.**
🔻 **Cursor 宣称自研的 Composer 2，其真实身份其实是 Moonshot AI 的 Kimi K2.5 加上强化学习（RL）。**

> - **Claim** [kleɪm] `v.` State or assert that something is the case, typically without providing proof. (宣称；断言)
>   - *Synonym:* **Assert**, **Maintain**.
>   - *Collocation:* **Claim to be** (自称是...).
> - **Identity** [aɪˈdentəti] `n.` The fact of being who or what a person or thing is. (身份；本体)
>   - *Etymology:* 来自拉丁语 *idem* (same).
> - **RL (Reinforcement Learning)**: 强化学习。机器学习的一个领域，通过奖励机制训练模型做出决策。
> - **[Entity] Moonshot AI (月之暗面):** 一家位于北京的中国顶尖 AI 初创公司，由杨植麟创立，以 Kimi 长文本大模型著称。

---

🔹 **APIのモデルIDから発覚し、ライセンス違反で騒動に。**
🔸 **It was revealed / through the API model ID**, / **sparking a controversy / over license violations.**
🔻 **此事因 API 模型 ID 而曝光，并因违反授权协议（License）引发了骚动。**

> - **Reveal** [rɪˈviːl] `v.` Make (previously unknown or secret information) known to others. (揭露；曝光)
>   - *Antonym:* **Conceal** (隐藏).
> - **Spark** [spɑːrk] `v.` Provide the stimulus for (a dramatic event or process). (引发；触发)
>   - *IELTS Writing:* **Spark a heated debate** (引发热议) 是写作高分短语。
> - **Violation** [ˌvaɪəˈleɪʃn] `n.` (C/U) An action that breaks or acts against something. (违反；违背)
>   - *Verb:* **Violate**.
>   - *Collocation:* **License violation** (违反许可证), **privacy violation** (侵犯隐私).

---

🔹 **Cursor Composer 2のAPIに「Kimi K2.5」の名前が残っていた**
🔸 **The name "Kimi K2.5"** / **remained in the API** / **of Cursor Composer 2.**
🔻 **Cursor Composer 2 的 API 中仍保留着“Kimi K2.5”的名称**

> - **Remain** [rɪˈmeɪn] `v. [Link/Intransitive]` Continue to possess a particular quality or fulfill a particular role. (保持；残留)
>   - *Note:* 作为系动词时，后接形容词或名词；作为不及物动词时，意为“留下”。

---

🔹 **3月19日、AIコーディングエディタCursorが「Composer 2」を発表しました。**
🔸 **On March 19,** / **the AI coding editor Cursor** / **announced "Composer 2."**
🔻 **3 月 19 日，AI 编程编辑器 Cursor 发布了“Composer 2”。**

> - **Editor** [ˈedɪtər] `n. [C]` A program used for editing text or code. (编辑器)
> - **[Entity] Cursor:** 一款基于 VS Code 分叉开发的 AI 辅助编程工具，因其强大的代码补全和编辑功能而在开发者中极具人气。

---

🔹 **自社で開発した最強のコーディングモデル――そう銘打たれていました。**
🔸 **It was branded as** / **the strongest coding model** / **developed in-house.**
🔻 **它被冠以“自研最强编程模型”的头衔。**

> - **Brand** [brænd] `v.` To describe or identify in a particular way. (冠以...称号；贴标签)
>   - *Usage:* **Brand somebody as something** (通常指负面标签，但在市场语境下指品牌定位).
> - **Strongest** [ˈstrɔːŋɡɪst] `adj. (Superlative)` 最强的。

---

🔹 **発表から24時間も経たないうちに、開発者のFynnがCursorのOpenAI互換APIをいじっていて、あるモデルIDを見つけました。**
🔸 **Less than 24 hours / after the announcement**, / **a developer named Fynn** / **was tinkering with / Cursor's OpenAI-compatible API** / **and discovered a certain model ID.**
🔻 **发布后不到 24 小时，一位名为 Fynn 的开发者在捣鼓 Cursor 的 OpenAI 兼容 API 时，发现了一个特定的模型 ID。**

> - **Tinker** [ˈtɪŋkər] `v. [Intransitive]` Attempt to repair or improve something in a casual or desultory way. (修补；捣鼓；瞎弄)
>   - *Collocation:* **Tinker with something**.
> - **Compatible** [kəmˈpætəbl] `adj.` Able to exist or occur together without conflict. (兼容的)
>   - *Noun:* **Compatibility**.
>   - *Antonym:* **Incompatible**.

---

🔹 **accounts/anysphere/models/kimi-k2p5-rl-0317-s515-fast**
🔸 **(This is the technical ID identifier / for the model.)**
🔻 **(这是该模型的后端技术标识符。)**

> - **[Entity] Anysphere:** Cursor 的母公司名称，由几位 MIT 毕业生创立。

---

🔹 **このIDを分解すると、全てが読めます。**
🔸 **Breaking down this ID** / **reveals everything.**
🔻 **将这个 ID 分解后，一切便昭然若揭。**

> - **Break down** [phrasal verb] To divide into smaller parts in order to analyze. (分解；分析)
>   - *Synonym:* **Analyze**, **Dissect**.

---

🔹 **パーツ | 意味**
🔸 **Component / Meaning**
🔻 **组成部分 | 含义**

---

🔹 **anysphere | Cursorの親会社名**
🔸 **anysphere | The name of Cursor's parent company**
🔻 **anysphere | Cursor 的母公司名称**

> - **Parent company** [n. [C]] A company that owns enough voting stock in another firm to control management and operations. (母公司)

---

🔹 **kimi-k2p5 | Kimi K2.5（Moonshot AIのモデル）**
🔸 **kimi-k2p5 | Kimi K2.5 (Moonshot AI's model)**
🔻 **kimi-k2p5 | Kimi K2.5（月之暗面公司的模型）**

---

🔹 **rl | 強化学習（Reinforcement Learning）**
🔸 **rl | Reinforcement Learning**
🔻 **rl | 强化学习**

---

🔹 **0317 | 2026年3月17日（学習日）**
🔸 **0317 | March 17, 2026 (Training date)**
🔻 **0317 | 2026 年 3 月 17 日（训练日期）**

---

🔹 **s515 | バージョン識別子**
🔸 **s515 | Version identifier**
🔻 **s515 | 版本标识符**

> - **Identifier** [aɪˈdentɪfaɪər] `n. [C]` A sequence of characters used to identify or refer to a program element. (标识符)

---

🔹 **fast | 高速配信バリアント**
🔸 **fast | High-speed delivery variant**
🔻 **fast | 高速推理变体**

> - **Variant** [ˈværiənt] `n. [C]` A version of something that differs in some respect from other forms of the same thing. (变体；变型)
>   - *Note:* 在 AI 中常指模型的不同规模（如 small, base, large）或优化版本。

---

🔹 **つまりComposer 2は、中国のAI企業Moonshot AIが公開しているオープンウェイトモデル「Kimi K2.5」をベースに、コーディング用の強化学習をかけたものでした。**
🔸 **In other words, / Composer 2 was based on / "Kimi K2.5," / an open-weight model / released by the Chinese AI firm Moonshot AI, / with reinforcement learning applied / for coding purposes.**
🔻 **换句话说，Composer 2 是以中国 AI 企业月之暗面（Moonshot AI）公开的开放权重模型“Kimi K2.5”为基础，针对编程进行了强化学习后的产物。**

> - **Open-weight** [adj.] Refers to AI models where the parameters (weights) are public, but the training code or data might not be. (开放权重的)
>   - *Distinction:* 与 **Open-source** (开源) 不同，开放权重仅提供训练好的“脑细胞结构”，不一定提供“配方”。
> - **Apply** [əˈplaɪ] `v.` Put into operation or use. (应用；实施)
>   - *Irregular:* Applied (past).

---

🔹 **Cursorの発表ブログにもリリースノートにも、「Kimi K2.5」の文字はどこにもありません。**
🔸 **The name "Kimi K2.5"** / **does not appear anywhere** / **in Cursor's announcement blog / or the release notes.**
🔻 **在 Cursor 的发布博客和更新日志（Release Notes）中，完全没有提到“Kimi K2.5”这个词。**

> - **Release notes** [n. [plural]] Documents that are distributed with software products when these products are updated. (发布说明；更新日志)

---

🔹 **CursorのOpenAIベースURLをいじってたらこれが出てきた。**
🔸 **I was messing with / Cursor's OpenAI base URL / and this popped up.**
🔻 **我捣鼓 Cursor 的 OpenAI 基础 URL 时，这玩意儿弹了出来。**

> - **Mess with** [phrasal verb] To meddle or interfere with something. (摆弄；折腾)
> - **Pop up** [phrasal verb] To appear or occur suddenly. (突然出现；弹出)

---

🔹 **つまりComposer 2はKimi K2.5にRLかけただけ。せめてモデルIDくらいリネームしとけよ。**
🔸 **Basically, / Composer 2 is just Kimi K2.5 / with RL applied. / They could have / at least renamed the model ID.**
🔻 **也就是说 Composer 2 只是给 Kimi K2.5 做了下强化学习。好歹把模型 ID 给改了吧。**

> - **Basically** [ˈbeɪsɪkli] `adv.` Used to indicate that a statement summarizes the most important aspects. (基本上；总的说来)
> - **At least** [idiom] Not less than; if nothing else. (至少)

---

🔹 **Composer 2はどんなAIモデルなのか**
🔸 **What kind of AI model** / **is Composer 2?**
🔻 **Composer 2 究竟是什么样的 AI 模型？**

---

🔹 **CursorはComposer 2を「自社で最も高性能なコーディングモデル」として発表しました。**
🔸 **Cursor announced Composer 2** / **as "the company's highest-performance coding model."**
🔻 **Cursor 将 Composer 2 作为“公司内部性能最强的编程模型”发布。**

> - **High-performance** [adj.] Capable of operating at high speed or with great efficiency. (高性能的)

---

🔹 **「継続的な事前学習」と「スケールした強化学習」を独自の技術革新として強調していました。**
🔸 **They emphasized** / **"continual pre-training"** / **and "scaled reinforcement learning"** / **as their unique technological innovations.**
🔻 **他们强调“持续预训练”和“大规模强化学习”是其独有的技术创新。**

> - **Emphasize** [ˈemfəsaɪz] `v.` Give special importance or prominence to something. (强调)
>   - *Synonym:* **Highlight**, **Stress**.
> - **Innovation** [ˌɪnəˈveɪʃn] `n. [C/U]` A new method, idea, product, etc. (创新)
>   - *Verb:* **Innovate**.
> - **Continual** [kənˈtɪnjuəl] `adj.` Forming a sequence in which the same action or event is repeated frequently. (持续的)
>   - *Distinction:* **Continual** 指断断续续但频繁发生；**Continuous** 指完全没有中断。

---

🔹 **技術的には「compaction-in-the-loop reinforcement learning」と呼ばれる手法が使われています。**
🔸 **Technically,** / **a method called / "compaction-in-the-loop reinforcement learning" / is being utilized.**
🔻 **在技术上，其使用了被称为“循环压缩强化学习”（compaction-in-the-loop RL）的方法。**

> - **Utilize** [ˈjuːtəlaɪz] `v.` Make practical and effective use of. (利用)
>   - *Academic Note:* 比 use 更正式。

---

🔹 **生成がトークン数の上限に達すると、モデルが自分のコンテキストを約1,000トークンに圧縮してから続きを書く。**
🔸 **When generation / reaches the token limit,** / **the model compresses its own context / to approximately 1,000 tokens / before continuing to write.**
🔻 **当生成内容达到 Token 数量上限时，模型会将自己的上下文压缩到约 1000 个 Token，然后再继续编写。**

> - **Compress** [kəmˈpres] `v.` Flatten by pressure; squeeze or press. (压缩)
> - **Approximately** [əˈprɒksɪmətli] `adv.` Used to show that something is almost, but not completely, accurate or exact. (大约)
>   - *Synonym:* **Roughly**, **Around**.
> - **Token**: AI 处理文本的基本单位，通常 1 个 Token 约等于 0.75 个英文单词。

---

🔹 **この要約を学習ループに組み込んだことで、長いコードベースでも破綻しにくくなったとされています。**
🔸 **By incorporating this summarization / into the learning loop,** / **it is said / that the model is less likely / to break down / even with long codebases.**
🔻 **通过将这种摘要机制整合进学习循环中，据说即使在长代码库下，模型也不容易出现崩溃或逻辑断层。**

> - **Incorporate** [ɪnˈkɔːrpəreɪt] `v.` Take in or contain something as part of a whole; include. (合并；整合)
>   - *Collocation:* **Incorporate A into B**.
> - **Summarization** [ˌsʌməraɪˈzeɪʃn] `n. [U]` The act of expressing the most important facts or ideas about something in a short and clear form. (摘要；总结)
> - **Codebase**: 代码库。

---

🔹 **技術自体は評価に値します。問題は、その土台がどこから来たのかを一切言わなかったことです。**
🔸 **The technology itself / is worthy of praise.** / **The problem is / that they failed to mention / where the foundation came from.**
🔻 **技术本身值得肯定。问题在于，他们完全没有提及这一技术底座究竟源自何处。**

> - **Worthy of** [adj. phrase] Deserving effort, attention, or respect. (值得...的)
>   - *Example:* **Worthy of praise/notice**.
> - **Foundation** [faʊnˈdeɪʃn] `n. [C]` The lowest load-bearing part of a building; an underlying basis or principle. (地基；底座；基础)

---

🔹 **Kimi K2.5とは何か、なぜ問題なのか**
🔸 **What is Kimi K2.5,** / **and why is it a problem?**
🔻 **什么是 Kimi K2.5？为什么这会成为一个问题？**

---

🔹 **Kimi K2.5は、中国のAIスタートアップMoonshot AIが開発したオープンウェイトモデルです。**
🔸 **Kimi K2.5 is / an open-weight model** / **developed by the Chinese AI startup / Moonshot AI.**
🔻 **Kimi K2.5 是由中国 AI 初创公司月之暗面（Moonshot AI）开发的开放权重模型。**

> - **Startup** [ˈstɑːrtʌp] `n. [C]` A newly established business. (初创企业)

---

🔹 **コーディング・画像認識・エージェント動作を1つのモデルで処理でき、「Agent Swarm」という機能では最大100の分身を同時に動かしてタスクを並列処理できます。**
🔸 **It can handle / coding, image recognition, and agent actions / with a single model;** / **its "Agent Swarm" feature / can simultaneously run / up to 100 "clones" / to process tasks in parallel.**
🔻 **它能用单一模型处理编程、图像识别和智能体动作，其“Agent Swarm”（智能体集群）功能可同时运行多达 100 个分身，并行处理任务。**

> - **Simultaneously** [ˌsaɪmlˈteɪniəsli] `adv.` At the same time. (同时地)
> - **Clone** [kləʊn] `n. [C]` A person or thing that regards as identical to another. (分身；克隆体)
> - **In parallel** [idiom] Occurring at the same time and having some relation to each other. (并行地)

---

🔹 **オープンウェイトとは、モデルの重み（パラメータ）が公開されていて、誰でもダウンロードして使えるという意味です。**
🔸 **"Open-weight" means / that the model's weights (parameters) / are public,** / **allowing anyone / to download and use them.**
🔻 **“开放权重”意味着模型的权重（参数）是公开的，任何人都可以下载并使用。**

---

🔹 **ただし「オープンソース」とは違い、使い方にはライセンスの制限があります。**
🔸 **However, / unlike "open source,"** / **there are license restrictions / on its usage.**
🔻 **然而，与“开源”不同，其使用方式受到许可证的限制。**

> - **Restriction** [rɪˈstrɪkʃn] `n. [C/U]` A limiting condition or measure. (限制)
>   - *Verb:* **Restrict**.

---

🔹 **そしてこのライセンスが、今回の騒動の核心です。**
🔸 **And this license** / **is at the heart of / the current controversy.**
🔻 **而这个许可证，正是此次风波的核心所在。**

> - **At the heart of** [idiom] To be the most important part of something. (是...的核心)

---

🔹 **Kimi K2.5のライセンスはどうなっているか**
🔸 **What are the terms / of the Kimi K2.5 license?**
🔻 **Kimi K2.5 的授权条款是怎样的？**

---

🔹 **Kimi K2.5のライセンスは「Modified MIT License」で、こう書かれています。**
🔸 **The Kimi K2.5 license / is a "Modified MIT License,"** / **which states the following:**
🔻 **Kimi K2.5 采用的是“修订版 MIT 许可证”，内容如下：**

---

🔹 **月間アクティブユーザー1億人超、または月間売上2,000万ドル超の製品・サービスに使用する場合、ユーザーインターフェース上に「Kimi K2.5」を目立つ形で表示しなければならない**
🔸 **For use in products or services / with over 100 million monthly active users / or over $20 million in monthly revenue,** / **"Kimi K2.5" must be / prominently displayed / on the user interface.**
🔻 **若用于月活跃用户超过 1 亿或月营收超过 2000 万美元的产品/服务，必须在用户界面显著位置标明“Kimi K2.5”。**

> - **Monthly active users (MAU)**: 月活跃用户。
> - **Revenue** [ˈrevənjuː] `n. [U]` Income, especially when of a company or organization. (营收；收入)
> - **Prominently** [ˈprɒmɪnəntli] `adv.` In a way that is easily seen or noticed. (显著地；醒目地)

---

🔹 **ポイントは2点あります。**
🔸 **There are / two key points.**
🔻 **关键点有两处。**

---

🔹 **1. この義務は派生著作物にも明示的に適用されると書かれています。**
🔸 **1. It states / that this obligation / explicitly applies / to derivative works as well.**
🔻 **1. 条款规定，该义务明确适用于“派生作品”。**

> - **Obligation** [ˌɒblɪˈɡeɪʃn] `n. [C/U]` An act or course of action to which a person is morally or legally bound. (义务)
> - **Explicitly** [ɪkˈsplɪsɪtli] `adv.` In a clear and detailed manner, leaving no room for confusion. (明确地)
>   - *Antonym:* **Implicitly** (含蓄地).
> - **Derivative work** [n. [C]] A work based on or derived from one or more already existing works. (派生作品；衍生作品)

---

🔹 **つまり「強化学習をかけたから別モデルだ」という抗弁は通りにくい**
🔸 **In other words, / the defense that / "it's a different model / because we applied RL" / is unlikely to hold up.**
🔻 **也就是说，“因为加了强化学习所以是不同模型”这种抗辩理由很难站得住脚。**

> - **Defense** [dɪˈfens] `n. [C/U]` The action of defending from or resisting attack; a justification. (辩护；抗辩)
> - **Hold up** [phrasal verb] To remain strong or successful; to be valid. (站得住脚；经得起推敲)

---

🔹 **2. Cursorの年間売上は約20億ドル（ARR）、月商に換算すると約1億6,700万ドル。閾値の8倍以上です**
🔸 **2. Cursor's annual revenue / is approximately $2 billion (ARR), / which translates to / about $167 million per month.** / **This is more than / eight times the threshold.**
🔻 **2. Cursor 的年营收约为 20 亿美元（ARR），换算成月营收约为 1.67 亿美元。这是门槛金额的 8 倍以上。**

> - **ARR (Annual Recurring Revenue)**: 年度经常性收入。SaaS 行业的关键指标。
> - **Translate to** [v.] To result in; to be equivalent to. (转化；换算成)
> - **Threshold** [ˈθreʃhəʊld] `n. [C]` The level or point at which something would happen. (门槛；阈值)

---

🔹 **にもかかわらず、CursorのUIには「Composer 2」としか表示されていません。**
🔸 **Nevertheless, / Cursor's UI / only displays / "Composer 2."**
🔻 **尽管如此，Cursor 的界面上仅显示了“Composer 2”。**

> - **Nevertheless** [ˌnevəðəˈles] `adv.` In spite of that; notwithstanding. (然而；尽管如此)
>   - *IELTS Note:* 极佳的转折词。

---

🔹 **ブログ記事にもドキュメントにも、Kimi K2.5の文字は一切ありません。**
🔸 **There is no mention / of Kimi K2.5 / in either the blog posts / or the documentation.**
🔻 **无论在博客文章还是文档中，都完全没有提到 Kimi K2.5。**

---

🔹 **Moonshot AIはどう反応したか**
🔸 **How did / Moonshot AI respond?**
🔻 **月之暗面（Moonshot AI）有何反应？**

---

🔹 **Moonshot AI側からは複数の動きがありました。**
🔸 **There were / several moves / from Moonshot AI's side.**
🔻 **月之暗面方面出现了多项动作。**

---

🔹 **少なくとも2名のMoonshot社員がSNSで「ライセンス違反だ」と投稿し、その後削除**
🔸 **At least two Moonshot employees / posted "It's a license violation" / on SNS, / and later deleted the posts.**
🔻 **至少有两名月之暗面员工在社交媒体上发布了“违反授权协议”的贴子，随后将其删除。**

---

🔹 **プリトレーニング責任者のYulun Duが、トークナイザーの類似性を指摘し、ライセンス遵守について公に疑問を呈した**
🔸 **Yulun Du, / head of pre-training, / pointed out / the similarity of the tokenizers / and publicly questioned / license compliance.**
🔻 **预训练负责人杜煜伦指出分词器（Tokenizer）具有相似性，并公开对许可协议的遵守情况表示怀疑。**

> - **Compliance** [kəmˈplaɪəns] `n. [U]` The action or fact of complying with a wish or command. (合规性；遵守)
>   - *Verb:* **Comply (with)**.
> - **[Figure] Yulun Du (杜煜伦):** 月之暗面技术核心成员之一。

---

🔹 **投稿が削除されたことから、水面下で交渉が進んでいる可能性があります。**
🔸 **Since the posts were deleted, / it is possible / that negotiations / are proceeding / behind the scenes.**
🔻 **从贴子被删除这一点来看，双方可能正在幕后进行谈判。**

> - **Negotiation** [nɪˌɡəʊʃiˈeɪʃn] `n. [C/U]` Discussion aimed at reaching an agreement. (谈判)
> - **Behind the scenes** [idiom] Out of public view; secretly. (在幕后；在水面下)

---

🔹 **ただ、責任者レベルが公に発言している以上、単なる誤解で終わる話ではなさそうです。**
🔸 **However, / as long as / leadership-level individuals / are speaking out publicly, / this is unlikely to end / as a mere misunderstanding.**
🔻 **不过，既然负责人级别的人物都已公开表态，这恐怕不像是能以“单纯的误会”收场的事情。**

> - **Leadership-level** [adj.] 指公司高层或核心负责人。
> - **Mere** [mɪər] `adj.` Used to emphasize how small or insignificant someone or something is. (仅仅的；单纯的)

---

🔹 **Cursorはなぜ黙っているのか**
🔸 **Why is Cursor / remaining silent?**
🔻 **Cursor 为何保持缄默？**

---

🔹 **この記事の執筆時点で、Cursorは公式に何もコメントしていません。**
🔸 **As of / the writing of this article, / Cursor has made / no official comment.**
🔻 **截至本文撰写时，Cursor 尚未做出任何官方回应。**

> - **As of** [prep.] Indicating a time or date from which something begins or at which it exists. (截至；自...)

---

🔹 **背景にはビジネス上の事情があるかもしれません。**
🔸 **There may be / business-related reasons / in the background.**
🔻 **其背后可能存在商业上的考量。**

---

🔹 **Cursorの親会社Anysphereは293億ドルの企業評価額を受けており、500億ドルへの引き上げを目指しているとされています。**
🔸 **Cursor's parent company, Anysphere, / is valued at $29.3 billion / and is reportedly aiming / to raise its valuation / to $50 billion.**
🔻 **Cursor 的母公司 Anysphere 目前估值为 293 亿美元，据称正寻求将其估值提升至 500 亿美元。**

> - **Valuation** [ˌvæljuˈeɪʃn] `n. [C/U]` An estimation of something's worth, especially one carried out by a professional appraiser. (估值)
> - **Reportedly** [rɪˈpɔːrtɪdli] `adv.` According to what some say or report. (据报道；据传)

---

🔹 **その交渉過程で「自社開発モデル」の看板は重要なセールスポイントだったはずです。**
🔸 **In that negotiation process, / the label of / an "in-house developed model" / must have been / a crucial selling point.**
🔻 **在这一谈判过程中，“自研模型”的招牌无疑是一个关键的卖点。**

> - **Crucial** [ˈkruːʃl] `adj.` Decisive or critical, especially in the success or failure of something. (至关重要的)
> - **Selling point** [n. [C]] A feature that makes a product more attractive to buyers. (卖点)

---

🔹 **「実は他社のモデルに強化学習をかけただけでした」と認めることは、そのストーリーを根底から覆しかねません。**
🔸 **Admitting that / "it was actually just / another company's model / with RL applied" / could undermine that narrative / to its very core.**
🔻 **承认“其实只是给别家模型做了强化学习”，可能会从根基上颠覆其商业叙事。**

> - **Undermine** [ˌʌndəˈmaɪn] `v.` Lessen the effectiveness, power, or ability of, especially gradually or insidiously. (削弱；动摇；破坏)
> - **Narrative** [ˈnærətɪv] `n. [C]` A representation of a particular situation or process in such a way as to reflect or conform to an overarching set of aims or values. (叙事；说法)
> - **To the core** [idiom] Completely; entirely. (彻底地)

---

🔹 **「強化学習したら別モデル」は通用するのか**
🔸 **Does the argument / "it's a different model / if RL is applied" / hold weight?**
🔻 **“强化学习后即为新模型”的说法行得通吗？**

---

🔹 **Cursorが取りうる反論の1つは「RLで十分に改変したから、もはや派生著作物ではない」という主張です。**
🔸 **One possible counterargument / Cursor could make / is the claim that / "because we modified it / sufficiently through RL, / it is no longer / a derivative work."**
🔻 **Cursor 可能采取的辩解之一是：“由于通过强化学习进行了充分修改，它已不再属于派生作品。”**

> - **Counterargument** [ˈkaʊntərɑːrɡjumənt] `n. [C]` An argument or set of reasons put forward to oppose an idea or theory developed in another argument. (反论；抗辩)
> - **Sufficiently** [səˈfɪʃntli] `adv.` To a degree that is enough or satisfactory. (充分地)

---

🔹 **しかし、Kimi K2.5のライセンスは派生著作物にも帰属表示義務が及ぶと明記しています。**
🔸 **However, / the Kimi K2.5 license / explicitly states / that the attribution obligation / extends to derivative works.**
🔻 **然而，Kimi K2.5 的授权协议明确规定，署名义务也涵盖派生作品。**

> - **Attribution** [ˌætrɪˈbjuːʃn] `n. [U]` The action of ascribing a work or remark to a particular author, artist, or person. (归属；署名)

---

🔹 **モデルの重みをそのまま出発点にしている以上、どれだけRLをかけても「ゼロから作った」とは言えません。**
🔸 **As long as / the model weights / are used as the starting point, / no matter how much RL is applied, / one cannot say / it was "built from scratch."**
🔻 **只要是以模型的权重作为起点，无论进行多少强化学习，都不能说是“从零开始打造”的。**

> - **From scratch** [idiom] From the very beginning, without using anything that already exists. (从零开始)

---

🔹 **HNのコメント欄では、こんな意見が出ています。**
🔸 **In the comment section / of HN, / the following opinions / have emerged.**
🔻 **在 HN 的评论区中，出现了如下观点：**

> - **[Entity] HN (Hacker News):** 硅谷著名的技术新闻社区，由 Y Combinator 运营。

---

🔹 **「Opus 4.6を打ち負かすコーディング性能は素直に凄い。でも、それを隠す理由がわからない」**
🔸 **"The coding performance / that beats Opus 4.6 / is honestly amazing. / However, / I don't understand the reason / for hiding it."**
🔻 **“能够击败 Opus 4.6 的编程性能确实很厉害。但我不明白为什么要隐瞒真相。”**

---

🔹 **技術的な功績と、帰属表示の義務は別の話です。**
🔸 **Technological achievement / and the obligation for attribution / are separate issues.**
🔻 **技术成就与署名义务是两码事。**

---

🔹 **優れた成果を出したなら、なおさら土台への敬意を示すべきだった、というのがコミュニティの大勢です。**
🔸 **The general consensus / in the community / is that / if they achieved great results, / they should have / shown all the more respect / for the foundation.**
🔻 **社区的主流观点认为，既然取得了如此优秀的成果，就更应该对技术底座表示尊重。**

> - **Consensus** [kənˈsensəs] `n. [singular/U]` A general agreement. (共识)
> - **All the more** [idiom] Even more than before. (更加)

---

🔹 **開発者コミュニティの反応**
🔸 **Reactions / from the developer community**
🔻 **开发者社区的反应**

---

🔹 **Hacker Newsでは210ポイントを超えるスレッドになり、X（旧Twitter）でも急速に拡散しました。**
🔸 **It became a thread / with over 210 points on Hacker News, / and it spread rapidly / on X (formerly Twitter).**
🔻 **该话题在 Hacker News 上获得了超过 210 分的热度，并在 X（原 Twitter）上迅速传播。**

---

🔹 **反応は概ね3つに分かれています。**
🔸 **Reactions / are generally divided / into three categories.**
🔻 **反应大致分为三类。**

---

🔹 **批判派 | $2B企業がOSSの帰属表示を隠すのは不誠実**
🔸 **Critics | It is dishonest / for a $2B company / to hide the attribution / of an OSS model.**
🔻 **批判派 | 一家年营收 20 亿的公司隐瞒开源模型的署名，这是不诚实的表现。**

---

🔹 **擁護派 | OSSモデル+RLは正当な技術活用。結果で評価すべき**
🔸 **Supporters | Using an OSS model with RL / is a legitimate use of technology. / It should be judged / by the results.**
🔻 **拥护派 | 开源模型结合强化学习是正当的技术应用。应该以结果论成败。**

> - **Legitimate** [lɪˈdʒɪtɪmət] `adj.` Conforming to the law or to rules. (合法的；正当的)

---

🔹 **懐疑派 | 自社モデル開発を謳って$50B評価を目指す姿勢が問題**
🔸 **Skeptics | The issue lies / in the stance of / aiming for a $50B valuation / by claiming in-house model development.**
🔻 **怀疑派 | 问题在于其一边宣称自研模型，一边寻求 500 亿估值的态度。**

> - **Skeptic** [ˈskeptɪk] `n. [C]` A person inclined to question or doubt accepted opinions. (怀疑论者)

---

🔹 **Cursor Composer 2のベースモデルはKimi K2.5のようだ！**
🔸 **It seems / that the base model of Cursor Composer 2 / is Kimi K2.5!**
🔻 **Cursor Composer 2 的基础模型似乎是 Kimi K2.5！**

---

🔹 **Kimiモデルをコーディング性能向上のために強化学習でさらにポストトレーニングしている。**
🔸 **They are further post-training / the Kimi model / with reinforcement learning / to improve coding performance.**
🔻 **他们通过强化学习对 Kimi 模型进行了进一步的后训练，以提升编程性能。**

> - **Post-training**: 后训练。在基础模型训练完成后进行的微调或强化学习阶段。

---

🔹 **Cursorがゼロから基盤モデルを作るわけがないので、おそらく本当だろう。**
🔸 **Since there's no way / Cursor would build a foundation model / from scratch, / it's likely true.**
🔻 **鉴于 Cursor 不可能从零开始构建基础模型，这事儿大概率是真的。**

---

🔹 **今後の展開としては3つのシナリオが考えられます。**
🔸 **As for future developments, / three scenarios / can be considered.**
🔻 **关于后续进展，可以预见三种剧本。**

---

🔹 **帰属表示を追加して和解する、RLによる改変が「十分な変形」だと主張して争う、あるいは別のベースモデルでComposer 2を作り直す。**
🔸 **Settling by adding attribution, / disputing by claiming / that the RL modification is a "sufficient transformation," / or rebuilding Composer 2 / with a different base model.**
🔻 **通过补上署名来达成和解；坚持认为强化学习构成了“充分变形”并进行抗争；或者换一个基础模型重做 Composer 2。**

> - **Settle** [ˈsetl] `v.` Resolve or reach an agreement about (an argument or problem). (解决；和解)
> - **Transformation** [ˌtrænsfəˈmeɪʃn] `n. [C/U]` A thorough or dramatic change in form or appearance. (转变；变形)

---

🔹 **どの道を選んでも、AIコーディングツール業界に前例を作ることになります。**
🔸 **Whichever path they choose, / it will set a precedent / in the AI coding tool industry.**
🔻 **无论选择哪条路，都将为 AI 编程工具行业开创先例。**

> - **Precedent** [ˈpresɪdənt] `n. [C]` An earlier event or action that is regarded as an example or guide to be considered in subsequent similar circumstances. (先例；前例)
>   - *Collocation:* **Set a precedent** (开创先例).

---

🔹 **AIコーディングツールの「中身」は誰が検証するのか**
🔸 **Who will verify / the "insides" / of AI coding tools?**
🔻 **谁来验证 AI 编程工具的“内里”？**

---

🔹 **私たちはAIツールに月額20ドルを払い、その中で動いているモデルが何なのかを知らないまま使っています。**
🔸 **We pay $20 a month / for AI tools / and use them / without knowing / what model is running inside.**
🔻 **我们每月为 AI 工具支付 20 美元，却在对其内部运行模型一无所知的情况下使用着它们。**

---

🔹 **食品なら原材料表示が義務づけられているのに、AIモデルにはそれがない。**
🔸 **While ingredient labeling / is mandatory for food, / there is no such thing / for AI models.**
🔻 **如果是食品，强制要求标注原材料，但 AI 模型却没有这种规定。**

> - **Mandatory** [ˈmændətəri] `adj.` Required by law or rules; compulsory. (强制的；义务的)

---

🔹 **映画で言えば、ゴーストライターが書いた脚本にスター監督が自分の名前だけを載せた状態です。**
🔸 **In cinematic terms, / it's like a star director / putting only their own name / on a script / written by a ghostwriter.**
🔻 **打个电影界的比方，这就像是明星导演在代笔编剧写的剧本上只署了自己的名字。**

> - **Cinematic** [ˌsɪnəˈmætɪk] `adj.` Relating to movies. (电影的)
> - **Ghostwriter** [ˈɡəʊstraɪtər] `n. [C]` A person whose job is to write material for someone else who is the named author. (代笔人；枪手)

---

🔹 **作品の出来が良くても、クレジットを奪ったら業界の信頼が壊れます。**
🔸 **Even if the work is good, / if you take away the credit, / the industry's trust / will be destroyed.**
🔻 **即使作品本身很优秀，但如果剥夺了应有的署名权，行业的信任基础就会崩塌。**

> - **Credit** [ˈkredɪt] `n. [U]` Public acknowledgment or praise, given to a person whose name is linked with a specific action or accomplishment. (声望；信誉；署名)

---

🔹 **Cursorが今後どう対応するかはわかりません。**
🔸 **It is unclear / how Cursor / will respond in the future.**
🔻 **尚不清楚 Cursor 今后将如何应对。**

---

🔹 **ただ、1つだけ確かなことがあります。**
🔸 **However, / one thing / is certain.**
🔻 **但有一点是可以肯定的。**

---

🔹 **APIに残ったモデルIDは、自分の名前を消し忘れたゴーストライターのようなものでした。**
🔸 **The model ID / remaining in the API / was like a ghostwriter / who forgot to erase / their own name.**
🔻 **残留在 API 中的模型 ID，就像是一个忘了擦掉自己名字的代笔编剧。**

---

🔹 **そして、インターネットはその名前を見逃しませんでした。**
🔸 **And / the internet / did not miss that name.**
🔻 **而互联网并没有漏掉那个名字。**

---

🔹 **参照元 / 1. Fynn (@fynnso) — モデルID発見のツイート / ...**
🔸 **References** / **1. Fynn (@fynnso) — Tweet discovering the model ID / ...**
🔻 **参考来源** / **1. Fynn (@fynnso) — 发现模型 ID 的推文 / ...**

---

**说明：** 原文具体 URL 未提供；若你补充 kkm-mako.com 上该文链接，可将 frontmatter 中 `source_url` 填入以便回溯。
