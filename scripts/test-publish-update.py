#!/usr/bin/env python3
"""离线检查发布流程，不调用真实 npm。"""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

with tempfile.TemporaryDirectory(prefix="wdskills-publish-") as directory:
    root = Path(directory)
    (root / "scripts").mkdir()
    script = root / "scripts/publish-update.sh"
    shutil.copyfile(Path(__file__).with_name("publish-update.sh"), script)
    npm = root / "npm"
    npm.write_text('''#!/usr/bin/env bash
echo "$PWD|$*" >> "$CALL_LOG"
case "$1" in
  whoami) [[ "${NEEDS_LOGIN:-0}" == 0 || -f "$LOGIN_MARK" ]] ;;
  login) [[ "${FAIL_LOGIN:-0}" == 0 ]] || exit 1; touch "$LOGIN_MARK" ;;
  version) exit "${FAIL_VERSION:-0}" ;;
  publish) exit "${FAIL_PUBLISH:-0}" ;;
esac
''')
    npm.chmod(0o755)
    log = root / "calls"
    mark = root / "logged-in"
    registry = "--registry=https://registry.npmjs.org/"
    whoami = f"whoami {registry}"
    publish = f"publish {registry} --access public"

    def check(args, expected, code=0, **flags):
        log.write_text("")
        mark.unlink(missing_ok=True)
        env = {**os.environ, "PATH": f"{root}:{os.environ['PATH']}",
               "CALL_LOG": str(log), "LOGIN_MARK": str(mark),
               "NEEDS_LOGIN": "0", "FAIL_LOGIN": "0", "FAIL_VERSION": "0",
               "FAIL_PUBLISH": "0", **flags}
        result = subprocess.run(["bash", str(script), *args], cwd="/",
                                env=env, capture_output=True, text=True)
        assert result.returncode == code, result.stdout + result.stderr
        assert log.read_text().splitlines() == [f"{root}|{line}" for line in expected]

    check([], [whoami, "version patch --no-git-tag-version", publish])
    for mode in ("minor", "major"):
        check([mode], [whoami, f"version {mode} --no-git-tag-version", publish])
    check(["current"], [whoami, publish])
    check(["--dry-run"], [f"publish --dry-run {registry} --access public"])
    check(["current"], [whoami, f"login {registry}", whoami, publish], NEEDS_LOGIN="1")
    check([], [whoami, f"login {registry}"], code=1, NEEDS_LOGIN="1", FAIL_LOGIN="1")
    check([], [whoami, "version patch --no-git-tag-version"], code=1, FAIL_VERSION="1")
    check([], [whoami, "version patch --no-git-tag-version", publish], code=1, FAIL_PUBLISH="1")
    check(["--help"], [])
    check(["invalid"], [], code=1)
    check(["patch", "minor"], [], code=1)

print("发布脚本离线验证通过（12 个场景）。")
