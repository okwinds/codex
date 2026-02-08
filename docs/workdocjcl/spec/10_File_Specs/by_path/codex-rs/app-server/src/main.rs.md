# `codex-rs/app-server/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1227`
- sha256: `10a2cffdef627e42cf632c1d52c9dd764c571395ebb11c4950900bb5bab52b9a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/main.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/main.rs:1` `use codex_app_server::run_main;`
- `use` `codex-rs/app-server/src/main.rs:2` `use codex_arg0::arg0_dispatch_or_else;`
- `use` `codex-rs/app-server/src/main.rs:3` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/app-server/src/main.rs:4` `use codex_core::config_loader::LoaderOverrides;`
- `use` `codex-rs/app-server/src/main.rs:5` `use std::path::PathBuf;`
- `const` `codex-rs/app-server/src/main.rs:9` `const MANAGED_CONFIG_PATH_ENV_VAR: &str = "CODEX_APP_SERVER_MANAGED_CONFIG_PATH";`
- `fn` `codex-rs/app-server/src/main.rs:11` `fn main() -> anyhow::Result<()> {`
- `fn` `codex-rs/app-server/src/main.rs:30` `fn managed_config_path_from_debug_env() -> Option<PathBuf> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_app_server::run_main;`
- `use codex_arg0::arg0_dispatch_or_else;`
- `use codex_common::CliConfigOverrides;`
- `use codex_core::config_loader::LoaderOverrides;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
