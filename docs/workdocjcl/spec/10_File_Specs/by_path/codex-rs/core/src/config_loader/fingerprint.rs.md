# `codex-rs/core/src/config_loader/fingerprint.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2099`
- sha256: `c22698a749bd1206fd66c26debb20a65b23b39a4efdd87f135eb3dd293a95b25`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/fingerprint.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/fingerprint.rs:1` `use codex_app_server_protocol::ConfigLayerMetadata;`
- `use` `codex-rs/core/src/config_loader/fingerprint.rs:2` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/core/src/config_loader/fingerprint.rs:3` `use sha2::Digest;`
- `use` `codex-rs/core/src/config_loader/fingerprint.rs:4` `use sha2::Sha256;`
- `use` `codex-rs/core/src/config_loader/fingerprint.rs:5` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/config_loader/fingerprint.rs:6` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/config_loader/fingerprint.rs:51` `fn canonical_json(value: &JsonValue) -> JsonValue {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_app_server_protocol::ConfigLayerMetadata;`
- `use serde_json::Value as JsonValue;`
- `use sha2::Digest;`
- `use sha2::Sha256;`
- `use std::collections::HashMap;`
- `use toml::Value as TomlValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
