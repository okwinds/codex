# `codex-rs/exec/src/cli.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9268`
- sha256: `c451dc0c006f8e53a406b37a18139426da868481853526f45cf4980d620da2fa`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/cli.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Cli {`
- `pub enum Command {`
- `pub struct ResumeArgs {`
- `pub struct ReviewArgs {`
- `pub enum Color {`

## Definitions (auto, per-file)
- `use` `codex-rs/exec/src/cli.rs:1` `use clap::Args;`
- `use` `codex-rs/exec/src/cli.rs:2` `use clap::FromArgMatches;`
- `use` `codex-rs/exec/src/cli.rs:3` `use clap::Parser;`
- `use` `codex-rs/exec/src/cli.rs:4` `use clap::ValueEnum;`
- `use` `codex-rs/exec/src/cli.rs:5` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/exec/src/cli.rs:6` `use std::path::PathBuf;`
- `struct` `codex-rs/exec/src/cli.rs:10` `pub struct Cli {`
- `enum` `codex-rs/exec/src/cli.rs:109` `pub enum Command {`
- `struct` `codex-rs/exec/src/cli.rs:118` `struct ResumeArgsRaw {`
- `struct` `codex-rs/exec/src/cli.rs:150` `pub struct ResumeArgs {`
- `impl` `codex-rs/exec/src/cli.rs:168` `impl From<ResumeArgsRaw> for ResumeArgs {`
- `fn` `codex-rs/exec/src/cli.rs:169` `fn from(raw: ResumeArgsRaw) -> Self {`
- `impl` `codex-rs/exec/src/cli.rs:187` `impl Args for ResumeArgs {`
- `fn` `codex-rs/exec/src/cli.rs:188` `fn augment_args(cmd: clap::Command) -> clap::Command {`
- `fn` `codex-rs/exec/src/cli.rs:192` `fn augment_args_for_update(cmd: clap::Command) -> clap::Command {`
- `impl` `codex-rs/exec/src/cli.rs:197` `impl FromArgMatches for ResumeArgs {`
- `fn` `codex-rs/exec/src/cli.rs:198` `fn from_arg_matches(matches: &clap::ArgMatches) -> Result<Self, clap::Error> {`
- `fn` `codex-rs/exec/src/cli.rs:202` `fn update_from_arg_matches(&mut self, matches: &clap::ArgMatches) -> Result<(), clap::Error> {`
- `struct` `codex-rs/exec/src/cli.rs:209` `pub struct ReviewArgs {`
- `enum` `codex-rs/exec/src/cli.rs:245` `pub enum Color {`
- `use` `codex-rs/exec/src/cli.rs:254` `use super::*;`
- `use` `codex-rs/exec/src/cli.rs:255` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/exec/src/cli.rs:258` `fn resume_parses_prompt_after_global_flags() {`
- `const` `codex-rs/exec/src/cli.rs:259` `const PROMPT: &str = "echo resume-with-global-flags-after-subcommand";`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Args;`
- `use clap::FromArgMatches;`
- `use clap::Parser;`
- `use clap::ValueEnum;`
- `use codex_common::CliConfigOverrides;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
