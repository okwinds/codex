# `codex-rs/execpolicy-legacy/src/exec_call.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `621`
- sha256: `ba8337e5e43eed053228c04907a02efdfc49f1b56231c7ba831ca40d9e165698`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/exec_call.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ExecCall {`
- `pub fn new(program: &str, args: &[&str]) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/exec_call.rs:1` `use std::fmt::Display;`
- `use` `codex-rs/execpolicy-legacy/src/exec_call.rs:3` `use serde::Serialize;`
- `struct` `codex-rs/execpolicy-legacy/src/exec_call.rs:6` `pub struct ExecCall {`
- `impl` `codex-rs/execpolicy-legacy/src/exec_call.rs:11` `impl ExecCall {`
- `fn` `codex-rs/execpolicy-legacy/src/exec_call.rs:12` `pub fn new(program: &str, args: &[&str]) -> Self {`
- `impl` `codex-rs/execpolicy-legacy/src/exec_call.rs:20` `impl Display for ExecCall {`
- `fn` `codex-rs/execpolicy-legacy/src/exec_call.rs:21` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt::Display;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
