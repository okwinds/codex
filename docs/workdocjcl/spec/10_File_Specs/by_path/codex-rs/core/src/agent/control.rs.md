# `codex-rs/core/src/agent/control.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18315`
- sha256: `3f4a33cea9f04fc40a7a02549710c4301c01c514d0b13912401b8a1418de1127`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/agent/control.rs:8` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/agent/control.rs:9` `use std::sync::Arc;`
- `use` `codex-rs/core/src/agent/control.rs:10` `use std::sync::Weak;`
- `use` `codex-rs/core/src/agent/control.rs:11` `use tokio::sync::watch;`
- `impl` `codex-rs/core/src/agent/control.rs:28` `impl AgentControl {`
- `fn` `codex-rs/core/src/agent/control.rs:132` `fn upgrade(&self) -> CodexResult<Arc<ThreadManagerState>> {`
- `use` `codex-rs/core/src/agent/control.rs:141` `use super::*;`
- `use` `codex-rs/core/src/agent/control.rs:142` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/agent/control.rs:143` `use crate::CodexThread;`
- `use` `codex-rs/core/src/agent/control.rs:144` `use crate::ThreadManager;`
- `use` `codex-rs/core/src/agent/control.rs:145` `use crate::agent::agent_status_from_event;`
- `use` `codex-rs/core/src/agent/control.rs:146` `use crate::config::Config;`
- `use` `codex-rs/core/src/agent/control.rs:147` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/agent/control.rs:148` `use assert_matches::assert_matches;`
- `use` `codex-rs/core/src/agent/control.rs:149` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/agent/control.rs:150` `use codex_protocol::protocol::ErrorEvent;`
- `use` `codex-rs/core/src/agent/control.rs:151` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/agent/control.rs:152` `use codex_protocol::protocol::TurnAbortReason;`
- `use` `codex-rs/core/src/agent/control.rs:153` `use codex_protocol::protocol::TurnAbortedEvent;`
- `use` `codex-rs/core/src/agent/control.rs:154` `use codex_protocol::protocol::TurnCompleteEvent;`
- `use` `codex-rs/core/src/agent/control.rs:155` `use codex_protocol::protocol::TurnStartedEvent;`
- `use` `codex-rs/core/src/agent/control.rs:156` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/agent/control.rs:157` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/agent/control.rs:158` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/agent/control.rs:160` `async fn test_config_with_cli_overrides(`
- `fn` `codex-rs/core/src/agent/control.rs:173` `async fn test_config() -> (TempDir, Config) {`
- `struct` `codex-rs/core/src/agent/control.rs:177` `struct AgentControlHarness {`
- `impl` `codex-rs/core/src/agent/control.rs:184` `impl AgentControlHarness {`
- `fn` `codex-rs/core/src/agent/control.rs:185` `async fn new() -> Self {`
- `fn` `codex-rs/core/src/agent/control.rs:201` `async fn start_thread(&self) -> (ThreadId, Arc<CodexThread>) {`
- `fn` `codex-rs/core/src/agent/control.rs:212` `async fn send_prompt_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/agent/control.rs:225` `async fn get_status_returns_not_found_without_manager() {`
- `fn` `codex-rs/core/src/agent/control.rs:232` `async fn on_event_updates_status_from_task_started() {`
- `fn` `codex-rs/core/src/agent/control.rs:241` `async fn on_event_updates_status_from_task_complete() {`
- `fn` `codex-rs/core/src/agent/control.rs:250` `async fn on_event_updates_status_from_error() {`
- `fn` `codex-rs/core/src/agent/control.rs:261` `async fn on_event_updates_status_from_turn_aborted() {`
- `fn` `codex-rs/core/src/agent/control.rs:271` `async fn on_event_updates_status_from_shutdown_complete() {`
- `fn` `codex-rs/core/src/agent/control.rs:277` `async fn spawn_agent_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/agent/control.rs:291` `async fn send_prompt_errors_when_thread_missing() {`
- `fn` `codex-rs/core/src/agent/control.rs:303` `async fn get_status_returns_not_found_for_missing_thread() {`
- `fn` `codex-rs/core/src/agent/control.rs:310` `async fn get_status_returns_pending_init_for_new_thread() {`
- `fn` `codex-rs/core/src/agent/control.rs:318` `async fn subscribe_status_errors_for_missing_thread() {`
- `fn` `codex-rs/core/src/agent/control.rs:330` `async fn subscribe_status_updates_on_shutdown() {`
- `fn` `codex-rs/core/src/agent/control.rs:350` `async fn send_prompt_submits_user_message() {`
- `fn` `codex-rs/core/src/agent/control.rs:379` `async fn spawn_agent_creates_thread_and_sends_prompt() {`
- `fn` `codex-rs/core/src/agent/control.rs:410` `async fn spawn_agent_respects_max_threads_limit() {`
- `fn` `codex-rs/core/src/agent/control.rs:453` `async fn spawn_agent_releases_slot_after_shutdown() {`
- `fn` `codex-rs/core/src/agent/control.rs:487` `async fn spawn_agent_limit_shared_across_clones() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::agent::AgentStatus;`
- `use crate::agent::guards::Guards;`
- `use crate::error::CodexErr;`
- `use crate::error::Result as CodexResult;`
- `use crate::thread_manager::ThreadManagerState;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::Op;`
- `use codex_protocol::user_input::UserInput;`
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
- `use assert_matches::assert_matches;`
- `use codex_protocol::config_types::ModeKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
