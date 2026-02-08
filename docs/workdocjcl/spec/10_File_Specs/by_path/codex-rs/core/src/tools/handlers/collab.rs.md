# `codex-rs/core/src/tools/handlers/collab.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `57482`
- sha256: `5c4624b62572560af2bb2ea00a6d12f94dc722311c8df4b094dbcef703bc5496`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/tools/handlers/collab.rs:18` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:19` `use codex_protocol::protocol::CollabAgentInteractionBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:20` `use codex_protocol::protocol::CollabAgentInteractionEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:21` `use codex_protocol::protocol::CollabAgentSpawnBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:22` `use codex_protocol::protocol::CollabAgentSpawnEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:23` `use codex_protocol::protocol::CollabCloseBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:24` `use codex_protocol::protocol::CollabCloseEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:25` `use codex_protocol::protocol::CollabResumeBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:26` `use codex_protocol::protocol::CollabResumeEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:27` `use codex_protocol::protocol::CollabWaitingBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:28` `use codex_protocol::protocol::CollabWaitingEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:29` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:30` `use codex_protocol::protocol::SubAgentSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:31` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:32` `use serde::Serialize;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:34` `pub struct CollabHandler;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:42` `struct CloseAgentArgs {`
- `impl` `codex-rs/core/src/tools/handlers/collab.rs:47` `impl ToolHandler for CollabHandler {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:48` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:52` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:56` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:89` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:90` `use crate::agent::AgentRole;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:92` `use crate::agent::exceeds_thread_spawn_depth_limit;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:93` `use crate::agent::next_thread_spawn_depth;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:94` `use std::sync::Arc;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:97` `struct SpawnAgentArgs {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:103` `struct SpawnAgentResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:107` `pub async fn handle(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:195` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:196` `use std::sync::Arc;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:199` `struct SendInputArgs {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:207` `struct SendInputResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:211` `pub async fn handle(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:283` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:284` `use crate::agent::next_thread_spawn_depth;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:285` `use crate::rollout::find_thread_path_by_id_str;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:286` `use std::sync::Arc;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:289` `struct ResumeAgentArgs {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:298` `pub async fn handle(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:385` `async fn try_resume_closed_agent(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:429` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:430` `use crate::agent::status::is_final;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:431` `use futures::FutureExt;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:432` `use futures::StreamExt;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:433` `use futures::stream::FuturesUnordered;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:434` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:435` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:436` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:437` `use tokio::sync::watch::Receiver;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:438` `use tokio::time::Instant;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:440` `use tokio::time::timeout_at;`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:443` `struct WaitArgs {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:449` `struct WaitResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:454` `pub async fn handle(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:594` `async fn wait_for_final_status(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:618` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:619` `use std::sync::Arc;`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:626` `pub async fn handle(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:705` `fn agent_id(id: &str) -> Result<ThreadId, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:710` `fn collab_spawn_error(err: CodexErr) -> FunctionCallError {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:719` `fn collab_agent_error(agent_id: ThreadId, err: CodexErr) -> FunctionCallError {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:734` `fn thread_spawn_source(parent_thread_id: ThreadId, depth: i32) -> SessionSource {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:741` `fn build_agent_spawn_config(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:751` `fn build_agent_resume_config(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:761` `fn build_agent_shared_config(`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:799` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:800` `use crate::AuthManager;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:801` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:802` `use crate::ThreadManager;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:803` `use crate::agent::MAX_THREAD_SPAWN_DEPTH;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:804` `use crate::built_in_model_providers;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:805` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:806` `use crate::config::types::ShellEnvironmentPolicy;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:807` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:808` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:809` `use crate::protocol::Op;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:810` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:811` `use crate::protocol::SessionSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:812` `use crate::protocol::SubAgentSource;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:813` `use crate::turn_diff_tracker::TurnDiffTracker;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:814` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:815` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:816` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:817` `use codex_protocol::protocol::InitialHistory;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:818` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:819` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:820` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:821` `use serde_json::json;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:822` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:823` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:824` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:825` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:826` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/tools/handlers/collab.rs:827` `use tokio::time::timeout;`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:829` `fn invocation(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:845` `fn function_payload(args: serde_json::Value) -> ToolPayload {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:851` `fn thread_manager() -> ThreadManager {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:859` `async fn handler_rejects_non_function_payloads() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:881` `async fn handler_rejects_unknown_tool() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:899` `async fn spawn_agent_rejects_empty_message() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:919` `async fn spawn_agent_errors_when_manager_dropped() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:937` `async fn spawn_agent_rejects_when_depth_limit_exceeded() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:965` `async fn send_input_rejects_empty_message() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:985` `async fn send_input_rejects_invalid_id() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1003` `async fn send_input_reports_missing_agent() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1024` `async fn send_input_interrupts_before_prompt() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1063` `async fn resume_agent_rejects_invalid_id() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1081` `async fn resume_agent_reports_missing_agent() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1102` `async fn resume_agent_noops_for_active_agent() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1145` `async fn resume_agent_restores_closed_agent_and_accepts_send_input() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1237` `async fn resume_agent_rejects_when_depth_limit_exceeded() {`
- `struct` `codex-rs/core/src/tools/handlers/collab.rs:1265` `struct WaitResult {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1271` `async fn wait_rejects_non_positive_timeout() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1292` `async fn wait_rejects_invalid_id() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1310` `async fn wait_rejects_empty_ids() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1328` `async fn wait_returns_not_found_for_missing_agents() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1371` `async fn wait_times_out_when_status_is_not_final() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1418` `async fn wait_clamps_short_timeouts_to_minimum() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1449` `async fn wait_returns_final_status_without_timeout() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1505` `async fn close_agent_submits_shutdown_and_returns_status() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1548` `async fn build_agent_spawn_config_uses_turn_context_values() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1549` `fn pick_allowed_approval_policy(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1565` `fn pick_allowed_sandbox_policy(`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1626` `async fn build_agent_spawn_config_preserves_base_user_instructions() {`
- `fn` `codex-rs/core/src/tools/handlers/collab.rs:1642` `async fn build_agent_resume_config_clears_base_instructions() {`

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
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use codex_protocol::protocol::CollabAgentInteractionBeginEvent;`
- `use codex_protocol::protocol::CollabAgentInteractionEndEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
