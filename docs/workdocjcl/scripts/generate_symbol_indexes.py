#!/usr/bin/env python3
# Generate language-level symbol indexes (file:line -> symbol signature).

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
MANIFEST = WORKDOC_ROOT / "inventory" / "file_manifest_repo.txt"
OUT_DIR = WORKDOC_ROOT / "spec" / "13_Indexes"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_manifest() -> list:
    return [l.strip() for l in MANIFEST.read_text("utf-8").splitlines() if l.strip()]


def scan_file(path: Path, rel: str, patterns: list, max_bytes: int = 1024 * 1024) -> list:
    if path.stat().st_size > max_bytes:
        return []
    lines = path.read_text("utf-8", errors="replace").splitlines()
    results = []
    for lineno, line in enumerate(lines, start=1):
        for kind, rx in patterns:
            if rx.search(line):
                results.append(
                    {
                        "file": rel,
                        "line": lineno,
                        "kind": kind,
                        "signature": line.strip(),
                    }
                )
    return results


def write_index(basename: str, title: str, items: list) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    md = []
    md.append(f"# {title}")
    md.append("")
    md.append(f"- generated_utc: `{utc_now()}`")
    md.append(f"- symbol_count: `{len(items)}`")
    md.append("")
    md.append("| Kind | Location | Signature |")
    md.append("|---|---|---|")
    for it in items:
        loc = f"`{it['file']}:{it['line']}`"
        md.append(f"| `{it['kind']}` | {loc} | `{it['signature']}` |")

    (OUT_DIR / f"{basename}_SYMBOL_INDEX.md").write_text("\n".join(md) + "\n", "utf-8")
    (OUT_DIR / f"{basename}_SYMBOL_INDEX.json").write_text(
        json.dumps({"generated_utc": utc_now(), "items": items}, ensure_ascii=False) + "\n",
        "utf-8",
    )


def main() -> int:
    # 清理旧生成物，避免语言/文件变更后残留过期索引文件。
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    rels = load_manifest()

    rust_patterns = [
        ("pub_struct", re.compile(r"^\s*pub\s+struct\s+\w+")),
        ("pub_enum", re.compile(r"^\s*pub\s+enum\s+\w+")),
        ("pub_trait", re.compile(r"^\s*pub\s+trait\s+\w+")),
        ("pub_fn", re.compile(r"^\s*pub\s+(async\s+)?fn\s+\w+\s*\(")),
        ("fn_main", re.compile(r"^\s*fn\s+main\s*\(")),
        ("pub_const", re.compile(r"^\s*pub\s+const\s+\w+")),
        ("pub_static", re.compile(r"^\s*pub\s+static\s+\w+")),
        ("pub_type", re.compile(r"^\s*pub\s+type\s+\w+")),
        ("pub_mod", re.compile(r"^\s*pub\s+mod\s+\w+")),
    ]

    ts_patterns = [
        ("export_fn", re.compile(r"^\s*export\s+(async\s+)?function\s+\w+\s*\(")),
        ("export_class", re.compile(r"^\s*export\s+class\s+\w+")),
        ("export_interface", re.compile(r"^\s*export\s+interface\s+\w+")),
        ("export_type", re.compile(r"^\s*export\s+type\s+\w+")),
        ("export_const", re.compile(r"^\s*export\s+const\s+\w+")),
        ("export_enum", re.compile(r"^\s*export\s+enum\s+\w+")),
    ]

    py_patterns = [
        ("def", re.compile(r"^def\s+\w+\s*\(")),
        ("class", re.compile(r"^class\s+\w+")),
    ]

    rust_items = []
    ts_items = []
    py_items = []

    for rel in rels:
        p = ROOT / rel
        if not p.exists():
            continue
        if rel.endswith(".rs"):
            rust_items.extend(scan_file(p, rel, rust_patterns))
        elif rel.endswith((".ts", ".tsx")):
            ts_items.extend(scan_file(p, rel, ts_patterns))
        elif rel.endswith(".py"):
            py_items.extend(scan_file(p, rel, py_patterns))

    write_index("RUST", "Rust Symbol Index", rust_items)
    write_index("TYPESCRIPT", "TypeScript Symbol Index", ts_items)
    write_index("PYTHON", "Python Symbol Index", py_items)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
