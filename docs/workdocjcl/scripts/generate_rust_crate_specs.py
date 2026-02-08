#!/usr/bin/env python3
# Generate per-crate specs for codex-rs workspace.

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import tomli


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
WORKDOC_REPO_PREFIX = "docs/workdocjcl"
WS_ROOT = ROOT / "codex-rs"
OUT_ROOT = WORKDOC_ROOT / "spec" / "11_Rust_Crate_Specs"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_toml(path: Path) -> dict:
    return tomli.loads(path.read_text("utf-8"))


def extract_pub_surface_rust(path: Path) -> list:
    if not path.exists():
        return []
    text = path.read_text("utf-8", errors="replace")
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("pub "):
            if re.match(r"pub\s+(use|mod)\s+", s) or re.match(r"pub\s+(struct|enum|trait|fn)\s+", s):
                out.append(s)
        if s.startswith("fn main(") or s.startswith("pub fn main("):
            out.append(s)
        if len(out) >= 80:
            break
    return out


def guess_role(crate_name: str, rel_path: str) -> str:
    # Coarse classification for navigability; authoritative mapping still in CODE_TO_SPEC_MAP.md.
    if crate_name == "codex-core":
        return "core engine (turn loop, tools, config, rollout)"
    if crate_name == "codex-cli":
        return "top-level CLI multitool (clap) for codex executable"
    if crate_name == "codex-tui":
        return "terminal UI (ratatui-based) and interactive runtime"
    if crate_name == "codex-protocol":
        return "shared protocol types (events/config/model I/O) used across crates"
    if crate_name == "codex-state":
        return "SQLite-backed state DB and rollout metadata extraction"
    if "execpolicy" in crate_name:
        return "execpolicy rules and enforcement"
    if rel_path.startswith("utils/"):
        return "shared utility crate"
    if "mcp" in crate_name:
        return "MCP client/server or related support"
    if "login" in crate_name:
        return "login/auth flows and credential handling"
    return "crate"


def main() -> int:
    # 清理旧生成物，避免 workspace members 变化导致残留过期 crate spec。
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    ws = read_toml(WS_ROOT / "Cargo.toml")
    members = ws["workspace"]["members"]

    index_lines = [
        "# Rust Crate Specs Index",
        "",
        f"- generated_utc: `{utc_now()}`",
        f"- workspace_root: `{WS_ROOT}`",
        f"- member_count: `{len(members)}`",
        "",
        "| Member path | Crate name | Role (heuristic) | Spec |",
        "|---|---|---|---|",
    ]

    for member in members:
        crate_path = WS_ROOT / member
        cargo_toml = crate_path / "Cargo.toml"
        if not cargo_toml.exists():
            continue
        data = read_toml(cargo_toml)
        pkg = data.get("package", {})
        name = pkg.get("name", "(unknown)")
        desc = pkg.get("description")
        role = guess_role(name, member)
        has_lib = (crate_path / "src" / "lib.rs").exists()
        has_main = (crate_path / "src" / "main.rs").exists()
        bins = []
        for b in data.get("bin", []) or []:
            bins.append({"name": b.get("name"), "path": b.get("path")})
        features = sorted((data.get("features") or {}).keys())
        deps = sorted((data.get("dependencies") or {}).keys())

        pub_surface = []
        if has_lib:
            pub_surface = extract_pub_surface_rust(crate_path / "src" / "lib.rs")
        elif has_main:
            pub_surface = extract_pub_surface_rust(crate_path / "src" / "main.rs")

        spec_name = f"{name}.md".replace("/", "_")
        spec_path = OUT_ROOT / spec_name

        lines = []
        lines.append(f"# `{name}`")
        lines.append("")
        lines.append(f"- path: `{crate_path.relative_to(ROOT)}`")
        lines.append(f"- generated_utc: `{utc_now()}`")
        if desc:
            lines.append(f"- description: {desc}")
        lines.append(f"- role: {role}")
        lines.append("")
        lines.append("## Build Targets")
        lines.append(f"- has_lib_rs: `{str(has_lib).lower()}`")
        lines.append(f"- has_main_rs: `{str(has_main).lower()}`")
        if bins:
            lines.append("- explicit_bins:")
            for b in bins:
                lines.append(f"  - name: `{b.get('name')}` path: `{b.get('path')}`")
        else:
            lines.append("- explicit_bins: (none)")
        lines.append("")
        lines.append("## Key Dependencies (direct, from Cargo.toml)")
        if deps:
            for d in deps[:60]:
                lines.append(f"- `{d}`")
            if len(deps) > 60:
                lines.append(f"- (… {len(deps)-60} more)")
        else:
            lines.append("- (none)")
        lines.append("")
        lines.append("## Features")
        if features:
            for f in features[:80]:
                lines.append(f"- `{f}`")
            if len(features) > 80:
                lines.append(f"- (… {len(features)-80} more)")
        else:
            lines.append("- (none)")
        lines.append("")
        lines.append("## Public Surface (auto, from src/lib.rs or src/main.rs)")
        if pub_surface:
            for s in pub_surface:
                lines.append(f"- `{s}`")
        else:
            lines.append("- (none detected)")
        lines.append("")
        lines.append("## Spec Links")
        lines.append(f"- `{WORKDOC_REPO_PREFIX}/spec/00_Overview/MODULE_MAP.md`")
        lines.append(f"- `{WORKDOC_REPO_PREFIX}/spec/09_Verification/CODE_TO_SPEC_MAP.md`")
        if name in ("codex-cli", "codex-core", "codex-tui", "codex-protocol", "codex-state"):
            lines.append(f"- `{WORKDOC_REPO_PREFIX}/spec/00_Overview/ARCHITECTURE.md`")
        if name == "codex-state":
            lines.append(f"- `{WORKDOC_REPO_PREFIX}/spec/02_Data/ENTITIES.md`")
        if name == "codex-core":
            lines.append(f"- `{WORKDOC_REPO_PREFIX}/spec/05_Integrations/TOOLS.md`")
        spec_path.write_text("\n".join(lines) + "\n", "utf-8")

        index_lines.append(
            f"| `{member}` | `{name}` | {role} | `{spec_name}` |"
        )

    (OUT_ROOT / "INDEX.md").write_text("\n".join(index_lines) + "\n", "utf-8")
    (OUT_ROOT / "META.json").write_text(
        json.dumps(
            {"generated_utc": utc_now(), "member_count": len(members)}, ensure_ascii=False, indent=2
        )
        + "\n",
        "utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
