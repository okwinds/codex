# `codex-rs/core/src/tools/runtimes/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7736`
- sha256: `0c570f1f7c8457c7be1fc0998f2e3e3963e90cc3c59b1ba5218dc9732e0e0015`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/runtimes/mod.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:7` `use crate::exec::ExecExpiration;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:8` `use crate::sandboxing::CommandSpec;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:9` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:10` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:11` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:12` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:13` `use std::path::Path;`
- `mod` `codex-rs/core/src/tools/runtimes/mod.rs:15` `pub mod apply_patch;`
- `mod` `codex-rs/core/src/tools/runtimes/mod.rs:16` `pub mod shell;`
- `mod` `codex-rs/core/src/tools/runtimes/mod.rs:17` `pub mod unified_exec;`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:91` `fn shell_single_quote(input: &str) -> String {`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:97` `use super::*;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:98` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:99` `use crate::shell_snapshot::ShellSnapshot;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:100` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:101` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:102` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:103` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:104` `use tokio::sync::watch;`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:106` `fn shell_with_snapshot(`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:122` `fn maybe_wrap_shell_lc_with_snapshot_bootstraps_in_user_shell() {`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:142` `fn maybe_wrap_shell_lc_with_snapshot_escapes_single_quotes() {`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:159` `fn maybe_wrap_shell_lc_with_snapshot_uses_bash_bootstrap_shell() {`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:179` `fn maybe_wrap_shell_lc_with_snapshot_uses_sh_bootstrap_shell() {`
- `fn` `codex-rs/core/src/tools/runtimes/mod.rs:199` `fn maybe_wrap_shell_lc_with_snapshot_preserves_trailing_args() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecExpiration;`
- `use crate::sandboxing::CommandSpec;`
- `use crate::sandboxing::SandboxPermissions;`
- `use crate::shell::Shell;`
- `use crate::tools::sandboxing::ToolError;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use super::*;`
- `use crate::shell::ShellType;`
- `use crate::shell_snapshot::ShellSnapshot;`
- `use pretty_assertions::assert_eq;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use tempfile::tempdir;`
- `use tokio::sync::watch;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
