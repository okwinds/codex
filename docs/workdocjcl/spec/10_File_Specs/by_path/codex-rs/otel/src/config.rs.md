# `codex-rs/otel/src/config.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2223`
- sha256: `52a59af5c1426bb48cd71d0c4dd805f398374a9e0088999cf5806399611a9cea`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/config.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct OtelSettings {`
- `pub enum OtelHttpProtocol {`
- `pub struct OtelTlsConfig {`
- `pub enum OtelExporter {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/config.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/otel/src/config.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/otel/src/config.rs:4` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `struct` `codex-rs/otel/src/config.rs:32` `pub struct OtelSettings {`
- `enum` `codex-rs/otel/src/config.rs:44` `pub enum OtelHttpProtocol {`
- `struct` `codex-rs/otel/src/config.rs:52` `pub struct OtelTlsConfig {`
- `enum` `codex-rs/otel/src/config.rs:59` `pub enum OtelExporter {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
