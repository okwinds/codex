# `codex-rs/core/src/unified_exec/process_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `27179`
- sha256: `2b4f2be4d74247b806cf680a9fa3c9a013d70200009a4e155ea3b8e2856f0e43`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/unified_exec/process_manager.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:1` `use rand::Rng;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:2` `use std::cmp::Reverse;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:3` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:4` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:5` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:6` `use std::sync::Arc;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:7` `use tokio::sync::Notify;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:8` `use tokio::sync::mpsc;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:9` `use tokio::time::Duration;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:10` `use tokio::time::Instant;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:11` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:13` `use crate::exec_env::create_env;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:14` `use crate::exec_policy::ExecApprovalRequest;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:15` `use crate::protocol::ExecCommandSource;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:16` `use crate::sandboxing::ExecEnv;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:17` `use crate::tools::events::ToolEmitter;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:18` `use crate::tools::events::ToolEventCtx;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:19` `use crate::tools::events::ToolEventStage;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:20` `use crate::tools::orchestrator::ToolOrchestrator;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:21` `use crate::tools::runtimes::unified_exec::UnifiedExecRequest as UnifiedExecToolRequest;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:22` `use crate::tools::runtimes::unified_exec::UnifiedExecRuntime;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:23` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:24` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:25` `use crate::truncate::approx_token_count;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:26` `use crate::truncate::formatted_truncate_text;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:27` `use crate::unified_exec::ExecCommandRequest;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:28` `use crate::unified_exec::MAX_UNIFIED_EXEC_PROCESSES;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:29` `use crate::unified_exec::MAX_YIELD_TIME_MS;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:30` `use crate::unified_exec::MIN_EMPTY_YIELD_TIME_MS;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:31` `use crate::unified_exec::ProcessEntry;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:32` `use crate::unified_exec::ProcessStore;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:33` `use crate::unified_exec::UnifiedExecContext;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:34` `use crate::unified_exec::UnifiedExecError;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:35` `use crate::unified_exec::UnifiedExecProcessManager;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:36` `use crate::unified_exec::UnifiedExecResponse;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:37` `use crate::unified_exec::WARNING_UNIFIED_EXEC_PROCESSES;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:38` `use crate::unified_exec::WriteStdinRequest;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:39` `use crate::unified_exec::async_watcher::emit_exec_end_for_unified_exec;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:40` `use crate::unified_exec::async_watcher::spawn_exit_watcher;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:41` `use crate::unified_exec::async_watcher::start_streaming_output;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:42` `use crate::unified_exec::clamp_yield_time;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:43` `use crate::unified_exec::generate_chunk_id;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:44` `use crate::unified_exec::head_tail_buffer::HeadTailBuffer;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:45` `use crate::unified_exec::process::OutputBuffer;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:46` `use crate::unified_exec::process::OutputHandles;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:47` `use crate::unified_exec::process::UnifiedExecProcess;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:48` `use crate::unified_exec::resolve_max_tokens;`
- `const` `codex-rs/core/src/unified_exec/process_manager.rs:50` `const UNIFIED_EXEC_ENV: [(&str, &str); 10] = [`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:63` `fn apply_unified_exec_env(mut env: HashMap<String, String>) -> HashMap<String, String> {`
- `struct` `codex-rs/core/src/unified_exec/process_manager.rs:70` `struct PreparedProcessHandles {`
- `impl` `codex-rs/core/src/unified_exec/process_manager.rs:80` `impl UnifiedExecProcessManager {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:330` `async fn refresh_process_state(&self, process_id: &str) -> ProcessStatus {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:356` `async fn prepare_process_handles(`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:386` `async fn send_input(`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:397` `async fn store_process(`
- `const` `codex-rs/core/src/unified_exec/process_manager.rs:536` `const POST_EXIT_OUTPUT_GRACE: Duration = Duration::from_millis(50);`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:591` `fn prune_processes_if_needed(store: &mut ProcessStore) -> bool {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:613` `fn process_id_to_prune_from_meta(meta: &[(String, Instant, bool)]) -> Option<String> {`
- `enum` `codex-rs/core/src/unified_exec/process_manager.rs:659` `enum ProcessStatus {`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:674` `use super::*;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:675` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:676` `use tokio::time::Duration;`
- `use` `codex-rs/core/src/unified_exec/process_manager.rs:677` `use tokio::time::Instant;`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:680` `fn unified_exec_env_injects_defaults() {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:699` `fn unified_exec_env_overrides_existing_values() {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:711` `fn pruning_prefers_exited_processes_outside_recently_used() {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:733` `fn pruning_falls_back_to_lru_when_no_exited() {`
- `fn` `codex-rs/core/src/unified_exec/process_manager.rs:755` `fn pruning_protects_recent_processes_even_if_exited() {`

## Dependencies (auto sample)
### Imports / Includes
- `use rand::Rng;`
- `use std::cmp::Reverse;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use tokio::sync::Notify;`
- `use tokio::sync::mpsc;`
- `use tokio::time::Duration;`
- `use tokio::time::Instant;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::exec_env::create_env;`
- `use crate::exec_policy::ExecApprovalRequest;`
- `use crate::protocol::ExecCommandSource;`
- `use crate::sandboxing::ExecEnv;`
- `use crate::tools::events::ToolEmitter;`
- `use crate::tools::events::ToolEventCtx;`
- `use crate::tools::events::ToolEventStage;`
- `use crate::tools::orchestrator::ToolOrchestrator;`
- `use crate::tools::runtimes::unified_exec::UnifiedExecRequest as UnifiedExecToolRequest;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
