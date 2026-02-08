# `codex-rs/core/src/transport_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `556`
- sha256: `3310fa5f01963a4990cc8beb2df9278a51c4932c518bc7ea7998e95807813153`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/transport_manager.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct TransportManager {`
- `pub fn new() -> Self {`
- `pub fn disable_websockets(&self) -> bool {`
- `pub fn activate_http_fallback(&self, websocket_enabled: bool) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/transport_manager.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/transport_manager.rs:2` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/core/src/transport_manager.rs:3` `use std::sync::atomic::Ordering;`
- `struct` `codex-rs/core/src/transport_manager.rs:6` `pub struct TransportManager {`
- `impl` `codex-rs/core/src/transport_manager.rs:10` `impl TransportManager {`
- `fn` `codex-rs/core/src/transport_manager.rs:11` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/transport_manager.rs:15` `pub fn disable_websockets(&self) -> bool {`
- `fn` `codex-rs/core/src/transport_manager.rs:19` `pub fn activate_http_fallback(&self, websocket_enabled: bool) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::atomic::Ordering;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
