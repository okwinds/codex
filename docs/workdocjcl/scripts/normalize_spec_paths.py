#!/usr/bin/env python3
"""
把 spec 文档中“旧路径前缀”规范化为当前 repo-root 路径：

- workdocjcl/spec/...      -> docs/workdocjcl/spec/...
- workdocjcl/inventory/... -> docs/workdocjcl/inventory/...
- workdocjcl/scripts/...   -> docs/workdocjcl/scripts/...

背景：
- workdocjcl 目录从 repo root 迁移到了 `docs/workdocjcl/`；
- 生成脚本已切换到新位置，但历史手写章节仍可能引用旧前缀。

范围：
- 仅处理 `docs/workdocjcl/spec/**/*.md`（不改代码、不改生成的 JSON mapping）。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
SPEC_ROOT = ROOT / "docs" / "workdocjcl" / "spec"


# 仅替换“未带 docs/ 前缀”的旧路径，避免把 `docs/workdocjcl/...` 变成 `docs/docs/workdocjcl/...`。
REPLACEMENTS = (
    (re.compile(r"(?<!docs/)workdocjcl/spec/"), "docs/workdocjcl/spec/"),
    (re.compile(r"(?<!docs/)workdocjcl/inventory/"), "docs/workdocjcl/inventory/"),
    (re.compile(r"(?<!docs/)workdocjcl/scripts/"), "docs/workdocjcl/scripts/"),
    # 安全兜底：如果历史上已经出现重复前缀，统一收敛
    (re.compile(r"docs/docs/workdocjcl/"), "docs/workdocjcl/"),
)


@dataclass(frozen=True)
class RewriteStats:
    files_total: int
    files_changed: int
    bytes_before: int
    bytes_after: int


def rewrite_file(path: Path) -> tuple[bool, int, int]:
    before = path.read_text("utf-8")
    after = before
    for pat, dst in REPLACEMENTS:
        after = pat.sub(dst, after)
    if after == before:
        return (False, len(before.encode("utf-8")), len(after.encode("utf-8")))
    path.write_text(after, "utf-8")
    return (True, len(before.encode("utf-8")), len(after.encode("utf-8")))


def main() -> int:
    files = sorted(SPEC_ROOT.rglob("*.md"))
    changed = 0
    b_before = 0
    b_after = 0
    for f in files:
        did, bb, ba = rewrite_file(f)
        b_before += bb
        b_after += ba
        if did:
            changed += 1

    stats = RewriteStats(
        files_total=len(files),
        files_changed=changed,
        bytes_before=b_before,
        bytes_after=b_after,
    )
    print(stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
