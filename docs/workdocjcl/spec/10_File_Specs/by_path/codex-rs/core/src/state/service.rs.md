# `codex-rs/core/src/state/service.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1716`
- sha256: `7d0903c9d9e661c81d134bda1d655892b80d0bf5b4fe25457282d3fe0d64eb16`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/state/service.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/state/service.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/state/service.rs:3` `use crate::AuthManager;`
- `use` `codex-rs/core/src/state/service.rs:4` `use crate::RolloutRecorder;`
- `use` `codex-rs/core/src/state/service.rs:5` `use crate::agent::AgentControl;`
- `use` `codex-rs/core/src/state/service.rs:6` `use crate::analytics_client::AnalyticsEventsClient;`
- `use` `codex-rs/core/src/state/service.rs:7` `use crate::client::ModelClient;`
- `use` `codex-rs/core/src/state/service.rs:8` `use crate::exec_policy::ExecPolicyManager;`
- `use` `codex-rs/core/src/state/service.rs:9` `use crate::file_watcher::FileWatcher;`
- `use` `codex-rs/core/src/state/service.rs:10` `use crate::hooks::Hooks;`
- `use` `codex-rs/core/src/state/service.rs:11` `use crate::mcp_connection_manager::McpConnectionManager;`
- `use` `codex-rs/core/src/state/service.rs:12` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/state/service.rs:13` `use crate::skills::SkillsManager;`
- `use` `codex-rs/core/src/state/service.rs:14` `use crate::state_db::StateDbHandle;`
- `use` `codex-rs/core/src/state/service.rs:15` `use crate::tools::sandboxing::ApprovalStore;`
- `use` `codex-rs/core/src/state/service.rs:16` `use crate::unified_exec::UnifiedExecProcessManager;`
- `use` `codex-rs/core/src/state/service.rs:17` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/state/service.rs:18` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/state/service.rs:19` `use tokio::sync::RwLock;`
- `use` `codex-rs/core/src/state/service.rs:20` `use tokio_util::sync::CancellationToken;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use crate::AuthManager;`
- `use crate::RolloutRecorder;`
- `use crate::agent::AgentControl;`
- `use crate::analytics_client::AnalyticsEventsClient;`
- `use crate::client::ModelClient;`
- `use crate::exec_policy::ExecPolicyManager;`
- `use crate::file_watcher::FileWatcher;`
- `use crate::hooks::Hooks;`
- `use crate::mcp_connection_manager::McpConnectionManager;`
- `use crate::models_manager::manager::ModelsManager;`
- `use crate::skills::SkillsManager;`
- `use crate::state_db::StateDbHandle;`
- `use crate::tools::sandboxing::ApprovalStore;`
- `use crate::unified_exec::UnifiedExecProcessManager;`
- `use codex_otel::OtelManager;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::RwLock;`
- `use tokio_util::sync::CancellationToken;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
