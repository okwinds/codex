# `codex-rs/core/src/command_safety/windows_dangerous_commands.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21453`
- sha256: `fccf9178f0c49eee6e7fe39a1483310755dd1ab76e58b8ac4c89bc152af81d62`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/command_safety/windows_dangerous_commands.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn is_dangerous_command_windows(command: &[String]) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:1` `use std::path::Path;`
- `use` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:3` `use once_cell::sync::Lazy;`
- `use` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:4` `use regex::Regex;`
- `use` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:5` `use shlex::split as shlex_split;`
- `use` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:6` `use url::Url;`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:8` `pub fn is_dangerous_command_windows(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:23` `fn is_dangerous_powershell(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:93` `fn is_dangerous_cmd(command: &[String]) -> bool {`
- `const` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:131` `const CMD_SEPARATORS: &[&str] = &["&", "&&", "|", "||"];`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:160` `fn is_direct_gui_launch(command: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:191` `fn split_embedded_cmd_operators(token: &str) -> Vec<String> {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:226` `fn has_force_delete_cmdlet(tokens: &[String]) -> bool {`
- `const` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:227` `const DELETE_CMDLETS: &[&str] = &["remove-item", "ri", "rm", "del", "erase", "rd", "rmdir"];`
- `const` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:230` `const SEG_SEPS: &[char] = &[';', '|', '&', '\n', '\r', '\t'];`
- `const` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:233` `const SOFT_SEPS: &[char] = &['{', '}', '(', ')', '[', ']', ',', ';'];`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:294` `fn has_force_flag_cmd(args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:299` `fn has_recursive_flag_cmd(args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:304` `fn has_quiet_flag_cmd(args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:308` `fn args_have_url(args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:312` `fn looks_like_url(token: &str) -> bool {`
- `static` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:315` `static RE: Lazy<Option<Regex>> =`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:337` `fn executable_basename(exe: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:344` `fn is_powershell_executable(exe: &str) -> bool {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:351` `fn is_browser_executable(name: &str) -> bool {`
- `struct` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:365` `struct ParsedPowershell {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:369` `fn parse_powershell_invocation(args: &[String]) -> Option<ParsedPowershell> {`
- `use` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:413` `use super::is_dangerous_command_windows;`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:415` `fn vec_str(items: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:420` `fn powershell_start_process_url_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:430` `fn powershell_start_process_url_with_trailing_semicolon_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:439` `fn powershell_start_process_local_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:448` `fn cmd_start_with_url_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:458` `fn msedge_with_url_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:466` `fn explorer_with_directory_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:476` `fn powershell_remove_item_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:485` `fn powershell_remove_item_recurse_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:494` `fn powershell_ri_alias_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:503` `fn powershell_remove_item_without_force_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:513` `fn cmd_del_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:520` `fn cmd_erase_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:527` `fn cmd_del_without_force_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:534` `fn cmd_rd_recursive_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:541` `fn cmd_rd_without_quiet_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:548` `fn cmd_rmdir_recursive_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:556` `fn powershell_remove_item_path_recurse_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:565` `fn powershell_remove_item_force_with_semicolon_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:574` `fn powershell_remove_item_force_inside_block_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:583` `fn powershell_remove_item_force_inside_brackets_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:592` `fn cmd_del_path_containing_f_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:602` `fn cmd_rd_path_containing_s_is_not_flagged() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:612` `fn cmd_bypass_chained_del_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:619` `fn powershell_chained_no_space_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:628` `fn powershell_comma_separated_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:637` `fn cmd_echo_del_is_not_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:644` `fn cmd_del_single_string_argument_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:653` `fn cmd_del_chained_single_string_argument_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:662` `fn cmd_chained_no_space_del_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:671` `fn cmd_chained_andand_no_space_del_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:680` `fn cmd_chained_oror_no_space_del_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:689` `fn cmd_start_url_single_string_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:698` `fn cmd_chained_no_space_rmdir_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:707` `fn cmd_del_force_uppercase_flag_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:714` `fn cmdexe_r_del_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:721` `fn cmd_start_quoted_url_single_string_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:730` `fn cmd_start_title_then_url_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:739` `fn powershell_rm_alias_force_is_dangerous() {`
- `fn` `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:748` `fn powershell_benign_force_separate_command_is_not_dangerous() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use once_cell::sync::Lazy;`
- `use regex::Regex;`
- `use shlex::split as shlex_split;`
- `use url::Url;`
- `use super::is_dangerous_command_windows;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
