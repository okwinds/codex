# `codex-rs/core/src/tools/context.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7376`
- sha256: `0c48672d99d1089a4d5f8213aeb0f06bb7d47416ea917496ad71580d98031fc1`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/context.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ToolInvocation {`
- `pub enum ToolPayload {`
- `pub fn log_payload(&self) -> Cow<'_, str> {`
- `pub enum ToolOutput {`
- `pub fn log_preview(&self) -> String {`
- `pub fn success_for_logging(&self) -> bool {`
- `pub fn into_response(self, call_id: &str, payload: &ToolPayload) -> ResponseInputItem {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/context.rs:1` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/context.rs:2` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/context.rs:3` `use crate::tools::TELEMETRY_PREVIEW_MAX_BYTES;`
- `use` `codex-rs/core/src/tools/context.rs:4` `use crate::tools::TELEMETRY_PREVIEW_MAX_LINES;`
- `use` `codex-rs/core/src/tools/context.rs:5` `use crate::tools::TELEMETRY_PREVIEW_TRUNCATION_NOTICE;`
- `use` `codex-rs/core/src/tools/context.rs:6` `use crate::turn_diff_tracker::TurnDiffTracker;`
- `use` `codex-rs/core/src/tools/context.rs:7` `use codex_protocol::mcp::CallToolResult;`
- `use` `codex-rs/core/src/tools/context.rs:8` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/core/src/tools/context.rs:9` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/tools/context.rs:10` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tools/context.rs:11` `use codex_protocol::models::ShellToolCallParams;`
- `use` `codex-rs/core/src/tools/context.rs:12` `use codex_utils_string::take_bytes_at_char_boundary;`
- `use` `codex-rs/core/src/tools/context.rs:13` `use std::borrow::Cow;`
- `use` `codex-rs/core/src/tools/context.rs:14` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/context.rs:15` `use tokio::sync::Mutex;`
- `type` `codex-rs/core/src/tools/context.rs:17` `pub type SharedTurnDiffTracker = Arc<Mutex<TurnDiffTracker>>;`
- `struct` `codex-rs/core/src/tools/context.rs:20` `pub struct ToolInvocation {`
- `enum` `codex-rs/core/src/tools/context.rs:30` `pub enum ToolPayload {`
- `impl` `codex-rs/core/src/tools/context.rs:47` `impl ToolPayload {`
- `fn` `codex-rs/core/src/tools/context.rs:48` `pub fn log_payload(&self) -> Cow<'_, str> {`
- `enum` `codex-rs/core/src/tools/context.rs:59` `pub enum ToolOutput {`
- `impl` `codex-rs/core/src/tools/context.rs:72` `impl ToolOutput {`
- `fn` `codex-rs/core/src/tools/context.rs:73` `pub fn log_preview(&self) -> String {`
- `fn` `codex-rs/core/src/tools/context.rs:80` `pub fn success_for_logging(&self) -> bool {`
- `fn` `codex-rs/core/src/tools/context.rs:87` `pub fn into_response(self, call_id: &str, payload: &ToolPayload) -> ResponseInputItem {`
- `fn` `codex-rs/core/src/tools/context.rs:118` `fn telemetry_preview(content: &str) -> String {`
- `use` `codex-rs/core/src/tools/context.rs:160` `use super::*;`
- `use` `codex-rs/core/src/tools/context.rs:161` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/tools/context.rs:164` `fn custom_tool_calls_should_roundtrip_as_custom_outputs() {`
- `fn` `codex-rs/core/src/tools/context.rs:185` `fn function_payloads_remain_function_outputs() {`
- `fn` `codex-rs/core/src/tools/context.rs:208` `fn telemetry_preview_returns_original_within_limits() {`
- `fn` `codex-rs/core/src/tools/context.rs:214` `fn telemetry_preview_truncates_by_bytes() {`
- `fn` `codex-rs/core/src/tools/context.rs:226` `fn telemetry_preview_truncates_by_lines() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::tools::TELEMETRY_PREVIEW_MAX_BYTES;`
- `use crate::tools::TELEMETRY_PREVIEW_MAX_LINES;`
- `use crate::tools::TELEMETRY_PREVIEW_TRUNCATION_NOTICE;`
- `use crate::turn_diff_tracker::TurnDiffTracker;`
- `use codex_protocol::mcp::CallToolResult;`
- `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::models::ShellToolCallParams;`
- `use codex_utils_string::take_bytes_at_char_boundary;`
- `use std::borrow::Cow;`
- `use std::sync::Arc;`
- `use tokio::sync::Mutex;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
