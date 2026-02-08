# `codex-rs/core/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5329`
- sha256: `1bc0d4979938493e252d1eb3dc2790133cb369afcfab7f9efd31f6fabab4391d`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/core/src/lib.rs:8` `mod analytics_client;`
- `mod` `codex-rs/core/src/lib.rs:9` `pub mod api_bridge;`
- `mod` `codex-rs/core/src/lib.rs:10` `mod apply_patch;`
- `mod` `codex-rs/core/src/lib.rs:11` `pub mod auth;`
- `mod` `codex-rs/core/src/lib.rs:12` `pub mod bash;`
- `mod` `codex-rs/core/src/lib.rs:13` `mod client;`
- `mod` `codex-rs/core/src/lib.rs:14` `mod client_common;`
- `mod` `codex-rs/core/src/lib.rs:15` `pub mod codex;`
- `mod` `codex-rs/core/src/lib.rs:17` `mod codex_thread;`
- `mod` `codex-rs/core/src/lib.rs:18` `mod compact_remote;`
- `mod` `codex-rs/core/src/lib.rs:21` `mod agent;`
- `mod` `codex-rs/core/src/lib.rs:22` `mod codex_delegate;`
- `mod` `codex-rs/core/src/lib.rs:23` `mod command_safety;`
- `mod` `codex-rs/core/src/lib.rs:24` `pub mod config;`
- `mod` `codex-rs/core/src/lib.rs:25` `pub mod config_loader;`
- `mod` `codex-rs/core/src/lib.rs:26` `pub mod connectors;`
- `mod` `codex-rs/core/src/lib.rs:27` `mod context_manager;`
- `mod` `codex-rs/core/src/lib.rs:28` `pub mod custom_prompts;`
- `mod` `codex-rs/core/src/lib.rs:29` `pub mod env;`
- `mod` `codex-rs/core/src/lib.rs:30` `mod environment_context;`
- `mod` `codex-rs/core/src/lib.rs:31` `pub mod error;`
- `mod` `codex-rs/core/src/lib.rs:32` `pub mod exec;`
- `mod` `codex-rs/core/src/lib.rs:33` `pub mod exec_env;`
- `mod` `codex-rs/core/src/lib.rs:34` `mod exec_policy;`
- `mod` `codex-rs/core/src/lib.rs:35` `pub mod features;`
- `mod` `codex-rs/core/src/lib.rs:36` `mod file_watcher;`
- `mod` `codex-rs/core/src/lib.rs:37` `mod flags;`
- `mod` `codex-rs/core/src/lib.rs:38` `pub mod git_info;`
- `mod` `codex-rs/core/src/lib.rs:39` `pub mod hooks;`
- `mod` `codex-rs/core/src/lib.rs:40` `pub mod instructions;`
- `mod` `codex-rs/core/src/lib.rs:41` `pub mod landlock;`
- `mod` `codex-rs/core/src/lib.rs:42` `pub mod mcp;`
- `mod` `codex-rs/core/src/lib.rs:43` `mod mcp_connection_manager;`
- `mod` `codex-rs/core/src/lib.rs:44` `pub mod models_manager;`
- `mod` `codex-rs/core/src/lib.rs:48` `mod mcp_tool_call;`
- `mod` `codex-rs/core/src/lib.rs:49` `mod mentions;`
- `mod` `codex-rs/core/src/lib.rs:50` `mod message_history;`
- `mod` `codex-rs/core/src/lib.rs:51` `mod model_provider_info;`
- `mod` `codex-rs/core/src/lib.rs:52` `pub mod parse_command;`
- `mod` `codex-rs/core/src/lib.rs:53` `pub mod path_utils;`
- `mod` `codex-rs/core/src/lib.rs:54` `pub mod personality_migration;`
- `mod` `codex-rs/core/src/lib.rs:55` `pub mod powershell;`
- `mod` `codex-rs/core/src/lib.rs:56` `mod proposed_plan_parser;`
- `mod` `codex-rs/core/src/lib.rs:57` `pub mod sandboxing;`
- `mod` `codex-rs/core/src/lib.rs:58` `mod session_prefix;`
- `mod` `codex-rs/core/src/lib.rs:59` `mod stream_events_utils;`
- `mod` `codex-rs/core/src/lib.rs:60` `mod tagged_block_parser;`
- `mod` `codex-rs/core/src/lib.rs:61` `mod text_encoding;`
- `mod` `codex-rs/core/src/lib.rs:62` `pub mod token_data;`
- `mod` `codex-rs/core/src/lib.rs:63` `mod truncate;`
- `mod` `codex-rs/core/src/lib.rs:64` `mod unified_exec;`
- `mod` `codex-rs/core/src/lib.rs:65` `pub mod windows_sandbox;`
- `mod` `codex-rs/core/src/lib.rs:75` `mod event_mapping;`
- `mod` `codex-rs/core/src/lib.rs:76` `pub mod review_format;`
- `mod` `codex-rs/core/src/lib.rs:77` `pub mod review_prompts;`
- `mod` `codex-rs/core/src/lib.rs:78` `mod thread_manager;`
- `mod` `codex-rs/core/src/lib.rs:79` `pub mod web_search;`
- `type` `codex-rs/core/src/lib.rs:84` `pub type ConversationManager = ThreadManager;`
- `type` `codex-rs/core/src/lib.rs:86` `pub type NewConversation = NewThread;`
- `type` `codex-rs/core/src/lib.rs:88` `pub type CodexConversation = CodexThread;`
- `mod` `codex-rs/core/src/lib.rs:92` `pub mod default_client;`
- `mod` `codex-rs/core/src/lib.rs:93` `pub mod project_doc;`
- `mod` `codex-rs/core/src/lib.rs:94` `mod rollout;`
- `mod` `codex-rs/core/src/lib.rs:96` `pub mod seatbelt;`
- `mod` `codex-rs/core/src/lib.rs:97` `pub mod shell;`
- `mod` `codex-rs/core/src/lib.rs:98` `pub mod shell_snapshot;`
- `mod` `codex-rs/core/src/lib.rs:99` `pub mod skills;`
- `mod` `codex-rs/core/src/lib.rs:100` `pub mod spawn;`
- `mod` `codex-rs/core/src/lib.rs:101` `pub mod state_db;`
- `mod` `codex-rs/core/src/lib.rs:102` `pub mod terminal;`
- `mod` `codex-rs/core/src/lib.rs:103` `mod tools;`
- `mod` `codex-rs/core/src/lib.rs:104` `pub mod turn_diff_tracker;`
- `mod` `codex-rs/core/src/lib.rs:105` `mod turn_metadata;`
- `mod` `codex-rs/core/src/lib.rs:127` `mod function_tool;`
- `mod` `codex-rs/core/src/lib.rs:128` `mod state;`
- `mod` `codex-rs/core/src/lib.rs:129` `mod tasks;`
- `mod` `codex-rs/core/src/lib.rs:130` `mod user_shell_command;`
- `mod` `codex-rs/core/src/lib.rs:131` `pub mod util;`
- `mod` `codex-rs/core/src/lib.rs:164` `pub mod compact;`
- `mod` `codex-rs/core/src/lib.rs:165` `pub mod memory_trace;`
- `mod` `codex-rs/core/src/lib.rs:166` `pub mod otel_init;`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
