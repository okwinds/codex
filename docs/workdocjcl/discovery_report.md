# Project Discovery Report (Compat)

- repo_root: `/Users/okwinds/Files/工作/若凡光年/技术平台/Code/codex`
- git_commit: `53d847406134bdb5b25c014a6b6fed5e484b28be`
- generated_utc: `2026-02-03T07:06:03Z`

## What this repository is
This is the monorepo for **OpenAI Codex CLI** (a local coding agent). It contains:
- A **Rust workspace** (`codex-rs/`) that implements the maintained CLI, TUI, sandboxing, state, MCP, and integrations.
- A **Node.js wrapper package** (`codex-cli/`, published as `@openai/codex`) that dispatches to the correct platform-specific native binary packaged under `codex-cli/vendor/…`.
- A **TypeScript SDK** (`sdk/typescript/`) and a **shell-tool MCP server** (`shell-tool-mcp/`).

## High-level tech stack
- Rust (Cargo workspace; edition 2024)
- Node.js/TypeScript (pnpm workspace)
- Bazel build files (`BUILD.bazel`, `MODULE.bazel`) and Nix flake (`flake.nix`) for hermetic builds/dev

## Repo size snapshot
- total_files_scanned (ignoring common build dirs): `2455`
- top extensions (count):
  - `.rs`: 828
  - `.txt`: 441
  - `.ts`: 419
  - `.snap`: 221
  - `.json`: 177
  - `.md`: 127
  - `.toml`: 68
  - `.bazel`: 59
  - `<noext>`: 24
  - `.yml`: 22
  - `.py`: 13
  - `.yaml`: 6
  - `.sh`: 6
  - `.lock`: 5
  - `.patch`: 5
  - `.sql`: 4
  - `.js`: 3
  - `.png`: 3
  - `.bzl`: 2
  - `.nix`: 2

## Rust workspace (`codex-rs/`)
- workspace_root: `/Users/okwinds/Files/工作/若凡光年/技术平台/Code/codex/codex-rs`
- member_count: `50`
- notable crates (partial, by name):
  - `codex-cli` at `codex-rs/cli`
  - `codex-core` at `codex-rs/core`
  - `codex-exec` at `codex-rs/exec`
  - `codex-mcp-server` at `codex-rs/mcp-server`
  - `codex-protocol` at `codex-rs/protocol`
  - `codex-tui` at `codex-rs/tui`
  - `codex-state` at `codex-rs/state`

## Node/pnpm workspace
- packages_count: `4`
- `@openai/codex` (0.0.0-dev) at `codex-cli`
- `@openai/codex-responses-api-proxy` (0.0.0-dev) at `codex-rs/responses-api-proxy/npm`
- `@openai/codex-sdk` (0.0.0-dev) at `sdk/typescript`
- `@openai/codex-shell-tool-mcp` (0.0.0-dev) at `shell-tool-mcp`

## Important top-level folders
- `codex-rs/`: maintained Rust implementation
- `codex-cli/`: `@openai/codex` npm package wrapper (native binary launcher)
- `sdk/`: SDKs (TypeScript)
- `shell-tool-mcp/`: MCP server exposing shell tool in a hardened way
- `docs/`: user-facing docs (getting started, config, sandbox, auth, etc.)
- `scripts/`: repo utilities
- `third_party/`, `patches/`: vendored deps/patches for build systems

## Notes
- The upstream skill script `discover_project.sh` requires Bash associative arrays and fails on macOS Bash 3.2; this report is a compatible replacement generated via Python + repo scans.
