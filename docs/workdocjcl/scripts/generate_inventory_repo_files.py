#!/usr/bin/env python3
"""
生成 workdocjcl 所需的仓库文件清单（inventory manifests）。

为什么需要：
- workdocjcl 的若干“无遗漏”生成脚本依赖 `inventory/file_manifest_repo.txt` 等清单。
- workdocjcl 自身位于 `docs/workdocjcl/`，如果把该目录也纳入清单，会导致“规格文档为自己生成规格”的递归与噪声。

输出（写入 `docs/workdocjcl/inventory/`）：
- file_manifest_repo.txt：git tracked 文件（排除 docs/workdocjcl/**）
- file_manifest.txt：与 file_manifest_repo.txt 保持一致（作为 fallback manifest）
- file_manifest_all.txt：同上（避免历史脚本引用缺失）
- repo_stats.json：基础统计（文件数/总字节数/HEAD）
"""

from __future__ import annotations

import json
import subprocess
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
OUT_DIR = WORKDOC_ROOT / "inventory"

EXCLUDE_PREFIXES = (
    "docs/workdocjcl/",
    ".git/",
)
EXCLUDE_BASENAMES = {
    ".DS_Store",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_head() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True)
        .strip()
    )


def git_ls_files() -> list[str]:
    out = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True)
    rels = [l.strip() for l in out.splitlines() if l.strip()]
    filtered: list[str] = []
    for rel in rels:
        if any(rel.startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        if Path(rel).name in EXCLUDE_BASENAMES:
            continue
        filtered.append(rel)
    return filtered


def write_manifest(path: Path, rels: list[str]) -> None:
    path.write_text("\n".join(rels) + "\n", "utf-8")


@dataclass(frozen=True)
class RepoStats:
    generated_utc: str
    head: str
    tracked_files: int
    tracked_bytes_total: int
    top_level_dirs: dict[str, int]
    extensions_top: list[tuple[str, int]]


def build_stats(rels: list[str]) -> RepoStats:
    total_bytes = 0
    top_level: Counter[str] = Counter()
    exts: Counter[str] = Counter()

    for rel in rels:
        parts = rel.split("/", 1)
        top_level[parts[0]] += 1
        ext = Path(rel).suffix.lower() or "(no_ext)"
        exts[ext] += 1

        p = ROOT / rel
        try:
            total_bytes += p.stat().st_size
        except FileNotFoundError:
            # 文件在 ls-files 里但本地缺失：仍然保留在清单中以暴露问题
            pass

    return RepoStats(
        generated_utc=utc_now(),
        head=git_head(),
        tracked_files=len(rels),
        tracked_bytes_total=total_bytes,
        top_level_dirs=dict(top_level.most_common()),
        extensions_top=exts.most_common(30),
    )


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rels = git_ls_files()

    # 稳定排序：便于 diff 与 review
    rels = sorted(rels)

    write_manifest(OUT_DIR / "file_manifest_repo.txt", rels)
    write_manifest(OUT_DIR / "file_manifest.txt", rels)
    write_manifest(OUT_DIR / "file_manifest_all.txt", rels)

    stats = build_stats(rels)
    (OUT_DIR / "repo_stats.json").write_text(
        json.dumps(asdict(stats), ensure_ascii=False, indent=2) + "\n", "utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

