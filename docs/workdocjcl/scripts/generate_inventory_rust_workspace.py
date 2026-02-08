#!/usr/bin/env python3
"""
生成 Rust workspace inventory（workdocjcl/inventory/rust_workspace.*）。

注意：这里**不依赖** `cargo metadata`（环境可能没有 Rust toolchain），而是：
- 以 `codex-rs/Cargo.toml` 的 `[workspace].members` 为准；
- 逐 member 解析其 `Cargo.toml` 的 `[package]` 与 `[[bin]]`。

用途：
- 为 `generate_bidirectional_index.py` 提供 crate owner 映射输入；
- 为复刻者提供 crate 清单（便于定位入口与边界）。
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import tomli

ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
OUT_DIR = WORKDOC_ROOT / "inventory"
WS_ROOT = ROOT / "codex-rs"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel_from_repo_root(abs_path: str) -> str:
    p = Path(abs_path)
    try:
        return str(p.resolve().relative_to(ROOT.resolve())).replace("\\", "/")
    except Exception:
        return str(p).replace("\\", "/")


def read_toml(path: Path) -> dict:
    return tomli.loads(path.read_text("utf-8"))


@dataclass(frozen=True)
class RustBin:
    name: str
    path: str


@dataclass(frozen=True)
class RustMember:
    path: str
    name: str
    edition: object
    version: object
    publish: object
    has_main_rs: bool
    bins: list[RustBin]
    missing: bool = False


def build_members() -> list[RustMember]:
    ws = read_toml(WS_ROOT / "Cargo.toml")
    members = ws.get("workspace", {}).get("members", []) or []
    out: list[RustMember] = []

    for member in members:
        # Cargo workspace members are relative to `codex-rs/` (workspace root).
        member_rel_to_ws = str(member).replace("\\", "/").rstrip("/")
        crate_dir = (WS_ROOT / member_rel_to_ws).resolve()
        rel_dir = rel_from_repo_root(str(crate_dir))
        cargo_toml = crate_dir / "Cargo.toml"
        if not cargo_toml.exists():
            out.append(
                RustMember(
                    path=rel_dir,
                    name="",
                    edition="",
                    version="",
                    publish=None,
                    has_main_rs=False,
                    bins=[],
                    missing=True,
                )
            )
            continue

        doc = read_toml(cargo_toml)
        pkg = doc.get("package", {}) or {}
        name = pkg.get("name", "")
        edition = pkg.get("edition", "")
        version = pkg.get("version", "")
        publish = pkg.get("publish")

        has_main = (crate_dir / "src" / "main.rs").exists()

        bins: list[RustBin] = []
        for b in doc.get("bin", []) or []:
            if not isinstance(b, dict):
                continue
            bins.append(RustBin(name=str(b.get("name") or ""), path=str(b.get("path") or "")))

        out.append(
            RustMember(
                path=rel_dir,
                name=str(name),
                edition=edition,
                version=version,
                publish=publish,
                has_main_rs=has_main,
                bins=sorted(bins, key=lambda b: b.name),
                missing=False,
            )
        )

    out.sort(key=lambda m: m.path)
    return out


def write_md(workspace_root: str, members: list[RustMember]) -> None:
    md: list[str] = []
    md.append("# Rust Workspace Inventory")
    md.append("")
    md.append(f"- generated_utc: `{utc_now()}`")
    md.append(f"- workspace_root: `{workspace_root}`")
    md.append(f"- member_count: `{len(members)}`")
    md.append("")
    md.append("| Path | Crate name | Has `src/main.rs` | [[bin]] entries |")
    md.append("|---|---|---:|---|")
    for m in members:
        if m.missing:
            md.append(f"| `{m.path}` | (missing) | no |  |")
            continue
        bins = ", ".join([b.name for b in m.bins if b.name]) if m.bins else ""
        md.append(
            f"| `{m.path}` | `{m.name}` | {'yes' if m.has_main_rs else 'no'} | {bins} |"
        )
    (OUT_DIR / "rust_workspace.md").write_text("\n".join(md) + "\n", "utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    members = build_members()

    payload = {
        "generated_utc": utc_now(),
        "workspace_root": str((ROOT / "codex-rs").resolve()),
        "members": [asdict(m) for m in members],
    }
    (OUT_DIR / "rust_workspace.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", "utf-8"
    )
    write_md(str((ROOT / "codex-rs").resolve()), members)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
