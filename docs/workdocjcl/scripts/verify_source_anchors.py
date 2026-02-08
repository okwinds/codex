#!/usr/bin/env python3
"""
Spec → Code Source Anchors 校验器（复刻级对齐门槛）

目标：
- 让 spec 文档中的“来源（Source）”不只是说明，而是可重复验证的约束：
  - 引用的代码文件必须存在
  - 引用的 symbol（函数/类型/常量等）必须能在文件中定位（best-effort）
  - 若带行号，行号必须在文件范围内
  - 若使用 glob（*.rs），必须至少匹配 1 个文件

范围：
- 仅校验 `docs/workdocjcl/spec/` 下的 Markdown spec 文件
- 默认跳过高频自动生成区（File capsules / crate specs / package specs / indexes），
  只抓“手写/语义规格”章节，避免被 2000+ 自动生成文件淹没。

输出：
- docs/workdocjcl/spec/09_Verification/SOURCE_ANCHOR_REPORT.json
- docs/workdocjcl/spec/09_Verification/SOURCE_ANCHOR_REPORT.md
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
SPEC_ROOT = WORKDOC_ROOT / "spec"
VERIFY_DIR = SPEC_ROOT / "09_Verification"


SKIP_DIR_PREFIXES = (
    SPEC_ROOT / "04_Business_Logic" / "PROMPTS",
    SPEC_ROOT / "10_File_Specs",
    SPEC_ROOT / "11_Rust_Crate_Specs",
    SPEC_ROOT / "12_Node_Package_Specs",
    SPEC_ROOT / "13_Indexes",
    SPEC_ROOT / "05_Integrations" / "TOOLS_DETAILED",
    SPEC_ROOT / "05_Integrations" / "SKILLS_SYSTEM_ARTIFACTS",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_head() -> str:
    head_path = ROOT / ".git" / "HEAD"
    if not head_path.exists():
        return "(no-git)"
    head = head_path.read_text("utf-8").strip()
    if head.startswith("ref:"):
        ref = head.split(":", 1)[1].strip()
        ref_path = ROOT / ".git" / ref
        if ref_path.exists():
            return ref_path.read_text("utf-8").strip()
    return head


@dataclass(frozen=True)
class Anchor:
    raw: str
    path: str
    line: Optional[int]
    symbol: Optional[str]
    is_glob: bool


@dataclass(frozen=True)
class Finding:
    kind: str
    spec_file: str
    anchor_raw: str
    detail: str


@dataclass(frozen=True)
class Report:
    generated_utc: str
    head: str
    spec_files_checked: int
    anchors_total: int
    findings_total: int
    findings: list[Finding]


def iter_spec_md_files() -> list[Path]:
    files: list[Path] = []
    for p in SPEC_ROOT.rglob("*.md"):
        if any(str(p).startswith(str(d)) for d in SKIP_DIR_PREFIXES):
            continue
        files.append(p)
    return sorted(files)


def extract_source_section(text: str) -> str:
    """
    提取“来源（Source）”章节下的内容（尽量中文/英文兼容）。
    若找不到，返回空字符串。
    """
    # Common patterns:
    # - "## 来源（Source）"
    # - "## Source"
    # - "## 5. 来源（Source）"
    m = re.search(r"^##\s+.*?(来源（Source）|来源|Source)\s*$", text, flags=re.M)
    if not m:
        return ""
    start = m.end()
    # until next H2
    m2 = re.search(r"^##\s+", text[start:], flags=re.M)
    end = start + m2.start() if m2 else len(text)
    return text[start:end]


def parse_anchor(raw: str) -> Optional[Anchor]:
    raw = raw.strip()
    if not raw:
        return None
    # path may include glob
    is_glob = any(ch in raw for ch in ("*", "?", "["))

    # Allow formats:
    # - path/to/file
    # - path/to/file:123
    # - path/to/file#Symbol
    # - path/to/file:123#Symbol
    path_part = raw
    symbol = None
    if "#" in raw:
        path_part, symbol = raw.split("#", 1)
        symbol = symbol.strip() or None

    line = None
    if ":" in path_part:
        # split last :<digits>
        pm = re.match(r"^(.*):(\d+)$", path_part)
        if pm:
            path_part = pm.group(1)
            line = int(pm.group(2))

    path_part = path_part.strip()
    if not path_part:
        return None
    # normalize separators
    path_part = path_part.replace("\\", "/")
    return Anchor(raw=raw, path=path_part, line=line, symbol=symbol, is_glob=is_glob)


def extract_anchors_from_source_section(section: str) -> list[Anchor]:
    # Use backticked references as the canonical anchor format in this workdoc.
    anchors: list[Anchor] = []
    for m in re.finditer(r"`([^`]+)`", section):
        a = parse_anchor(m.group(1))
        if not a:
            continue
        # only consider repo-root relative paths
        if a.path.startswith(("http://", "https://", "/")):
            continue
        anchors.append(a)
    return anchors


def file_line_count(path: Path) -> int:
    # read as bytes, count '\n'
    data = path.read_bytes()
    if not data:
        return 0
    return data.count(b"\n") + 1


def symbol_exists(path: Path, symbol: str) -> bool:
    """
    best-effort：不做语言解析，只做多策略匹配
    - 直接 substring
    - 以 \b 边界做 regex
    """
    try:
        text = path.read_text("utf-8", errors="replace")
    except Exception:
        return False

    if symbol in text:
        return True
    # For Rust/TS: symbol may contain :: or .; extract last segment for boundary match
    last = re.split(r"::|\.", symbol)[-1]
    if not last:
        return False
    return re.search(rf"\b{re.escape(last)}\b", text) is not None


def verify_anchor(spec_file: Path, a: Anchor, findings: list[Finding]) -> None:
    if a.is_glob:
        matches = list(ROOT.glob(a.path))
        if not matches:
            findings.append(
                Finding(
                    kind="glob_no_match",
                    spec_file=str(spec_file.relative_to(ROOT)),
                    anchor_raw=a.raw,
                    detail=f"glob `{a.path}` matches 0 files",
                )
            )
            return
        # For globs, we don't check line/symbol.
        return

    target = (ROOT / a.path).resolve()
    try:
        rel = target.relative_to(ROOT.resolve())
    except Exception:
        rel = None

    if rel is None or not target.exists():
        findings.append(
            Finding(
                kind="path_missing",
                spec_file=str(spec_file.relative_to(ROOT)),
                anchor_raw=a.raw,
                detail=f"path not found: `{a.path}`",
            )
        )
        return

    if a.line is not None:
        lc = file_line_count(target)
        if a.line < 1 or a.line > lc:
            findings.append(
                Finding(
                    kind="line_out_of_range",
                    spec_file=str(spec_file.relative_to(ROOT)),
                    anchor_raw=a.raw,
                    detail=f"line {a.line} out of range (1..{lc}) for `{a.path}`",
                )
            )

    if a.symbol:
        if not symbol_exists(target, a.symbol):
            findings.append(
                Finding(
                    kind="symbol_not_found",
                    spec_file=str(spec_file.relative_to(ROOT)),
                    anchor_raw=a.raw,
                    detail=f"symbol `{a.symbol}` not found in `{a.path}`",
                )
            )


def main() -> int:
    VERIFY_DIR.mkdir(parents=True, exist_ok=True)
    findings: list[Finding] = []
    files = iter_spec_md_files()
    anchors_total = 0

    for f in files:
        text = f.read_text("utf-8", errors="replace")
        section = extract_source_section(text)
        if not section.strip():
            # Not all spec chapters are necessarily code-backed, but for replicability we want explicit anchors.
            findings.append(
                Finding(
                    kind="missing_source_section",
                    spec_file=str(f.relative_to(ROOT)),
                    anchor_raw="(none)",
                    detail="missing '来源（Source）/Source' section",
                )
            )
            continue
        anchors = extract_anchors_from_source_section(section)
        anchors_total += len(anchors)
        if not anchors:
            findings.append(
                Finding(
                    kind="source_section_has_no_anchors",
                    spec_file=str(f.relative_to(ROOT)),
                    anchor_raw="(none)",
                    detail="source section contains no backticked anchors",
                )
            )
            continue
        for a in anchors:
            verify_anchor(f, a, findings)

    report = Report(
        generated_utc=utc_now(),
        head=git_head(),
        spec_files_checked=len(files),
        anchors_total=anchors_total,
        findings_total=len(findings),
        findings=findings,
    )

    out_json = VERIFY_DIR / "SOURCE_ANCHOR_REPORT.json"
    out_md = VERIFY_DIR / "SOURCE_ANCHOR_REPORT.md"
    out_json.write_text(json.dumps(asdict(report), ensure_ascii=False, indent=2) + "\n", "utf-8")

    md: list[str] = []
    md.append("# Source Anchor Report")
    md.append("")
    md.append(f"- generated_utc: `{report.generated_utc}`")
    md.append(f"- head: `{report.head}`")
    md.append(f"- spec_files_checked: `{report.spec_files_checked}`")
    md.append(f"- anchors_total: `{report.anchors_total}`")
    md.append(f"- findings_total: `{report.findings_total}`")
    md.append("")
    if report.findings:
        md.append("## Findings")
        for fx in report.findings[:300]:
            md.append(f"- `{fx.kind}` in `{fx.spec_file}`: `{fx.detail}` (anchor: `{fx.anchor_raw}`)")
        if len(report.findings) > 300:
            md.append(f"- (… {len(report.findings) - 300} more)")
    else:
        md.append("## Findings")
        md.append("- (none)")

    md.append("")
    md.append("## 来源（Source）")
    md.append(f"- `{WORKDOC_ROOT.relative_to(ROOT) / 'scripts' / 'verify_source_anchors.py'}`")
    out_md.write_text("\n".join(md) + "\n", "utf-8")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
