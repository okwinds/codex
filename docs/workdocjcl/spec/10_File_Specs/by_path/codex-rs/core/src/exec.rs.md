# `codex-rs/core/src/exec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36534`
- sha256: `83cabc7b2fb994200b59ee89b56f3360e188a9df907ccf8d2084ef4f8d99bbb3`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/exec.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct ExecParams {`
- `pub enum ExecExpiration {`
- `pub enum SandboxType {`
- `pub struct StdoutStream {`
- `pub struct StreamOutput<T: Clone> {`
- `pub fn new(text: String) -> Self {`
- `pub fn from_utf8_lossy(&self) -> StreamOutput<String> {`
- `pub struct ExecToolCallOutput {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/exec.rs:2` `use std::os::unix::process::ExitStatusExt;`
- `use` `codex-rs/core/src/exec.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/exec.rs:5` `use std::io;`
- `use` `codex-rs/core/src/exec.rs:6` `use std::path::Path;`
- `use` `codex-rs/core/src/exec.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/exec.rs:8` `use std::process::ExitStatus;`
- `use` `codex-rs/core/src/exec.rs:9` `use std::time::Duration;`
- `use` `codex-rs/core/src/exec.rs:10` `use std::time::Instant;`
- `use` `codex-rs/core/src/exec.rs:12` `use async_channel::Sender;`
- `use` `codex-rs/core/src/exec.rs:13` `use tokio::io::AsyncRead;`
- `use` `codex-rs/core/src/exec.rs:14` `use tokio::io::AsyncReadExt;`
- `use` `codex-rs/core/src/exec.rs:15` `use tokio::io::BufReader;`
- `use` `codex-rs/core/src/exec.rs:16` `use tokio::process::Child;`
- `use` `codex-rs/core/src/exec.rs:17` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/exec.rs:19` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/exec.rs:20` `use crate::error::Result;`
- `use` `codex-rs/core/src/exec.rs:21` `use crate::error::SandboxErr;`
- `use` `codex-rs/core/src/exec.rs:22` `use crate::get_platform_sandbox;`
- `use` `codex-rs/core/src/exec.rs:23` `use crate::protocol::Event;`
- `use` `codex-rs/core/src/exec.rs:24` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/exec.rs:25` `use crate::protocol::ExecCommandOutputDeltaEvent;`
- `use` `codex-rs/core/src/exec.rs:26` `use crate::protocol::ExecOutputStream;`
- `use` `codex-rs/core/src/exec.rs:27` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/exec.rs:28` `use crate::sandboxing::CommandSpec;`
- `use` `codex-rs/core/src/exec.rs:29` `use crate::sandboxing::ExecEnv;`
- `use` `codex-rs/core/src/exec.rs:30` `use crate::sandboxing::SandboxManager;`
- `use` `codex-rs/core/src/exec.rs:31` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/exec.rs:32` `use crate::spawn::StdioPolicy;`
- `use` `codex-rs/core/src/exec.rs:33` `use crate::spawn::spawn_child_async;`
- `use` `codex-rs/core/src/exec.rs:34` `use crate::text_encoding::bytes_to_string_smart;`
- `use` `codex-rs/core/src/exec.rs:35` `use codex_utils_pty::process_group::kill_child_process_group;`
- `const` `codex-rs/core/src/exec.rs:37` `pub const DEFAULT_EXEC_COMMAND_TIMEOUT_MS: u64 = 10_000;`
- `const` `codex-rs/core/src/exec.rs:41` `const SIGKILL_CODE: i32 = 9;`
- `const` `codex-rs/core/src/exec.rs:42` `const TIMEOUT_CODE: i32 = 64;`
- `const` `codex-rs/core/src/exec.rs:43` `const EXIT_CODE_SIGNAL_BASE: i32 = 128; // conventional shell: 128 + signal`
- `const` `codex-rs/core/src/exec.rs:44` `const EXEC_TIMEOUT_EXIT_CODE: i32 = 124; // conventional timeout exit code`
- `const` `codex-rs/core/src/exec.rs:47` `const READ_CHUNK_SIZE: usize = 8192; // bytes per read`
- `const` `codex-rs/core/src/exec.rs:48` `const AGGREGATE_BUFFER_INITIAL_CAPACITY: usize = 8 * 1024; // 8 KiB`
- `const` `codex-rs/core/src/exec.rs:54` `const EXEC_OUTPUT_MAX_BYTES: usize = 1024 * 1024; // 1 MiB`
- `struct` `codex-rs/core/src/exec.rs:61` `pub struct ExecParams {`
- `enum` `codex-rs/core/src/exec.rs:74` `pub enum ExecExpiration {`
- `impl` `codex-rs/core/src/exec.rs:80` `impl From<Option<u64>> for ExecExpiration {`
- `fn` `codex-rs/core/src/exec.rs:81` `fn from(timeout_ms: Option<u64>) -> Self {`
- `impl` `codex-rs/core/src/exec.rs:88` `impl From<u64> for ExecExpiration {`
- `fn` `codex-rs/core/src/exec.rs:89` `fn from(timeout_ms: u64) -> Self {`
- `impl` `codex-rs/core/src/exec.rs:94` `impl ExecExpiration {`
- `fn` `codex-rs/core/src/exec.rs:95` `async fn wait(self) {`
- `enum` `codex-rs/core/src/exec.rs:118` `pub enum SandboxType {`
- `impl` `codex-rs/core/src/exec.rs:131` `impl SandboxType {`
- `struct` `codex-rs/core/src/exec.rs:143` `pub struct StdoutStream {`
- `fn` `codex-rs/core/src/exec.rs:149` `pub async fn process_exec_tool_call(`
- `fn` `codex-rs/core/src/exec.rs:249` `fn extract_create_process_as_user_error_code(err: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/exec.rs:262` `fn windowsapps_path_kind(path: &str) -> &'static str {`
- `fn` `codex-rs/core/src/exec.rs:277` `fn record_windows_sandbox_spawn_failure(`
- `fn` `codex-rs/core/src/exec.rs:315` `async fn exec_windows_sandbox(`
- `use` `codex-rs/core/src/exec.rs:319` `use crate::config::find_codex_home;`
- `use` `codex-rs/core/src/exec.rs:320` `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use` `codex-rs/core/src/exec.rs:321` `use codex_windows_sandbox::run_windows_sandbox_capture;`
- `use` `codex-rs/core/src/exec.rs:322` `use codex_windows_sandbox::run_windows_sandbox_capture_elevated;`
- `fn` `codex-rs/core/src/exec.rs:422` `fn finalize_exec_result(`
- `use` `codex-rs/core/src/exec.rs:482` `use super::CodexErr;`
- `use` `codex-rs/core/src/exec.rs:483` `use crate::sandboxing::SandboxTransformError;`
- `impl` `codex-rs/core/src/exec.rs:485` `impl From<SandboxTransformError> for CodexErr {`
- `fn` `codex-rs/core/src/exec.rs:486` `fn from(err: SandboxTransformError) -> Self {`
- `const` `codex-rs/core/src/exec.rs:517` `const SANDBOX_DENIED_KEYWORDS: [&str; 7] = [`
- `const` `codex-rs/core/src/exec.rs:544` `const QUICK_REJECT_EXIT_CODES: [i32; 3] = [2, 126, 127];`
- `const` `codex-rs/core/src/exec.rs:551` `const SIGSYS_CODE: i32 = libc::SIGSYS;`
- `struct` `codex-rs/core/src/exec.rs:563` `pub struct StreamOutput<T: Clone> {`
- `struct` `codex-rs/core/src/exec.rs:569` `struct RawExecToolCallOutput {`
- `impl` `codex-rs/core/src/exec.rs:577` `impl StreamOutput<String> {`
- `fn` `codex-rs/core/src/exec.rs:578` `pub fn new(text: String) -> Self {`
- `impl` `codex-rs/core/src/exec.rs:586` `impl StreamOutput<Vec<u8>> {`
- `fn` `codex-rs/core/src/exec.rs:587` `pub fn from_utf8_lossy(&self) -> StreamOutput<String> {`
- `fn` `codex-rs/core/src/exec.rs:596` `fn append_capped(dst: &mut Vec<u8>, src: &[u8], max_bytes: usize) {`
- `fn` `codex-rs/core/src/exec.rs:605` `fn aggregate_output(`
- `struct` `codex-rs/core/src/exec.rs:639` `pub struct ExecToolCallOutput {`
- `impl` `codex-rs/core/src/exec.rs:648` `impl Default for ExecToolCallOutput {`
- `fn` `codex-rs/core/src/exec.rs:649` `fn default() -> Self {`
- `fn` `codex-rs/core/src/exec.rs:662` `async fn exec(`
- `fn` `codex-rs/core/src/exec.rs:709` `async fn consume_truncated_output(`
- `const` `codex-rs/core/src/exec.rs:765` `const IO_DRAIN_TIMEOUT_MS: u64 = 2_000; // 2 s should be plenty for local pipes`
- `use` `codex-rs/core/src/exec.rs:768` `use tokio::task::JoinHandle;`
- `fn` `codex-rs/core/src/exec.rs:770` `async fn await_with_timeout(`
- `fn` `codex-rs/core/src/exec.rs:862` `fn synthetic_exit_status(code: i32) -> ExitStatus {`
- `use` `codex-rs/core/src/exec.rs:863` `use std::os::unix::process::ExitStatusExt;`
- `fn` `codex-rs/core/src/exec.rs:868` `fn synthetic_exit_status(code: i32) -> ExitStatus {`
- `use` `codex-rs/core/src/exec.rs:869` `use std::os::windows::process::ExitStatusExt;`
- `use` `codex-rs/core/src/exec.rs:877` `use super::*;`
- `use` `codex-rs/core/src/exec.rs:878` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/exec.rs:879` `use std::time::Duration;`
- `use` `codex-rs/core/src/exec.rs:880` `use tokio::io::AsyncWriteExt;`
- `fn` `codex-rs/core/src/exec.rs:882` `fn make_exec_output(`
- `fn` `codex-rs/core/src/exec.rs:899` `fn sandbox_detection_requires_keywords() {`
- `fn` `codex-rs/core/src/exec.rs:908` `fn sandbox_detection_identifies_keyword_in_stderr() {`
- `fn` `codex-rs/core/src/exec.rs:914` `fn sandbox_detection_respects_quick_reject_exit_codes() {`
- `fn` `codex-rs/core/src/exec.rs:923` `fn sandbox_detection_ignores_non_sandbox_mode() {`
- `fn` `codex-rs/core/src/exec.rs:929` `fn sandbox_detection_uses_aggregated_output() {`
- `fn` `codex-rs/core/src/exec.rs:943` `async fn read_capped_limits_retained_bytes() {`
- `fn` `codex-rs/core/src/exec.rs:955` `fn aggregate_output_prefers_stderr_on_contention() {`
- `fn` `codex-rs/core/src/exec.rs:975` `fn aggregate_output_fills_remaining_capacity_with_stderr() {`
- `fn` `codex-rs/core/src/exec.rs:995` `fn aggregate_output_rebalances_when_stderr_is_small() {`
- `fn` `codex-rs/core/src/exec.rs:1014` `fn aggregate_output_keeps_stdout_then_stderr_when_under_cap() {`
- `fn` `codex-rs/core/src/exec.rs:1035` `fn sandbox_detection_flags_sigsys_exit_code() {`
- `fn` `codex-rs/core/src/exec.rs:1043` `async fn kill_child_process_group_kills_grandchildren_on_timeout() -> Result<()> {`
- `fn` `codex-rs/core/src/exec.rs:1099` `async fn process_exec_tool_call_respects_cancellation_token() -> Result<()> {`
- `fn` `codex-rs/core/src/exec.rs:1138` `fn long_running_command() -> Vec<String> {`
- `fn` `codex-rs/core/src/exec.rs:1147` `fn long_running_command() -> Vec<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::os::unix::process::ExitStatusExt;`
- `use std::collections::HashMap;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::ExitStatus;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use async_channel::Sender;`
- `use tokio::io::AsyncRead;`
- `use tokio::io::AsyncReadExt;`
- `use tokio::io::BufReader;`
- `use tokio::process::Child;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::error::CodexErr;`
- `use crate::error::Result;`
- `use crate::error::SandboxErr;`
- `use crate::get_platform_sandbox;`
- `use crate::protocol::Event;`
- `use crate::protocol::EventMsg;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
