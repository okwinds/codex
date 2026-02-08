# `codex-rs/core/src/thread_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22128`
- sha256: `266b594035dc61fdbf96530c7031d415ca98e7d254c73605fb9f8fbfad4dfe9a`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `pub fn subscribe_file_watcher(&self) -> broadcast::Receiver<FileWatcherEvent> {`
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
- `use` `codex-rs/core/src/thread_manager.rs:14` `use crate::file_watcher::FileWatcher;`
- `use` `codex-rs/core/src/thread_manager.rs:15` `use crate::file_watcher::FileWatcherEvent;`
- `use` `codex-rs/core/src/thread_manager.rs:16` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/thread_manager.rs:17` `use crate::protocol::Event;`
- `use` `codex-rs/core/src/thread_manager.rs:18` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/thread_manager.rs:19` `use crate::protocol::SessionConfiguredEvent;`
- `use` `codex-rs/core/src/thread_manager.rs:20` `use crate::rollout::RolloutRecorder;`
- `use` `codex-rs/core/src/thread_manager.rs:21` `use crate::rollout::truncation;`
- `use` `codex-rs/core/src/thread_manager.rs:22` `use crate::skills::SkillsManager;`
- `use` `codex-rs/core/src/thread_manager.rs:23` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/thread_manager.rs:24` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/core/src/thread_manager.rs:25` `use codex_protocol::openai_models::ModelPreset;`
- `use` `codex-rs/core/src/thread_manager.rs:26` `use codex_protocol::protocol::InitialHistory;`
- `use` `codex-rs/core/src/thread_manager.rs:27` `use codex_protocol::protocol::McpServerRefreshConfig;`
- `use` `codex-rs/core/src/thread_manager.rs:28` `use codex_protocol::protocol::Op;`
- `use` `codex-rs/core/src/thread_manager.rs:29` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/thread_manager.rs:30` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/thread_manager.rs:31` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/thread_manager.rs:32` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/thread_manager.rs:33` `use std::sync::Arc;`
- `use` `codex-rs/core/src/thread_manager.rs:35` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/thread_manager.rs:36` `use tokio::runtime::Handle;`
- `use` `codex-rs/core/src/thread_manager.rs:38` `use tokio::runtime::RuntimeFlavor;`
- `use` `codex-rs/core/src/thread_manager.rs:39` `use tokio::sync::RwLock;`
- `use` `codex-rs/core/src/thread_manager.rs:40` `use tokio::sync::broadcast;`
- `use` `codex-rs/core/src/thread_manager.rs:41` `use tracing::warn;`
- `const` `codex-rs/core/src/thread_manager.rs:43` `const THREAD_CREATED_CHANNEL_CAPACITY: usize = 1024;`
- `fn` `codex-rs/core/src/thread_manager.rs:45` `fn build_file_watcher(codex_home: PathBuf, skills_manager: Arc<SkillsManager>) -> Arc<FileWatcher> {`
- `struct` `codex-rs/core/src/thread_manager.rs:88` `pub struct NewThread {`
- `struct` `codex-rs/core/src/thread_manager.rs:96` `pub struct ThreadManager {`
- `impl` `codex-rs/core/src/thread_manager.rs:119` `impl ThreadManager {`
- `fn` `codex-rs/core/src/thread_manager.rs:120` `pub fn new(`
- `fn` `codex-rs/core/src/thread_manager.rs:148` `pub fn with_models_provider(auth: CodexAuth, provider: ModelProviderInfo) -> Self {`
- `fn` `codex-rs/core/src/thread_manager.rs:159` `pub fn with_models_provider_and_home(`
- `fn` `codex-rs/core/src/thread_manager.rs:188` `pub fn session_source(&self) -> SessionSource {`
- `fn` `codex-rs/core/src/thread_manager.rs:192` `pub fn skills_manager(&self) -> Arc<SkillsManager> {`
- `fn` `codex-rs/core/src/thread_manager.rs:196` `pub fn subscribe_file_watcher(&self) -> broadcast::Receiver<FileWatcherEvent> {`
- `fn` `codex-rs/core/src/thread_manager.rs:200` `pub fn get_models_manager(&self) -> Arc<ModelsManager> {`
- `fn` `codex-rs/core/src/thread_manager.rs:204` `pub async fn list_models(`
- `fn` `codex-rs/core/src/thread_manager.rs:215` `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {`
- `fn` `codex-rs/core/src/thread_manager.rs:219` `pub async fn list_thread_ids(&self) -> Vec<ThreadId> {`
- `fn` `codex-rs/core/src/thread_manager.rs:223` `pub async fn refresh_mcp_servers(&self, refresh_config: McpServerRefreshConfig) {`
- `fn` `codex-rs/core/src/thread_manager.rs:244` `pub fn subscribe_thread_created(&self) -> broadcast::Receiver<ThreadId> {`
- `fn` `codex-rs/core/src/thread_manager.rs:248` `pub async fn get_thread(&self, thread_id: ThreadId) -> CodexResult<Arc<CodexThread>> {`
- `fn` `codex-rs/core/src/thread_manager.rs:252` `pub async fn start_thread(&self, config: Config) -> CodexResult<NewThread> {`
- `fn` `codex-rs/core/src/thread_manager.rs:256` `pub async fn start_thread_with_tools(`
- `fn` `codex-rs/core/src/thread_manager.rs:272` `pub async fn resume_thread_from_rollout(`
- `fn` `codex-rs/core/src/thread_manager.rs:283` `pub async fn resume_thread_with_history(`
- `fn` `codex-rs/core/src/thread_manager.rs:303` `pub async fn remove_thread(&self, thread_id: &ThreadId) -> Option<Arc<CodexThread>> {`
- `fn` `codex-rs/core/src/thread_manager.rs:308` `pub async fn remove_and_close_all_threads(&self) -> CodexResult<()> {`
- `fn` `codex-rs/core/src/thread_manager.rs:320` `pub async fn fork_thread(`
- `impl` `codex-rs/core/src/thread_manager.rs:354` `impl ThreadManagerState {`
- `fn` `codex-rs/core/src/thread_manager.rs:474` `async fn finalize_thread_spawn(`
- `fn` `codex-rs/core/src/thread_manager.rs:511` `fn truncate_before_nth_user_message(history: InitialHistory, n: usize) -> InitialHistory {`
- `use` `codex-rs/core/src/thread_manager.rs:524` `use super::*;`
- `use` `codex-rs/core/src/thread_manager.rs:525` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/thread_manager.rs:526` `use assert_matches::assert_matches;`
- `use` `codex-rs/core/src/thread_manager.rs:527` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/thread_manager.rs:528` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/thread_manager.rs:529` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/thread_manager.rs:530` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/thread_manager.rs:532` `fn user_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/thread_manager.rs:543` `fn assistant_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/thread_manager.rs:556` `fn drops_from_last_user_only() {`
- `fn` `codex-rs/core/src/thread_manager.rs:607` `async fn ignores_session_prefix_messages_when_truncating() {`

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
- `use crate::file_watcher::FileWatcher;`
- `use crate::file_watcher::FileWatcherEvent;`
- `use crate::models_manager::manager::ModelsManager;`
- `use crate::protocol::Event;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::SessionConfiguredEvent;`
- `use crate::rollout::RolloutRecorder;`
- `use crate::rollout::truncation;`
- `use crate::skills::SkillsManager;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
