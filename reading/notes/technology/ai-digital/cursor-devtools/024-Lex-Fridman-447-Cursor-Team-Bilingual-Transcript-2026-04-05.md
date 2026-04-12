---
title: "Lex Fridman #447：Cursor 团队 — 编程与 AI 的未来（中英双语逐行对照）"
source: Lex Fridman Podcast
source_url: https://lexfridman.com/cursor-team-transcript/
youtube_url: https://www.youtube.com/watch?v=oFfVt3S51T4
episode: 447
date: 2024-10-06
created_date: 2026-04-05
category: reading/notes/technology/ai-digital/cursor-devtools
related_english: forum/technology/007-Lex-Fridman-Podcast-447-Cursor-Team-Full-Transcript-2026-04-05.md
guests:
  - Michael Truell
  - Sualeh Asif
  - Arvid Lunnemark
  - Aman Sanger
tags:
  - Lex Fridman
  - Cursor
  - 双语精读
  - AI 编程
  - 播客转录
  - VS Code
note: 英文逐行下附中文；英文行行尾两空格为 Markdown 硬换行。转录可能有口误，译文按语义处理。
---

# Lex Fridman #447 — Cursor Team: Future of Programming with AI（中英对照）

**英文全文（无中文）**：[📄 007 英文-only 转录稿](../../forum/technology/007-Lex-Fridman-Podcast-447-Cursor-Team-Full-Transcript-2026-04-05.md)

**术语速览**：scaling laws / 缩放定律；MOE / 混合专家稀疏模型；KV cache / 键值缓存；LSP / 语言服务器协议；TTFT / 首 token 延迟；RLHF / 人类反馈强化学习；SWE-Bench / 软件工程评测集。

This is a transcript of Lex Fridman Podcast #447 with Cursor Team. The timestamps in the transcript are clickable links that take you directly to that point in the main video. Please note that the transcript is human generated, and may have errors. Here are some useful links:  
这是 Lex Fridman 播客第 447 期与 Cursor 团队的对话转录。文中的时间戳是可点击链接，可跳到视频对应位置。请注意转录为人工整理，可能有误。有用链接如下：

- Go back to [this episode’s main page](https://lexfridman.com/cursor-team/)  
- 返回[本期节目主页](https://lexfridman.com/cursor-team/)
- Watch the [full YouTube version of the podcast](https://youtube.com/watch?v=oFfVt3S51T4)  
- 观看[完整 YouTube 播客](https://youtube.com/watch?v=oFfVt3S51T4)

## Table of Contents  
## 目录

Here are the loose “chapters” in the conversation. Click link to jump approximately to that part in the transcript:  
下面是谈话的大致「章节」，点击链接可大致跳到转录对应位置：

- 0:00 – Introduction — 0:00 – 导语  
- 0:59 – Code editor basics — 0:59 – 代码编辑器基础  
- 3:09 – GitHub Copilot — 3:09 – GitHub Copilot  
- 10:27 – Cursor — 10:27 – Cursor  
- 16:54 – Cursor Tab — 16:54 – Cursor Tab（Tab 补全）  
- 23:08 – Code diff — 23:08 – 代码 diff  
- 31:20 – ML details — 31:20 – 机器学习细节  
- 36:54 – GPT vs Claude — 36:54 – GPT 对 Claude  
- 43:28 – Prompt engineering — 43:28 – 提示工程  
- 50:54 – AI agents — 50:54 – AI 智能体  
- 1:04:51 – Running code in background — 1:04:51 – 后台运行代码  
- 1:09:31 – Debugging — 1:09:31 – 调试  
- 1:14:58 – Dangerous code — 1:14:58 – 「危险」代码  
- 1:26:09 – Branching file systems — 1:26:09 – 分支文件系统  
- 1:29:20 – Scaling challenges — 1:29:20 – 规模化挑战  
- 1:43:32 – Context — 1:43:32 – 上下文  
- 1:48:39 – OpenAI o1 — 1:48:39 – OpenAI o1  
- 2:00:01 – Synthetic data — 2:00:01 – 合成数据  
- 2:03:48 – RLHF vs RLAIF — 2:03:48 – RLHF 与 RLAIF  
- 2:05:34 – Fields Medal for AI — 2:05:34 – AI 与菲尔兹奖  
- 2:08:17 – Scaling laws — 2:08:17 – 缩放定律  
- 2:17:06 – The future of programming — 2:17:06 – 编程的未来  

## Introduction  
## 导语

Lex [(00:00:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=0) The following is a conversation with the founding members of the Cursor team, Michael Truell, Sualeh Asif, Arvid Lunnemark, and Aman Sanger. Cursor is a code editor based on VS Code that adds a lot of powerful features for AI-assisted coding. It has captivated the attention and excitement of the programming and AI communities. So I thought this is an excellent opportunity to dive deep into the role of AI in programming. This is a super technical conversation that is bigger than just about one code editor. It’s about the future of programming and in general, the future of human AI collaboration in designing and engineering complicated and powerful systems. This is the Lex Fridman podcast. To support it, please check out our sponsors in the description. And now, dear friends, here’s Michael, Sualeh, Arvid and Aman.  
Lex（00:00:00）下面是对话 Cursor 团队创始成员 Michael Truell、Sualeh Asif、Arvid Lunnemark 与 Aman Sanger。Cursor 是基于 VS Code 的代码编辑器，为 AI 辅助编程增加了许多强大功能，在编程与 AI 社区都引起大量关注与兴奋。我认为这是深入探讨 AI 在编程中角色的好机会。本期技术对话不止于一款编辑器，而是关于编程的未来，以及总体上人类与 AI 在设计与工程化复杂强大系统时的协作未来。这里是 Lex Fridman 播客；欢迎通过片头赞助商支持节目。下面有请 Michael、Sualeh、Arvid 与 Aman。

## Code editor basics  
## 代码编辑器基础

Lex [(00:00:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=59) All right, this is awesome. We have Michael, Aman, Sualeh, Arvid here from the Cursor team. First up, big ridiculous question. What’s the point of a code editor?  
Lex（00:00:59）好，这太棒了。Cursor 团队的 Michael、Aman、Sualeh、Arvid 在场。先来一个很大的「傻问题」：代码编辑器的意义是什么？

Michael [(00:01:10)](https://youtube.com/watch?v=oFfVt3S51T4&t=70) So the code editor is largely the place where you build software and today or for a long time, that’s meant the place where you text edit a formal programming language. And for people who aren’t programmers, the way to think of a code editor is a really souped up word processor for programmers, where the reason it’s souped up is code has a lot of structure. And so the “word processor,” the code editor can actually do a lot for you that word processors sort of in the writing space haven’t been able to do for people editing texts there.  
Michael（00:01:10）在很大程度上，代码编辑器就是你构建软件的地方；长久以来，这意味着你在用文本编辑一门形式化的编程语言。对非程序员来说，可以把代码编辑器想成给程序员用的、加强版文字处理器——之所以「加强」，是因为代码结构很强，所以这款「文字处理器」能做的事，比在写作场景里编辑普通文本的文字处理器多得多。

[(00:01:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=102) And so that’s everything from giving you visual differentiation of the actual tokens in the code so you can scan it quickly to letting you navigate around the code base, sort of like you’re navigating around the internet with hyperlinks, you’re going to definitions of things you’re using to error checking to catch rudimentary bugs. And so traditionally that’s what a code editor has meant. And I think that what a code editor is is going to change a lot over the next 10 years as what it means to build software maybe starts to look a bit different.  
（00:01:42）包括：把代码里的 token 视觉区分开让你快速扫读；像在网上点超链接一样在代码库里跳转、跳到所用符号的定义；以及错误检查以抓住初级 bug。传统上这就是代码编辑器的含义。我认为未来十年「代码编辑器是什么」会大变，因为「构建软件」这件事本身可能开始看起来不太一样。

Lex [(00:02:16)](https://youtube.com/watch?v=oFfVt3S51T4&t=136) I think also a code editor should just be fun.  
Lex（00:02:16）我觉得代码编辑器还应该好玩。

Arvid [(00:02:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=139) Yes, that is very important. That is very important. And it’s actually sort of an underrated aspect of how we decide what to build. A lot of the things that we build and then we try them out, we do an experiment and then we actually throw them out because they’re not fun. And so a big part of being fun is being fast a lot of the time. Fast is fun.  
Arvid（00:02:19）对，这很重要，真的很重要。这其实有点被我们决定做什么时低估了：很多东西我们做了、试了、做实验，最后扔掉，因为不好玩。好玩很大一部分意味着经常要快——快就好玩。

Lex [(00:02:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=162) Yeah, fast is… That should be a T-shirt.  
Lex（00:02:42）对，快就是……这句该印 T 恤。

Michael [(00:02:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=168) Fundamentally, I think one of the things that draws a lot of people to building stuff on computers is this insane iteration speed, where in other disciplines you might be sort of gate capped by resources or the ability… Even the ability to get a large group together and coding is this amazing thing where it’s you and the computer and that alone, you can build really cool stuff really quickly.  
Michael（00:02:48）根本上，我觉得很多人被在电脑上造东西吸引，原因之一是疯狂的迭代速度——别的领域你可能被资源或能力门槛卡住；而编程很神奇：你和电脑，就能很快做出很酷的东西。

## GitHub Copilot  
## GitHub Copilot

Lex [(00:03:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=189) So for people who don’t know, Cursor is this super cool new editor that’s a fork of VS Code. It would be interesting to get your explanation of your own journey of editors. I think all of you were big fans of VS Code with Copilot. How did you arrive to VS Code and how did that lead to your journey with Cursor?  
Lex（00:03:09）不了解的人说一下：Cursor 是很酷的新编辑器，是 VS Code 的分支。想听听你们自己用编辑器的心路。我想你们都曾是很喜欢「VS Code + Copilot」的用户。你们怎么转到 VS Code，又怎么走向做 Cursor？

Aman [(00:03:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=213) Yeah, so I think a lot of us… Well, all of us were originally [inaudible 00:03:39] users.  
Aman（00:03:33）我们很多人——其实所有人——最初都是……（听不清）用户。

Sualeh [(00:03:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=219) Pure Vim.  
Sualeh（00:03:39）纯 Vim。

Aman [(00:03:40)](https://youtube.com/watch?v=oFfVt3S51T4&t=220) Pure Vim. Yeah. No Neovim, just Pure Vim and a terminal. And at least for myself, it was around the time that Copilot came out, so 2021 that I really wanted to try it. So I went into VS Code, the only code editor in which it was available, and even though I really enjoyed using Vim, just the experience of Copilot with VS Code was more than good enough to convince me to switch. And so that kind of was the default until we started working on Cursor.  
Aman（00:03:40）纯 Vim。对，不是 Neovim，就是纯 Vim 加终端。至少对我自己来说，Copilot 出来的大概 2021 年我很想试，于是进了 VS Code——当时只有这个编辑器能用 Copilot。尽管我很喜欢 Vim，但 VS Code 里 Copilot 的体验已经足够好，让我愿意切换。后来这就成了默认组合，直到我们开始做 Cursor。

Lex [(00:04:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=254) And maybe we should explain what Copilot does. It’s a really nice auto complete. As you start writing a thing, it suggests one or two or three lines how to complete the thing. And there’s a fun experience in that. You know like when you have a close friendship and your friend completes your sentences? When it’s done well, there’s an intimate feeling. There’s probably a better word than intimate, but there’s a cool feeling of holy shit, it gets me. And then there’s an unpleasant feeling when it doesn’t get you. And so there’s that kind of friction. But I would say for a lot of people, the feeling that it gets me overpowers that it doesn’t.  
Lex（00:04:14）也许该解释一下 Copilot 做什么：很好的自动补全。你写东西时，它会建议一两三行来完成。这有种好玩的体验——像密友接你的话；接得好时有种「被懂」的感觉（也许比 intimate 更合适的词），就是「我靠，它懂我」。接不好时就不爽。所以有摩擦。但对很多人来说，「懂我」的感觉压过「不懂」。

Arvid [(00:04:55)](https://youtube.com/watch?v=oFfVt3S51T4&t=295) And I think actually one of the underrated aspects of Github Copilot is that even when it’s wrong, it’s a little bit annoying, but it’s not that bad because you just type another character and then maybe then it gets you, or you type another character and then it gets you. So even when it’s wrong, it’s not that bad.  
Arvid（00:04:55）我觉得 GitHub Copilot 一个被低估的点是：就算错了有点烦，也没那么糟——你再敲一个字符，也许就对了；再敲一个，又对了。所以错了也没那么糟。

Sualeh [(00:05:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=309) You can sort of iterate and fix it. I mean, the other underrated part of Copilot for me was just the first real AI product. So the first language model consumer product.  
Sualeh（00:05:09）你可以迭代修正。对我来说 Copilot 另一个被低估之处是：它是第一个真正的 AI 产品——第一个面向消费者的语言模型产品。

Lex [(00:05:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=321) So Copilot was kind of like the first killer app for LMs.  
Lex（00:05:21）所以 Copilot 有点像语言模型的第一个杀手级应用。

Michael [(00:05:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=325) Yeah. And the beta was out in 2021.  
Michael（00:05:25）对，公测是 2021 年。

Lex [(00:05:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=329) Right. Okay. So what’s the origin story of Cursor?  
Lex（00:05:29）好。那 Cursor 的起源故事是什么？

Michael [(00:05:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=334) So around 2020, the scaling loss papers came out from OpenAI and that was a moment where this looked like clear predictable progress for the field where even if we didn’t have any more ideas, it looked like you could make these models a lot better if you had more compute and more data.  
Michael（00:05:34）大概 2020 年 OpenAI 发表了 scaling loss（缩放损失）论文，那一刻看起来领域里有清晰可预期的进展——就算没有新点子，只要有更多算力和数据，模型就能好很多。

Lex [(00:05:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=349) By the way, we’ll probably talk for three to four hours on the topic of scaling loss. But just to summarize, it’s a paper in a set of papers in a set of ideas that say bigger might be better for model size and data size in the realm of machine learning.  
Lex（00:05:49）顺便说我们可能花三四小时聊 scaling loss。简单讲，它属于一系列论文与观点：在机器学习里，模型更大、数据更大，可能更好。

Sualeh [(00:06:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=365) It’s bigger and better, but predictably better.  
Sualeh（00:06:05）更大也更好，而且是可预期地更好。

Lex [(00:06:08)](https://youtube.com/watch?v=oFfVt3S51T4&t=368) Okay, that’s another topic of conversation.  
Lex（00:06:08）好，这又是另一个话题。

Arvid [(00:06:10)](https://youtube.com/watch?v=oFfVt3S51T4&t=370) Yes. Yeah.  
Arvid（00:06:10）对，是的。

Michael [(00:06:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=371) So around that time for some of us, there were a lot of conceptual conversations about what’s this going to look like? What’s the story going to be for all these different knowledge worker fields about how they’re going to be made better by this technology getting better? And then I think there were a couple of moments where the theoretical gains predicted in that paper started to feel really concrete and it started to feel like a moment where you could actually go and not do a PhD if you wanted to do useful work in AI. It actually felt like now there was this whole set of systems one could build that were really useful. And I think that the first moment we already talked about a little bit, which was playing with the early beta of Copilot, that was awesome and magical.  
Michael（00:06:11）那时对我们有些人来说，有很多概念层面的讨论：这会变成什么样？各知识工种会被这项技术怎样变好？后来有几次，论文里预言的理论收益开始感觉很具体，你会觉得：想做有用的 AI 工作，不一定非要读博；好像现在就能造一整套真正有用的系统。第一个时刻我们提过一点：玩 Copilot 早期 beta，很神奇。

[(00:06:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=411) I think that the next big moment where everything kind of clicked together was actually getting early access to GPT-IV. So it was sort of end of 2022 was when we were tinkering with that model and the step-upping capabilities felt enormous. And previous to that, we had been working on a couple of different projects. Because of Copilot, because of scaling odds, because of our prior interest in the technology, we had been tinkering around with tools for programmers, but things that are very specific. So we were building tools for financial professionals who have to work within a Jupyter Notebook or playing around with can you do static analysis with these models?  
（00:06:51）我觉得下一个「一切串起来」的大时刻，其实是拿到 GPT-4（口误作 IV）的早期访问。大概 2022 年底我们在玩那个模型，能力跃升感觉巨大。在那之前我们做过几个很不同的项目：因为 Copilot、因为 scaling（口误作 odds）、因为对技术早有兴趣，我们一直在试程序员工具，但都很窄——比如给必须在 Jupyter 里干活的金融从业者做工具，或者玩「能不能用这些模型做静态分析」。

[(00:07:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=449) And then the step-up in GPT- IV felt like, look, that really made concrete the theoretical gains that we had predicted before. It felt like you could build a lot more just immediately at that point in time. And also if we were being consistent, it really felt like this wasn’t just going to be a point solution thing. This was going to be all of programming was going to flow through these models and it felt like that demanded a different type of programming environment, a different type of programming. And so we set off to build that sort of larger vision around then.  
（00:07:29）然后 GPT-4 这一跃，让我们之前预言的理论收益变得很具体；当时就觉得可以立刻多造很多东西。而且如果我们要逻辑一致，会觉得这不只是单点工具——编程都会流经这些模型，这就需要不同类型的编程环境、不同类型的编程。于是我们大约从那时出发去构建那种更大的愿景。

Sualeh [(00:07:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=479) There’s one that I distinctly remember. So my roommate is an IMO Gold winner and there’s a competition in the US called the PUTNAM, which is sort of the IMO for college people and it’s this math competition. It’s exceptionally good. So Shengtong and Aman I remember, sort of June of 2022, had this bet on whether the 2024 June or July you were going to win a gold medal in the IMO with models.  
Sualeh（00:07:59）有一件事我印象很深：我室友是 IMO 金牌，美国有个 Putnam 竞赛，有点像大学生版 IMO，数学竞赛，很难。我记得 2022 年 6 月左右，申彤和 Aman 打了个赌：到 2024 年 6 或 7 月，模型能不能在 IMO 拿金牌。

Lex [(00:08:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=511) IMO is the International Math Olympiad.  
Lex（00:08:31）IMO 是国际数学奥林匹克。

Sualeh [(00:08:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=513) Yeah, IMO is International Math Olympiad. And so Arvid and I are both also competing in it. So it was sort of personal and I remember thinking, Matt, this is not going to happen. Even though I sort of believed in progress, I thought IMO Gold, Aman is delusional. And to be honest, I mean, I was, to be clear, very wrong. But that was maybe the most prescient bet in the group.  
Sualeh（00:08:33）对，IMO 是国际数学奥林匹克。Arvid 和我也都参加过，所以有点私人。我当时想：不可能吧。我虽然信进展，但觉得 IMO 金牌、Aman 太妄想。说实话我错了，错得很彻底。但那可能是组里最「先知」的赌。

Lex [(00:09:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=545) So the new results from DeepMind, it turned out that you were correct.  
Lex（00:09:05）所以 DeepMind 的新结果证明你是对的。

Arvid [(00:09:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=551) Technically not.  
Arvid（00:09:11）严格说不是。

Aman [(00:09:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=552) Technically incorrect but one point away.  
Aman（00:09:12）严格说不对，但差一分。

Michael [(00:09:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=555) Aman was very enthusiastic about this stuff back then and before, Aman had this scaling loss T-shirt that he would wear around where it had the charts and the formulas on it.  
Michael（00:09:15）Aman 当时对这些特别狂热；他还有件 scaling loss T 恤，印着曲线和公式到处穿。

Lex [(00:09:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=565) So you felt the AGI or you felt the scaling loss.  
Lex（00:09:25）所以你感受到的是 AGI 还是 scaling loss。

Aman [(00:09:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=568) Yeah, I distinctly remember there was this one conversation I had with Michael before I hadn’t thought super deeply and critically about scaling laws and he kind of posed the question, why isn’t scaling all you need or why isn’t scaling going to result in massive gains in progress? And I think I went through the stages of grief. There is anger, denial, and then finally at the end just thinking about it, acceptance. And I think I’ve been quite hopeful and optimistic about progress since. I think one thing I’ll caveat is I think it also depends on which domains you’re going to see progress. Math is a great domain especially formal theorem proving because you get this fantastic signal of actually verifying if the thing was correct. And so this means something like RL can work really, really well and I think you could have systems that are perhaps very superhuman in math and still not technically have AGI.  
Aman（00:09:28）对，我清楚记得和 Michael 有一次对话，当时我还没很深想 scaling laws，他抛了个问题：为什么「scaling 就是你所需要的一切」不成立，或为什么 scaling 不会带来巨大进展？我觉得我经历了悲伤五阶段：愤怒、否认，最后想通了接受。之后我对进展一直比较乐观。要限定一句：也取决于你在哪些领域看到进展。数学是很好的领域，尤其是形式化定理证明，因为你有强信号能验证对错。所以强化学习（RL）能做得很好；我觉得可以出现数学上远超人类、但技术上还不算 AGI 的系统。

## Cursor  
## Cursor（产品）

Lex [(00:10:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=627) Okay, so can we take it all the way to Cursor. And what is Cursor? It’s a fork of VS Code and VS Code is one of the most popular editors for a long time. Everybody fell in love with it. Everybody left Vim, I left DMAX for it. Sorry. So unified in some fundamental way the developer community. And then you look at the space of things, you look at the scaling laws, AI is becoming amazing and you decided okay, it’s not enough to just write an extension via VS Code because there’s a lot of limitations to that. If AI is going to keep getting better and better and better, we need to really rethink how the AI is going to be part of the editing process. And so you decided to fork VS Code and start to build a lot of the amazing features we’ll be able to talk about. But what was that decision like? Because there’s a lot of extensions, including Copilot, of VS Code that are doing sort of AI type stuff. What was the decision like to just fork VS Code?  
Lex（00:10:27）好，说到 Cursor。Cursor 是什么？它是 VS Code 的分支；VS Code 长期是最流行的编辑器之一，大家都喜欢，大家都离开 Vim——我离开的是 Emacs（口误 DMAX），抱歉——某种意义上统一了开发者社区。你们看到局面、看到 scaling laws、AI 越来越强，于是觉得光写 VS Code 扩展不够，限制很多。若 AI 还会越来越好，就要重新想 AI 如何进入编辑流程。所以你们 fork VS Code，做很多我们待会要聊的厉害功能。但做这个决定是什么感觉？VS Code 上也有很多扩展，包括 Copilot，都在做 AI 类的事。决定直接 fork VS Code 是什么感觉？

Michael [(00:11:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=693) So the decision to do an editor seemed kind of self-evident to us for at least what we wanted to do and achieve because when we started working on the editor, the idea was these models are going to get much better, their capabilities are going to improve and it’s going to entirely change how you build software, both in a you will have big productivity gains but also radical and now the active building software is going to change a lot. And so you’re very limited in the control you have over a code editor if you’re a plugin to an existing coding environment and we didn’t want to get locked in by those limitations. We wanted to be able to just build the most useful stuff.  
Michael（00:11:33）对我们来说，做一款编辑器至少对我们想达成的事几乎是自明的：我们开始做编辑器时，想法是模型会强很多、能力会提升，构建软件的方式会彻底改变——既有巨大生产力，「动手写软件」这件事本身也会大变。如果你是现有环境的插件，对编辑器的控制力很有限，我们不想被这些限制锁死；我们想能造最有用的东西。

Lex [(00:12:08)](https://youtube.com/watch?v=oFfVt3S51T4&t=728) Okay. Well then the natural question is, VS Code is kind of with Copilot a competitor, so how do you win? Is it basically just the speed and the quality of the features?  
Lex（00:12:08）好。自然的问题是：VS Code 加 Copilot 也算竞品，你们怎么赢？基本上就靠速度和功能质量吗？

Aman [(00:12:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=740) Yeah, I mean I think this is a space that is quite interesting, perhaps quite unique where if you look at previous tech waves, maybe there’s kind of one major thing that happened and it unlocked a new wave of companies, but every single year, every single model capability or jump you get in model capabilities, you now unlock this new wave of features, things that are possible, especially in programming. And so I think in AI programming, being even just a few months ahead, let alone a year ahead makes your product much, much, much more useful. I think the Cursor a year from now will need to make the Cursor of today look obsolete. And I think Microsoft has done a number of fantastic things, but I don’t think they’re in a great place to really keep innovating and pushing on this in the way that a startup can.  
Aman（00:12:20）对，我觉得这个领域很有趣，也许很独特：以往技术浪潮可能一个大事就带起一波公司；但这里每一年、模型能力每跳一档，就解锁一波新功能、新可能，尤其在编程里。所以在 AI 编程里，哪怕只领先几个月，别说一年，产品都会有用得多。我觉得一年后的 Cursor 得让今天的 Cursor 显得过时。微软做了很多很棒的事，但我不认为他们像创业公司那样能持续快速创新、把天花板往上推。

Lex [(00:13:13)](https://youtube.com/watch?v=oFfVt3S51T4&t=793) Just rapidly implementing features.  
Lex（00:13:13）就是快速落地功能。

Aman [(00:13:16)](https://youtube.com/watch?v=oFfVt3S51T4&t=796) Yeah. And kind of doing the research experimentation necessary to really push the ceiling.  
Aman（00:13:16）对，还有做研究实验，把天花板真正顶上去。

Sualeh [(00:13:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=804) I don’t know if I think of it in terms of features as I think of it in terms of capabilities for programmers. As the new O1 model came out, and I’m sure there are going to be more models of different types, like longer context and maybe faster, there’s all these crazy ideas that you can try and hopefully 10% of the crazy ideas will make it into something kind of cool and useful and we want people to have that sooner. To rephrase, an underrated fact is we’re making it for ourself.  
Sualeh（00:13:24）我不一定用「功能」想，我更想「给程序员的能力」。新 o1 出来了，肯定还有更多不同类型模型——更长上下文、也许更快——有一堆疯狂想法可试，希望 10% 能变成又酷又有用的东西，我们希望用户更早拿到。换句话说，一个被低估的事实是：我们是给自己做的。

[(00:13:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=839) When we started Cursor, you really felt this frustration that models… You could see models getting better, but the Copilot experience had not changed. It was like, man, these guys, the ceiling is getting higher, why are they not making new things? They should be making new things. Where’s all the alpha features? There were no alpha features. I’m sure it was selling well. I’m sure it was a great business, but it didn’t feel… I’m one of these people that really want to try and use new things and there was no new thing for a very long while.  
（00:13:59）我们刚开始做 Cursor 时，真的很沮丧：模型明明在变好，Copilot 体验却几乎没变。就像：喂，天花板在升高，他们怎么不做新东西？该做新东西啊。alpha 功能呢？根本没有。肯定卖得好、生意好，但感觉……我是那种很想试新东西的人，却很久都没有新东西。

Lex [(00:14:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=875) Yeah, it’s interesting. I don’t know how you put that into words, but when you compare a Cursor with Copilot, Copilot pretty quickly started to feel stale for some reason.  
Lex（00:14:35）有意思。说不清怎么形容，但把 Cursor 和 Copilot 比，Copilot 不知为何很快就显得陈旧。

Arvid [(00:14:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=885) Yeah, I think one thing that I think helps us is that we’re sort of doing it all in one where we’re developing the UX and the way you interact with the model at the same time as we’re developing how we actually make the model give better answers. So how you build up the prompt or how do you find the context and for a Cursor Tab, how do you train the model? So I think that helps us to have all of it the same people working on the entire experience [inaudible 00:15:17] .  
Arvid（00:14:45）对，我觉得一点帮助是我们「一体化」：一边做交互、你和模型的互动方式，一边做怎么让模型给出更好的答案——怎么组 prompt、怎么找上下文、Cursor Tab 怎么训练模型。所以同一批人做整条体验……（听不清）

Sualeh [(00:15:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=917) Yeah, it’s like the person making the UI and the person training the model sit like 18 feet away-  
Sualeh（00:15:17）对，就像做 UI 的和训模型的人坐在十八英尺外——

Aman [(00:15:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=924) Often the same person even.  
Aman（00:15:24）经常是同一个人。

Sualeh [(00:15:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=925) Yeah, often even the same person. You can create things that are sort of not possible if you’re not talking, you’re not experimenting.  
Sualeh（00:15:25）对，经常同一个人。不沟通、不实验，就造不出这种东西。

Lex [(00:15:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=934) And you’re using, like you said, Cursor to write Cursor?  
Lex（00:15:34）而且像你说的，用 Cursor 写 Cursor？

Arvid [(00:15:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=937) Of course.  
Arvid（00:15:37）当然。

Michael [(00:15:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=937) Oh yeah.  
Michael（00:15:37）对。

Lex [(00:15:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=938) Well let’s talk about some of these features. Let’s talk about the all-knowing the all-powerful praise be to the Tab, auto complete on steroids basically. So how does Tab work? What is Tab?  
Lex（00:15:38）聊聊这些功能。说说全知全能、赞美 Tab——基本是类固醇版自动补全。Tab 怎么工作？是什么？

Michael [(00:15:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=953) To highlight and summarize at a high level, I’d say that there are two things that Cursor is pretty good at right now. There are other things that it does, but two things that it helps programmers with. One is this idea of looking over your shoulder and being a really fast colleague who can kind of jump ahead of you and type and figure out what you’re going to do next. And that was the original idea behind… That was kind of the kernel of the idea behind a good auto complete was predicting what you’re going to do next, but you can make that concept even more ambitious by not just predicting the characters after your Cursor but actually predicting the next entire change you’re going to make, the next diff, next place you’re going to jump to.  
Michael（00:15:53）高层概括，我觉得 Cursor 现在很擅长两件事（它还做别的）。一是「站在你身后」：像很快的同事，能跑到你前面打字、猜你下一步。好自动补全的核心本是预测下一步；但可以把野心再放大——不只预测光标后的字符，而是预测你下一个完整改动、下一个 diff、下一个跳转位置。

[(00:16:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=995) And the second thing Cursor is pretty good at right now too is helping you sometimes jump ahead of the AI and tell it what to do and go from instructions to code. And on both of those we’ve done a lot of work on making the editing experience for those things ergonomic and also making those things smart and fast.  
（00:16:35）二是有时帮你跑到 AI 前面，告诉它做什么，从指令到代码。这两块我们都做了很多，让编辑体验顺手，也让它们聪明、快。

## Cursor Tab  
## Cursor Tab

Sualeh [(00:16:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=1014) One of the things we really wanted was we wanted the model to be able to edit code for us. That was kind of a wish and we had multiple attempts at it before we had a good model that could edit code for you. Then after we had a good model, I think there’ve been a lot of effort to make the inference fast for having a good experience, and we’ve been starting to incorporate… I mean, Michael sort of mentioned this ability to jump to different places and that jump to different places I think came from a feeling of once you accept an edit, it’s like man, it should be just really obvious where to go next. It’s like I’d made this change, the model should just know that the next place to go to is 18 lines down. If you’re a WIM user, you could press 18JJ or whatever, but why am I doing this? The model should just know it.  
Sualeh（00:16:54）我们很想要的一件事是让模型能替我们改代码。这是愿望，在有好模型之前试过很多次。有了好模型之后，推理要快、体验才好，我们也开始融入……Michael 提过「跳到不同位置」——我觉得来自一种感觉：你接受一处修改后，下一步该去哪应该显而易见。我改完了，模型就该知道下一步在往下 18 行。如果你是 Vim 用户会按 18jj，但为什么要我按？模型就该知道。

[(00:17:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=1074) So the idea was you just press Tab, it would go 18 lines down and then show you the next edit and you would press Tab, so as long as you could keep pressing Tab. And so the internal competition was, how many Tabs can we make someone press? Once you have the idea, more abstractly, the thing to think about is how are the edits zero entropy? So once you’ve expressed your intent and the edit is… There’s no new bits of information to finish your thought, but you still have to type some characters to make the computer understand what you’re actually thinking, then maybe the model should just sort of read your mind and all the zero entropy bits should just be like tabbed away. That was sort of the abstract version.  
（00:17:54）想法就是你按 Tab，跳到 18 行下，显示下一处编辑，再 Tab……能一直 Tab 下去。内部比赛是：能让人按多少次 Tab？更抽象地想：哪些编辑是「零熵」？意图已经表达完、完成想法没有新信息比特了，但你还要敲字让电脑懂，那也许模型该读心，零熵的部分都 Tab 掉。这是抽象版。

Aman [(00:18:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=1122) There’s this interesting thing where if you look at language model loss on different domains, I believe the bits per byte, which is a kind of character normalize loss for code is lower than language, which means in general there are a lot of tokens in code that are super predictable, a lot of characters that are super predictable. And this is I think even magnified when you’re not just trying to auto complete code, but predicting what the user’s going to do next in their editing of existing code. And so the goal of Cursor Tab is let’s eliminate all the low entropy actions you take inside of the editor. When the intent is effectively determined, let’s just jump you forward in time, skip you forward.  
Aman（00:18:42）有个有趣现象：看不同领域的语言模型损失，代码的 bits per byte（一种按字符归一化的损失）比自然语言低，说明代码里很多 token、字符高度可预测。若不只补全新代码，还预测用户编辑现有代码时的下一步，这种效应更强。所以 Cursor Tab 的目标是：干掉编辑器里所有低熵动作。意图基本定了，就让你在时间里往前跳。

Lex [(00:19:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=1162) Well, what’s the intuition and what’s the technical details of how to do next Cursor prediction? That jump, that’s not so intuitive I think to people.  
Lex（00:19:22）那「下一处光标预测」的直觉和技术细节是什么？这个跳转对很多人来说不直观。

Aman [(00:19:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=1171) Yeah. I think I can speak to a few of the details on how to make these things work. They’re incredibly low latency, so you need to train small models on this task. In particular, they’re incredibly pre-fill token hungry. What that means is they have these really, really long prompts where they see a lot of your code and they’re not actually generating that many tokens. And so the perfect fit for that is using a sparse model, meaning an MOE model. So that was one breakthrough we made that substantially improved its performance at longer context. The other being a variant of speculative decoding that we built out called speculative edits. These are two, I think, important pieces of what make it quite high quality and very fast.  
Aman（00:19:31）可以说几条让这东西工作的细节。延迟要极低，所以要训小模型专做这任务。它们特别「吃」预填充 token：prompt 很长、看了很多代码，真正生成的 token 不多。这很适合稀疏模型，也就是 MOE（混合专家）。这是我们的一项突破，显著提升了长上下文表现。另一块是我们做的 speculative decoding 变体，叫 speculative edits（推测式编辑）。我觉得这两块是高质量和很快的关键。

Lex [(00:20:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=1220) Okay, so MOE [inaudible 00:20:22], the input is huge, the output is small.  
Lex（00:20:20）好，所以 MOE……（听不清）输入巨大、输出小。

Aman [(00:20:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=1224) Yeah.  
Aman（00:20:24）对。

Lex [(00:20:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=1225) Okay. So what else can you say about how to make… Does caching play a role-  
Lex（00:20:25）好。还有什么？缓存重要吗——

Aman [(00:20:30)](https://youtube.com/watch?v=oFfVt3S51T4&t=1230) Oh, caching plays a huge role. Because you’re dealing with this many input tokens, if every single keystroke that you’re typing in a given line you had to rerun the model on all of those tokens passed in, you’re just going to one, significantly degrade latency, two, you’re going to kill your GPUs with load. So you need to design the actual prompts you use for the model such that they’re caching aware. And then yeah, you need to reuse the KV cache across requests just so that you’re spending less work, less compute.  
Aman（00:20:30）缓存作用巨大。输入 token 这么多，若每敲一键都要对全部输入重跑模型，会严重拖慢延迟，也会把 GPU 压垮。所以 prompt 设计要「缓存友好」。还要跨请求复用 KV 缓存，少算、少耗算力。

Lex [(00:21:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=1264) Again, what are the things that Tab is supposed to be able to do in the near term, just to linger on that? Generate code, fill empty space, also edit code across multiple lines and then jump to different locations inside the same file and then-  
Lex（00:21:04）再说近景：Tab 近期要能做什么？生成代码、填空、跨多行编辑、同文件内跳到不同位置，然后——

Sualeh [(00:21:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=1285) Hopefully jump to different files also. So if you make an edit in one file and maybe you have to go to another file to finish your thought, it should go to the second file also.  
Sualeh（00:21:25）希望也能跳到不同文件。你在一个文件改完，要完成想法得去另一个文件，它也该能去第二个文件。

Arvid [(00:21:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=1296) The full generalization is next action prediction. Sometimes you need to run a command in the terminal and it should be able to suggest the command based on the code that you wrote too, or sometimes you actually need to… It suggests something, but it’s hard for you to know if it’s correct because you actually need some more information to learn. You need to know the type to be able to verify that it’s correct. And so maybe it should actually take you to a place that’s the definition of something and then take you back so that you have all the requisite knowledge to be able to accept the next completion.  
Arvid（00:21:36）完全推广是「下一动作预测」。有时要在终端跑命令，它应能根据你写的代码建议命令；有时它给了建议，你难判断对错，因为你还需要更多信息——比如要知道类型才能验证。也许它该先带你去定义处再带回来，让你有足够信息接受下一处补全。

Lex [(00:22:13)](https://youtube.com/watch?v=oFfVt3S51T4&t=1333) So providing the human the knowledge.  
Lex（00:22:13）所以是给人类补知识。

Arvid [(00:22:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=1335) Yes.  
Arvid（00:22:15）对。

Lex [(00:22:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=1337) Right.  
Lex（00:22:17）嗯。

Arvid [(00:22:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=1337) Yeah.  
Arvid（00:22:17）对。

Lex [(00:22:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=1339) I just gotten to know a guy named Primeagen who I believe has an… You can order coffee via SSH.  
Lex（00:22:19）我刚认识一个叫 Primeagen 的人，好像有……可以用 SSH 点咖啡。

Aman [(00:22:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=1348) Oh yeah.  
Aman（00:22:28）对。

Arvid [(00:22:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=1349) We did that.  
Arvid（00:22:29）我们做过。

Sualeh [(00:22:30)](https://youtube.com/watch?v=oFfVt3S51T4&t=1350) We did that.  
Sualeh（00:22:30）我们做过。

Lex [(00:22:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=1351) So can also the model do that and provide you with caffeine? Okay. So that’s the general framework.  
Lex（00:22:31）那模型也能这样给你咖啡因？好，这是大框架。

Michael [(00:22:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=1359) Yeah. And the magic moment would be if… Programming is this weird discipline where sometimes the next five minutes, not always, but sometimes the next five minutes of what you’re going to do is actually predictable from the stuff you’ve done recently. And so can you get to a world where that next five minutes either happens by you disengaging and it taking you through? Or maybe a little bit more of just you seeing next step what it’s going to do and you’re like, okay, that’s good, that’s good, that’s good, that’s good, and you can just sort of tap, tap through these big changes.  
Michael（00:22:39）对。魔法时刻是：编程这学科很怪，有时（不总是）你接下来五分钟要做的事，从你刚做的事就能预测。能不能到一个世界：这五分钟要么你放手让它带你走完；要么你多看一步它要做什么，你说好好好，然后一路点点点通过这些大改动。

## Code diff  
## 代码 diff

Lex [(00:23:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=1389) As we’re talking about this, I should mention one of the really cool and noticeable things about Cursor is that there’s this whole diff interface situation going on. So the model suggests with the red and the green of here’s how we’re going to modify the code, and in the chat window you can apply and it shows you the diff and you can accept the diff. So maybe can you speak to whatever direction of that?  
Lex（00:23:09）聊到这里要提一句：Cursor 很酷很明显的一点是整套 diff 界面。模型用红绿提示怎么改代码，聊天里可以应用，显示 diff，你可以接受。能说说你们在这方面的方向吗？

Sualeh [(00:23:32)](https://youtube.com/watch?v=oFfVt3S51T4&t=1412) We’ll probably have four or five different kinds of diffs. So we have optimized the diff for the auto complete, so that has a different diff interface than when you’re reviewing larger blocks of code. And then we’re trying to optimize another diff thing for when you’re doing multiple different files. And at a high level, the difference is for when you’re doing auto- complete, it should be really, really fast to read. Actually it should be really fast to read in all situations, but in auto-complete your eyes are focused in one area, you can’t be in too many… The humans can’t look in too many different places.  
Sualeh（00:23:32）我们可能会有四五种 diff。自动补全场景的 diff 已优化，和大块代码审查的界面不同；还在优化多文件场景的另一种。高层区别是：自动补全时你要读得极快——其实所有情况都要快，但补全时眼睛盯一个区域，人不能同时看太多地方。

Lex [(00:24:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=1455) So you’re talking about on the interface side?  
Lex（00:24:15）所以是界面侧？

Sualeh [(00:24:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=1457) On the interface side. So it currently has this box on this side. So we have the current box, and it you tries to delete code in some place and tries to add other code, it tries to show you a box on the side.  
Sualeh（00:24:17）界面侧。现在这边有个框：当前框里，它要删某处代码、加别处代码，就在侧边用框展示。

Aman [(00:24:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=1468) You can maybe show it if we pull it up in Cursor.com. This is what we’re talking.  
Aman（00:24:28）可以在 Cursor.com 上打开给大家看，我们说的就是那个。

Sualeh [(00:24:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=1473) So that box-  
Sualeh（00:24:33）所以那个框——

Aman [(00:24:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=1473) Exactly here.  
Aman（00:24:33）就这里。

Sualeh [(00:24:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=1475) It was like three or four different attempts at trying to make this thing work where first the attempt was this blue crossed out line. So before it was a box on the side, it used to show you the code to delete by showing you Google Docs style, you would see a line through it and then you would see the new code. That was super distracting. And then we tried many different… There was deletions, there was trying the red highlight.  
Sualeh（00:24:35）试了三四个版本才做成现在这样。最早是蓝色删除线：还不是侧边框时，用 Google 文档那种划掉再显示新代码，特别干扰。后来试了很多：删除线、红色高亮等等。

[(00:25:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=1505) Then the next iteration of it, which is sort of funny, you would hold the, on Mac, the option button. So it would sort of highlight a region of code to show you that there might be something coming. So maybe in this example, the input and the value would all get blue. And the blue was to highlight that the AI had a suggestion for you. So instead of directly showing you the thing, it would just hint that the AI had a suggestion and if you really wanted to see it, you would hold the option button and then you would see the new suggestion. And if you release the option button, you would then see your original code.  
（00:25:05）下一版有点好笑：在 Mac 上按住 option。会先高亮一片代码暗示「可能有建议」。比如 input 和 value 都变蓝，表示 AI 有建议。不直接显示，只暗示；你真要看就按住 option 才看到新建议，松开又回到原代码。

Lex [(00:25:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=1547) So by the way, that’s pretty nice, but you have to know to hold the option button.  
Lex（00:25:47）其实挺不错，但你得知道要按住 option。

Aman [(00:25:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=1551) Yeah.  
Aman（00:25:51）对。

Lex [(00:25:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=1551) And by the way, I’m not a Mac user, but I got it. Option. It’s a button I guess you people have.  
Lex（00:25:51）我不是 Mac 用户但也懂了。Option，你们 Mac 人有的键。

Sualeh [(00:26:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=1560) Again, it’s just not intuitive. I think that’s the key thing.  
Sualeh（00:26:00）还是不直观，我觉得这是关键。

Aman [(00:26:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=1563) And there’s a chance this is also not the final version of it.  
Aman（00:26:03）这也可能不是最终版。

Arvid [(00:26:07)](https://youtube.com/watch?v=oFfVt3S51T4&t=1567) I am personally very excited for making a lot of improvements in this area. We often talk about it as the verification problem where these diffs are great for small edits. For large edits or when it’s multiple files or something, it’s actually a little bit prohibitive to review these diffs. So there are a couple of different ideas here. One idea that we have is, okay, parts of the diffs are important. They have a lot of information. And then parts of the diff are just very low entropy. They’re the same thing over and over again. And so maybe you can highlight the important pieces and then gray out the not so important pieces. Or maybe you can have a model that looks at the diff and sees, oh, there’s a likely bug here. I will mark this with a little red squiggly and say, you should probably review this part of the diff. Ideas in that vein I think are exciting.  
Arvid（00:26:07）我个人很期待这块大量改进。我们常叫「验证问题」：小改动时 diff 很好；大改动或多文件时，审 diff 有点受不了。有几个想法：diff 里有的部分重要、信息量大，有的很低熵、重复。也许高亮重要的、灰掉不重要的。或者让模型看 diff：这里可能有问题，打红波浪线，提示你重点看。这类想法很令人兴奋。

Lex [(00:27:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=1631) Yeah, that’s a really fascinating space of UX design engineering. So you’re basically trying to guide the human programmer through all the things they need to read and nothing more, optimally.  
Lex（00:27:11）这是 UX 与工程里很迷人的空间：本质上是在最优地引导人类程序员只读该读的、不多不少。

Arvid [(00:27:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=1645) And you want an intelligent model to do it. Currently, diff algorithms, they’re just like normal algorithms. There’s no intelligence. There’s intelligence that went into designing the algorithm, but then you don’t care if it’s about this thing or this thing as you want the model to do this.  
Arvid（00:27:25）而且你希望智能模型来做。现在的 diff 算法就是普通算法，没有智能；设计算法时有智能，但它不关心这段还是那段，而你想让模型关心。

Sualeh [(00:27:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=1667) So I think the general question is like, man, these models are going to get much smarter. As the models get much smarter, changes they will be able to propose are much bigger. So as the changes gets bigger and bigger and bigger, the humans have to do more and more and more verification work. It gets more and more and more… You need to help them out. I don’t want to spend all my time reviewing code.  
Sualeh（00:27:47）总问题是：模型会越来越聪明，能提议的改动越来越大，人就要做越来越多验证……得帮人。我不想一辈子都在审代码。

Lex [(00:28:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=1695) Can you say a little more across multiple files [inaudible 00:28:19]?  
Lex（00:28:15）多文件场景能再多说点吗（听不清）？

Aman [(00:28:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=1700) Yeah. I mean, so GitHub tries to solve this with code review. When you’re doing code review, you’re reviewing multiple diffs across multiple files. But like Arvid said earlier, I think you can do much better than code review. Code review kind of sucks. You spend a lot of time trying to grok this code that’s often quite unfamiliar to you and it often doesn’t even actually catch that many bugs. And I think you can significantly improve that review experience using language models, for example, using the kinds of tricks that Arvid had described of maybe pointing you towards the regions that actually matter. I think also if the code is produced by these language models and it’s not produced by someone else… The code review experience is design for both the reviewer and the person that produced the code. In the case where the person that produced the code is a language model, you don’t have to care that much about their experience and you can design the entire thing around the reviewer such that the reviewer’s job is as fun, as easy, as productive as possible. I think that feels like the issue with just naively trying to make these things look like code review. I think you can be a lot more creative and push the boundary on what’s possible.  
Aman（00:28:20）GitHub 用 code review 解决：多文件多个 diff。但像 Arvid 说的，可以比 code review 好得多。code review 挺糟：花很多时间啃你不熟的代码，还抓不到多少 bug。用语言模型能显著改善，比如 Arvid 说的 tricks，把你指向真正重要的区域。而且若代码是模型写的不是人写的——code review 本来要兼顾作者和审查者；若作者是模型，你不太用管作者体验，可以整个围绕审查者设计，让审查者更爽、更轻松、更高效。 naive 地做成传统 code review 就有这个问题。可以更创意、把边界推更远。

Arvid [(00:29:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=1783) And just one idea there is, I think ordering matters. Generally, when you review a PR, you have this list of files and you’re reviewing them from top to bottom, but actually, you actually want to understand this part first because that came logically first, and then you want to understand the next part and you don’t want to have to figure out that yourself, you want a model to.  
Arvid（00:29:43）一个想法是顺序很重要。一般审 PR 按文件列表从上到下，但你其实想先理解逻辑上最先的那块，再下一块；你不想自己琢磨顺序，你想模型带你。

Arvid [(00:30:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=1800) And you don’t want to have to figure out that yourself. You want a model to guide you through the thing.  
Arvid（00:30:00）不想自己琢磨，你想模型引导你走。

Lex [(00:30:06)](https://youtube.com/watch?v=oFfVt3S51T4&t=1806) And is the step of creation going to be more and more natural language, is the goal versus with actual writing the book?  
Lex（00:30:06）创作步骤会越来越靠自然语言吗，相对真的写书那样？

Arvid [(00:30:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=1812) I think sometimes. I don’t think it’s going to be the case that all of programming will be natural language, and the reason for that is if I’m pair programming with Sualeh and Sualeh is at the computer and the keyboard, and sometimes if I’m driving, I want to say to Sualeh, “Hey, implement this function,” and that works. And then sometimes it’s just so annoying to explain to Sualeh what I want him to do, and so I actually take over the keyboard and I show him. I write part of the example and then it makes sense and that’s the easiest way to communicate. And so I think that’s also the case for AI. Sometimes the easiest way to communicate with the AI will be to show an example and then it goes and does the thing everywhere else.  
Arvid（00:30:12）有时会。我不认为编程都会变成自然语言。我和 Sualeh 结对，他在键盘前，有时我开车（主导）会说「实现这个函数」，行。有时解释太烦，我就抢键盘示范，写段例子，他就懂了，这是最容易的沟通。对 AI 也一样：有时最容易的是给例子，它再去别处照做。

[(00:30:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=1854) Or sometimes if you’re making a website for example, the easiest way to show to the AI what you want is not to tell it what to do but drag things around or draw things, and maybe eventually we will get to brain machine interfaces or whatever and you can understand what you’re thinking. And so I think natural language will have a place. I think it will definitely not be the way most people program most of the time.  
（00:30:54）有时做网站，最容易的不是用语言吩咐，而是拖拽、画出来；也许以后还有脑机接口之类。自然语言会有位置，但绝不会是大多数人大多数时候编程的方式。

## ML details  
## 机器学习细节

Lex [(00:31:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=1880) I’m really feeling the AGI with this editor. It feels like there’s a lot of machine learning going on underneath. Tell me about some of the ML stuff that makes it all work?  
Lex（00:31:20）用这编辑器我真有点 AGI 感。底下好像很多机器学习。说说哪些 ML 让它跑起来？

Aman [(00:31:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=1891) Where Cursor really works via this ensemble of custom models that we’ve trained alongside the frontier models that are fantastic at the reasoning intense things. And so Cursor Tab for example, is a great example of where you can specialize this model to be, even better than even frontier models if you look at evals on the task we set it at. The other domain, which it’s surprising that it requires custom models but it’s necessary and works quite well, is in Apply. So I think these models are… The frontier models are quite good at sketching out plans for code and generating rough sketches of the change, but actually, creating diffs is quite hard for frontier models, for your training models. You try to do this with Sonnet, with o1, any frontier model and it really messes up stupid things like counting line numbers, especially in super, super large files. And so what we’ve done to alleviate this is we let the model sketch out this rough code block that indicates what the change will be and we train a model to then Apply that change to the file.  
Aman（00:31:31）Cursor 靠我们训的一组定制模型，加上擅长重推理的前沿模型一起工作。Cursor Tab 就是好例子：在我们设定的任务评测上，专用模型可以比前沿模型还强。另一个需要定制模型、乍看意外但很必要且效果好的是 Apply（应用补丁）。前沿模型擅长勾勒计划、粗粒度改动的草图，但真正生成 diff 很难——用 Sonnet、o1 等前沿模型试，会在数行号这种蠢事上翻车，超大文件尤甚。我们的缓解方式是：让模型先画出表示改动的粗代码块，再训一个模型把改动 Apply 到文件上。

Lex [(00:32:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=1962) And we should say that Apply is the model looks at your code, it gives you a really damn good suggestion of what new things to do. And the seemingly for humans trivial step of combining the two, you’re saying is not so trivial.  
Lex（00:32:42）Apply 就是模型看你的代码，给很强的「要做什么」建议。对人来说把两者合并这步看似平凡，你说并不平凡。

Sualeh [(00:32:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=1979) Contrary to popular perception, it is not a deterministic algorithm.  
Sualeh（00:32:59）与常见想象相反，它不是确定性算法。

Aman [(00:33:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=1983) Yeah, I think you see shallow copies of apply elsewhere and it just breaks most of the time because you think you can try to do some deterministic matching and then it fails at least 40% of the time and that just results in a terrible product experience. I think in general, this regime of you are going to get smarter and smarter models. So one other thing that Apply lets you do is it lets you use fewer tokens with the most intelligent models. This is both expensive in terms of latency for generating all these tokens and cost. So you can give this very, very rough sketch and then have your model models go and implement it because it’s a much easier task to implement this very, very sketched out code. And I think that this regime will continue where you can use smarter and smarter models to do the planning and then maybe the implementation details can be handled by the less intelligent ones. Perhaps you’ll have maybe o1, maybe it’ll be even more capable models given an even higher level plan that is recursively applied by sauna and then the apply model.  
Aman（00:33:03）别处浅拷贝式 apply 多半会崩：你以为确定性匹配就行，至少 40% 失败，体验很糟。模型会越来越聪明。Apply 另一件事是让你用最聪明模型时少生成 token——生成多 token 既拖延迟又贵。所以可以给极粗的草图，再用（别的）模型去实现，实现粗草图是更容易的任务。这种模式会继续：更聪明的模型做规划，细节交给弱一点的模型。也许 o1 或更强的模型给更高层计划，再递归交给 Sonnet（口误 sauna）和 apply 模型。

Sualeh [(00:34:16)](https://youtube.com/watch?v=oFfVt3S51T4&t=2056) Maybe we should talk about how to make it fast if you like. Fast is always an interesting detail.  
Sualeh（00:34:16）也许该聊聊怎么变快。快总是有趣细节。

Arvid [(00:34:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=2061) Fast is good.  
Arvid（00:34:21）快就是好。

Lex [(00:34:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=2062) Yeah, how do you make it fast?  
Lex（00:34:22）怎么快？

Aman [(00:34:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=2065) Yeah, so one big component of making it fast is speculative edits. So speculative edits are a variant of speculative decoding, and maybe it’d be helpful to briefly describe speculative decoding. With speculative decoding, what you do is you can take advantage of the fact that most of the time, and I’ll add the caveat that it would be when you’re memory bound in language model generation, if you process multiple tokens at once, it is faster than generating one token at a time. So this is the same reason why if you look at tokens per second with prompt tokens versus generated tokens, it’s much much faster for prompt tokens.  
Aman（00:34:25）一大块是 speculative edits（推测式编辑）。它是 speculative decoding（推测解码）的变体。简述推测解码：多数时候——补充一句，在生成受内存带宽限制时——一次处理多个 token 比一个一个生成更快。所以你看每秒 token 数，prompt token 比生成 token 快得多。

[(00:35:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=2109) So what we do is instead of using what speculative decoding normally does, which is using a really small model to predict these draft tokens that your larger model will then go in and verify, with code edits, we have a very strong prior of what the existing code will look like and that prior is literally the same exact code. So you can do is you can just feed chunks of the original code back into the model, and then the model will just pretty much agree most of the time that, “Okay, I’m just going to spit this code back out.” And so you can process all of those lines in parallel and you just do this with sufficiently many chunks. And then eventually you’ll reach a point of disagreement where the model will now predict text that is different from the ground truth original code. It’ll generate those tokens and then we will decide after enough tokens match the original code to re- start speculating in chunks of code.  
（00:35:09）通常推测解码用小模型起草、大模型验证；代码编辑里我们对现有代码有很强的先验——先验就是原代码本身。可以把原代码分块喂回模型，模型大多数时候会同意「原样吐回」。这些行可以并行处理，用足够多的块反复做。最终会到分歧点：模型预测与真实原代码不同，就生成那些 token；原代码匹配足够长后再重新分块推测。

[(00:36:02)](https://youtube.com/watch?v=oFfVt3S51T4&t=2162) What this actually ends up looking like is just a much faster version of normal editing code. So it looks like a much faster version of the model rewriting all the code. So we can use the same exact interface that we use for diffs, but it will just stream down a lot faster.  
（00:36:02）效果就像正常改代码，但快得多；像模型重写全代码的快放。界面和普通 diff 一样，只是流式下来快得多。

Sualeh [(00:36:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=2181) And then the advantage is that while it’s streaming, you can just also start reviewing the code before it’s done so there’s no big loading screen. Maybe that is part of the advantage.  
Sualeh（00:36:21）流式时你可以在没完之前就开始读，没有大加载屏，这也是优势。

Lex [(00:36:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=2196) So the human can start reading before the thing is done.  
Lex（00:36:36）所以人可以在生成完之前开始读。

Sualeh [(00:36:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=2199) I think the interesting riff here is something like… I feel like speculation is a fairly common idea nowadays. It’s not only in language models. There’s obviously speculation in CPUs and there’s speculation for databases and there’s speculation all over the place.  
Sualeh（00:36:39）有趣的延伸是：推测现在很常见，不只语言模型，CPU、数据库，到处都有推测。

## GPT vs Claude  
## GPT 对 Claude

Lex [(00:36:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=2214) Well, let me ask the ridiculous question of which LLM is better at coding? GPT, Claude, who wins in the context of programming? And I’m sure the answer is much more nuanced because it sounds like every single part of this involves a different model.  
Lex（00:36:54）问个「傻问题」：哪个大模型写代码更强？GPT、Claude，编程语境谁赢？答案肯定更细，因为你们产品里不同环节像是不同模型。

Aman [(00:37:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=2232) I think there’s no model that Pareto dominates others, meaning it is better in all categories that we think matter, the categories being speed, ability to edit code, ability to process lots of code, long context, a couple of other things and coding capabilities. The one that I’d say right now is just net best is Sonnet. I think this is a consensus opinion. o1’s really interesting and it’s really good at reasoning. So if you give it really hard programming interview style problems or lead code problems, it can do quite well on them, but it doesn’t feel like it understands your rough intent as well as Sonnet does. If you look at a lot of the other frontier models, one qualm I have is it feels like they’re not necessarily over… I’m not saying they train on benchmarks, but they perform really well in benchmarks relative to everything that’s in the middle. So if you tried on all these benchmarks and things that are in the distribution of the benchmarks they’re evaluated on, they’ll do really well. But when you push them a little bit outside of that, Sonnet is I think the one that does best at maintaining that same capability. You have the same capability in the benchmark as when you try to instruct it to do anything with coding.  
Aman（00:37:12）没有模型能在我们在意的维度上全面帕累托碾压别人：速度、改代码能力、处理大量代码、长上下文、还有编程能力等。我现在会说综合最好的是 Sonnet（Anthropic），这应该是共识。o1 很有意思、推理强，给它很难的面试题或 LeetCode 它能做得不错，但粗意图理解不如 Sonnet。很多前沿模型有个我不爽的点：不是说它们训了 benchmark，但它们在 benchmark 分布上表现相对「中间地带」好得离谱；在评测分布里试都很好，稍微推出分布，Sonnet 最能保持同样水平——benchmark 里多强，真让你指挥写代码也多强。

Lex [(00:38:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=2318) Another ridiculous question is the difference between the normal programming experience versus what benchmarks represent? Where do benchmarks fall short, do you think, when we’re evaluating these models?  
Lex（00:38:38）另一个傻问题：真实编程相对 benchmark 代表的东西差在哪？评模型时 benchmark 缺什么？

Sualeh [(00:38:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=2329) By the way, that’s a really, really hard, critically important detail of how different benchmarks are versus real coding, where real coding, it’s not interview style coding. Humans are saying half-broken English sometimes and sometimes you’re saying, “Oh, do what I did before.” Sometimes you’re saying, “Go add this thing and then do this other thing for me and then make this UI element.” And then it’s just a lot of things are context dependent. You really want to understand the human and then do what the human wants, as opposed to this… Maybe the way to put it abstractly is the interview problems are very well specified. They lean a lot on specification while the human stuff is less specified.  
Sualeh（00:38:49）这是很难、但极其关键的一点：benchmark 和真实编程差很多。真实编程不是面试式写题；人有时说半吊子英语，有时说「照我上次那样」，有时说「加这个再做那个再改这个 UI」。很多事依赖上下文。你要懂人再做事。抽象说：面试题规格很满、靠规格；人的东西规格更松。

Michael [(00:39:50)](https://youtube.com/watch?v=oFfVt3S51T4&t=2390) I think that this benchmark question is both complicated by what Sualeh just mentioned, and then also what Aman was getting into is that even if you… There’s this problem of the skew between what can you actually model in a benchmark versus real programming, and that can be sometimes hard to encapsulate because it’s real programming’s very messy and sometimes things aren’t super well specified what’s correct or what isn’t. But then it’s also doubly hard because of this public benchmark problem. And that’s both because public benchmarks are sometimes hill climbed on, then it’s really, really hard to also get the data from the public benchmarks out of the models.  
Michael（00:39:50）benchmark 问题既被 Sualeh 说的复杂化，也被 Aman 说的复杂化：benchmark 能建模的真实编程有多偏，这本身难封装；真实编程很乱，对错有时说不清。更难的是公开 benchmark：可能被爬榜；也很难把公开 benchmark 数据从模型训练里真正清掉。

[(00:40:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=2428) And so for instance, one of the most popular agent benchmarks, SWE-Bench, is really, really contaminated in the training data of these foundation models. And so if you ask these foundation models to do a SWE-Bench problem, but you actually don’t give them the context of a code base, they can hallucinate the right file pass, they can hallucinate the right function names. And so it’s also just the public aspect of these things is tricky.  
（00:40:28）比如最流行的智能体 benchmark 之一 SWE-Bench，在基础模型训练数据里污染很重。你若让模型做 SWE-Bench 题却不给代码库上下文，它能 hallucinate 对的路径、函数名。公开性本身也很棘手。

Aman [(00:40:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=2453) In that case, it could be trained on the literal issues or pull requests themselves, and maybe the labs will start to do a better job or they’ve already done a good job at decontaminating those things, but they’re not going to omit the actual training data of the repository itself. These are all some of the most popular Python repositories. SimPy is one example. I don’t think they’re going to handicap their models on SimPy and all these popular Python repositories in order to get true evaluation scores in these benchmarks.  
Aman（00:40:53）那种情况可能连 issue、PR 原文都进训练了；实验室也许会更好做去污染，或已经做得不错，但他们不会把仓库本体训练数据砍掉——那都是最热门的 Python 仓库之一。比如 SimPy。我不认为他们会为了让 benchmark「真分数」而在 SimPy 这类热门库上自废武功。

Michael [(00:41:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=2484) I think that given the dirts in benchmarks, there have been a few interesting crutches that places that build systems with these models or build these models actually use to get a sense of are they going the the right direction or not. And in a lot of places, people will actually just have humans play with the things and give qualitative feedback on these. One or two of the foundation model companies, they have people who that’s a big part of their role. And internally, we also qualitatively assess these models and actually lean on that a lot in addition to private emails that we have.  
Michael（00:41:24）benchmark 这么脏，做系统或做模型的地方会用些有趣的「拐杖」判断方向对不对。很多地方就是让人玩、给定性反馈。一两家基础模型公司有人专职干这个。我们内部也大量定性评估，还加私有邮件等。

Arvid [(00:41:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=2516) It’s like the vibe.  
Arvid（00:41:56）就像 vibe。

Lex [(00:41:57)](https://youtube.com/watch?v=oFfVt3S51T4&t=2517) The vibe, yeah, the vibe.  
Lex（00:41:57）Vibe，对，vibe。

Arvid [(00:41:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=2519) It’s like the vibe.  
Arvid（00:41:59）就是 vibe。

Lex [(00:42:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=2520) The vibe benchmark, human benchmark, the humans. You pull in the humans to do a vibe check.  
Lex（00:42:00）Vibe 基准、人类基准，人类来做 vibe check。

Arvid [(00:42:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=2525) Yeah.  
Arvid（00:42:05）对。

Lex [(00:42:06)](https://youtube.com/watch?v=oFfVt3S51T4&t=2526) Okay. That’s what I do. Just reading online forums and Reddit and X. Well, I don’t know how to properly load in people’s opinions because they’ll say things like, “I feel like Claude or GPT has gotten dumber,” or something. They’ll say, “I feel like…” And then I sometimes feel like that too, but I wonder if it’s the model’s problem or mine.  
Lex（00:42:06）我就是这样，刷论坛、Reddit、X。不知道怎么正确加载大众意见；有人说「感觉 Claude 或 GPT 变笨了」，「我感觉……」我有时也这样，但不知是模型还是我的问题。

Aman [(00:42:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=2554) With Claude, there’s an interesting take I heard where I think AWS has different chips and I suspect they have slightly different numerics than Nvidia GPUs, and someone speculated that Claude’s degraded performance had to do with maybe using the quantized version that existed on AWS Bedrock versus whatever was running on Anthropics GPUs.  
Aman（00:42:34）Claude 有个有趣说法：AWS 芯片不同，数值和 Nvidia GPU 可能略有不同；有人猜 Claude 表现变差也许和 Bedrock 上量化版、对比 Anthropic 自己 GPU 上跑的有关。

Lex [(00:43:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=2580) I interview a bunch of people that have conspiracy theories. I’m glad you spoke to this conspiracy.  
Lex（00:43:00）我采访过很多阴谋论爱好者。很高兴你们也谈这个「阴谋」。

Sualeh [(00:43:06)](https://youtube.com/watch?v=oFfVt3S51T4&t=2586) Well, it’s not like conspiracy theory as much as humans. Humans are humans and there’s these details-  
Sualeh（00:43:06）不完全是阴谋论，更是人。人就是人，有这些细节——

Lex [(00:43:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=2594) Yes.  
Lex（00:43:14）对。

Sualeh [(00:43:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=2594) And you’re doing this queasy amount of flops and chips are messy and man, you can just have bugs. It’s hard to overstate how hard bugs are to avoid.  
Sualeh（00:43:14）你在跑海量 flops，芯片很乱，就是会有 bug。bug 有多难避免怎么说都不过分。

## Prompt engineering  
## 提示工程

Lex [(00:43:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=2608) What’s the role of a good prompt in all of this? We mentioned that benchmarks have really structured, well-formulated prompts. What should a human be doing to maximize success and what’s the importance of what the humans… You wrote a blog post on… You called it Prompt Design.  
Lex（00:43:28）好 prompt 在这里起什么作用？benchmark 的 prompt 很结构化。人该怎么做才能最大化成功？你们写了篇博客叫 Prompt Design。

Arvid [(00:43:50)](https://youtube.com/watch?v=oFfVt3S51T4&t=2630) Yeah, I think it depends on which model you’re using, and all of them are slightly different and they respond differently to different prompts, but I think the original GPT-4 and the original [inaudible 00:44:07] models last year, they were quite sensitive to the prompts, and they also had a very small context window. And so we have all of these pieces of information around the code base that would maybe be relevant in the prompt. You have the docs, you have the files that you add, you have the conversation history, and then there’s a problem like how do you decide what you actually put in the prompt and when you have a limited space? And even for today’s models, even when you have long context, filling out the entire context window means that it’s slower. It means that sometimes the model actually gets confused and some models get more confused than others.  
Arvid（00:43:50）取决于用哪个模型；模型略有不同、对 prompt 反应不同。去年原版 GPT-4 等（听不清）对 prompt 很敏感，上下文也很小。代码库周围很多信息可能相关：文档、你加的文件、对话历史。问题是怎么在有限空间里决定放什么？即使今天有长上下文，塞满窗口也会更慢，有时模型会困惑，有的模型更容易困惑。

[(00:44:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=2683) And we have this one system internally that we call Preempt, which helps us with that a little bit. And I think it was built for the era before where we had 8,000 token contact windows. And it’s a little bit similar to when you’re making a website. You want it to work on mobile, you want it to work on a desktop screen, and you have this dynamic information which you don’t have. For example, if you’re designing a print magazine, you know exactly where you can put stuff. But when you have a website or when you have a prompt, you have these inputs and then you need to format them to always work, even if the input is really big, then you might have to cut something down. And so the idea was, okay, let’s take some inspiration. What’s the best way to design websites? Well, the thing that we really like is React and the declarative approach where you use JSX in JavaScript, and then you declare, “This is what I want and I think this has higher priority or this has higher Z index than something else.”  
（00:44:43）我们内部有个系统叫 Preempt（口误或拼写），帮处理这一点。它像是 8000 token 上下文时代建的（contact 应为 context）。有点像做网站：要适配手机、桌面，信息是动态的；印杂志你知道往哪摆，网站或 prompt 有输入，要格式化成总能用，输入很大时可能要裁。想法是借鉴网页：我们喜欢 React 声明式，用 JSX，声明「我要什么、谁优先级更高、z-index 谁在上」。

[(00:45:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=2756) And then you have this rendering engine in web design. It’s like Chrome, and in our case it’s a preempt renderer, which then fits everything onto the page. And as you declare, decide what you want and then it figures out what you want. And so we have found that to be quite helpful and I think the role of it has shifted over time where initially it was to fit to these small context windows. Now it’s really useful because it helps us with splitting up the data that goes into the prompt and the actual rendering of it. And so it’s easier to debug because you can change the rendering of the prompt and then try it on old prompts because you have the raw data that went into the prompt, and then you can see, “Did my change actually improve it for this entire eval set?”  
（00:45:56）网页里有渲染引擎，像 Chrome；我们这边是 preempt renderer，把东西排进页面。你声明意图，它帮你落地。我们发现很有用；角色随时间变了：最初是 fit 小窗口；现在更有用，因为把「进 prompt 的数据」和「渲染」拆开，更容易 debug——改渲染再在旧 prompt 上试，你有原始数据，能看「这次改动是否提升整组 eval」。

Lex [(00:46:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=2805) So do you literally prompt with JSX?  
Lex（00:46:45）你们真用 JSX 写 prompt？

Aman [(00:46:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=2808) Yes. Yes.  
Aman（00:46:48）对，对。

Arvid [(00:46:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=2808) Yeah. So it looks like react. There are components. We have one component that’s a file component and it takes in the cursor. Usually there’s one line where the cursor is in your file and that’s probably the most important line because that’s the one you’re looking at. And so then you can give priorities. So that line has the highest priority, and then you subtract one for every line that is farther away. And then eventually when it’s rendered, it figures out how many lines can actually fit and it centers around that thing.  
Arvid（00:46:48）对，像 React。有组件。有个文件组件接收光标位置。光标所在行通常最重要，因为你在看。可以给优先级：那行最高，越远每行减一。渲染时再算能装多少行、围绕光标居中。

Lex [(00:47:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=2837) That’s amazing.  
Lex（00:47:17）太猛了。

Aman [(00:47:18)](https://youtube.com/watch?v=oFfVt3S51T4&t=2838) And you can do other fancy things where if you have lots of code blocks from the entire code base, you could use retrieval and things like embedding and re-ranking scores to add priorities for you through these components.  
Aman（00:47:18）还可以玩花活：若有很多代码块来自全库，可用检索、embedding、重排分数给这些组件加优先级。

Lex [(00:47:30)](https://youtube.com/watch?v=oFfVt3S51T4&t=2850) So should humans when they ask questions, also try to use something like that? Would it be beneficial to write JSX in the problem or the whole idea is this should be loose and messy?  
Lex（00:47:30）那人提问时也该用类似东西吗？在问题里写 JSX 有用吗？还是就该松散随意？

Arvid [(00:47:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=2863) I think our goal is that you should just do whatever is the most natural thing for you, and then our job is to figure out how do we actually retrieve the relative event things so that your thinking actually makes sense?  
Arvid（00:47:43）我们的目标是：你做最自然的事，我们的工作是想怎么检索到相关东西，让你的想法对上。

Lex [(00:47:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=2876) Well, this is the discussion I had with Aravind of Perplexity is his whole idea is you should let the person be as lazy as he wants. That’s a beautiful thing, but I feel like you’re allowed to ask more of programmers, right?  
Lex（00:47:56）我和 Perplexity 的 Aravind 聊过，他的理念是让人能多懒就多懒，很美；但我觉得程序员可以多要求一点，对吧？

Arvid [(00:48:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=2894) Yes.  
Arvid（00:48:14）对。

Lex [(00:48:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=2894) So if you say, “Just do what you want,” humans are lazy. There’s a tension between just being lazy versus provide more as be prompted… Almost like the system pressuring you or inspiring you to be articulate. Not in terms of the grammar of the sentences, but in terms of the depth of thoughts that you convey inside the prompts.  
Lex（00:48:14）若说「随便你」，人会很懒。懒与多提供信息之间有张力……像系统推你或激励你把 prompt 里想表达的深度说清楚，不是语法，而是思想深度。

Aman [(00:48:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=2919) I think even as a system gets closer to some level of perfection, often when you ask the model for something, not enough intent is conveyed to know what to do. And there are a few ways to resolve that intent. One is the simple thing of having the model just ask you, “I’m not sure how to do these parts based on your query. Could you clarify that?” I think the other could be maybe if there are five or six possible generations, “Given the uncertainty present in your query so far, why don’t we just actually show you all of those and let you pick them?”  
Aman（00:48:39）即使系统接近某种完美，你问模型时意图仍常不够清晰。几种解法：一是模型反问「我不确定这几部分，能澄清吗？」二是若可能有五六种生成，「基于你目前的不确定性，不如全列出来让你选？」

Lex [(00:49:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=2959) How hard is it for the model to choose to talk back versus generally… It’s hard, how deal with the uncertainty. Do I choose to ask for more information to reduce the ambiguity?  
Lex（00:49:19）模型多难在「回问」和一般生成之间选？不确定时怎么处理？该追问减歧义吗？

Sualeh [(00:49:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=2976) So one of the things we do, it’s like a recent addition, is try to suggest files that you can add. And while you’re typing, one can guess what the uncertainty is and maybe suggest that maybe you’re writing your API and we can guess using the commits that you’ve made previously in the same file that the client and the server is super useful and there’s a hard technical problem of how do you resolve it across all commits? Which files are the most important given your current prompt? And we’re still initial version is ruled out and I’m sure we can make it much more accurate. It’s very experimental, but then the idea is we show you, do you just want to add this file, this file, this file also to tell the model to edit those files for you?  
Sualeh（00:49:36）我们最近加的一件事是建议可添加的文件。你打字时可以猜不确定性：也许你在写 API，用同文件历史 commit 猜 client/server 很有用；跨 commit 解析哪块最难，当前 prompt 下哪些文件最重要——还在早期版本，肯定能更准。很实验，但想法是：要不要加这些文件让模型一起改？

[(00:50:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=3037) Because if maybe you’re making the API, you should also edit the client and the server that is using the API and the other one resolving the API. So that would be cool as both there’s the phase where you’re writing a prompt and there’s… Before you even click, “Enter,” maybe we can help resolve some of the uncertainty.  
（00:50:37）因为你在做 API，可能 client、服务端、解析 API 的另一端都要改。酷的是：写 prompt 的阶段、甚至你还没按 Enter，也许就能帮解一点不确定性。

## AI agents  
## AI 智能体

Lex [(00:50:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=3054) To what degree do you use agentic approaches? How useful are agents?  
Lex（00:50:54）你们在多大程度上用 agent 路线？agent 有用吗？

Arvid [(00:50:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=3059) We think agents are really, really cool.  
Arvid（00:50:59）我们觉得 agent 很酷。

Lex [(00:50:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=3059) Okay.  
Lex（00:50:59）好。

Arvid [(00:51:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=3063) I think agents, it’s like resembles like a human… You can feel that you’re getting closer to AGI because you see a demo where it acts as a human would and it’s really, really cool. I think agents are not yet super useful for many things. I think we’re getting close to where they will actually be useful. And so I think there are certain types of tasks where having an agent would be really nice. I would love to have an agent. For example, if we have a bug where you sometimes can’t Command+C and Command+V inside our chat input box, and that’s a task that’s super well specified. I just want to say in two sentences, “This does not work, please fix it.” And then I would love to have an agent that just goes off, does it, and then a day later, I come back and I review the thing.  
Arvid（00:51:03）agent 像 human……看 demo 像人一样行动，你会感觉离 AGI 更近，很酷。但很多事上 agent 还不好用；快接近真正好用了。有些任务很适合 agent。我希望有 agent：比如我们有个 bug，聊天输入框里有时不能 Cmd+C/V，规格很清楚。两句话「不行，修一下」，我希望 agent 自己去跑，一天后我回来审。

Lex [(00:52:02)](https://youtube.com/watch?v=oFfVt3S51T4&t=3122) You mean it goes, finds the right file?  
Lex（00:52:02）就是去找对文件？

Arvid [(00:52:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=3125) Yeah, it finds the right files, it tries to reproduce the bug, it fixes the bug and then it verifies that it’s correct. And this could be a process that takes a long time. And so I think I would love to have that. And then I think a lot of programming, there is often this belief that agents will take over all of programming. I don’t think we think that that’s the case because a lot of programming, a lot of the value is in iterating, or you don’t actually want to specify something upfront because you don’t really know what you want until you have seen an initial version and then you want to iterate on that and then you provide more information.  
Arvid（00:52:05）对，找对文件、复现、修、验证。这过程可能很长。我很想要。但很多人以为 agent 会接管全部编程；我们不这么想。很多编程价值在迭代；你事先不想全定规格，因为看到初版才知道要什么，再迭代、再给信息。

[(00:52:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=3163) And so for a lot of programming, I think you actually want a system that’s instant, that gives you an initial version instantly back and then you can iterate super, super quickly.  
（00:52:43）所以很多编程里你其实要即时系统：马上给初版，再极快迭代。

Lex [(00:52:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=3172) What about something like that recently came out, replica agent, that does also setting up the development environment and solving software packages, configuring everything, configuring the databases and actually deploying the app. Is that also in the set of things you dream about?  
Lex（00:52:52）最近有种 replica agent，搭环境、解依赖、配置、配数据库、部署应用——你们也梦想这种吗？

Arvid [(00:53:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=3189) I think so. I think that would be really cool. For certain types of programming, it would be really cool.  
Arvid（00:53:09）会。很酷。某些编程类型会很酷。

Lex [(00:53:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=3195) Is that within scope of Cursor?  
Lex（00:53:15）在 Cursor 范围内吗？

Arvid [(00:53:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=3197) Yeah, we aren’t actively working on it right now, but it’s definitely… We want to make the programmer’s life easier and more fun and some things are just really tedious and you need to go through a bunch of steps and you want to delegate that to an agent. And then some things you can actually have an agent in the background while you’re working. Let’s say you have a PR that’s both backend and frontend, and you’re working in the frontend and then you can have a background agent that doesn’t work and figure out what you’re doing. And then when you get to the backend part of your PR, then you have some initial piece of code that you can iterate on. And so that would also be really cool.  
Arvid（00:53:17）在。我们没在积极做，但肯定……想让人更轻松好玩；有些事很烦、要很多步，想交给 agent。也可以前台做前端、后台 agent 帮你跑后端——口误「doesn't work」应为 works/works on——你做到 PR 后端部分时已有初稿可迭代。那也很酷。

Lex [(00:53:58)](https://youtube.com/watch?v=oFfVt3S51T4&t=3238) One of the things we already talked about is speed, but I wonder if we can just linger on that some more in the various places that the technical details involved in making this thing really fast. So every single aspect of Cursor, most aspects of Cursor feel really fast. Like I mentioned, the Apply is probably the slowest thing. And for me from… I’m sorry, the pain on Arvid’s face as I say that.  
Lex（00:53:58）我们聊过速度，想再细一点：哪些技术细节让整体很快。Cursor 很多地方感觉很快。我说 Apply 可能最慢——抱歉 Arvid 你表情很痛苦。

Arvid [(00:54:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=3262) I know. It’s a pain. It’s a pain that we’re feeling and we’re working on fixing it.  
Arvid（00:54:22）知道。痛，我们在痛，也在修。

Lex [(00:54:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=3267) Yeah, it says something that feels… I don’t know what it is, like one second or two seconds, that feels slow. That means that actually shows that everything else is just really, really fast. So is there some technical details about how to make some of these models, how to make the chat fast, how to make the diffs fast? Is there something that just jumps to mind?  
Lex（00:54:27）一两秒就觉得慢，说明别的真的很快。让 chat、diff 快，有什么技术细节？

Aman [(00:54:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=3289) Yeah. So we can go over a lot of the strategies that we use. One interesting thing is cache warming. And so what you can do is if as the user’s typing, you can have… You’re probably going to use some piece of context and you can know that before the user’s done typing. So as we discussed before, reusing the KV cache results in lower latency, lower costs, cross requests. So as the user starts typing, you can immediately warm the cache with let’s say the current file contents, and then when they press enter, there’s very few tokens it actually has to pre-fill and compute before starting the generation. This will significantly lower TTFT.  
Aman（00:54:49）可以讲很多策略。一个是 cache warming：用户打字时你可能已知道要用的上下文，不必等打完。复用 KV 缓存降延迟、降成本、跨请求。用户打字时就用当前文件等内容预热缓存，按 Enter 时预填充很少 token 就能开始生成，显著降低 TTFT（首 token 时间）。

Lex [(00:55:30)](https://youtube.com/watch?v=oFfVt3S51T4&t=3330) Can you explain how KV cache works?  
Lex（00:55:30）KV cache 怎么工作？

Aman [(00:55:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=3333) Yeah, so the way transformers work.  
Aman（00:55:33）Transformer 的工作原理。

Lex [(00:55:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=3337) I like it.  
Lex（00:55:37）我喜欢。

Aman [(00:55:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=3341) One of the mechanisms that allow transformers to not just independently… The mechanism that allows transformers to not just independently look at each token, but see previous tokens are the keys and values to attention. And generally, the way attention works is you have at your current token some query, and then you’ve all the keys and values of all your previous tokens, which are some kind of representation that the model stores internally of all the previous tokens in the prompt. And by default, when you’re doing a chat, the model has to, for every single token, do this forward pass through the entire model. That’s a lot of matrix multiplies that happen, and that is really, really slow.  
Aman（00:55:41）Transformer 不只独立看每个 token，还能看前面 token，靠的是注意力的 key 和 value。一般 attention：当前 token 有 query，前面所有 token 有 key/value，是模型内部存的表示。默认聊天时，每个 token 都要整模型前向，很多矩阵乘，很慢。

[(00:56:23)](https://youtube.com/watch?v=oFfVt3S51T4&t=3383) Instead, if you have already done that and you stored the keys and values and you keep that in the GPU, then when I… Let’s say I have to sort it for the last N tokens. If I now want to compute the output token for the N+1nth token, I don’t need to pass those first N tokens through the entire model because I already have all those keys and values. And so you just need to do the forward pass through that last token. And then when you’re doing attention, you’re reusing those keys and values that have been computed, which is the only kind of sequential part or sequentially dependent part of the transformer.  
（00:56:23）若已算过并缓存 key/value 在 GPU，要算第 N+1 个输出 token 时，不必再把前 N 个 token 整段过模型，因为已有 KV。只需对最后一个 token 做前向；attention 时复用已算的 KV，这是 transformer 里唯一序列依赖的部分。

Lex [(00:56:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=3419) Is there higher level caching of caching of the prompts or that kind of stuff that could help?  
Lex（00:56:59）更高层的 prompt 缓存之类有帮助吗？

Aman [(00:57:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=3425) I see. Yeah. There’s other types of caching you can do. One interesting thing that you can do for Cursor Tab is you can basically predict ahead as if the user would’ve accepted the suggestion and then trigger another request. And so then you’ve cached, you’ve done the speculative. It’s a mix of speculation and caching, right? Because speculating what would happen if they accepted it. And then you have this value that is cached this suggestion. And then when they press tab, the next one would be waiting for them immediately. It’s a clever heuristic/trick that uses a higher level caching and can give the… It feels fast despite there not actually being any changes in the model.  
Aman（00:57:05）有。Cursor Tab 可做一件事：假设用户会接受建议，提前预测并再发请求。这是推测+缓存混合：推测接受后的下一步。缓存该建议。用户按 Tab 时下一个已经备好。高层缓存启发式，感觉快，模型本身没变。

Sualeh [(00:57:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=3474) And if you can make the KV cache smaller, one of the advantages you get is like maybe you can speculate even more. Maybe you can guess, “Here’s the 10 things that could be useful, predict the next 10,” and then it’s possible the user hits the one of the 10. It’s much higher chance than the user hits the exact one that you showed them. Maybe they type in other character and hit something else in the cache. So there’s all these tricks where… The general phenomena here is, I think it’s also super useful for RL is maybe a single sample from the model isn’t very good, but if you predict 10 different things, turns out that one of the 10 that’s right is the probability is much higher. There’s these passive K curves and part of RL, what RL does is you can exploit this passive K phenomena to make many different predictions.  
Sualeh（00:57:54）若能把 KV cache 做小，好处之一也许是能更多推测：猜「可能有用的 10 种」，预测接下来 10 个，用户命中其中之一的概率远高于命中你展示的那一个确切结果。也许他多打一个字符就命中缓存里别的。这类技巧里……一般现象是：对 RL 也超有用——模型单次采样可能不好，但若预测 10 种不同东西，往往其中一种对的概率高得多。有所谓 pass@k 类曲线；RL 做的事就是利用这种现象做多路预测。

[(00:58:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=3533) And one way to think about this, the model knows internally has some uncertainty over which of the key things is correct or which of the key things does the human wants? When we RL our Cursor Tab model, one of the things we’re doing is we’re predicting which of the 100 different suggestions the model produces is more amenable for humans? Which of them do humans more like than other things? Maybe there’s something where the model can predict very far ahead versus a little bit, maybe somewhere in the middle. And then you can give a reward to the things that humans would like more and punish the things that it would like, and then train the model to output the suggestions that humans would like more. You have these RL loops that are very useful that exploit these passive K curves. Aman, maybe can go into even more detail.  
（00:58:53）一种理解是：模型内部对「哪个关键点才对」或「人到底想要哪个」有不确定性。我们给 Cursor Tab 模型做 RL 时，在做的事之一是：模型生出 100 条建议里，哪条对人更友好？人更喜欢哪条？也许有的模型能预测很远、有的只近一点、有的居中。然后给人更喜欢的奖励、不喜欢的惩罚，训练模型输出人更喜欢的建议。这些 RL 回路很有用，利用 pass@k 现象。Aman 可以再细讲。

Aman [(00:59:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=3588) Yeah, it is a little different than speed, but technically, you tie it back in because you can get away with the smaller model if you RL your smaller model and it gets the same performance as the bigger one.  
Aman（00:59:48）这和速度略不同，但技术上能串起来：若对小模型做 RL，性能能追上大模型，你就能用小模型凑合。

Aman [(01:00:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=3600)… as the bigger one. So while I was mentioning stuff about KV, about reducing the size of your KV cache, there are other techniques there as well that are really helpful for speed. So kind of back in the day, all the way two years ago, people mainly use multi-head attention, and I think there’s been a migration towards more efficient attention schemes like group query or multi-query attention, and this is really helpful for then with larger batch sizes being able to generate the tokens much faster. The interesting thing here is this now has no effect on that time to first token pre-fill speed. The thing this matters for is now generating tokens. And why is that? Because when you’re generating tokens, instead of being bottlenecked by doing these super parallelizable matrix multiplies across all your tokens, you’re bottlenecked by how quickly… For a long context with large batch sizes, by how quickly you can read those cache, keys, and values.  
Aman（01:00:00）……和大模型一样。所以除了 KV、缩小 KV cache，还有别的提速技巧。大概两年前大家主要用 multi-head attention，现在更多迁到更高效的 group-query（GQA）或 multi-query attention（MQA），大 batch 时生成 token 快很多。有趣的是：这对首 token 预填充时间没影响；影响的是**生成** token。为何？生成时瓶颈不再是跨 token 的高度可并行矩阵乘，而是……长上下文、大 batch 时，读 cache 的 key/value 有多快。

[(01:01:07)](https://youtube.com/watch?v=oFfVt3S51T4&t=3667) And so then that’s memory bandwidth, and how can we make this faster? We can try to compress the size of these keys and values. So multi-query attention is the most aggressive of these. Where normally with multi-head attention, you have some number of, quote, unquote, “attention heads” and some number of query heads. Multi-query just preserves the query heads, gets rid of all the key value heads. So there’s only one kind of key value head, and there’s all the remaining query heads. With group query, you instead preserve all the query heads and then your keys and values are… There are fewer heads for the keys and values, but you’re not reducing it to just one. But anyways, the whole point here is you’re just reducing the size of your KV cache.  
（01:01:07）那就是内存带宽；怎么更快？压缩 key/value 的尺寸。MQA 最激进：多头注意力里通常有若干「注意力头」和 query 头；MQA 保留 query 头、去掉多余的 KV 头，只剩一种 KV 头配所有 query 头。GQA 则是保留全部 query 头，KV 头比 MHA 少但不缩到只剩一个。总之就是缩小 KV cache。

Arvid [(01:02:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=3720) And then there is MLA.  
Arvid（01:02:00）还有 MLA。

Aman [(01:02:02)](https://youtube.com/watch?v=oFfVt3S51T4&t=3722) Yeah, multi-latent. That’s a little more complicated. And the way that this works is it kind of turns the entirety of your keys and values across all your heads into this one latent vector that has then kind of expanded in for its time.  
Aman（01:02:02）对，multi-latent attention，更复杂一点。做法大致是把各头的 key/value 压进一个潜向量，再按时间步展开回去。

Sualeh [(01:02:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=3739) But MLA is from this company called DeepSeek. It’s quite an interesting algorithm. Maybe the key idea is in both MQA and in other places, what you’re doing is you’re reducing the number of KV heads. And the advantage you get from that is there’s less of them, but maybe the theory is that you actually want a lot of different… You want each of the keys and values to actually be different. So one way to reduce the size is you keep one big shared vector for all the keys and values and then you have smaller vectors for every single token. So that you can store the only the smaller thing as some sort of low-rank reduction, and the low-rank reduction, well, that… At the end of the time, when you eventually want to compute the final thing, remember that your memory band, which means that you still have some compute left that you can use for these things. And if you can expand the latent vector back out and somehow this is far more efficient because you’re reducing… For example, maybe you’re reducing vec 32 or something like the size of the vector that you’re keeping.  
Sualeh（01:02:19）MLA 来自 DeepSeek，算法挺有意思。要点是：MQA 等地方都在减少 KV 头数，好处是少，但理论上你又希望各 KV 真有差异。一种折中是：所有 KV 共享一个大向量，每个 token 再配小向量；存盘只存低秩压缩的小块；最后要算 attention 时再展开——内存带宽紧时你仍剩些算力可做展开；若潜向量能高效展开，整体更省，例如把保留向量维数降到 32 量级。

Aman [(01:03:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=3817) Yeah, there’s perhaps some richness in having a separate set of keys and values and query that kind of pairwise match up versus compressing that all into one in that interaction at least.  
Aman（01:03:37）对，分开的 K/V/Q 两两配对也许信息更丰富，至少在那层交互里，比全压成一个更灵活。

Lex [(01:03:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=3831) Okay, and all of that is dealing with being memory bound. I mean, ultimately, how does that map to the user experience? Trying to get the-  
Lex（01:03:51）好，这些都在对付内存带宽瓶颈。最终怎么落到用户体验？想达到——

Aman [(01:04:02)](https://youtube.com/watch?v=oFfVt3S51T4&t=3842) Yeah. The two things that it maps to is you can now make your cache a lot larger because you’ve less space allocated for the KV cache. You can maybe cache a lot more aggressively in a lot more things, so you get more cache hits, which are helpful for reducing the time to first token for the reasons that were kind of described earlier. And then the second being, when you start doing inference with more and more requests and larger and larger batch sizes, you don’t see much of a slowdown as it’s generating the tokens at the speed of that.  
Aman（01:04:02）主要映射两件事：一是 KV 占得少，cache 可以做得更大，更激进缓存更多东西，cache 命中多，有助于降首 token 时间（原因如前）。二是推理请求越来越多、batch 越来越大时，生成 token 的速度不至于明显拖慢。

Sualeh [(01:04:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=3871) Well, it also allows you to make your prompt bigger for certain-  
Sualeh（01:04:31）也让某些场景下 prompt 可以更大——

Aman [(01:04:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=3874) Yeah. Yeah, so the size of your KV cache is both the size of all your prompts multiplied by the number of prompts being processed in parallel. So you could increase either those dimensions, right? The batch size or the size of your prompts without degrading the latency of generating tokens.  
Aman（01:04:34）对。KV cache 总大小≈各 prompt 大小×并行处理的 prompt 数。所以你可以增大 batch 或增大 prompt，而不至于拖累生成 token 的延迟。

## Running code in background  
## 后台运行代码

Lex [(01:04:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=3891) Arvid, you wrote a blog post Shadow Workspace: Iterating on Code in the Background. So what’s going on [inaudible 01:04:59]?  
Lex（01:04:51）Arvid，你写过博客《Shadow Workspace：在后台迭代代码》。具体是怎么回事？[01:04:59 听不清]

Arvid [(01:04:58)](https://youtube.com/watch?v=oFfVt3S51T4&t=3898) So to be clear, we want there to be a lot of stuff happening in the background, and we’re experimenting with a lot of things. Right now, we don’t have much stuff happening other than the cache warming or figuring out the right context that goes into your command key prompts for example. But the idea is if you can actually spend computation in the background, then you can help the user maybe at a slightly longer time horizon than just predicting the next few lines that you’re going to make. But actually in the next 10 minutes, what are you going to make? And by doing it in background, you can spend more computation doing that. And so the idea of the Shadow Workspace that we implemented, and we use it internally for experiments is that to actually get advantage of doing stuff in the background, you want some kind of feedback signal to give back to the model because otherwise you can get higher performance by just letting the model think for longer, and so o1 is a good example of that.  
Arvid（01:04:58）说清楚：我们希望后台很多事在跑，也在试很多。目前除了 cache warming、或帮你凑 Cmd+K 等 prompt 的上下文，后台还没太多。但想法是：若能在后台花算力，就能在比「预测下几行」更长的时间尺度上帮人——比如接下来 10 分钟你会写什么。后台算力可以多花。Shadow Workspace 我们实现了、内部做实验用；要真正从后台计算获益，需要某种反馈信号给模型，否则只靠「让模型想更久」也能涨性能，o1 就是例子。

[(01:06:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=3963) But another way you can improve performance is by letting the model iterate and get feedback. And so one very important piece of feedback when you’re a programmer is the language server, which is this thing, it exists for most different languages, and there’s a separate language server per language. And it can tell you, “You’re using the wrong type here,” and then gives you an error, or it can allow you to go to definition and sort of understands the structure of your code. So language servers are extensions developed by… There is a TypeScript language server developed by the TypeScript people, a Rust language server developed by the Rust people, and then they all interface over the language server protocol to VS Code. So that VS Code doesn’t need to have all of the different languages built into VS Code but rather you can use the existing compiler infrastructure.  
（01:06:03）另一种提性能是让模型迭代拿反馈。程序员很重要的反馈源是语言服务器：多数语言都有，每种语言一个。它能报「这里类型错了」、给跳转定义、理解代码结构。语言服务器由各语言团队写——TS 有 TS 的、Rust 有 Rust 的——通过 LSP 对接 VS Code，这样 VS Code 不必内置所有语言，复用现有编译器基础设施。

Lex [(01:06:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=4012) For linting purposes, what-  
Lex（01:06:52）用于 lint 的话，什么——

Arvid [(01:06:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=4012) It’s for linting. It’s for going to definition and for seeing the right types that you’re using.  
Arvid（01:06:52）lint、跳定义、看你用的类型对不对。

Lex [(01:06:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=4019) So it’s doing type checking also.  
Lex（01:06:59）所以也做类型检查。

Arvid [(01:07:01)](https://youtube.com/watch?v=oFfVt3S51T4&t=4021) Yes, type checking and going to references. And that’s like when you’re working in a big project, you kind of need that. If you don’t have that, it’s really hard to code in a big project.  
Arvid（01:07:01）对，类型检查、找引用。大项目里基本需要；没有会很难写。

Lex [(01:07:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=4032) Can you say, again, how that’s being used inside Cursor, the language server protocol communication thing?  
Lex（01:07:12）再说一遍 Cursor 里怎么用 LSP？

Arvid [(01:07:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=4040) So it’s being used in Cursor to show to the programmer just like in VS Code, but then the idea is you want to show that same information to the models, the IM models, and you want to do that in a way that doesn’t affect the user because you want to do it in background. And so the idea behind the Shadow Workspace was, okay, one way we can do this is we spawn a separate window of Cursor that’s hidden, and so you can set this flag in it and like turn it’s hidden. There is a window but you don’t actually see it. And inside of this window, the AI agents can modify code however they want as long as they don’t save it because it’s still the same folder and then can get feedback from the linters and go to definition and iterate on their code.  
Arvid（01:07:20）Cursor 里像 VS Code 一样给人看；但还要把同样信息给模型（口误 IM 应为 LM），且不影响用户——所以放后台。Shadow Workspace 的想法：起一个隐藏的 Cursor 窗口，设 flag 隐藏，有窗口但你看不见。AI 可在里面随便改代码，只要不保存（仍是同一文件夹），就能从 linter、跳定义拿反馈并迭代。

Lex [(01:08:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=4084) So literally run everything in the background as if… Right, maybe even run the code.  
Lex（01:08:04）就是字面意义后台跑全套……对，也许还能跑代码。

Arvid [(01:08:10)](https://youtube.com/watch?v=oFfVt3S51T4&t=4090) So that’s the eventual version and that’s what you want. And a lot of the blog post is actually about how do you make that happen because it’s a little bit tricky. You want it to be on the user’s machine so that it exactly mirrors the user’s environment. And then on Linux, you can do this cool thing where you can actually mirror the file system and have the AI make changes to the files, and it thinks that it’s operating on the file level, but actually, that’s stored in memory and you can create this kernel-like extension to make it work. Whereas on Mac and Windows, it’s a little bit more difficult, but it’s a fun technical problem, so that’s why.  
Arvid（01:08:10）那是终局版，也是你想要的。博客很多篇幅在讲怎么做到——有点棘手。要在用户机器上跑，才能镜像环境。Linux 上可以镜像文件系统，AI 改文件时它以为在动磁盘，实际在内存里，可做类似内核扩展。Mac/Windows 更难，但是有趣的技术问题。

Aman [(01:08:57)](https://youtube.com/watch?v=oFfVt3S51T4&t=4137) One may be hacky but interesting idea that I like is holding a lock on saving. And so basically, you can then have the language model kind of hold the lock on saving to disk and then instead of you operating in the ground truth version of the files that are saved to disk, you actually are operating what was the Shadow Workspace before and these unsaved things that only exist in memory that you still get linter errors for, and you can code in. And then when you try to maybe run code, it’s just like there’s a small warning that there’s a lock, and then you kind of will take back the lock from the language server if you’re trying to do things concurrently or from the Shadow Workspace if you’re trying to do things concurrently.  
Aman（01:08:57）有个有点 hack 但我很喜欢的想法：给「保存」加锁。模型可以持有写盘锁；于是你操作的不是磁盘上的真值文件，而是 Shadow Workspace 里未保存、只在内存里、但仍能跑 linter 的那份。真要跑代码时会有小提示说被锁了；若与语言服务器或 Shadow Workspace 并发，再收回锁。

## Debugging  
## 调试

Lex [(01:09:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=4171) That’s such an exciting future by the way. It’s a bit of a tangent, but to allow a model to change files, it’s scary for people but it’s really cool, to be able to just let the agent do a set of tasks and you come back the next day and kind of observe like it’s a colleague or something like that.  
Lex（01:09:31）顺便说这未来很令人兴奋。有点跑题：让模型改文件有人害怕，但很酷——让 agent 干一堆活，你第二天回来像看同事一样看结果。

Aman [(01:09:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=4192) And I think there may be different versions of runability where, for the simple things where you’re doing things in the span of a few minutes on behalf of the user as they’re programming, it makes sense to make something work locally in their machine. I think for the more aggressive things where you’re making larger changes that take longer periods of time, you’ll probably want to do this in some sandbox remote environment and that’s another incredibly tricky problem of how do you exactly reproduce or mostly reproduce to the point of it being effectively equivalent for running code the user’s environment with this remote sandbox.  
Aman（01:09:52）可运行性也有不同档位：几分钟内替用户做的事，本地机器跑通合理；更大、更久的改动，可能要在远程沙箱做——这又极难：如何把远端沙箱复现到与用户环境跑代码「实质等价」。

Sualeh [(01:10:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=4227) I’m curious what kind of agents you want for coding? Do you want them to find bugs? Do you want them to implement new features? What agents do you want?  
Sualeh（01:10:27）你理想里编程 agent 要干嘛？找 bug？做新功能？你想要哪种？

Lex [(01:10:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=4236) So by the way, when I think about agents, I don’t think just about coding. I think so for this particular podcast, there’s video editing and a lot of… If you look in Adobe, a lot… There’s code behind. It’s very poorly documented code, but you can interact with Premiere, for example, using code, and basically all the uploading, everything I do on YouTube, everything as you could probably imagine, I do all of that through code and including translation and overdubbing, all of this. So I envision all of those kinds of tasks. So automating many of the tasks that don’t have to do directly with the editing, so that. Okay, that’s what I was thinking about. But in terms of coding, I would be fundamentally thinking about bug finding, many levels of kind of bug finding and also bug finding like logical bugs, not logical like spiritual bugs or something. Ones like big directions of implementation, that kind of stuff.  
Lex（01:10:36）我想到 agent 不只编程。就本期播客：剪辑、Adobe 背后……有代码，文档很差，但可用代码驱动 Premiere 等；我 YouTube 上传、翻译、配音等很多都靠代码自动化。所以我想象的是这类任务。编程方面，我主要想多层级找 bug，包括逻辑 bug（不是玄学 bug），以及实现大方向上的那种问题。

Sualeh [(01:11:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=4298) Magical [inaudible 01:11:39] and bug finding.  
Sualeh（01:11:38）魔法[听不清]和找 bug。

Aman [(01:11:40)](https://youtube.com/watch?v=oFfVt3S51T4&t=4300) Yeah. I mean, it’s really interesting that these models are so bad at bug finding when just naively prompted to find a bug. They’re incredibly poorly calibrated.  
Aman（01:11:40）有意思的是：你朴素地 prompt「找 bug」，模型表现很差，校准度离谱。

Arvid [(01:11:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=4311) Even the smartest models.  
Arvid（01:11:51）再聪明的模型也一样。

Aman [(01:11:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=4312) Exactly, even o1.  
Aman（01:11:52）对，连 o1 也是。

Lex [(01:11:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=4313) How do you explain that? Is there a good intuition?  
Lex（01:11:53）怎么解释？有好直觉吗？

Aman [(01:11:58)](https://youtube.com/watch?v=oFfVt3S51T4&t=4318) I think these models are really strong reflection of the pre-training distribution, and I do think they generalize as the loss gets lower and lower, but I don’t think the loss and the scale is quite… The loss is low enough such that they’re really fully generalizing on code. The things that we use these things for, the frontier models that they’re quite good at, are really code generation and question answering. And these things exist in massive quantities in pre-training with all of the code in GitHub on the scale of many, many trillions of tokens and questions and answers on things like stack overflow and maybe GitHub issues.  
Aman（01:11:58）模型很强地反映预训练分布；loss 越低越会泛化，但我不认为 loss/规模已经低到在代码上**完全**泛化。前沿模型我们真在用的强项主要是代码生成和问答。预训练里 GitHub 海量代码、万亿级 token，Stack Overflow、GitHub issue 式问答也极多。

[(01:12:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=4359) And so when you try to push one of these things that really don’t exist very much online, like for example, the Cursor Tab objective of predicting the next edit given the edits done so far, the brittleness kind of shows. And then bug detection is another great example, where there aren’t really that many examples of actually detecting real bugs and then proposing fixes and the models just kind of really struggle at it. But I think it’s a question of transferring the model in the same way that you get this fantastic transfer from pre-trained models just on code in general to the Cursor Tab objective. You’ll see a very, very similar thing with generalized models that are really good at code to bug detection. It just takes a little bit of kind nudging in that direction.  
（01:12:39）若推网上很少存在的目标——比如 Cursor Tab「给定已做编辑预测下一处编辑」——脆弱性就露出来。bug 检测同理：真实检出 bug 并给修复的样本不多，模型很吃力。但这是迁移问题：从通用代码预训练迁到 Cursor Tab 目标已经很强；好代码模型迁到 bug 检测也会类似，只需朝那方向推一把。

Sualeh [(01:13:25)](https://youtube.com/watch?v=oFfVt3S51T4&t=4405) Look to be clear, I think they sort of understand code really well. While they’re being pre-trained, the representation that’s being built up almost certainly like somewhere in the stream, the model knows that maybe there’s something sketchy going on. It sort of has some sketchiness but actually eliciting the sketchiness to actually… Part of it is that humans are really calibrated on which bugs are really important. It’s not just actually saying there’s something sketchy. It’s like it’s this sketchy trivial, it’s this sketchy like you’re going to take the server down.  
Sualeh（01:13:25）说清楚：我觉得它们懂代码。预训练里表征建起来，流里某处多半知道「有点可疑」；但要把可疑**说出来**……一部分原因是人对「哪些 bug 重要」校准得很好：不只说「可疑」，还要分琐碎可疑和会把服务器搞挂那种。

[(01:14:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=4444) Part of it is maybe the cultural knowledge of why is a staff engineer is good because they know that three years ago someone wrote a really sketchy piece of code that took the server down and as opposed to maybe you just… This thing is an experiment. So a few bugs are fine, you’re just trying to experiment and get the feel of the thing. And so if the model gets really annoying when you’re writing an experiment, that’s really bad, but if you’re writing something for super production, you’re writing a database. You’re writing code in Postgres or Linux or whatever. You’re Linus Torvalds. It’s sort of unacceptable to have even an edge case and just having the calibration of how paranoid is the user and like-  
（01:14:04）还有文化知识：资深工程师强，可能因为三年前有人写过一段很坑的代码把服务器搞挂；对比你只是在实验，几个 bug 无所谓。若你写实验模型很烦人就糟了；若写生产级、数据库、Postgres/Linux 内核那种，连边角 case 都不能随便——要校准用户有多「偏执」、以及——

Aman [(01:14:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=4491) But even then if you’re putting in a maximum paranoia, it still just doesn’t quite get it.  
Aman（01:14:51）但即使你调到最大「偏执」，还是差点意思。

Sualeh [(01:14:57)](https://youtube.com/watch?v=oFfVt3S51T4&t=4497) Yeah, yeah. Yeah.  
Sualeh（01:14:57）对，对。

## Dangerous code  
## 「危险」代码

Lex [(01:14:58)](https://youtube.com/watch?v=oFfVt3S51T4&t=4498) I mean, but this is hard for humans too to understand which line of code is important, which is not. I think one of your principles on a website says if a code can do a lot of damage, one should add a comment that say, “This line of code is dangerous.”  
Lex（01:14:58）人对人也难判断哪行重要哪行不重要。你们网站某条原则说：若代码能造成很大破坏，应加注释写「这行很危险」。

Arvid [(01:15:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=4517) And all caps, repeated 10 times.  
Arvid（01:15:17）全大写，重复十遍。

Lex [(01:15:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=4520) No, you say for every single line of code inside the function you have to… And that’s quite profound, that says something about human beings because the engineers move on, even the same person might just forget how it can sink the Titanic a single function. You might not intuit that quite clearly by looking at the single piece of code.  
Lex（01:15:20）不，是函数里**每一行**都要……这很深刻：人会换岗，同一个人也可能忘了单个函数怎样能弄沉泰坦尼克；单看片段未必直觉到。

Arvid [(01:15:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=4542) Yeah. And I think that one is partially also for today’s AI models where if you actually write dangerous, dangerous, dangerous in every single line, the models will pay more attention to that and will be more likely to find bugs in that region.  
Arvid（01:15:42）对，部分也是给今天的 AI：你真在每行写 dangerous×3，模型会更注意、更可能在那块找 bug。

Lex [(01:16:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=4560) That’s actually just straight up a really good practice of labeling code of how much damages can do.  
Lex（01:16:00）这确实是标注「破坏力」的好实践。

Arvid [(01:16:08)](https://youtube.com/watch?v=oFfVt3S51T4&t=4568) Yeah. I mean, it’s controversial. Some people think it’s ugly. Sualeh does not like it.  
Arvid（01:16:08）有争议。有人嫌丑。Sualeh 不喜欢。

Sualeh [(01:16:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=4574) Well, I think it’s… In fact, I actually think this is one of the things I learned from Arvid is sort of aesthetically I don’t like it, but I think there’s certainly something where it’s useful for the models and humans just forget a lot, and it’s really easy to make a small mistake and cause… Just bring down the server. Of course, we test a lot and whatever, but there’s always these things that you have to be very careful.  
Sualeh（01:16:14）这事……其实我跟 Arvid 学到的一点：审美上我不喜欢，但对模型有用，人又健忘，小错就能……把服务器打挂。当然会测，但总有些事要极度小心。

Aman [(01:16:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=4602) Yeah, like with just normal docstrings, I think people will often just skim it when making a change and think, “Oh, I know how to do this,” and you really need to point it out to them so that doesn’t slip through.  
Aman（01:16:42）普通 docstring 也常被人改代码时一扫而过，觉得「我会」，你得把风险点醒，别漏过去。

Lex [(01:16:55)](https://youtube.com/watch?v=oFfVt3S51T4&t=4615) Yeah. You have to be reminded that you could do a lot of damage that’s like we don’t really think about that. You think about, “Okay, how do I figure out how this works so I can improve it?” You don’t think about the other direction that it could-  
Lex（01:16:55）要提醒自己：你能造成很大破坏，我们平常不这么想。人常想「怎么搞懂好改进」，少想反方向的破坏——

Arvid [(01:17:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=4629) Until we have formal verification for everything, then you can do whatever you want and you know for certain that you have not introduced a bug if the proof pass.  
Arvid（01:17:09）等万物都有形式化验证，你就可以随便改，证明过了就确定没引入 bug。

Aman [(01:17:18)](https://youtube.com/watch?v=oFfVt3S51T4&t=4638) Well, concretely, what do you think that future would look like?  
Aman（01:17:18）具体说你觉得那未来长什么样？

Arvid [(01:17:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=4642) I think people will just not write to tests anymore, and the model will suggest… You write a function, the model will suggest a spec, and you review the spec. And in the meantime, smart reasoning model computes a proof that the implementation follows the spec, and I think that happens for most functions.  
Arvid（01:17:22）人可能不再手写测试；你写函数，模型提议规约（spec），你审规约；同时强推理模型证明实现符合规约——多数函数会这样。

Michael [(01:17:44)](https://youtube.com/watch?v=oFfVt3S51T4&t=4664) Do you think this gets at a little bit some of the stuff you were talking about earlier with the difficulty of specifying intent for what you want with software, where sometimes it might be because the intent is really hard to specify, it’s also then going to be really hard to prove that it’s actually matching whatever your intent is?  
Michael（01:17:44）这是否接上你前面说的：软件意图难写清，若意图难写，是否也难证明实现真符合意图？

Arvid [(01:17:58)](https://youtube.com/watch?v=oFfVt3S51T4&t=4678) You think that spec is hard to generate?  
Arvid（01:17:58）你觉得 spec 难生成？

Michael [(01:18:01)](https://youtube.com/watch?v=oFfVt3S51T4&t=4681) Yeah, or just for a given spec, maybe you can… I think there is a question of, can you actually do the formal verification? Is that possible? I think that there’s more to dig into there, but then also-  
Michael（01:18:01）对，或给定 spec，能否真的做形式化验证？可能还有——

Arvid [(01:18:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=4695) Even if you have the spec?  
Arvid（01:18:15）即便有 spec？

Sualeh [(01:18:16)](https://youtube.com/watch?v=oFfVt3S51T4&t=4696) If you have the spec-  
Sualeh（01:18:16）若有 spec——

Michael [(01:18:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=4699) Even if you have the spec, is the spec written in natural language? Or is it-  
Michael（01:18:19）即便有 spec，是自然语言写的？还是——

Arvid [(01:18:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=4701) No, [inaudible 01:18:21] the spec would be formal.  
Arvid（01:18:21）不，[听不清] spec 应是形式的。

Aman [(01:18:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=4704) But how easier would that be [inaudible 01:18:26]?  
Aman（01:18:24）但那会多容易？[听不清]

Michael [(01:18:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=4707) Okay. So then I think that you care about things that are not going to be easily well specified in the spec language.  
Michael（01:18:27）好。那你关心的是 spec 语言里不好写清的东西。

Arvid [(01:18:30)](https://youtube.com/watch?v=oFfVt3S51T4&t=4710) I see, I see.  
Arvid（01:18:30）明白。

Michael [(01:18:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=4711) Would be maybe an argument against formal verification is all you need.  
Michael（01:18:31）这可能是反对「形式化验证就够」的论点。

Aman [(01:18:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=4716) The worry is there’s this massive document-  
Aman（01:18:36）担心的是巨大文档——

Michael [(01:18:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=4719) [inaudible 01:18:39] replacing something like unit tests, sure.  
Michael（01:18:39）[听不清]取代单元测试之类，可以。

Arvid [(01:18:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=4721) Yeah, yeah. I think you can probably also evolve the spec languages to capture some of the things that they don’t really capture right now. I don’t know. I think it’s very exciting.  
Arvid（01:18:41）对。规约语言大概也能演进，把现在抓不住的抓住。我觉得很兴奋。

Lex [(01:18:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=4734) And you’re speaking not just about single functions, you’re speaking about entire code bases.  
Lex（01:18:54）你不只说单函数，是说整库。

Arvid [(01:19:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=4740) I think entire code bases is harder, but that is what I would love to have and I think it should be possible. And because you can even… There’s a lot of work recently where you can prove formally verified down to the hardware, so through the… You formally verify the C code and then you formally verify through the GCC compiler and then through the Verilog down to the hardware. And that’s incredibly big system, but it actually works. And I think big code bases are sort of similar in that and they’re like multi-layered system. And if you can decompose it and formally verify each part, then I think it should be possible. I think this specification problem is a real problem, but…  
Arvid（01:19:00）整库更难，但我想要且觉得可能。最近有工作一路形式化验证到硬件：C 代码、过 GCC、再到 Verilog 到硬件，系统巨大但可行。大代码库也像多层系统；能分解、逐层验证就应可能。规格问题确实难，但……

Aman [(01:19:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=4779) How do you handle side effects or how do you handle, I guess, external dependencies like calling the Stripe API?  
Aman（01:19:39）副作用呢？外部依赖呢？比如调 Stripe API？

Sualeh [(01:19:46)](https://youtube.com/watch?v=oFfVt3S51T4&t=4786) Maybe Stripe would write a spec for their API.  
Sualeh（01:19:46）也许 Stripe 会给 API 写规约。

Aman [(01:19:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=4789) But you can’t do this for everything. Can you do this for everything you use? How do you do it for… If there’s a language… Maybe people will use language models as primitives in the programs they write, and there’s a dependence on it and how do you now include that?  
Aman（01:19:49）但不能样样如此。若程序里把语言模型当原语依赖，又怎么纳入证明？

Arvid [(01:20:02)](https://youtube.com/watch?v=oFfVt3S51T4&t=4802) I think you might be able to prove that still.  
Arvid（01:20:02）我觉得仍可能证明。

Aman [(01:20:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=4805) Prove what about language models?  
Aman（01:20:05）证明语言模型的什么？

Arvid [(01:20:07)](https://youtube.com/watch?v=oFfVt3S51T4&t=4807) I think it feels possible that you could actually prove that a language model is aligned for example, or you can prove that it actually gives the right answer.  
Arvid（01:20:07）感觉也许能证明模型对齐，或证明它给对答案。

Sualeh [(01:20:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=4820) That’s the dream.  
Sualeh（01:20:20）那是梦想。

Lex [(01:20:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=4821) Yeah, that is… I mean, if it’s possible. That’s your I have a dream speech. If it’s possible, that will certainly help with making sure your code doesn’t have bugs and making sure AI doesn’t destroy all human civilization. So the full spectrum of AI safety to just bug finding. So you said the models struggle with bug finding. What’s the hope?  
Lex（01:20:21）对，若可能——你的「我有一个梦想」演讲。若能，既帮代码少 bug，也帮 AI 别毁灭文明：从 AI 安全到找 bug 全谱。你们说模型找 bug 难，希望在哪？

Sualeh [(01:20:44)](https://youtube.com/watch?v=oFfVt3S51T4&t=4844) My hope initially is, and I can let Michael chime in too, but it was like it should first help with the stupid bugs. It should query quickly, catch the stupid bugs off by one error is like… Sometimes you write something in a comment and do the other way. It’s very common. I do this. I write less than in a comment and I maybe write the greater than or something like that. And the model is like, “Yeah, you looks sketchy. You sure you want to do that?” But eventually, it should be able to catch harder bugs too.  
Sualeh（01:20:44）我最初希望——Michael 也补充——是先搞定蠢 bug：快问快答、抓差一、注释写 `<` 代码写 `>` 那种。我常干。模型说「有点可疑，确定吗？」最终也要能抓更难 bug。

Michael [(01:21:16)](https://youtube.com/watch?v=oFfVt3S51T4&t=4876) Yeah. And I think that it’s also important to note that this is… Having good bug, finding models feels necessary to get to the highest reaches of having AI do more and more programming for you, where you’re going to… If AI is building more and more of the system for you, you need to not just generate but also verify. And without that, some of the problems that we’ve talked about before with programming, with these models will just become untenable. So it’s not just for humans like you write a bug, I write a bug, find the bug for me, but it’s also being able to verify the AI’s code and check it is really important.  
Michael（01:21:16）还要强调：要强 bug 模型才能走到「AI 替你写越来越多」的最高形态；系统它建得越多，你不只要生成还要验证。没有这步，前面说的编程问题会不可收拾。不只人写 bug 要人帮找，更要能验 AI 写的代码。

Arvid [(01:21:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=4912) Yeah. And then how do you actually do this? We have had a lot of contentious dinner discussions of how do you actually train a bug model, but one very popular idea is it’s kind of potentially easy to introduce a bug than actually finding the bug. And so you can train a model to introduce bugs in existing code and then you can train a reverse bug model then that can find bugs using this synthetic data. So that’s one example, but there are lots of ideas for how to [inaudible 01:22:22].  
Arvid（01:21:52）怎么做？我们晚饭吵过很多次怎么训 bug 模型；流行想法是：注入 bug 可能比找 bug 容易，于是训模型往代码里塞 bug，再训「反 bug」模型用合成数据找 bug。例子之一，别的想法也很多[听不清]。

Michael [(01:22:23)](https://youtube.com/watch?v=oFfVt3S51T4&t=4943) You can also do a bunch of work not even at the model level of taking the biggest models and then maybe giving them access to a lot of information that’s not just the code. It’s kind of a hard problem to stare at a file and be like, “Where’s the bug?” And that’s hard for humans often, right? And so often you have to run the code and being able to see things like traces and step through a debugger, there’s another whole other direction where it tends toward that.  
Michael（01:22:23）也可在模型外下功夫：最大模型加上不止代码的信息。盯着文件问「bug 在哪」人也难；常要跑起来、看 trace、调试器单步，另一大方向。

[(01:22:46)](https://youtube.com/watch?v=oFfVt3S51T4&t=4966) It could also be that there are two different product form factors here. It could be that you have a really specialty model that’s quite fast that’s running in the background and trying to spot bugs. And it might be that sometimes sort of to Arvid’s earlier example about some nefarious input box bug. It might be that sometimes you want to like… You know there’s a bug, you’re not just checking hypothesis free, you’re like, “This is a problem, I really want to solve it,” and you zap that with tons and tons and tons of compute, and you’re willing to put in $50 to solve that bug or something even more.  
（01:22:46）也可能有两种产品形态：后台跑一个快的小专模盯 bug；有时像 Arvid 说的输入框坏 bug，你已知道有问题，不是无假设乱扫，而是「我就要搞定」，砸大量算力，愿意花 50 美元换修 bug。

Lex [(01:23:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=4992) Have you thought about integrating money into this whole thing? I would pay probably a large amount of money if you found a bug or even generated code that I really appreciated. I had a moment a few days ago when I started using Cursor where it generated perfect three functions for interacting with the YouTube API to update captions for localization in different languages. The API documentation is not very good and the code across, if I… I googled it for a while. I couldn’t find exactly, there’s a lot of confusing information, and Cursor generated perfectly.  
Lex（01:23:12）想过把钱整进产品吗？找到 bug 或生成我特别感激的代码，我愿意付不少。前几天 Cursor 给我生成了三条完美的 YouTube API 函数，做多语言字幕更新；文档很乱，我搜半天也糊，Cursor 一次对。

[(01:23:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=5033) I just sit back, I read the code, I was like, “This is correct. I tested it, it’s correct.” I was like, “I want to tip.” I want a button that goes, “Here’s $5.” One that’s really good just to support the company and support what the interface is. And the other is that probably sends a strong signal like good job. So there’s this much stronger signal than just accepting the code. You just actually send a strong good job. That and for bug finding, obviously, there’s a lot of people that would pay a huge amount of money for a bug bounty thing, right? You guys think about that?  
（01:23:53）我坐那儿读代码：「对，我测了，对。」我想给小费，要个按钮「这是 5 美元」——既支持公司，也是比「接受代码」强得多的正向信号。找 bug 显然很多人愿为赏金付大钱，你们想过吗？

Arvid [(01:24:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=5073) Yeah, it’s a controversial idea inside the company. I think it sort of depends on how much you believe in humanity almost. I think it would be really cool if you spend nothing to try to find a bug. And if it doesn’t find a bug, you spend $0. And then if it does find a bug and you click accept, then it also shows in parentheses like $1. And so you spend $1 to accept the bug. And then of course, there’s a worry like okay, “We spent a lot of computation, maybe people will just copy paste.” I think that’s a worry. Then there is also the worry that introducing money into the product makes it… It doesn’t feel as fun anymore. You have to think about money. And all you want to think about is the code, and so maybe it actually makes more sense to separate it out, and you pay some fee every month, and then you get all of these things for free.  
Arvid（01:24:33）公司内部有争议，有点像你多信人性。我觉得很酷的是：试找 bug 先花 0；没找到就 0；找到了你点接受，括号里写 $1，你花 1 美元认领。但也会担心：我们烧了很多算力，有人只复制粘贴。另一个担心：钱进产品就不那么好玩，你得想钱，而你想只想代码；也许更好是月费包圆，这些都「免费」包在订阅里。

Lex [(01:25:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=5129) But there could be a tipping component which is not like it cost this-  
Lex（01:25:29）但可以有打赏成分，不是按成本——

Arvid [(01:25:32)](https://youtube.com/watch?v=oFfVt3S51T4&t=5132) Yes, but it still has that dollar symbol. I think it’s fine, but I also see the point where maybe you don’t want to introduce it.  
Arvid（01:25:32）对，但仍有美元符号。我觉得可以，但也理解有人不想引入。

Aman [(01:25:40)](https://youtube.com/watch?v=oFfVt3S51T4&t=5140) Yeah, I was going to say the moment that feels like people do this is when they share it. When they have this fantastic example, they just share it with their friends.  
Aman（01:25:40）我想说人们真会掏钱分享的时刻：有超棒例子就发给朋友。

Michael [(01:25:46)](https://youtube.com/watch?v=oFfVt3S51T4&t=5146) There is also a potential world where there’s a technical solution to this like honor system problem too, where if we can get to a place where we understand the output of the system more, I mean, to the stuff we were talking about with error checking with the LSP and then also running the code. But if you could get to a place where you could actually somehow verify, “Oh, I have fixed the bug,” maybe then the bounty system doesn’t need to rely on the honor system too.  
Michael（01:25:46）也可能有技术解「荣誉系统」问题：若我们更懂系统输出——LSP 报错、跑代码等——能某种方式验证「bug 真修好了」，赏金就不必全靠自觉。

## Branching file systems  
## 分支文件系统

Lex [(01:26:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=5169) How much interaction is there between the terminal and the code? How much information is gained from if you run the code in the terminal? Can you do a loop where it runs the code and suggests how to change the code? If the code and runtime gets an error? Is right now there’s separate worlds completely? I know you can do control K inside the terminal to help you write the code.  
Lex（01:26:09）终端和代码交互有多深？在终端跑代码能拿到多少信息？能否循环：跑代码→根据报错建议改代码？现在是否完全两个世界？我知道终端里能 Cmd+K 帮你写命令。

Aman [(01:26:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=5195) You can use terminal context as well inside of check command K kind of everything. We don’t have the looping part yet, so we suspect something like this could make a lot of sense. There’s a question of whether it happens in the foreground too or if it happens in the background like what we’ve been discussing.  
Aman（01:26:35）Cmd+K 等场景也能用终端上下文。闭环循环还没有，我们觉得合理。问题是前台做还是像我们聊的后台做。

Lex [(01:26:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=5212) Sure. The background’s pretty cool. I could be running the code in different ways. Plus there’s a database side to this, which how do you protect it from not modifying the database, but okay.  
Lex（01:26:52）后台很酷。还有数据库侧：怎么避免乱改库，但先不展开。

Sualeh [(01:27:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=5223) I mean, there’s certainly cool solutions there. There’s this new API that is being developed for… It’s not in AWS, but it certainly… I think it’s in PlanetScale. I don’t know if PlanetScale was the first one to you add it. It’s this ability sort of add branches to a database, which is like if you’re working on a feature and you want to test against the broad database, but you don’t actually want to test against the broad database, you could sort of add a branch to the database. And the way they do that is they add a branch to the write-ahead log. And there’s obviously a lot of technical complexity in doing it correctly. I guess database companies need new things to do. They have good databases now. And I think turbopuffer, which is one of the databases we use, is going to add maybe branching to the write-ahead log. So maybe the AI agents will use branching, they’ll test against some branch, and it’s sort of going to be a requirement for the database to support branching or something.  
Sualeh（01:27:03）那边肯定有酷解法。有种新 API 在开发……不在 AWS，PlanetScale 一类在搞：给数据库加「分支」，做功能时要测真实库又不想真碰生产库，就分支。做法是在 WAL 上分支。做对很难。数据库公司也要新活干。turbopuffer 我们也在用，可能也会在 WAL 上做分支。也许以后 agent 用分支测，数据库支持分支会变成某种要求。

Aman [(01:28:10)](https://youtube.com/watch?v=oFfVt3S51T4&t=5290) It would be really interesting if you could branch a file system, right?  
Aman（01:28:10）若能分支文件系统会很有趣，对吧？

Sualeh [(01:28:13)](https://youtube.com/watch?v=oFfVt3S51T4&t=5293) Yeah. I feel like everything needs branching. It’s like-  
Sualeh（01:28:13）对，感觉万物都要能分支，像——

Aman [(01:28:13)](https://youtube.com/watch?v=oFfVt3S51T4&t=5293) Yeah.  
Aman（01:28:13）对。

Lex [(01:28:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=5297) Yeah. The problem with the multiverse, right? If you branch on everything that’s like a lot.  
Lex（01:28:17）多元宇宙问题：啥都分支就爆炸了。

Sualeh [(01:28:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=5304) There’s obviously these super clever algorithms to make sure that you don’t actually use a lot of space or CPU or whatever.  
Sualeh（01:28:24）显然有聪明算法控制空间、CPU 等。

Lex [(01:28:32)](https://youtube.com/watch?v=oFfVt3S51T4&t=5312) Okay. This is a good place to ask about infrastructure. So you guys mostly use AWS, what are some interesting details? What are some interesting challenges? Why’d you choose AWS? Why is AWS still winning? Hashtag.  
Lex（01:28:32）好，问基础设施：你们多用 AWS，有什么有趣细节与挑战？为何选 AWS？为何还赢？#梗

Arvid [(01:28:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=5325) AWS is just really, really good. It is really good. Whenever you use an AWS product, you just know that it’s going to work. It might be absolute hell to go through the steps to set it up.  
Arvid（01:28:45）AWS 真的很好。用它的产品你知道会work。搭起来可能是地狱。

Lex [(01:29:02)](https://youtube.com/watch?v=oFfVt3S51T4&t=5342) Why is the interface so horrible?  
Lex（01:29:02）界面为何这么烂？

Sualeh [(01:29:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=5344) Because it’s-  
Sualeh（01:29:04）因为——

Arvid [(01:29:05)](https://youtube.com/watch?v=oFfVt3S51T4&t=5345) It’s just so good. It doesn’t need to-  
Arvid（01:29:05）太好用了，不需要——

Lex [(01:29:06)](https://youtube.com/watch?v=oFfVt3S51T4&t=5346) It’s the nature of winning.  
Lex（01:29:06）赢家的常态。

Sualeh [(01:29:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=5349) I think it’s exactly. It’s just nature they’re winning.  
Sualeh（01:29:09）就是这样，赢的自然。

Arvid [(01:29:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=5351) Yeah, yeah. But AWS we can always trust, it will always work. And if there is a problem, it’s probably your problem. Yeah.  
Arvid（01:29:11）对。AWS 可信，总会work。有问题多半是你自己的问题。

## Scaling challenges  
## 规模化挑战

Lex [(01:29:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=5360) Okay. Is there some interesting challenges to… You guys are pretty new startup to scaling, to so many people and-  
Lex（01:29:20）好。你们相对新的创业公司，扩到这么多人、这么多请求，有什么有趣挑战——

Michael [(01:29:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=5369) Yeah, I think that it has been an interesting journey adding each extra zero to the request per second. You run into all of these with the general components you’re using for caching and databases, run into issues as you make things bigger and bigger, and now we’re at the scale where we get into overflows on our tables and things like that. And then also there have been some custom systems that we’ve built. For instance, our retrieval system for computing, a semantic index of your code base and answering questions about a code base that have, continually, I feel like been one of the trickier things to scale.  
Michael（01:29:29）每秒请求每多一个数量级都是旅程。缓存、数据库等通用组件越放大问题越多，我们现在表溢出之类都遇到了。还有自研系统：给代码库建语义索引、答代码库问题那套检索，一直是最难扩的一块。

Michael [(01:30:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=5400)… that have continually, I feel like, been one of the trickier things to scale.  
Michael（01:30:00）……一直是最难扩的之一。

Sualeh [(01:30:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=5404) I have a few friends who are super senior engineers and one of their lines is, it’s very hard to predict where systems will break when you scale them. You can try to predict in advance, but there’s always something weird that’s going to happen when you add these extras here. You thought through everything, which you didn’t actually think through everything. But I think for that particular system, we’ve… So for concrete details, the thing we do is obviously we upload when… We chunk up all of your code, and then we send up the code for embedding and we embed the code. And then we store the embeddings in a database, but we don’t actually store any of the code. And then there’s reasons around making sure that we don’t introduce client bugs because we’re very, very paranoid about client bugs. We store much of the details on the server. Everything is encrypted.  
Sualeh（01:30:04）我有极资深朋友常说：系统扩起来哪里会炸很难预判；你以为想全了其实没有。具体这套：我们把代码分块上传做 embedding，向量存库，**不存代码原文**。原因包括少引入客户端 bug——我们非常怕客户端 bug。细节多在服务端，全加密。

[(01:31:08)](https://youtube.com/watch?v=oFfVt3S51T4&t=5468) So one of the technical challenges is always making sure that the local index, the local code base state is the same as the state that is on the server. The way, technically, we ended up doing that is, for every single file you can keep this hash, and then for every folder you can keep a hash, which is the hash of all of its children. You can recursively do that until the top. Why do something complicated? One thing you could do is you could keep a hash for every file and every minute, you could try to download the hashes that are on the server, figure out what are the files that don’t exist on the server. Maybe you just created a new file, maybe you just deleted a file, maybe you checked out a new branch, and try to reconcile the state between the client and the server.  
（01:31:08）技术挑战之一是本地索引/代码库状态要与服务端一致。做法：每文件一个哈希，每文件夹哈希为其子项哈希递归到根。为何不搞复杂？笨办法是每分钟拉服务端哈希比对新建删改、切分支等——客户端与服务端对齐。

[(01:31:57)](https://youtube.com/watch?v=oFfVt3S51T4&t=5517) But that introduces absolutely ginormous network overhead both on the client side. Nobody really wants us to hammer their WiFi all the time if you’re using Cursor. But also, it would introduce ginormous overhead on the database. It would be reading these tens of terabytes database, approaching 20 terabytes or something data base every second. That’s just crazy. You definitely don’t want to do that. So what you do, you just try to reconcile the single hash, which is at the root of the project. And then if something mismatches, then you go, you find where all the things disagree. Maybe you look at the children and see if the hashes match. If the hashes don’t match, go look at their children and so on. But you only do that in the scenario where things don’t match. For most people, most of the time, the hashes match.  
（01:31:57）但那会巨大网络开销：没人想我们一直狂打 WiFi；数据库也扛不住每秒扫十几二十 TB。所以只比对**项目根**单一哈希；不一致再向下找分歧：看子节点哈希，不匹配再往下。只在不一致时这么做；多数时候哈希一致。

Lex [(01:32:50)](https://youtube.com/watch?v=oFfVt3S51T4&t=5570) So it’s like a hierarchical reconciliation-  
Lex（01:32:50）像分层对账——

Sualeh [(01:32:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=5573) Yeah.  
Sualeh（01:32:53）对。

Lex [(01:32:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=5573)… of hashes-  
Lex（01:32:53）……哈希——

Sualeh [(01:32:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=5573) Something like that.  
Sualeh（01:32:53）类似那样。

Aman [(01:32:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=5574) Yeah, it’s called a Merkle tree.  
Aman（01:32:54）对，叫 Merkle 树。

Lex [(01:32:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=5576) Yeah, Merkle. Yeah. Yeah, this is cool to see that you have to think through all these problems.  
Lex（01:32:56）Merkle，对。这些问题都要想清楚，很酷。

Sualeh [(01:33:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=5583) The reason it’s gotten hard is just because the number of people using it and some of your customers have really, really large code bases to the point where… We originally reordered dark code base, which is big, but it’s just not the size of some company that’s been there for 20 years and has a ginormous number of files and you want to scale that across programmers. There’s all these details where building the simple thing is easy, but scaling it to a lot of people, a lot of companies is obviously a difficult problem, which is independent of, actually… so that there’s part of this scaling. Our current solution is also coming up with new ideas that, obviously, we’re working on, but then scaling all of that in the last few weeks, months.  
Sualeh（01:33:03）难在用户量、客户库巨大——我们自家 dark 库已经大，但比不过二十年公司海量文件还要跨程序员扩。简单版好做，扩到人、到公司难，这是 scaling 的另一面。我们方案也在迭代，最近几周几个月都在扩。

Aman [(01:33:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=5628) Yeah. There are a lot of clever things, additional things that go into this indexing system. For example, the bottleneck in terms of costs is not soaring things in the vector database or the database. It’s actually embedding the code. You don’t want to re-embed the code base for every single person in a company that is using the same exact code except for maybe they’re a different branch with a few different files or they’ve made a few local changes. Because again, embeddings are the bottleneck, you can do this one clever trick and not have to worry about the complexity of dealing with branches and the other databases where you just have some cash on the actual vectors computed from the hash of a given chunk. So this means that when the nth person at a company goes and embed their code base, it’s really, really fast. You do all this without actually storing any code on our servers at all. No code data is stored. We just store the vectors in the vector database and the vector cache.  
Aman（01:33:48）索引系统还有很多巧思。成本瓶颈不在向量库存储，而在 **embedding 代码**。同公司多人同代码库，只差分支或本地小改，不应每人全量重嵌。embedding 是瓶颈，可玩一招：按 chunk 哈希缓存已算向量，少碰分支合并的复杂度。公司第 n 个人嵌库就极快。且服务器**不存代码**，只取向量库与向量缓存。

Lex [(01:34:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=5685) What’s the biggest gains at this time you get from indexing the code base? Just out of curiosity, what benefit do users have? It seems like longer term, there’ll be more and more benefit, but in the short term, just asking questions of the code base, what’s the usefulness of that?  
Lex（01:34:45）现在索引代码库最大收益是什么？用户短期问代码库问题，用处多大？长期似乎更多。

Arvid [(01:35:06)](https://youtube.com/watch?v=oFfVt3S51T4&t=5706) I think the most obvious one is just, you want to find out where something is happening in your large code base, and you have a fuzzy memory of, “Okay, I want to find the place where we do X,” but you don’t exactly know what to search for in a normal text search. So you ask a chat, you hit command enter to ask with the code base chat. And then very often, it finds the right place that you were thinking of.  
Arvid（01:35:06）最明显：大库里找「某事在哪发生」，只记得模糊想搜 X，文本搜索不知道搜啥。用代码库对话 Cmd+Enter 问，常常就找到你想的那处。

Aman [(01:35:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=5733) Like you mentioned, in the future, I think there’s only going to get more and more powerful, where we’re working a lot on improving the quality of our retrieval. I think the ceiling for that is really, really much higher than people give the credit for.  
Aman（01:35:33）如你所说，未来会更强；我们在猛提检索质量，天花板比大家想的高得多。

Lex [(01:35:46)](https://youtube.com/watch?v=oFfVt3S51T4&t=5746) One question that’s good to ask here, have you considered and why haven’t you much done local stuff to where you can do the… It seems like everything was just discussed as exceptionally difficult to do. To go to the cloud, you have to think about all these things with the caching and the large code base where a large number of programmers are using the same code base. You have to figure out the puzzle of that. A lot of it, most software just does this heavy computational stuff locally. So have you considered doing embeddings locally?  
Lex（01:35:46）好问题：本地 embedding 考虑过吗？为何没多做？云上缓存、多人同库很难；很多软件重算放本地。你们想过本地嵌吗？

Arvid [(01:36:18)](https://youtube.com/watch?v=oFfVt3S51T4&t=5778) Yeah, we thought about it, and I think it would be cool to do it locally. I think it’s just really hard. One thing to keep in mind is that some of our users use the latest MacBook Pro, but most of our users, more than 80% of our users are in Windows machines, which many of them are not very powerful. So local models really only works on the latest computers, and it’s also a big overhead to build that in. So even if we would like to do that, it’s currently not something that we are able to focus on. I think there are some people that do that, and I think that’s great, but especially as models get bigger and bigger and you want to do fancier things with bigger models, it becomes even harder to do it locally.  
Arvid（01:36:18）想过，本地很酷，但很难。有人用最新 MacBook Pro，但八成多用户是 Windows，很多机器不强。本地模型基本只在新电脑上跑得动，工程量也大。想做但目前没法聚焦。有人做本地我们觉得很棒；模型越大、事越花，本地越难。

Sualeh [(01:37:07)](https://youtube.com/watch?v=oFfVt3S51T4&t=5827) Yeah. It’s not a problem of weaker computers. It’s just that for example, if you’re some big company, you have big company code base. It’s just really hard to process big company code base even on the beefiest MacBook Pros. It’s not even a matter of if you’re just a student or something. I think if you’re the best programmer at a big company, you’re still going to have a horrible experience. If you do everything locally where you could do it and scrape by, but again, it wouldn’t be fun anymore.  
Sualeh（01:37:07）不全是机器弱：大公司代码库即使用最强 MacBook Pro 也难本地处理。不是学生才这样，大公司最强程序员也会很痛苦。全本地也许能硬扛，但不好玩了。

Aman [(01:37:40)](https://youtube.com/watch?v=oFfVt3S51T4&t=5860) Yeah. Like at approximate nearest neighbors and this massive code base is going to just eat up your memory and your CPU, and it’s based off of that. That’s just that. Let’s talk about also the modeling side where, as Arvid said, there are these massive headwinds against local models where one, things that seem to move towards MOEs, which one benefit is maybe their more memory bandwidth bound, which plays in favor of local versus using GPUs or using Nvidia GPUs. But the downside is, these models are just bigger in total, and they’re going to need to fit, often not even on a single node but multiple nodes. There’s no way that’s going to fit inside of even really good MacBooks. I think especially for coding, it’s not a question as much of, does it clear some bar of the model’s good enough to do these things and then we’re satisfied? Which may be the case for other problems and maybe where local models shine, but people are always going to want the best, the most intelligent, the most capable things, and that’s going to be really, really hard to run for almost all people, locally.  
Aman（01:37:40）近似最近邻加大代码库会吃光内存 CPU。模型侧：MOE 等趋势对本地有利有弊——带宽绑定有时利于本地；但模型总量更大，常要多机，好 MacBook 也塞不下。编程不是「过线就够」——别的任务也许本地够用；人要的是最好、最聪明、最能干，这几乎不可能人人本地跑。

Sualeh [(01:38:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=5931) Don’t you want the most capable model? You want [inaudible 01:38:55] too?  
Sualeh（01:38:51）你不想最强模型吗？你也想[听不清]？

Aman [(01:38:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=5936) And also o1-  
Aman（01:38:56）还有 o1——

Lex [(01:38:58)](https://youtube.com/watch?v=oFfVt3S51T4&t=5938) I like how you’re pitching me.  
Lex（01:38:58）你们在给我推销。

Aman [(01:39:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=5940) o1 is another-  
Aman（01:39:00）o1 又是——

Lex [(01:39:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=5940) Would you be satisfied with an inferior model? Listen, yes, I’m one of those, but there’s some people that like to do stuff locally, especially like… Really, there’s a whole obviously open source movement that resists. It’s good that they exist actually because you want to resist the power centers that are growing our-  
Lex（01:39:00）次优模型你满足吗？听我说，我是这类人之一，但有人爱本地，尤其开源运动抵制中心化——他们存在是好事，要制衡权力中心——

Arvid [(01:39:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=5960) There’s actually an alternative to local models that I am particularly fond of. I think it’s still very much in the research stage, but you could imagine to do homomorphic encryption for language model inference. So you encrypt your input on your local machine, then you send that up, and then the server can use loss of computation. They can run models that you cannot run locally on this encrypted data, but they cannot see what the data is, and then they send back the answer and you decrypt the answer and only you can see the answer. So I think that’s still very much research and all of it is about trying to make the overhead lower because right now, the overhead is really big, but if you can make that happen, I think that would be really, really cool, and I think it would be really, really impactful because I think one thing that’s actually worrisome is that, as these models get better and better, they’re going to become more and more economically useful.  
Arvid（01:39:20）本地模型之外我特别喜欢全同态加密推理：本地加密输入上传，服务端在密文上算（口误 loss 应为 lots），跑你本地跑不动的大模型，但看不到明文，返回密文你本地解密。仍偏研究，开销巨大，要压低。若成会很酷也很有影响：模型越有用，越多数据会流经少数中心。

[(01:40:18)](https://youtube.com/watch?v=oFfVt3S51T4&t=6018) So more and more of the world’s information and data will flow through one or two centralized actors. And then there are worries about, there can be traditional hacker attempts, but it also creates this scary part where if all of the world’s information is flowing through one node in plaintext, you can have surveillance in very bad ways. Sometimes that will happen for… Initially, will be good reasons. People will want to try to protect against bad actors using AI models in bad ways, and then you will add in some surveillance code. And then someone else will come in and you’re on a slippery slope, and then you start doing bad things with a lot of the world’s data. So I am very hopeful that we can solve homomorphic encryption for-  
（01:40:18）世界越来越多信息流经一两个中心。黑客是一方面；更可怕的是明文全过一个节点可被监控。起初可能出于好意：防坏人滥用 AI，加监控代码；然后滑坡，对世界数据做坏事。我很希望全同态推理能成——

Lex [(01:41:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=6071) Yeah, and-  
Lex（01:41:11）对，以及——

Arvid [(01:41:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=6072)… language model inference.  
Arvid（01:41:12）……语言模型推理。

Lex [(01:41:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=6072)… doing privacy, preserving machine learning. But I would say, that’s the challenge we have with all software these days. It’s like there’s so many features that can be provided from the cloud and all us increasingly rely on it and make our life awesome. But there’s downsides, and that’s why you rely on really good security to protect from basic attacks. But there’s also only a small set of companies that are controlling that data, and they obviously have leverage and they could be infiltrated in all kinds of ways. That’s the world we live in. So it’s-  
Lex（01:41:12）……隐私保护机器学习。但这也是当今所有软件的难题：云能提供的功能很多，我们越来越依赖，生活很爽；也有代价，要靠安全防基础攻击；数据又集中在少数公司，可被渗透。我们活在这样的世界。所以——

Sualeh [(01:41:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=6103) Yeah, the thing I’m just actually quite worried about is the world where… Anthropic has this responsible scaling policy where we’re the low ASLs, which is the Anthropic security level or whatever of the models. But as we get to ASL-3, ASL-4, whatever models which are very powerful… But for mostly reasonable security reasons, you would want to monitor all the prompts. But I think that’s reasonable and understandable where everyone is coming from. But man, it’d be really horrible if all the world’s information is monitored that heavily, it’s way too centralized. It’s like this really fine line you’re walking where on the one side, you don’t want the models to go rogue. On the other side, humans like… I don’t know if I trust all the world’s information to pass through three model providers.  
Sualeh（01:41:43）我挺担心的是：Anthropic 有责任扩展政策、低 ASL（Anthropic 安全等级）等；到 ASL-3、4 超强模型，出于安全理由会想监控所有 prompt，这可以理解。但若世界信息都被这么监控就太糟、太集中。一边怕模型失控，一边……我不知道是否该信任全球信息只过三家模型商。

Aman [(01:42:44)](https://youtube.com/watch?v=oFfVt3S51T4&t=6164) Why do you think it’s different than cloud providers?  
Aman（01:42:44）这和云厂商有何不同？

Arvid [(01:42:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=6167) Because I think a lot of this data would never have gone to the cloud providers in the first place where this is often… You want to give more data to the AI models, you want to give personal data that you would never have put online in the first place to these companies or to these models. It also centralizes control where right now, for cloud, you can often use your own encryption keys, and AWS can’t really do much. But here, it’s just centralized actors that see the exact plain text of everything.  
Arvid（01:42:47）很多数据本不会上传统云；AI 你想给更多、更私人的，本来不会上网的也给模型。云你还能自带密钥 AWS 难动；这里中心玩家看到的是明文一切。

## Context  
## 上下文

Lex [(01:43:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=6211) Yeah. On the topic of a context, that’s actually been a friction for me. When I’m writing code in Python, there’s a bunch of stuff imported. You could probably intuit the kind of stuff I would like to include in the context. How hard is it to auto figure out the context?  
Lex（01:43:31）上下文话题对我确实是摩擦：写 Python 一堆 import，你大概能猜我想放进上下文的东西。自动凑上下文有多难？

Michael [(01:43:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=6231) It’s tricky. I think we can do a lot better at computing the context automatically in the future. One thing that’s important to note is, there are trade-offs with including automatic context. So the more context you include for these models, first of all, the slower they are and the more expensive those requests are, which means you can then do less model calls and do less fancy stuff in the background. Also, for a lot of these models, they get confused if you have a lot of information in the prompt. So the bar for accuracy and for relevance of the context you include should be quite high. Already, we do some automatic context in some places within the product. It’s definitely something we want to get a lot better at. I think that there are a lot of cool ideas to try there, both on the learning better retrieval systems, like better embedding models, better rerankers.  
Michael（01:43:51）棘手。未来自动算上下文能好很多。要注意取舍：上下文越多越慢越贵，后台能玩的调用就更少；很多模型 prompt 信息一多就糊涂。所以自动上下文的准确与相关性门槛要高。产品里已局部自动上下文，还要猛提。方向包括更好检索：embedding、reranker。

[(01:44:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=6288) I think that there are also cool academic ideas, stuff we’ve tried out internally, but also the field is grappling with writ large about, can you get language models to a place where you can actually just have the model itself understand a new corpus of information? The most popular talked about version of this is can you make the context windows infinite? Then if you make the context windows infinite, can you make the model actually pay attention to the infinite context? And then after you can make it pay attention to the infinite context to make it somewhat feasible to actually do it, can you then do caching for that infinite context? You don’t have to recompute that all the time. But there are other cool ideas that are being tried, that are a little bit more analogous to fine-tuning of actually learning this information in the weights of the model. It might be that you actually get a qualitative lead different type of understanding if you do it more at the weight level than if you do it at the in-context learning level.  
（01:44:48）学界也在吵：能否让模型真正「理解」新语料？最热的是无限上下文；无限了能否真 attend；可行了能否缓存无限上下文免重算。还有更像微调、把知识写进权重的路线。权重级相对 in-context 也许是质的不同理解。

[(01:45:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=6337) I think the jury’s still a little bit out on how this is all going to work in the end? But in the interim, us as a company, we are really excited about better retrieval systems and picking the parts of the code base that are most relevant to what you’re doing, and we could do that a lot better.  
（01:45:37）最终怎么走陪审团还没定论。现阶段我们更兴奋的是更好检索、抓最相关代码块，我们还能强很多。

Aman [(01:45:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=6352) One interesting proof of concept for the learning this knowledge directly in the weights is with VS Code. So we’re in a VS Code fork and VS Code. The code is all public. So these models in pre-training have seen all the code. They’ve probably also seen questions and answers about it. And then they’ve been fine-tuned and RLHFed to be able to answer questions about code in general. So when you ask it a question about VS Code, sometimes it’ll hallucinate, but sometimes it actually does a pretty good job at answering the question. I think this is just by… It happens to be okay, but what if you could actually specifically train or post-train a model such that it really was built to understand this code base?  
Aman（01:45:52）权重里学知识的有趣 PoC 是 VS Code：我们是 VS Code fork，代码全公开，预训练见过，可能还有问答，再微调 RLHF 答代码问题。问 VS Code 有时 hallucinate 有时还行。若专门 post-train 真懂某代码库呢？

[(01:46:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=6398) It’s an open research question, one that we’re quite interested in. And then there’s also uncertainty of, do you want the model to be the thing that end-to-end is doing everything, i.e. it’s doing the retrieval in its internals and then answering a question, creating the code, or do you want to separate the retrieval from the frontier model, where maybe you’ll get some really capable models that are much better than the best open source ones in a handful of months? And then you’ll want to separately train a really good open source model to be the retriever, to be the thing that feeds in the context to these larger models.  
（01:46:38）开放问题，我们很感兴趣。也不确定：要端到端模型内部检索+答+写码，还是检索与前沿模型分离——几个月后前沿远超开源，再单独训强 retriever 喂大模型？

Lex [(01:47:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=6434) Can you speak a little more to post-training a model to understand the code base? What do you mean by that? Is this a synthetic data direction? Is this-  
Lex（01:47:14）多说说 post-train 让模型懂代码库？什么意思？合成数据方向？还是——

Aman [(01:47:23)](https://youtube.com/watch?v=oFfVt3S51T4&t=6443) Yeah, there are many possible ways you could try doing it. There’s certainly no shortage of ideas. It’s just a question of going in and trying all of them and being empirical about which one works best. One very naive thing is to try to replicate what’s done with VS Code and these frontier models. So let’s continue pre-training. Some kind of continued pre-training that includes general code data but also throws in of the data of some particular repository that you care about. And then in post-training, meaning in… Let’s just start with instruction fine-tuning. You have a normal instruction fine-tuning data set about code. Then you throw in a lot of questions about code in that repository.  
Aman（01:47:23）路子很多，不缺想法，要试 empirically。很笨的办法是仿 VS Code+前沿：继续预训练，通用代码+你关心的仓库数据。post-training 先指令微调：普通代码指令集，再加大量该仓库问答。

[(01:48:07)](https://youtube.com/watch?v=oFfVt3S51T4&t=6487) So you could either get ground truth ones, which might be difficult or you could do what you hinted at or suggested using synthetic data, i.e. having the model ask questions about various recent pieces of the code. So you take the pieces of the code, then prompt the model or have a model propose a question for that piece of code, and then add those as instruction fine-tuning data points. And then in theory, this might unlock the model’s ability to answer questions about that code base.  
（01:48:07）真值问答难搞就用合成：对最近代码块让模型出题，加成指令数据。理论上可解锁答该库问题能力。

## OpenAI o1  
## OpenAI o1

Lex [(01:48:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=6519) Let me ask you about OpenAI o1. What do you think is the role of that kind of test time compute system in programming?  
Lex（01:48:39）问问 OpenAI o1：这类测试时算力（推理时扩算）在编程里角色是什么？

Aman [(01:48:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=6527) I think test time compute is really, really interesting. So there’s been the pre-training regime which will, as you scale up the amount of data and the size of your model, get you better and better performance both on loss and then on downstream benchmarks and just general performance. So we use it for coding or other tasks. We’re starting to hit a bit of a data wall. Meaning, it’s going to be hard to continue scaling up this regime. So scaling up test time compute is an interesting way, if now increasing the number of inference time flops that we use but still getting… Yeah, as you increase the number of flops you use inference time getting corresponding improvements in the performance of these models. Traditionally, we just had to literally train a bigger model that always used that many more flops, but now, we could perhaps use the same size model and run it for longer to be able to get an answer at the quality of a much larger model.  
Aman（01:48:47）测试时算力很有意思。预训练范式随数据量、模型变大，loss 与下游都会变好，我们用于编程等任务。但现在撞「数据墙」，难继续按老路扩。扩测试时算力有趣：同样增大推理 FLOPs 能换性能提升；传统要训更大模型才多费那些 FLOPs，现在也许同尺寸模型多跑几步就能逼近更大模型的答案质量。

[(01:49:46)](https://youtube.com/watch?v=oFfVt3S51T4&t=6586) So the really interesting thing I like about this is there are some problems that perhaps require 100 trillion parameter model intelligence trained on 100 trillion tokens. But that’s maybe 1%, maybe 0.1% of all queries. So are you going to spend all of this effort, all of this compute training a model that costs that much and then run it so infrequently? It feels completely wasteful when instead you get the model that can… You train the model that is capable of doing the 99.9% of queries, then you have a way of inference time running it longer for those few people that really, really want max intelligence.  
（01:49:46）我喜欢的点是：有些问题也许要「百万亿参数×百万亿 token」级智能，但可能只占查询的 1% 或 0.1%。你真要砸钱训那么贵的模型却极少跑？浪费。不如训能覆盖 99.9% 查询的模型，再对极少数要极限智能的人加长推理。

Lex [(01:50:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=6628) How do you figure out which problem requires what level of intelligence? Is that possible to dynamically figure out when to use GPT-4, when to use a small model and when you need the o1?  
Lex（01:50:28）怎么判断哪题要多高智能？能否动态决定何时 GPT-4、何时小模型、何时 o1？

Aman [(01:50:44)](https://youtube.com/watch?v=oFfVt3S51T4&t=6644) Yeah, that’s an open research problem, certainly. I don’t think anyone’s actually cracked this model routing problem quite well. We have initial implementations of this for something like Cursor Tab, but at the level of going between 4o sonnet to o1, it’s a bit trickier. There’s also a question like, what level of intelligence do you need to determine if the thing is too hard for the four level model? Maybe you need the o1 level model. It’s really unclear.  
Aman（01:50:44）开放问题，没人真正把模型路由做好。Cursor Tab 层我们有初版；4o/Sonnet 与 o1 之间切换更难。还有：判断「4 级模型不够」本身要多聪明？也许要 o1 级？不清楚。

Lex [(01:51:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=6679) But you mentioned this. So there’s a pre-training process then there’s post-training, and then there’s test time compute. Is that fair to separate? Where’s the biggest gains?  
Lex（01:51:19）你提到预训练、post-training、测试时算力，这样分公平吗？最大收益在哪？

Aman [(01:51:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=6691) Well, it’s weird because test time compute, there’s a whole training strategy needed to get test time compute to work. The other really weird thing about this is outside of the big labs and maybe even just OpenAI, no one really knows how it works. There’ve been some really interesting papers that show hints of what they might be doing. So perhaps they’re doing something with tree search using process reward models. But yeah, I think the issue is we don’t quite know exactly what it looks like, so it would be hard to comment on where it fits in. I would put it in post-training, but maybe the compute spent for this kind of… forgetting test time compute to work for a model is going to dwarf pre-training eventually.  
Aman（01:51:31）怪在：测试时算力本身也要一整套训练策略才 work。更怪的是大实验室外、甚至 OpenAI 外，没人真懂怎么做的。有论文给线索，也许过程奖励模型+树搜索。我们不知细节，难说归哪。我倾向算 post-training，但让测试时算力 work 花的算力也许终有一天超过预训练。

Lex [(01:52:18)](https://youtube.com/watch?v=oFfVt3S51T4&t=6738) So we don’t even know if o1 is using just chain of thought or we don’t know how they’re using any of these? We don’t know anything?  
Lex（01:52:18）所以我们连 o1 是不是只靠思维链、怎么用这些都不知道？

Aman [(01:52:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=6747) It’s fun to speculate.  
Aman（01:52:27）瞎猜很有趣。

Lex [(01:52:30)](https://youtube.com/watch?v=oFfVt3S51T4&t=6750) If you were to build a competing model, what would you do?  
Lex（01:52:30）若你做竞品模型，你会怎么做？

Aman [(01:52:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=6755) Yeah. So one thing to do would be, I think you probably need to train a process reward model, which is… So maybe we can get into reward models and outcome reward models versus process reward models. Outcome reward models are the traditional reward models that people are trained for language modeling, and it’s just looking at the final thing. So if you’re doing some math problem, let’s look at that final thing. You’ve done everything and let’s assign a grade to it, how likely we think… What’s the reward for this outcome? Process reward models instead try to grade the chain of thought. So OpenAI had preliminary paper on this, I think, last summer where they use human labelers to get this pretty large several hundred thousand data set of creating chains of thought. Ultimately, it feels like I haven’t seen anything interesting in the ways that people use process reward models outside of just using it as a means of affecting how we choose between a bunch of samples.  
Aman（01:52:35）可能要训过程奖励模型（PRM）。结果奖励模型（ORM）是传统 LM 奖励：只看最终答案，数学题做完打分。PRM 则给思维链步骤打分。OpenAI 去年夏天有初步论文，用人标几十万条思维链。但我没见谁把 PRM 用得特别花，多半还是用来在多样本里挑最好的。

[(01:53:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=6816) So what people do in all these papers is they sample a bunch of outputs from the language model, and then use the process reward models to grade all those generations alongside maybe some other heuristics and then use that to choose the best answer. The really interesting thing that people think might work and people want to work is tree search with these process reward models. Because if you really can grade every single step of the chain of thought, then you can branch out and explore multiple paths of this chain of thought and then use these process reward models to evaluate how good is this branch that you’re taking.  
（01:53:36）论文里常见：从 LM 采样一堆输出，用 PRM（加启发式）打分选最好。大家真想做成的是 PRM+树搜索：若能给思维链每一步打分，就能分支探索多条路，用 PRM 评估这条支好不好。

Lex [(01:54:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=6854) Yeah. When the quality of the branch is somehow strongly correlated with the quality of the outcome at the very end, so you have a good model of knowing which branch to take. So not just in the short term, in the long term?  
Lex（01:54:14）分支质量若与最终答案质量强相关，你就有好模型知道该走哪支——不只短期，长期也是？

Aman [(01:54:26)](https://youtube.com/watch?v=oFfVt3S51T4&t=6866) Yeah. The interesting work that I think has been done is figuring out how to properly train the process… Or the interesting work that has been open sourced and people I think talk about is how to train the process reward models, maybe in a more automated way. I could be wrong here, could not be mentioning some papers. I haven’t seen anything super that seems to work really well for using the process reward models creatively to do tree search and code.  
Aman（01:54:26）有趣工作是如何正确训 PRM——开源圈在聊的可能是自动化标 PRM。我可能漏论文。没见谁把 PRM+树搜索在代码上玩得很转。

Lex [(01:54:52)](https://youtube.com/watch?v=oFfVt3S51T4&t=6892) This is an AI safety, maybe a bit of a philosophy question. So OpenAI says that they’re hiding the chain of thought from the user, and they’ve said that that was a difficult decision to make. Instead of showing the chain of thought, they’re asking the model to summarize the chain of thought. They’re also in the background saying they’re going to monitor the chain of thought to make sure the model is not trying to manipulate the user, which is a fascinating possibility. But anyway, what do you think about hiding the chain of thought?  
Lex（01:54:52）AI 安全/哲学题：OpenAI 说对用户隐藏思维链，称是艰难决定；改让模型总结思维链；还说后台会监控思维链防模型操纵用户。你怎么看藏思维链？

Michael [(01:55:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=6921) One consideration for OpenAI, and this is completely speculative, could be that they want to make it hard for people to distill these capabilities out of their model. It might actually be easier if you had access to that hidden chain of thought to replicate the technology, because pretty important data, like seeing the steps that the model took to get to the final results.  
Michael（01:55:21）纯猜测：OpenAI 可能想让人难从模型里蒸馏能力。若能看到隐藏思维链，复现技术更容易——那是重要数据，逐步怎么走到结果。

Lex [(01:55:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=6939) So you could probably train on that also?  
Lex（01:55:39）也能拿来训？

Michael [(01:55:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=6942) And there was a mirror situation with this, with some of the large language model providers, and also this is speculation, but some of these APIs used to offer easy access to log probabilities for all the tokens that they’re generating and also log probabilities over the prompt tokens. And then some of these APIs took those away. Again, complete speculation, but one of the thoughts is that the reason those were taken away is if you have access to log probabilities similar to this hidden chain of thought, that can give you even more information to try and distill these capabilities out of the APIs, out of these biggest models and to models you control. As an asterisk on also the previous discussion about us integrating o1, I think that we’re still learning how to use this model. So we made o1 available in Cursor because when we got the model, we were really interested in trying it out. I think a lot of programmers are going to be interested in trying it out.  
Michael（01:55:42）类似情况：有些 LLM API 曾开放生成 token 与 prompt token 的 log prob，后来又收走。猜测是 log prob 像隐藏思维链，能帮人从大模型蒸馏到你控制的模型。另注：我们接 o1 也还在学怎么用。拿到模型时我们很兴奋，就在 Cursor 里开放了，很多程序员也会想试。

[(01:56:40)](https://youtube.com/watch?v=oFfVt3S51T4&t=7000) o1 is not part of the default Cursor experience in any way up, and we still haven’t found a way to yet integrate it into the editor in a way that we reach for every hour, maybe even every day. So I think that the jury’s still out on how to use the model, and we haven’t seen examples yet of people releasing things where it seems really clear like, oh, that’s now the use case. The obvious one to turn to is maybe this can make it easier for you to have these background things running, to have these models and loops, to have these models be agentic. But we’re still discovering,  
（01:56:40）o1 还不是默认体验，我们也没找到每小时甚至每天都想用的编辑器集成方式。怎么用这模型陪审团还没定论；也还没见谁发布「显然这就是场景」的东西。自然想到也许是后台跑、循环、agentic。但我们还在摸索，

Sualeh [(01:57:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=7042) To be clear, we have ideas. We just need to try and get something incredibly useful before we put it out there.  
Sualeh（01:57:22）说清楚：我们有想法，但要试到特别有用再端出来。

Aman [(01:57:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=7049) But it has these significant limitations. Even barring capabilities, it does not stream. That means it’s really, really painful to use for things where you want to supervise the output. Instead, you’re just waiting for the wall text to show up. Also, it does feel like the early innings of test time, compute and search where it’s just a very, very much a v0, and there’s so many things that don’t feel quite right. I suspect in parallel to people increasing the amount of pre-training data and the size of the models and pre-training and finding tricks there, you’ll now have this other thread of getting search to work better and better.  
Aman（01:57:29）但限制很大：先不谈能力，它**不流式**，要盯着输出时很痛苦，只能等一大坨字出现。也像测试时算力+搜索的早期局数，很 v0，很多不对劲。我猜一边人们继续扩预训练数据、模型、找技巧，另一边会把搜索越做越好。

Lex [(01:58:13)](https://youtube.com/watch?v=oFfVt3S51T4&t=7093) So let me ask you about strawberry tomorrow eyes. So it looks like GitHub Copilot might be integrating o1 in some kind of way, and I think some of the comments are saying, does this mean Cursor is done? I think I saw one comment saying that.  
Lex（01:58:13）那我问问「strawberry tomorrow eyes」（口误或梗，可能指某新模型代号）。GitHub Copilot 似乎在接 o1，评论说这是不是意味着 Cursor 完了？

Arvid [(01:58:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=7115) It’s a time to shut down Cursor. Yeah.  
Arvid（01:58:35）该关掉 Cursor 了。对。

Lex [(01:58:36)](https://youtube.com/watch?v=oFfVt3S51T4&t=7116) Time to shut down Cursor.  
Lex（01:58:36）该关 Cursor 了。

Arvid [(01:58:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=7118) [inaudible 01:58:38].  
Arvid（01:58:38）[听不清]。

Lex [(01:58:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=7119) Thank you. So is it time to shut down Cursor?  
Lex（01:58:39）谢谢。所以真该关 Cursor 吗？

Michael [(01:58:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=7121) I think this space is a little bit different from past software spaces over the 2010s, where I think that the ceiling here is really, really, really incredibly high. So I think that the best product in three to four years will just be soon much more useful than the best product today. You can wax poetic about moats this and brand that and this is our advantage, but I think in the end, just if you stop innovating on the product, you will lose. That’s also great for startups, that’s great for people trying to enter this market because it means you have an opportunity to win against people who have lots of users already by just building something better. So I think over the next few years, it’s just about building the best product, building the best system. That both comes down to the modeling engine side of things, and it also comes down to the editing experience.  
Michael（01:58:41）这领域和 2010 年代很多软件不同，天花板极高。三四年后的最好产品会比今天好用得多。护城河、品牌你可以吟诗，但最终停创新就会输。这对创业也好：已有大量用户也能被更好的产品打败。未来几年就是最好产品、最好系统——建模引擎与编辑体验两边。

Aman [(01:59:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=7177) Yeah, I think most of the additional value from Cursor versus everything else out there is not just integrating the new model fast like o1. It comes from all of the depth that goes into these custom models that you don’t realize are working for you in every facet of the product, as well as the really thoughtful UX with every single feature.  
Aman（01:59:37）Cursor 相对别家的额外价值，不只像接 o1 那样快上新模型；而是你没意识到的、产品各处都在干活的定制模型深度，以及每个功能都很讲究的 UX。

## Synthetic data  
## 合成数据

Lex [(02:00:01)](https://youtube.com/watch?v=oFfVt3S51T4&t=7201) All right. From that profound answer-  
Lex（02:00:01）好。从刚才深刻的回答——

Lex [(02:00:01)](https://youtube.com/watch?v=oFfVt3S51T4&t=7201) All right, from that profound answer, let’s descend back down to the technical. You mentioned you have a taxonomy of synthetic data.  
Lex（02:00:01）好，从深刻回答回到技术。你提到合成数据有分类法。

Aman [(02:00:08)](https://youtube.com/watch?v=oFfVt3S51T4&t=7208) Oh yeah.  
Aman（02:00:08）对。

Lex [(02:00:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=7209) Can you please explain?  
Lex（02:00:09）能讲讲吗？

Aman [(02:00:10)](https://youtube.com/watch?v=oFfVt3S51T4&t=7210) Yeah, I think there are three main kinds of synthetic data. So what is synthetic data, first? So there’s normal data, like non-synthetic data, which is just data that’s naturally created, i.e. usually it’ll be from humans having done things. So from some human process you get this data. Synthetic data, the first one would be distillation. So having a language model, output tokens or probability distributions over tokens, and then you can train some less capable model on this.  
Aman（02:00:10）合成数据大概三类。先啥叫合成？非合成就是自然产生，通常人做事留下。合成第一类：**蒸馏**——大模型输出 token 或 token 分布，再训较弱模型。

[(02:00:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=7245) This approach is not going to get you a more capable model than the original one that has produced the tokens, but it’s really useful for if there’s some capability you want to elicit from some really expensive high-latency model. You can then distill that down into some smaller task-specific model.  
（02:00:45）这不会得到比Teacher更强的模型，但若想从贵、高延迟大模型里抽出某能力，可蒸馏成小任务专用模型。

[(02:01:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=7264) The second kind is when one direction of the problem is easier than the reverse. So a great example of this is bug detection, like we mentioned earlier, where it’s a lot easier to introduce reasonable-looking bugs than it is to actually detect them. And this is probably the case for humans too. And so what you can do, is you can get a model that’s not trained in that much data, that’s not that smart, to introduce a bunch of bugs and code. And then you can use that to then train… Use the synthetic data to train a model that can be really good at detecting bugs.  
（02:01:04）第二类是问题单向更易：**造**比**找**容易，bug 检测是例子；人也如此。可让不太强、数据不多的模型往代码里塞合理-looking bug，再用合成数据训擅找 bug 的模型。

[(02:01:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=7302) The last category I think is, I guess the main one that it feels like the big labs are doing for synthetic data, which is producing text with language models that can then be verified easily. So extreme example of this is if you have a verification system that can detect if language is Shakespeare level, and then you have a bunch of monkeys typing and typewriters. You can eventually get enough training data to train a Shakespeare-level language model.  
（02:01:42）第三类大概是实验室主路线：用 LM 生成文本，再**易验证**。极端例子：有系统能判是否莎士比亚级，再加无穷猴子打字，最终能训出莎士比亚级 LM。

[(02:02:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=7332) And I mean this is very much the case for math where verification is actually really, really easy for formal languages. And then what you can do, is you can have an okay model, generate a ton of rollouts, and then choose the ones that you know have actually proved the ground truth theorems, and train that further.  
（02:02:12）数学尤其如此：形式语言里验证很容易。中等模型狂采样 rollout，筛出真证出定理的再训。

[(02:02:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=7354) There’s similar things you can do for code with lead code like problems, where if you have some set of tests that you know correspond to if something passes these tests, it actually solved problem. You could do the same thing where you verify that it’s passed the test and then train the model in the outputs that have passed the tests.  
（02:02:34）代码 LeetCode 类题类似：有测试集能判定通过即解题，就筛通过测试的输出再训。

[(02:02:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=7371) I think it’s going to be a little tricky getting this to work in all domains, or just in general. Having the perfect verifier feels really, really hard to do with just open-ended miscellaneous tasks. You give the model or more long horizon tasks, even in coding.  
（02:02:51）泛化到所有领域会难；开放任务要完美验证器很难，代码里长程任务也是。

Lex [(02:03:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=7389) That’s because you’re not as optimistic as Arvid. But yeah, so yeah, that third category requires having a verifier.  
Lex（02:03:09）因为你没 Arvid 那么乐观。第三类确实要验证器。

Aman [(02:03:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=7397) Verification, it feels like it’s best when you know for a fact that it’s correct. And then it wouldn’t be like using a language model to verify. It would be using tests or formal systems.  
Aman（02:03:17）验证最好是你**确定**对错；那就不是用 LM 验，而是用测试或形式系统。

Michael [(02:03:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=7408) Or running the thing too. Doing the human form of verification, where you just do manual quality control.  
Michael（02:03:28）或跑起来。人验：人工质检。

Aman [(02:03:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=7414) Yeah.  
Aman（02:03:34）对。

Michael [(02:03:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=7414) But the language model version of that, where it’s running the thing and it actually understands the output.  
Michael（02:03:34）LM 版是跑起来且真理解输出。

Aman [(02:03:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=7419) Yeah. No, that’s-  
Aman（02:03:39）对，那是——

Michael [(02:03:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=7421) I’m sure it’s somewhere in between.  
Michael（02:03:41）肯定介于其间。

Aman [(02:03:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=7421) Yeah. I think that’s the category that is most likely to result in massive gains.  
Aman（02:03:41）我觉得这类最可能带来巨大收益。

## RLHF vs RLAIF  
## RLHF 与 RLAIF

Lex [(02:03:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=7428) What about RL with feedback side RLHF versus RLAIF? What’s the role of that in getting better performance on the models?  
Lex（02:03:48）RLHF 对 RLAIF？在提模型性能上角色？

Aman [(02:04:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=7440) Yeah. So RLHF is when the reward model you use is trained from some labels you’ve collected from humans giving feedback. I think this works if you have the ability to get a ton of human feedback for this kind of task that you care about.  
Aman（02:04:00）RLHF 是奖励模型用人标反馈训。你若能为目标任务搞海量人类反馈就管用。

[(02:04:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=7461) RLAIF is interesting because you’re depending on… This is actually, it’s depending on the constraint that verification is actually a decent bit easier than generation. Because it feels like, okay, what are you doing? Are you using this language model to look at the language model outputs and then prove the language model? But no, it actually may work if the language model has a much easier time verifying some solution than it does generating it. Then you actually could perhaps get this kind of recursive loop. But I don’t think it’s going to look exactly like that.  
（02:04:21）RLAIF 有趣在依赖「验证比生成容易得多」。听起来像 LM 看 LM 输出再证 LM？但若验比生容易得多，也许能递归循环。但不会像字面那么直。

[(02:04:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=7496) The other thing you could do, that we kind of do, is a little bit of a mix of RLAIF and RLHF, where usually the model is actually quite correct and this is the case of precursor tap picking between two possible generations of what is the better one. And then it just needs a little bit of human nudging with only on the order 50, 100 examples to align that prior the model has with exactly with what you want.  
（02:04:56）我们有点像混合 RLAIF+RLHF：常是模型已较对，比如 **Cursor Tab** 二选一哪条更好，只需几十到百条人标微调，把模型先验对齐你要的。

[(02:05:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=7529) It looks different than I think normal RLHF where you’re usually training these reward models in tons of examples.  
（02:05:29）和典型 RLHF（海量样本训奖励模型）不太一样。

## Fields Medal for AI  
## AI 与菲尔兹奖

Lex [(02:05:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=7535) What’s your intuition when you compare generation and verification or generation and ranking? Is ranking way easier than generation?  
Lex（02:05:35）生成 vs 验证、生成 vs 排序，直觉？排序比生成容易得多？

Aman [(02:05:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=7545) My intuition would just say, yeah, it should be. This is going back to… Like, if you believe P does not equal NP, then there’s this massive class of problems that are much, much easier to verify given proof, than actually proving it.  
Aman（02:05:45）直觉是应该。回到若信 P≠NP，一大类问题给定证明验证比找证明容易得多。

Lex [(02:06:03)](https://youtube.com/watch?v=oFfVt3S51T4&t=7563) I wonder if the same thing will prove P not equal to NP or P equal to NP.  
Lex（02:06:03）不知同一件事会不会证明 P≠NP 或 P=NP。

Arvid [(02:06:10)](https://youtube.com/watch?v=oFfVt3S51T4&t=7570) That would be really cool.  
Arvid（02:06:10）那会超酷。

Lex [(02:06:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=7571) That’d be a whatever Field’s Medal by AI. Who gets the credit? Another the open philosophical question.  
Lex（02:06:11）那就是 AI 拿菲尔兹奖之类。功劳归谁？又一个开放哲学问题。

Michael [(02:06:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=7579) Whoever prompted it.  
Michael（02:06:19）谁写的 prompt。

Sualeh [(02:06:24)](https://youtube.com/watch?v=oFfVt3S51T4&t=7584) I’m actually surprisingly curious what a good bet for one AI will get the Field’s Medal will be. I actually don’t have-  
Sualeh（02:06:24）我好奇「AI 拿菲尔兹奖」的好赌注该押多少。我其实没有——

Michael [(02:06:31)](https://youtube.com/watch?v=oFfVt3S51T4&t=7591) Isn’t this Aman’s specialty?  
Michael（02:06:31）这不是 Aman 专业吗？

Sualeh [(02:06:33)](https://youtube.com/watch?v=oFfVt3S51T4&t=7593) I don’t know what Aman’s bet here is.  
Sualeh（02:06:33）不知 Aman 押什么。

Lex [(02:06:35)](https://youtube.com/watch?v=oFfVt3S51T4&t=7595) Oh, sorry, Nobel Prize or Field’s Medal first?  
Lex（02:06:35）抱歉，诺贝尔奖还是菲尔兹奖先？

Sualeh [(02:06:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=7597) Field’s Medal-  
Sualeh（02:06:37）菲尔兹——

Aman [(02:06:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=7598) Oh, Field’s Medal level?  
Aman（02:06:38）哦，菲尔兹奖级别？

Arvid [(02:06:39)](https://youtube.com/watch?v=oFfVt3S51T4&t=7599) Field’s Medal comes first, I think.  
Arvid（02:06:39）我觉得菲尔兹先。

Sualeh [(02:06:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=7601) [inaudible 02:06:41].  
Sualeh（02:06:41）[听不清]。

Lex [(02:06:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=7601) Field’s Medal comes first. Well, you would say that, of course.  
Lex（02:06:41）菲尔兹先。你当然会这么说。

Arvid [(02:06:44)](https://youtube.com/watch?v=oFfVt3S51T4&t=7604) But it’s also this isolated system you verify and…  
Arvid（02:06:44）但也是孤立系统可验证……

Lex [(02:06:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=7607) Sure.  
Lex（02:06:47）当然。

Sualeh [(02:06:48)](https://youtube.com/watch?v=oFfVt3S51T4&t=7608) I don’t even know if I-  
Sualeh（02:06:48）我都不知是否——

Arvid [(02:06:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=7609) You don’t need to do [inaudible 02:06:50].  
Arvid（02:06:49）不必[听不清]。

Aman [(02:06:50)](https://youtube.com/watch?v=oFfVt3S51T4&t=7610) I feel like I have much more to do there. It felt like the path to get to IMO was a little bit more clear. Because it already could get a few IMO problems and there was a bunch of low-hanging fruit, given the literature at the time, of what tactics people could take. I think I’m, one, much less versed in the space of theorem proving now. And two, less intuition about how close we are to solving these really, really hard open problems.  
Aman（02:06:50）我觉得那边事还多。IMO 路径当时更清晰：已能解几题，文献里战术低垂果实多。我现在定理证明领域生疏多了，对多接近那些极难开放问题也没直觉。

Lex [(02:07:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=7635) So you think you’ll be Field’s Medal first? It won’t be in physics or in-  
Lex（02:07:15）所以你觉得菲尔兹先？不会物理先？

Sualeh [(02:07:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=7640) Oh, 100%. I think that’s probably more likely. It is probably much more likely that it’ll get in. Yeah, yeah, yeah. Well I think it both to… I don’t know, BSD, which is a Birch and Swinnerton-Dyer conjecture, or [inaudible 02:07:33] iPods, or any one of these hard math problems are just actually really hard. It’s sort of unclear what the path to get even a solution looks like. We don’t even know what a path looks like, let alone [inaudible 02:07:47].  
Sualeh（02:07:20）百分百，更可能先进数学。BSD（Birch–Swinnerton-Dyer）或[听不清]之类极难题，路都不清，别说解。

Arvid [(02:07:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=7667) And you don’t buy the idea this is just like an isolated system and you can actually have a good reward system, and it feels like it’s easier to train for that.  
Arvid（02:07:47）你不信孤立系统+好奖励就容易训出来？

Aman [(02:07:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=7676) I think we might get Field’s Medal before AGI.  
Aman（02:07:56）我觉得菲尔兹奖可能比 AGI 先。

Sualeh [(02:07:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=7679) I mean, I’d be very happy. I’d be very happy. But I don’t know if I… I think 2028, 2030.  
Sualeh（02:07:59）我会很开心。我猜 2028、2030。

Lex [(02:07:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=7679) For Field’s Medal?  
Lex（02:07:59）指菲尔兹奖？

Sualeh [(02:08:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=7689) Field’s Medal.  
Sualeh（02:08:09）菲尔兹奖。

Lex [(02:08:11)](https://youtube.com/watch?v=oFfVt3S51T4&t=7691) All right. It feels like forever from now, given how fast things have been going.  
Lex（02:08:11）好。事发展这么快，却感觉还很远。

## Scaling laws  
## 缩放定律

[(02:08:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=7697) Speaking of how fast things have been going, let’s talk about scaling laws. So for people who don’t know, maybe it’s good to talk about this whole idea of scaling laws. What are they, where’d you think stand, and where do you think things are going?  
（02:08:17）说到速度快，谈缩放定律。不懂的人先听概念：是什么、现状、往哪走？

Aman [(02:08:34)](https://youtube.com/watch?v=oFfVt3S51T4&t=7714) I think it was interesting. The original scaling laws paper by open AI was slightly wrong. Because I think of some issues they did with learning right schedules. And then Chinchilla showed a more correct version. And then from then people have again deviated from doing the compute optimal thing. Because people start now optimizing more so for making the thing work really well given an inference budget.  
Aman（02:08:34）有意思：OpenAI 原始缩放定律论文略有问题，学习率日程等；Chinchilla 更对。后来人们又偏离算力最优，因为更在意**推理预算**下要好用。

[(02:08:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=7739) And I think there are a lot more dimensions to these curves than what we originally used, of just compute number of parameters and data. Like inference compute is the obvious one. I think context length is another obvious one. So let’s say you care about the two things of inference compute and then context window, maybe the thing you want to train, is some kind of SSM. Because they’re much, much cheaper and faster at super, super long context. And even if, maybe it was 10 X more scaling properties during training, meaning you spend 10 X more compute to train the thing to get the same level of capabilities, it’s worth it. Because you care most about that inference budget for really long context windows. So it’ll be interesting to see how people play with all these dimensions.  
（02:08:59）曲线维度也比当初「算力、参数、数据」多：推理算力、上下文长度都明显。若最在意推理与超长上下文，也许该训 SSM 等，超长上下文便宜快得多；即便训练多花 10× 算力换同等能力也值，因为你在乎推理。看大家怎么调这些旋钮。

Lex [(02:09:47)](https://youtube.com/watch?v=oFfVt3S51T4&t=7787) So yeah, I mean you speak to the multiple dimensions, obviously. The original conception was just looking at the variables of the size of the model as measured by parameters, and the size of the data as measured by the number of tokens, and looking at the ratio of the two.  
Lex（02:09:47）你提到多维。最初就是参数规模与 token 数据规模及二者比例。

Aman [(02:09:59)](https://youtube.com/watch?v=oFfVt3S51T4&t=7799) Yeah.  
Aman（02:09:59）对。

Lex [(02:10:00)](https://youtube.com/watch?v=oFfVt3S51T4&t=7800) And it’s kind of a compelling notion that there is a number, or at least a minimum. And it seems like one was emerging. Do you still believe that there is a kind of bigger is better?  
Lex（02:10:00）有种迷人想法：存在某个数或下限，似乎在浮现。你还信「越大越好」吗？

Aman [(02:10:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=7815) I mean I think bigger is certainly better for just raw performance.  
Aman（02:10:15）更大肯定对原始性能更好。

Sualeh [(02:10:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=7821) And raw intelligence.  
Sualeh（02:10:21）原始智能也是。

Aman [(02:10:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=7822) And raw intelligence. I think the path that people might take, is… I’m particularly bullish on distillation. And how many knobs can you turn to, if we spend a ton, ton of money on training, get the most capable cheap model. Really, really caring as much as you can. Because the naive version of caring as much as you can about inference time compute, is what people have already done with the Llama models. Or just over-training the shit out of 7B models on way, way, way more tokens than is essential optimal.  
Aman（02:10:22）路径可能是……我极看好蒸馏：砸大钱训练，能拧多少旋钮得到**最能干又便宜**的模型。朴素在乎推理算力就是 Llama 那路：7B 用远超 Chinchilla 最优的 token 死命过训。

[(02:10:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=7854) But if you really care about it, maybe the thing to do is what Gamma did, which is let’s not just train on tokens, let’s literally train on minimizing the KL divergence with the distribution of gemma 27B, right? So knowledge distillation there. And you’re spending the compute of literally training this 27 billion parameter model on all these tokens, just to get out this, I don’t know, smaller model.  
（02:10:54）真在乎也许该像 Gemma 路线：不只训 token，而是最小化与 Gemma 27B 分布的 KL，知识蒸馏。等于烧训练 27B 同款算力，只为挤出更小模型。

Lex [(02:11:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=7880) And the distillation gives you just a faster model, smaller means faster.  
Lex（02:11:20）蒸馏就是更小更快？

Aman [(02:11:23)](https://youtube.com/watch?v=oFfVt3S51T4&t=7883) Yeah. Distillation in theory is, I think, getting out more signal from the data that you’re training on. And it’s perhaps another way of getting over, not completely over, but partially helping with the data wall. Where you only have so much data to train on, let’s train this really, really big model on all these tokens and we’ll distill it into this smaller one. And maybe we can get more signal per token for this much smaller model than we would’ve originally if we trained it.  
Aman（02:11:23）对。蒸馏理论上从同样数据榨更多信号，部分缓解数据墙：数据有限就先训巨大再蒸馏小模型，小模型每 token 信号也许更高。

Lex [(02:11:51)](https://youtube.com/watch?v=oFfVt3S51T4&t=7911) So if I gave you $10 trillion, how would you spend it? I mean you can’t buy an island or whatever. How would you allocate it in terms of improving the big model versus maybe paying for HF in the RLHF? Or-  
Lex（02:11:51）给你十万亿美元怎么花？不能买岛。多大比例投大模型 vs RLHF 人类反馈？

Aman [(02:12:09)](https://youtube.com/watch?v=oFfVt3S51T4&t=7929) Yeah, yeah. I think there’s a lot of these secrets and details about training these large models that I just don’t know, and are only privy to the large labs. And the issue is, I would waste a lot of that money if I even attempted this, because I wouldn’t know those things. Suspending a lot of disbelief and assuming you had the know- how, or if you’re saying you have to operate with the limited information you have now-  
Aman（02:12:09）大模型训练很多秘密只有大实验室懂；我若乱花会浪费很多钱。若假设你全知——或信息有限下——

Lex [(02:12:37)](https://youtube.com/watch?v=oFfVt3S51T4&t=7957) No, no, no. Actually, I would say you swoop in and you get all the information, all the little heuristics, all the little parameters, all the parameters that define how the thing is trained.  
Lex（02:12:37）不，假设你空降拿到全部信息、启发式、超参、训练定义。

Aman [(02:12:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=7969) Mm-hmm.  
Aman（02:12:49）嗯。

Lex [(02:12:50)](https://youtube.com/watch?v=oFfVt3S51T4&t=7970) If we look in how to invest money for the next five years in terms of maximizing what you called raw intelligence-  
Lex（02:12:50）若看未来五年投资以最大化你说的原始智能——

Sualeh [(02:12:57)](https://youtube.com/watch?v=oFfVt3S51T4&t=7977) I mean, isn’t the answer really simple? You just try to get as much compute as possible. At the end of the day all you need to buy, is the GPUs. And then the researchers can find all… You can tune whether you want to pre-train a big model or a small model.  
Sualeh（02:12:57）答案很简单吧：尽量多买算力。说到底买 GPU；研究员再调预训练大还是小。

Aman [(02:13:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=7995) Well this gets into the question of are you really limited by compute and money, or are you limited by these other things?  
Aman（02:13:15）这就变成：瓶颈真是算力钱，还是别的？

Sualeh [(02:13:22)](https://youtube.com/watch?v=oFfVt3S51T4&t=8002) I’m more privy to Arvid’s belief that we’re sort of idea-limited, but there’s always that like-  
Sualeh（02:13:22）我更倾向 Arvid：我们想法受限，但总有那种——

Arvid [(02:13:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=8007) But if you have a lot of compute, you can run a lot of experiments.  
Arvid（02:13:27）但算力多能跑很多实验。

Lex [(02:13:32)](https://youtube.com/watch?v=oFfVt3S51T4&t=8012) So you would run a lot of experiments versus use that compute to trend a gigantic model?  
Lex（02:13:32）所以多跑实验 vs 用算力训巨型模型？

Arvid [(02:13:38)](https://youtube.com/watch?v=oFfVt3S51T4&t=8018) I would, but I do believe that we are limited in terms of ideas that we have.  
Arvid（02:13:38）我会，但我信想法有限。

Aman [(02:13:44)](https://youtube.com/watch?v=oFfVt3S51T4&t=8024) I think yeah, because even with all this compute and all the data you could collect in the world, I think you really are ultimately limited by not even ideas, but just really good engineering. Even with all the capital in the world, would you really be able to assemble… There aren’t that many people in the world who really can make the difference here. And there’s so much work that goes into research that is just pure, really, really hard engineering work. As a very hand-wavy example, if you look at the original Transformer paper, how much work was joining together a lot of these really interesting concepts embedded in the literature, versus then going in and writing all the codes, maybe the CUDA kernels, maybe whatever else. I don’t know if it ran them GPUs or TPUs. Originally such that it actually saturated the GPU performance. Getting GNOME Azure to go in and do all this code. And GNOME is probably one of the the best engineers in the world.  
Aman（02:13:44）对，即便算力数据无限，最终瓶颈可能不是想法而是**工程**。全世界能改变局面的人没那么多；研究里大量是纯硬工程。随手举例：Transformer 原文多少工作是拼文献概念 vs 写代码 CUDA 核、喂满 GPU？口误 GNOME Azure 可能指 Noam Shazeer 等顶尖工程师。

[(02:14:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=8083) Or maybe going a step further, like the next generation of models, having these things… Like getting model parallelism to work, and scaling it on thousands of, or maybe tens of thousands of V100s, which I think GBDE-III may have been. There’s just so much engineering effort that has to go into all of these things to make it work. If you really brought that cost down to maybe not zero, but just made it 10 X easier, made it super easy for someone with really fantastic ideas, to immediately get to the version of the new architecture they dreamed up, that is getting 50, 40% utilization on their GPUs, I think that would just speed up research by a ton.  
（02:14:43）再进一步：下一代模型并行、成千上万 V100 上扩（口误 GBDE-III 可能指某项目）。工程浩大。若把成本降到接近零或 10× 更容易，有想法的人立刻能把新架构跑到 GPU 40–50% 利用率，研究会快很多。

Sualeh [(02:15:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=8127) I mean I think if you see a clear path to improvement, you should always take the low-hanging fruit first, right? I think probably OpenAI and all the other labs that did the right thing to pick off the low-hanging fruit. Where the low-hanging fruit is like, you could scale up to a GPT-4.25 scale and you just keep scaling, and things keep getting better. And as long as… There’s no point of experimenting with new ideas when everything is working. And you should sort of bang on and to try to get as much as much juice out of the possible. And then maybe when you really need new ideas for… I think if you’re spending $10 trillion, you probably want to spend some… Then actually reevaluate probably your idea a little bit at that point.  
Sualeh（02:15:27）有明显改进路径就先摘低垂果实。OpenAI 等实验室先扩 GPT-4 量级一路 scale 更好，路通时没必要乱试新想法；先榨干。真要花十万亿时再重新评估想法。

Aman [(02:16:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=8175) I think all of us believe new ideas are probably needed to get all the way there to AGI. And all of us also probably believe there exist ways of testing out those ideas at smaller scales, and being fairly confident that they’ll play out. It’s just quite difficult for the labs in their current position to dedicate their very limited research and engineering talent to exploring all these other ideas, when there’s this core thing that will probably improve performance for some decent amount of time.  
Aman（02:16:15）我们都信通往 AGI 需要新想法；也信小尺度可试且能外推。但实验室有限人手难全去探索旁路，因为主路还能涨一阵子。

## The future of programming  
## 编程的未来

Lex [(02:16:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=8216) But also, these big labs like winning. So they’re just going wild. Okay, so big question, looking out into the future: You’re now at the center of the programming world. How do you think programming, the nature of programming changes in the next few months, in the next year, in the next two years and the next five years, 10 years?  
Lex（02:16:56）大实验室也在赢，在狂飙。大问题：你们处在编程世界中心，未来数月、年、两年、五到十年，编程本质怎么变？

Michael [(02:17:20)](https://youtube.com/watch?v=oFfVt3S51T4&t=8240) I think we’re really excited about a future where the programmer is in the driver’s seat for a long time. And you’ve heard us talk about this a little bit, but one that emphasizes speed and agency for the programmer and control. The ability to modify anything you want to modify, the ability to iterate really fast on what you’re building. And this is a little different, I think, than where some people are jumping to in the space, where I think one idea that’s captivated people, is can you talk to your computer? Can you have it build software for you? As if you’re talking to an engineering department or an engineer over Slack. And can it just be this sort of isolated text box? And part of the reason we’re not excited about that, is some of the stuff we’ve talked about with latency, but then a big piece, a reason we’re not excited about that, is because that comes with giving up a lot of control.  
Michael（02:17:20）我们兴奋的是程序员长期**掌舵**：强调速度、能动性与控制——想改啥改啥，迭代极快。这和圈里有人跳到的方向不同：迷人想法是「跟电脑说话像跟工程部 Slack，孤立文本框就做完？」我们不兴奋，一部分是延迟问题，更大是那会放弃大量控制。

[(02:18:19)](https://youtube.com/watch?v=oFfVt3S51T4&t=8299) It’s much harder to be really specific when you’re talking in the text box. And if you’re necessarily just going to communicate with a thing like you would be communicating with an engineering department, you’re actually advocating tons of really important decisions to this bot. And this kind of gets at, fundamentally, what engineering is. I think that some people who are a little bit more removed from engineering might think of it as the spec is completely written out and then the engineers just come and they just implement. And it’s just about making the thing happen in code and making the thing exist. But I think a lot of the best engineering, the engineering we enjoy, involves tons of tiny micro decisions about what exactly you’re building, and about really hard trade-offs between speed and cost and just all the other things involved in a system. As long as humans are actually the ones designing the software and the ones specifying what they want to be built, and it’s not just like company run by all AIs, we think you’ll really want the human in a driver’s seat dictating these decisions.  
（02:18:19）文本框里很难极度具体；若沟通方式像对工程部，等于把大量关键决策交给 bot。工程本质在此：外行可能以为规格写满工程师只实现；我们享受的好工程是无数微观决策与速度成本等权衡。只要还是人设计软件、人指定要建什么，不是全 AI 公司，你就想人掌舵定这些决策。

[(02:19:26)](https://youtube.com/watch?v=oFfVt3S51T4&t=8366) And so the jury’s still out on what that looks like. I think that one weird idea for what that could look like, is it could look like you can control the level of abstraction you view a code base at. And you can point at specific parts of a code base that… Like, maybe you digest a code base by looking at it in the form of pseudocode. And you can actually edit that pseudocode too, and then have changes get made down at the sort of formal programming level. And you can gesture at any piece of logic in your software component of programming. You keep the inflow text editing component of programming, you keep the control of, you can even go down into the code, you can go at higher levels of abstraction, while also giving you these big productivity gains.  
（02:19:26）具体长什么样陪审团未定。一个怪想法：你能控制看代码库的抽象层级；用伪代码消化库、编辑伪代码再下沉到正式代码；对任意逻辑做手势式指向。保留文本编辑流、保留钻进代码与高抽象切换，同时巨大提效。

Lex [(02:20:14)](https://youtube.com/watch?v=oFfVt3S51T4&t=8414) It’d be nice if you can go up and down the abstraction stack.  
Lex（02:20:14）能在抽象栈上下穿梭会很好。

Michael [(02:20:18)](https://youtube.com/watch?v=oFfVt3S51T4&t=8418) Yeah. And there are a lot of details to figure out there that’s sort of like a fuzzy idea. Time will tell if it actually works. But these principles of control and speed in the human in the driver’s seat, we think are really important. We think for some things like Arvid mentioned before, for some styles of programming, you can hand it off chatbot-style. If you have a bug that’s really well specified. But that’s not most of programming, and that’s also not most of the programming we think a lot of people value.  
Michael（02:20:18）细节很多，现在还模糊，时间检验。但控制、速度、人掌舵我们信很重要。有些场景如 Arvid 说规格很清的 bug 可以聊天机器人式交出去；但那不是编程的大部分，也不是大家最看重的那部分。

Lex [(02:20:43)](https://youtube.com/watch?v=oFfVt3S51T4&t=8443) What about the fundamental skill of programming? There’s a lot of people, like young people right now kind of scared, because they love programming, but they’re scared about, “Will I be able to have a future if I pursue this career path?” Do you think the very skill of programming will change fundamentally?  
Lex（02:20:43）编程基本功呢？很多年轻人爱编程却怕选这行没未来。编程技能会根本变吗？

Michael [(02:21:04)](https://youtube.com/watch?v=oFfVt3S51T4&t=8464) I actually think this is a really, really exciting time to be building software. We remember what programming was like in 2013, 2012, whatever it was. And there was just so much more cruft and boilerplate and looking up something really gnarly. And that stuff still exists. It’s definitely not at zero. But programming today is way more fun than back then. It’s like we’re really getting down to the delight concentration. And all the things that really draw people to programming, for instance, this element of being able to build things really fast and speed and also individual control, all those are just being turned up a ton.  
Michael（02:21:04）我觉得现在做软件超兴奋。我们记得 2012、2013 编程多啰嗦、样板、查恶心文档；现在还有，但好玩多了，像在提纯「乐趣浓度」。吸引人编程的快建、速度、个人掌控都在放大。

[(02:21:49)](https://youtube.com/watch?v=oFfVt3S51T4&t=8509) And so I think it’s going to be a really, really fun time for people who build software. I think that the skills will probably change too. I think that people’s taste and creative ideas will be magnified. And it will be maybe less, a little bit, about boilerplate text editing. Maybe even a little bit less about carefulness, which I think is really important today if you’re a programmer. I think it’ll be a lot more fun.  
（02:21:49）做软件的人会很好玩。技能也会变：品味与创意被放大；少一点点纯敲样板；也许少一点点当下很重要的「小心」——整体更有趣。

Lex [(02:22:13)](https://youtube.com/watch?v=oFfVt3S51T4&t=8533) What do you guys think?  
Lex（02:22:13）你们呢？

Arvid [(02:22:15)](https://youtube.com/watch?v=oFfVt3S51T4&t=8535) I agree. I’m very excited to be able to change… One thing that happened recently, was we wanted to do a relatively big migration to our code base. We were using AsyncLocalStorage in Node.js, which is known to be not very performant, and we wanted to migrate to a context object. And this is a big migration and affects the entire code base. [inaudible 02:22:38] and I spent, I don’t know, five days working through this, even with today’s AI tools. And I am really excited for a future where I can just show a couple of examples and then the AI applies that to all of the locations. And then it highlights, “Oh, this is a new example, what should I do?” And then I show exactly what to do there. And then that can be done in 10 minutes. And then you can iterate much, much faster. Then you don’t have to think as much upfront and stand at the blackboard and think, “Exactly how are we going to do this, because the cost is so high?” But you can just try something first and you realize, “Oh, this is not actually exactly what I want.” And then you can change it instantly again after. And so yeah, I think being a programmer in the future is going to be a lot of fun.  
Arvid（02:22:15）同意。最近我们要大迁移：Node 里 AsyncLocalStorage 性能差，要迁到 context 对象，动全库。[听不清]我花了大概五天，即便有今天的 AI。我期待未来给几个例子 AI 就铺到所有位置；遇到新情况高亮问「咋办？」我示范，十分钟搞定，再更快迭代。不必先黑板想清「成本太高」；先试再改。未来编程会很好玩。

Aman [(02:23:26)](https://youtube.com/watch?v=oFfVt3S51T4&t=8606) Yeah, I really like that point about… It feels like a lot of the time with programming, there are two ways you can go about it. One is you think really hard, carefully upfront about the best possible way to do it and then you spend your limited time of engineering to actually implement it. But I must refer just getting in the code and taking a crack at seeing how it lays out and then iterating really quickly on that. That feels more fun.  
Aman（02:23:26）我喜欢这点：编程两路，一是先想清楚最优再实现；另一是直接进代码试布局再快迭代，后者更.fun（口误 I must refer 应为 I much prefer）。

Lex [(02:23:55)](https://youtube.com/watch?v=oFfVt3S51T4&t=8635) Yeah, just speaking to generate the boilerplate, is great. So you just focus on the nuanced, difficult design decisions. Migration, I feel like this is a cool one. It seems like a larger language models is able to basically translate for one program language to another. Or translate, migrate in the general sense of what migrate is. But that’s in the current moment. So mean the fear has to do with, okay, as these models get better and better, then you’re doing less and less creative decisions. And is it going to kind of move to a place where you’re operating in the design space of natural language where natural language is the main programming language? And I guess I could ask that by way of advice. If somebody’s interested in programming now, what do you think they should learn? You guys started in some Java and I forget the… Oh, some PHP.  
Lex（02:23:55）对，生成样板很好，你就专注细难的设计决策。迁移也很酷，大模型像语言间翻译或广义迁移。但恐惧是：模型越好你越不做创意决策，会不会自然语言成主「编程语言」？顺带给建议：现在想学编程该学什么？你们起步 Java 还有……PHP？

Michael [(02:23:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=8636) PHP.  
Michael（02:23:56）PHP。

Arvid [(02:23:56)](https://youtube.com/watch?v=oFfVt3S51T4&t=8636) PHP.  
Arvid（02:23:56）PHP。

Michael [(02:24:53)](https://youtube.com/watch?v=oFfVt3S51T4&t=8693) Objective-C.  
Michael（02:24:53）Objective-C。

Lex [(02:24:54)](https://youtube.com/watch?v=oFfVt3S51T4&t=8694) Objective-C. There you go. I mean in the end, we all know JavaScript was going to win and not TypeScript. It’s going to be like vanilla JavaScript. It’s just going to eat the world and maybe live with PHP. And I mean it also brings up the question of, I think Don Knuth has this idea that some percent of the population is geeks, and there’s a particular kind of psychology in mind required for programming. And it feels like more and more that expands the kind of person that should be able to, can do great programming, might expand.  
Lex（02:24:54）Objective-C，行。说到底大家都知道会赢的是 JavaScript 不是 TypeScript，原味 JS 吃世界，也许和 PHP 共存。Knuth 说人口里有比例是 geek，编程要特定心理；感觉能做好编程的人群在扩大。

Aman [(02:25:32)](https://youtube.com/watch?v=oFfVt3S51T4&t=8732) I think different people do programming for different reasons. But I think the true, maybe the best programmers, are the ones that really love, just absolutely love programming. For example, there are folks on our team who literally when they get back from work, they go and then they boot up cursor and then they start coding on their side projects for the entire night. And they stay up until 3:00 a.m. doing that. And when they’re sad, they said, “I just really need to code.” And I think there’s that level of programmer where this obsession and love of programming, I think makes, really, the best programmers. And I think these types of people will really get into the details of how things work.  
Aman（02:25:32）人编程理由不同；最好那批是真正热爱编程。我们团队有人下班开 Cursor 做 side project 通宵到三点；难过就说「我需要写代码」。这种痴迷会钻进细节。

Lex [(02:26:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=8789) I guess the question I’m asking, that exact programmer, let’s think about that person. When the super tab, the super awesome praise be the tab succeeds, and you keep pressing tab-  
Lex（02:26:29）我问的是这种人：超强 Tab、神 Tab 成真，你一直按 Tab——

Sualeh [(02:26:42)](https://youtube.com/watch?v=oFfVt3S51T4&t=8802) That person in the team loves cursor tab more than anybody else, right?  
Sualeh（02:26:42）团队里这种人最爱 Cursor Tab，对吧？

Arvid [(02:26:45)](https://youtube.com/watch?v=oFfVt3S51T4&t=8805) Yeah. And it’s also not just… Pressing tab is just pressing tab. That’s the easy way to say it in the catchphrase. But what you’re actually doing when you’re pressing tab, is that you’re injecting intent all the time while you’re doing it. Sometimes you’re rejecting it, sometimes you’re typing a few more characters. And that’s the way that you’re sort of shaping the things that’s being created. And I think programming will change a lot to just, “What is it that you want to make?”  
Arvid（02:26:45）也不只是按 Tab—— slogan 这么说简单。按 Tab 时你在持续注入意图：有时拒绝，有时多打几个字，塑造生成物。编程会变成更多「你想做什么」。

Sualeh [(02:27:17)](https://youtube.com/watch?v=oFfVt3S51T4&t=8837) It’s sort of higher bandwidth. The communication to the computer just becomes higher and higher bandwidth as opposed to just typing as much lower bandwidth than communicating intent.  
Sualeh（02:27:17）带宽更高：与计算机沟通比纯打字高得多，那是在传意图。

Lex [(02:27:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=8847) I mean, this goes to your manifesto titled Engineering Genius. “We are an applied research lab building extraordinary productive human AI systems.” So speaking to this hybrid element.  
Lex（02:27:27）这接上你们宣言《Engineering Genius》：「我们是应用研究实验室，打造极高生产力的人机系统。」谈这种混合。

[(02:27:41)](https://youtube.com/watch?v=oFfVt3S51T4&t=8861)“To start, we’re building the engineer of the future, a human AI programmer that’s an order of magnitude more effective than any one engineer. This hybrid engineer will have effortless control over their code base and no low entropy keystrokes. They will iterate at the speed of their judgment, even in the most complex systems. Using a combination of AI and human ingenuity they will outsmart and out engineer the best pure AI systems. We are a group of researchers and engineers.  
（02:27:41）「首先，我们在打造未来的工程师——比任何单人工程师高效一个数量级的人机程序员。混合工程师将毫不费力掌控代码库，没有低熵击键；即便最复杂系统也能以判断速度迭代。结合 AI 与人类才智，他们将胜过最好的纯 AI 系统。我们是研究者与工程师群体。」

[(02:28:12)](https://youtube.com/watch?v=oFfVt3S51T4&t=8892) We build software and models to invent at the edge of what’s useful and what’s possible. Our work has already improved the lives of hundreds of thousands of programmers.”  
（02:28:12）「我们构建软件与模型，在有用与可能的边界上发明。我们的工作已改善数十万程序员的生活。」

[(02:28:21)](https://youtube.com/watch?v=oFfVt3S51T4&t=8901) And on the way to that, we’ll at least make programming more fun. So thank you for talking today.  
（02:28:21）「路上我们至少会让编程更有趣。谢谢今天来聊。」

Arvid [(02:28:26)](https://youtube.com/watch?v=oFfVt3S51T4&t=8906) Thank you.  
Arvid（02:28:26）谢谢。

Michael [(02:28:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=8907) Thanks for having us.  
Michael（02:28:27）谢谢邀请。

Aman [(02:28:27)](https://youtube.com/watch?v=oFfVt3S51T4&t=8907) Thank you.  
Aman（02:28:27）谢谢。

Sualeh [(02:28:28)](https://youtube.com/watch?v=oFfVt3S51T4&t=8908) Thank you.  
Sualeh（02:28:28）谢谢。

Lex [(02:28:29)](https://youtube.com/watch?v=oFfVt3S51T4&t=8909) Thanks for listening to this conversation with Michael, Sualeh, Arvid and Aman. To support this podcast. Please check out our sponsors in the description. And now let me leave you with a random, funny and perhaps profound programming code I saw on Reddit. Nothing is as permanent as a temporary solution that works. Thank you for listening and hope to see you next time.  
Lex（02:28:29）感谢收听与 Michael、Sualeh、Arvid、Aman 的对话。欢迎支持播客赞助商。最后用 Reddit 看到的一句随机、好笑又也许深刻的编程话收尾：**能用的临时方案，没有什么比它更永久。** 谢谢收听，下期见。

---

**双语稿完。** 英文逐行原文见 [📄 007 英文-only 转录稿](../../forum/technology/007-Lex-Fridman-Podcast-447-Cursor-Team-Full-Transcript-2026-04-05.md)。
