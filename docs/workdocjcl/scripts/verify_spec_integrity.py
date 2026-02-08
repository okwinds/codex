#!/usr/bin/env python3
"""
轻量一致性校验（不改代码）：

1) SPEC_INDEX.md 中的链接目标是否存在
2) CODE_TO_SPEC_MAP.md 中的 code/spec 路径是否存在

目的：
- “复刻级”文档不仅要内容全，还要能被人/工具可靠导航。
- 迁移到 `docs/workdocjcl/` 后，需要一个可重复运行的自检入口。
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
SPEC_ROOT = WORKDOC_ROOT / "spec"
VERIFY_DIR = SPEC_ROOT / "09_Verification"

SPEC_INDEX = SPEC_ROOT / "SPEC_INDEX.md"
CODE_TO_SPEC_MAP = VERIFY_DIR / "CODE_TO_SPEC_MAP.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass(frozen=True)
class Finding:
    kind: str
    source: str
    detail: str


@dataclass(frozen=True)
class Report:
    generated_utc: str
    head: str
    spec_index_links_total: int
    spec_index_links_missing: int
    code_to_spec_rows_total: int
    code_to_spec_code_missing: int
    code_to_spec_spec_missing: int
    findings: list[Finding]


def git_head() -> str:
    head = (ROOT / ".git" / "HEAD").read_text("utf-8").strip()
    if head.startswith("ref:"):
        ref = head.split(":", 1)[1].strip()
        return (ROOT / ".git" / ref).read_text("utf-8").strip()
    return head


def parse_spec_index_links(text: str) -> list[str]:
    # capture markdown links like [text](path)
    return [m.group(1) for m in re.finditer(r"\]\(([^)]+)\)", text)]


def parse_backticked_paths(text: str) -> list[str]:
    return [m.group(1) for m in re.finditer(r"`([^`]+)`", text)]


def main() -> int:
    findings: list[Finding] = []

    spec_index_text = SPEC_INDEX.read_text("utf-8", errors="replace")
    links = parse_spec_index_links(spec_index_text)
    missing_links = 0
    for target in links:
        p = (SPEC_ROOT / target).resolve()
        if not p.exists():
            missing_links += 1
            findings.append(
                Finding(kind="spec_index_link_missing", source=str(SPEC_INDEX), detail=target)
            )

    # CODE_TO_SPEC_MAP: treat backticked `path` that looks like repo-root relative paths.
    map_text = CODE_TO_SPEC_MAP.read_text("utf-8", errors="replace")
    ticks = parse_backticked_paths(map_text)

    # Heuristic: the table contains code paths like `codex-rs/...` and spec paths like `docs/workdocjcl/spec/...`.
    code_paths = [t for t in ticks if t.startswith(("codex-rs/", "codex-cli/", "shell-tool-mcp/", "sdk/", "docs/"))]
    # Split into rows count approximation by counting table lines (| ... | ... | ... |)
    rows_total = sum(1 for line in map_text.splitlines() if line.strip().startswith("| `"))

    code_missing = 0
    spec_missing = 0
    for t in code_paths:
        if "*" in t or "?" in t or "[" in t:
            matches = list(ROOT.glob(t))
            if matches:
                continue
            if t.startswith("docs/workdocjcl/spec/"):
                spec_missing += 1
                findings.append(
                    Finding(kind="code_to_spec_spec_missing", source=str(CODE_TO_SPEC_MAP), detail=t)
                )
            else:
                code_missing += 1
                findings.append(
                    Finding(kind="code_to_spec_code_missing", source=str(CODE_TO_SPEC_MAP), detail=t)
                )
            continue

        p = (ROOT / t).resolve()
        if not p.exists():
            if t.startswith("docs/workdocjcl/spec/"):
                spec_missing += 1
                findings.append(
                    Finding(kind="code_to_spec_spec_missing", source=str(CODE_TO_SPEC_MAP), detail=t)
                )
            else:
                code_missing += 1
                findings.append(
                    Finding(kind="code_to_spec_code_missing", source=str(CODE_TO_SPEC_MAP), detail=t)
                )

    report = Report(
        generated_utc=utc_now(),
        head=git_head(),
        spec_index_links_total=len(links),
        spec_index_links_missing=missing_links,
        code_to_spec_rows_total=rows_total,
        code_to_spec_code_missing=code_missing,
        code_to_spec_spec_missing=spec_missing,
        findings=findings,
    )

    out_json = VERIFY_DIR / "SPEC_INTEGRITY_REPORT.json"
    out_md = VERIFY_DIR / "SPEC_INTEGRITY_REPORT.md"

    out_json.write_text(json.dumps(asdict(report), ensure_ascii=False, indent=2) + "\n", "utf-8")

    md: list[str] = []
    md.append("# Spec Integrity Report")
    md.append("")
    md.append(f"- generated_utc: `{report.generated_utc}`")
    md.append(f"- head: `{report.head}`")
    md.append("")
    md.append("## Summary")
    md.append(f"- spec_index_links_total: `{report.spec_index_links_total}`")
    md.append(f"- spec_index_links_missing: `{report.spec_index_links_missing}`")
    md.append(f"- code_to_spec_rows_total: `{report.code_to_spec_rows_total}`")
    md.append(f"- code_to_spec_code_missing: `{report.code_to_spec_code_missing}`")
    md.append(f"- code_to_spec_spec_missing: `{report.code_to_spec_spec_missing}`")
    md.append("")
    if findings:
        md.append("## Findings")
        for f in findings[:200]:
            md.append(f"- `{f.kind}` in `{f.source}`: `{f.detail}`")
        if len(findings) > 200:
            md.append(f"- (… {len(findings) - 200} more)")
    else:
        md.append("## Findings")
        md.append("- (none)")
    md.append("")
    md.append("## 来源（Source）")
    md.append(f"- `{WORKDOC_ROOT.relative_to(ROOT) / 'scripts' / 'verify_spec_integrity.py'}`")
    md.append(f"- `{SPEC_INDEX.relative_to(ROOT)}`")
    md.append(f"- `{CODE_TO_SPEC_MAP.relative_to(ROOT)}`")
    out_md.write_text("\n".join(md) + "\n", "utf-8")

    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
