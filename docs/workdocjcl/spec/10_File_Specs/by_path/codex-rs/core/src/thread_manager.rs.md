# `codex-rs/core/src/thread_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19286`
- sha256: `c9dd44b241ebf5ce74726fa35e07175c4ce73ec29263531e129c640c9550057e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/thread_manager.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct NewThread {`
- `pub struct ThreadManager {`
- `pub fn new(`
- `pub fn with_models_provider(auth: CodexAuth, provider: ModelProviderInfo) -> Self {`
- `pub fn with_models_provider_and_home(`
- `pub fn session_source(&self) -> SessionSource {`
- `pub fn skills_manager(&self) -> Arc<SkillsManager> {`
- `pub fn get_models_manager(&self) -> Arc<ModelsManager> {`
- `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {`
- `pub fn subscribe_thread_created(&self) -> broadcast::Receiver<ThreadId> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/thread_manager.rs:1` `use crate::AuthManager;`
- `use` `codex-rs/core/src/thread_manager.rs:3` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/thread_manager.rs:5` `use crate::ModelProviderInfo;`
- `use` `codex-rs/core/src/thread_manager.rs:6` `use crate::agent::AgentControl;`
- `use` `codex-rs/core/src/thread_manager.rs:7` `use crate::codex::Codex;`
- `use` `codex-rs/core/src/thread_manager.rs:8` `use crate::codex::CodexSpawnOk;`
- `use` `codex-rs/core/src/thread_manager.rs:9` `use crate::codex::INITIAL_SUBMIT_ID;`
- `use` `codex-rs/core/src/thread_manager.rs:10` `use crate::codex_thread::CodexThread;`
- `use` `codex-rs/core/src/thread_manager.rs:11` `use crate::config::Config;`
- `use` `codex-rs/core/src/thread_manager.rs:12` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/thread_manager.rs:13` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/thread_manager.rs:14` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/thread_manager.rs:15` `use crate::protocol::Event;`
- `use` `codex-rs/core/src/thread_manager.rs:16` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/thread_manager.rs:17` `use crate::protocol::SessionConfiguredEvent;`
- `use` `codex-rs/core/src/thread_manager.rs:18` `use crate::rollout::RolloutRecorder;`
- `use` `codex-rs/core/src/thread_manager.rs:19` `use crate::rollout::truncation;`
- `use` `codex-rs/core/src/thread_manager.rs:20` `use crate::skills::SkillsManager;`
- `use` `codex-rs/core/src/thread_manager.rs:21` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/thread_manager.rs:22` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/core/src/thread_manager.rs:23` `use codex_protocol::openai_models::ModelPreset;`
- `use` `codex-rs/core/src/thread_manager.rs:24` `use codex_protocol::protocol::InitialHistory;`
- `use` `codex-rs/core/src/thread_manager.rs:25` `use codex_protocol::protocol::McpServerRefreshConfig;`
- `use` `codex-rs/core/src/thread_manager.rs:26` `use codex_protocol::protocol::Op;`
- `use` `codex-rs/core/src/thread_manager.rs:27` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/thread_manager.rs:28` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/thread_manager.rs:29` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/thread_manager.rs:30` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/thread_manager.rs:31` `use std::sync::Arc;`
- `use` `codex-rs/core/src/thread_manager.rs:33` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/thread_manager.rs:34` `use tokio::sync::RwLock;`
- `use` `codex-rs/core/src/thread_manager.rs:35` `use tokio::sync::broadcast;`
- `use` `codex-rs/core/src/thread_manager.rs:36` `use tracing::warn;`
- `const` `codex-rs/core/src/thread_manager.rs:38` `const THREAD_CREATED_CHANNEL_CAPACITY: usize = 1024;`
- `struct` `codex-rs/core/src/thread_manager.rs:42` `pub struct NewThread {`
- `struct` `codex-rs/core/src/thread_manager.rs:50` `pub struct ThreadManager {`
- `impl` `codex-rs/core/src/thread_manager.rs:72` `impl ThreadManager {`
- `fn` `codex-rs/core/src/thread_manager.rs:73` `pub fn new(`
- `fn` `codex-rs/core/src/thread_manager.rs:101` `pub fn with_models_provider(auth: CodexAuth, provider: ModelProviderInfo) -> Self {`
- `fn` `codex-rs/core/src/thread_manager.rs:112` `pub fn with_models_provider_and_home(`
- `fn` `codex-rs/core/src/thread_manager.rs:138` `pub fn session_source(&self) -> SessionSource {`
- `fn` `codex-rs/core/src/thread_manager.rs:142` `pub fn skills_manager(&self) -> Arc<SkillsManager> {`
- `fn` `codex-rs/core/src/thread_manager.rs:146` `pub fn get_models_manager(&self) -> Arc<ModelsManager> {`
- `fn` `codex-rs/core/src/thread_manager.rs:150` `pub async fn list_models(`
- `fn` `codex-rs/core/src/thread_manager.rs:161` `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {`
- `fn` `codex-rs/core/src/thread_manager.rs:165` `pub async fn list_thread_ids(&self) -> Vec<ThreadId> {`
- `fn` `codex-rs/core/src/thread_manager.rs:169` `pub async fn refresh_mcp_servers(&self, refresh_config: McpServerRefreshConfig) {`
- `fn` `codex-rs/core/src/thread_manager.rs:190` `pub fn subscribe_thread_created(&self) -> broadcast::Receiver<ThreadId> {`
- `fn` `codex-rs/core/src/thread_manager.rs:194` `pub async fn get_thread(&self, thread_id: ThreadId) -> CodexResult<Arc<CodexThread>> {`
- `fn` `codex-rs/core/src/thread_manager.rs:198` `pub async fn start_thread(&self, config: Config) -> CodexResult<NewThread> {`
- `fn` `codex-rs/core/src/thread_manager.rs:202` `pub async fn start_thread_with_tools(`
- `fn` `codex-rs/core/src/thread_manager.rs:218` `pub async fn resume_thread_from_rollout(`
- `fn` `codex-rs/core/src/thread_manager.rs:229` `pub async fn resume_thread_with_history(`
- `fn` `codex-rs/core/src/thread_manager.rs:249` `pub async fn remove_thread(&self, thread_id: &ThreadId) -> Option<Arc<CodexThread>> {`
- `fn` `codex-rs/core/src/thread_manager.rs:254` `pub async fn remove_and_close_all_threads(&self) -> CodexResult<()> {`
- `fn` `codex-rs/core/src/thread_manager.rs:266` `pub async fn fork_thread(`
- `impl` `codex-rs/core/src/thread_manager.rs:300` `impl ThreadManagerState {`
- `fn` `codex-rs/core/src/thread_manager.rs:399` `async fn finalize_thread_spawn(`
- `fn` `codex-rs/core/src/thread_manager.rs:436` `fn truncate_before_nth_user_message(history: InitialHistory, n: usize) -> InitialHistory {`
- `use` `codex-rs/core/src/thread_manager.rs:449` `use super::*;`
- `use` `codex-rs/core/src/thread_manager.rs:450` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/thread_manager.rs:451` `use assert_matches::assert_matches;`
- `use` `codex-rs/core/src/thread_manager.rs:452` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/thread_manager.rs:453` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/thread_manager.rs:454` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/thread_manager.rs:455` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/thread_manager.rs:457` `fn user_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/thread_manager.rs:468` `fn assistant_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/thread_manager.rs:481` `fn drops_from_last_user_only() {`
- `fn` `codex-rs/core/src/thread_manager.rs:532` `async fn ignores_session_prefix_messages_when_truncating() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::AuthManager;`
- `use crate::CodexAuth;`
- `use crate::ModelProviderInfo;`
- `use crate::agent::AgentControl;`
- `use crate::codex::Codex;`
- `use crate::codex::CodexSpawnOk;`
- `use crate::codex::INITIAL_SUBMIT_ID;`
- `use crate::codex_thread::CodexThread;`
- `use crate::config::Config;`
- `use crate::error::CodexErr;`
- `use crate::error::Result as CodexResult;`
- `use crate::models_manager::manager::ModelsManager;`
- `use crate::protocol::Event;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::SessionConfiguredEvent;`
- `use crate::rollout::RolloutRecorder;`
- `use crate::rollout::truncation;`
- `use crate::skills::SkillsManager;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::CollaborationModeMask;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
