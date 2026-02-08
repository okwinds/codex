# `codex-rs/common/src/config_override.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7025`
- sha256: `3a588d4aee3d956c235a884d0ca20bd976ecdf1ec93ce546dd9298dd33e8f4db`
- generated_utc: `2026-02-08T10:45:25Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/config_override.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CliConfigOverrides {`
- `pub fn parse_overrides(&self) -> Result<Vec<(String, Value)>, String> {`
- `pub fn apply_on_value(&self, target: &mut Value) -> Result<(), String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/config_override.rs:10` `use clap::ArgAction;`
- `use` `codex-rs/common/src/config_override.rs:11` `use clap::Parser;`
- `use` `codex-rs/common/src/config_override.rs:12` `use serde::de::Error as SerdeError;`
- `use` `codex-rs/common/src/config_override.rs:13` `use toml::Value;`
- `struct` `codex-rs/common/src/config_override.rs:19` `pub struct CliConfigOverrides {`
- `impl` `codex-rs/common/src/config_override.rs:39` `impl CliConfigOverrides {`
- `fn` `codex-rs/common/src/config_override.rs:42` `pub fn parse_overrides(&self) -> Result<Vec<(String, Value)>, String> {`
- `fn` `codex-rs/common/src/config_override.rs:82` `pub fn apply_on_value(&self, target: &mut Value) -> Result<(), String> {`
- `fn` `codex-rs/common/src/config_override.rs:91` `fn canonicalize_override_key(key: &str) -> String {`
- `fn` `codex-rs/common/src/config_override.rs:101` `fn apply_single_override(root: &mut Value, path: &str, value: Value) {`
- `use` `codex-rs/common/src/config_override.rs:102` `use toml::value::Table;`
- `fn` `codex-rs/common/src/config_override.rs:143` `fn parse_toml_value(raw: &str) -> Result<Value, toml::de::Error> {`
- `use` `codex-rs/common/src/config_override.rs:154` `use super::*;`
- `fn` `codex-rs/common/src/config_override.rs:157` `fn parses_basic_scalar() {`
- `fn` `codex-rs/common/src/config_override.rs:163` `fn parses_bool() {`
- `fn` `codex-rs/common/src/config_override.rs:172` `fn fails_on_unquoted_string() {`
- `fn` `codex-rs/common/src/config_override.rs:177` `fn parses_array() {`
- `fn` `codex-rs/common/src/config_override.rs:184` `fn canonicalizes_use_linux_sandbox_bwrap_alias() {`
- `fn` `codex-rs/common/src/config_override.rs:194` `fn parses_inline_table() {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::ArgAction;`
- `use clap::Parser;`
- `use serde::de::Error as SerdeError;`
- `use toml::Value;`
- `use toml::value::Table;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
