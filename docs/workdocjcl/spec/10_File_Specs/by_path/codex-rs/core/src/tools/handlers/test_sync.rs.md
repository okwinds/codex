# `codex-rs/core/src/tools/handlers/test_sync.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4556`
- sha256: `8a3b2c8b9d2f5a43f3a9897fa248b8ae52e1a9a788578147abcb89ac9a9d98a0`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/test_sync.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct TestSyncHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:1` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:2` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:3` `use std::collections::hash_map::Entry;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:5` `use std::sync::OnceLock;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:6` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:8` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:9` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:10` `use tokio::sync::Barrier;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:11` `use tokio::time::sleep;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:13` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:14` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:15` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:16` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:17` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:18` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/test_sync.rs:19` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/test_sync.rs:21` `pub struct TestSyncHandler;`
- `const` `codex-rs/core/src/tools/handlers/test_sync.rs:23` `const DEFAULT_TIMEOUT_MS: u64 = 1_000;`
- `static` `codex-rs/core/src/tools/handlers/test_sync.rs:25` `static BARRIERS: OnceLock<tokio::sync::Mutex<HashMap<String, BarrierState>>> = OnceLock::new();`
- `struct` `codex-rs/core/src/tools/handlers/test_sync.rs:27` `struct BarrierState {`
- `struct` `codex-rs/core/src/tools/handlers/test_sync.rs:33` `struct BarrierArgs {`
- `struct` `codex-rs/core/src/tools/handlers/test_sync.rs:41` `struct TestSyncArgs {`
- `fn` `codex-rs/core/src/tools/handlers/test_sync.rs:50` `fn default_timeout_ms() -> u64 {`
- `fn` `codex-rs/core/src/tools/handlers/test_sync.rs:54` `fn barrier_map() -> &'static tokio::sync::Mutex<HashMap<String, BarrierState>> {`
- `impl` `codex-rs/core/src/tools/handlers/test_sync.rs:59` `impl ToolHandler for TestSyncHandler {`
- `fn` `codex-rs/core/src/tools/handlers/test_sync.rs:60` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/test_sync.rs:64` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/test_sync.rs:101` `async fn wait_on_barrier(args: BarrierArgs) -> Result<(), FunctionCallError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use std::collections::HashMap;`
- `use std::collections::hash_map::Entry;`
- `use std::sync::Arc;`
- `use std::sync::OnceLock;`
- `use std::time::Duration;`
- `use async_trait::async_trait;`
- `use serde::Deserialize;`
- `use tokio::sync::Barrier;`
- `use tokio::time::sleep;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
