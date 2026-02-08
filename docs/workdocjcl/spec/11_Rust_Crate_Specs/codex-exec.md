# `codex-exec`

- path: `codex-rs/exec`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-exec` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `clap`
- `codex-arg0`
- `codex-cloud-requirements`
- `codex-common`
- `codex-core`
- `codex-protocol`
- `codex-utils-absolute-path`
- `owo-colors`
- `serde`
- `serde_json`
- `shlex`
- `supports-color`
- `tokio`
- `tracing`
- `tracing-subscriber`
- `ts-rs`
- `uuid`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod event_processor_with_jsonl_output;`
- `pub mod exec_events;`
- `pub use cli::Cli;`
- `pub use cli::Command;`
- `pub use cli::ReviewArgs;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
