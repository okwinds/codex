# `codex-rs/core/src/agent/control.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22903`
- sha256: `fa571ccfbd5a98d18c4793a32808d91404360151581524127b2cabfc18441398`
- generated_utc: `2026-02-08T10:45:26Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/agent/control.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/agent/control.rs:1` `use crate::agent::AgentStatus;`
- `use` `codex-rs/core/src/agent/control.rs:2` `use crate::agent::guards::Guards;`
- `use` `codex-rs/core/src/agent/control.rs:3` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/agent/control.rs:4` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/agent/control.rs:5` `use crate::thread_manager::ThreadManagerState;`
- `use` `codex-rs/core/src/agent/control.rs:6` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/agent/control.rs:7` `use codex_protocol::protocol::Op;`
- `use` `codex-rs/core/src/agent/control.rs:8` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/agent/control.rs:9` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/agent/control.rs:10` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/agent/control.rs:11` `use std::sync::Arc;`
- `use` `codex-rs/core/src/agent/control.rs:12` `use std::sync::Weak;`
- `use` `codex-rs/core/src/agent/control.rs:13` `use tokio::sync::watch;`
- `impl` `codex-rs/core/src/agent/control.rs:30` `impl AgentControl {`
- `fn` `codex-rs/core/src/agent/control.rs:160` `fn upgrade(&self) -> CodexResult<Arc<ThreadManagerState>> {`
- `use` `codex-rs/core/src/agent/control.rs:169` `use super::*;`
- `use` `codex-rs/core/src/agent/control.rs:170` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/agent/control.rs:171` `use crate::CodexThread;`
- `use` `codex-rs/core/src/agent/control.rs:172` `use crate::ThreadManager;`
- `use` `codex-rs/core/src/agent/control.rs:173` `use crate::agent::agent_status_from_event;`
- `use` `codex-rs/core/src/agent/control.rs:174` `use crate::config::Config;`
- `use` `codex-rs/core/src/agent/control.rs:175` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/agent/control.rs:176` `use assert_matches::assert_matches;`
- `use` `codex-rs/core/src/agent/control.rs:177` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/agent/control.rs:178` `use codex_protocol::protocol::ErrorEvent;`
- `use` `codex-rs/core/src/agent/control.rs:179` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/agent/control.rs:180` `use codex_protocol::protocol::TurnAbortReason;`
- `use` `codex-rs/core/src/agent/control.rs:181` `use codex_protocol::protocol::TurnAbortedEvent;`
- `use` `codex-rs/core/src/agent/control.rs:182` `use codex_protocol::protocol::TurnCompleteEvent;`
- `use` `codex-rs/core/src/agent/control.rs:183` `use codex_protocol::protocol::TurnStartedEvent;`
- `use` `codex-rs/core/src/agent/control.rs:184` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/agent/control.rs:185` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/agent/control.rs:186` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/agent/control.rs:188` `async fn test_config_with_cli_overrides(`
- `fn` `codex-rs/core/src/agent/control.rs:201` `async fn test_config() -> (TempDir, Config) {`
- `struct` `codex-rs/core/src/agent/control.rs:205` `struct AgentControlHarness {`
- `impl` `codex-rs/core/src/agent/control.rs:212` `impl AgentControlHarness {`
- `fn` `codex-rs/core/src/agent/control.rs:213` `async fn new() -> Self {`
- `fn` `codex-rs/core/src/agent/control.rs:229` `async fn start_thread(&self) -> (ThreadId, Arc<CodexThread>) {`
- `fn` `codex-rs/core/src/agent/control.rs:240` `async fn send_prompt_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/agent/control.rs:253` `async fn get_status_returns_not_found_without_manager() {`
- `fn` `codex-rs/core/src/agent/control.rs:260` `async fn on_event_updates_status_from_task_started() {`
- `fn` `codex-rs/core/src/agent/control.rs:269` `async fn on_event_updates_status_from_task_complete() {`
- `fn` `codex-rs/core/src/agent/control.rs:278` `async fn on_event_updates_status_from_error() {`
- `fn` `codex-rs/core/src/agent/control.rs:289` `async fn on_event_updates_status_from_turn_aborted() {`
- `fn` `codex-rs/core/src/agent/control.rs:299` `async fn on_event_updates_status_from_shutdown_complete() {`
- `fn` `codex-rs/core/src/agent/control.rs:305` `async fn spawn_agent_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/agent/control.rs:319` `async fn resume_agent_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/agent/control.rs:337` `async fn send_prompt_errors_when_thread_missing() {`
- `fn` `codex-rs/core/src/agent/control.rs:349` `async fn get_status_returns_not_found_for_missing_thread() {`
- `fn` `codex-rs/core/src/agent/control.rs:356` `async fn get_status_returns_pending_init_for_new_thread() {`
- `fn` `codex-rs/core/src/agent/control.rs:364` `async fn subscribe_status_errors_for_missing_thread() {`
- `fn` `codex-rs/core/src/agent/control.rs:376` `async fn subscribe_status_updates_on_shutdown() {`
- `fn` `codex-rs/core/src/agent/control.rs:396` `async fn send_prompt_submits_user_message() {`
- `fn` `codex-rs/core/src/agent/control.rs:425` `async fn spawn_agent_creates_thread_and_sends_prompt() {`
- `fn` `codex-rs/core/src/agent/control.rs:456` `async fn spawn_agent_respects_max_threads_limit() {`
- `fn` `codex-rs/core/src/agent/control.rs:499` `async fn spawn_agent_releases_slot_after_shutdown() {`
- `fn` `codex-rs/core/src/agent/control.rs:533` `async fn spawn_agent_limit_shared_across_clones() {`
- `fn` `codex-rs/core/src/agent/control.rs:569` `async fn resume_agent_respects_max_threads_limit() {`
- `fn` `codex-rs/core/src/agent/control.rs:622` `async fn resume_agent_releases_slot_after_resume_failure() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::agent::AgentStatus;`
- `use crate::agent::guards::Guards;`
- `use crate::error::CodexErr;`
- `use crate::error::Result as CodexResult;`
- `use crate::thread_manager::ThreadManagerState;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::Op;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::user_input::UserInput;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::Weak;`
- `use tokio::sync::watch;`
- `use super::*;`
- `use crate::CodexAuth;`
- `use crate::CodexThread;`
- `use crate::ThreadManager;`
- `use crate::agent::agent_status_from_event;`
- `use crate::config::Config;`
- `use crate::config::ConfigBuilder;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
