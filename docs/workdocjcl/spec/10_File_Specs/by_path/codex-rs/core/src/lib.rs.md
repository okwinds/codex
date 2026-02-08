# `codex-rs/core/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5301`
- sha256: `fda7a6de1af426fc8dc4a0e87098eba96fbb4191fbf170589a1134ef13a2bbe8`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `mod` `codex-rs/core/src/lib.rs:16` `mod codex_thread;`
- `mod` `codex-rs/core/src/lib.rs:17` `mod compact_remote;`
- `mod` `codex-rs/core/src/lib.rs:20` `mod agent;`
- `mod` `codex-rs/core/src/lib.rs:21` `mod codex_delegate;`
- `mod` `codex-rs/core/src/lib.rs:22` `mod command_safety;`
- `mod` `codex-rs/core/src/lib.rs:23` `pub mod config;`
- `mod` `codex-rs/core/src/lib.rs:24` `pub mod config_loader;`
- `mod` `codex-rs/core/src/lib.rs:25` `pub mod connectors;`
- `mod` `codex-rs/core/src/lib.rs:26` `mod context_manager;`
- `mod` `codex-rs/core/src/lib.rs:27` `pub mod custom_prompts;`
- `mod` `codex-rs/core/src/lib.rs:28` `pub mod env;`
- `mod` `codex-rs/core/src/lib.rs:29` `mod environment_context;`
- `mod` `codex-rs/core/src/lib.rs:30` `pub mod error;`
- `mod` `codex-rs/core/src/lib.rs:31` `pub mod exec;`
- `mod` `codex-rs/core/src/lib.rs:32` `pub mod exec_env;`
- `mod` `codex-rs/core/src/lib.rs:33` `mod exec_policy;`
- `mod` `codex-rs/core/src/lib.rs:34` `pub mod features;`
- `mod` `codex-rs/core/src/lib.rs:35` `mod flags;`
- `mod` `codex-rs/core/src/lib.rs:36` `pub mod git_info;`
- `mod` `codex-rs/core/src/lib.rs:37` `pub mod instructions;`
- `mod` `codex-rs/core/src/lib.rs:38` `pub mod landlock;`
- `mod` `codex-rs/core/src/lib.rs:39` `pub mod mcp;`
- `mod` `codex-rs/core/src/lib.rs:40` `mod mcp_connection_manager;`
- `mod` `codex-rs/core/src/lib.rs:41` `pub mod models_manager;`
- `mod` `codex-rs/core/src/lib.rs:42` `mod transport_manager;`
- `mod` `codex-rs/core/src/lib.rs:46` `mod mcp_tool_call;`
- `mod` `codex-rs/core/src/lib.rs:47` `mod mentions;`
- `mod` `codex-rs/core/src/lib.rs:48` `mod message_history;`
- `mod` `codex-rs/core/src/lib.rs:49` `mod model_provider_info;`
- `mod` `codex-rs/core/src/lib.rs:50` `pub mod parse_command;`
- `mod` `codex-rs/core/src/lib.rs:51` `pub mod path_utils;`
- `mod` `codex-rs/core/src/lib.rs:52` `pub mod personality_migration;`
- `mod` `codex-rs/core/src/lib.rs:53` `pub mod powershell;`
- `mod` `codex-rs/core/src/lib.rs:54` `mod proposed_plan_parser;`
- `mod` `codex-rs/core/src/lib.rs:55` `pub mod sandboxing;`
- `mod` `codex-rs/core/src/lib.rs:56` `mod session_prefix;`
- `mod` `codex-rs/core/src/lib.rs:57` `mod stream_events_utils;`
- `mod` `codex-rs/core/src/lib.rs:58` `mod tagged_block_parser;`
- `mod` `codex-rs/core/src/lib.rs:59` `mod text_encoding;`
- `mod` `codex-rs/core/src/lib.rs:60` `pub mod token_data;`
- `mod` `codex-rs/core/src/lib.rs:61` `mod truncate;`
- `mod` `codex-rs/core/src/lib.rs:62` `mod unified_exec;`
- `mod` `codex-rs/core/src/lib.rs:63` `pub mod windows_sandbox;`
- `mod` `codex-rs/core/src/lib.rs:74` `mod event_mapping;`
- `mod` `codex-rs/core/src/lib.rs:75` `pub mod review_format;`
- `mod` `codex-rs/core/src/lib.rs:76` `pub mod review_prompts;`
- `mod` `codex-rs/core/src/lib.rs:77` `mod thread_manager;`
- `mod` `codex-rs/core/src/lib.rs:78` `pub mod web_search;`
- `type` `codex-rs/core/src/lib.rs:83` `pub type ConversationManager = ThreadManager;`
- `type` `codex-rs/core/src/lib.rs:85` `pub type NewConversation = NewThread;`
- `type` `codex-rs/core/src/lib.rs:87` `pub type CodexConversation = CodexThread;`
- `mod` `codex-rs/core/src/lib.rs:91` `pub mod default_client;`
- `mod` `codex-rs/core/src/lib.rs:92` `pub mod project_doc;`
- `mod` `codex-rs/core/src/lib.rs:93` `mod rollout;`
- `mod` `codex-rs/core/src/lib.rs:95` `pub mod seatbelt;`
- `mod` `codex-rs/core/src/lib.rs:96` `pub mod shell;`
- `mod` `codex-rs/core/src/lib.rs:97` `pub mod shell_snapshot;`
- `mod` `codex-rs/core/src/lib.rs:98` `pub mod skills;`
- `mod` `codex-rs/core/src/lib.rs:99` `pub mod spawn;`
- `mod` `codex-rs/core/src/lib.rs:100` `pub mod state_db;`
- `mod` `codex-rs/core/src/lib.rs:101` `pub mod terminal;`
- `mod` `codex-rs/core/src/lib.rs:102` `mod tools;`
- `mod` `codex-rs/core/src/lib.rs:103` `pub mod turn_diff_tracker;`
- `mod` `codex-rs/core/src/lib.rs:104` `mod turn_metadata;`
- `mod` `codex-rs/core/src/lib.rs:126` `mod function_tool;`
- `mod` `codex-rs/core/src/lib.rs:127` `mod state;`
- `mod` `codex-rs/core/src/lib.rs:128` `mod tasks;`
- `mod` `codex-rs/core/src/lib.rs:129` `mod user_notification;`
- `mod` `codex-rs/core/src/lib.rs:130` `mod user_shell_command;`
- `mod` `codex-rs/core/src/lib.rs:131` `pub mod util;`
- `mod` `codex-rs/core/src/lib.rs:163` `pub mod compact;`
- `mod` `codex-rs/core/src/lib.rs:164` `pub mod otel_init;`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
