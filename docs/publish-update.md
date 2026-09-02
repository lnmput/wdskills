# 一键发布更新

脚本依据 [PUBLISH.md](../PUBLISH.md)，用于将本仓库的 `@lnmput/wdskills` 更新发布到 npm。它与本地 Codex Skill 同步命令 `make update` 用途不同。

## 使用方法

需要安装 Node.js（本项目要求 16 或以上）及 npm，并具有该 npm 包的发布权限。先完成需要发布的 Skill 修改，再在项目根目录执行：

```bash
bash scripts/publish-update.sh
```

脚本会检查 npm 官方源登录状态，必要时启动 `npm login`；登录成功后执行 `npm version patch --no-git-tag-version`，最后通过官方源以公开权限发布。默认将补丁版本加一，例如 `1.0.4 → 1.0.5`。登录或发布要求浏览器授权、双重认证时，仍需按 npm 提示完成。

也可以从任意目录运行：

```bash
bash /Users/yangzie/www/wdskills/scripts/publish-update.sh
```

| 命令参数 | 用途 |
| --- | --- |
| 无参数或 `patch` | 补丁更新，例如 `1.0.4 → 1.0.5` |
| `minor` | 功能更新，例如 `1.0.4 → 1.1.0` |
| `major` | 主版本更新，例如 `1.0.4 → 2.0.0` |
| `current` | 发布当前版本，不递增；适用于已手动改版或发布失败后重试 |
| `--dry-run` | 预览当前版本发布内容，不登录、不改版本、不上传 |
| `--help` | 查看帮助 |

例如，发布次版本：

```bash
bash scripts/publish-update.sh minor
```

## 发布前预览

```bash
bash scripts/publish-update.sh --dry-run
```

该命令执行 `npm publish --dry-run`，检查当前版本的打包内容。它不模拟递增后的版本，也不能证明账号权限、OTP 或线上版本可用；npm 的生命周期钩子仍可能执行。正式发布使用当前工作区内容，包含未提交但符合 npm 打包规则的文件，请检查预览列表。

## 双重认证与失败重试

如果 npm 要求 OTP，可通过环境变量传入验证码：

```bash
npm_config_otp=123456 bash scripts/publish-update.sh
```

把 `123456` 替换为当前有效验证码。若版本已经递增、发布却失败，脚本保留本地版本，避免在网络结果不明确时自动回滚或重复发布。确认 npm 上该版本尚未发布后执行：

```bash
npm_config_otp=123456 bash scripts/publish-update.sh current
```

不需要 OTP 时省略环境变量。若该版本已经发布成功，无需重试；只有准备下一次更新时才再次递增版本。

登录、权限和版本冲突问题参见 [PUBLISH.md 的常见问题](../PUBLISH.md)。脚本始终指定 `https://registry.npmjs.org/`，避免向镜像源发布；任何步骤失败都会停止。

## 文件与 Git

版本更新由 npm 同步写入 `package.json` 和已有的 `package-lock.json`，不自动提交、创建标签或推送 Git。发布后请检查并自行提交版本文件。运行 `current` 不会同步版本文件，手动修改版本时需要自行保持两者一致。

## 脚本验证

```bash
python3 scripts/test-publish-update.py
```

验证使用临时目录和模拟 npm，覆盖默认发布、登录、失败重试、参数检查及预览，不访问 npm、不修改仓库版本。
