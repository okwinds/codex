#!/usr/bin/env python3
"""
生成 Node/pnpm workspace inventory（workdocjcl/inventory/node_workspace.*）。

不依赖 `pnpm install` 或 node_modules：
- 解析 `pnpm-workspace.yaml` 中的 packages patterns（非常简化的 YAML 解析，只支持本仓库现状）。
- 对每个匹配目录读取 `package.json`，提取 name/version/bin/engines/scripts/deps。

用途：
- 为 `generate_bidirectional_index.py` 提供 package owner 映射输入；
- 为复刻者提供发布包清单与入口（bin）。
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
OUT_DIR = WORKDOC_ROOT / "inventory"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_pnpm_workspace_patterns() -> list[str]:
    """
    仅支持 pnpm-workspace.yaml 的一个子集：
    packages:
      - 'path'
      - "path"
      - path
    """
    p = ROOT / "pnpm-workspace.yaml"
    lines = p.read_text("utf-8").splitlines()
    patterns: list[str] = []
    in_packages = False
    for raw in lines:
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        if s == "packages:":
            in_packages = True
            continue
        if not in_packages:
            continue
        if not s.startswith("-"):
            # packages block ended
            break
        item = s.lstrip("-").strip().strip("'").strip('"')
        if item:
            patterns.append(item)
    return patterns


@dataclass(frozen=True)
class NodePackage:
    pattern: str
    path: str
    name: str
    version: str
    private: object
    bin: object
    type: object
    engines: object
    scripts: list[str]
    dependencies: list[str]
    devDependencies: list[str]


def load_package_json(dir_path: Path) -> dict:
    return json.loads((dir_path / "package.json").read_text("utf-8"))


def collect_packages(patterns: list[str]) -> list[NodePackage]:
    pkgs: list[NodePackage] = []
    for pat in patterns:
        # 仅支持本仓库 patterns 为具体路径（不处理通配符）
        rel = pat.replace("\\", "/").rstrip("/")
        d = ROOT / rel
        if not d.exists():
            continue
        if not (d / "package.json").exists():
            continue
        doc = load_package_json(d)
        pkgs.append(
            NodePackage(
                pattern=pat,
                path=rel,
                name=str(doc.get("name") or ""),
                version=str(doc.get("version") or ""),
                private=doc.get("private"),
                bin=doc.get("bin"),
                type=doc.get("type"),
                engines=doc.get("engines"),
                scripts=sorted(list((doc.get("scripts") or {}).keys())),
                dependencies=sorted(list((doc.get("dependencies") or {}).keys())),
                devDependencies=sorted(list((doc.get("devDependencies") or {}).keys())),
            )
        )
    pkgs.sort(key=lambda p: p.path)
    return pkgs


def write_md(pkgs: list[NodePackage]) -> None:
    md: list[str] = []
    md.append("# Node/pnpm Workspace Inventory")
    md.append("")
    md.append(f"- generated_utc: `{utc_now()}`")
    md.append(f"- workspace_root: `{str(ROOT)}`")
    md.append(f"- package_count: `{len(pkgs)}`")
    md.append("")
    md.append("| Path | Package name | Version | Bin | Engines |")
    md.append("|---|---|---|---|---|")
    for p in pkgs:
        md.append(
            f"| `{p.path}` | `{p.name}` | `{p.version}` | `{p.bin}` | `{p.engines}` |"
        )
    (OUT_DIR / "node_workspace.md").write_text("\n".join(md) + "\n", "utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    patterns = parse_pnpm_workspace_patterns()
    pkgs = collect_packages(patterns)

    payload = {
        "generated_utc": utc_now(),
        "workspace_root": str(ROOT),
        "packages": [asdict(p) for p in pkgs],
    }
    (OUT_DIR / "node_workspace.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", "utf-8"
    )
    write_md(pkgs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

