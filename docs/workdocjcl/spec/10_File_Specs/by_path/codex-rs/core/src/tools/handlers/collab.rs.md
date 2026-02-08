# `codex-rs/core/src/tools/handlers/collab.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `42847`
- sha256: `4c4af891e50973ad4fd70cba497453779af9aee78196485c75535755fadaf60a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/collab.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CollabHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/collab.rs:1` `use crate::agent::AgentStatus;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:2` `use crate::agent::exceeds_thread_spawn_depth_limit;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:3` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:4` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:5` `use crate::config::Config;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:6` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:7` `use crate::features::Feature;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:8` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:9` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:10` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:11` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:12` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:13` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:14` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:15` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:16` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:17` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:18` `use codex_protocol::protocol::CollabAgentInteractionBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:19` `use codex_protocol::protocol::CollabAgentInteractionEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:20` `use codex_protocol::protocol::CollabAgentSpawnBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:21` `use codex_protocol::protocol::CollabAgentSpawnEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:22` `use codex_protocol::protocol::CollabCloseBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:23` `use codex_protocol::protocol::CollabCloseEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:24` `use codex_protocol::protocol::CollabWaitingBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:25` `use codex_protocol::protocol::CollabWaitingEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:26` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:27` `use serde::Serialize;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:29` `pub struct CollabHandler;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:37` `struct CloseAgentArgs {`
- `impl` `codex-rs/core/src/tools/handlers/collab.rs:42` `impl ToolHandler for CollabHandler {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:43` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:47` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:51` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:83` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:84` `use crate::agent::AgentRole;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:86` `use crate::agent::exceeds_thread_spawn_depth_limit;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:87` `use crate::agent::next_thread_spawn_depth;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:88` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:89` `use codex_protocol::protocol::SubAgentSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:90` `use std::sync::Arc;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:93` `struct SpawnAgentArgs {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:99` `struct SpawnAgentResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:103` `pub async fn handle(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:195` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:196` `use std::sync::Arc;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:199` `struct SendInputArgs {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:207` `struct SendInputResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:211` `pub async fn handle(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:284` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:285` `use crate::agent::status::is_final;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:286` `use futures::FutureExt;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:287` `use futures::StreamExt;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:288` `use futures::stream::FuturesUnordered;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:289` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:290` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:291` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:292` `use tokio::sync::watch::Receiver;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:293` `use tokio::time::Instant;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:295` `use tokio::time::timeout_at;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:298` `struct WaitArgs {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:304` `struct WaitResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:309` `pub async fn handle(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:450` `async fn wait_for_final_status(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:474` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:475` `use std::sync::Arc;`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:482` `pub async fn handle(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:562` `fn agent_id(id: &str) -> Result<ThreadId, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:567` `fn collab_spawn_error(err: CodexErr) -> FunctionCallError {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:576` `fn collab_agent_error(agent_id: ThreadId, err: CodexErr) -> FunctionCallError {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:591` `fn build_agent_spawn_config(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:631` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:632` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:633` `use crate::ThreadManager;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:634` `use crate::agent::MAX_THREAD_SPAWN_DEPTH;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:635` `use crate::built_in_model_providers;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:636` `use crate::client::ModelClient;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:637` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:638` `use crate::config::types::ShellEnvironmentPolicy;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:639` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:640` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:641` `use crate::protocol::Op;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:642` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:643` `use crate::protocol::SessionSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:644` `use crate::protocol::SubAgentSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:645` `use crate::turn_diff_tracker::TurnDiffTracker;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:646` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:647` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:648` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:649` `use serde_json::json;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:650` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:651` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:652` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:653` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:654` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:655` `use tokio::time::timeout;`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:657` `fn invocation(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:673` `fn function_payload(args: serde_json::Value) -> ToolPayload {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:679` `fn thread_manager() -> ThreadManager {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:687` `async fn handler_rejects_non_function_payloads() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:709` `async fn handler_rejects_unknown_tool() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:727` `async fn spawn_agent_rejects_empty_message() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:747` `async fn spawn_agent_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:765` `async fn spawn_agent_rejects_when_depth_limit_exceeded() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:805` `async fn send_input_rejects_empty_message() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:825` `async fn send_input_rejects_invalid_id() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:843` `async fn send_input_reports_missing_agent() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:864` `async fn send_input_interrupts_before_prompt() {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:903` `struct WaitResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:909` `async fn wait_rejects_non_positive_timeout() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:930` `async fn wait_rejects_invalid_id() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:948` `async fn wait_rejects_empty_ids() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:966` `async fn wait_returns_not_found_for_missing_agents() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1007` `async fn wait_times_out_when_status_is_not_final() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1052` `async fn wait_clamps_short_timeouts_to_minimum() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1083` `async fn wait_returns_final_status_without_timeout() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1137` `async fn close_agent_submits_shutdown_and_returns_status() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1178` `async fn build_agent_spawn_config_uses_turn_context_values() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1219` `async fn build_agent_spawn_config_preserves_base_user_instructions() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::agent::AgentStatus;`
- `use crate::agent::exceeds_thread_spawn_depth_limit;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::config::Config;`
- `use crate::error::CodexErr;`
- `use crate::features::Feature;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use async_trait::async_trait;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::BaseInstructions;`
- `use codex_protocol::protocol::CollabAgentInteractionBeginEvent;`
- `use codex_protocol::protocol::CollabAgentInteractionEndEvent;`
- `use codex_protocol::protocol::CollabAgentSpawnBeginEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
