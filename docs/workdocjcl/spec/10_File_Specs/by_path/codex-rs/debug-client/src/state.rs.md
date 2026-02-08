# `codex-rs/debug-client/src/state.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `549`
- sha256: `9ad8d564add8eb814879fa639f9b57f5066f0148c6a935be796a39dbe1b3a8f0`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/debug-client/src/state.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct State {`
- `pub enum PendingRequest {`
- `pub enum ReaderEvent {`

## Definitions (auto, per-file)
- `use` `codex-rs/debug-client/src/state.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/debug-client/src/state.rs:3` `use codex_app_server_protocol::RequestId;`
- `struct` `codex-rs/debug-client/src/state.rs:6` `pub struct State {`
- `enum` `codex-rs/debug-client/src/state.rs:13` `pub enum PendingRequest {`
- `enum` `codex-rs/debug-client/src/state.rs:20` `pub enum ReaderEvent {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use codex_app_server_protocol::RequestId;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
