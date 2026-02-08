# `codex-rs/exec-server/src/posix/escalate_server.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10510`
- sha256: `2b2335d59a31bfc326f016d0908c5170b8e1e9b381d7657821d52fe2f7373982`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/escalate_server.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:2` `use std::os::fd::AsRawFd;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:4` `use std::process::Stdio;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:6` `use std::time::Duration;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:8` `use anyhow::Context as _;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:9` `use path_absolutize::Absolutize as _;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:11` `use codex_core::SandboxState;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:12` `use codex_core::exec::process_exec_tool_call;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:13` `use codex_core::protocol_config_types::WindowsSandboxLevel;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:14` `use codex_core::sandboxing::SandboxPermissions;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:15` `use tokio::process::Command;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:16` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:18` `use crate::posix::escalate_protocol::BASH_EXEC_WRAPPER_ENV_VAR;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:19` `use crate::posix::escalate_protocol::ESCALATE_SOCKET_ENV_VAR;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:20` `use crate::posix::escalate_protocol::EscalateAction;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:21` `use crate::posix::escalate_protocol::EscalateRequest;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:22` `use crate::posix::escalate_protocol::EscalateResponse;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:23` `use crate::posix::escalate_protocol::SuperExecMessage;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:24` `use crate::posix::escalate_protocol::SuperExecResult;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:25` `use crate::posix::escalation_policy::EscalationPolicy;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:26` `use crate::posix::mcp::ExecParams;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:27` `use crate::posix::socket::AsyncDatagramSocket;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:28` `use crate::posix::socket::AsyncSocket;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:29` `use codex_core::exec::ExecExpiration;`
- `impl` `codex-rs/exec-server/src/posix/escalate_server.rs:37` `impl EscalateServer {`
- `fn` `codex-rs/exec-server/src/posix/escalate_server.rs:49` `pub async fn exec(`
- `fn` `codex-rs/exec-server/src/posix/escalate_server.rs:113` `async fn escalate_task(`
- `fn` `codex-rs/exec-server/src/posix/escalate_server.rs:141` `async fn handle_escalate_session_with_policy(`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:233` `use super::*;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:234` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:235` `use std::collections::HashMap;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:236` `use std::path::Path;`
- `use` `codex-rs/exec-server/src/posix/escalate_server.rs:237` `use std::path::PathBuf;`
- `struct` `codex-rs/exec-server/src/posix/escalate_server.rs:239` `struct DeterministicEscalationPolicy {`
- `impl` `codex-rs/exec-server/src/posix/escalate_server.rs:244` `impl EscalationPolicy for DeterministicEscalationPolicy {`
- `fn` `codex-rs/exec-server/src/posix/escalate_server.rs:245` `async fn determine_action(`
- `fn` `codex-rs/exec-server/src/posix/escalate_server.rs:256` `async fn handle_escalate_session_respects_run_in_sandbox_decision() -> anyhow::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/escalate_server.rs:291` `async fn handle_escalate_session_executes_escalated_command() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::os::fd::AsRawFd;`
- `use std::path::PathBuf;`
- `use std::process::Stdio;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use anyhow::Context as _;`
- `use path_absolutize::Absolutize as _;`
- `use codex_core::SandboxState;`
- `use codex_core::exec::process_exec_tool_call;`
- `use codex_core::protocol_config_types::WindowsSandboxLevel;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use tokio::process::Command;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::posix::escalate_protocol::BASH_EXEC_WRAPPER_ENV_VAR;`
- `use crate::posix::escalate_protocol::ESCALATE_SOCKET_ENV_VAR;`
- `use crate::posix::escalate_protocol::EscalateAction;`
- `use crate::posix::escalate_protocol::EscalateRequest;`
- `use crate::posix::escalate_protocol::EscalateResponse;`
- `use crate::posix::escalate_protocol::SuperExecMessage;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
