# `codex-rs/common/src/config_override.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6399`
- sha256: `f540ed75b7d802ca0bba2dd96b7cdb637eb89d815871e12fcf2a5a753712dd29`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `fn` `codex-rs/common/src/config_override.rs:93` `fn apply_single_override(root: &mut Value, path: &str, value: Value) {`
- `use` `codex-rs/common/src/config_override.rs:94` `use toml::value::Table;`
- `fn` `codex-rs/common/src/config_override.rs:135` `fn parse_toml_value(raw: &str) -> Result<Value, toml::de::Error> {`
- `use` `codex-rs/common/src/config_override.rs:146` `use super::*;`
- `fn` `codex-rs/common/src/config_override.rs:149` `fn parses_basic_scalar() {`
- `fn` `codex-rs/common/src/config_override.rs:155` `fn parses_bool() {`
- `fn` `codex-rs/common/src/config_override.rs:164` `fn fails_on_unquoted_string() {`
- `fn` `codex-rs/common/src/config_override.rs:169` `fn parses_array() {`
- `fn` `codex-rs/common/src/config_override.rs:176` `fn parses_inline_table() {`

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
