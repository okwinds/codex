# `codex-app-server`

- path: `codex-rs/app-server`
- generated_utc: `2026-02-08T10:45:12Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-app-server` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `async-trait`
- `chrono`
- `clap`
- `codex-app-server-protocol`
- `codex-arg0`
- `codex-backend-client`
- `codex-chatgpt`
- `codex-cloud-requirements`
- `codex-common`
- `codex-core`
- `codex-feedback`
- `codex-file-search`
- `codex-login`
- `codex-protocol`
- `codex-rmcp-client`
- `codex-utils-absolute-path`
- `codex-utils-json-to-toml`
- `futures`
- `owo-colors`
- `serde`
- `serde_json`
- `tempfile`
- `time`
- `tokio`
- `tokio-tungstenite`
- `toml`
- `tracing`
- `tracing-subscriber`
- `uuid`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use crate::transport::AppServerTransport;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
