# `codex-rs/core/src/unified_exec/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14724`
- sha256: `49a299960856a210bfbd610c49b004bcb60a7f0c50ed4f3164da16f15771b850`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/unified_exec/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new(session: Arc<Session>, turn: Arc<TurnContext>, call_id: String) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/unified_exec/mod.rs:24` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:25` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:26` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:27` `use std::sync::Arc;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:28` `use std::time::Duration;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:30` `use rand::Rng;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:31` `use rand::rng;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:32` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:34` `use crate::codex::Session;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:35` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:36` `use crate::sandboxing::SandboxPermissions;`
- `mod` `codex-rs/core/src/unified_exec/mod.rs:38` `mod async_watcher;`
- `mod` `codex-rs/core/src/unified_exec/mod.rs:39` `mod errors;`
- `mod` `codex-rs/core/src/unified_exec/mod.rs:40` `mod head_tail_buffer;`
- `mod` `codex-rs/core/src/unified_exec/mod.rs:41` `mod process;`
- `mod` `codex-rs/core/src/unified_exec/mod.rs:42` `mod process_manager;`
- `impl` `codex-rs/core/src/unified_exec/mod.rs:65` `impl UnifiedExecContext {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:66` `pub fn new(session: Arc<Session>, turn: Arc<TurnContext>, call_id: String) -> Self {`
- `impl` `codex-rs/core/src/unified_exec/mod.rs:116` `impl ProcessStore {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:117` `fn remove(&mut self, process_id: &str) -> Option<ProcessEntry> {`
- `impl` `codex-rs/core/src/unified_exec/mod.rs:127` `impl Default for UnifiedExecProcessManager {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:128` `fn default() -> Self {`
- `struct` `codex-rs/core/src/unified_exec/mod.rs:135` `struct ProcessEntry {`
- `use` `codex-rs/core/src/unified_exec/mod.rs:162` `use super::head_tail_buffer::HeadTailBuffer;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:163` `use super::*;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:164` `use crate::codex::Session;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:165` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:166` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:167` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:168` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:169` `use crate::unified_exec::ExecCommandRequest;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:170` `use crate::unified_exec::WriteStdinRequest;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:171` `use core_test_support::skip_if_sandbox;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:172` `use std::sync::Arc;`
- `use` `codex-rs/core/src/unified_exec/mod.rs:173` `use tokio::time::Duration;`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:175` `async fn test_session_and_turn() -> (Arc<Session>, Arc<TurnContext>) {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:182` `async fn exec_command(`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:216` `async fn write_stdin(`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:235` `fn push_chunk_preserves_prefix_and_suffix() {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:257` `fn head_tail_buffer_default_preserves_prefix_and_suffix() {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:268` `async fn unified_exec_persists_across_requests() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:304` `async fn multi_unified_exec_sessions() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:356` `async fn unified_exec_timeouts() -> anyhow::Result<()> {`
- `const` `codex-rs/core/src/unified_exec/mod.rs:359` `const TEST_VAR_VALUE: &str = "unified_exec_var_123";`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:404` `async fn requests_with_large_timeout_are_capped() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:417` `async fn completed_commands_do_not_persist_sessions() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/unified_exec/mod.rs:442` `async fn reusing_completed_process_returns_unknown_process() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use rand::Rng;`
- `use rand::rng;`
- `use tokio::sync::Mutex;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::sandboxing::SandboxPermissions;`
- `use super::head_tail_buffer::HeadTailBuffer;`
- `use super::*;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::codex::make_session_and_context;`
- `use crate::protocol::AskForApproval;`
- `use crate::protocol::SandboxPolicy;`
- `use crate::unified_exec::ExecCommandRequest;`
- `use crate::unified_exec::WriteStdinRequest;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
