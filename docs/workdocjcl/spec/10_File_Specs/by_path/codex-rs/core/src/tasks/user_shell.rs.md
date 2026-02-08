# `codex-rs/core/src/tasks/user_shell.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10235`
- sha256: `a108fd351fe622ba02134ce8cd0fefa557eb82e7d5b3bf17435b42e34f4a7d51`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `const` `codex-rs/core/src/tasks/user_shell.rs:36` `const USER_SHELL_TIMEOUT_MS: u64 = 60 * 60 * 1000; // 1 hour`
- `impl` `codex-rs/core/src/tasks/user_shell.rs:43` `impl UserShellCommandTask {`
- `impl` `codex-rs/core/src/tasks/user_shell.rs:50` `impl SessionTask for UserShellCommandTask {`
- `fn` `codex-rs/core/src/tasks/user_shell.rs:51` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/user_shell.rs:55` `async fn run(`

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

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
