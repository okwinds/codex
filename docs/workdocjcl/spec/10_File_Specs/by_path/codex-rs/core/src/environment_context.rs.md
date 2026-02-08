# `codex-rs/core/src/environment_context.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6526`
- sha256: `5c244dfcabea7354bbd388ba9e8432e0cbbd16698ded9d67e84dbe12c18880c3`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/environment_context.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new(cwd: Option<PathBuf>, shell: Shell) -> Self {`
- `pub fn equals_except_shell(&self, other: &EnvironmentContext) -> bool {`
- `pub fn diff(before: &TurnContext, after: &TurnContext, shell: &Shell) -> Self {`
- `pub fn from_turn_context(turn_context: &TurnContext, shell: &Shell) -> Self {`
- `pub fn serialize_to_xml(self) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/environment_context.rs:1` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/environment_context.rs:2` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/environment_context.rs:3` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/environment_context.rs:4` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/environment_context.rs:5` `use codex_protocol::protocol::ENVIRONMENT_CONTEXT_CLOSE_TAG;`
- `use` `codex-rs/core/src/environment_context.rs:6` `use codex_protocol::protocol::ENVIRONMENT_CONTEXT_OPEN_TAG;`
- `use` `codex-rs/core/src/environment_context.rs:7` `use serde::Deserialize;`
- `use` `codex-rs/core/src/environment_context.rs:8` `use serde::Serialize;`
- `use` `codex-rs/core/src/environment_context.rs:9` `use std::path::PathBuf;`
- `impl` `codex-rs/core/src/environment_context.rs:18` `impl EnvironmentContext {`
- `fn` `codex-rs/core/src/environment_context.rs:19` `pub fn new(cwd: Option<PathBuf>, shell: Shell) -> Self {`
- `fn` `codex-rs/core/src/environment_context.rs:26` `pub fn equals_except_shell(&self, other: &EnvironmentContext) -> bool {`
- `fn` `codex-rs/core/src/environment_context.rs:37` `pub fn diff(before: &TurnContext, after: &TurnContext, shell: &Shell) -> Self {`
- `fn` `codex-rs/core/src/environment_context.rs:46` `pub fn from_turn_context(turn_context: &TurnContext, shell: &Shell) -> Self {`
- `impl` `codex-rs/core/src/environment_context.rs:51` `impl EnvironmentContext {`
- `fn` `codex-rs/core/src/environment_context.rs:62` `pub fn serialize_to_xml(self) -> String {`
- `impl` `codex-rs/core/src/environment_context.rs:75` `impl From<EnvironmentContext> for ResponseItem {`
- `fn` `codex-rs/core/src/environment_context.rs:76` `fn from(ec: EnvironmentContext) -> Self {`
- `use` `codex-rs/core/src/environment_context.rs:91` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/environment_context.rs:93` `use super::*;`
- `use` `codex-rs/core/src/environment_context.rs:94` `use core_test_support::test_path_buf;`
- `use` `codex-rs/core/src/environment_context.rs:95` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/environment_context.rs:97` `fn fake_shell() -> Shell {`
- `fn` `codex-rs/core/src/environment_context.rs:106` `fn serialize_workspace_write_environment_context() {`
- `fn` `codex-rs/core/src/environment_context.rs:122` `fn serialize_read_only_environment_context() {`
- `fn` `codex-rs/core/src/environment_context.rs:133` `fn serialize_external_sandbox_environment_context() {`
- `fn` `codex-rs/core/src/environment_context.rs:144` `fn serialize_external_sandbox_with_restricted_network_environment_context() {`
- `fn` `codex-rs/core/src/environment_context.rs:155` `fn serialize_full_access_environment_context() {`
- `fn` `codex-rs/core/src/environment_context.rs:166` `fn equals_except_shell_compares_cwd() {`
- `fn` `codex-rs/core/src/environment_context.rs:173` `fn equals_except_shell_ignores_sandbox_policy() {`
- `fn` `codex-rs/core/src/environment_context.rs:181` `fn equals_except_shell_compares_cwd_differences() {`
- `fn` `codex-rs/core/src/environment_context.rs:189` `fn equals_except_shell_ignores_shell() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::TurnContext;`
- `use crate::shell::Shell;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::ENVIRONMENT_CONTEXT_CLOSE_TAG;`
- `use codex_protocol::protocol::ENVIRONMENT_CONTEXT_OPEN_TAG;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::path::PathBuf;`
- `use crate::shell::ShellType;`
- `use super::*;`
- `use core_test_support::test_path_buf;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
