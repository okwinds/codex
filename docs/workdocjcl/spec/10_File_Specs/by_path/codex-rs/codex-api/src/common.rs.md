# `codex-rs/codex-api/src/common.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7010`
- sha256: `c9543b23591501bb0509311cae3486c6d9a4f7343af1cc8cd5e2466d362ccecb`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/common.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Prompt {`
- `pub struct CompactionInput<'a> {`
- `pub struct MemoryTraceSummarizeInput {`
- `pub struct MemoryTrace {`
- `pub struct MemoryTraceMetadata {`
- `pub struct MemoryTraceSummaryOutput {`
- `pub enum ResponseEvent {`
- `pub struct Reasoning {`
- `pub enum TextFormatType {`
- `pub struct TextFormat {`
- `pub struct TextControls {`
- `pub enum OpenAiVerbosity {`
- `pub struct ResponsesApiRequest<'a> {`
- `pub struct ResponseCreateWsRequest {`
- `pub struct ResponseAppendWsRequest {`
- `pub enum ResponsesWsRequest {`
- `pub fn create_text_param_for_request(`
- `pub struct ResponseStream {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/common.rs:1` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/common.rs:2` `use codex_protocol::config_types::ReasoningSummary as ReasoningSummaryConfig;`
- `use` `codex-rs/codex-api/src/common.rs:3` `use codex_protocol::config_types::Verbosity as VerbosityConfig;`
- `use` `codex-rs/codex-api/src/common.rs:4` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/common.rs:5` `use codex_protocol::openai_models::ReasoningEffort as ReasoningEffortConfig;`
- `use` `codex-rs/codex-api/src/common.rs:6` `use codex_protocol::protocol::RateLimitSnapshot;`
- `use` `codex-rs/codex-api/src/common.rs:7` `use codex_protocol::protocol::TokenUsage;`
- `use` `codex-rs/codex-api/src/common.rs:8` `use futures::Stream;`
- `use` `codex-rs/codex-api/src/common.rs:9` `use serde::Deserialize;`
- `use` `codex-rs/codex-api/src/common.rs:10` `use serde::Serialize;`
- `use` `codex-rs/codex-api/src/common.rs:11` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/common.rs:12` `use std::pin::Pin;`
- `use` `codex-rs/codex-api/src/common.rs:13` `use std::task::Context;`
- `use` `codex-rs/codex-api/src/common.rs:14` `use std::task::Poll;`
- `use` `codex-rs/codex-api/src/common.rs:15` `use tokio::sync::mpsc;`
- `struct` `codex-rs/codex-api/src/common.rs:19` `pub struct Prompt {`
- `struct` `codex-rs/codex-api/src/common.rs:35` `pub struct CompactionInput<'a> {`
- `struct` `codex-rs/codex-api/src/common.rs:43` `pub struct MemoryTraceSummarizeInput {`
- `struct` `codex-rs/codex-api/src/common.rs:51` `pub struct MemoryTrace {`
- `struct` `codex-rs/codex-api/src/common.rs:58` `pub struct MemoryTraceMetadata {`
- `struct` `codex-rs/codex-api/src/common.rs:63` `pub struct MemoryTraceSummaryOutput {`
- `enum` `codex-rs/codex-api/src/common.rs:69` `pub enum ResponseEvent {`
- `struct` `codex-rs/codex-api/src/common.rs:98` `pub struct Reasoning {`
- `enum` `codex-rs/codex-api/src/common.rs:107` `pub enum TextFormatType {`
- `struct` `codex-rs/codex-api/src/common.rs:113` `pub struct TextFormat {`
- `struct` `codex-rs/codex-api/src/common.rs:127` `pub struct TextControls {`
- `enum` `codex-rs/codex-api/src/common.rs:136` `pub enum OpenAiVerbosity {`
- `impl` `codex-rs/codex-api/src/common.rs:143` `impl From<VerbosityConfig> for OpenAiVerbosity {`
- `fn` `codex-rs/codex-api/src/common.rs:144` `fn from(v: VerbosityConfig) -> Self {`
- `struct` `codex-rs/codex-api/src/common.rs:154` `pub struct ResponsesApiRequest<'a> {`
- `struct` `codex-rs/codex-api/src/common.rs:172` `pub struct ResponseCreateWsRequest {`
- `struct` `codex-rs/codex-api/src/common.rs:192` `pub struct ResponseAppendWsRequest {`
- `enum` `codex-rs/codex-api/src/common.rs:198` `pub enum ResponsesWsRequest {`
- `fn` `codex-rs/codex-api/src/common.rs:205` `pub fn create_text_param_for_request(`
- `struct` `codex-rs/codex-api/src/common.rs:224` `pub struct ResponseStream {`
- `impl` `codex-rs/codex-api/src/common.rs:228` `impl Stream for ResponseStream {`
- `type` `codex-rs/codex-api/src/common.rs:229` `type Item = Result<ResponseEvent, ApiError>;`
- `fn` `codex-rs/codex-api/src/common.rs:231` `fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::ApiError;`
- `use codex_protocol::config_types::ReasoningSummary as ReasoningSummaryConfig;`
- `use codex_protocol::config_types::Verbosity as VerbosityConfig;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::openai_models::ReasoningEffort as ReasoningEffortConfig;`
- `use codex_protocol::protocol::RateLimitSnapshot;`
- `use codex_protocol::protocol::TokenUsage;`
- `use futures::Stream;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use std::pin::Pin;`
- `use std::task::Context;`
- `use std::task::Poll;`
- `use tokio::sync::mpsc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
