# `codex-rs/codex-api/src/sse/chat.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `25842`
- sha256: `dc0fdb1e96951ef8d7cf785170f027cc66484d563fe72d6add96d6bfb6efe029`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/sse/chat.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/sse/chat.rs:1` `use crate::common::ResponseEvent;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:2` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:3` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:4` `use crate::telemetry::SseTelemetry;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:5` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:6` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:7` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:8` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:9` `use eventsource_stream::Eventsource;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:10` `use futures::Stream;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:11` `use futures::StreamExt;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:12` `use std::collections::HashMap;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:13` `use std::collections::HashSet;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:14` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:15` `use std::sync::OnceLock;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:16` `use std::time::Duration;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:17` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:18` `use tokio::time::Instant;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:19` `use tokio::time::timeout;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:20` `use tracing::debug;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:21` `use tracing::trace;`
- `struct` `codex-rs/codex-api/src/sse/chat.rs:62` `struct ToolCallState {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:78` `async fn flush_and_complete(`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:323` `async fn append_assistant_text(`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:350` `async fn append_reasoning_text(`
- `use` `codex-rs/codex-api/src/sse/chat.rs:387` `use super::*;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:388` `use assert_matches::assert_matches;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:389` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:390` `use futures::TryStreamExt;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:391` `use serde_json::json;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:392` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-api/src/sse/chat.rs:393` `use tokio_util::io::ReaderStream;`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:395` `fn build_body(events: &[serde_json::Value]) -> String {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:408` `async fn completes_on_done_sentinel_without_json() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:413` `async fn collect_events(body: &str) -> Vec<ResponseEvent> {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:432` `async fn concatenates_tool_call_arguments_across_deltas() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:485` `async fn emits_multiple_tool_calls() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:527` `async fn emits_tool_calls_for_multiple_choices() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:566` `async fn merges_tool_calls_by_index_when_id_missing_on_subsequent_deltas() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:608` `async fn preserves_tool_call_name_when_empty_deltas_arrive() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:649` `async fn emits_tool_calls_even_when_content_and_reasoning_present() {`
- `fn` `codex-rs/codex-api/src/sse/chat.rs:688` `async fn drops_partial_tool_calls_on_stop_finish_reason() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::common::ResponseEvent;`
- `use crate::common::ResponseStream;`
- `use crate::error::ApiError;`
- `use crate::telemetry::SseTelemetry;`
- `use codex_client::StreamResponse;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::models::ResponseItem;`
- `use eventsource_stream::Eventsource;`
- `use futures::Stream;`
- `use futures::StreamExt;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::sync::Arc;`
- `use std::sync::OnceLock;`
- `use std::time::Duration;`
- `use tokio::sync::mpsc;`
- `use tokio::time::Instant;`
- `use tokio::time::timeout;`
- `use tracing::debug;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
