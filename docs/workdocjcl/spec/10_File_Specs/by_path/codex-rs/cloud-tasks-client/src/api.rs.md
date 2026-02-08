# `codex-rs/cloud-tasks-client/src/api.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4860`
- sha256: `3320e612c20fc7445e11615ba296cf456a715a4a414b71920f292d4d6148eea5`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks-client/src/api.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum CloudTaskError {`
- `pub struct TaskId(pub String);`
- `pub enum TaskStatus {`
- `pub struct TaskSummary {`
- `pub enum AttemptStatus {`
- `pub struct TurnAttempt {`
- `pub enum ApplyStatus {`
- `pub struct ApplyOutcome {`
- `pub struct CreatedTask {`
- `pub struct TaskListPage {`
- `pub struct DiffSummary {`
- `pub struct TaskText {`
- `pub trait CloudBackend: Send + Sync {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks-client/src/api.rs:1` `use chrono::DateTime;`
- `use` `codex-rs/cloud-tasks-client/src/api.rs:2` `use chrono::Utc;`
- `use` `codex-rs/cloud-tasks-client/src/api.rs:3` `use serde::Deserialize;`
- `use` `codex-rs/cloud-tasks-client/src/api.rs:4` `use serde::Serialize;`
- `type` `codex-rs/cloud-tasks-client/src/api.rs:6` `pub type Result<T> = std::result::Result<T, CloudTaskError>;`
- `enum` `codex-rs/cloud-tasks-client/src/api.rs:9` `pub enum CloudTaskError {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:22` `pub struct TaskId(pub String);`
- `enum` `codex-rs/cloud-tasks-client/src/api.rs:26` `pub enum TaskStatus {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:34` `pub struct TaskSummary {`
- `enum` `codex-rs/cloud-tasks-client/src/api.rs:53` `pub enum AttemptStatus {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:64` `pub struct TurnAttempt {`
- `enum` `codex-rs/cloud-tasks-client/src/api.rs:75` `pub enum ApplyStatus {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:82` `pub struct ApplyOutcome {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:93` `pub struct CreatedTask {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:98` `pub struct TaskListPage {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:104` `pub struct DiffSummary {`
- `struct` `codex-rs/cloud-tasks-client/src/api.rs:111` `pub struct TaskText {`
- `impl` `codex-rs/cloud-tasks-client/src/api.rs:120` `impl Default for TaskText {`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:121` `fn default() -> Self {`
- `trait` `codex-rs/cloud-tasks-client/src/api.rs:134` `pub trait CloudBackend: Send + Sync {`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:135` `async fn list_tasks(`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:141` `async fn get_task_summary(&self, id: TaskId) -> Result<TaskSummary>;`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:142` `async fn get_task_diff(&self, id: TaskId) -> Result<Option<String>>;`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:144` `async fn get_task_messages(&self, id: TaskId) -> Result<Vec<String>>;`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:146` `async fn get_task_text(&self, id: TaskId) -> Result<TaskText>;`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:148` `async fn list_sibling_attempts(`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:156` `async fn apply_task_preflight(`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:161` `async fn apply_task(&self, id: TaskId, diff_override: Option<String>) -> Result<ApplyOutcome>;`
- `fn` `codex-rs/cloud-tasks-client/src/api.rs:162` `async fn create_task(`

## Dependencies (auto sample)
### Imports / Includes
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
