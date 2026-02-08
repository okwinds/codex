# `codex-rs/core/src/function_tool.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `271`
- sha256: `2df0e491ae2cc8f7683a59462a862d9db675f05567912f213bcebb5ae601fd47`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/function_tool.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum FunctionCallError {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/function_tool.rs:1` `use thiserror::Error;`
- `enum` `codex-rs/core/src/function_tool.rs:4` `pub enum FunctionCallError {`

## Dependencies (auto sample)
### Imports / Includes
- `use thiserror::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
