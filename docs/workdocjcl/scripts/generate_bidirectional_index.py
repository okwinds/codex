#!/usr/bin/env python3
# Build a bidirectional index mapping every repo file -> capsule -> crate/package spec (if any).

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
MANIFEST = WORKDOC_ROOT / "inventory" / "file_manifest_repo.txt"
RUST_WS = WORKDOC_ROOT / "inventory" / "rust_workspace.json"
NODE_WS = WORKDOC_ROOT / "inventory" / "node_workspace.json"

OUT_MD = WORKDOC_ROOT / "spec" / "09_Verification" / "BIDIRECTIONAL_INDEX.md"
OUT_JSON = WORKDOC_ROOT / "spec" / "09_Verification" / "file_to_spec_map.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(p: Path) -> dict:
    return json.loads(p.read_text("utf-8"))


def main() -> int:
    rels = [l.strip() for l in MANIFEST.read_text("utf-8").splitlines() if l.strip()]

    rust = load_json(RUST_WS)
    rust_members = []
    for m in rust["members"]:
        if m.get("missing"):
            continue
        path = m.get("path")
        name = m.get("name")
        if not path or not name:
            continue
        # rust member paths are like "codex-rs/core"
        rust_members.append((path.replace("\\", "/").rstrip("/"), name))
    rust_members.sort(key=lambda x: len(x[0]), reverse=True)

    node = load_json(NODE_WS)
    node_pkgs = []
    for p in node["packages"]:
        path = p.get("path")
        name = p.get("name")
        if not path or not name:
            continue
        node_pkgs.append((path.replace("\\", "/").rstrip("/"), name))
    node_pkgs.sort(key=lambda x: len(x[0]), reverse=True)

    mapping = {}

    def find_owner(path: str):
        for prefix, crate_name in rust_members:
            if path == prefix or path.startswith(prefix + "/"):
                return ("rust_crate", crate_name)
        for prefix, pkg_name in node_pkgs:
            if path == prefix or path.startswith(prefix + "/"):
                return ("node_package", pkg_name)
        return ("repo", None)

    # Aggregate counts
    counts = {"rust_crate": {}, "node_package": {}, "repo": 0}

    for rel in rels:
        owner_type, owner_name = find_owner(rel)
        capsule = f"workdocjcl/spec/10_File_Specs/by_path/{rel}.md"
        crate_spec = None
        pkg_spec = None
        if owner_type == "rust_crate":
            crate_spec = f"workdocjcl/spec/11_Rust_Crate_Specs/{owner_name}.md"
            counts["rust_crate"][owner_name] = counts["rust_crate"].get(owner_name, 0) + 1
        elif owner_type == "node_package":
            pkg_spec = f"workdocjcl/spec/12_Node_Package_Specs/{owner_name.replace('/','_')}.md"
            counts["node_package"][owner_name] = counts["node_package"].get(owner_name, 0) + 1
        else:
            counts["repo"] += 1

        mapping[rel] = {
            "capsule": capsule,
            "owner_type": owner_type,
            "owner_name": owner_name,
            "crate_spec": crate_spec,
            "package_spec": pkg_spec,
        }

    OUT_JSON.write_text(json.dumps({"generated_utc": utc_now(), "mapping": mapping}, ensure_ascii=False, indent=2) + "\n", "utf-8")

    md = []
    md.append("# 双向覆盖索引（Bidirectional Coverage Index）")
    md.append("")
    md.append(f"- generated_utc: `{utc_now()}`")
    md.append(f"- repo_file_count: `{len(rels)}` (from `workdocjcl/inventory/file_manifest_repo.txt`)")
    md.append("")
    md.append("本索引用于回答两个问题：")
    md.append("1) **任意代码文件** → 它的 file capsule 在哪里？属于哪个 crate/package？")
    md.append("2) **任意 crate/package** → 它覆盖了哪些文件？（通过 `file_to_spec_map.json` 可反查）")
    md.append("")
    md.append("## 1. 生成物")
    md.append("- 文件到规格映射（机器可读）：`workdocjcl/spec/09_Verification/file_to_spec_map.json`")
    md.append("- 文件胶囊索引：`workdocjcl/spec/10_File_Specs/INDEX.md`")
    md.append("- Rust crate 索引：`workdocjcl/spec/11_Rust_Crate_Specs/INDEX.md`")
    md.append("- Node package 索引：`workdocjcl/spec/12_Node_Package_Specs/INDEX.md`")
    md.append("")
    md.append("## 2. 覆盖统计（owners）")
    md.append("")
    md.append("### 2.1 Rust crates")
    for k in sorted(counts["rust_crate"].keys()):
        md.append(f"- `{k}`: {counts['rust_crate'][k]} files")
    md.append("")
    md.append("### 2.2 Node packages")
    for k in sorted(counts["node_package"].keys()):
        md.append(f"- `{k}`: {counts['node_package'][k]} files")
    md.append("")
    md.append(f"### 2.3 Repo-level (non-crate/package)\n- {counts['repo']} files")
    md.append("")
    md.append("## 3. 使用方式（How to use）")
    md.append("- 查某个文件 `path/to/file`：在 `file_to_spec_map.json` 里找 key，得到 capsule + owner spec 路径。")
    md.append("- 查某个 crate/package 覆盖范围：在 JSON 里筛选 `owner_name`。")
    md.append("")

    OUT_MD.write_text("\n".join(md) + "\n", "utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
