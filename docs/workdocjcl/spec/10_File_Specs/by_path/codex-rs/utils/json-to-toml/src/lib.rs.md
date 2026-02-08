# `codex-rs/utils/json-to-toml/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2502`
- sha256: `4d8ae4a4b4ab6febe636e283e5f6d0d0953202a31bcd5822b9b9086b5dd183c3`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/json-to-toml/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn json_to_toml(v: JsonValue) -> TomlValue {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/json-to-toml/src/lib.rs:1` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/utils/json-to-toml/src/lib.rs:2` `use toml::Value as TomlValue;`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:5` `pub fn json_to_toml(v: JsonValue) -> TomlValue {`
- `use` `codex-rs/utils/json-to-toml/src/lib.rs:32` `use super::*;`
- `use` `codex-rs/utils/json-to-toml/src/lib.rs:33` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/utils/json-to-toml/src/lib.rs:34` `use serde_json::json;`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:37` `fn json_number_to_toml() {`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:43` `fn json_array_to_toml() {`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:52` `fn json_bool_to_toml() {`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:58` `fn json_float_to_toml() {`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:64` `fn json_null_to_toml() {`
- `fn` `codex-rs/utils/json-to-toml/src/lib.rs:70` `fn json_object_nested() {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde_json::Value as JsonValue;`
- `use toml::Value as TomlValue;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
