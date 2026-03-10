# GitHub 推送说明

本仓库已配置好 `.gitignore`、`LARGE_FILES_MANIFEST.md` 和 `README.md`。按以下步骤完成 Git 初始化并推送到 GitHub。

## 前置条件

1. **安装 Git**：若未安装，请从 [https://git-scm.com/download/win](https://git-scm.com/download/win) 下载并安装。
2. **GitHub 账户**：已有 GitHub 账号。

## 方式 A：手动创建仓库

### 1. 在 GitHub 网页创建仓库

1. 打开 [https://github.com/new](https://github.com/new)
2. 仓库名建议：`ai-content-organizer` 或 `AI-driven-organizer`
3. 选择**私有**（Private）
4. **不要**勾选「Initialize with README」
5. 点击 Create repository

### 2. 在本地执行 Git 命令

在项目根目录（`d:\AI驱动整理乱七八糟`）打开终端，执行：

**方式 1：使用 Python 脚本（推荐）**

```bash
python git_setup.py
```

然后手动执行推送命令：

```bash
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git branch -M main
git push -u origin main
```

**方式 2：直接使用 Git 命令**

```bash
git init
git add .
git status
git commit -m "Initial commit: AI 驱动整理项目（大文件仅存条目，见 LARGE_FILES_MANIFEST.md）"
git branch -M main
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```

将 `<你的用户名>` 和 `<仓库名>` 替换为实际值。

## 方式 B：使用 GitHub CLI (gh)

若已安装 [GitHub CLI](https://cli.github.com/)：

**方式 1：使用 Python 脚本（推荐）**

```bash
python git_setup.py
```

然后执行：

```bash
gh auth login
gh repo create ai-content-organizer --private --source=. --remote=origin --push
```

**方式 2：直接使用命令**

```bash
cd "d:\AI驱动整理乱七八糟"
git init
git add .
git commit -m "Initial commit: AI 驱动整理项目（大文件仅存条目，见 LARGE_FILES_MANIFEST.md）"
gh auth login
gh repo create ai-content-organizer --private --source=. --remote=origin --push
```

## 验证

推送成功后，`git status` 应显示 `nothing to commit, working tree clean`。在 GitHub 网页可看到 README、INDEX、规则文件及阅读笔记等，且不包含 images、videos、PDF 等大文件。
