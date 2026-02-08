# `codex-rs/tui/src/bottom_pane/prompt_args.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `29091`
- sha256: `dde282150c220547e7097e1875c12c40038e60b7a76acaff18aeaa2bc56ecb5a`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/prompt_args.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum PromptArgsError {`
- `pub enum PromptExpansionError {`
- `pub fn user_message(&self) -> String {`
- `pub fn parse_slash_name(line: &str) -> Option<(&str, &str, usize)> {`
- `pub struct PromptArg {`
- `pub struct PromptExpansion {`
- `pub fn parse_positional_args(rest: &str, text_elements: &[TextElement]) -> Vec<PromptArg> {`
- `pub fn prompt_argument_names(content: &str) -> Vec<String> {`
- `pub fn parse_prompt_inputs(`
- `pub fn expand_custom_prompt(`
- `pub fn prompt_has_numeric_placeholders(content: &str) -> bool {`
- `pub fn extract_positional_args_for_prompt_line(`
- `pub fn expand_if_numeric_with_positional_args(`
- `pub fn expand_numeric_placeholders(content: &str, args: &[PromptArg]) -> PromptExpansion {`
- `pub fn prompt_command_with_arg_placeholders(name: &str, args: &[String]) -> (String, usize) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:1` `use codex_protocol::custom_prompts::CustomPrompt;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:2` `use codex_protocol::custom_prompts::PROMPTS_CMD_PREFIX;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:3` `use codex_protocol::user_input::ByteRange;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:4` `use codex_protocol::user_input::TextElement;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:5` `use lazy_static::lazy_static;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:6` `use regex_lite::Regex;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:7` `use shlex::Shlex;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:8` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:9` `use std::collections::HashSet;`
- `static` `codex-rs/tui/src/bottom_pane/prompt_args.rs:12` `static ref PROMPT_ARG_REGEX: Regex =`
- `enum` `codex-rs/tui/src/bottom_pane/prompt_args.rs:17` `pub enum PromptArgsError {`
- `impl` `codex-rs/tui/src/bottom_pane/prompt_args.rs:22` `impl PromptArgsError {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:23` `fn describe(&self, command: &str) -> String {`
- `enum` `codex-rs/tui/src/bottom_pane/prompt_args.rs:36` `pub enum PromptExpansionError {`
- `impl` `codex-rs/tui/src/bottom_pane/prompt_args.rs:47` `impl PromptExpansionError {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:48` `pub fn user_message(&self) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:67` `pub fn parse_slash_name(line: &str) -> Option<(&str, &str, usize)> {`
- `struct` `codex-rs/tui/src/bottom_pane/prompt_args.rs:89` `pub struct PromptArg {`
- `struct` `codex-rs/tui/src/bottom_pane/prompt_args.rs:95` `pub struct PromptExpansion {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:103` `pub fn parse_positional_args(rest: &str, text_elements: &[TextElement]) -> Vec<PromptArg> {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:112` `pub fn prompt_argument_names(content: &str) -> Vec<String> {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:135` `fn shift_text_element_left(elem: &TextElement, offset: usize) -> Option<TextElement> {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:149` `pub fn parse_prompt_inputs(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:191` `pub fn expand_custom_prompt(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:256` `pub fn prompt_has_numeric_placeholders(content: &str) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:276` `pub fn extract_positional_args_for_prompt_line(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:316` `pub fn expand_if_numeric_with_positional_args(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:335` `pub fn expand_numeric_placeholders(content: &str, args: &[PromptArg]) -> PromptExpansion {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:379` `fn parse_tokens_with_elements(rest: &str, text_elements: &[TextElement]) -> Vec<PromptArg> {`
- `struct` `codex-rs/tui/src/bottom_pane/prompt_args.rs:391` `struct ElementReplacement {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:400` `fn replace_text_elements_with_sentinels(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:432` `fn apply_replacements_to_token(token: String, replacements: &[ElementReplacement]) -> PromptArg {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:488` `fn expand_named_placeholders_with_elements(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:516` `fn append_arg_with_elements(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:534` `fn append_joined_args_with_elements(`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:550` `pub fn prompt_command_with_arg_placeholders(name: &str, args: &[String]) -> (String, usize) {`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:564` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/prompt_args.rs:565` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:568` `fn expand_arguments_basic() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:589` `fn quoted_values_ok() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:614` `fn invalid_arg_token_reports_error() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:629` `fn missing_required_args_reports_error() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:645` `fn escaped_placeholder_is_ignored() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:657` `fn escaped_placeholder_remains_literal() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:677` `fn positional_args_treat_placeholder_with_spaces_as_single_token() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:714` `fn extract_positional_args_shifts_element_offsets_into_args_str() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:751` `fn key_value_args_treat_placeholder_with_spaces_as_single_token() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:785` `fn positional_args_allow_placeholder_inside_quotes() {`
- `fn` `codex-rs/tui/src/bottom_pane/prompt_args.rs:822` `fn key_value_args_allow_placeholder_inside_quotes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::custom_prompts::CustomPrompt;`
- `use codex_protocol::custom_prompts::PROMPTS_CMD_PREFIX;`
- `use codex_protocol::user_input::ByteRange;`
- `use codex_protocol::user_input::TextElement;`
- `use lazy_static::lazy_static;`
- `use regex_lite::Regex;`
- `use shlex::Shlex;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
