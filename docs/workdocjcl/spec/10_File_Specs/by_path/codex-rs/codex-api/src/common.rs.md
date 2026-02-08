# `codex-rs/codex-api/src/common.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6195`
- sha256: `6172f4f97c5bac7203fbaf79590a6fce8f3b9f8a7ecaa0094d902ee6694301f1`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/codex-api/src/common.rs:9` `use serde::Serialize;`
- `use` `codex-rs/codex-api/src/common.rs:10` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/common.rs:11` `use std::pin::Pin;`
- `use` `codex-rs/codex-api/src/common.rs:12` `use std::task::Context;`
- `use` `codex-rs/codex-api/src/common.rs:13` `use std::task::Poll;`
- `use` `codex-rs/codex-api/src/common.rs:14` `use tokio::sync::mpsc;`
- `struct` `codex-rs/codex-api/src/common.rs:18` `pub struct Prompt {`
- `struct` `codex-rs/codex-api/src/common.rs:34` `pub struct CompactionInput<'a> {`
- `enum` `codex-rs/codex-api/src/common.rs:41` `pub enum ResponseEvent {`
- `struct` `codex-rs/codex-api/src/common.rs:70` `pub struct Reasoning {`
- `enum` `codex-rs/codex-api/src/common.rs:79` `pub enum TextFormatType {`
- `struct` `codex-rs/codex-api/src/common.rs:85` `pub struct TextFormat {`
- `struct` `codex-rs/codex-api/src/common.rs:99` `pub struct TextControls {`
- `enum` `codex-rs/codex-api/src/common.rs:108` `pub enum OpenAiVerbosity {`
- `impl` `codex-rs/codex-api/src/common.rs:115` `impl From<VerbosityConfig> for OpenAiVerbosity {`
- `fn` `codex-rs/codex-api/src/common.rs:116` `fn from(v: VerbosityConfig) -> Self {`
- `struct` `codex-rs/codex-api/src/common.rs:126` `pub struct ResponsesApiRequest<'a> {`
- `struct` `codex-rs/codex-api/src/common.rs:144` `pub struct ResponseCreateWsRequest {`
- `struct` `codex-rs/codex-api/src/common.rs:162` `pub struct ResponseAppendWsRequest {`
- `enum` `codex-rs/codex-api/src/common.rs:168` `pub enum ResponsesWsRequest {`
- `fn` `codex-rs/codex-api/src/common.rs:175` `pub fn create_text_param_for_request(`
- `struct` `codex-rs/codex-api/src/common.rs:194` `pub struct ResponseStream {`
- `impl` `codex-rs/codex-api/src/common.rs:198` `impl Stream for ResponseStream {`
- `type` `codex-rs/codex-api/src/common.rs:199` `type Item = Result<ResponseEvent, ApiError>;`
- `fn` `codex-rs/codex-api/src/common.rs:201` `fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {`

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
