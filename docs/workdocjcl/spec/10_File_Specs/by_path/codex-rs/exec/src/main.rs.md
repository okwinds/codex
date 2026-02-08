# `codex-rs/exec/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2556`
- sha256: `8594d341f85e890a245b8a4d083b591e50598c52b48fb56b83667182e9a5d9a1`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/main.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/exec/src/main.rs:12` `use clap::Parser;`
- `use` `codex-rs/exec/src/main.rs:13` `use codex_arg0::arg0_dispatch_or_else;`
- `use` `codex-rs/exec/src/main.rs:14` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/exec/src/main.rs:15` `use codex_exec::Cli;`
- `use` `codex-rs/exec/src/main.rs:16` `use codex_exec::run_main;`
- `struct` `codex-rs/exec/src/main.rs:19` `struct TopCli {`
- `fn` `codex-rs/exec/src/main.rs:27` `fn main() -> anyhow::Result<()> {`
- `use` `codex-rs/exec/src/main.rs:44` `use super::*;`
- `use` `codex-rs/exec/src/main.rs:45` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/exec/src/main.rs:48` `fn top_cli_parses_resume_prompt_after_config_flag() {`
- `const` `codex-rs/exec/src/main.rs:49` `const PROMPT: &str = "echo resume-with-global-flags-after-subcommand";`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use codex_arg0::arg0_dispatch_or_else;`
- `use codex_common::CliConfigOverrides;`
- `use codex_exec::Cli;`
- `use codex_exec::run_main;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
