# Skill开发与Codex更新

`/Users/yangzie/www/wdskills` 是所有自研Skill的唯一源码仓库。开发或修改完成后，在仓库根目录只需执行：

```bash
make update
```

它会自动扫描全部Skill、批量校验，并为新增Skill创建Codex符号链接。已有Skill通过链接直接读取仓库源码，因此保存修改后内容已经同步；运行`make update`主要用于校验和补齐新链接。

如果遇到同名真实目录、文件或错误链接，命令会报告`CONFLICT`并保留原内容，不会覆盖或删除。

更新成功后，新建一个Codex任务即可测试最新版本。

## 新建Skill

在仓库一级目录创建包含`SKILL.md`的文件夹：

```text
/Users/yangzie/www/wdskills/
└── my-new-skill/
    ├── SKILL.md
    ├── references/   # 可选
    ├── scripts/      # 可选
    └── assets/       # 可选
```

完成后仍然只运行`make update`。

## 排错命令

正常开发不需要这些命令：

```bash
make status    # 查看链接状态
make validate  # 只校验Skill
make sync      # 只补齐链接
make test      # 测试管理脚本
```

Git只管理`/Users/yangzie/www/wdskills`中的源码、脚本和文档；不要把整个`/Users/yangzie/.codex/skills`加入仓库。
