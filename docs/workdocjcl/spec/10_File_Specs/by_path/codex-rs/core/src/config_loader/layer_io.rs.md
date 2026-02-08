# `codex-rs/core/src/config_loader/layer_io.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3577`
- sha256: `33c3be24806cca996f29d873da8ee5fc4ef7e5bbce0c7628ccf6b50c1ad6d5b4`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/layer_io.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/layer_io.rs:1` `use super::LoaderOverrides;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:2` `use super::diagnostics::config_error_from_toml;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:3` `use super::diagnostics::io_error_from_config_error;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:5` `use super::macos::load_managed_admin_config_layer;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:6` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:7` `use std::io;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:8` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:9` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:10` `use tokio::fs;`
- `use` `codex-rs/core/src/config_loader/layer_io.rs:11` `use toml::Value as TomlValue;`
- `const` `codex-rs/core/src/config_loader/layer_io.rs:14` `const CODEX_MANAGED_CONFIG_SYSTEM_PATH: &str = "/etc/codex/managed_config.toml";`

## Dependencies (auto sample)
### Imports / Includes
- `use super::LoaderOverrides;`
- `use super::diagnostics::config_error_from_toml;`
- `use super::diagnostics::io_error_from_config_error;`
- `use super::macos::load_managed_admin_config_layer;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tokio::fs;`
- `use toml::Value as TomlValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
