#!/usr/bin/env python3
# Generate per-package specs for pnpm workspace packages.

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
OUT_ROOT = WORKDOC_ROOT / "spec" / "12_Node_Package_Specs"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text("utf-8"))


def main() -> int:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    ws = read_json(WORKDOC_ROOT / "inventory" / "node_workspace.json")
    packages = ws["packages"]

    index = [
        "# Node Package Specs Index",
        "",
        f"- generated_utc: `{utc_now()}`",
        f"- package_count: `{len(packages)}`",
        "",
        "| Path | Package | Spec | Bin | Engines |",
        "|---|---|---|---|---|",
    ]

    for p in packages:
        pkg_path = ROOT / p["path"]
        pkg_json = pkg_path / "package.json"
        if not pkg_json.exists():
            continue
        data = read_json(pkg_json)

        name = data.get("name", "(unknown)")
        spec_name = f"{name}.md".replace("/", "_")
        spec_path = OUT_ROOT / spec_name

        scripts = data.get("scripts") or {}
        deps = data.get("dependencies") or {}
        dev_deps = data.get("devDependencies") or {}
        bins = data.get("bin")

        lines = []
        lines.append(f"# `{name}`")
        lines.append("")
        lines.append(f"- path: `{pkg_path.relative_to(ROOT)}`")
        lines.append(f"- version: `{data.get('version')}`")
        lines.append(f"- generated_utc: `{utc_now()}`")
        if data.get("description"):
            lines.append(f"- description: {data['description']}")
        lines.append("")
        lines.append("## Entry Points")
        if bins:
            lines.append(f"- bin: `{bins}`")
        else:
            lines.append("- bin: (none)")
        if data.get("exports"):
            lines.append(f"- exports: `{data.get('exports')}`")
        if data.get("main"):
            lines.append(f"- main: `{data.get('main')}`")
        if data.get("module"):
            lines.append(f"- module: `{data.get('module')}`")
        if data.get("types"):
            lines.append(f"- types: `{data.get('types')}`")
        lines.append("")
        lines.append("## Scripts")
        if scripts:
            for k in sorted(scripts.keys()):
                lines.append(f"- `{k}`: `{scripts[k]}`")
        else:
            lines.append("- (none)")
        lines.append("")
        lines.append("## Dependencies (direct)")
        if deps:
            for k in sorted(deps.keys())[:80]:
                lines.append(f"- `{k}`: `{deps[k]}`")
        else:
            lines.append("- (none)")
        lines.append("")
        lines.append("## Dev Dependencies (direct)")
        if dev_deps:
            for k in sorted(dev_deps.keys())[:80]:
                lines.append(f"- `{k}`: `{dev_deps[k]}`")
        else:
            lines.append("- (none)")
        lines.append("")
        lines.append("## Spec Links")
        lines.append("- `workdocjcl/spec/00_Overview/PROJECT.md`")
        if str(pkg_path.relative_to(ROOT)).startswith("codex-cli/"):
            lines.append("- `workdocjcl/spec/07_Infrastructure/PACKAGING.md`")
        if str(pkg_path.relative_to(ROOT)).startswith("shell-tool-mcp/"):
            lines.append("- `workdocjcl/spec/05_Integrations/MCP.md`")

        spec_path.write_text("\n".join(lines) + "\n", "utf-8")

        index.append(
            f"| `{p['path']}` | `{name}` | `{spec_name}` | `{bins}` | `{data.get('engines')}` |"
        )

    (OUT_ROOT / "INDEX.md").write_text("\n".join(index) + "\n", "utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
