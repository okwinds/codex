# `codex-rs/debug-client/src/reader.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12194`
- sha256: `51df9ddb8a0f6cd879dc767cdb5026fa75e2432ef4cde5e4bc0bf02a02edee04`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/debug-client/src/reader.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn start_reader(`

## Definitions (auto, per-file)
- `use` `codex-rs/debug-client/src/reader.rs:1` `use std::io::BufRead;`
- `use` `codex-rs/debug-client/src/reader.rs:2` `use std::io::BufReader;`
- `use` `codex-rs/debug-client/src/reader.rs:3` `use std::process::ChildStdout;`
- `use` `codex-rs/debug-client/src/reader.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/debug-client/src/reader.rs:5` `use std::sync::Mutex;`
- `use` `codex-rs/debug-client/src/reader.rs:6` `use std::sync::mpsc::Sender;`
- `use` `codex-rs/debug-client/src/reader.rs:7` `use std::thread;`
- `use` `codex-rs/debug-client/src/reader.rs:8` `use std::thread::JoinHandle;`
- `use` `codex-rs/debug-client/src/reader.rs:10` `use anyhow::Context;`
- `use` `codex-rs/debug-client/src/reader.rs:11` `use codex_app_server_protocol::CommandExecutionApprovalDecision;`
- `use` `codex-rs/debug-client/src/reader.rs:12` `use codex_app_server_protocol::CommandExecutionRequestApprovalResponse;`
- `use` `codex-rs/debug-client/src/reader.rs:13` `use codex_app_server_protocol::FileChangeApprovalDecision;`
- `use` `codex-rs/debug-client/src/reader.rs:14` `use codex_app_server_protocol::FileChangeRequestApprovalResponse;`
- `use` `codex-rs/debug-client/src/reader.rs:15` `use codex_app_server_protocol::JSONRPCMessage;`
- `use` `codex-rs/debug-client/src/reader.rs:16` `use codex_app_server_protocol::JSONRPCNotification;`
- `use` `codex-rs/debug-client/src/reader.rs:17` `use codex_app_server_protocol::JSONRPCRequest;`
- `use` `codex-rs/debug-client/src/reader.rs:18` `use codex_app_server_protocol::JSONRPCResponse;`
- `use` `codex-rs/debug-client/src/reader.rs:19` `use codex_app_server_protocol::ServerNotification;`
- `use` `codex-rs/debug-client/src/reader.rs:20` `use codex_app_server_protocol::ServerRequest;`
- `use` `codex-rs/debug-client/src/reader.rs:21` `use codex_app_server_protocol::ThreadItem;`
- `use` `codex-rs/debug-client/src/reader.rs:22` `use codex_app_server_protocol::ThreadListResponse;`
- `use` `codex-rs/debug-client/src/reader.rs:23` `use codex_app_server_protocol::ThreadResumeResponse;`
- `use` `codex-rs/debug-client/src/reader.rs:24` `use codex_app_server_protocol::ThreadStartResponse;`
- `use` `codex-rs/debug-client/src/reader.rs:25` `use serde::Serialize;`
- `use` `codex-rs/debug-client/src/reader.rs:26` `use std::io::Write;`
- `use` `codex-rs/debug-client/src/reader.rs:28` `use crate::output::LabelColor;`
- `use` `codex-rs/debug-client/src/reader.rs:29` `use crate::output::Output;`
- `use` `codex-rs/debug-client/src/reader.rs:30` `use crate::state::PendingRequest;`
- `use` `codex-rs/debug-client/src/reader.rs:31` `use crate::state::ReaderEvent;`
- `use` `codex-rs/debug-client/src/reader.rs:32` `use crate::state::State;`
- `fn` `codex-rs/debug-client/src/reader.rs:34` `pub fn start_reader(`
- `fn` `codex-rs/debug-client/src/reader.rs:109` `fn handle_server_request(`
- `fn` `codex-rs/debug-client/src/reader.rs:144` `fn handle_response(`
- `fn` `codex-rs/debug-client/src/reader.rs:209` `fn handle_filtered_notification(`
- `fn` `codex-rs/debug-client/src/reader.rs:225` `fn emit_filtered_item(item: ThreadItem, thread_id: &str, output: &Output) -> anyhow::Result<()> {`
- `fn` `codex-rs/debug-client/src/reader.rs:303` `fn write_multiline(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::BufRead;`
- `use std::io::BufReader;`
- `use std::process::ChildStdout;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::mpsc::Sender;`
- `use std::thread;`
- `use std::thread::JoinHandle;`
- `use anyhow::Context;`
- `use codex_app_server_protocol::CommandExecutionApprovalDecision;`
- `use codex_app_server_protocol::CommandExecutionRequestApprovalResponse;`
- `use codex_app_server_protocol::FileChangeApprovalDecision;`
- `use codex_app_server_protocol::FileChangeRequestApprovalResponse;`
- `use codex_app_server_protocol::JSONRPCMessage;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCRequest;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::ServerNotification;`
- `use codex_app_server_protocol::ServerRequest;`
- `use codex_app_server_protocol::ThreadItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
