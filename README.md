# WdSkills Installer 🚀

这是一个为 Google Antigravity / Gemini Coder 打造的自定义 Skills 交互式安装与更新工具。通过它，你可以一键将该项目下的所有自定义 Skills 安装到全局或特定项目的工作区中，并在后续轻松更新。

---

## 📦 如何使用

### 1. 运行安装器
在本项目根目录下直接运行：
```bash
npx .
```

### 2. 交互式选项
- **选择安装位置**：
  - `Global (全局)`：安装到 `~/.gemini/config/skills/`，使所有项目/工作区中的 Agent 均可加载这些 Skills。
  - `Workspace (工作区)`：安装到当前项目的 `./.agents/skills/`，仅在当前项目生效。
- **选择安装的 Skills**：使用 **键盘上下键** 移动，**空格键** 勾选/取消勾选，**回车键** 确认安装。

---

## 🌐 共享给他人使用

你可以通过以下两种方式将这些 Skills 分享给团队或社区：

### 方式 A：直接通过 GitHub 运行（最简单，免发布）
如果你将该项目上传到了公共 GitHub 仓库（例如 `github.com/your-username/wdskills`），其他人无需下载代码，直接在他们的终端运行以下命令即可：
```bash
npx github:your-username/wdskills
```
*提示：后续当你在 GitHub 上更新了 Skills 之后，他们再次运行该命令，即可自动拉取最新代码并覆盖更新本地 Skills。*

### 方式 B：发布到 npm 注册表
1. 修改 `package.json` 中的 `"name"` 字段为你的包名（如 `wdskills` 或你的 Scope 包名 `@your-scope/wdskills`）。
2. 在项目根目录执行发布：
   ```bash
   npm publish --access public
   ```
3. 其他人只需运行：
   ```bash
   npx @lnmput/wdskills
   ```
   *提示：需要更新时，运行 `npx @lnmput/wdskills@latest` 即可获取最新版本并覆盖更新。*

---

## 🛠️ 项目结构
```text
.
├── bin/
│   └── cli.js                     # 交互式安装器脚本
├── extract-product-detail-json/   # 自定义 Skill A
│   └── SKILL.md
├── korean-fashion-translator/     # 自定义 Skill B
│   └── SKILL.md
└── package.json                   # 模块配置
```
