---
title: "Claude Mythos Preview: Assessing Cybersecurity Capabilities"
source: "Anthropic"
source_url: "https://red.anthropic.com/2026/mythos-preview/"
author: ["Nicholas Carlini", "Newton Cheng", "Keane Lucas", "Michael Moore", "Milad Nasr", "Vinay Prabhushankar", "Winnie Xiao", "Evyatar Ben Asher", "Hakeem Angulu", "Jackie Bow", "Keir Bradwell", "Ben Buchanan", "Daniel Freeman", "Alex"]
date: "2026-04-07"
created_date: "2026-04-08"
category: "reading/notes/technology/ai-digital"
tags: ["Anthropic", "Claude Mythos Preview", "Cybersecurity", "Zero-day", "Vulnerability Discovery", "Exploitation", "Memory Safety", "AI Safety"]
---

# Claude Mythos Preview: Assessing Cybersecurity Capabilities 

## Summary / 概要 

Anthropic 发布了 Claude Mythos Preview，这是一款在计算机安全任务方面表现出惊人能力的通用语言模型。测试表明，该模型能够在人类指导下，在所有主要操作系统和浏览器中识别并利用零日漏洞（zero-day vulnerabilities）。尽管这些能力的出现是模型通用改进的下游结果，但 Anthropic 决定通过 Project Glasswing 限制其发布，以降低潜在风险。

---

## Bilingual Intensive Reading / 双语精读 

### Assessing Claude Mythos Preview’s cybersecurity capabilities 
### 评估 Claude Mythos Preview 的网络安全能力 

Earlier today we announced Claude Mythos Preview, a new general-purpose language model. This model performs strongly across the board, but it is strikingly capable at computer security tasks.  
今天早些时候，我们发布了 Claude Mythos Preview，这是一款全新的通用语言模型。该模型在各方面表现都很强劲，但在计算机安全任务方面的能力尤为惊人。 

This blog post provides technical details for researchers and practitioners who want to understand exactly how we have been testing this model, and what we have found over the past month.  
本博文为希望准确了解我们如何测试该模型以及我们在过去一个月中发现了什么的专业研究人员和从业者提供了技术细节。 

### The significance of Claude Mythos Preview for cybersecurity 
### Claude Mythos Preview 对网络安全的意义 

During our testing, we found that Mythos Preview is capable of identifying and then exploiting zero-day vulnerabilities in every major operating system and every major web browser when directed by a user.  
在测试过程中，我们发现 Mythos Preview 在用户指导下，能够识别并利用所有主要操作系统和主要 Web 浏览器中的零日漏洞。 

The exploits it constructs are not just run-of-the-mill stack-smashing exploits. In one case, Mythos Preview wrote a web browser exploit that chained together multiple different vulnerabilities to form a JIT heap spray.  
它构建的漏洞利用程序不仅仅是普通的栈溢出（stack-smashing）利用。在其中一个案例中，Mythos Preview 编写了一个 Web 浏览器漏洞利用程序，将多个不同的漏洞串联起来，形成了 JIT 堆喷射（JIT heap spray）。 

Non-experts can also leverage Mythos Preview to find and exploit sophisticated vulnerabilities. Engineers at Anthropic with no formal security training have asked Mythos Preview to find remote code execution (RCE) vulnerabilities in production software, and the model has successfully done so.  
非专业人士也可以利用 Mythos Preview 来发现和利用复杂的漏洞。Anthropic 的一些没有接受过正式安全培训的工程师曾要求 Mythos Preview 在生产软件中寻找远程代码执行（RCE）漏洞，模型成功做到了。 

These capabilities have emerged very quickly. Last month, we wrote that “Opus 4.6 is currently far better at identifying and fixing vulnerabilities than at exploiting them.” Our internal evaluations show that Mythos Preview has closed this gap.  
这些能力出现得非常快。上个月我们还写道：“Opus 4.6 目前在识别和修复漏洞方面远强于利用漏洞。”我们的内部评估显示，Mythos Preview 已经弥补了这一差距。 

We did not explicitly train Mythos Preview to have these capabilities. Rather, they emerged as a downstream consequence of general improvements in code, reasoning, and autonomy.  
我们并没有明确训练 Mythos Preview 具备这些能力。相反，它们是代码、推理和自主性方面通用改进的下游结果。 

Once the security landscape has reached a new equilibrium, we believe that powerful language models will benefit defenders more than attackers. But the transitional period may be tumultuous regardless.  
一旦安全格局达到新的平衡，我们相信强大的语言模型对防御者的益处将超过攻击者。但无论如何，过渡期可能会动荡不安。 

### Evaluating Claude Mythos Preview’s ability to find zero-days 
### 评估 Claude Mythos Preview 发现零日漏洞的能力 

Zero-day vulnerabilities—bugs that were not previously known to exist—allow us to address this limitation. If a language model can identify such bugs, we can be certain it is not because they previously appeared in its training data.  
零日漏洞（即以前未知的漏洞）使我们能够解决这一局限。如果语言模型能识别此类漏洞，我们可以确定这不是因为它之前出现在其训练数据中。 

The bugs we describe in this section are primarily memory safety vulnerabilities. This is for four reasons:  
我们在本节中描述的漏洞主要是内存安全漏洞。这有四个原因： 

1. “Pointers are real. They’re what the hardware understands.” Critical software systems are built in memory-unsafe languages like C and C++.  
1. “指针是真实的。它们是硬件所理解的。”关键软件系统是用 C 和 C++ 等内存不安全语言构建的。 

2. Because these codebases are so frequently audited, almost all trivial bugs have been found and patched. What’s left is the kind of bug that is challenging to find.  
2. 由于这些代码库被频繁审计，几乎所有琐碎的漏洞都已被发现并修复。剩下的是那种极具挑战性的漏洞。 

3. Memory safety violations are particularly easy to verify. Tools like Address Sanitizer perfectly separate real bugs from hallucinations.  
3. 内存安全违规特别容易验证。Address Sanitizer 等工具可以完美地将真实漏洞与幻觉区分开来。 

4. Our research team has extensive experience with memory corruption exploitation, allowing us to validate these findings more efficiently.  
4. 我们的研究团队在内存损坏漏洞利用方面拥有丰富的经验，使我们能够更有效地验证这些发现。 

### Finding zero-day vulnerabilities: Case Studies 
### 发现零日漏洞：案例研究 

#### A 27-year-old OpenBSD bug 
#### 一个存在了 27 年的 OpenBSD 漏洞 

Mythos Preview identified a vulnerability in the OpenBSD implementation of SACK (Selective Acknowledgement) that would allow an adversary to crash any OpenBSD host that responds over TCP.  
Mythos Preview 在 OpenBSD 的 SACK（选择性确认）实现中发现了一个漏洞，该漏洞允许对手使任何通过 TCP 响应的 OpenBSD 主机崩溃。 

The vulnerability is quite subtle. OpenBSD tracks SACK state as a singly linked list of holes. Mythos Preview found that if a single SACK block simultaneously deletes the only hole in the list and also triggers the append-a-new-hole path, the append writes through a pointer that is now NULL.  
该漏洞非常微妙。OpenBSD 将 SACK 状态跟踪为孔洞（holes）的单向链表。Mythos Preview 发现，如果单个 SACK 块同时删除列表中唯一的孔洞并触发追加新孔洞路径，追加操作将通过一个现已为 NULL 的指针进行写入。 

#### A 16-year-old FFmpeg vulnerability 
#### 一个存在了 16 年的 FFmpeg 漏洞 

Mythos Preview autonomously identified a 16-year-old vulnerability in one of FFmpeg's most popular codecs, H.264.  
Mythos Preview 自主识别了 FFmpeg 最受欢迎的编解码器之一 H.264 中一个存在了 16 年的漏洞。 

In addition to this vulnerability, Mythos Preview identified several other important vulnerabilities in FFmpeg after several hundred runs over the repository, at a cost of roughly ten thousand dollars in API credits.  
除了这个漏洞外，Mythos Preview 在对代码库进行数百次运行后，还发现了 FFmpeg 中的其他几个重要漏洞，API 积分成本约为 1 万美元。 

### Exploiting zero-day vulnerabilities 
### 利用零日漏洞 

#### Remote code execution in FreeBSD 
#### FreeBSD 中的远程代码执行 

Mythos Preview fully autonomously identified and then exploited a 17-year-old remote code execution vulnerability in FreeBSD that allows anyone to gain root on a machine running NFS.  
Mythos Preview 完全自主地识别并利用了 FreeBSD 中一个存在了 17 年的远程代码执行漏洞，该漏洞允许任何人在运行 NFS 的机器上获取 root 权限。 

When we say “fully autonomously”, we mean that no human was involved in either the discovery or exploitation of this vulnerability after the initial request to find the bug.  
当我们说“完全自主”时，我们的意思是，在最初要求寻找漏洞之后，没有任何人类参与该漏洞的发现或利用。 

### Suggestions for defenders today 
### 给当今防御者的建议 

1. **Use generally-available frontier models to strengthen defenses now.** Current frontier models, like Claude Opus 4.6, remain extremely competent at finding vulnerabilities.  
1. **立即使用通用的前沿模型来加强防御。** 当前的前沿模型（如 Claude Opus 4.6）在发现漏洞方面仍然非常出色。 

2. **Shorten patch cycles.** The N-day exploits we walked through were written fully autonomously, starting from just a CVE identifier and a git commit hash.  
2. **缩短补丁周期。** 我们演示的 N 日漏洞利用程序是完全自主编写的，仅从一个 CVE 标识符和一个 git 提交哈希开始。 

3. **Automate your technical incident response pipeline.** As vulnerability discovery accelerates, detection and response teams should expect a matching rise in incidents.  
3. **自动化您的技术事件响应流程。** 随着漏洞发现的加速，检测和响应团队应预料到事件也会相应增加。 

### Conclusion 
### 结论 

Given enough eyeballs, all bugs are shallow. Writing exploits is likewise a mostly mechanical process. It should be no surprise that language models are becoming extremely capable at these tasks.  
只要有足够的关注，所有漏洞都是浅显的。编写漏洞利用程序同样是一个基本机械的过程。语言模型在这些任务中变得极其强大也就不足为奇了。 

In the long run, we expect that defense capabilities will dominate. But the transitional period will likely be difficult.  
从长远来看，我们预计防御能力将占据主导地位。但过渡期可能会很艰难。 
