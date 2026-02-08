# `codex-rs/core/src/tasks/ghost_snapshot.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11104`
- sha256: `dd9800c2ce65ffd252afbd7948e57f1f22f13c29e380ad9eed67719054b46b27`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/ghost_snapshot.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:1` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:2` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:3` `use crate::protocol::WarningEvent;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:4` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:5` `use crate::tasks::SessionTask;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:6` `use crate::tasks::SessionTaskContext;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:7` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:8` `use codex_git::CreateGhostCommitOptions;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:9` `use codex_git::GhostSnapshotReport;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:10` `use codex_git::GitToolingError;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:11` `use codex_git::create_ghost_commit_with_report;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:12` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:13` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:14` `use codex_utils_readiness::Readiness;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:15` `use codex_utils_readiness::Token;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:16` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:17` `use std::time::Duration;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:18` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:19` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:20` `use tracing::info;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:21` `use tracing::warn;`
- `const` `codex-rs/core/src/tasks/ghost_snapshot.rs:27` `const SNAPSHOT_WARNING_THRESHOLD: Duration = Duration::from_secs(240);`
- `impl` `codex-rs/core/src/tasks/ghost_snapshot.rs:30` `impl SessionTask for GhostSnapshotTask {`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:31` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:35` `async fn run(`
- `impl` `codex-rs/core/src/tasks/ghost_snapshot.rs:159` `impl GhostSnapshotTask {`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:165` `fn format_snapshot_warnings(`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:182` `fn format_large_untracked_warning(`
- `const` `codex-rs/core/src/tasks/ghost_snapshot.rs:190` `const MAX_DIRS: usize = 3;`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:205` `fn format_ignored_untracked_files_warning(`
- `const` `codex-rs/core/src/tasks/ghost_snapshot.rs:214` `const MAX_FILES: usize = 3;`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:235` `fn format_bytes(bytes: i64) -> String {`
- `const` `codex-rs/core/src/tasks/ghost_snapshot.rs:236` `const KIB: i64 = 1024;`
- `const` `codex-rs/core/src/tasks/ghost_snapshot.rs:237` `const MIB: i64 = 1024 * 1024;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:250` `use super::*;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:251` `use codex_git::LargeUntrackedDir;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:252` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tasks/ghost_snapshot.rs:253` `use std::path::PathBuf;`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:256` `fn large_untracked_warning_includes_threshold() {`
- `fn` `codex-rs/core/src/tasks/ghost_snapshot.rs:270` `fn large_untracked_warning_disabled_when_threshold_disabled() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::TurnContext;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::WarningEvent;`
- `use crate::state::TaskKind;`
- `use crate::tasks::SessionTask;`
- `use crate::tasks::SessionTaskContext;`
- `use async_trait::async_trait;`
- `use codex_git::CreateGhostCommitOptions;`
- `use codex_git::GhostSnapshotReport;`
- `use codex_git::GitToolingError;`
- `use codex_git::create_ghost_commit_with_report;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::user_input::UserInput;`
- `use codex_utils_readiness::Readiness;`
- `use codex_utils_readiness::Token;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use tokio::sync::oneshot;`
- `use tokio_util::sync::CancellationToken;`
- `use tracing::info;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
