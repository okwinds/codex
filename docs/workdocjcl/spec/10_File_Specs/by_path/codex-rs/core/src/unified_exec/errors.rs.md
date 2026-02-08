# `codex-rs/core/src/unified_exec/errors.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1098`
- sha256: `5605aa97b62c1a33e33d193c9bd3f10b291b4734318862d16047747908c5c887`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/unified_exec/errors.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/unified_exec/errors.rs:1` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/unified_exec/errors.rs:2` `use thiserror::Error;`
- `impl` `codex-rs/core/src/unified_exec/errors.rs:26` `impl UnifiedExecError {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecToolCallOutput;`
- `use thiserror::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
