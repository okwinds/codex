# `codex-rs/core/src/tasks/user_shell.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11530`
- sha256: `9fbaac1cc74031f04f6ad413288c4a206370c075d929ca6ccf03b319c7582c26`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/user_shell.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tasks/user_shell.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:2` `use std::time::Duration;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:4` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:5` `use codex_async_utils::CancelErr;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:6` `use codex_async_utils::OrCancelExt;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:7` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:8` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:9` `use tracing::error;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:10` `use uuid::Uuid;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:12` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:13` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:14` `use crate::exec::SandboxType;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:15` `use crate::exec::StdoutStream;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:16` `use crate::exec::StreamOutput;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:17` `use crate::exec::execute_exec_env;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:18` `use crate::exec_env::create_env;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:19` `use crate::parse_command::parse_command;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:20` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:21` `use crate::protocol::ExecCommandBeginEvent;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:22` `use crate::protocol::ExecCommandEndEvent;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:23` `use crate::protocol::ExecCommandSource;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:24` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:25` `use crate::protocol::TurnStartedEvent;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:26` `use crate::sandboxing::ExecEnv;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:27` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:28` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:29` `use crate::tools::format_exec_output_str;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:30` `use crate::tools::runtimes::maybe_wrap_shell_lc_with_snapshot;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:31` `use crate::user_shell_command::user_shell_command_record_item;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:33` `use super::SessionTask;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:34` `use super::SessionTaskContext;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:35` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:36` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tasks/user_shell.rs:37` `use codex_protocol::models::ResponseItem;`
- `const` `codex-rs/core/src/tasks/user_shell.rs:39` `const USER_SHELL_TIMEOUT_MS: u64 = 60 * 60 * 1000; // 1 hour`
- `impl` `codex-rs/core/src/tasks/user_shell.rs:56` `impl UserShellCommandTask {`
- `impl` `codex-rs/core/src/tasks/user_shell.rs:63` `impl SessionTask for UserShellCommandTask {`
- `fn` `codex-rs/core/src/tasks/user_shell.rs:64` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/user_shell.rs:68` `async fn run(`
- `fn` `codex-rs/core/src/tasks/user_shell.rs:284` `async fn persist_user_shell_output(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use async_trait::async_trait;`
- `use codex_async_utils::CancelErr;`
- `use codex_async_utils::OrCancelExt;`
- `use codex_protocol::user_input::UserInput;`
- `use tokio_util::sync::CancellationToken;`
- `use tracing::error;`
- `use uuid::Uuid;`
- `use crate::codex::TurnContext;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::exec::SandboxType;`
- `use crate::exec::StdoutStream;`
- `use crate::exec::StreamOutput;`
- `use crate::exec::execute_exec_env;`
- `use crate::exec_env::create_env;`
- `use crate::parse_command::parse_command;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::ExecCommandBeginEvent;`
- `use crate::protocol::ExecCommandEndEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
