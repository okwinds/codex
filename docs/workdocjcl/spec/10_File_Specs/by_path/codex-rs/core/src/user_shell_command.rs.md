# `codex-rs/core/src/user_shell_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4436`
- sha256: `96b3cc5239e27486d7ad6f248125d30770867dba53cbdb661d6c2bd775d90f10`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/user_shell_command.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn is_user_shell_command_text(text: &str) -> bool {`
- `pub fn format_user_shell_command_record(`
- `pub fn user_shell_command_record_item(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/user_shell_command.rs:1` `use std::time::Duration;`
- `use` `codex-rs/core/src/user_shell_command.rs:3` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/user_shell_command.rs:4` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/user_shell_command.rs:6` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/user_shell_command.rs:7` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/user_shell_command.rs:8` `use crate::tools::format_exec_output_str;`
- `const` `codex-rs/core/src/user_shell_command.rs:10` `pub const USER_SHELL_COMMAND_OPEN: &str = "<user_shell_command>";`
- `const` `codex-rs/core/src/user_shell_command.rs:11` `pub const USER_SHELL_COMMAND_CLOSE: &str = "</user_shell_command>";`
- `fn` `codex-rs/core/src/user_shell_command.rs:13` `pub fn is_user_shell_command_text(text: &str) -> bool {`
- `fn` `codex-rs/core/src/user_shell_command.rs:19` `fn format_duration_line(duration: Duration) -> String {`
- `fn` `codex-rs/core/src/user_shell_command.rs:24` `fn format_user_shell_command_body(`
- `fn` `codex-rs/core/src/user_shell_command.rs:45` `pub fn format_user_shell_command_record(`
- `fn` `codex-rs/core/src/user_shell_command.rs:54` `pub fn user_shell_command_record_item(`
- `use` `codex-rs/core/src/user_shell_command.rs:72` `use super::*;`
- `use` `codex-rs/core/src/user_shell_command.rs:73` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/user_shell_command.rs:74` `use crate::exec::StreamOutput;`
- `use` `codex-rs/core/src/user_shell_command.rs:75` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/user_shell_command.rs:78` `fn detects_user_shell_command_text_variants() {`
- `fn` `codex-rs/core/src/user_shell_command.rs:86` `async fn formats_basic_record() {`
- `fn` `codex-rs/core/src/user_shell_command.rs:110` `async fn uses_aggregated_output_over_streams() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use crate::codex::TurnContext;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::tools::format_exec_output_str;`
- `use super::*;`
- `use crate::codex::make_session_and_context;`
- `use crate::exec::StreamOutput;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
