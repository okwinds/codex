# `codex-rs/core/src/sandboxing/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6857`
- sha256: `ecaad9667978b18696a06e1190c9b59aaf084062156fc33a86955a3adcf4fb7f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/sandboxing/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CommandSpec {`
- `pub struct ExecEnv {`
- `pub enum SandboxPreference {`
- `pub struct SandboxManager;`
- `pub fn new() -> Self {`
- `pub fn denied(&self, sandbox: SandboxType, out: &ExecToolCallOutput) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/sandboxing/mod.rs:9` `use crate::exec::ExecExpiration;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:10` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:11` `use crate::exec::SandboxType;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:12` `use crate::exec::StdoutStream;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:13` `use crate::exec::execute_exec_env;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:14` `use crate::landlock::create_linux_sandbox_command_args;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:15` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:17` `use crate::seatbelt::MACOS_PATH_TO_SEATBELT_EXECUTABLE;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:19` `use crate::seatbelt::create_seatbelt_command_args;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:21` `use crate::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:22` `use crate::spawn::CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:23` `use crate::tools::sandboxing::SandboxablePreference;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:24` `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:26` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:27` `use std::path::Path;`
- `use` `codex-rs/core/src/sandboxing/mod.rs:28` `use std::path::PathBuf;`
- `struct` `codex-rs/core/src/sandboxing/mod.rs:31` `pub struct CommandSpec {`
- `struct` `codex-rs/core/src/sandboxing/mod.rs:42` `pub struct ExecEnv {`
- `enum` `codex-rs/core/src/sandboxing/mod.rs:54` `pub enum SandboxPreference {`
- `struct` `codex-rs/core/src/sandboxing/mod.rs:70` `pub struct SandboxManager;`
- `impl` `codex-rs/core/src/sandboxing/mod.rs:72` `impl SandboxManager {`
- `fn` `codex-rs/core/src/sandboxing/mod.rs:73` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/sandboxing/mod.rs:180` `pub fn denied(&self, sandbox: SandboxType, out: &ExecToolCallOutput) -> bool {`
- `fn` `codex-rs/core/src/sandboxing/mod.rs:185` `pub async fn execute_env(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecExpiration;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::exec::SandboxType;`
- `use crate::exec::StdoutStream;`
- `use crate::exec::execute_exec_env;`
- `use crate::landlock::create_linux_sandbox_command_args;`
- `use crate::protocol::SandboxPolicy;`
- `use crate::seatbelt::MACOS_PATH_TO_SEATBELT_EXECUTABLE;`
- `use crate::seatbelt::create_seatbelt_command_args;`
- `use crate::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use crate::spawn::CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR;`
- `use crate::tools::sandboxing::SandboxablePreference;`
- `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
