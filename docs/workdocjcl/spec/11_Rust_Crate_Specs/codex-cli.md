# `codex-cli`

- path: `codex-rs/cli`
- generated_utc: `2026-02-08T10:45:13Z`
- role: top-level CLI multitool (clap) for codex executable

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `clap`
- `clap_complete`
- `codex-app-server`
- `codex-app-server-protocol`
- `codex-app-server-test-client`
- `codex-arg0`
- `codex-chatgpt`
- `codex-cloud-tasks`
- `codex-common`
- `codex-core`
- `codex-exec`
- `codex-execpolicy`
- `codex-login`
- `codex-mcp-server`
- `codex-protocol`
- `codex-responses-api-proxy`
- `codex-rmcp-client`
- `codex-stdio-to-uds`
- `codex-tui`
- `libc`
- `owo-colors`
- `regex-lite`
- `serde_json`
- `supports-color`
- `tempfile`
- `tokio`
- `toml`
- `tracing`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod debug_sandbox;`
- `pub mod login;`
- `pub struct SeatbeltCommand {`
- `pub struct LandlockCommand {`
- `pub struct WindowsCommand {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
