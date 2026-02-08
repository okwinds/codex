# `codex-rs/cli/src/debug_sandbox.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8428`
- sha256: `a71d0508b92e4ae73ada4b8141561ae344e9c677458fb28d074696474f1fd357`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/debug_sandbox.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn create_sandbox_mode(full_auto: bool) -> SandboxMode {`

## Definitions (auto, per-file)
- `mod` `codex-rs/cli/src/debug_sandbox.rs:2` `mod pid_tracker;`
- `mod` `codex-rs/cli/src/debug_sandbox.rs:4` `mod seatbelt;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:6` `use std::path::PathBuf;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:8` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:9` `use codex_core::config::Config;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:10` `use codex_core::config::ConfigOverrides;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:11` `use codex_core::exec_env::create_env;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:12` `use codex_core::landlock::spawn_command_under_linux_sandbox;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:14` `use codex_core::seatbelt::spawn_command_under_seatbelt;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:15` `use codex_core::spawn::StdioPolicy;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:16` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:18` `use crate::LandlockCommand;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:19` `use crate::SeatbeltCommand;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:20` `use crate::WindowsCommand;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:21` `use crate::exit_status::handle_exit_status;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:24` `use seatbelt::DenialLogger;`
- `fn` `codex-rs/cli/src/debug_sandbox.rs:27` `pub async fn run_command_under_seatbelt(`
- `fn` `codex-rs/cli/src/debug_sandbox.rs:49` `pub async fn run_command_under_seatbelt(`
- `fn` `codex-rs/cli/src/debug_sandbox.rs:56` `pub async fn run_command_under_landlock(`
- `fn` `codex-rs/cli/src/debug_sandbox.rs:76` `pub async fn run_command_under_windows(`
- `enum` `codex-rs/cli/src/debug_sandbox.rs:96` `enum SandboxType {`
- `fn` `codex-rs/cli/src/debug_sandbox.rs:103` `async fn run_command_under_sandbox(`
- `use` `codex-rs/cli/src/debug_sandbox.rs:139` `use codex_core::windows_sandbox::WindowsSandboxLevelExt;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:140` `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:141` `use codex_windows_sandbox::run_windows_sandbox_capture;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:142` `use codex_windows_sandbox::run_windows_sandbox_capture_elevated;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:195` `use std::io::Write;`
- `use` `codex-rs/cli/src/debug_sandbox.rs:199` `use std::io::Write;`
- `fn` `codex-rs/cli/src/debug_sandbox.rs:273` `pub fn create_sandbox_mode(full_auto: bool) -> SandboxMode {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use codex_common::CliConfigOverrides;`
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigOverrides;`
- `use codex_core::exec_env::create_env;`
- `use codex_core::landlock::spawn_command_under_linux_sandbox;`
- `use codex_core::seatbelt::spawn_command_under_seatbelt;`
- `use codex_core::spawn::StdioPolicy;`
- `use codex_protocol::config_types::SandboxMode;`
- `use crate::LandlockCommand;`
- `use crate::SeatbeltCommand;`
- `use crate::WindowsCommand;`
- `use crate::exit_status::handle_exit_status;`
- `use seatbelt::DenialLogger;`
- `use codex_core::windows_sandbox::WindowsSandboxLevelExt;`
- `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use codex_windows_sandbox::run_windows_sandbox_capture;`
- `use codex_windows_sandbox::run_windows_sandbox_capture_elevated;`
- `use std::io::Write;`
- `use std::io::Write;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/03_API/CLI.md`
