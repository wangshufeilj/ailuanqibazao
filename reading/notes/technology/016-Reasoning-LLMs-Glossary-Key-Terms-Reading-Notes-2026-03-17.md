---
title: 推理大语言模型关键术语汇编 (Glossary of Key Terms in Reasoning LLMs)
source: 整理自 AI 研究领域经典论文与技术文档 (Compiled from seminal AI research papers and technical docs)
date: 2026-03-17
created_date: 2026-03-17
category: reading/notes/technology
tags:
  - 推理大模型
  - 思维链
  - CoT
  - ToT
  - GoT
  - ReAct
  - 过程监督
  - 结果监督
  - 提示注入
  - 术语表
  - 英语精读
  - LLM
  - o1
  - DeepSeek-R1
  - 词汇表
---

# 🟢 文章结构与背景信息 | Article Structure & Background Information

# 来源 (Source): 整理自 AI 研究领域经典论文与技术文档 (Compiled from seminal AI research papers and technical docs)
# 主题 (Topic): 推理大语言模型关键术语汇编 (Glossary of Key Terms in Reasoning LLMs)
# 核心价值 (Value): 本文涵盖了从 2020 年到 2025 年人工智能推理领域的核心术语，是理解当下"推理模型"（如 OpenAI o1, DeepSeek-R1）的必备学术词汇指南。

[Structure Map]
Root: Glossary of Key Terms in Reasoning LLMs (推理大语言模型术语表)
│
├── Part I: Foundation & Core Concepts (基础与核心概念)
│   ├── Large Language Model (基础架构)
│   └── Reasoning Model (推理模型定义)
│
├── Part II: Prompting & Behavioral Paradigms (提示工程与行为范式)
│   ├── Chain-of-Thought (思维链)
│   ├── Least-to-Most (从少到多)
│   └── ReAct Framework (推理-行动框架)
│
├── Part III: Advanced Reasoning Architectures (高级推理架构)
│   ├── Tree-of-Thought (思维树：分支探索)
│   └── Graph-of-Thought (思维图：网络化探索)
│
├── Part IV: Training & Evaluation Methodologies (训练与评估方法论)
│   ├── CoT Prompting vs. Tuning (提示与微调的区别)
│   ├── Process vs. Outcome Supervision (过程监督与结果监督)
│   ├── Verifier Model (验证器模型)
│   └── Test-time Compute (推理时计算/思维时间)
│
└── Part V: Security & Specialized Systems (安全与特化系统)
    ├── Prompt Injection (安全风险：提示注入)
    └── Hybrid Reasoning Model (效率平衡：混合推理)

---

### 🔹 **Glossary / of / Key Terms / in / Reasoning LLMs**
### 🔸 **推理大语言模型 / 关键 / 术语 / 表**

> 1. **Glossary** [ˈɡlɒsəri] (n. [C]): A list of technical or special words, especially those in a particular text, explaining their meanings. **术语表，词汇表**。
>    *   [搭配] A glossary of technical terms (技术术语表).
>    *   [考点] 写作中常用以对专业领域词汇进行总结。
> 2. **Reasoning** [ˈriːzənɪŋ] (n. [U]): The process of thinking about something in a logical way in order to form a conclusion or judgment. **推理，逻辑思考**。
>    *   [动词形式] **Reason** (v. 推理；说服).
>    *   [形容词] **Reasonable** (合理的).

---

### 🔹 **Large Language Model (LLM): / A machine learning model, / often with billions of parameters, / trained on vast text corpora / to predict and generate text.**
### 🔸 **大语言模型 (LLM)：/ 一种机器学习模型，/ 通常拥有数十亿个参数，/ 在海量文本语料库上训练，/ 用于预测和生成文本。**

> 1. **Parameter** [pəˈræmɪtə(r)] (n. [C]): In AI, a variable within a model whose value is determined by the training data. **参数**。
>    *   [扩展] **Variable** (变量); **Metric** (度量标准).
> 2. **Corpus** [ˈkɔːpəs] (n. [C]): A collection of written or spoken texts. **语料库**。
>    *   [复数形式] **Corpora** (本句中使用).
>    *   [考点] 雅思阅读中常涉及语言学话题。
> 3. **Predict** [prɪˈdɪkt] (v. [T]): To say that something will happen in the future. **预测**。
>    *   [名词] **Prediction**; [形容词] **Predictive**.
>    *   [同义] **Forecast, Anticipate**.

---

### 🔹 **LLMs / can / carry on / dialogues, / answer questions, / and / perform / various language tasks / based on / learned patterns / in data.**
### 🔸 **大语言模型 / 可以 / 进行 / 对话，/ 回答问题，/ 并且 / 执行 / 各种语言任务，/ 基于 / 数据中 / 学习到的模式。**

> 1. **Carry on** (phr. v.): To continue doing something; to engage in. **继续；进行（对话等）**。
>    *   [用法] Carry on a conversation (进行交谈).
> 2. **Perform** [pəˈfɔːm] (v. [T]): To do an action or piece of work. **执行，履行**。
>    *   [考点] 雅思写作常用词，替代简单的 "do"。
>    *   [名词] **Performance** (表现，性能).
> 3. **Pattern** [ˈpætən] (n. [C]): A regular and intelligible form or sequence discernible in certain actions or situations. **模式，规律**。

---

### 🔹 **Reasoning model: / An LLM / fine-tuned / to break complex problems / into / intermediate steps / ("reasoning traces") / before producing / a final answer.**
### 🔸 **推理模型：/ 一种经过 / 微调的 / 大语言模型，/ 旨在将复杂问题 / 分解为 / 中间步骤 / （"推理轨迹"），/ 然后产出 / 最终答案。**

> 1. **Fine-tune** [ˌfaɪn ˈtjuːn] (v. [T]): To make very small changes to something in order to make it as good or as effective as possible. **微调**。
>    *   [熟词僻义] "Tune" 常指调音，在此指优化模型参数。
> 2. **Intermediate** [ˌɪntəˈmiːdiət] (adj.): Located between two places, things, states, etc. **中间的，过渡的**。
>    *   [搭配] Intermediate level (中级水平).
> 3. **Trace** [treɪs] (n. [C]): A mark, object, or other indication of the existence or passing of something. **轨迹，踪迹**。
>    *   [动词] **Trace back to** (追溯到).

---

### 🔹 **It / "thinks aloud" / by generating / a chain-of-thought, / enabling / more systematic problem solving / (especially for math, logic, coding tasks).**
### 🔸 **它通过 / 生成 / 思维链 / 来进行 / "出声思考"，/ 从而实现 / 更系统的解题 / （特别是在数学、逻辑、编程任务中）。**

> 1. **Think aloud** (idiom): To speak one's thoughts as they occur. **出声思考，自言自语**。
>    *   [考点] 形象地描述推理模型的工作方式。
> 2. **Systematic** [ˌsɪstəˈmætɪk] (adj.): Done or acting according to a fixed plan or system; methodical. **系统的，有条理的**。
>    *   [副词] **Systematically**.
>    *   [反义] **Chaotic, Disorganized**.
> 3. **Enable** [ɪˈneɪbl] (v. [T]): To make it possible for somebody/something to do something. **使能够**。
>    *   [结构] **Enable sb. to do sth.**

---

### 🔹 **Chain-of-Thought (CoT): / A prompting technique / or / model behavior / where / the LLM / generates / a sequence of / intermediate reasoning steps / leading to / the final answer, / rather than / answering / immediately.**
### 🔸 **思维链 (CoT)：/ 一种提示技术 / 或 / 模型行为，/ 即 / 大语言模型 / 生成 / 一系列 / 中间推理步骤，/ 引导至 / 最终答案，/ 而不是 / 立即 / 回答。**

> 1. **Sequence** [ˈsiːkwəns] (n. [C]): A particular order in which related events, movements, or things follow each other. **顺序，序列**。
>    *   [形容词] **Sequential** (按次序的).
> 2. **Lead to** (phr. v.): To result in; to cause. **导致，引导至**。
>    *   [雅思同义] **Result in, Give rise to, Bring about**.
> 3. **Rather than** (prep.): Instead of. **而不是**。
>    *   [用法] 雅思阅读中常用于对比两类事物。

---

### 🔹 **CoT prompts / like / "Let's think step by step" / significantly / improve / performance / on multi-step problems.**
### 🔸 **思维链提示 / 例如 / "让我们一步步思考" / 显著地 / 提高 / 在多步问题上的 / 表现。**

> 1. **Significantly** [sɪɡˈnɪfɪkəntli] (adv.): In a sufficiently great or important way as to be worthy of attention. **显著地，重大地**。
>    *   [形容词] **Significant**; [名词] **Significance**.
>    *   [同义] **Considerably, Substantially**.
> 2. **Improve** [ɪmˈpruːv] (v. [I/T]): To make or become better. **改善，提高**。
>    *   [名词] **Improvement**.

---

### 🔹 **Self-consistency: / An inference strategy / where / multiple reasoning paths / are sampled / and / the most common answer / among them / is chosen, / assuming / the correct answer / will appear / consistently.**
### 🔸 **自一致性：/ 一种推理策略，/ 即 / 采样 / 多条推理路径 / 并 / 选择其中 / 最常见的答案，/ 假设 / 正确答案 / 会一致地 / 出现。**

> 1. **Inference** [ˈɪnfərəns] (n. [C/U]): The act or process of reaching a conclusion about something from known facts or evidence. **推理，推断**。
>    *   [动词] **Infer**.
> 2. **Sample** [ˈsɑːmpl] (v. [T]): To take a small amount of something to test it. **采样，取样**。
>    *   [熟词僻义] 常见为"样本（名词）"。
> 3. **Consistently** [kənˈsɪstəntli] (adv.): In a way that does not change and is always the same. **一致地，始终如一地**。
>    *   [名词] **Consistency**.

---

### 🔹 **This / majority voting approach / reduces / random errors / in / chain-of-thought reasoning.**
### 🔸 **这种 / 多数投票法 / 减少了 / 思维链推理中的 / 随机错误。**

> 1. **Majority voting** [məˈdʒɒrəti ˈvəʊtɪŋ] (n.): A system where the option with the most votes wins. **多数投票制**。
> 2. **Approach** [əˈprəʊtʃ] (n. [C]): A way of dealing with something. **方法，方式**。
>    *   [同义] **Method, Strategy**.
> 3. **Random** [ˈrændəm] (adj.): Done, chosen, or happening without method or conscious decision. **随机的**。

---

### 🔹 **Least-to-Most prompting: / A prompting strategy / that / breaks a complex problem / into / a sequence of / smaller sub-problems / (least complex first, then progressively harder) / and / solves / them / one by one.**
### 🔸 **从少到多提示：/ 一种提示策略，/ 它 / 将复杂问题分解为 / 一系列 / 较小的子问题 / （先是最简单的，然后逐渐变难） / 并且 / 逐一 / 解决 / 它们。**

> 1. **Progressively** [prəˈɡresɪvli] (adv.): Steadily and in stages. **渐进地，逐渐地**。
>    *   [动词] **Progress** (进步).
> 2. **Sub-problem** [sʌb ˈprɒbləm] (n. [C]): A part of a larger problem. **子问题**。
>    *   [前缀] **Sub-** 表示"下的，次的"。
> 3. **One by one** (idiom): Separately and in order. **逐个地，依次地**。

---

### 🔹 **It / helps / LLMs / handle / tasks / requiring / decomposition / and / yields / better accuracy / on / symbolic and multi-step tasks.**
### 🔸 **它 / 帮助 / 大语言模型 / 处理 / 需要 / 分解的 / 任务，/ 并在 / 符号和多步任务上 / 产生 / 更好的准确率。**

> 1. **Handle** [ˈhændl] (v. [T]): To deal with or control. **处理，应付**。
>    *   [雅思同义] **Cope with, Address, Tackle**.
> 2. **Decomposition** [ˌdiːˌkɒmpəˈzɪʃn] (n. [U]): The process of breaking down into components or basic elements. **分解**。
>    *   [动词] **Decompose**.
> 3. **Yield** [jiːld] (v. [T]): To produce or provide (a natural product, profit, or result). **产生，屈服**。
>    *   [熟词僻义] 常用义为"让步"，在此指"产出结果"。
> 4. **Symbolic** [sɪmˈbɒlɪk] (adj.): Relating to or using symbols. **符号的**。

---

### 🔹 **ReAct framework: / A paradigm / where / the LLM / interleaves / Reasoning (CoT thought processes) / and / Acting (taking actions like API calls or tool use).**
### 🔸 **ReAct 框架：/ 一种范式，/ 即 / 大语言模型 / 交替进行 / 推理（CoT 思维过程） / 和 / 行动（执行 API 调用或工具使用等动作）。**

> 1. **Paradigm** [ˈpærədaɪm] (n. [C]): A typical example or pattern of something; a model. **范式，典范**。
>    *   [用法] Paradigm shift (范式转移/重大变革).
> 2. **Interleave** [ˌɪntəˈliːv] (v. [T]): To place something between the pages of a book or the layers of something. **交替，交织**。
>    *   [考点] 描述两个过程交叉进行。
> 3. **API call** (n.): Application Programming Interface call, a way for models to talk to external software. **API 调用**。

---

### 🔹 **The LLM / generates / thoughts and actions / alternately, / enabling / it / to / query external tools, / observe results, / and / refine / its reasoning / iteratively.**
### 🔸 **大语言模型 / 交替地 / 生成 / 想法和行动，/ 使其 / 能够 / 查询外部工具，/ 观察结果，/ 并且 / 迭代地 / 完善 / 其推理。**

> 1. **Alternately** [ɔːlˈtɜːnətli] (adv.): In a way that involves two things happening or following each other repeatedly. **交替地**。
>    *   [形容词] **Alternate**; [名词] **Alternative** (备选方案).
> 2. **Refine** [rɪˈfaɪn] (v. [T]): To improve something by making small changes to it. **完善，精炼**。
>    *   [名词] **Refinement**.
> 3. **Iteratively** [ˈɪtərətɪvli] (adv.): In a way that involves repeating a process or set of instructions. **迭代地**。
>    *   [名词] **Iteration**.

---

### 🔹 **Tree-of-Thought (ToT): / An approach / that / generalizes / CoT / by exploring / a tree of / possible reasoning steps.**
### 🔸 **思维树 (ToT)：/ 一种方法，/ 它 / 通过 / 探索 / 可能推理步骤的 / 树状结构 / 来 / 推广 / 思维链。**

> 1. **Generalize** [ˈdʒenrəlaɪz] (v. [T]): To extend the application of (something) to a larger field. **概括，推广**。
>    *   [名词] **Generalization**.
> 2. **Explore** [ɪkˈsplɔː(r)] (v. [T]): To examine or consider something thoroughly. **探索**。

---

### 🔹 **At each step, / the model / can / branch into / multiple possible "thoughts," / and / a search procedure / (depth-first, breadth-first, with heuristic evaluations) / is used / to find / the best path / to a solution.**
### 🔸 **在每一步，/ 模型 / 可以 / 分支成 / 多个可能的"想法"，/ 并且 / 使用 / 一种搜索程序 / （深度优先、广度优先及启发式评估） / 来找到 / 通往解决方案的 / 最佳路径。**

> 1. **Branch** [brɑːntʃ] (v. [I]): To divide into two or more parts or directions. **分支，分叉**。
> 2. **Procedure** [prəˈsiːdʒə(r)] (n. [C/U]): A set of actions that is the official or accepted way of doing something. **程序，步骤**。
> 3. **Heuristic** [hjuˈrɪstɪk] (adj.): Proceeding to a solution by trial and error or by rules that are only loosely defined. **启发式的**。

---

### 🔹 **Graph-of-Thought (GoT): / An extension of ToT / where / the reasoning process / forms / an arbitrary graph / (not just a tree).**
### 🔸 **思维图 (GoT)：/ 思维树的扩展，/ 其中 / 推理过程 / 形成 / 一个任意的图形 / （不只是树）。**

> 1. **Extension** [ɪkˈstenʃn] (n. [C/U]): A part that is added to something to enlarge or prolong it. **扩展，延伸**。
>    *   [动词] **Extend**.
> 2. **Arbitrary** [ˈɑːbɪtrəri] (adj.): Based on random choice or personal whim, rather than any reason or system. **任意的，武断的**。

---

### 🔹 **Thoughts / are / nodes / and / can / have / multiple predecessors and successors, / allowing / merging and diverging / of / reasoning paths.**
### 🔸 **想法 / 是 / 节点 / 并且 / 可以 / 拥有 / 多个前驱和后继，/ 允许 / 推理路径的 / 合并和发散。**

> 1. **Predecessor** [ˈpriːdəsesə(r)] (n. [C]): A thing that has been followed or replaced by another. **前任，前驱**。
> 2. **Successor** [səkˈsesə(r)] (n. [C]): A thing that comes after another. **继任者，后继**。
> 3. **Merge** [mɜːdʒ] (v. [I/T]): To combine or make two or more things combine to form a single thing. **合并**。
> 4. **Diverge** [daɪˈvɜːdʒ] (v. [I]): (Of paths, opinions, etc.) to separate and go in different directions. **发散，分叉**。

---

### 🔹 **This / enables / even more flexible exploration / of / solution paths / than / a tree search.**
### 🔸 **这 / 使得 / 相比 / 树搜索，/ 能够 / 对解决方案路径进行 / 更加灵活的探索。**

> 1. **Flexible** [ˈfleksəbl] (adj.): Able to change or be changed easily according to the situation. **灵活的**。
>    *   [名词] **Flexibility**.

---

### 🔹 **Chain-of-Thought prompting vs. tuning: / CoT prompting / refers to / providing / instructions or examples / at inference time / to / induce / step-by-step reasoning.**
### 🔸 **思维链提示 vs. 调优：/ 思维链提示 / 指的是 / 在推理阶段 / 提供 / 指令或示例 / 以 / 诱导 / 逐步推理。**

> 1. **Refer to** (phr. v.): To mention or describe something. **提及，指的是**。
> 2. **Induce** [ɪnˈdjuːs] (v. [T]): To succeed in persuading or leading someone to do something; to cause. **诱导，引起**。
>    *   [名词] **Induction**.

---

### 🔹 **CoT fine-tuning / refers to / training the model / (usually via supervised or RL) / to / internally / generate / chains-of-thought.**
### 🔸 **思维链微调 / 指的是 / 训练模型 / （通常通过监督学习或强化学习） / 以 / 在内部 / 生成 / 思维链。**

> 1. **Supervised** [ˈsuːpəvaɪzd] (adj.): Controlled or watched by someone. **监督的**。
>    *   [名词] **Supervision**.
> 2. **RL (Reinforcement Learning)** (n.): A type of machine learning where an agent learns to make decisions by performing actions and receiving rewards. **强化学习**。
> 3. **Internally** [ɪnˈtɜːnəli] (adv.): In a way that exists or happens inside something. **内部地**。

---

### 🔹 **Fine-tuned reasoning models / often / keep / CoT / hidden / by default, / whereas / prompting / makes / it / explicit / in outputs.**
### 🔸 **经过微调的推理模型 / 通常 / 默认 / 保持 / 思维链 / 隐藏，/ 而 / 提示 / 则使 / 其 / 在输出中 / 显式化。**

> 1. **By default** (idiom): If you do not make a different decision or choice. **默认情况下**。
> 2. **Whereas** [ˌweərˈæz] (conj.): Used to compare or contrast two facts. **然而，但是**。
>    *   [考点] 雅思写作中用于引导对比连词。
> 3. **Explicit** [ɪkˈsplɪsɪt] (adj.): Stated clearly and in detail, leaving no room for confusion or doubt. **显式的，明确的**。
>    *   [反义] **Implicit** (隐式的).

---

### 🔹 **Process supervision: / A training approach / where / the model / is rewarded / for / the correctness / of / each step / in / its reasoning process / (not just the final answer).**
### 🔸 **过程监督：/ 一种训练方法，/ 其中 / 模型 / 因 / 其推理过程中 / 每一步 / 的正确性 / 而获得奖励 / （而不只是最终答案）。**

> 1. **Reward** [rɪˈwɔːd] (v. [T]): To give something to somebody because they have done something good or helpful. **奖励**。
> 2. **Correctness** [kəˈrektnəs] (n. [U]): The quality of being right. **正确性**。

---

### 🔹 **This / requires / a way / to / evaluate or label / intermediate steps / as / valid or not.**
### 🔸 **这 / 需要 / 一种方法 / 来 / 评估或标记 / 中间步骤 / 是否 / 有效。**

> 1. **Evaluate** [ɪˈvæljueɪt] (v. [T]): To form an opinion of the amount, value, or quality of something. **评估**。
>    *   [名词] **Evaluation**.
> 2. **Valid** [ˈvælɪd] (adj.): Based on what is logical or true. **有效的，合理的**。
>    *   [名词] **Validity**.

---

### 🔹 **Process supervision / aims / to / produce / more interpretable and reliable / chains-of-thought.**
### 🔸 **过程监督 / 旨在 / 产出 / 更具可解释性和可靠性的 / 思维链。**

> 1. **Interpretable** [ɪnˈtɜːprətəbl] (adj.): Able to be explained or understood. **可解释的**。
> 2. **Reliable** [rɪˈlaɪəbl] (adj.): That can be trusted to do something well. **可靠的**。
>    *   [名词] **Reliability**.

---

### 🔹 **Outcome supervision: / A training approach / where / the model / is rewarded / based only on / the final outcome / (e.g. whether the final answer is correct).**
### 🔸 **结果监督：/ 一种训练方法，/ 其中 / 模型 / 仅根据 / 最终结果 / 获得奖励 / （例如最终答案是否正确）。**

> 1. **Outcome** [ˈaʊtkʌm] (n. [C]): The final result of an election, or a process. **结果**。

---

### 🔹 **The internal reasoning steps / are not / directly / constrained / – a correct final answer / yields / a reward / regardless of / how / the model / arrived at it.**
### 🔸 **内部推理步骤 / 没有被 / 直接 / 约束 / —— 只要最终答案正确 / 就会产生 / 奖励，/ 无论 / 模型 / 是如何得出它的。**

> 1. **Constrain** [kənˈstreɪn] (v. [T]): To force somebody to do something or behave in a particular way. **约束，限制**。
>    *   [名词] **Constraint**.
> 2. **Regardless of** (prep.): Without being affected by something. **不管，不论**。
> 3. **Arrive at** (phr. v.): To reach a decision, conclusion, or agreement. **达成，得出（结论等）**。

---

### 🔹 **This / is / simpler / but / can / reinforce / spurious reasoning.**
### 🔸 **这 / 更简单 / 但 / 可能 / 强化 / 虚假推理。**

> 1. **Reinforce** [ˌriːɪnˈfɔːs] (v. [T]): To make a feeling, an idea, etc. stronger. **强化，增强**。
> 2. **Spurious** [ˈspjʊəriəs] (adj.): False, although seeming to be genuine or true. **虚假的，伪造的**。
>    *   [考点] 雅思/考研英语高级词汇。

---

### 🔹 **Test-time compute (inference compute): / The computational resources and operations / a model / uses / to generate / an answer / at inference time.**
### 🔸 **推理时计算 (inference compute)：/ 模型 / 在推理时 / 用于生成 / 答案的 / 计算资源和操作。**

> 1. **Computational** [ˌkɒmpjuˈteɪʃənl] (adj.): Involving the use of computers or mathematical calculations. **计算的**。
> 2. **Operation** [ˌɒpəˈreɪʃn] (n. [C]): A process or action that is part of a plan. **操作，运算**。

---

### 🔹 **Increasing / test-time compute / – for example / by allowing / the model / to generate / multiple solutions / or / longer chains-of-thought / – often / boosts / performance / on complex tasks.**
### 🔸 **增加 / 推理时计算 / —— 例如 / 通过允许 / 模型 / 生成 / 多个解决方案 / 或 / 更长的思维链 / —— 通常会 / 提升 / 在复杂任务上的 / 表现。**

> 1. **Boost** [buːst] (v. [T]): To make something increase, or become better or more successful. **提升，推动**。

---

### 🔹 **It's / analogous to / "thinking longer" / on / a question.**
### 🔸 **这 / 类似于 / 在一个问题上 / "思考得更久"。**

> 1. **Analogous** [əˈnæləɡəs] (adj.): Comparable in certain respects. **类似的，可比拟的**。
>    *   [名词] **Analogy** (类比).
>    *   [搭配] **be analogous to sth.** (与某物类似).

---

### 🔹 **Verifier model: / An auxiliary model (or function) / used / to check / the correctness or consistency / of / either / the chain-of-thought / or / the final answer.**
### 🔸 **验证器模型：/ 一种辅助模型（或函数），/ 用于 / 检查 / 思维链 / 或 / 最终答案的 / 正确性或一致性。**

> 1. **Auxiliary** [ɔːɡˈzɪliəri] (adj.): Giving help or support to the main group of people. **辅助的，备用的**。

---

### 🔹 **For instance, / a verifier / might / re-evaluate / a solution / or / catch errors / in reasoning, / providing / a form of / quality control.**
### 🔸 **例如，/ 验证器 / 可能会 / 重新评估 / 解决方案 / 或 / 捕捉 / 推理中的 / 错误，/ 提供 / 一种形式的 / 质量控制。**

> 1. **Catch** [kætʃ] (v. [T]): To discover or find something, especially a mistake. **捕捉，发现（错误）**。

---

### 🔹 **Verifiers / can be / separate LLMs / trained / as / critics / or / simple evaluators / like / code test runners.**
### 🔸 **验证器 / 可以是 / 独立的 / 被训练 / 作为 / 评论者 / 的大语言模型，/ 或者是 / 像代码测试运行器那样的 / 简单评估器。**

> 1. **Critic** [ˈkrɪtɪk] (n. [C]): A person who expresses opinions about the good and bad qualities of something. **评论者，批评家**。

---

### 🔹 **Prompt injection (in agents): / A security exploit / where / malicious input / is crafted / to / hijack / the model's prompt or chain-of-thought, / causing / it / to / ignore / original instructions / or / perform / unintended actions.**
### 🔸 **提示注入（在智能体中）：/ 一种安全漏洞，/ 其中 / 恶意输入 / 被精心设计 / 以 / 劫持 / 模型的提示或思维链，/ 导致 / 其 / 忽略 / 原始指令 / 或 / 执行 / 非预期的行动。**

> 1. **Exploit** [ˈeksplɔɪt] (n. [C]): A way of using a system or piece of software that relies on a bug or vulnerability. **漏洞利用**。
>    *   [动词] **Exploit** (利用，剥削).
> 2. **Malicious** [məˈlɪʃəs] (adj.): Intending to do harm. **恶意的**。
>    *   [名词] **Malice**.
> 3. **Craft** [krɑːft] (v. [T]): To make something using a lot of skill. **精心制作**。
> 4. **Hijack** [ˈhaɪdʒæk] (v. [T]): To take control of something illegally. **劫持**。
> 5. **Unintended** [ˌʌnɪnˈtendɪd] (adj.): Not planned or intended. **非预期的**。

---

### 🔹 **In / agent scenarios / (with tools), / prompt injection / can / lead the LLM / to / execute / harmful commands / or / reveal / secrets / by manipulating / the context / it processes.**
### 🔸 **在 / 智能体场景中 / （带有工具），/ 提示注入 / 可能 / 引导大语言模型 / 去 / 执行 / 有害命令 / 或 / 泄露 / 秘密，/ 通过操纵 / 它处理的 / 上下文。**

> 1. **Execute** [ˈeksɪkjuːt] (v. [T]): To carry out an instruction or a program. **执行**。
> 2. **Reveal** [rɪˈviːl] (v. [T]): To make something known to somebody. **揭露，泄露**。
> 3. **Manipulate** [məˈnɪpjuleɪt] (v. [T]): To control or influence something or someone, often in a dishonest way. **操纵**。

---

### 🔹 **Hybrid reasoning model: / A model or system / that / can / toggle / between / reasoning mode / and / a faster standard mode / depending on / the task.**
### 🔸 **混合推理模型：/ 一个模型或系统，/ 它 / 可以 / 在 / 推理模式 / 和 / 更快的标准模式 / 之间 / 切换，/ 取决于 / 任务。**

> 1. **Toggle** [ˈtɒɡl] (v. [I/T]): To switch between two different settings on a computer. **切换**。
> 2. **Depending on** (prep.): Used to say that something is decided by something else. **取决于**。

---

### 🔹 **For example, / IBM's Granite 3.2 / allows / users / to / enable / "thinking" / for complex queries / but / skip / it / for simple ones.**
### 🔸 **例如，/ IBM 的 Granite 3.2 / 允许 / 用户 / 对复杂查询 / 开启 / "思考"，/ 但 / 对简单查询 / 跳过 / 它。**

> 1. **Query** [ˈkwɪəri] (n. [C]): A question, especially one expressing doubt or requesting information. **查询，疑问**。

---

### 🔹 **This / hybrid approach / aims / to / balance / performance and efficiency / on / a case-by-case basis.**
### 🔸 **这种 / 混合方法 / 旨在 / 在 / 具体情况具体分析的基础上 / 平衡 / 性能和效率。**

> 1. **Efficiency** [ɪˈfɪʃnsi] (n. [U]): The quality of doing something well with no waste of time or money. **效率**。
> 2. **On a case-by-case basis** (idiom): Looking at each situation individually. **视具体情况而定，逐案处理**。

---

### 📝 **人物/组织/机构背景注释 (Entity Annotations)**

*   **OpenAI**: 美国人工智能研究实验室，代表作包括 ChatGPT 和文中提到的 **o1** 系列推理模型。
*   **IBM**: 国际商业机器公司，其 **Granite** 系列模型是企业级开源模型的代表。
*   **DeepMind**: 谷歌旗下的顶尖 AI 实验室，在强化学习和搜索算法方面有深厚积淀。
*   **GPT-3 (Generative Pre-trained Transformer 3)**: 由 OpenAI 在 2020 年发布的里程碑式模型，开启了大模型时代。
*   **DeepSeek**: 中国人工智能公司（深度求索），在 2025 年发布的 **DeepSeek-R1** 是开源推理模型的领军者之一。
*   **Wei et al. (Jason Wei)**: 思维链 (CoT) 的核心提出者，曾就职于 Google Brain 和 OpenAI。
