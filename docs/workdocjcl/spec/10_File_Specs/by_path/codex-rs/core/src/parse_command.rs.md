# `codex-rs/core/src/parse_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `86921`
- sha256: `4b4f799a77db7163aa3e953fcdc124581e8de9cdf0ee9afbedd748106db8154a`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/parse_command.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn shlex_join(tokens: &[String]) -> String {`
- `pub fn extract_shell_command(command: &[String]) -> Option<(&str, &str)> {`
- `pub fn parse_command(command: &[String]) -> Vec<ParsedCommand> {`
- `pub fn parse_command_impl(command: &[String]) -> Vec<ParsedCommand> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/parse_command.rs:1` `use crate::bash::extract_bash_command;`
- `use` `codex-rs/core/src/parse_command.rs:2` `use crate::bash::try_parse_shell;`
- `use` `codex-rs/core/src/parse_command.rs:3` `use crate::bash::try_parse_word_only_commands_sequence;`
- `use` `codex-rs/core/src/parse_command.rs:4` `use crate::powershell::extract_powershell_command;`
- `use` `codex-rs/core/src/parse_command.rs:5` `use codex_protocol::parse_command::ParsedCommand;`
- `use` `codex-rs/core/src/parse_command.rs:6` `use shlex::split as shlex_split;`
- `use` `codex-rs/core/src/parse_command.rs:7` `use shlex::try_join as shlex_try_join;`
- `use` `codex-rs/core/src/parse_command.rs:8` `use std::path::PathBuf;`
- `fn` `codex-rs/core/src/parse_command.rs:10` `pub fn shlex_join(tokens: &[String]) -> String {`
- `fn` `codex-rs/core/src/parse_command.rs:16` `pub fn extract_shell_command(command: &[String]) -> Option<(&str, &str)> {`
- `fn` `codex-rs/core/src/parse_command.rs:30` `pub fn parse_command(command: &[String]) -> Vec<ParsedCommand> {`
- `use` `codex-rs/core/src/parse_command.rs:47` `use super::*;`
- `use` `codex-rs/core/src/parse_command.rs:48` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/parse_command.rs:49` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/parse_command.rs:50` `use std::string::ToString;`
- `fn` `codex-rs/core/src/parse_command.rs:52` `fn shlex_split_safe(s: &str) -> Vec<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:56` `fn vec_str(args: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:60` `fn assert_parsed(args: &[String], expected: Vec<ParsedCommand>) {`
- `fn` `codex-rs/core/src/parse_command.rs:66` `fn git_status_is_unknown() {`
- `fn` `codex-rs/core/src/parse_command.rs:76` `fn supports_git_grep_and_ls_files() {`
- `fn` `codex-rs/core/src/parse_command.rs:117` `fn handles_git_pipe_wc() {`
- `fn` `codex-rs/core/src/parse_command.rs:128` `fn bash_lc_redirect_not_quoted() {`
- `fn` `codex-rs/core/src/parse_command.rs:139` `fn handles_complex_bash_command_head() {`
- `fn` `codex-rs/core/src/parse_command.rs:166` `fn supports_searching_for_navigate_to_route() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/parse_command.rs:180` `fn handles_complex_bash_command() {`
- `fn` `codex-rs/core/src/parse_command.rs:193` `fn supports_rg_files_with_path_and_pipe() {`
- `fn` `codex-rs/core/src/parse_command.rs:205` `fn supports_rg_files_then_head() {`
- `fn` `codex-rs/core/src/parse_command.rs:217` `fn keeps_mutating_xargs_pipeline() {`
- `fn` `codex-rs/core/src/parse_command.rs:235` `fn rg_files_with_matches_flags_are_search() {`
- `fn` `codex-rs/core/src/parse_command.rs:279` `fn supports_cat() {`
- `fn` `codex-rs/core/src/parse_command.rs:292` `fn zsh_lc_supports_cat() {`
- `fn` `codex-rs/core/src/parse_command.rs:305` `fn supports_bat() {`
- `fn` `codex-rs/core/src/parse_command.rs:318` `fn supports_batcat() {`
- `fn` `codex-rs/core/src/parse_command.rs:331` `fn supports_less() {`
- `fn` `codex-rs/core/src/parse_command.rs:344` `fn supports_more() {`
- `fn` `codex-rs/core/src/parse_command.rs:357` `fn cd_then_cat_is_single_read() {`
- `fn` `codex-rs/core/src/parse_command.rs:369` `fn cd_with_double_dash_then_cat_is_read() {`
- `fn` `codex-rs/core/src/parse_command.rs:381` `fn cd_with_multiple_operands_uses_last() {`
- `fn` `codex-rs/core/src/parse_command.rs:393` `fn bash_cd_then_bar_is_same_as_bar() {`
- `fn` `codex-rs/core/src/parse_command.rs:404` `fn bash_cd_then_cat_is_read() {`
- `fn` `codex-rs/core/src/parse_command.rs:416` `fn supports_ls_with_pipe() {`
- `fn` `codex-rs/core/src/parse_command.rs:428` `fn supports_eza_exa_tree_du() {`
- `fn` `codex-rs/core/src/parse_command.rs:460` `fn supports_head_n() {`
- `fn` `codex-rs/core/src/parse_command.rs:473` `fn supports_head_file_only() {`
- `fn` `codex-rs/core/src/parse_command.rs:486` `fn supports_cat_sed_n() {`
- `fn` `codex-rs/core/src/parse_command.rs:499` `fn supports_tail_n_plus() {`
- `fn` `codex-rs/core/src/parse_command.rs:512` `fn supports_tail_n_last_lines() {`
- `fn` `codex-rs/core/src/parse_command.rs:526` `fn supports_tail_file_only() {`
- `fn` `codex-rs/core/src/parse_command.rs:539` `fn supports_npm_run_build_is_unknown() {`
- `fn` `codex-rs/core/src/parse_command.rs:549` `fn supports_grep_recursive_current_dir() {`
- `fn` `codex-rs/core/src/parse_command.rs:561` `fn supports_grep_recursive_specific_file() {`
- `fn` `codex-rs/core/src/parse_command.rs:579` `fn supports_egrep_and_fgrep() {`
- `fn` `codex-rs/core/src/parse_command.rs:599` `fn grep_files_with_matches_flags_are_search() {`
- `fn` `codex-rs/core/src/parse_command.rs:635` `fn supports_grep_query_with_slashes_not_shortened() {`
- `fn` `codex-rs/core/src/parse_command.rs:649` `fn supports_grep_weird_backtick_in_query() {`
- `fn` `codex-rs/core/src/parse_command.rs:661` `fn supports_cd_and_rg_files() {`
- `fn` `codex-rs/core/src/parse_command.rs:672` `fn supports_single_string_script_with_cd_and_pipe() {`
- `fn` `codex-rs/core/src/parse_command.rs:685` `fn supports_python_walks_files() {`
- `fn` `codex-rs/core/src/parse_command.rs:697` `fn supports_python3_walks_files() {`
- `fn` `codex-rs/core/src/parse_command.rs:709` `fn python_without_file_walk_is_unknown() {`
- `fn` `codex-rs/core/src/parse_command.rs:721` `fn small_formatting_always_true_commands() {`
- `fn` `codex-rs/core/src/parse_command.rs:731` `fn awk_behavior() {`
- `fn` `codex-rs/core/src/parse_command.rs:744` `fn head_behavior() {`
- `fn` `codex-rs/core/src/parse_command.rs:760` `fn tail_behavior() {`
- `fn` `codex-rs/core/src/parse_command.rs:787` `fn sed_behavior() {`
- `fn` `codex-rs/core/src/parse_command.rs:815` `fn empty_tokens_is_not_small() {`
- `fn` `codex-rs/core/src/parse_command.rs:821` `fn supports_nl_then_sed_reading() {`
- `fn` `codex-rs/core/src/parse_command.rs:834` `fn supports_sed_n() {`
- `fn` `codex-rs/core/src/parse_command.rs:847` `fn supports_awk_with_file() {`
- `fn` `codex-rs/core/src/parse_command.rs:860` `fn filters_out_printf() {`
- `fn` `codex-rs/core/src/parse_command.rs:874` `fn drops_yes_in_pipelines() {`
- `fn` `codex-rs/core/src/parse_command.rs:887` `fn supports_sed_n_then_nl_as_search() {`
- `fn` `codex-rs/core/src/parse_command.rs:903` `fn preserves_rg_with_spaces() {`
- `fn` `codex-rs/core/src/parse_command.rs:915` `fn ls_with_glob() {`
- `fn` `codex-rs/core/src/parse_command.rs:926` `fn trim_on_semicolon() {`
- `fn` `codex-rs/core/src/parse_command.rs:943` `fn split_on_or_connector() {`
- `fn` `codex-rs/core/src/parse_command.rs:961` `fn parses_mixed_sequence_with_pipes_semicolons_and_or() {`
- `fn` `codex-rs/core/src/parse_command.rs:1005` `fn strips_true_in_sequence() {`
- `fn` `codex-rs/core/src/parse_command.rs:1025` `fn strips_true_inside_bash_lc() {`
- `fn` `codex-rs/core/src/parse_command.rs:1046` `fn shorten_path_on_windows() {`
- `fn` `codex-rs/core/src/parse_command.rs:1058` `fn head_with_no_space() {`
- `fn` `codex-rs/core/src/parse_command.rs:1070` `fn bash_dash_c_pipeline_parsing() {`
- `fn` `codex-rs/core/src/parse_command.rs:1083` `fn tail_with_no_space() {`
- `fn` `codex-rs/core/src/parse_command.rs:1095` `fn grep_with_query_and_path() {`
- `fn` `codex-rs/core/src/parse_command.rs:1107` `fn supports_ag_ack_pt_rga() {`
- `fn` `codex-rs/core/src/parse_command.rs:1143` `fn ag_ack_pt_files_with_matches_flags_are_search() {`
- `fn` `codex-rs/core/src/parse_command.rs:1171` `fn rg_with_equals_style_flags() {`
- `fn` `codex-rs/core/src/parse_command.rs:1183` `fn cat_with_double_dash_and_sed_ranges() {`
- `fn` `codex-rs/core/src/parse_command.rs:1206` `fn drop_trailing_nl_in_pipeline() {`
- `fn` `codex-rs/core/src/parse_command.rs:1218` `fn ls_with_time_style_and_path() {`
- `fn` `codex-rs/core/src/parse_command.rs:1230` `fn fd_file_finder_variants() {`
- `fn` `codex-rs/core/src/parse_command.rs:1251` `fn find_basic_name_filter() {`
- `fn` `codex-rs/core/src/parse_command.rs:1263` `fn find_type_only_path() {`
- `fn` `codex-rs/core/src/parse_command.rs:1274` `fn bin_bash_lc_sed() {`
- `fn` `codex-rs/core/src/parse_command.rs:1285` `fn bin_zsh_lc_sed() {`
- `fn` `codex-rs/core/src/parse_command.rs:1297` `fn powershell_command_is_stripped() {`
- `fn` `codex-rs/core/src/parse_command.rs:1307` `fn pwsh_with_noprofile_and_c_alias_is_stripped() {`
- `fn` `codex-rs/core/src/parse_command.rs:1317` `fn powershell_with_path_is_stripped() {`
- `fn` `codex-rs/core/src/parse_command.rs:1333` `pub fn parse_command_impl(command: &[String]) -> Vec<ParsedCommand> {`
- `fn` `codex-rs/core/src/parse_command.rs:1396` `fn simplify_once(commands: &[ParsedCommand]) -> Option<Vec<ParsedCommand>> {`
- `fn` `codex-rs/core/src/parse_command.rs:1455` `fn is_valid_sed_n_arg(arg: Option<&str>) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:1477` `fn sed_read_path(args: &[String]) -> Option<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1523` `fn normalize_tokens(cmd: &[String]) -> Vec<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1542` `fn contains_connectors(tokens: &[String]) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:1548` `fn split_on_connectors(tokens: &[String]) -> Vec<Vec<String>> {`
- `fn` `codex-rs/core/src/parse_command.rs:1566` `fn trim_at_connector(tokens: &[String]) -> Vec<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1579` `fn short_display_path(path: &str) -> String {`
- `fn` `codex-rs/core/src/parse_command.rs:1624` `fn first_non_flag_operand(args: &[String], flags_with_vals: &[&str]) -> Option<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1631` `fn single_non_flag_operand(args: &[String], flags_with_vals: &[&str]) -> Option<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1674` `fn parse_grep_like(main_cmd: &[String], args: &[String]) -> ParsedCommand {`
- `fn` `codex-rs/core/src/parse_command.rs:1731` `fn awk_data_file_operand(args: &[String]) -> Option<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1756` `fn python_walks_files(args: &[String]) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:1775` `fn is_python_command(cmd: &str) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:1783` `fn cd_target(args: &[String]) -> Option<String> {`
- `fn` `codex-rs/core/src/parse_command.rs:1808` `fn is_pathish(s: &str) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:1817` `fn parse_fd_query_and_path(tail: &[String]) -> (Option<String>, Option<String>) {`
- `fn` `codex-rs/core/src/parse_command.rs:1850` `fn parse_find_query_and_path(tail: &[String]) -> (Option<String>, Option<String>) {`
- `fn` `codex-rs/core/src/parse_command.rs:1876` `fn parse_shell_lc_commands(original: &[String]) -> Option<Vec<ParsedCommand>> {`
- `fn` `codex-rs/core/src/parse_command.rs:2009` `fn is_small_formatting_command(tokens: &[String]) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:2078` `fn is_mutating_xargs_command(tokens: &[String]) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:2082` `fn xargs_subcommand(tokens: &[String]) -> Option<&[String]> {`
- `fn` `codex-rs/core/src/parse_command.rs:2108` `fn xargs_is_mutating_subcommand(tokens: &[String]) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:2120` `fn xargs_has_in_place_flag(tokens: &[String]) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:2126` `fn drop_small_formatting_commands(mut commands: Vec<Vec<String>>) -> Vec<Vec<String>> {`
- `fn` `codex-rs/core/src/parse_command.rs:2131` `fn summarize_main_tokens(main_cmd: &[String]) -> ParsedCommand {`
- `fn` `codex-rs/core/src/parse_command.rs:2558` `fn is_abs_like(path: &str) -> bool {`
- `fn` `codex-rs/core/src/parse_command.rs:2573` `fn join_paths(base: &str, rel: &str) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::bash::extract_bash_command;`
- `use crate::bash::try_parse_shell;`
- `use crate::bash::try_parse_word_only_commands_sequence;`
- `use crate::powershell::extract_powershell_command;`
- `use codex_protocol::parse_command::ParsedCommand;`
- `use shlex::split as shlex_split;`
- `use shlex::try_join as shlex_try_join;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::path::PathBuf;`
- `use std::string::ToString;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
