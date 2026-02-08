#!/usr/bin/env python3
# Generates a file-by-file “capsule” spec for every repo file listed in inventory/file_manifest.txt

import hashlib
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
INVENTORY_MANIFEST_REPO = WORKDOC_ROOT / "inventory" / "file_manifest_repo.txt"
INVENTORY_MANIFEST_FALLBACK = WORKDOC_ROOT / "inventory" / "file_manifest.txt"
OUT_ROOT = WORKDOC_ROOT / "spec" / "10_File_Specs"
OUT_BY_PATH = OUT_ROOT / "by_path"

MAX_READ_BYTES = 1024 * 512  # 512KB cap for content-based extraction


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(1024 * 256)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def read_head(path: Path) -> bytes:
    with path.open("rb") as f:
        return f.read(MAX_READ_BYTES)


def classify_path(rel: str) -> str:
    low = rel.lower()
    if low.endswith((".md", ".rst")):
        return "doc"
    if low.endswith((".toml", ".yaml", ".yml", ".json", ".lock", ".bazel", ".bzl", ".nix", ".cfg", ".ini")):
        return "config"
    if "/tests/" in low or low.endswith((".snap", ".snap.new")) or low.endswith((".test.ts", ".spec.ts", "_test.rs")):
        return "test"
    if low.startswith(".github/") or low.startswith(".devcontainer/"):
        return "build"
    if low.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".woff", ".woff2", ".ttf", ".otf")):
        return "asset"
    if low.endswith((".rs", ".ts", ".tsx", ".js", ".mjs", ".cjs", ".py", ".go", ".java", ".kt", ".sh")):
        return "source"
    return "unknown"


def extract_env_vars(text: str) -> list:
    vars_found = set()
    # Rust
    for m in re.finditer(r'std::env::var(?:_os)?\(\s*"([^"]+)"\s*\)', text):
        vars_found.add(m.group(1))
    # Node/TS
    for m in re.finditer(r"process\.env\.([A-Za-z0-9_]+)", text):
        vars_found.add(m.group(1))
    for m in re.finditer(r'process\.env\[\s*["\']([^"\']+)["\']\s*\]', text):
        vars_found.add(m.group(1))
    # Python
    for m in re.finditer(r"os\.environ(?:\.get)?\(\s*['\"]([^'\"]+)['\"]", text):
        vars_found.add(m.group(1))
    return sorted(vars_found)

def extract_side_effects(rel: str, text: str) -> list:
    effects = set()
    low = rel.lower()
    # Process execution
    if any(x in text for x in ("child_process", "spawn(", "exec(", "Command::new", "tokio::process::Command")):
        effects.add("spawns subprocesses")
    # Filesystem writes
    if any(x in text for x in ("writeFile", "writeFileSync", "fs::write", "tokio::fs::write", "create_dir_all", "OpenOptions", "File::create")):
        effects.add("writes to filesystem")
    # Network
    if any(x in text for x in ("reqwest::", "hyper::", "fetch(", "axios", "TcpListener", "axum::", "ureq::")):
        effects.add("performs network I/O")
    # DB
    if "sqlx::" in text or "sqlite" in low:
        effects.add("reads/writes SQLite or DB")
    # Stdout/stderr
    if any(x in text for x in ("println!", "eprintln!", "console.log", "console.error", "print(")):
        effects.add("writes to stdout/stderr")
    return sorted(effects)

def extract_error_handling(text: str) -> list:
    notes = set()
    if "process.exit(" in text:
        notes.add("calls process.exit(...)")
    if "throw new Error" in text or re.search(r"throw\s+\w", text):
        notes.add("throws exceptions")
    if any(x in text for x in ("expect(", "unwrap(", "panic!", "unreachable!", "bail!(")):
        notes.add("uses Rust panic/expect/unwrap-style failure paths")
    if any(x in text for x in ("Result<", "anyhow::Result", "thiserror", "ErrorKind")):
        notes.add("returns structured errors (Result/ErrorKind)")
    if any(x in text for x in ("retry", "max_retries", "timeout", "backoff")):
        notes.add("has retry/timeout/backoff logic")
    return sorted(notes)

def extract_definitions(rel: str, text: str) -> list:
    defs = []
    if rel.endswith(".rs"):
        patterns = [
            ("mod", re.compile(r"^\s*(pub\s+)?mod\s+([a-zA-Z0-9_]+)\s*;")),
            ("use", re.compile(r"^\s*use\s+.+;")),
            ("struct", re.compile(r"^\s*(pub\s+)?struct\s+([A-Za-z0-9_]+)")),
            ("enum", re.compile(r"^\s*(pub\s+)?enum\s+([A-Za-z0-9_]+)")),
            ("trait", re.compile(r"^\s*(pub\s+)?trait\s+([A-Za-z0-9_]+)")),
            ("type", re.compile(r"^\s*(pub\s+)?type\s+([A-Za-z0-9_]+)")),
            ("const", re.compile(r"^\s*(pub\s+)?const\s+([A-Za-z0-9_]+)")),
            ("static", re.compile(r"^\s*(pub\s+)?static\s+([A-Za-z0-9_]+)")),
            ("fn", re.compile(r"^\s*(pub\s+)?(async\s+)?fn\s+([A-Za-z0-9_]+)\s*\(")),
            ("impl", re.compile(r"^\s*impl(\s*<[^>]+>)?\s+.*\{\s*$")),
        ]
        for lineno, line in enumerate(text.splitlines(), start=1):
            for kind, rx in patterns:
                if rx.search(line):
                    defs.append((kind, lineno, line.strip()))
                    break
    elif rel.endswith((".ts", ".tsx", ".js", ".mjs", ".cjs")):
        patterns = [
            ("import", re.compile(r"^\s*import\s+")),
            ("export", re.compile(r"^\s*export\s+")),
            ("class", re.compile(r"^\s*(export\s+)?class\s+\w+")),
            ("function", re.compile(r"^\s*(export\s+)?(async\s+)?function\s+\w+\s*\(")),
            ("const", re.compile(r"^\s*(export\s+)?const\s+\w+")),
            ("type", re.compile(r"^\s*(export\s+)?type\s+\w+")),
            ("interface", re.compile(r"^\s*(export\s+)?interface\s+\w+")),
            ("enum", re.compile(r"^\s*(export\s+)?enum\s+\w+")),
        ]
        for lineno, line in enumerate(text.splitlines(), start=1):
            for kind, rx in patterns:
                if rx.search(line):
                    defs.append((kind, lineno, line.strip()))
                    break
    elif rel.endswith(".py"):
        patterns = [
            ("import", re.compile(r"^\s*(from\s+\S+\s+)?import\s+")),
            ("class", re.compile(r"^\s*class\s+\w+")),
            ("def", re.compile(r"^\s*def\s+\w+\s*\(")),
            ("main", re.compile(r"^if\s+__name__\s*==\s*['\"]__main__['\"]\s*:")),
        ]
        for lineno, line in enumerate(text.splitlines(), start=1):
            for kind, rx in patterns:
                if rx.search(line):
                    defs.append((kind, lineno, line.strip()))
                    break
    return defs


def extract_public_surface(rel: str, text: str) -> list:
    # Keep this intentionally shallow: we’ll list signature lines that matter for replication.
    out = []
    if rel.endswith(".rs"):
        patterns = [
            r"^\s*pub\s+struct\s+\w+",
            r"^\s*pub\s+enum\s+\w+",
            r"^\s*pub\s+trait\s+\w+",
            r"^\s*pub\s+fn\s+\w+\s*\(",
            r"^\s*fn\s+main\s*\(",
        ]
        for line in text.splitlines():
            if any(re.search(p, line) for p in patterns):
                out.append(line.strip())
                if len(out) >= 50:
                    break
    elif rel.endswith((".ts", ".tsx", ".js", ".mjs", ".cjs")):
        patterns = [
            r"^\s*export\s+(async\s+)?function\s+\w+\s*\(",
            r"^\s*export\s+class\s+\w+",
            r"^\s*export\s+interface\s+\w+",
            r"^\s*export\s+type\s+\w+",
            r"^\s*export\s+const\s+\w+",
            r"^\s*module\.exports\s*=",
        ]
        for line in text.splitlines():
            if any(re.search(p, line) for p in patterns):
                out.append(line.strip())
                if len(out) >= 50:
                    break
    elif rel.endswith(".py"):
        patterns = [
            r"^\s*def\s+\w+\s*\(",
            r"^\s*class\s+\w+",
            r"^if\s+__name__\s*==\s*['\"]__main__['\"]\s*:",
        ]
        for line in text.splitlines():
            if any(re.search(p, line) for p in patterns):
                out.append(line.strip())
                if len(out) >= 50:
                    break
    return out


def spec_links_for(rel: str) -> list:
    # Minimal heuristic mapping. Deep mapping lives in CODE_TO_SPEC_MAP.md.
    links = []
    if rel.startswith("codex-cli/"):
        links.append("07_Infrastructure/PACKAGING.md")
    if rel.startswith("codex-rs/cli/"):
        links.append("03_API/CLI.md")
    if rel.startswith("codex-rs/core/"):
        links.append("00_Overview/ARCHITECTURE.md")
    if rel.startswith("codex-rs/state/"):
        links.append("02_Data/ENTITIES.md")
    if rel.startswith("codex-rs/protocol/"):
        links.append("02_Data/ROLLOUT_FORMAT.md")
    if rel.startswith("codex-rs/tui/"):
        links.append("06_UI/TUI.md")
    if rel.startswith("sdk/typescript/"):
        links.append("00_Overview/PROJECT.md")
    if rel.startswith("shell-tool-mcp/"):
        links.append("05_Integrations/MCP.md")
    return sorted(set(links))

def guess_purpose(kind: str, rel: str, public_surface: list) -> str:
    low = rel.lower()
    if rel == "codex-cli/bin/codex.js":
        return "Node wrapper entrypoint for @openai/codex: selects the correct platform-specific native binary and executes it with signal forwarding."
    if rel == "codex-rs/cli/src/main.rs":
        return "Rust CLI multitool entrypoint: parses args, routes to subcommands, defaults to launching TUI when no subcommand is provided."
    if rel == "codex-rs/core/src/codex.rs":
        return "Core engine turn loop and Submission/Event interface."
    if low.startswith(".github/workflows/"):
        return "GitHub Actions workflow definition."
    if low.startswith(".github/actions/") and low.endswith("action.yml"):
        return "GitHub Action definition (composite/docker action)."
    if low.startswith(".devcontainer/"):
        return "Devcontainer configuration for local development environments."
    if low.endswith(".sql") and "/migrations/" in low:
        return "SQLite migration file (schema evolution)."
    if low in ("build.bazel", "module.bazel") or low.endswith(".bzl") or low.endswith(".bazel"):
        return "Bazel build configuration file."
    if low.startswith("flake.") or low.endswith(".nix"):
        return "Nix flake / Nix configuration file."
    if low.endswith("package.json"):
        return "Node package manifest (name/scripts/dependencies/exports)."
    if low.endswith("pnpm-lock.yaml") or low.endswith("pnpm-workspace.yaml"):
        return "pnpm workspace/lockfile for Node packages."
    if low.endswith(".gitignore") or low.endswith(".dockerignore"):
        return "Ignore rules for tooling (git/docker)."
    if low == "justfile":
        return "Just task runner definitions (developer workflow helpers)."
    if kind == "doc":
        return "Documentation file."
    if kind == "config":
        return "Configuration file for build/tooling/runtime."
    if kind == "test":
        return "Test or snapshot file used for automated verification."
    if kind == "asset":
        return "Asset file (image/font/etc.) used by docs or UI."
    if kind == "source":
        if public_surface:
            return "Source file implementing exported/public items listed below."
        return "Source file (no public surface detected by heuristic)."
    return "Repository file."


def write_capsule(rel: str) -> None:
    path = ROOT / rel
    if not path.exists():
        return

    kind = classify_path(rel)
    size = path.stat().st_size
    digest = sha256_file(path)
    generated = utc_now()

    # Content extraction
    env_vars = []
    public_surface = []
    imports_sample = []

    if kind in ("source", "config", "test", "doc") and size <= MAX_READ_BYTES:
        try:
            head = read_head(path)
            # Heuristic: treat as text if decodable as utf-8 with replacement.
            text = head.decode("utf-8", errors="replace")
            env_vars = extract_env_vars(text)
            public_surface = extract_public_surface(rel, text)
            for line in text.splitlines():
                line_s = line.strip()
                if rel.endswith(".rs") and line_s.startswith("use "):
                    imports_sample.append(line_s)
                elif rel.endswith((".ts", ".tsx", ".js", ".mjs", ".cjs")) and (
                    line_s.startswith("import ") or line_s.startswith("export ")
                ):
                    imports_sample.append(line_s)
                elif rel.endswith(".py") and (line_s.startswith("import ") or line_s.startswith("from ")):
                    imports_sample.append(line_s)
                if len(imports_sample) >= 20:
                    break
        except Exception:
            pass

    purpose = guess_purpose(kind, rel, public_surface)

    out_path = OUT_BY_PATH / (rel + ".md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    spec_links = spec_links_for(rel)
    spec_links_lines = "\n".join([f"- `workdocjcl/spec/{p}`" for p in spec_links]) if spec_links else "- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)"

    public_lines = "\n".join([f"- `{l}`" for l in public_surface]) if public_surface else "- (none detected)"
    imports_lines = "\n".join([f"- `{l}`" for l in imports_sample]) if imports_sample else "- (none detected)"
    env_lines = "\n".join([f"- `{v}`" for v in env_vars]) if env_vars else "- (none detected)"

    defs_lines = "- (not extracted)\n"
    if kind == "source" and size <= MAX_READ_BYTES:
        defs = extract_definitions(rel, text)
        if defs:
            max_rows = 200
            shown = defs[:max_rows]
            defs_lines = "\n".join([f"- `{k}` `{rel}:{ln}` `{sig}`" for k, ln, sig in shown]) + "\n"
            if len(defs) > max_rows:
                defs_lines += f"- (… {len(defs) - max_rows} more definitions omitted; see symbol indexes under `workdocjcl/spec/13_Indexes/`)\n"
        else:
            defs_lines = "- (no definitions detected by heuristic)\n"

    env_inputs_line = ""
    if env_vars:
        env_inputs_line = "- env: " + ", ".join([f"`{v}`" for v in env_vars]) + "\n"

    outputs_line = "- none (file is declarative: doc/config/test/asset)\n"
    if kind == "source":
        if size <= MAX_READ_BYTES:
            side_effects = extract_side_effects(rel, text)
            if side_effects:
                outputs_line = "\n".join([f"- {e}" for e in side_effects]) + "\n"
            else:
                outputs_line = "- (no obvious side effects detected by heuristic)\n"
        else:
            outputs_line = "- (file too large for side-effect heuristic; inspect manually)\n"

    error_lines = "- (none detected)\n"
    if kind == "source" and size <= MAX_READ_BYTES:
        errs = extract_error_handling(text)
        if errs:
            error_lines = "\n".join([f"- {e}" for e in errs]) + "\n"
        else:
            error_lines = "- (no obvious error-handling patterns detected by heuristic)\n"

    content = (
        f"# `{rel}`\n\n"
        "## Identity\n"
        f"- kind: `{kind}`\n"
        f"- ext: `{Path(rel).suffix or '<noext>'}`\n"
        f"- size_bytes: `{size}`\n"
        f"- sha256: `{digest}`\n"
        f"- generated_utc: `{generated}`\n\n"
        "## Purpose (Why)\n"
        f"{purpose}\n\n"
        "## Interfaces (Inputs/Outputs)\n"
        "### Inputs\n"
        f"- filesystem: `{rel}` (read)\n"
        f"{env_inputs_line}\n"
        "### Outputs / Side Effects\n"
        f"{outputs_line}\n"
        "## Public Surface (auto)\n"
        f"{public_lines}\n\n"
        "## Definitions (auto, per-file)\n"
        f"{defs_lines}\n"
        "## Dependencies (auto sample)\n"
        "### Imports / Includes\n"
        f"{imports_lines}\n"
        "### Referenced env vars\n"
        f"{env_lines}\n\n"
        "## Error Handling / Edge Cases\n"
        f"{error_lines}\n"
        "## Spec Links\n"
        f"{spec_links_lines}\n"
    )

    out_path.write_text(content, "utf-8")


def main() -> int:
    manifest = INVENTORY_MANIFEST_REPO if INVENTORY_MANIFEST_REPO.exists() else INVENTORY_MANIFEST_FALLBACK
    if not manifest.exists():
        print(f"missing manifest: {manifest}", file=sys.stderr)
        return 2

    OUT_BY_PATH.mkdir(parents=True, exist_ok=True)
    rels = [line.strip() for line in manifest.read_text("utf-8").splitlines() if line.strip()]

    # Only include paths that exist inside repo root.
    rels = [r for r in rels if (ROOT / r).exists()]

    for rel in rels:
        write_capsule(rel)

    # INDEX.md
    index_lines = [
        "# File Capsule Index",
        "",
        f"- generated_utc: `{utc_now()}`",
        f"- file_count: `{len(rels)}`",
        "",
        "Each repo file has a corresponding capsule under `10_File_Specs/by_path/`.",
        "",
        "| Repo path | Capsule | kind |",
        "|---|---|---|",
    ]
    for rel in rels:
        cap = f"by_path/{rel}.md"
        index_lines.append(f"| `{rel}` | `{cap}` | `{classify_path(rel)}` |")
    (OUT_ROOT / "INDEX.md").write_text("\n".join(index_lines) + "\n", "utf-8")

    # Coverage marker
    (OUT_ROOT / "COVERAGE.json").write_text(
        f'{{"generated_utc":"{utc_now()}","file_count":{len(rels)}}}\n', "utf-8"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
