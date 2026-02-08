# `codex-rs/core/src/config/schema.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4718`
- sha256: `77e675feedd9635057113c8bd3786c6a129581fd9423ed34ea726db23f094a97`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/schema.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn config_schema() -> RootSchema {`
- `pub fn config_schema_json() -> anyhow::Result<Vec<u8>> {`
- `pub fn write_config_schema(out_path: &Path) -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config/schema.rs:1` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/config/schema.rs:2` `use crate::config::types::RawMcpServerConfig;`
- `use` `codex-rs/core/src/config/schema.rs:3` `use crate::features::FEATURES;`
- `use` `codex-rs/core/src/config/schema.rs:4` `use schemars::r#gen::SchemaGenerator;`
- `use` `codex-rs/core/src/config/schema.rs:5` `use schemars::r#gen::SchemaSettings;`
- `use` `codex-rs/core/src/config/schema.rs:6` `use schemars::schema::InstanceType;`
- `use` `codex-rs/core/src/config/schema.rs:7` `use schemars::schema::ObjectValidation;`
- `use` `codex-rs/core/src/config/schema.rs:8` `use schemars::schema::RootSchema;`
- `use` `codex-rs/core/src/config/schema.rs:9` `use schemars::schema::Schema;`
- `use` `codex-rs/core/src/config/schema.rs:10` `use schemars::schema::SchemaObject;`
- `use` `codex-rs/core/src/config/schema.rs:11` `use serde_json::Map;`
- `use` `codex-rs/core/src/config/schema.rs:12` `use serde_json::Value;`
- `use` `codex-rs/core/src/config/schema.rs:13` `use std::path::Path;`
- `fn` `codex-rs/core/src/config/schema.rs:56` `pub fn config_schema() -> RootSchema {`
- `fn` `codex-rs/core/src/config/schema.rs:66` `fn canonicalize(value: &Value) -> Value {`
- `fn` `codex-rs/core/src/config/schema.rs:83` `pub fn config_schema_json() -> anyhow::Result<Vec<u8>> {`
- `fn` `codex-rs/core/src/config/schema.rs:92` `pub fn write_config_schema(out_path: &Path) -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config/schema.rs:100` `use super::canonicalize;`
- `use` `codex-rs/core/src/config/schema.rs:101` `use super::config_schema_json;`
- `use` `codex-rs/core/src/config/schema.rs:103` `use similar::TextDiff;`
- `fn` `codex-rs/core/src/config/schema.rs:106` `fn config_schema_matches_fixture() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::ConfigToml;`
- `use crate::config::types::RawMcpServerConfig;`
- `use crate::features::FEATURES;`
- `use schemars::r#gen::SchemaGenerator;`
- `use schemars::r#gen::SchemaSettings;`
- `use schemars::schema::InstanceType;`
- `use schemars::schema::ObjectValidation;`
- `use schemars::schema::RootSchema;`
- `use schemars::schema::Schema;`
- `use schemars::schema::SchemaObject;`
- `use serde_json::Map;`
- `use serde_json::Value;`
- `use std::path::Path;`
- `use super::canonicalize;`
- `use super::config_schema_json;`
- `use similar::TextDiff;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
