# `codex-rs/cloud-tasks-client/src/mock.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6824`
- sha256: `47212e968baafc6d7a0b622740cd45d57abdd943528b433138549f59c9d07e58`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks-client/src/mock.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct MockClient;`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:1` `use crate::ApplyOutcome;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:2` `use crate::AttemptStatus;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:3` `use crate::CloudBackend;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:4` `use crate::CloudTaskError;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:5` `use crate::DiffSummary;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:6` `use crate::Result;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:7` `use crate::TaskId;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:8` `use crate::TaskStatus;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:9` `use crate::TaskSummary;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:10` `use crate::TurnAttempt;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:11` `use crate::api::TaskText;`
- `use` `codex-rs/cloud-tasks-client/src/mock.rs:12` `use chrono::Utc;`
- `struct` `codex-rs/cloud-tasks-client/src/mock.rs:15` `pub struct MockClient;`
- `impl` `codex-rs/cloud-tasks-client/src/mock.rs:18` `impl CloudBackend for MockClient {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:19` `async fn list_tasks(`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:72` `async fn get_task_summary(&self, id: TaskId) -> Result<TaskSummary> {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:80` `async fn get_task_diff(&self, id: TaskId) -> Result<Option<String>> {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:84` `async fn get_task_messages(&self, _id: TaskId) -> Result<Vec<String>> {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:90` `async fn get_task_text(&self, _id: TaskId) -> Result<TaskText> {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:101` `async fn apply_task(&self, id: TaskId, _diff_override: Option<String>) -> Result<ApplyOutcome> {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:111` `async fn apply_task_preflight(`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:125` `async fn list_sibling_attempts(`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:143` `async fn create_task(`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:157` `fn mock_diff_for(id: &TaskId) -> String {`
- `fn` `codex-rs/cloud-tasks-client/src/mock.rs:171` `fn count_from_unified(diff: &str) -> (usize, usize) {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::ApplyOutcome;`
- `use crate::AttemptStatus;`
- `use crate::CloudBackend;`
- `use crate::CloudTaskError;`
- `use crate::DiffSummary;`
- `use crate::Result;`
- `use crate::TaskId;`
- `use crate::TaskStatus;`
- `use crate::TaskSummary;`
- `use crate::TurnAttempt;`
- `use crate::api::TaskText;`
- `use chrono::Utc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
