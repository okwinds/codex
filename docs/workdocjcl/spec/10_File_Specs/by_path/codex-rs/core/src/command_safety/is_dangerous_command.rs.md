# `codex-rs/core/src/command_safety/is_dangerous_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11344`
- sha256: `543bc998ad8c0aef1406ec89e3dd5fb2041419ca4a0ae69e9c25f74c459a857b`
- generated_utc: `2026-02-08T10:45:26Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/command_safety/is_dangerous_command.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn command_might_be_dangerous(command: &[String]) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/command_safety/is_dangerous_command.rs:1` `use crate::bash::parse_shell_lc_plain_commands;`
- `mod` `codex-rs/core/src/command_safety/is_dangerous_command.rs:4` `mod windows_dangerous_commands;`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:6` `pub fn command_might_be_dangerous(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:30` `fn is_git_global_option_with_value(arg: &str) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:43` `fn is_git_global_option_with_inline_value(arg: &str) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:103` `fn is_dangerous_to_call_with_exec(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:136` `fn git_branch_is_delete(branch_args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:147` `fn short_flag_group_contains(arg: &str, target: char) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:151` `fn git_push_is_dangerous(push_args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:165` `fn git_push_refspec_is_dangerous(arg: &str) -> bool {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:170` `fn git_clean_is_force(clean_args: &[String]) -> bool {`
- `use` `codex-rs/core/src/command_safety/is_dangerous_command.rs:180` `use super::*;`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:182` `fn vec_str(items: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:187` `fn git_reset_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:192` `fn bash_git_reset_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:201` `fn zsh_git_reset_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:210` `fn git_status_is_not_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:215` `fn bash_git_status_is_not_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:224` `fn sudo_git_reset_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:231` `fn usr_bin_git_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:240` `fn git_branch_delete_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:255` `fn git_branch_delete_with_stacked_short_flags_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:271` `fn git_branch_delete_with_global_options_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:291` `fn git_checkout_reset_is_not_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:300` `fn git_push_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:319` `fn git_push_plus_refspec_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:332` `fn git_push_delete_flag_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:342` `fn git_push_delete_refspec_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:354` `fn git_push_without_force_is_not_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:361` `fn git_clean_force_is_dangerous_even_when_f_is_not_first_flag() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:374` `fn rm_rf_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/is_dangerous_command.rs:379` `fn rm_f_is_dangerous() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::bash::parse_shell_lc_plain_commands;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
