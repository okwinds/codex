# `codex-rs/debug-client/src/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13755`
- sha256: `03d3c491594d2592a18c60c9f8a4098330fc2274fd353f3cd155324026d098b4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/debug-client/src/client.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct AppServerClient {`
- `pub fn spawn(`
- `pub fn initialize(&mut self) -> Result<()> {`
- `pub fn start_thread(&mut self, params: ThreadStartParams) -> Result<String> {`
- `pub fn resume_thread(&mut self, params: ThreadResumeParams) -> Result<String> {`
- `pub fn request_thread_start(&self, params: ThreadStartParams) -> Result<RequestId> {`
- `pub fn request_thread_resume(&self, params: ThreadResumeParams) -> Result<RequestId> {`
- `pub fn request_thread_list(&self, cursor: Option<String>) -> Result<RequestId> {`
- `pub fn send_turn(&self, thread_id: &str, text: String) -> Result<RequestId> {`
- `pub fn start_reader(`
- `pub fn thread_id(&self) -> Option<String> {`
- `pub fn set_thread_id(&self, thread_id: String) {`
- `pub fn use_thread(&self, thread_id: String) -> bool {`
- `pub fn shutdown(&mut self) {`
- `pub fn build_thread_start_params(`
- `pub fn build_thread_resume_params(`

## Definitions (auto, per-file)
- `use` `codex-rs/debug-client/src/client.rs:1` `use std::io::BufRead;`
- `use` `codex-rs/debug-client/src/client.rs:2` `use std::io::BufReader;`
- `use` `codex-rs/debug-client/src/client.rs:3` `use std::io::Write;`
- `use` `codex-rs/debug-client/src/client.rs:4` `use std::process::Child;`
- `use` `codex-rs/debug-client/src/client.rs:5` `use std::process::ChildStdin;`
- `use` `codex-rs/debug-client/src/client.rs:6` `use std::process::ChildStdout;`
- `use` `codex-rs/debug-client/src/client.rs:7` `use std::process::Command;`
- `use` `codex-rs/debug-client/src/client.rs:8` `use std::process::Stdio;`
- `use` `codex-rs/debug-client/src/client.rs:9` `use std::sync::Arc;`
- `use` `codex-rs/debug-client/src/client.rs:10` `use std::sync::Mutex;`
- `use` `codex-rs/debug-client/src/client.rs:11` `use std::sync::atomic::AtomicI64;`
- `use` `codex-rs/debug-client/src/client.rs:12` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/debug-client/src/client.rs:13` `use std::sync::mpsc::Sender;`
- `use` `codex-rs/debug-client/src/client.rs:15` `use anyhow::Context;`
- `use` `codex-rs/debug-client/src/client.rs:16` `use anyhow::Result;`
- `use` `codex-rs/debug-client/src/client.rs:17` `use codex_app_server_protocol::AskForApproval;`
- `use` `codex-rs/debug-client/src/client.rs:18` `use codex_app_server_protocol::ClientInfo;`
- `use` `codex-rs/debug-client/src/client.rs:19` `use codex_app_server_protocol::ClientNotification;`
- `use` `codex-rs/debug-client/src/client.rs:20` `use codex_app_server_protocol::ClientRequest;`
- `use` `codex-rs/debug-client/src/client.rs:21` `use codex_app_server_protocol::CommandExecutionApprovalDecision;`
- `use` `codex-rs/debug-client/src/client.rs:22` `use codex_app_server_protocol::FileChangeApprovalDecision;`
- `use` `codex-rs/debug-client/src/client.rs:23` `use codex_app_server_protocol::InitializeCapabilities;`
- `use` `codex-rs/debug-client/src/client.rs:24` `use codex_app_server_protocol::JSONRPCMessage;`
- `use` `codex-rs/debug-client/src/client.rs:25` `use codex_app_server_protocol::JSONRPCRequest;`
- `use` `codex-rs/debug-client/src/client.rs:26` `use codex_app_server_protocol::JSONRPCResponse;`
- `use` `codex-rs/debug-client/src/client.rs:27` `use codex_app_server_protocol::RequestId;`
- `use` `codex-rs/debug-client/src/client.rs:28` `use codex_app_server_protocol::ThreadListParams;`
- `use` `codex-rs/debug-client/src/client.rs:29` `use codex_app_server_protocol::ThreadResumeParams;`
- `use` `codex-rs/debug-client/src/client.rs:30` `use codex_app_server_protocol::ThreadResumeResponse;`
- `use` `codex-rs/debug-client/src/client.rs:31` `use codex_app_server_protocol::ThreadStartParams;`
- `use` `codex-rs/debug-client/src/client.rs:32` `use codex_app_server_protocol::ThreadStartResponse;`
- `use` `codex-rs/debug-client/src/client.rs:33` `use codex_app_server_protocol::TurnStartParams;`
- `use` `codex-rs/debug-client/src/client.rs:34` `use codex_app_server_protocol::UserInput;`
- `use` `codex-rs/debug-client/src/client.rs:35` `use serde::Serialize;`
- `use` `codex-rs/debug-client/src/client.rs:37` `use crate::output::Output;`
- `use` `codex-rs/debug-client/src/client.rs:38` `use crate::reader::start_reader;`
- `use` `codex-rs/debug-client/src/client.rs:39` `use crate::state::PendingRequest;`
- `use` `codex-rs/debug-client/src/client.rs:40` `use crate::state::ReaderEvent;`
- `use` `codex-rs/debug-client/src/client.rs:41` `use crate::state::State;`
- `struct` `codex-rs/debug-client/src/client.rs:43` `pub struct AppServerClient {`
- `impl` `codex-rs/debug-client/src/client.rs:53` `impl AppServerClient {`
- `fn` `codex-rs/debug-client/src/client.rs:54` `pub fn spawn(`
- `fn` `codex-rs/debug-client/src/client.rs:93` `pub fn initialize(&mut self) -> Result<()> {`
- `fn` `codex-rs/debug-client/src/client.rs:118` `pub fn start_thread(&mut self, params: ThreadStartParams) -> Result<String> {`
- `fn` `codex-rs/debug-client/src/client.rs:133` `pub fn resume_thread(&mut self, params: ThreadResumeParams) -> Result<String> {`
- `fn` `codex-rs/debug-client/src/client.rs:148` `pub fn request_thread_start(&self, params: ThreadStartParams) -> Result<RequestId> {`
- `fn` `codex-rs/debug-client/src/client.rs:159` `pub fn request_thread_resume(&self, params: ThreadResumeParams) -> Result<RequestId> {`
- `fn` `codex-rs/debug-client/src/client.rs:170` `pub fn request_thread_list(&self, cursor: Option<String>) -> Result<RequestId> {`
- `fn` `codex-rs/debug-client/src/client.rs:188` `pub fn send_turn(&self, thread_id: &str, text: String) -> Result<RequestId> {`
- `fn` `codex-rs/debug-client/src/client.rs:206` `pub fn start_reader(`
- `fn` `codex-rs/debug-client/src/client.rs:225` `pub fn thread_id(&self) -> Option<String> {`
- `fn` `codex-rs/debug-client/src/client.rs:230` `pub fn set_thread_id(&self, thread_id: String) {`
- `fn` `codex-rs/debug-client/src/client.rs:236` `pub fn use_thread(&self, thread_id: String) -> bool {`
- `fn` `codex-rs/debug-client/src/client.rs:244` `pub fn shutdown(&mut self) {`
- `fn` `codex-rs/debug-client/src/client.rs:251` `fn track_pending(&self, request_id: RequestId, kind: PendingRequest) {`
- `fn` `codex-rs/debug-client/src/client.rs:256` `fn remember_thread_locked(&self, state: &mut State) {`
- `fn` `codex-rs/debug-client/src/client.rs:264` `fn next_request_id(&self) -> RequestId {`
- `fn` `codex-rs/debug-client/src/client.rs:282` `fn read_until_response(&mut self, request_id: &RequestId) -> Result<JSONRPCResponse> {`
- `fn` `codex-rs/debug-client/src/client.rs:322` `fn handle_server_request(`
- `fn` `codex-rs/debug-client/src/client.rs:378` `pub fn build_thread_start_params(`
- `fn` `codex-rs/debug-client/src/client.rs:394` `pub fn build_thread_resume_params(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::BufRead;`
- `use std::io::BufReader;`
- `use std::io::Write;`
- `use std::process::Child;`
- `use std::process::ChildStdin;`
- `use std::process::ChildStdout;`
- `use std::process::Command;`
- `use std::process::Stdio;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::atomic::AtomicI64;`
- `use std::sync::atomic::Ordering;`
- `use std::sync::mpsc::Sender;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_app_server_protocol::AskForApproval;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::ClientNotification;`
- `use codex_app_server_protocol::ClientRequest;`
- `use codex_app_server_protocol::CommandExecutionApprovalDecision;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
