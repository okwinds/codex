# `codex-rs/exec-server/src/posix/escalate_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4270`
- sha256: `e5c308f496db54b33120075b5f644f23a2c117b6a0abdc7a98e9834733cf3af2`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/escalate_client.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:1` `use std::io;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:2` `use std::os::fd::AsRawFd;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:3` `use std::os::fd::FromRawFd as _;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:4` `use std::os::fd::OwnedFd;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:6` `use anyhow::Context as _;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:8` `use crate::posix::escalate_protocol::BASH_EXEC_WRAPPER_ENV_VAR;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:9` `use crate::posix::escalate_protocol::ESCALATE_SOCKET_ENV_VAR;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:10` `use crate::posix::escalate_protocol::EscalateAction;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:11` `use crate::posix::escalate_protocol::EscalateRequest;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:12` `use crate::posix::escalate_protocol::EscalateResponse;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:13` `use crate::posix::escalate_protocol::SuperExecMessage;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:14` `use crate::posix::escalate_protocol::SuperExecResult;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:15` `use crate::posix::socket::AsyncDatagramSocket;`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:16` `use crate::posix::socket::AsyncSocket;`
- `fn` `codex-rs/exec-server/src/posix/escalate_client.rs:18` `fn get_escalate_client() -> anyhow::Result<AsyncDatagramSocket> {`
- `const` `codex-rs/exec-server/src/posix/escalate_client.rs:32` `const HANDSHAKE_MESSAGE: [u8; 1] = [0];`
- `use` `codex-rs/exec-server/src/posix/escalate_client.rs:85` `use std::ffi::CString;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::os::fd::AsRawFd;`
- `use std::os::fd::FromRawFd as _;`
- `use std::os::fd::OwnedFd;`
- `use anyhow::Context as _;`
- `use crate::posix::escalate_protocol::BASH_EXEC_WRAPPER_ENV_VAR;`
- `use crate::posix::escalate_protocol::ESCALATE_SOCKET_ENV_VAR;`
- `use crate::posix::escalate_protocol::EscalateAction;`
- `use crate::posix::escalate_protocol::EscalateRequest;`
- `use crate::posix::escalate_protocol::EscalateResponse;`
- `use crate::posix::escalate_protocol::SuperExecMessage;`
- `use crate::posix::escalate_protocol::SuperExecResult;`
- `use crate::posix::socket::AsyncDatagramSocket;`
- `use crate::posix::socket::AsyncSocket;`
- `use std::ffi::CString;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
