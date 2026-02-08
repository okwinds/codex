# `codex-rs/core/src/bash.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12390`
- sha256: `b5aa218e4f4f26927f814cd9a7010e3c9339012b80271494990b140d7f46a0db`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/bash.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn try_parse_shell(shell_lc_arg: &str) -> Option<Tree> {`
- `pub fn try_parse_word_only_commands_sequence(tree: &Tree, src: &str) -> Option<Vec<Vec<String>>> {`
- `pub fn extract_bash_command(command: &[String]) -> Option<(&str, &str)> {`
- `pub fn parse_shell_lc_plain_commands(command: &[String]) -> Option<Vec<Vec<String>>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/bash.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/bash.rs:3` `use tree_sitter::Node;`
- `use` `codex-rs/core/src/bash.rs:4` `use tree_sitter::Parser;`
- `use` `codex-rs/core/src/bash.rs:5` `use tree_sitter::Tree;`
- `use` `codex-rs/core/src/bash.rs:6` `use tree_sitter_bash::LANGUAGE as BASH;`
- `use` `codex-rs/core/src/bash.rs:8` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/bash.rs:9` `use crate::shell::detect_shell_type;`
- `fn` `codex-rs/core/src/bash.rs:13` `pub fn try_parse_shell(shell_lc_arg: &str) -> Option<Tree> {`
- `fn` `codex-rs/core/src/bash.rs:29` `pub fn try_parse_word_only_commands_sequence(tree: &Tree, src: &str) -> Option<Vec<Vec<String>>> {`
- `const` `codex-rs/core/src/bash.rs:36` `const ALLOWED_KINDS: &[&str] = &[`
- `const` `codex-rs/core/src/bash.rs:52` `const ALLOWED_PUNCT_TOKENS: &[&str] = &["&&", "||", ";", "|", "\"", "'"];`
- `fn` `codex-rs/core/src/bash.rs:97` `pub fn extract_bash_command(command: &[String]) -> Option<(&str, &str)> {`
- `fn` `codex-rs/core/src/bash.rs:115` `pub fn parse_shell_lc_plain_commands(command: &[String]) -> Option<Vec<Vec<String>>> {`
- `fn` `codex-rs/core/src/bash.rs:122` `fn parse_plain_command_from_node(cmd: tree_sitter::Node, src: &str) -> Option<Vec<String>> {`
- `fn` `codex-rs/core/src/bash.rs:180` `fn parse_double_quoted_string(node: Node, src: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/bash.rs:198` `fn parse_raw_string(node: Node, src: &str) -> Option<String> {`
- `use` `codex-rs/core/src/bash.rs:212` `use super::*;`
- `use` `codex-rs/core/src/bash.rs:213` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/bash.rs:215` `fn parse_seq(src: &str) -> Option<Vec<Vec<String>>> {`
- `fn` `codex-rs/core/src/bash.rs:221` `fn accepts_single_simple_command() {`
- `fn` `codex-rs/core/src/bash.rs:227` `fn accepts_multiple_commands_with_allowed_operators() {`
- `fn` `codex-rs/core/src/bash.rs:240` `fn extracts_double_and_single_quoted_strings() {`
- `fn` `codex-rs/core/src/bash.rs:255` `fn accepts_double_quoted_strings_with_newlines() {`
- `fn` `codex-rs/core/src/bash.rs:269` `fn accepts_mixed_quote_concatenation() {`
- `fn` `codex-rs/core/src/bash.rs:281` `fn rejects_double_quoted_strings_with_expansions() {`
- `fn` `codex-rs/core/src/bash.rs:287` `fn accepts_numbers_as_words() {`
- `fn` `codex-rs/core/src/bash.rs:300` `fn rejects_parentheses_and_subshells() {`
- `fn` `codex-rs/core/src/bash.rs:306` `fn rejects_redirections_and_unsupported_operators() {`
- `fn` `codex-rs/core/src/bash.rs:312` `fn rejects_command_and_process_substitutions_and_expansions() {`
- `fn` `codex-rs/core/src/bash.rs:320` `fn rejects_variable_assignment_prefix() {`
- `fn` `codex-rs/core/src/bash.rs:325` `fn rejects_trailing_operator_parse_error() {`
- `fn` `codex-rs/core/src/bash.rs:330` `fn parse_zsh_lc_plain_commands() {`
- `fn` `codex-rs/core/src/bash.rs:337` `fn accepts_concatenated_flag_and_value() {`
- `fn` `codex-rs/core/src/bash.rs:352` `fn accepts_concatenated_flag_with_single_quotes() {`
- `fn` `codex-rs/core/src/bash.rs:366` `fn rejects_concatenation_with_variable_substitution() {`
- `fn` `codex-rs/core/src/bash.rs:373` `fn rejects_concatenation_with_command_substitution() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use tree_sitter::Node;`
- `use tree_sitter::Parser;`
- `use tree_sitter::Tree;`
- `use tree_sitter_bash::LANGUAGE as BASH;`
- `use crate::shell::ShellType;`
- `use crate::shell::detect_shell_type;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
