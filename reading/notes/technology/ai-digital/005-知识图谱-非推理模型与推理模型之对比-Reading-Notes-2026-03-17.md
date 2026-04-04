---
title: 知识图谱：非推理模型与推理模型之对比 (Knowledge Map: Non-Reasoning vs. Reasoning Models)
source: 行业技术深度分析报告 (Technical Deep Dive/Whitepaper)
source_url:
author:
date: 2026-03-17
category: reading/notes/technology/ai-digital
tags:
  - 推理模型
  - 非推理模型
  - 通用模型
  - 模型对比
  - 训练目标
  - 训练信号
  - 过程监督
  - 思维链
  - CoT
  - 推理行为
  - 延迟
  - 吞吐量
  - 成本
  - 可控性
  - reasoning_effort
  - 准确性
  - 可靠性
  - 幻觉
  - 透明度
  - 可解释AI
  - 工具使用
  - Agent
  - 隐私
  - 英语精读
  - 知识图谱
---

```markdown
# 知识图谱：非推理模型与推理模型之对比 (Knowledge Map: Non-Reasoning vs. Reasoning Models)

## 🔹 文章结构概览 (Article Structure Overview)

1.  **引言 (Introduction)**
    *   **总体 (Overall):** 介绍AI领域中通用模型（非推理）与推理模型的分类。
    *   **段落 (Paragraph):** 指出两者核心架构相似，但在推理过程中的目标和行为存在显著差异。
    *   **内部 (Internal):** 明确本文将从训练信号、推理行为、延迟/吞吐量、成本、可控性、准确性、幻觉、透明度、工具使用及隐私等维度展开论述。

2.  **核心差异维度解析 (Core Dimensions of Difference)**
    *   **训练目标 (Training Objectives):**
        *   *非推理:* 侧重最终答案的正确性（预测下一词、RLHF）。
        *   *推理:* 侧重“思考过程”（过程监督、思维链奖励）。
    *   **推理行为 (Inference Behavior):**
        *   *非推理:* 直接给出答案，倾向简洁。
        *   *推理:* 逐步拆解问题，输出冗长但结构化。
    *   **性能指标 (Performance: Latency & Throughput):**
        *   推理模型由于计算量大，延迟更高，吞吐量更低（如Azure o1 vs GPT-4o）。
    *   **成本考量 (Cost):**
        *   更多Token意味着更高昂的API调用或算力成本。
    *   **可控性与提示词 (Controllability):**
        *   推理模型支持“推理强度”调节，对“Step-by-step”指令更敏感。
    *   **准确性与可靠性 (Accuracy):**
        *   *推理模型:* 擅长复杂逻辑/数学，但在简单任务中可能“过度思考”。
        *   *非推理:* 在创意/简单任务中更灵活直接。
    *   **幻觉特征 (Hallucinations):**
        *   *非推理:* 事实性错误。
        *   *推理:* 逻辑链条误导，更具欺骗性。
    *   **透明度与调试 (Transparency):**
        *   推理模型提供中间步骤，更易于Debug和符合AI治理要求。
    *   **工具使用 (Tool Use):**
        *   推理模型天然适配Agent架构，擅长调用外部API。
    *   **隐私考量 (Privacy):**
        *   中间思考过程可能泄露敏感原文。

3.  **总结 (Summary)**
    *   两者并非简单的优劣之分，而是适用于不同的应用场景。

## 🔹 背景信息 (Background Information)
- **来源:** 行业技术深度分析报告 (Technical Deep Dive/Whitepaper)
- **作者:** 暂无明确个人署名，通常为AI研究机构或技术咨询团队。
- **背景:** 随着OpenAI o1等推理模型的兴起，业界亟需建立针对“Reasoning LLMs”的新评价体系。
- **涉及机构:** 
    - **OpenAI:** 全球领先的AI研究公司，ChatGPT开发者。
    - **IBM:** 国际商业机器公司，老牌技术巨头，近期在LLM效率与逻辑方面有大量研究。
    - **Azure:** 微软的云计算平台，提供OpenAI模型的企业级托管服务。
    - **NIST:** 美国国家标准与技术研究院。
    - **EU AI Act:** 欧盟人工智能法案。
```

---

🔹 **Non-Reasoning / vs. / Reasoning Models**
🔸 **非推理模型 / 与 / 推理模型之对比**
> **Categorize** [ˈkætəɡəraɪz] *v.* 把…分类 (To place in a particular class or group). 
> 【考点】**Categorize A into B** 将A分类为B。名词形式为 **Categorization**。
> 【近义词】Classify, Sort, Group.

🔹 **As / the AI landscape / diversifies, / it’s useful / to categorize models / into general-purpose (non-reasoning) LLMs / and reasoning LLMs.**
🔸 **随着 / 人工智能领域 / 变得日益多元化， / 将模型分类为 / 通用型（非推理）大语言模型 / 和推理型大语言模型 / 是非常有用的。**
> 1. **Landscape** [ˈlændskeɪp] *n.* 领域，前景 (The overall situation or field of activity). 
> 【熟词僻义】原意为“风景、景观”，在学术/商务英语中常引申为“行业格局、态势”。
> 【例句】The political landscape has changed significantly. 政治格局发生了重大变化。
> 2. **Diversify** [daɪˈvɜːrsɪfaɪ] *v.* 变得多样化 (To become more varied or different). 
> 【词性变化】**Diversity** (*n.* 多样性)；**Diverse** (*adj.* 不同的，多种多样的)。
> 3. **General-purpose** [ˈdʒenrəl ˈpɜːrpəs] *adj.* 通用的，万能的 (Having a range of different uses).
> 【反义词】Specialized, Dedicated.

🔹 **Both categories / are large language models / at their core, / often / even sharing / the same base architecture.**
🔸 **这两类 / 在核心上 / 都是大语言模型， / 通常 / 甚至共享 / 相同的基础架构。**
> 1. **Core** [kɔːr] *n.* 核心，精髓 (The central or most important part).
> 【常见短语】**At its core** 本质上，核心上。
> 2. **Architecture** [ˈɑːrkɪtektʃər] *n.* 架构，建筑学 (The complex or carefully designed structure of something).
> 【雅思考点】在IT/AI语境下指“系统架构、算法结构”。

🔹 **The difference / lies in / their objectives / and behaviors / during inference.**
🔸 **两者的区别 / 在于 / 它们在推理过程中的 / 目标 / 和行为。**
> 1. **Inference** [ˈɪnfərəns] *n.* 推理 (The process of reaching a conclusion).
> 【AI术语】在人工智能中特指模型生成答案的过程（与训练阶段相对）。
> 2. **Lie in** [laɪ ɪn] *phrasal v.* 在于 (To exist or be found in something).
> 【用法】常用于解释原因或本质。
> 【近义词】Consist in, Reside in.

🔹 **This section / delineates / those differences / in detail / — from / what they optimize for, / to / how they respond, / and / what trade-offs / they entail.**
🔸 **本节 / 详细地 / 描述了 / 那些差异 / ——从 / 它们的优化目标， / 到 / 它们如何做出响应， / 以及 / 它们涉及 / 哪些权衡。**
> 1. **Delineate** [dɪˈlɪnieɪt] *v.* 描绘，勾勒 (To describe or portray something precisely).
> 【考研/写作】高级动词，用于替代 describe。
> 2. **Trade-off** [ˈtreɪd ɔːf] *n.* 权衡，折衷 (A balance achieved between two desirable but incompatible features).
> 【用法】常指为了获得某种好处而必须牺牲另一部分。
> 3. **Entail** [ɪnˈteɪl] *v.* 牵涉，意味着 (To involve something as a necessary or inevitable part or consequence).
> 【考点】**Entail doing something**。注意其不可数名词形式没有常用用法。

🔹 **Objective / and / Training Signals:**
🔸 **目标 / 与 / 训练信号：**

🔹 **Traditional LLMs / are typically trained / (after pre-training) / with objectives / like / next-word prediction, / instruction following, / and possibly / RLHF / (Reinforcement Learning from Human Feedback) / to be helpful / and harmless.**
🔸 **传统的 LLM / 通常（在预训练之后） / 通过 / 诸如 / 下一词预测、 / 指令遵循 / 以及可能采用的 / RLHF / （人类反馈强化学习） / 等目标进行训练， / 以使其既有帮助 / 又无害。**
> 1. **Reinforcement** [ˌriːɪnˈfɔːrsmənt] *n.* 强化 (The process of encouraging or establishing a belief or pattern of behavior).
> 【词根】Re- (再次) + force (力量) + -ment (名词后缀)。
> 2. **Harmless** [ˈhɑːrmləs] *adj.* 无害的 (Not able or likely to cause harm).
> 【写作考点】AI伦理三要素：Helpful (有用), Honest (诚实), Harmless (无害)。

🔹 **Their training signal / emphasizes / producing / a correct and well-formed / final answer.**
🔸 **它们的训练信号 / 强调 / 生成 / 正确且格式良好的 / 最终答案。**
> 1. **Emphasize** [ˈemfəsaɪz] *v.* 强调 (To give special importance or prominence to something in speaking or writing).
> 【词性变化】**Emphasis** (*n.* 强调)；**Emphatic** (*adj.* 强调的)。
> 2. **Well-formed** [wel fɔːrmd] *adj.* 格式正确的，构造良好的 (Correctly following the rules of a language or system).

🔹 **In contrast, / reasoning models / incorporate / additional signals / that emphasize / the process.**
🔸 **相比之下， / 推理模型 / 融合了 / 强调 / 过程的 / 额外信号。**
> 1. **In contrast** [ɪn ˈkɑːntræst] *adv.* 与之相反，相比之下 (Used to point out a striking difference).
> 【写作】常用的逻辑转折短语。
> 2. **Incorporate** [ɪnˈkɔːrpəreɪt] *v.* 包含，合并 (To include something as part of a whole).
> 【用法】**Incorporate A into B**。

🔹 **They / often / undergo / an extra fine-tuning stage / where / they are rewarded / not only / for being correct, / but / for “showing their work” / in a useful way / [49, 16].**
🔸 **它们 / 通常 / 经历 / 一个额外的微调阶段， / 在该阶段中， / 它们不仅 / 因为正确 / 而获得奖励， / 还因为 / 以有用的方式 / “展示其工作过程” / 而获得奖励。**
> 1. **Undergo** [ˌʌndərˈɡoʊ] *v.* 经历，经受 (To experience or be subjected to something, typically something unpleasant or arduous).
> 【不规则变化】Undergo - Underwent - Undergone。
> 2. **Fine-tuning** [ˌfaɪn ˈtuːnɪŋ] *n.* 微调 (Making small adjustments to something in order to achieve the best or a desired performance).
> 【AI术语】在预训练模型基础上进行特定任务的训练。

🔹 **For example, / a reasoning model / might get / a positive reward / for outputting / a chain-of-thought / that leads to / a correct solution, / or even / for each correct / intermediate step / (process supervision) / [12].**
🔸 **例如， / 一个推理模型 / 可能会因为 / 输出 / 一个导致 / 正确解法的 / 思维链 / 而获得正向奖励， / 甚至是 / 因为每一个正确的 / 中间步骤 / （过程监督） / 而获赏。**
> 1. **Chain-of-thought** [tʃeɪn əv θɔːt] *n.* 思维链 (CoT) (A sequence of thoughts or logic).
> 【AI术语】让模型写出思考过程的技术。
> 2. **Intermediate** [ˌɪntərˈmiːdiət] *adj.* 中间的，过渡的 (Coming between two things in time, place, order, character, etc.).
> 【词根】Inter- (在……之间) + med (中间)。
> 3. **Supervision** [ˌsuːpərˈvɪʒn] *n.* 监督 (The action or process of watching and directing what someone does or how something is done).

🔹 **Non-reasoning models, / on the other hand, / might have been trained / to directly map / a question / to an answer / without any explicit / intermediate reasoning / in the output.**
🔸 **另一方面， / 非推理模型 / 可能接受的训练是 / 直接将 / 问题 / 映射到 / 答案， / 而不在输出中 / 包含任何明确的 / 中间推理。**
> 1. **On the other hand** [ɒn ði ˈʌðər hænd] *adv.* 另一方面 (Used to introduce a contrasting point of view).
> 2. **Explicit** [ɪkˈsplɪsɪt] *adj.* 明确的，直白的 (Stated clearly and in detail, leaving no room for confusion or doubt).
> 【反义词】Implicit (含蓄的，隐晦的)。
> 3. **Map** [mæp] *v.* 映射 (To associate each element of a set with an element of another set).
> 【熟词僻义】名词为“地图”，动词在数学/计算机领域指“一一对应”。

🔹 **This fundamental difference / means / reasoning models / are explicitly optimized / to use / more computation / per query / — they are taught / that thinking longer / (to a point) / is good.**
🔸 **这种根本差异 / 意味着 / 推理模型 / 经过了明确优化 / 以在 / 每次查询中 / 使用 / 更多的计算量 / ——它们被教会 / “思考得更久” / （在一定限度内） / 是有益的。**
> 1. **Fundamental** [ˌfʌndəˈmentl] *adj.* 根本的，基础的 (Forming a necessary base or core; of central importance).
> 2. **Computation** [ˌkɑːmpjuˈteɪʃn] *n.* 计算 (The action of mathematical calculation).
> 3. **Query** [ˈkwɪri] *n.* 查询，疑问 (A question, especially one addressed to an official or organization).

🔹 **A regular model, / if it can answer / in one sentence, / it will, / because / brevity / was often rewarded / during RLHF fine-tuning.**
🔸 **一个常规模型， / 如果它能用 / 一句话回答， / 它就会这样做， / 因为 / 在 RLHF 微调期间， / 简洁 / 通常会受到奖励。**
> 1. **Brevity** [ˈbrevəti] *n.* 简洁，简炼 (Concise and exact use of words in writing or speech).
> 【雅思/考研】书面语，常用短语 **Brevity is the soul of wit** (简洁是智慧的灵魂)。
> 2. **Regular** [ˈreɡjələr] *adj.* 常规的，普通的 (Ordinary; normal).

🔹 **A reasoning model / might instead / be nudged / to provide / a step-by-step answer, / because / that was set / as the ideal / in its fine-tuning.**
🔸 **相反， / 推理模型 / 可能会被引导 / 去提供 / 逐步的回答， / 因为 / 这在它的微调过程中 / 被设定为 / 理想状态。**
> 1. **Nudge** [nʌdʒ] *v.* 引导，轻推 (To coax or gently encourage someone to do something).
> 【考点】**Nudge someone to do something**。常用于行为经济学和AI对齐。
> 2. **Ideal** [aɪˈdiːəl] *n./adj.* 理想 (Satisfying one's conception of what is perfect; most suitable).

🔹 **Behavior / at / Inference:**
🔸 **推理阶段的 / 行为：**

🔹 **When you prompt / a non-reasoning model / with a question, / especially / a complex one, / it tends to / give an answer / as directly as possible.**
🔸 **当你向 / 非推理模型 / 提问时， / 尤其是 / 复杂的问题， / 它往往会 / 尽可能直接地 / 给出答案。**
> 1. **Prompt** [prɑːmpt] *v.* 提示，促使 (To encourage someone to say or do something).
> 【AI术语】名词指提示词，动词指输入提示词。
> 2. **Complex** [kəmˈpleks] *adj.* 复杂的 (Consisting of many different and connected parts).
> 【近义词】Complicated, Intricate.

🔹 **If / it’s not sure, / it might / hedge / or / produce / a generic response.**
🔸 **如果 / 它不确定， / 它可能会 / 模棱两可 / 或 / 生成 / 笼统的回应。**
> 1. **Hedge** [hedʒ] *v.* 避重就轻，避免正面回答 (To avoid making a direct statement or committing oneself).
> 【熟词僻义】原意为“树篱”，在写作/金融中指“规避、套期保值”。
> 2. **Generic** [dʒəˈnerɪk] *adj.* 通用的，种类的，无特征的 (Characteristic of or relating to a class or group of things; not specific).
> 【例句】A generic brand. 通用品牌（白牌）。

🔹 **A reasoning model, / when similarly challenged, / is more likely / to “talk through” / the problem.**
🔸 **当受到类似的挑战时， / 推理模型 / 更有可能 / 对问题进行 / “透彻的讨论”。**
> 1. **Talk through** [tɔːk θruː] *phrasal v.* 详细讨论 (To discuss something in detail to understand it or make a decision).
> 2. **Challenged** [ˈtʃælɪndʒd] *v.* 受到挑战 (To be invited to take part in a contest or to prove something).

🔹 **Even if / the final answer / is uncertain, / the model will / enumerate / what it knows, / break the question / into parts, / attempt / to solve each part, / and so on.**
🔸 **即使 / 最终答案 / 是不确定的， / 模型也会 / 列举 / 它所知道的信息， / 将问题分解 / 为若干部分， / 尝试 / 解决每一个部分， / 依此类推。**
> 1. **Enumerate** [ɪˈnuːməreɪt] *v.* 列举，枚举 (To mention a number of things one by one).
> 【词性变化】**Enumeration** (*n.*)。
> 2. **Attempt** [əˈtempt] *v.* 尝试 (To make an effort to achieve or complete something difficult).
> 【用法】**Attempt to do something**。

🔹 **This / leads to / much longer responses / on average.**
🔸 **这 / 导致了 / 平均而言 / 长得多的回复。**
> 1. **On average** [ɒn ˈævərɪdʒ] *adv.* 平均而言 (Normally; usually).
> 2. **Response** [rɪˈspɑːns] *n.* 回应 (A reaction to something).

🔹 **IBM / reported / that / reasoning models / can generate / nearly 20× more tokens / than standard models / for the same query / [19].**
🔸 **IBM / 报告称， / 推理模型 / 针对同一查询 / 产生的 Token 数量 / 几乎比标准模型 / 多出 20 倍 / [19]。**
> 1. **IBM** [ˌaɪ biː ˈem] *注*：国际商业机器公司 (International Business Machines Corporation)，美国著名的科技巨头。
> 2. **Token** [ˈtoʊkən] *n.* 令牌，代币 (A voucher that can be exchanged for goods).
> 【AI术语】文本处理的最小单位（通常约等于0.75个单词）。

🔹 **So, / one obvious / behavioral difference: / reasoning models / produce / verbose, structured outputs / (lists, stepwise derivations, numbered paragraphs), / whereas / non-reasoning models / produce / concise answers / or / a couple of paragraphs of explanation / at most.**
🔸 **因此， / 一个明显的 / 行为差异是： / 推理模型 / 产生 / 冗长且结构化的输出 / （列表、逐步推导、带编号的段落）， / 而 / 非推理模型 / 则产生 / 简洁的答案 / 或 / 最多两段解释。**
> 1. **Verbose** [vɜːrˈboʊs] *adj.* 冗长的，啰嗦的 (Using or expressed in more words than are needed).
> 【反义词】Concise (简洁的), Succinct.
> 2. **Derivation** [ˌderɪˈveɪʃn] *n.* 推导，起源 (The obtaining or developing of something from a source or origin).
> 3. **Whereas** [ˌwerˈæz] *conj.* 然而，尽管 (In contrast or comparison with the fact that).
> 【雅思/考研写作】高级连词，用于对比。

🔹 **The verbosity / is not just fluff / — it’s the model / literally performing / the task / via language.**
🔸 **这种冗长 / 不仅仅是废话 / ——它实际上是模型 / 在通过语言 / 执行 / 任务。**
> 1. **Fluff** [flʌf] *n.* 虚假信息，无用之物 (Entertainment or writing that is perceived as trivial or superficial).
> 【熟词僻义】原意为“绒毛”，此处引申为“没有营养的废话”。
> 2. **Literally** [ˈlɪtərəli] *adv.* 真正地，确实地 (Used for emphasis while not being literally true).
> 【用法】在口语中常用于强调。
> 3. **Via** [ˈvaɪə] *prep.* 通过，经由 (By way of; through).

🔹 **Latency / and / Throughput:**
🔸 **延迟 / 与 / 吞吐量：**

🔹 **Because / reasoning models / do more computation / (generating / many more tokens / per prompt, / possibly performing / multiple “internal” forward passes / if using techniques / like self-consistency / or tool use), / they are / inherently / slower / and / have lower throughput.**
🔸 **因为 / 推理模型 / 执行了更多的计算 / （在每个提示词下 / 生成 / 更多的 Token， / 如果使用了 / 诸如自一致性 / 或工具使用等技术， / 甚至可能执行 / 多次“内部”前向传递）， / 它们 / 本质上 / 更慢 / 且 / 吞吐量更低。**
> 1. **Latency** [ˈleɪtənsi] *n.* 延迟 (The delay before a transfer of data begins following an instruction for its transfer).
> 2. **Throughput** [ˈθruːpʊt] *n.* 吞吐量 (The amount of material or items passing through a system or process).
> 3. **Inherently** [ɪnˈhɪrəntli] *adv.* 内在地，本质地 (In a permanent, essential, or characteristic way).
> 【词根】Inherent (*adj.* 固有的)。
> 4. **Forward pass** [ˈfɔːrwərd pæs] *注*：神经网络中的前向传递，指数据从输入层通过各层到达输出层的过程。

🔹 **An easy / mental model: / if / a normal model / gives an answer / in 2 sentences (20 tokens) / and / a reasoning model / gives an answer / in 10 sentences (100 tokens) / with / some back-and-forth, / and if / generation speed / is, say, X tokens per second, / then / the reasoning model / will take 5x longer.**
🔸 **一个简单的 / 心理模型是： / 如果 / 一个普通模型 / 用 2 句话（20 个 Token） / 给出答案， / 而 / 一个推理模型 / 用 10 句话（100 个 Token） / 给出答案 / 并伴随 / 一些反复， / 且如果 / 生成速度 / 假设为每秒 X 个 Token， / 那么 / 推理模型 / 将花费 5 倍的时间。**
> 1. **Mental model** [ˈmentl ˈmɑːdl] *n.* 心理模型，思维模型。
> 2. **Back-and-forth** [ˌbæk ənd ˈfɔːrθ] *n.* 反复，往返 (A conversation or negotiation that involves an exchange of ideas or opinions).

🔹 **In practice, / Azure’s data / comparing models / shows / reasoning-optimized models / indeed / have higher latency.**
🔸 **在实践中， / 微软 Azure 的 / 模型对比数据 / 显示， / 推理优化模型 / 确实 / 具有更高的延迟。**
> 1. **Azure** [ˈæʒər] *注*：微软公司的公有云计算服务平台。
> 2. **Optimize** [ˈɑːptɪmaɪz] *v.* 优化 (Make the best or most effective use of a situation, opportunity, or resource).

🔹 **For instance, / one Azure test / found / their o1 reasoning model / had / an end-to-end latency / of ~35 seconds / on a certain long prompt, / versus / ~25 seconds / for GPT-4o / (a general model of similar size) / [65].**
🔸 **例如， / 微软 Azure 的一项测试 / 发现， / 它们的 o1 推理模型 / 在某个长提示词下的 / 端到端延迟 / 约为 35 秒， / 而 / GPT-4o / （一个规模类似的通用模型） / 则约为 25 秒 / [65]。**
> 1. **o1** *注*：OpenAI 开发的系列推理模型。
> 2. **GPT-4o** *注*：OpenAI 开发的通用全能型模型。
> 3. **Versus** [ˈvɜːrsəs] *prep.* 对比 (Against). 缩写为 **vs.**。

🔹 **Mini versions / (like GPT-4o-mini vs o3-mini) / show / the same trend: / the one / doing more reasoning / is slower / [65].**
🔸 **迷你版本 / （如 GPT-4o-mini 对比 o3-mini） / 显示了 / 同样的趋势： / 进行更多推理的模型 / 速度更慢 / [65]。**
> 1. **Trend** [trend] *n.* 趋势 (A general direction in which something is developing or changing).

🔹 **Throughput / (queries per second a system can handle) / therefore / is lower / for reasoning models / unless / you add more compute resources.**
🔸 **因此， / 对于推理模型来说， / 吞吐量 / （系统每秒可以处理的查询数） / 会更低， / 除非 / 你增加更多的计算资源。**
> 1. **Handle** [ˈhændl] *v.* 处理 (To manage, deal with, or be responsible for).

🔹 **From a deployment perspective, / this means / if you switch / an application / from using / a fast general model / to / a deep reasoning model, / you may need / to scale up / infrastructure / or / accept slower responses / for users.**
🔸 **从部署的角度来看， / 这意味着 / 如果你将 / 一个应用 / 从使用 / 快速通用模型 / 切换到 / 深度推理模型， / 你可能需要 / 扩大 / 基础设施规模， / 否则就必须 / 接受 / 用户响应速度变慢。**
> 1. **Perspective** [pərˈspektɪv] *n.* 视角，观点 (A particular attitude toward or way of regarding something).
> 【常用短语】**From a ... perspective**。
> 2. **Infrastructure** [ˈɪnfrəstrʌktʃər] *n.* 基础设施 (The basic physical and organizational structures and facilities).
> 3. **Scale up** [skeɪl ʌp] *phrasal v.* 扩大规模 (To increase the size, amount, or importance of something).

🔹 **We’ll quantify this / further / in Section 10 / with cost models.**
🔸 **我们将在第 10 节 / 通过成本模型 / 进一步 / 量化这一点。**
> 1. **Quantify** [ˈkwɑːntɪfaɪ] *v.* 量化 (To express or measure the quantity of).
> 2. **Section** [ˈsekʃn] *n.* 章节 (A distinct group within a larger body of something).

🔹 **Cost / (API or Compute):**
🔸 **成本 / （API 或计算）：**

🔹 **Most API providers / charge / by tokens.**
🔸 **大多数 API 提供商 / 按 Token / 收费。**
> 1. **Charge** [tʃɑːrdʒ] *v.* 收费 (To demand an amount as a price from someone for a service rendered or goods supplied).
> 【用法】**Charge someone for something**。

🔹 **If / a reasoning model / spews out / a 500-token rationale / plus / a 50-token answer, / you’ll pay / for 550 tokens.**
🔸 **如果 / 一个推理模型 / 喷出（输出） / 一个 500 Token 的基本原理 / 加上 / 一个 50 Token 的答案， / 你将支付 / 550 个 Token 的费用。**
> 1. **Spew out** [spjuː aʊt] *phrasal v.* 喷涌出 (To expel large quantities of something rapidly and forcibly).
> 【生动表达】通常指火山口喷发，此处生动描述模型大量输出文字。
> 2. **Rationale** [ˌræʃəˈnæl] *n.* 理由，基本原理 (A set of reasons or a logical basis for a course of action or a particular belief).
> 【词根】Rational (*adj.* 理性的)。

🔹 **Using / a non-reasoning model / that / just outputs / a 50-token answer / would cost / one-tenth that.**
🔸 **使用 / 一个仅输出 / 50 Token 答案的 / 非推理模型， / 其成本 / 仅为前者的十分之一。**
> 1. **One-tenth** [wʌn tenθ] *n.* 十分之一。分数表达：分子用基数词，分母用序数词。

🔹 **Therefore, / unless / pricing schemes / change, / using reasoning models / can be / significantly more expensive / per query.**
🔸 **因此， / 除非 / 定价方案 / 发生变化， / 否则使用推理模型 / 在每次查询中 / 可能会 / 显著昂贵。**
> 1. **Scheme** [skiːm] *n.* 方案，计划 (A large-scale systematic plan or arrangement).
> 2. **Significantly** [sɪɡˈnɪfɪkəntli] *adv.* 显著地 (In a sufficiently great or important way as to be worthy of attention).

🔹 **OpenAI’s pricing / for their high-end models, / for example, / might be / \$0.03 per 1K input tokens / and / \$0.06 per 1K output tokens / for GPT-4.**
🔸 **例如， / OpenAI / 对其高端模型的定价 / 可能是 / GPT-4 每 1000 个输入 Token 0.03 美元， / 以及 / 每 1000 个输出 Token 0.06 美元。**
> 1. **High-end** [ˌhaɪ ˈend] *adj.* 高端的 (Denoting the most expensive of a range of products).

🔹 **If / your query / is short / but / the model’s answer / including rationale / is 1K tokens, / that’s about / \$0.06 / just for the answer / — maybe / trivial / for one query, / but / multiply it / by millions of queries / and / it adds up.**
🔸 **如果 / 你的查询 / 很短， / 但 / 模型的回答 / （包括基本原理） / 是 1000 个 Token， / 那仅答案部分 / 就大约需要 / 0.06 美元 / ——对于一次查询来说 / 也许 / 微不足道， / 但 / 如果乘以数百万次查询， / 它的总额就会变得非常可观。**
> 1. **Trivial** [ˈtrɪviəl] *adj.* 微不足道的，琐碎的 (Of little value or importance).
> 2. **Add up** [æd ʌp] *phrasal v.* 积少成多，合乎逻辑 (To increase gradually until there is a large amount).
> 3. **Multiply** [ˈmʌltɪplaɪ] *v.* 乘，成倍增加 (To increase or cause to increase greatly in number or amount).

🔹 **Some platforms / might / eventually / price / differently / (perhaps / not charging / for the hidden chain-of-thought tokens / if / they’re not returned / to the user, etc.), / but / currently, / more tokens = more cost.**
🔸 **一些平台 / 最终 / 可能会 / 采取不同的 / 定价策略 / （或许 / 如果 / 隐藏的思维链 Token / 没有返回 / 给用户， / 就不予计费等）， / 但 / 目前来看， / Token 越多 = 成本越高。**
> 1. **Eventually** [ɪˈventʃuəli] *adv.* 最终地 (In the end, especially after a long delay, dispute, or series of problems).
> 2. **Hidden** [ˈhɪdn] *adj.* 隐藏的 (Kept out of sight; concealed).

🔹 **Additionally, / on self-hosted models, / more tokens / means / more GPU time, / which / equals / higher operational cost / and / energy usage.**
🔸 **此外， / 在私有化部署的模型上， / 更多的 Token / 意味着 / 更多的 GPU 时间， / 这 / 等于 / 更高的运营成本 / 和 / 能源消耗。**
> 1. **Self-hosted** [self ˈhoʊstɪd] *adj.* 自托管的，私有化部署的。
> 2. **Operational** [ˌɑːpəˈreɪʃənl] *adj.* 运营的，操作的 (Relating to the routine functioning and activities of a business or organization).

🔹 **We’ll see / later / how / some services / (like IBM’s toggleable reasoning mode [9] / or / OpenAI’s adjustable “reasoning_effort” / in GPT-5 [19, 66]) / attempt / to give users / control / over this cost / by scaling / the reasoning depth.**
🔸 **我们稍后会看到 / 一些服务 / （如 IBM 的可切换推理模式 [9] / 或 / OpenAI 在 GPT-5 中可调节的“推理强度” [19, 66]） / 是如何 / 尝试 / 通过缩放 / 推理深度 / 来让用户 / 控制 / 这部分成本的。**
> 1. **Toggleable** [ˈtɒɡləbl] *adj.* 可切换的 (Able to be switched between two different states).
> 2. **Depth** [depθ] *n.* 深度 (The distance from the top or surface to the bottom of something).

🔹 **Controllability / and / Prompts:**
🔸 **可控性 / 与 / 提示词：**

🔹 **Non-reasoning models / are typically controlled / via prompts / that / directly instruct / the task / or style, / but / you don’t usually have / a direct knob / for “think more.”**
🔸 **非推理模型 / 通常 / 通过 / 直接指示 / 任务 / 或风格的 / 提示词进行控制， / 但 / 你通常没有 / 一个直接的“多思考” / 旋钮。**
> 1. **Knob** [nɑːb] *n.* 旋钮，球形把手 (A round button on a machine that you turn to operate it).
> 【比喻】此处指调节参数的开关。
> 2. **Instruct** [ɪnˈstrʌkt] *v.* 指示，教授 (To direct or command someone to do something).

🔹 **You can try / adding / “Please explain your answer,” / but / the model / might still / give / a superficial explanation.**
🔸 **你可以尝试 / 添加 / “请解释你的答案”， / 但 / 模型 / 可能仍然 / 给出 / 肤浅的解释。**
> 1. **Superficial** [ˌsuːpərˈfɪʃl] *adj.* 肤浅的，表面的 (Not thorough, deep, or complete).
> 【词根】Super- (上面) + fic (面)。

🔹 **With / reasoning models, / you often have / explicit controls / or / at least / predictable prompt patterns / to induce / certain behaviors.**
🔸 **对于 / 推理模型， / 你通常拥有 / 明确的控制手段 / 或者 / 至少是 / 可预测的提示词模式 / 来诱导 / 特定行为。**
> 1. **Predictable** [prɪˈdɪktəbl] *adj.* 可预测的 (Able to be predicted).
> 2. **Induce** [ɪnˈduːs] *v.* 诱导，引起 (To succeed in persuading or influencing someone to do something).

🔹 **For example, / Azure’s reasoning models / have / a parameter / reasoning_effort / with values / like / “low/ medium/high" / — effectively / a knob / to say / how much thinking / the model / should do / [67].**
🔸 **例如， / 微软 Azure 的推理模型 / 拥有 / 一个参数 / reasoning_effort（推理强度）， / 其取值 / 诸如 / “低/中/高” / ——这实际上是 / 一个旋钮， / 用来告知 / 模型 / 应该进行 / 多少思考 / [67]。**
> 1. **Parameter** [pəˈræmɪtər] *n.* 参数 (A numerical or other measurable factor forming one of a set that defines a system).
> 2. **Effectively** [ɪˈfektɪvli] *adv.* 实际上，有效地 (Actually but not officially or explicitly).

🔹 **That's not / something / that / exists / for standard models.**
🔸 **这在 / 标准模型中 / 是不 / 存在的。**
> 1. **Exist** [ɪɡˈzɪst] *v.* 存在 (To have objective reality or being).

🔹 **Similarly, / these models / might respond / to system prompts / like / "Think step by step / and / show your reasoning” / much more / thoroughly.**
🔸 **同样地， / 这些模型 / 可能会 / 更加彻底地 / 响应 / 诸如 / “逐步思考 / 并 / 展示你的推理过程” / 等系统提示词。**
> 1. **Thoroughly** [ˈθɜːroʊli] *adv.* 彻底地，周详地 (In a thorough manner).

🔹 **In fact, / a reasoning model / might ignore / a direct user question / initially / and / start by / outputting / a plan / or / breakdown / (since / it was trained / to do so), / whereas / a normal model / would consider / that / digressive.**
🔸 **事实上， / 推理模型 / 最初 / 可能会忽略 / 用户的直接提问， / 而是以 / 输出 / 计划 / 或 / 拆解 / 开始（因为 / 它受到的训练 / 就是如此）， / 而 / 普通模型 / 则会认为 / 那样做是 / 离题的。**
> 1. **Initially** [ɪˈnɪʃəli] *adv.* 最初，开头 (At the beginning).
> 2. **Breakdown** [ˈbreɪkdaʊn] *n.* 细目，故障 (An explanatory analysis or list of items).
> 【熟词僻义】原意为“机器故障”或“精神崩溃”，此处引申为“任务拆解”。
> 3. **Digressive** [daɪˈɡresɪv] *adj.* 离题的，枝节的 (Characterized by digression; tending to depart from the main subject).
> 【词性变化】**Digress** (*v.* 离题)；**Digression** (*n.*)。

🔹 **This difference / can surprise / users / at first / ("Why is the model giving me / this long-winded response?"), / but / it's by design.**
🔸 **这种差异 / 起初 / 可能会让用户 / 感到惊讶 / （“为什么模型给我 / 这个长篇大论的回复？”）， / 但 / 这是有意为之。**
> 1. **Long-winded** [ˌlɔːŋ ˈwɪndɪd] *adj.* 啰嗦的，冗长的 (Tediously long in speaking or writing).
> 2. **By design** [baɪ dɪˈzaɪn] *idiom* 有意地，故意地 (Intentionally).

🔹 **Accuracy / and / Reliability:**
🔸 **准确性 / 与 / 可靠性：**

🔹 **On tasks / that / benefit / from multi-step reasoning / (say complex math, / multi-hop QA, / code synthesis), / reasoning models / are / strictly superior / — often / by large margins / — if / used correctly.**
🔸 **在那些 / 受益于 / 多步推理的 / 任务中 / （比如复杂的数学、 / 多跳问答、 / 代码合成）， / 推理模型 / 是 / 绝对领先的 / ——通常 / 领先幅度很大 / ——如果 / 使用得当的话。**
> 1. **Superior** [suːˈpɪriər] *adj.* 优越的，上级的 (Higher in station, rank, degree, importance, or quality).
> 【考点】**Be superior to** 比……优越。
> 2. **Margin** [ˈmɑːrdʒɪn] *n.* 幅度，利润，边缘 (The amount by which one thing is different from another).
> 【常见短语】**By a wide/large margin** 以巨大优势。
> 3. **Multi-hop QA** [ˈmʌlti hɑːp ˌkjuː ˈeɪ] *注*：多跳问答，指需要结合多个分散事实才能得出答案的问答任务。
> 4. **Synthesis** [ˈsɪnθəsɪs] *n.* 合成，综合 (The combination of ideas to form a theory or system).

🔹 **For instance, / GPT-4.1 (general model) / might score / say 50% / on a math word problem set, / whereas / GPT-5 (reasoning model) / might score 80–90% / [30, 68].**
🔸 **例如， / GPT-4.1（通用模型） / 在数学应用题集上的 / 得分可能 / 假设是 50%， / 而 / GPT-5（推理模型） / 的得分可能达到 80-90% / [30, 68]。**
> 1. **Word problem** [wɜːrd ˈprɑːbləm] *n.* 应用题（用文字叙述的数学题）。

🔹 **We see this / in benchmarks: / reasoning-heavy benchmarks / (GSM8K, MATH, etc.) / have / their top scores / dominated / by models / known to employ / chain-of-thought.**
🔸 **我们在 / 基准测试中 / 也能看到这一点： / 重推理的基准测试 / （如 GSM8K、MATH 等） / 的最高分 / 被那些 / 已知采用 / 思维链的 / 模型所 / 占据。**
> 1. **Benchmark** [ˈbentʃmɑːrk] *n.* 基准测试，参照点 (A standard or point of reference against which things may be compared or assessed).
> 2. **Dominate** [ˈdɑːmɪneɪt] *v.* 统治，占据主导地位 (To have a commanding influence on; exercise control over).

🔹 **On the flip side, / for tasks / that / don’t require / complex reasoning / — like / straightforward classification, / summarization / of a short text, / or / casual dialogue / — a reasoning model / may be / on par / or / sometimes / even slightly worse / than a simpler model.**
🔸 **另一方面， / 对于那些 / 不需要 / 复杂推理的 / 任务 / ——比如 / 直接的分类、 / 短文本的 / 摘要 / 或 / 闲聊 / ——推理模型 / 的表现可能 / 与简单模型 / 持平， / 甚至 / 有时 / 略逊一筹。**
> 1. **On the flip side** [ɒn ðə flɪp saɪd] *idiom* 另一方面 (Looking at the different, usually negative, aspect of something).
> 2. **Straightforward** [ˌstreɪtˈfɔːrwərd] *adj.* 直接的，坦率的 (Uncomplicated and easy to understand).
> 3. **On par** [ɒn pɑːr] *idiom* 不相上下，并驾齐驱 (At the same level or standard as someone or something else).

🔹 **Why / worse?**
🔸 **为什么 / 会更差呢？**

🔹 **Because / the reasoning fine-tuning / may / bias / the model / to “overthink” / even / when / not needed, / potentially / introducing / unnecessary detail / or / small errors / in simple tasks.**
🔸 **因为 / 推理微调 / 可能会 / 使 / 模型 / 倾向于 / “过度思考”， / 甚至 / 在 / 不需要的时候 / 也是如此， / 从而可能 / 在简单任务中 / 引入 / 不必要的细节 / 或 / 小错误。**
> 1. **Bias** [ˈbaɪəs] *v./n.* 使有偏见，偏向 (Cause to feel or show inclination or prejudice for or against someone or something).
> 2. **Overthink** [ˌoʊvərˈθɪŋk] *v.* 过度思考 (To think about something too much or for too long).

🔹 **IBM / observed / that / on / certain instruction-following benchmarks / (like answering tricky instructions), / distilled reasoning versions / of Llama and Qwen / actually / showed regressions / compared to / the original models / [69, 70].**
🔸 **IBM / 观察到， / 在 / 特定的指令遵循基准测试中 / （如回答棘手的指令）， / Llama 和 Qwen 的 / 蒸馏推理版本 / 实际上 / 表现出了 / 性能倒退， / 与 / 原始模型 / 相比而言 / [69, 70]。**
> 1. **Tricky** [ˈtrɪki] *adj.* 棘手的，狡猾的 (Requiring care and skill because difficult or awkward).
> 2. **Regression** [rɪˈɡreʃn] *n.* 退化，回归 (A return to a former or less developed state).
> 【技术语境】指软件或模型在升级后某些旧功能反而变差了。
> 3. **Llama / Qwen** *注*：由 Meta（前 Facebook）和阿里巴巴分别开发的知名开源大语言模型。

🔹 **The reasoning-tuned models / perhaps / focused / so much / on logical structure / that / they lost / a bit of / the free-form flexibility.**
🔸 **经过推理调优的模型 / 或许 / 过于 / 专注于 / 逻辑结构， / 以至于 / 它们失去了 / 一部分 / 自由形式的灵活性。**
> 1. **Flexibility** [ˌfleksəˈbɪləti] *n.* 灵活性 (The quality of bending easily or being easily modified).

🔹 **Meanwhile, / a more general model / might / give / a direct answer / that’s / perfectly fine.**
🔸 **与此同时， / 更通用的模型 / 可能会 / 给出 / 一个 / 非常不错的 / 直接回答。**
> 1. **Meanwhile** [ˈmiːnwaɪl] *adv.* 与此同时 (In the intervening period of time).

🔹 **So, / the reliability advantage / of reasoning models / is / task-dependent.**
🔸 **因此， / 推理模型 / 的可靠性优势 / 是 / 取决于任务的。**
> 1. **Task-dependent** [tæsk dɪˈpendənt] *adj.* 任务相关的，取决于任务的。

🔹 **They / shine / on problems / with verifiable solutions / (math, logic puzzles, code compiling) / [71].**
🔸 **它们 / 在那些 / 拥有可验证答案的 / 问题上 / （如数学、逻辑谜题、代码编译） / 表现优异 / [71]。**
> 1. **Shine** [ʃaɪn] *v.* 表现突出，发光 (To be very good at something).
> 2. **Verifiable** [ˈverɪfaɪəbl] *adj.* 可验证的 (Able to be checked or demonstrated to be true, accurate, or justified).

🔹 **In / open-ended creativity / or / subjective tasks, / reasoning traces / might / not help / or / might / even constrain / creativity.**
🔸 **在 / 开放式创意 / 或 / 主观任务中， / 推理痕迹 / 也许 / 没有帮助， / 甚至 / 可能会 / 限制 / 创造力。**
> 1. **Open-ended** [ˌoʊpən ˈendɪd] *adj.* 开放式的 (Having no determined limit or boundary).
> 2. **Subjective** [səbˈdʒektɪv] *adj.* 主观的 (Based on or influenced by personal feelings, tastes, or opinions).
> 3. **Trace** [treɪs] *n.* 痕迹，踪迹 (A mark, object, or other indication of the existence or passing of something).
> 4. **Constrain** [kənˈstreɪn] *v.* 限制，束缚 (To severely restrict the scope, extent, or activity of).

🔹 **This nuance / is / important: / it / suggests / a hybrid approach / might be best / — using / reasoning mode / when / appropriate / and / defaulting / to general mode / otherwise.**
🔸 **这种微妙的差别 / 非常 / 重要： / 它 / 表明 / 混合方法 / 可能是最佳的 / ——在 / 合适的 / 时候 / 使用 / 推理模式， / 否则 / 默认 / 使用通用模式。**
> 1. **Nuance** [ˈnuːɑːns] *n.* 细微差别 (A subtle difference in or shade of meaning, expression, or sound).
> 【雅思/考研】高频词，描述复杂事物间的精细区别。
> 2. **Hybrid** [ˈhaɪbrɪd] *adj./n.* 混合的，混合动力 (A thing made by combining two different elements; a mixture).
> 3. **Default** [dɪˈfɔːlt] *v.* 默认 (To revert to a preselected option).
> 【熟词僻义】原意为“违约、欠债”，计算机语境指“默认值”。

🔹 **Hallucination / Differences:**
🔸 **幻觉的 / 差异：**

🔹 **Both model types / can / hallucinate / (produce false information).**
🔸 **两种类型的模型 / 都会 / 产生幻觉 / （生成错误信息）。**
> 1. **Hallucinate** [həˈluːsɪneɪt] *v.* 产生幻觉 (To experience a seemingly real perception of something not actually present).
> 【AI术语】指模型煞有其事地胡说八道。

🔹 **But / the nature / of / hallucinations / differs.**
🔸 **但是 / 幻觉的 / 本质 / 却有所不同。**
> 1. **Nature** [ˈneɪtʃər] *n.* 本质，自然 (The basic or inherent features of something).

🔹 **A non-reasoning model / might / just confidently state / a false fact / (“The capital of Mars is X”).**
🔸 **非推理模型 / 可能会 / 只是自信地陈述 / 一个错误事实 / （“火星的首都是 X”）。**
> 1. **Confidently** [ˈkɑːnfɪdəntli] *adv.* 自信地 (In a self-assured way).

🔹 **A reasoning model / might / produce / a convincing-looking argument / that / ends in / a false conclusion.**
🔸 **推理模型 / 可能会 / 产生 / 一个看起来很有说服力的论证， / 却以 / 错误的结论 / 告终。**
> 1. **Convincing** [kənˈvɪnsɪŋ] *adj.* 有说服力的 (Capable of causing someone to believe that something is true or real).
> 2. **Argument** [ˈɑːrɡjumənt] *n.* 论证，争吵 (A reason or set of reasons given with the aim of persuading others that an action or idea is right or wrong).

🔹 **For example, / it might / cite / a series of logical steps, / one of which / is / subtly incorrect / or / based on / a faulty premise, / leading to / a wrong answer / that / appears / well-justified / [32].**
🔸 **例如， / 它可能会 / 引用 / 一系列逻辑步骤， / 其中之一 / 是 / 微妙的错误 / 或 / 基于 / 错误的前提， / 从而导致 / 得到一个 / 看起来 / 理由充分的 / 错误答案 / [32]。**
> 1. **Cite** [saɪt] *v.* 引用 (To quote a passage, book, or author as evidence for or justification of an argument or statement).
> 2. **Subtly** [ˈsʌtli] *adv.* 微妙地 (In a manner that is so delicate or precise as to be difficult to analyze or describe).
> 3. **Faulty** [ˈfɔːlti] *adj.* 有错误的 (Working badly or unreliably because of imperfections).
> 4. **Premise** [ˈpremɪs] *n.* 前提 (A previous statement or proposition from which another is inferred or follows as a conclusion).
> 5. **Well-justified** [wel ˈdʒʌstɪfaɪd] *adj.* 理由充足的。

🔹 **In / one sense, / reasoning models / are / less likely / to hallucinate blatantly / on factual queries / because / they / tend to / cross-check information / internally.**
🔸 **在 / 某种意义上， / 推理模型 / 较不 / 容易在事实性查询中 / 产生露骨的幻觉， / 因为 / 它们 / 往往会 / 在内部 / 交叉检查信息。**
> 1. **In one sense** [ɪn wʌn sens] *idiom* 在某种意义上。
> 2. **Blatantly** [ˈbleɪtəntli] *adv.* 公然地，露骨地 (In a completely conspicuous and unsubtle way).
> 3. **Cross-check** [ˈkrɔːs tʃek] *v.* 交叉核对 (To verify figures or information by using an alternative source or method).

🔹 **They / might / recall / multiple facts, / weigh them, / and / thus / avoid / easy mistakes.**
🔸 **它们 / 可能会 / 回想起 / 多个事实， / 权衡它们， / 并 / 因此 / 避免 / 简单的错误。**
> 1. **Recall** [rɪˈkɔːl] *v.* 回想，召回 (To bring a fact, event, or situation back into one's mind).
> 2. **Weigh** [weɪ] *v.* 权衡，称重 (To assess the nature or importance of something by considering its different aspects).

🔹 **However, / when / they do go wrong, / they often / wrap the hallucination / in a rationale, / which / can make / it / harder / for users / to disentangle / truth from fiction.**
🔸 **然而， / 当 / 它们确实出错时， / 它们通常 / 会将幻觉 / 包裹在一种逻辑原理中， / 这 / 使得 / 用户 / 更难 / 从虚假中 / 辨别 / 真相。**
> 1. **Wrap** [ræp] *v.* 包裹 (To cover or enclose something in paper or soft material).
> 2. **Disentangle** [ˌdɪsɪnˈtæŋɡl] *v.* 解开，理清 (To separate something from that which it is entangled with).
> 【词根】Dis- (离开) + entangle (缠绕)。

🔹 **There’s / also / the phenomenon / of / “rationalizing hallucinations” / — the model / knows / the user expects / an explanation, / so / even if / it’s guessing an answer, / it will / invent / a chain-of-thought / to justify / that guess.**
🔸 **还存在 / 所谓 / “合理化幻觉” / 的现象 / ——模型 / 知道 / 用户期待 / 解释， / 所以 / 即使 / 它在瞎猜答案， / 它也会 / 编造 / 一段思维链 / 来为 / 那个猜测 / 辩护。**
> 1. **Phenomenon** [fəˈnɑːmɪnən] *n.* 现象 (A fact or situation that is observed to exist or happen).
> 【注意】复数形式为 **Phenomena**。
> 2. **Rationalize** [ˈræʃnəlaɪz] *v.* 使合理化 (To attempt to explain or justify behavior or an attitude with logical reasons, even if these are not appropriate).
> 3. **Invent** [ɪnˈvent] *v.* 发明，编造 (To create or design something that has not existed before; to make up a false story or device).
> 4. **Justify** [ˈdʒʌstɪfaɪ] *v.* 证明……有理 (To show or prove to be right or reasonable).

🔹 **Non-reasoning models, / by not providing / a rationale, / at least / don’t / compound / the misinformation / with / a fake explanation.**
🔸 **非推理模型 / 由于不提供 / 逻辑原理， / 至少 / 不会 / 用 / 虚假的解释 / 来加剧 / 错误信息。**
> 1. **Compound** [kəmˈpaʊnd] *v.* 加剧，混合 (To make a bad situation worse by adding something else).
> 【熟词僻义】名词为“化合物、大院”，动词在考研中常考“加重、使恶化”。
> 2. **Misinformation** [ˌmɪsˌɪnfərˈmeɪʃn] *n.* 错误信息 (False or inaccurate information, especially that which is intended to deceive).
> 3. **Fake** [feɪk] *adj.* 虚假的 (Not genuine; counterfeit).

🔹 **This / has implications / for trust: / some / argue / that / reasoning models / appear / more trustworthy / (because / they explain), / but / can actually / mislead / more / if / their explanations / are / wrong / and / the user / is / lulled into / accepting / them.**
🔸 **这对 / 信任 / 具有启示意义： / 有些人 / 认为 / 推理模型 / 看起来 / 更值得信赖 / （因为 / 它们会解释）， / 但 / 实际上 / 可能会 / 产生更多的 / 误导 / ——如果 / 它们的解释 / 是 / 错误的， / 且 / 用户 / 被诱导 / 接受了 / 它们。**
> 1. **Implication** [ˌɪmplɪˈkeɪʃn] *n.* 启示，可能的影响 (The conclusion that can be drawn from something although it is not explicitly stated).
> 2. **Trustworthy** [ˈtrʌstwɜːrði] *adj.* 值得信赖的 (Able to be relied on as honest or truthful).
> 3. **Lull into** [lʌl ˈɪntuː] *phrasal v.* 使放松警惕而进入 (To cause someone to feel deceptive sense of safety or confidence).
> 【例句】Lulled into a false sense of security. 被虚假的安全感所蒙蔽。

🔹 **We’ll / revisit / this / in Section 11 / on / why / they don’t / always / say / what / they think / (and / the complexity / of / aligning / the truth / of / the rationale / with / the truth / of / the answer).**
🔸 **我们将在 / 第 11 节 / 重新讨论 / 这一点 / ——关于 / 为什么 / 它们并不 / 总是 / 表达 / 它们的 / 真实想法 / （以及 / 使 / 推理逻辑的 / 真实性 / 与 / 答案的 / 真实性 / 保持一致 / 的复杂性）。**
> 1. **Revisit** [ˌriːˈvɪzɪt] *v.* 重新讨论，再次访问 (To consider a situation or problem again or in a different way).
> 2. **Align** [əˈlaɪn] *v.* 使一致，结盟 (To place or arrange in a straight line; to give support to a person, organization, or cause).
> 【AI术语】Alignment (对齐) 指让AI的目标与人类价值观一致。

🔹 **Transparency / and / Debugging:**
🔸 **透明度 / 与 / 调试：**

🔹 **Because / reasoning models / (especially / those / that / output / their reasoning) / provide / intermediate steps, / they / offer / a form / of / transparency / that / can be / very useful.**
🔸 **因为 / 推理模型 / （尤其是 / 那些 / 输出 / 自身推理过程的 / 模型） / 提供了 / 中间步骤， / 它们 / 提供了一种 / 形式 / 的 / 透明度， / 这 / 可能会 / 非常有用。**
> 1. **Transparency** [trænsˈpærənsi] *n.* 透明度 (The quality of being done in an open way without secrets).
> 【词性变化】**Transparent** (*adj.* 透明的)。

🔹 **If / a reasoning model / arrives at / a wrong answer, / a developer / or / user / can often / pinpoint / where / in the chain / things / went wrong.**
🔸 **如果 / 一个推理模型 / 得出了 / 错误答案， / 开发人员 / 或 / 用户 / 通常可以 / 精确指出 / 链条中的 / 哪个环扣 / 出了问题。**
> 1. **Arrive at** [əˈraɪv æt] *phrasal v.* 得出（结论），到达 (To reach a decision or conclusion after a lot of consideration).
> 2. **Pinpoint** [ˈpɪnpɔɪnt] *v.* 精确指出 (To find or identify with great accuracy).

🔹 **For example, / “Oh, / in step 3 / of its reasoning / it assumed / X, / which / is false / — that’s / why / the conclusion / is / wrong.”**
🔸 **例如， / “噢， / 在它推理的 / 第 3 步中， / 它假设了 / X， / 而那是错误的 / ——这 / 就是 / 为什么 / 结论 / 是 / 错误的原因。”**
> 1. **Assume** [əˈsuːm] *v.* 假设 (To suppose to be the case, without proof).

🔹 **This / is / much harder / to do / with / a one-shot answer / from / a standard model.**
🔸 **对于 / 来自 / 标准模型的 / 一次性答案 / 来说， / 这样做 / 要难得多。**
> 1. **One-shot** [ˌwʌn ˈʃɑːt] *adj.* 一次性的 (Achieved or occurring only once).

🔹 **In / that sense, / reasoning models / are / easier / to debug / or / to augment / — a user / could / correct / the model / at / an intermediate step / (“Actually, / that premise / is incorrect, / consider Y / instead”) / and / have it / continue, / something / that / is / nearly impossible / if / the model / didn’t / expose / its thought process.**
🔸 **在 / 那个意义上， / 推理模型 / 更容易 / 调试 / 或 / 增强 / ——用户 / 可以 / 在 / 中间步骤 / 纠正 / 模型 / （“实际上， / 那个前提 / 是错误的， / 请考虑 Y / 替代”）， / 并 / 让它 / 继续执行， / 这 / 在 / 模型 / 没有 / 暴露 / 其思维过程 / 的情况下 / 几乎是不可能的。**
> 1. **Debug** [ˌdiːˈbʌɡ] *v.* 调试，排除故障 (To identify and remove errors from computer hardware or software).
> 2. **Augment** [ɔːɡˈment] *v.* 增强，扩大 (To make something greater by adding to it).
> 3. **Expose** [ɪkˈspoʊz] *v.* 暴露，揭露 (To make something visible by uncovering it).

🔹 **On / the other hand, / as mentioned, / the chain-of-thought / could / be / too convoluted / or / misleading / if / not faithful.**
🔸 **另一方面， / 正如所提到的， / 如果 / 思维链 / 不够忠实， / 它可能 / 会 / 过于复杂 / 或 / 具有误导性。**
> 1. **Convoluted** [ˈkɑːnvəluːtɪd] *adj.* 复杂的，费解的 (Extremely complex and difficult to follow).
> 2. **Faithful** [ˈfeɪθfl] *adj.* 忠实的 (Remaining loyal and steadfast).
> 【AI术语】Faithfulness 指思维链是否真实反映了模型的内部逻辑。

🔹 **But / generally, / the AI safety community / sees / chain-of-thought / as / a step / toward / explainable AI, / since / it’s / an artifact / of the model’s decision-making / that / we can / inspect / [72, 73].**
🔸 **但 / 总的来说， / AI 安全社区 / 将 / 思维链 / 视为 / 迈向 / 可解释 AI / 的一步， / 因为 / 它是 / 模型决策过程中的 / 一个产物， / 我们可以对其进行 / 检查 / [72, 73]。**
> 1. **Artifact** [ˈɑːrtɪfækt] *n.* 产物，人工制品 (An object made by a human being; a functional structure in a computer system).
> 2. **Inspect** [ɪnˈspekt] *v.* 检查，视察 (To look at someone or something closely, typically to assess their condition or to discover any shortcomings).
> 3. **Explainable AI (XAI)** *注*：可解释的人工智能，旨在让机器学习模型的决策过程对人类透明、可理解。

🔹 **Many of / the governance frameworks / (e.g., / the U.S. NIST / AI Risk Management Framework / or / the EU AI Act’s / transparency obligations) / encourage / being able / to explain / automated decisions.**
🔸 **许多 / 治理框架 / （例如 / 美国 NIST 的 / AI 风险管理框架 / 或 / 欧盟 AI 法案的 / 透明度义务） / 都鼓励 / 能够 / 解释 / 自动决策。**
> 1. **Governance** [ˈɡʌvərnəns] *n.* 治理 (The action or manner of governing).
> 2. **U.S. NIST** *注*：美国国家标准与技术研究院 (National Institute of Standards and Technology)，隶属于美国商务部。
> 3. **EU AI Act** *注*：欧盟人工智能法案，世界上第一部全面的 AI 监管法规。
> 4. **Obligation** [ˌɑːblɪˈɡeɪʃn] *n.* 义务 (An act or course of action to which a person is morally or legally bound).

🔹 **Having / models / that / naturally generate / explanations / (even / if / they’re / to be taken / with a grain of salt) / is / a move / in that direction.**
🔸 **拥有 / 能够 / 自然生成 / 解释的 / 模型 / （即使 / 它们 / 需要 / 存疑地对待） / 是 / 朝着该方向 / 迈出的一步。**
> 1. **Take with a grain of salt** [teɪk wɪð ə ɡreɪn əv sɔːlt] *idiom* 对……持保留态度，不完全相信。
> 【考研/雅思】非常地道的习语。

🔹 **Tool Use / and / API Calls:**
🔸 **工具使用 / 与 / API 调用：**

🔹 **Non-reasoning models / typically / treat / knowledge retrieval / or / calculation / as implicit / — they rely on / their internal knowledge / and / language ability / for everything.**
🔸 **非推理模型 / 通常 / 将 / 知识检索 / 或 / 计算 / 视为隐性的 / ——它们在所有事情上 / 都依赖于 / 自身的内部知识 / 和 / 语言能力。**
> 1. **Retrieval** [rɪˈtriːvl] *n.* 检索 (The process of getting something back from somewhere).
> 【词性变化】**Retrieve** (*v.*)。
> 2. **Implicit** [ɪmˈplɪsɪt] *adj.* 隐性的 (Implied though not plainly expressed).

🔹 **Reasoning models / are / often designed / to work with / external tools.**
🔸 **推理模型 / 通常被设计为 / 与 / 外部工具 / 协作。**
> 1. **External** [ɪkˈstɜːrnl] *adj.* 外部的 (Belonging to or forming the outer surface or structure of something).

🔹 **They / might / output / a special token / or / format / to indicate / an action, / such as / calling / a search engine / or / running / a code interpreter / (this / is / part of / the ReAct paradigm).**
🔸 **它们 / 可能会 / 输出 / 一个特殊的 Token / 或 / 格式 / 来指示 / 某项操作， / 例如 / 调用 / 搜索引擎 / 或 / 运行 / 代码解释器 / （这 / 是 / ReAct 范式 / 的一部分）。**
> 1. **Indicate** [ˈɪndɪkeɪt] *v.* 指示，表明 (To point out; show).
> 2. **Interpreter** [ɪnˈtɜːrprɪtər] *n.* 解释器，口译员 (A program that can execute a set of instructions; a person who interprets).
> 3. **ReAct paradigm** *注*：Reasoning + Acting。一种让模型在推理的同时采取行动的提示技术。

🔹 **We / will / talk more / about / tool integration / in Section 8, / but / the key point / here / is / that / reasoning models / are / more amenable / to being integrated / into agents / — systems / that / can act / in the world / — because / their step-by-step output / can be / parsed / and / executed / by a controlling program.**
🔸 **我们 / 将在 / 第 8 节 / 详细讨论 / 工具集成， / 但 / 这里的 / 关键点 / 是， / 推理模型 / 更容易 / 被集成 / 到智能体（Agents）中 / ——即可以在现实世界中 / 采取行动的 / 系统 / ——因为 / 它们的逐步输出 / 可以被 / 控制程序 / 解析 / 并 / 执行。**
> 1. **Amenable** [əˈmiːnəbl] *adj.* 顺从的，可用某种方式处理的 (Open and responsive to suggestion; easily persuaded or controlled).
> 【用法】**Be amenable to something**。
> 2. **Parse** [pɑːrs] *v.* 解析 (To analyze a string or text into logical syntactic components).
> 3. **Execute** [ˈeksɪkjuːt] *v.* 执行 (To carry out or put into effect a plan, order, or course of action).

🔹 **A general model / can / certainly / be used / in an agent loop / too / (as / was done / with early agents / like AutoGPT / using GPT-4), / but / reasoning models / were / practically / built / for that kind of loop, / making them / a more natural fit / when / you need / the model / to orchestrate / complex actions / (like / “search for X, / then / summarize, / then / do Y”).**
🔸 **通用模型 / 当然 / 也可以 / 用于智能体循环 / （正如 / 早期的 / 智能体 / 如 AutoGPT / 使用 GPT-4 所做的那样）， / 但 / 推理模型 / 实际上 / 就是 / 为那种循环而设计的， / 这使得它们 / 成为更自然的选择 / ——当你 / 需要 / 模型 / 来编排 / 复杂动作 / （如“搜索 X， / 然后 / 总结， / 然后 / 执行 Y”）时。**
> 1. **Practically** [ˈpræktɪkli] *adv.* 实际上，几乎 (In a practical manner; almost).
> 2. **Orchestrate** [ˈɔːrkɪstreɪt] *v.* 编排，精心安排 (To plan or coordinate any situation or event).
> 【熟词僻义】原意为“管弦乐编曲”，现多用于描述复杂任务的协调与组织。
> 3. **AutoGPT** *注*：一个基于 GPT-4 的开源项目，旨在实现完全自主的 AI 任务执行。

🔹 **Privacy / Considerations:**
🔸 **隐私 / 考量：**

🔹 **Both types / share / similar privacy issues / (since / any LLM / could / output / training data / or / user data), / but / reasoning models / pose / an interesting twist: / their intermediate steps / might / inadvertently / reveal / sensitive information.**
🔸 **两种类型 / 都面临 / 类似的隐私问题 / （因为 / 任何 LLM / 都可能 / 输出 / 训练数据 / 或 / 用户数据）， / 但 / 推理模型 / 带来了一个 / 有趣的转折： / 它们的中间步骤 / 可能会 / 无意中 / 泄露 / 敏感信息。**
> 1. **Pose** [poʊz] *v.* 造成，提出 (To present or constitute a problem, danger, or difficulty).
> 【常用短语】**Pose a threat/risk/challenge**。
> 2. **Twist** [twɪst] *n.* 转折，扭曲 (An unexpected development of events).
> 3. **Inadvertently** [ˌɪnədˈvɜːrtəntli] *adv.* 不经意地，无意中 (Without intention; accidentally).
> 【反义词】Intentionally, Deliberately.
> 4. **Reveal** [rɪˈviːl] *v.* 泄露，揭示 (To make previously unknown or secret information known to others).

🔹 **For example, / suppose / a reasoning model / is / being used / to analyze / a confidential document / and / answer questions.**
🔸 **例如， / 假设 / 推理模型 / 正在 / 被用于 / 分析 / 一份机密文件 / 并 / 回答问题。**
> 1. **Confidential** [ˌkɑːnfɪˈdenʃl] *adj.* 机密的 (Intended to be kept secret).

🔹 **If / it’s / thinking through / the solution, / it might / regurgitate / whole sentences / from the confidential text / as part of / its reasoning trace, / even if / the final answer / only needed / a summary.**
🔸 **如果 / 它在 / 深入思考 / 解决方案， / 它可能会 / 机械地重复 / 机密文本中的 / 整句内容， / 作为 / 其推理痕迹的一部分， / 即使 / 最终答案 / 只需要 / 一个摘要。**
> 1. **Regurgitate** [rɪˈɡɜːrdʒɪteɪt] *v.* 涌回，机械地重复 (To repeat information without analyzing or comprehending it).
> 【生动表达】原指“反刍、呕吐”，在学术语境下指学生或AI不假思索地背诵、重复原文。

🔹 **If / the chain-of-thought / is / shown / to the user / or / stored / in logs, / that’s / a direct privacy leak / of the source material.**
🔸 **如果 / 思维链 / 被 / 展示 / 给用户 / 或 / 存储 / 在日志中， / 那就是 / 对源材料的 / 直接隐私泄露。**
> 1. **Leak** [liːk] *n./v.* 泄露 (An intentional disclosure of something secret or private).

🔹 **A general model / that / outputs / only / the final summary / might be / less likely / to output / large sensitive / verbatim chunks / (unless / prompted).**
🔸 **一个 / 仅输出 / 最终摘要的 / 通用模型 / 产生 / 大量敏感 / 逐字块 / 的可能性 / 可能会更小 / （除非 / 受到提示）。**
> 1. **Verbatim** [vɜːrˈbeɪtɪm] *adj./adv.* 逐字的，一字不差的 (In exactly the same words as were used originally).
> 2. **Chunk** [tʃʌŋk] *n.* 大块，部分 (A thick, solid piece of something).

🔹 **So, / deploying / reasoning models / in domains / with sensitive data / might / require / caution: / either / hide / the chain-of-thought / or / implement / redaction / of certain content / in the reasoning output.**
🔸 **因此， / 在 / 包含敏感数据的 / 领域 / 部署 / 推理模型 / 可能 / 需要 / 谨慎： / 要么 / 隐藏 / 思维链， / 要么 / 在推理输出中 / 执行 / 某些内容的 / 脫敏。**
> 1. **Caution** [ˈkɔːʃn] *n.* 谨慎 (Care taken to avoid danger or mistakes).
> 2. **Redaction** [rɪˈdækʃn] *n.* 编辑，（敏感信息的）删减或脫敏 (The process of censoring or obscuring part of a text for legal or security purposes).
> 【雅思/法律英语】核心词汇。

🔹 **One / can / hide it / by / instructing / the model / not to reveal / certain details / or / by / only using / the hidden CoT / (like / OpenAI’s approach / of summarizing / it).**
🔸 **人们 / 可以 / 通过 / 指示 / 模型 / 不要泄露 / 某些细节， / 或 / 通过 / 仅使用 / 隐藏的 CoT / （如 / OpenAI 采用的 / 对其进行摘要的 / 方法）来隐藏它。**
> 1. **Approach** [əˈproʊtʃ] *n.* 方法，途径 (A way of dealing with something).

🔹 **This / is / a bit of / a double-edged sword: / we want / transparency, / but / we / also / have to / manage / the additional data / the model / produces.**
🔸 **这 / 有点像 / 一把双刃剑： / 我们想要 / 透明度， / 但 / 我们 / 同时也 / 必须 / 管理 / 模型 / 产生的 / 额外数据。**
> 1. **Double-edged sword** [ˌdʌbl edʒd ˈsɔːrd] *n.* 双刃剑 (Something that has or can have both favorable and unfavorable consequences).

🔹 **Another / privacy angle: / if / the model / uses / tools / (like / an external search), / it might / send / parts of / the user query / to those tools / (e.g., / to a web search API).**
🔸 **另一个 / 隐私角度是： / 如果 / 模型 / 使用了 / 工具 / （如 / 外部搜索）， / 它可能会 / 将 / 用户查询的 / 部分内容 / 发送到那些工具 / （例如 / 发送给网络搜索 API）。**
> 1. **Angle** [ˈæŋɡl] *n.* 角度 (A particular way of approaching or considering an issue or problem).

🔹 **A non-reasoning model / wouldn’t / do that / because / it doesn’t / use tools / at all; / a reasoning agent / might, / unless / carefully / controlled.**
🔸 **非推理模型 / 不会 / 那样做， / 因为 / 它完全不 / 使用工具； / 推理智能体 / 则可能会， / 除非 / 受到精细的 / 控制。**
> 1. **At all** [æt ɔːl] *adv.* 根本，完全 (Used to intensify a negative statement).

🔹 **That / has implications / if, / say, / the query / contained / personal data / that / shouldn’t / leave / a secure environment, / but / the agent / blithely / queries it / on Google.**
🔸 **这 / 会产生影响 / ——如果 / 假设 / 查询中 / 包含 / 不应 / 离开 / 安全环境的 / 个人数据， / 而 / 智能体 / 却若无其事地 / 在谷歌上 / 查询它。**
> 1. **Blithely** [ˈblaɪðli] *adv.* 快乐地，无忧无虑地 (In a casual and cheerful manner, often inappropriately).
> 【雅思/写作】常带有一点贬义，指“欠考虑地、不顾后果地”。

🔹 **Best practices / (discussed later) / include / sanitizing / or / filtering / what / the model / is allowed / to send out.**
🔸 **最佳实践 / （稍后讨论） / 包括 / 对 / 允许模型 / 发出的 / 内容进行 / 清洗 / 或 / 过滤。**
> 1. **Sanitize** [ˈsænɪtaɪz] *v.* 消毒，清洗（敏感数据） (To make clean and hygienic; to alter something as to make it more acceptable by removing improper or offensive parts).

🔹 **To summarize / this section: / reasoning models / differ / from / non-reasoning models / in their goals / (process- vs outcome-optimized), / inference behavior / (multi-step vs direct), / resource usage / (higher latency/cost), / output style / (explanatory vs concise), / and / integration / (often / used with tools / and / verification).**
🔸 **本节总结： / 推理模型 / 不同 / 于 / 非推理模型， / 体现在它们的目标 / （过程优化 vs 结果优化）、 / 推理行为 / （多步 vs 直接）、 / 资源使用 / （更高的延迟/成本）、 / 输出风格 / （解释性 vs 简洁） / 以及 / 集成方式 / （通常 / 与工具 / 和 / 验证配合使用）。**
> 1. **Verification** [ˌverɪfɪˈkeɪʃn] *n.* 验证 (The process of establishing the truth, accuracy, or validity of something).

🔹 **Neither / is / strictly “better” / universally / — each / is / suited / to different scenarios.**
🔸 **两者 / 在通用意义上 / 都没有 / 绝对的“优劣” / ——每一种 / 都 / 适合 / 不同的场景。**
> 1. **Universally** [ˌjuːnɪˈvɜːrsəli] *adv.* 普遍地，通用地 (In every case or by every person in the world).
> 2. **Scenario** [səˈnærioʊ] *n.* 场景，设想 (A setting, context, or sequence of events).

🔹 **The following table / encapsulates / these differences / for quick reference, / before / we move into / how / to choose / between them / in practice.**
🔸 **下表 / 概括了 / 这些差异 / 以供快速参考， / 随后 / 我们将进入 / 在实践中 / 如何 / 在两者之间 / 进行选择。**
> 1. **Encapsulate** [ɪnˈkæpsjuleɪt] *v.* 概括，封装 (To express the essential features of something succinctly).
> 【词性变化】**Capsule** (*n.* 胶囊)。
> 2. **Reference** [ˈrefrəns] *n.* 参考 (The action of mentioning or alluding to something).