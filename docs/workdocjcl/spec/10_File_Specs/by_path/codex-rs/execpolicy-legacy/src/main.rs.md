# `codex-rs/execpolicy-legacy/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4978`
- sha256: `fe5658e959f30f77fd3aa2d861a10515dbb7899e730fe5edd183fac14fd5b02b`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/main.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct Args {`
- `pub enum Command {`
- `pub struct ExecArg {`
- `fn main() -> Result<()> {`
- `pub enum Output {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/main.rs:1` `use anyhow::Result;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:2` `use clap::Parser;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:3` `use clap::Subcommand;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:4` `use codex_execpolicy_legacy::ExecCall;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:5` `use codex_execpolicy_legacy::MatchedExec;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:6` `use codex_execpolicy_legacy::Policy;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:7` `use codex_execpolicy_legacy::PolicyParser;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:8` `use codex_execpolicy_legacy::ValidExec;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:9` `use codex_execpolicy_legacy::get_default_policy;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:11` `use serde::Serialize;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:12` `use serde::de;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:13` `use starlark::Error as StarlarkError;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:14` `use std::path::PathBuf;`
- `use` `codex-rs/execpolicy-legacy/src/main.rs:15` `use std::str::FromStr;`
- `const` `codex-rs/execpolicy-legacy/src/main.rs:17` `const MATCHED_BUT_WRITES_FILES_EXIT_CODE: i32 = 12;`
- `const` `codex-rs/execpolicy-legacy/src/main.rs:18` `const MIGHT_BE_SAFE_EXIT_CODE: i32 = 13;`
- `const` `codex-rs/execpolicy-legacy/src/main.rs:19` `const FORBIDDEN_EXIT_CODE: i32 = 14;`
- `struct` `codex-rs/execpolicy-legacy/src/main.rs:23` `pub struct Args {`
- `enum` `codex-rs/execpolicy-legacy/src/main.rs:38` `pub enum Command {`
- `struct` `codex-rs/execpolicy-legacy/src/main.rs:55` `pub struct ExecArg {`
- `fn` `codex-rs/execpolicy-legacy/src/main.rs:62` `fn main() -> Result<()> {`
- `fn` `codex-rs/execpolicy-legacy/src/main.rs:97` `fn check_command(`
- `enum` `codex-rs/execpolicy-legacy/src/main.rs:129` `pub enum Output {`
- `impl` `codex-rs/execpolicy-legacy/src/main.rs:163` `impl FromStr for ExecArg {`
- `type` `codex-rs/execpolicy-legacy/src/main.rs:164` `type Err = anyhow::Error;`
- `fn` `codex-rs/execpolicy-legacy/src/main.rs:166` `fn from_str(s: &str) -> Result<Self, Self::Err> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use clap::Parser;`
- `use clap::Subcommand;`
- `use codex_execpolicy_legacy::ExecCall;`
- `use codex_execpolicy_legacy::MatchedExec;`
- `use codex_execpolicy_legacy::Policy;`
- `use codex_execpolicy_legacy::PolicyParser;`
- `use codex_execpolicy_legacy::ValidExec;`
- `use codex_execpolicy_legacy::get_default_policy;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde::de;`
- `use starlark::Error as StarlarkError;`
- `use std::path::PathBuf;`
- `use std::str::FromStr;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
