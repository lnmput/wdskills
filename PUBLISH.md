# npm 发布与更新指南 🚀

本项目封装了一个方便的自定义 Skills 交互式安装器，包名为 **`@lnmput/wdskills`**。为了方便后续维护，本指南详细记录了发布、更新的完整流程，以及在发布过程中可能遇到的常见问题和解决方案。

---

## 🛠️ 标准发布与更新流程

每当您在项目中**修改了已有的 Skill**，或者**新建了 Skill**，请按照以下三个步骤进行更新发布：

### 1. 修改版本号
打开项目根目录下的 `package.json`，修改 `"version"` 字段：
```json
"version": "1.0.1" // 将其递增（例如从 1.0.0 改为 1.0.1）
```
> **注意**：npm 不允许发布相同版本号的代码。每次发布前必须递增版本号。

### 2. 登录您的 npm 账号（若已登录可跳过）
在终端中执行官方源登录命令：
```bash
npm login --registry=https://registry.npmjs.org/
```
*按终端提示在浏览器中完成登录授权即可。*

### 3. 执行发布
因为 `@lnmput/wdskills` 是一个 Scope（作用域）包，发布时必须显式指定**公开权限** `--access public`，同时指定官方源地址：
```bash
npm publish --registry=https://registry.npmjs.org/ --access public
```

---

## 🔍 常见问题与解决方案 (Troubleshooting)

### 问题 1：双重认证 (2FA / OTP) 报错
* **错误现象**：`npm error 403 Forbidden - Two-factor authentication or granular access token with bypass 2fa enabled is required`
* **原因**：您的 npm 账号开启了双重验证，发布时需要动态验证码。
* **解决方案**：在您的手机身份验证器（如 Google Authenticator）中查看 npm 6 位动态验证码，运行以下命令（用实际验证码替换 `123456`）：
  ```bash
  npm publish --registry=https://registry.npmjs.org/ --access public --otp=123456
  ```

### 问题 2：只读镜像源报错 (npmmirror.com / Taobao)
* **错误现象**：`npm error 403 Forbidden` 且报错地址指向 `npmmirror.com` 或 `taobao.org`
* **原因**：本地终端默认的 npm 配置使用了国内的镜像源，镜像源是只读的，不允许直接发布。
* **解决方案**：在发布时显式指定官方 registry 参数：
  ```bash
  npm publish --registry=https://registry.npmjs.org/ --access public
  ```

### 问题 3：未登录错误 (ENEEDAUTH)
* **错误现象**：`npm error code ENEEDAUTH` / `This command requires you to be logged in.`
* **原因**：当前终端未登录 npm 账号。
* **解决方案**：先运行 `npm login --registry=https://registry.npmjs.org/` 完成登录。

### 问题 4：权限或找不到作用域错误 (E404 / E403 Scoped Error)
* **错误现象**：`npm error 404 Not Found - PUT https://registry.npmjs.org/@lnmput%2fwdskills - Not found`
* **原因**：当前终端登录的 npm 账号，不拥有 `lnmput` 这个作用域（Scope）的发布权限。
* **解决方案**：
  1. 运行 `npm whoami --registry=https://registry.npmjs.org/` 确认当前登录账号。
  2. 若当前账号是别人或另外的账号，如果需要以您的当前账号发布，请在 `package.json` 中将包名修改为 `@您的实际用户名/wdskills` 再发布。

### 问题 5：版本冲突错误 (EPUBLISHCONFLICT)
* **错误现象**：`You cannot publish over the previously published versions: 1.0.0.`
* **原因**：当前要发布的版本号与 npm 上已存在的版本号相同。
* **解决方案**：修改 `package.json` 中的 `"version"`，使其比线上已有版本大，例如改为 `1.0.1`。

---

## 📋 常用命令速查表

| 命令 | 用途 | 说明 |
| :--- | :--- | :--- |
| `npm whoami --registry=https://registry.npmjs.org/` | 检查当前登录的账号名 | 确认发布权限 |
| `npm login --registry=https://registry.npmjs.org/` | 登录 npm 账号 | 支持网页跳转授权 |
| `npm publish --registry=https://registry.npmjs.org/ --access public` | 发布更新（无 2FA） | 必须使用 `--access public` |
| `npm publish --registry=https://registry.npmjs.org/ --access public --otp=xxxxxx` | 发布更新（带 2FA 验证码） | 将 `xxxxxx` 替换为手机验证码 |
| `npx @lnmput/wdskills` | 用户端安装/运行工具 | 自动拉取已发布的安装器 |
| `npx @lnmput/wdskills@latest` | 用户端强制更新运行 | 确保获取最新版本 Skills |
