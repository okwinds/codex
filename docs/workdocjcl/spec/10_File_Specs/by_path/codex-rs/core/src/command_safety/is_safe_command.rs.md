# `codex-rs/core/src/command_safety/is_safe_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19148`
- sha256: `9d6bd38879ffe643980754cb29a4418579772bb7c3648be4342c94b2dc6cb174`
- generated_utc: `2026-02-08T10:45:27Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/command_safety/is_safe_command.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn is_known_safe_command(command: &[String]) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/command_safety/is_safe_command.rs:1` `use crate::bash::parse_shell_lc_plain_commands;`
- `use` `codex-rs/core/src/command_safety/is_safe_command.rs:5` `use crate::command_safety::is_dangerous_command::find_git_subcommand;`
- `use` `codex-rs/core/src/command_safety/is_safe_command.rs:6` `use crate::command_safety::windows_safe_commands::is_safe_command_windows;`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:8` `pub fn is_known_safe_command(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:45` `fn is_safe_to_call_with_exec(command: &[String]) -> bool {`
- `const` `codex-rs/core/src/command_safety/is_safe_command.rs:86` `const UNSAFE_BASE64_OPTIONS: &[&str] = &["-o", "--output"];`
- `const` `codex-rs/core/src/command_safety/is_safe_command.rs:100` `const UNSAFE_FIND_OPTIONS: &[&str] = &[`
- `const` `codex-rs/core/src/command_safety/is_safe_command.rs:116` `const UNSAFE_RIPGREP_OPTIONS_WITH_ARGS: &[&str] = &[`
- `const` `codex-rs/core/src/command_safety/is_safe_command.rs:122` `const UNSAFE_RIPGREP_OPTIONS_WITHOUT_ARGS: &[&str] = &[`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:187` `fn git_branch_is_read_only(branch_args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:213` `fn git_has_config_override_global_option(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:221` `fn git_subcommand_args_are_read_only(args: &[String]) -> bool {`
- `const` `codex-rs/core/src/command_safety/is_safe_command.rs:224` `const UNSAFE_GIT_FLAGS: &[&str] = &[`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:246` `fn is_valid_sed_n_arg(arg: Option<&str>) -> bool {`
- `use` `codex-rs/core/src/command_safety/is_safe_command.rs:280` `use super::*;`
- `use` `codex-rs/core/src/command_safety/is_safe_command.rs:281` `use std::string::ToString;`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:283` `fn vec_str(args: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:288` `fn known_safe_examples() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:322` `fn git_branch_mutating_flags_are_not_safe() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:334` `fn git_branch_global_options_respect_safety_rules() {`
- `use` `codex-rs/core/src/command_safety/is_safe_command.rs:335` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:352` `fn git_first_positional_is_the_subcommand() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:361` `fn git_output_and_config_override_flags_are_not_safe() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:397` `fn cargo_check_is_not_safe() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:402` `fn zsh_lc_safe_command_sequence() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:407` `fn unknown_or_partial() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:436` `fn base64_output_options_are_unsafe() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:451` `fn ripgrep_rules() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:485` `fn windows_powershell_full_path_is_safe() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:499` `fn bash_lc_safe_examples() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:531` `fn bash_lc_safe_examples_with_operators() {`
- `fn` `codex-rs/core/src/command_safety/is_safe_command.rs:555` `fn bash_lc_unsafe_examples() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::bash::parse_shell_lc_plain_commands;`
- `use crate::command_safety::is_dangerous_command::find_git_subcommand;`
- `use crate::command_safety::windows_safe_commands::is_safe_command_windows;`
- `use super::*;`
- `use std::string::ToString;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
