# `codex-rs/debug-client/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9490`
- sha256: `fde1d13c033c9092e6997642e8c7e2273cdae9e9051e1dba496e37841e9de05f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/debug-client/src/main.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `fn main() -> Result<()> {`

## Definitions (auto, per-file)
- `mod` `codex-rs/debug-client/src/main.rs:1` `mod client;`
- `mod` `codex-rs/debug-client/src/main.rs:2` `mod commands;`
- `mod` `codex-rs/debug-client/src/main.rs:3` `mod output;`
- `mod` `codex-rs/debug-client/src/main.rs:4` `mod reader;`
- `mod` `codex-rs/debug-client/src/main.rs:5` `mod state;`
- `use` `codex-rs/debug-client/src/main.rs:7` `use std::io;`
- `use` `codex-rs/debug-client/src/main.rs:8` `use std::io::BufRead;`
- `use` `codex-rs/debug-client/src/main.rs:9` `use std::sync::mpsc;`
- `use` `codex-rs/debug-client/src/main.rs:11` `use anyhow::Context;`
- `use` `codex-rs/debug-client/src/main.rs:12` `use anyhow::Result;`
- `use` `codex-rs/debug-client/src/main.rs:13` `use clap::ArgAction;`
- `use` `codex-rs/debug-client/src/main.rs:14` `use clap::Parser;`
- `use` `codex-rs/debug-client/src/main.rs:15` `use codex_app_server_protocol::AskForApproval;`
- `use` `codex-rs/debug-client/src/main.rs:17` `use crate::client::AppServerClient;`
- `use` `codex-rs/debug-client/src/main.rs:18` `use crate::client::build_thread_resume_params;`
- `use` `codex-rs/debug-client/src/main.rs:19` `use crate::client::build_thread_start_params;`
- `use` `codex-rs/debug-client/src/main.rs:20` `use crate::commands::InputAction;`
- `use` `codex-rs/debug-client/src/main.rs:21` `use crate::commands::UserCommand;`
- `use` `codex-rs/debug-client/src/main.rs:22` `use crate::commands::parse_input;`
- `use` `codex-rs/debug-client/src/main.rs:23` `use crate::output::Output;`
- `use` `codex-rs/debug-client/src/main.rs:24` `use crate::state::ReaderEvent;`
- `struct` `codex-rs/debug-client/src/main.rs:28` `struct Cli {`
- `fn` `codex-rs/debug-client/src/main.rs:66` `fn main() -> Result<()> {`
- `fn` `codex-rs/debug-client/src/main.rs:151` `fn handle_command(`
- `fn` `codex-rs/debug-client/src/main.rs:239` `fn parse_approval_policy(value: &str) -> Result<AskForApproval> {`
- `fn` `codex-rs/debug-client/src/main.rs:251` `fn drain_events(event_rx: &mpsc::Receiver<ReaderEvent>, output: &Output) {`
- `fn` `codex-rs/debug-client/src/main.rs:284` `fn print_help(output: &Output) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::io::BufRead;`
- `use std::sync::mpsc;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use clap::ArgAction;`
- `use clap::Parser;`
- `use codex_app_server_protocol::AskForApproval;`
- `use crate::client::AppServerClient;`
- `use crate::client::build_thread_resume_params;`
- `use crate::client::build_thread_start_params;`
- `use crate::commands::InputAction;`
- `use crate::commands::UserCommand;`
- `use crate::commands::parse_input;`
- `use crate::output::Output;`
- `use crate::state::ReaderEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
