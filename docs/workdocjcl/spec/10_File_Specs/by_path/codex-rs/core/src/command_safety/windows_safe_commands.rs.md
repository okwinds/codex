# `codex-rs/core/src/command_safety/windows_safe_commands.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21045`
- sha256: `07f0d6ff2dc6531c64a091613740c38fea474fda6e69e29a465fdc01c4feaa2a`
- generated_utc: `2026-02-08T10:45:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/command_safety/windows_safe_commands.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn is_safe_command_windows(command: &[String]) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:1` `use base64::Engine;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:2` `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:3` `use serde::Deserialize;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:4` `use std::path::Path;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:5` `use std::process::Command;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:6` `use std::sync::LazyLock;`
- `const` `codex-rs/core/src/command_safety/windows_safe_commands.rs:8` `const POWERSHELL_PARSER_SCRIPT: &str = include_str!("powershell_parser.ps1");`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:12` `pub fn is_safe_command_windows(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:25` `fn try_parse_powershell_command_sequence(command: &[String]) -> Option<Vec<Vec<String>>> {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:35` `fn parse_powershell_invocation(executable: &str, args: &[String]) -> Option<Vec<Vec<String>>> {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:100` `fn parse_powershell_script(executable: &str, script: &str) -> Option<Vec<Vec<String>>> {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:111` `fn is_powershell_executable(exe: &str) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:127` `fn parse_with_powershell_ast(executable: &str, script: &str) -> PowershellParseOutcome {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:154` `fn encode_powershell_base64(script: &str) -> String {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:162` `fn encoded_parser_script() -> &'static str {`
- `static` `codex-rs/core/src/command_safety/windows_safe_commands.rs:163` `static ENCODED: LazyLock<String> =`
- `struct` `codex-rs/core/src/command_safety/windows_safe_commands.rs:170` `struct PowershellParserOutput {`
- `impl` `codex-rs/core/src/command_safety/windows_safe_commands.rs:175` `impl PowershellParserOutput {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:176` `fn into_outcome(self) -> PowershellParseOutcome {`
- `enum` `codex-rs/core/src/command_safety/windows_safe_commands.rs:194` `enum PowershellParseOutcome {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:200` `fn join_arguments_as_script(args: &[String]) -> String {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:211` `fn quote_argument(arg: &str) -> String {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:225` `fn is_safe_powershell_command(words: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:290` `fn is_safe_ripgrep(words: &[String]) -> bool {`
- `const` `codex-rs/core/src/command_safety/windows_safe_commands.rs:291` `const UNSAFE_RIPGREP_OPTIONS_WITH_ARGS: &[&str] = &["--pre", "--hostname-bin"];`
- `const` `codex-rs/core/src/command_safety/windows_safe_commands.rs:292` `const UNSAFE_RIPGREP_OPTIONS_WITHOUT_ARGS: &[&str] = &["--search-zip", "-z"];`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:305` `fn is_safe_git_command(words: &[String]) -> bool {`
- `const` `codex-rs/core/src/command_safety/windows_safe_commands.rs:306` `const SAFE_SUBCOMMANDS: &[&str] = &["status", "log", "show", "diff", "cat-file"];`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:349` `use super::*;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:350` `use crate::powershell::try_find_pwsh_executable_blocking;`
- `use` `codex-rs/core/src/command_safety/windows_safe_commands.rs:351` `use std::string::ToString;`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:354` `fn vec_str(args: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:359` `fn recognizes_safe_powershell_wrappers() {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:392` `fn accepts_full_path_powershell_invocations() {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:415` `fn allows_read_only_pipelines_and_git_usage() {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:466` `fn rejects_powershell_commands_with_side_effects() {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:565` `fn accepts_constant_expression_arguments() {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:580` `fn rejects_dynamic_arguments() {`
- `fn` `codex-rs/core/src/command_safety/windows_safe_commands.rs:595` `fn uses_invoked_powershell_variant_for_parsing() {`

## Dependencies (auto sample)
### Imports / Includes
- `use base64::Engine;`
- `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use serde::Deserialize;`
- `use std::path::Path;`
- `use std::process::Command;`
- `use std::sync::LazyLock;`
- `use super::*;`
- `use crate::powershell::try_find_pwsh_executable_blocking;`
- `use std::string::ToString;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
