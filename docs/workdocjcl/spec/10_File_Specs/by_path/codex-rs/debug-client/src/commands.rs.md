# `codex-rs/debug-client/src/commands.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4230`
- sha256: `0303a0b35e34929d242ec6e45fee497e942a2e7ad603803a1bdde8f95045ae9c`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/debug-client/src/commands.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum InputAction {`
- `pub enum UserCommand {`
- `pub enum ParseError {`
- `pub fn message(&self) -> String {`
- `pub fn parse_input(line: &str) -> Result<Option<InputAction>, ParseError> {`

## Definitions (auto, per-file)
- `enum` `codex-rs/debug-client/src/commands.rs:2` `pub enum InputAction {`
- `enum` `codex-rs/debug-client/src/commands.rs:8` `pub enum UserCommand {`
- `enum` `codex-rs/debug-client/src/commands.rs:18` `pub enum ParseError {`
- `impl` `codex-rs/debug-client/src/commands.rs:24` `impl ParseError {`
- `fn` `codex-rs/debug-client/src/commands.rs:25` `pub fn message(&self) -> String {`
- `fn` `codex-rs/debug-client/src/commands.rs:36` `pub fn parse_input(line: &str) -> Result<Option<InputAction>, ParseError> {`
- `use` `codex-rs/debug-client/src/commands.rs:80` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/debug-client/src/commands.rs:82` `use super::InputAction;`
- `use` `codex-rs/debug-client/src/commands.rs:83` `use super::ParseError;`
- `use` `codex-rs/debug-client/src/commands.rs:84` `use super::UserCommand;`
- `use` `codex-rs/debug-client/src/commands.rs:85` `use super::parse_input;`
- `fn` `codex-rs/debug-client/src/commands.rs:88` `fn parses_message() {`
- `fn` `codex-rs/debug-client/src/commands.rs:97` `fn parses_help_command() {`
- `fn` `codex-rs/debug-client/src/commands.rs:103` `fn parses_new_thread() {`
- `fn` `codex-rs/debug-client/src/commands.rs:109` `fn parses_resume() {`
- `fn` `codex-rs/debug-client/src/commands.rs:120` `fn parses_use() {`
- `fn` `codex-rs/debug-client/src/commands.rs:131` `fn parses_refresh_thread() {`
- `fn` `codex-rs/debug-client/src/commands.rs:140` `fn rejects_missing_resume_arg() {`
- `fn` `codex-rs/debug-client/src/commands.rs:149` `fn rejects_missing_use_arg() {`

## Dependencies (auto sample)
### Imports / Includes
- `use pretty_assertions::assert_eq;`
- `use super::InputAction;`
- `use super::ParseError;`
- `use super::UserCommand;`
- `use super::parse_input;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
