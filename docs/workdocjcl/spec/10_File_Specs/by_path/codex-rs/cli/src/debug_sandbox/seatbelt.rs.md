# `codex-rs/cli/src/debug_sandbox/seatbelt.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3703`
- sha256: `f66b9c094212dc83bc06e5c573a849ec4685961cae77721e92e7c0b407e87553`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/debug_sandbox/seatbelt.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct SandboxDenial {`
- `pub struct DenialLogger {`

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:1` `use std::collections::HashSet;`
- `use` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:2` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:3` `use tokio::process::Child;`
- `use` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:4` `use tokio::task::JoinHandle;`
- `use` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:6` `use super::pid_tracker::PidTracker;`
- `struct` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:8` `pub struct SandboxDenial {`
- `struct` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:13` `pub struct DenialLogger {`
- `impl` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:19` `impl DenialLogger {`
- `fn` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:87` `fn start_log_stream() -> Option<Child> {`
- `use` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:88` `use std::process::Stdio;`
- `const` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:90` `const PREDICATE: &str = r#"(((processID == 0) AND (senderImagePath CONTAINS "/Sandbox")) OR (subsystem == "com.apple.sandbox.reporting"))"#;`
- `fn` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:102` `fn parse_message(msg: &str) -> Option<(i32, String, String)> {`
- `static` `codex-rs/cli/src/debug_sandbox/seatbelt.rs:105` `static RE: std::sync::OnceLock<regex_lite::Regex> = std::sync::OnceLock::new();`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashSet;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::process::Child;`
- `use tokio::task::JoinHandle;`
- `use super::pid_tracker::PidTracker;`
- `use std::process::Stdio;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/03_API/CLI.md`
