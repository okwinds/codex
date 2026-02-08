#!/usr/bin/env python3
# Produce a status report proving “no omissions” at multiple layers.

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
MANIFEST = WORKDOC_ROOT / "inventory" / "file_manifest_repo.txt"
CAP_ROOT = WORKDOC_ROOT / "spec" / "10_File_Specs" / "by_path"
CRATE_INDEX = WORKDOC_ROOT / "spec" / "11_Rust_Crate_Specs" / "INDEX.md"
PKG_INDEX = WORKDOC_ROOT / "spec" / "12_Node_Package_Specs" / "INDEX.md"
SYM_DIR = WORKDOC_ROOT / "spec" / "13_Indexes"
OUT = WORKDOC_ROOT / "spec" / "09_Verification" / "NO_OMISSION_STATUS.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    rels = [l.strip() for l in MANIFEST.read_text("utf-8").splitlines() if l.strip()]
    repo_count = len(rels)

    # Capsule coverage
    missing = []
    for rel in rels:
        cap = CAP_ROOT / f"{rel}.md"
        if not cap.exists():
            missing.append(rel)

    # Basic counts
    cap_count = len(list(CAP_ROOT.rglob("*.md"))) if CAP_ROOT.exists() else 0
    rust_index_ok = CRATE_INDEX.exists()
    node_index_ok = PKG_INDEX.exists()
    sym_files = sorted([p.name for p in SYM_DIR.glob("*_SYMBOL_INDEX.md")]) if SYM_DIR.exists() else []

    md = []
    md.append("# No-Omission Status Report")
    md.append("")
    md.append(f"- generated_utc: `{utc_now()}`")
    md.append("")
    md.append("## 1. File-level coverage (hard requirement)")
    md.append(f"- repo_file_count: `{repo_count}` (`workdocjcl/inventory/file_manifest_repo.txt`)")
    md.append(f"- capsule_file_count: `{cap_count}` (`workdocjcl/spec/10_File_Specs/by_path/**/*.md`)")
    md.append(f"- missing_capsules: `{len(missing)}`")
    if missing:
        md.append("")
        md.append("### Missing capsule paths (first 50)")
        for m in missing[:50]:
            md.append(f"- `{m}`")

    md.append("")
    md.append("## 2. Crate/package coverage (structure)")
    md.append(f"- rust_crate_index_present: `{str(rust_index_ok).lower()}` (`{CRATE_INDEX.relative_to(ROOT)}`)")
    md.append(f"- node_package_index_present: `{str(node_index_ok).lower()}` (`{PKG_INDEX.relative_to(ROOT)}`)")
    md.append("")
    md.append("## 3. Symbol indexes (public surfaces)")
    md.append(f"- symbol_indexes: `{', '.join(sym_files) if sym_files else '(none)'}`")
    md.append("")
    md.append("## 4. Notes")
    md.append("- File capsules include per-file definition listings (heuristic) and are intended to eliminate “silent omissions”.")
    md.append("- Full replication still depends on semantics; see `KNOWN_GAPS.md` for the deepest remaining “behavioral” gaps.")
    md.append("")
    md.append("## 5. 来源（Source）")
    md.append(f"- `{WORKDOC_ROOT.relative_to(ROOT) / 'scripts' / 'generate_no_omission_status.py'}`")
    md.append(f"- `{MANIFEST.relative_to(ROOT)}`")
    md.append(f"- `{CRATE_INDEX.relative_to(ROOT)}`")
    md.append(f"- `{PKG_INDEX.relative_to(ROOT)}`")
    md.append(f"- `{SYM_DIR.relative_to(ROOT)}`")

    OUT.write_text("\n".join(md) + "\n", "utf-8")

    # Also write a JSON marker for tooling.
    (OUT.parent / "NO_OMISSION_STATUS.json").write_text(
        json.dumps(
            {
                "generated_utc": utc_now(),
                "repo_file_count": repo_count,
                "capsule_file_count": cap_count,
                "missing_capsules": missing,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        "utf-8",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
