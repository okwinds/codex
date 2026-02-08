# `codex-rs/core/src/rollout/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1980`
- sha256: `e3727df4933ce055a719d0f27b0c96d52e80991117982e8b77fd8183f3192b4f`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/error.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/error.rs:1` `use std::io::ErrorKind;`
- `use` `codex-rs/core/src/rollout/error.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/rollout/error.rs:4` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/rollout/error.rs:5` `use crate::rollout::SESSIONS_SUBDIR;`
- `fn` `codex-rs/core/src/rollout/error.rs:19` `fn map_rollout_io_error(io_err: &std::io::Error, codex_home: &Path) -> Option<CodexErr> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use crate::error::CodexErr;`
- `use crate::rollout::SESSIONS_SUBDIR;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
