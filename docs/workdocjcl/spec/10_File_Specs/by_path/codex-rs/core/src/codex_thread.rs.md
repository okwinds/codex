# `codex-rs/core/src/codex_thread.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2471`
- sha256: `3037d503f94e98c757c3c068d78af9d1f66874c47aeaca93bb4d627c44ea81a0`
- generated_utc: `2026-02-08T10:45:26Z`

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
- `use` `codex-rs/core/src/codex_thread.rs:3` `use crate::codex::SteerInputError;`
- `use` `codex-rs/core/src/codex_thread.rs:4` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/codex_thread.rs:5` `use crate::protocol::Event;`
- `use` `codex-rs/core/src/codex_thread.rs:6` `use crate::protocol::Op;`
- `use` `codex-rs/core/src/codex_thread.rs:7` `use crate::protocol::Submission;`
- `use` `codex-rs/core/src/codex_thread.rs:8` `use codex_protocol::config_types::Personality;`
- `use` `codex-rs/core/src/codex_thread.rs:9` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/codex_thread.rs:10` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/codex_thread.rs:11` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/codex_thread.rs:12` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/codex_thread.rs:13` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/codex_thread.rs:14` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/codex_thread.rs:15` `use tokio::sync::watch;`
- `use` `codex-rs/core/src/codex_thread.rs:17` `use crate::state_db::StateDbHandle;`
- `struct` `codex-rs/core/src/codex_thread.rs:20` `pub struct ThreadConfigSnapshot {`
- `struct` `codex-rs/core/src/codex_thread.rs:31` `pub struct CodexThread {`
- `impl` `codex-rs/core/src/codex_thread.rs:38` `impl CodexThread {`
- `fn` `codex-rs/core/src/codex_thread.rs:46` `pub async fn submit(&self, op: Op) -> CodexResult<String> {`
- `fn` `codex-rs/core/src/codex_thread.rs:50` `pub async fn steer_input(`
- `fn` `codex-rs/core/src/codex_thread.rs:59` `pub async fn submit_with_id(&self, sub: Submission) -> CodexResult<()> {`
- `fn` `codex-rs/core/src/codex_thread.rs:63` `pub async fn next_event(&self) -> CodexResult<Event> {`
- `fn` `codex-rs/core/src/codex_thread.rs:67` `pub async fn agent_status(&self) -> AgentStatus {`
- `fn` `codex-rs/core/src/codex_thread.rs:75` `pub fn rollout_path(&self) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/codex_thread.rs:79` `pub fn state_db(&self) -> Option<StateDbHandle> {`
- `fn` `codex-rs/core/src/codex_thread.rs:83` `pub async fn config_snapshot(&self) -> ThreadConfigSnapshot {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::agent::AgentStatus;`
- `use crate::codex::Codex;`
- `use crate::codex::SteerInputError;`
- `use crate::error::Result as CodexResult;`
- `use crate::protocol::Event;`
- `use crate::protocol::Op;`
- `use crate::protocol::Submission;`
- `use codex_protocol::config_types::Personality;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::user_input::UserInput;`
- `use std::path::PathBuf;`
- `use tokio::sync::watch;`
- `use crate::state_db::StateDbHandle;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
