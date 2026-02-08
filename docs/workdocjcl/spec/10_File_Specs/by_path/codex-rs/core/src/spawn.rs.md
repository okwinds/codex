# `codex-rs/core/src/spawn.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4007`
- sha256: `49eb737eab1cbd587ce2f1a2bae59f8cd7875df9430cea5d99e7e0bd215ba05b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/spawn.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub enum StdioPolicy {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/spawn.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/spawn.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/spawn.rs:3` `use std::process::Stdio;`
- `use` `codex-rs/core/src/spawn.rs:4` `use tokio::process::Child;`
- `use` `codex-rs/core/src/spawn.rs:5` `use tokio::process::Command;`
- `use` `codex-rs/core/src/spawn.rs:6` `use tracing::trace;`
- `use` `codex-rs/core/src/spawn.rs:8` `use crate::protocol::SandboxPolicy;`
- `const` `codex-rs/core/src/spawn.rs:18` `pub const CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR: &str = "CODEX_SANDBOX_NETWORK_DISABLED";`
- `const` `codex-rs/core/src/spawn.rs:23` `pub const CODEX_SANDBOX_ENV_VAR: &str = "CODEX_SANDBOX";`
- `enum` `codex-rs/core/src/spawn.rs:26` `pub enum StdioPolicy {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use std::process::Stdio;`
- `use tokio::process::Child;`
- `use tokio::process::Command;`
- `use tracing::trace;`
- `use crate::protocol::SandboxPolicy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
