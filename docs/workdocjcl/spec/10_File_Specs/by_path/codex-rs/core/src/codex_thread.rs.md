# `codex-rs/core/src/codex_thread.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2165`
- sha256: `75b22ee07c49f4b38f1fca8356bae5831af6a7dbd5abe2ed1466e0cfb16a65ea`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/codex_thread.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ThreadConfigSnapshot {`
- `pub struct CodexThread {`
- `pub fn rollout_path(&self) -> Option<PathBuf> {`
- `pub fn state_db(&self) -> Option<StateDbHandle> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/codex_thread.rs:1` `use crate::agent::AgentStatus;`
- `use` `codex-rs/core/src/codex_thread.rs:2` `use crate::codex::Codex;`
- `use` `codex-rs/core/src/codex_thread.rs:3` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/codex_thread.rs:4` `use crate::protocol::Event;`
- `use` `codex-rs/core/src/codex_thread.rs:5` `use crate::protocol::Op;`
- `use` `codex-rs/core/src/codex_thread.rs:6` `use crate::protocol::Submission;`
- `use` `codex-rs/core/src/codex_thread.rs:7` `use codex_protocol::config_types::Personality;`
- `use` `codex-rs/core/src/codex_thread.rs:8` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/codex_thread.rs:9` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/codex_thread.rs:10` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/codex_thread.rs:11` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/codex_thread.rs:12` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/codex_thread.rs:13` `use tokio::sync::watch;`
- `use` `codex-rs/core/src/codex_thread.rs:15` `use crate::state_db::StateDbHandle;`
- `struct` `codex-rs/core/src/codex_thread.rs:18` `pub struct ThreadConfigSnapshot {`
- `struct` `codex-rs/core/src/codex_thread.rs:29` `pub struct CodexThread {`
- `impl` `codex-rs/core/src/codex_thread.rs:36` `impl CodexThread {`
- `fn` `codex-rs/core/src/codex_thread.rs:44` `pub async fn submit(&self, op: Op) -> CodexResult<String> {`
- `fn` `codex-rs/core/src/codex_thread.rs:49` `pub async fn submit_with_id(&self, sub: Submission) -> CodexResult<()> {`
- `fn` `codex-rs/core/src/codex_thread.rs:53` `pub async fn next_event(&self) -> CodexResult<Event> {`
- `fn` `codex-rs/core/src/codex_thread.rs:57` `pub async fn agent_status(&self) -> AgentStatus {`
- `fn` `codex-rs/core/src/codex_thread.rs:65` `pub fn rollout_path(&self) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/codex_thread.rs:69` `pub fn state_db(&self) -> Option<StateDbHandle> {`
- `fn` `codex-rs/core/src/codex_thread.rs:73` `pub async fn config_snapshot(&self) -> ThreadConfigSnapshot {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::agent::AgentStatus;`
- `use crate::codex::Codex;`
- `use crate::error::Result as CodexResult;`
- `use crate::protocol::Event;`
- `use crate::protocol::Op;`
- `use crate::protocol::Submission;`
- `use codex_protocol::config_types::Personality;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::protocol::SessionSource;`
- `use std::path::PathBuf;`
- `use tokio::sync::watch;`
- `use crate::state_db::StateDbHandle;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
