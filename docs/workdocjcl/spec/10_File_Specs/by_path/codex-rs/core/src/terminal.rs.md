# `codex-rs/core/src/terminal.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `38350`
- sha256: `898b23396bbf4e8cbc63ea82e5c5b5b7f888981917cc022d7341387522708e6b`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/terminal.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct TerminalInfo {`
- `pub enum TerminalName {`
- `pub enum Multiplexer {`
- `pub fn user_agent() -> String {`
- `pub fn terminal_info() -> TerminalInfo {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/terminal.rs:6` `use std::sync::OnceLock;`
- `struct` `codex-rs/core/src/terminal.rs:10` `pub struct TerminalInfo {`
- `enum` `codex-rs/core/src/terminal.rs:25` `pub enum TerminalName {`
- `enum` `codex-rs/core/src/terminal.rs:58` `pub enum Multiplexer {`
- `struct` `codex-rs/core/src/terminal.rs:81` `struct TmuxClientInfo {`
- `impl` `codex-rs/core/src/terminal.rs:86` `impl TerminalInfo {`
- `fn` `codex-rs/core/src/terminal.rs:88` `fn new(`
- `fn` `codex-rs/core/src/terminal.rs:105` `fn from_term_program(`
- `fn` `codex-rs/core/src/terminal.rs:115` `fn from_term_program_and_term(`
- `fn` `codex-rs/core/src/terminal.rs:126` `fn from_name(`
- `fn` `codex-rs/core/src/terminal.rs:135` `fn from_term(term: String, multiplexer: Option<Multiplexer>) -> Self {`
- `fn` `codex-rs/core/src/terminal.rs:145` `fn unknown(multiplexer: Option<Multiplexer>) -> Self {`
- `fn` `codex-rs/core/src/terminal.rs:150` `fn user_agent_token(&self) -> String {`
- `static` `codex-rs/core/src/terminal.rs:185` `static TERMINAL_INFO: OnceLock<TerminalInfo> = OnceLock::new();`
- `trait` `codex-rs/core/src/terminal.rs:190` `trait Environment {`
- `fn` `codex-rs/core/src/terminal.rs:192` `fn var(&self, name: &str) -> Option<String>;`
- `fn` `codex-rs/core/src/terminal.rs:195` `fn has(&self, name: &str) -> bool {`
- `fn` `codex-rs/core/src/terminal.rs:200` `fn var_non_empty(&self, name: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/terminal.rs:205` `fn has_non_empty(&self, name: &str) -> bool {`
- `fn` `codex-rs/core/src/terminal.rs:210` `fn tmux_client_info(&self) -> TmuxClientInfo;`
- `struct` `codex-rs/core/src/terminal.rs:214` `struct ProcessEnvironment;`
- `impl` `codex-rs/core/src/terminal.rs:216` `impl Environment for ProcessEnvironment {`
- `fn` `codex-rs/core/src/terminal.rs:217` `fn var(&self, name: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/terminal.rs:228` `fn tmux_client_info(&self) -> TmuxClientInfo {`
- `fn` `codex-rs/core/src/terminal.rs:234` `pub fn user_agent() -> String {`
- `fn` `codex-rs/core/src/terminal.rs:239` `pub fn terminal_info() -> TerminalInfo {`
- `fn` `codex-rs/core/src/terminal.rs:258` `fn detect_terminal_info_from_env(env: &dyn Environment) -> TerminalInfo {`
- `fn` `codex-rs/core/src/terminal.rs:331` `fn detect_multiplexer(env: &dyn Environment) -> Option<Multiplexer> {`
- `fn` `codex-rs/core/src/terminal.rs:348` `fn is_tmux_term_program(value: &str) -> bool {`
- `fn` `codex-rs/core/src/terminal.rs:352` `fn terminal_from_tmux_client_info(`
- `fn` `codex-rs/core/src/terminal.rs:376` `fn tmux_version_from_env(env: &dyn Environment) -> Option<String> {`
- `fn` `codex-rs/core/src/terminal.rs:385` `fn split_term_program_and_version(value: &str) -> (String, Option<String>) {`
- `fn` `codex-rs/core/src/terminal.rs:392` `fn tmux_client_info() -> TmuxClientInfo {`
- `fn` `codex-rs/core/src/terminal.rs:399` `fn tmux_display_message(format: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/terminal.rs:416` `fn sanitize_header_value(value: String) -> String {`
- `fn` `codex-rs/core/src/terminal.rs:421` `fn is_valid_header_value_char(c: char) -> bool {`
- `fn` `codex-rs/core/src/terminal.rs:425` `fn terminal_name_from_term_program(value: &str) -> Option<TerminalName> {`
- `fn` `codex-rs/core/src/terminal.rs:451` `fn format_terminal_version(name: &str, version: &Option<String>) -> String {`
- `fn` `codex-rs/core/src/terminal.rs:458` `fn none_if_whitespace(value: String) -> Option<String> {`
- `use` `codex-rs/core/src/terminal.rs:464` `use super::*;`
- `use` `codex-rs/core/src/terminal.rs:465` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/terminal.rs:466` `use std::collections::HashMap;`
- `struct` `codex-rs/core/src/terminal.rs:468` `struct FakeEnvironment {`
- `impl` `codex-rs/core/src/terminal.rs:473` `impl FakeEnvironment {`
- `fn` `codex-rs/core/src/terminal.rs:474` `fn new() -> Self {`
- `fn` `codex-rs/core/src/terminal.rs:481` `fn with_var(mut self, key: &str, value: &str) -> Self {`
- `fn` `codex-rs/core/src/terminal.rs:486` `fn with_tmux_client_info(mut self, termtype: Option<&str>, termname: Option<&str>) -> Self {`
- `impl` `codex-rs/core/src/terminal.rs:495` `impl Environment for FakeEnvironment {`
- `fn` `codex-rs/core/src/terminal.rs:496` `fn var(&self, name: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/terminal.rs:500` `fn tmux_client_info(&self) -> TmuxClientInfo {`
- `fn` `codex-rs/core/src/terminal.rs:505` `fn terminal_info(`
- `fn` `codex-rs/core/src/terminal.rs:522` `fn detects_term_program() {`
- `fn` `codex-rs/core/src/terminal.rs:577` `fn detects_iterm2() {`
- `fn` `codex-rs/core/src/terminal.rs:593` `fn detects_apple_terminal() {`
- `fn` `codex-rs/core/src/terminal.rs:628` `fn detects_ghostty() {`
- `fn` `codex-rs/core/src/terminal.rs:644` `fn detects_vscode() {`
- `fn` `codex-rs/core/src/terminal.rs:668` `fn detects_warp_terminal() {`
- `fn` `codex-rs/core/src/terminal.rs:692` `fn detects_tmux_multiplexer() {`
- `fn` `codex-rs/core/src/terminal.rs:717` `fn detects_zellij_multiplexer() {`
- `fn` `codex-rs/core/src/terminal.rs:734` `fn detects_tmux_client_termtype() {`
- `fn` `codex-rs/core/src/terminal.rs:759` `fn detects_tmux_client_termname() {`
- `fn` `codex-rs/core/src/terminal.rs:784` `fn detects_tmux_term_program_uses_client_termtype() {`
- `fn` `codex-rs/core/src/terminal.rs:812` `fn detects_wezterm() {`
- `fn` `codex-rs/core/src/terminal.rs:862` `fn detects_kitty() {`
- `fn` `codex-rs/core/src/terminal.rs:914` `fn detects_alacritty() {`
- `fn` `codex-rs/core/src/terminal.rs:964` `fn detects_konsole() {`
- `fn` `codex-rs/core/src/terminal.rs:1014` `fn detects_gnome_terminal() {`
- `fn` `codex-rs/core/src/terminal.rs:1051` `fn detects_vte() {`
- `fn` `codex-rs/core/src/terminal.rs:1091` `fn detects_windows_terminal() {`
- `fn` `codex-rs/core/src/terminal.rs:1128` `fn detects_term_fallbacks() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::OnceLock;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
