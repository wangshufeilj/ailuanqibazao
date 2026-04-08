# GitHub 上传指南

## 当前状态

根据 Git 状态，您的仓库有以下文件需要处理：

### 未跟踪的文件（新文件）
- `.cursor/rules/file-classification.mdc`
- `.cursor/rules/python-tech-stack.mdc`
- `reading/notes/game/001-Joe-Merrick-Serebii-Pokemon-Polygon-Interview-Reading-Notes-2026-03-11.md`
- `reading/notes/law/002-ATP-Oil-Gas-Corporation-Bankruptcy-Case-Notes-2026-03-10.md`
- `reading/notes/politics/domestic-policy/us-domestic/001-Trump-Florsheim-Shoe-Company-Lawsuit-Notes-2026-03-11.md`
- `reading/notes/science/002-Tiny-Long-Armed-Dinosaur-Rethink-Miniaturization-Notes-2026-03-11.md`
- `reading/notes/science/003-Strange-Reason-Bears-Attacking-People-Japan-Vox-Notes-2026-03-11.md`
- `social/posts/education/001-Former-TA-Advice-for-Students-Reddit-2026-03-11.md`
- `social/posts/education/002-Older-Student-College-Experience-Reddit-2026-03-11.md`

### 已修改的文件
- （示例：按 `git status` 实际输出为准）

---

## 上传步骤

### 步骤 1: 检查远程仓库配置

首先检查是否已配置 GitHub 远程仓库：

```bash
git remote -v
```

如果没有输出或没有 `origin`，需要添加远程仓库。

### 步骤 2: 添加远程仓库（如果还没有）

如果您还没有在 GitHub 上创建仓库，请先：
1. 登录 GitHub
2. 点击右上角的 "+" → "New repository"
3. 输入仓库名称（例如：`AI驱动整理乱七八糟` 或 `ai-organized-files`）
4. 选择 Public 或 Private
5. **不要**初始化 README、.gitignore 或 license（因为本地已有内容）
6. 点击 "Create repository"

然后添加远程仓库：

**使用 HTTPS（推荐新手）：**
```bash
git remote add origin https://github.com/你的用户名/仓库名.git
```

**使用 SSH（如果已配置 SSH 密钥）：**
```bash
git remote add origin git@github.com:你的用户名/仓库名.git
```

### 步骤 3: 添加文件到暂存区

添加所有新文件和修改：

```bash
git add .
```

或者只添加特定文件：

```bash
git add .cursor/rules/
git add reading/
git add social/
```

### 步骤 4: 提交更改

```bash
git commit -m "添加新的笔记和规则文件"
```

或者更详细的提交信息：

```bash
git commit -m "添加游戏、法律、政治、科学笔记和教育类社交媒体帖子

- 添加 Pokemon 相关阅读笔记
- 添加 ATP 石油天然气公司破产案例笔记
- 添加特朗普 Florsheim 鞋业公司诉讼笔记
- 添加恐龙研究和熊攻击研究笔记
- 添加教育类 Reddit 帖子
- 更新文件分类规则和 Python 技术栈规范"
```

### 步骤 5: 推送到 GitHub

**首次推送：**
```bash
git push -u origin main
```

如果您的默认分支是 `master`：
```bash
git push -u origin master
```

**后续推送：**
```bash
git push
```

---

## 常见问题

### 1. 认证问题

如果遇到认证错误，您需要：

**HTTPS 方式：**
- 使用 Personal Access Token（PAT）代替密码
- 在 GitHub Settings → Developer settings → Personal access tokens → Tokens (classic) 创建新 token
- 推送时使用 token 作为密码

**SSH 方式：**
- 配置 SSH 密钥
- 参考：https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### 2. 分支名称问题

如果提示分支不存在，先检查当前分支：

```bash
git branch
```

然后推送对应分支：

```bash
git push -u origin 你的分支名
```

### 3. 大文件问题

如果文件太大（超过 100MB），GitHub 会拒绝。建议：
- 使用 Git LFS（Large File Storage）
- 或者将大文件添加到 `.gitignore`，不上传到 Git

### 4. 冲突问题

如果远程仓库有您本地没有的更改，需要先拉取：

```bash
git pull origin main --rebase
```

然后再推送。

---

## 快速命令序列（如果已配置远程仓库）

```bash
# 1. 添加所有更改
git add .

# 2. 提交
git commit -m "添加新的笔记和规则文件"

# 3. 推送
git push
```

---

## 注意事项

1. **大文件**：根据项目规则，图片、视频等大文件不应提交到 Git。如果目录中有这些文件，请先检查 `.gitignore` 配置。

2. **敏感信息**：确保没有提交包含密码、API 密钥等敏感信息的文件。

3. **提交信息**：建议使用清晰、描述性的提交信息，方便后续查看历史。

---

## 需要帮助？

如果遇到问题，请提供：
- 错误信息
- `git status` 的输出
- `git remote -v` 的输出
