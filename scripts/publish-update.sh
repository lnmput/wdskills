#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo '用法: bash scripts/publish-update.sh [patch|minor|major|current|--dry-run]'
  echo '默认 patch；current 重试当前版本；--dry-run 仅预览当前版本的发布内容。'
  echo '需要 OTP 时，通过 npm_config_otp 环境变量传入。'
}

if (( $# > 1 )); then usage >&2; exit 1; fi
mode="${1:-patch}"
case "$mode" in
  patch|minor|major|current|--dry-run) ;;
  -h|--help) usage; exit 0 ;;
  *) usage >&2; exit 1 ;;
esac

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
command -v npm >/dev/null || { echo '请先安装 Node.js 和 npm。' >&2; exit 1; }
registry='https://registry.npmjs.org/'

if [[ "$mode" == --dry-run ]]; then
  echo '仅预览当前版本：不登录、不递增版本、不上传。'
  npm publish --dry-run --registry="$registry" --access public
  exit 0
fi

echo '检查 npm 官方源登录状态……'
if ! npm whoami --registry="$registry"; then
  echo '无法确认登录状态，启动 npm 登录；若网络异常，请修复后重试。'
  npm login --registry="$registry"
  npm whoami --registry="$registry"
fi

if [[ "$mode" != current ]]; then
  # 同步 package.json 与 lockfile，不创建 Git 提交或标签。
  npm version "$mode" --no-git-tag-version
fi

echo '发布到 npm 官方源……'
if npm publish --registry="$registry" --access public; then
  echo '发布成功。用户可运行 npx @lnmput/wdskills@latest 获取更新。'
else
  echo '发布失败，本地版本保留。请排查上方错误，确认该版本未发布后使用 current 重试。' >&2
  echo '重试命令: bash scripts/publish-update.sh current' >&2
  exit 1
fi
