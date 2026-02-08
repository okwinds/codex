# `codex-rs/execpolicy/src/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2017`
- sha256: `8890f77cb36674e146653b4da46e7f66849719b78daad1096364a2bec7a283f0`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/error.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct TextPosition {`
- `pub struct TextRange {`
- `pub struct ErrorLocation {`
- `pub enum Error {`
- `pub fn location(&self) -> Option<ErrorLocation> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/error.rs:1` `use starlark::Error as StarlarkError;`
- `use` `codex-rs/execpolicy/src/error.rs:2` `use thiserror::Error;`
- `type` `codex-rs/execpolicy/src/error.rs:4` `pub type Result<T> = std::result::Result<T, Error>;`
- `struct` `codex-rs/execpolicy/src/error.rs:7` `pub struct TextPosition {`
- `struct` `codex-rs/execpolicy/src/error.rs:13` `pub struct TextRange {`
- `struct` `codex-rs/execpolicy/src/error.rs:19` `pub struct ErrorLocation {`
- `enum` `codex-rs/execpolicy/src/error.rs:25` `pub enum Error {`
- `impl` `codex-rs/execpolicy/src/error.rs:48` `impl Error {`
- `fn` `codex-rs/execpolicy/src/error.rs:49` `pub fn location(&self) -> Option<ErrorLocation> {`

## Dependencies (auto sample)
### Imports / Includes
- `use starlark::Error as StarlarkError;`
- `use thiserror::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
