# `codex-rs/core/src/agent/guards.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7602`
- sha256: `d71a1ded8d5f86dd6e392250e605ea0d61bdd3c61950b7dffa7ae6f878709515`
- generated_utc: `2026-02-08T10:45:26Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/agent/guards.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/agent/guards.rs:1` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/agent/guards.rs:2` `use crate::error::Result;`
- `use` `codex-rs/core/src/agent/guards.rs:3` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/agent/guards.rs:4` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/agent/guards.rs:5` `use codex_protocol::protocol::SubAgentSource;`
- `use` `codex-rs/core/src/agent/guards.rs:6` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/agent/guards.rs:7` `use std::sync::Arc;`
- `use` `codex-rs/core/src/agent/guards.rs:8` `use std::sync::Mutex;`
- `use` `codex-rs/core/src/agent/guards.rs:9` `use std::sync::atomic::AtomicUsize;`
- `use` `codex-rs/core/src/agent/guards.rs:10` `use std::sync::atomic::Ordering;`
- `fn` `codex-rs/core/src/agent/guards.rs:27` `fn session_depth(session_source: &SessionSource) -> i32 {`
- `impl` `codex-rs/core/src/agent/guards.rs:43` `impl Guards {`
- `fn` `codex-rs/core/src/agent/guards.rs:74` `fn register_spawned_thread(&self, thread_id: ThreadId) {`
- `fn` `codex-rs/core/src/agent/guards.rs:82` `fn try_increment_spawned(&self, max_threads: usize) -> bool {`
- `impl` `codex-rs/core/src/agent/guards.rs:106` `impl SpawnReservation {`
- `impl` `codex-rs/core/src/agent/guards.rs:113` `impl Drop for SpawnReservation {`
- `fn` `codex-rs/core/src/agent/guards.rs:114` `fn drop(&mut self) {`
- `use` `codex-rs/core/src/agent/guards.rs:123` `use super::*;`
- `use` `codex-rs/core/src/agent/guards.rs:124` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/agent/guards.rs:127` `fn session_depth_defaults_to_zero_for_root_sources() {`
- `fn` `codex-rs/core/src/agent/guards.rs:132` `fn thread_spawn_depth_increments_and_enforces_limit() {`
- `fn` `codex-rs/core/src/agent/guards.rs:143` `fn non_thread_spawn_subagents_default_to_depth_zero() {`
- `fn` `codex-rs/core/src/agent/guards.rs:151` `fn reservation_drop_releases_slot() {`
- `fn` `codex-rs/core/src/agent/guards.rs:161` `fn commit_holds_slot_until_release() {`
- `fn` `codex-rs/core/src/agent/guards.rs:184` `fn release_ignores_unknown_thread_id() {`
- `fn` `codex-rs/core/src/agent/guards.rs:209` `fn release_is_idempotent_for_registered_threads() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::CodexErr;`
- `use crate::error::Result;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::protocol::SubAgentSource;`
- `use std::collections::HashSet;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
