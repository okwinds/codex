# `codex-rs/app-server-protocol/src/schema_fixtures.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8992`
- sha256: `5cb69504332e4a91b5326c545f13f429fca2dd24ce433dac1f31fc2f0865c89c`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/schema_fixtures.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct SchemaFixtureOptions {`
- `pub fn read_schema_fixture_tree(schema_root: &Path) -> Result<BTreeMap<PathBuf, Vec<u8>>> {`
- `pub fn write_schema_fixtures(schema_root: &Path, prettier: Option<&Path>) -> Result<()> {`
- `pub fn write_schema_fixtures_with_options(`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:1` `use anyhow::Context;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:2` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:3` `use serde_json::Map;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:4` `use serde_json::Value;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:5` `use std::cmp::Ordering;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:6` `use std::collections::BTreeMap;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:7` `use std::path::Path;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:8` `use std::path::PathBuf;`
- `struct` `codex-rs/app-server-protocol/src/schema_fixtures.rs:11` `pub struct SchemaFixtureOptions {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:15` `pub fn read_schema_fixture_tree(schema_root: &Path) -> Result<BTreeMap<PathBuf, Vec<u8>>> {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:34` `pub fn write_schema_fixtures(schema_root: &Path, prettier: Option<&Path>) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:39` `pub fn write_schema_fixtures_with_options(`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:63` `fn ensure_empty_dir(dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:72` `fn read_file_bytes(path: &Path) -> Result<Vec<u8>> {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:94` `fn canonicalize_json(value: &Value) -> Value {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:152` `fn schema_array_item_sort_key(item: &Value) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:171` `fn collect_files_recursive(root: &Path) -> Result<BTreeMap<PathBuf, Vec<u8>>> {`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:214` `use super::*;`
- `use` `codex-rs/app-server-protocol/src/schema_fixtures.rs:215` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:218` `fn canonicalize_json_sorts_string_arrays() {`
- `fn` `codex-rs/app-server-protocol/src/schema_fixtures.rs:225` `fn canonicalize_json_sorts_schema_ref_arrays() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use serde_json::Map;`
- `use serde_json::Value;`
- `use std::cmp::Ordering;`
- `use std::collections::BTreeMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
