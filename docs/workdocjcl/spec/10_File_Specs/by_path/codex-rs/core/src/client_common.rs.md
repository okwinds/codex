# `codex-rs/core/src/client_common.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11337`
- sha256: `878fea9635c9339d219ce48b1a6931e818a04b8137f3bad46bd81858b9e4dc96`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/client_common.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Prompt {`
- `pub struct FreeformTool {`
- `pub struct FreeformToolFormat {`
- `pub struct ResponsesApiTool {`
- `pub struct ResponseStream {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/client_common.rs:1` `use crate::client_common::tools::ToolSpec;`
- `use` `codex-rs/core/src/client_common.rs:2` `use crate::config::types::Personality;`
- `use` `codex-rs/core/src/client_common.rs:3` `use crate::error::Result;`
- `use` `codex-rs/core/src/client_common.rs:5` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/client_common.rs:6` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/client_common.rs:7` `use futures::Stream;`
- `use` `codex-rs/core/src/client_common.rs:8` `use serde::Deserialize;`
- `use` `codex-rs/core/src/client_common.rs:9` `use serde_json::Value;`
- `use` `codex-rs/core/src/client_common.rs:10` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/client_common.rs:11` `use std::pin::Pin;`
- `use` `codex-rs/core/src/client_common.rs:12` `use std::task::Context;`
- `use` `codex-rs/core/src/client_common.rs:13` `use std::task::Poll;`
- `use` `codex-rs/core/src/client_common.rs:14` `use tokio::sync::mpsc;`
- `const` `codex-rs/core/src/client_common.rs:17` `pub const REVIEW_PROMPT: &str = include_str!("../review_prompt.md");`
- `const` `codex-rs/core/src/client_common.rs:20` `pub const REVIEW_EXIT_SUCCESS_TMPL: &str = include_str!("../templates/review/exit_success.xml");`
- `const` `codex-rs/core/src/client_common.rs:21` `pub const REVIEW_EXIT_INTERRUPTED_TMPL: &str =`
- `struct` `codex-rs/core/src/client_common.rs:26` `pub struct Prompt {`
- `impl` `codex-rs/core/src/client_common.rs:46` `impl Prompt {`
- `fn` `codex-rs/core/src/client_common.rs:66` `fn reserialize_shell_outputs(items: &mut [ResponseItem]) {`
- `fn` `codex-rs/core/src/client_common.rs:109` `fn is_shell_tool_name(name: &str) -> bool {`
- `struct` `codex-rs/core/src/client_common.rs:114` `struct ExecOutputJson {`
- `struct` `codex-rs/core/src/client_common.rs:120` `struct ExecOutputMetadataJson {`
- `fn` `codex-rs/core/src/client_common.rs:125` `fn parse_structured_shell_output(raw: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/client_common.rs:130` `fn build_structured_output(parsed: &ExecOutputJson) -> String {`
- `fn` `codex-rs/core/src/client_common.rs:150` `fn strip_total_output_header(output: &str) -> Option<(&str, u32)> {`
- `use` `codex-rs/core/src/client_common.rs:159` `use crate::tools::spec::JsonSchema;`
- `use` `codex-rs/core/src/client_common.rs:160` `use serde::Deserialize;`
- `use` `codex-rs/core/src/client_common.rs:161` `use serde::Serialize;`
- `impl` `codex-rs/core/src/client_common.rs:185` `impl ToolSpec {`
- `struct` `codex-rs/core/src/client_common.rs:197` `pub struct FreeformTool {`
- `struct` `codex-rs/core/src/client_common.rs:204` `pub struct FreeformToolFormat {`
- `struct` `codex-rs/core/src/client_common.rs:211` `pub struct ResponsesApiTool {`
- `struct` `codex-rs/core/src/client_common.rs:222` `pub struct ResponseStream {`
- `impl` `codex-rs/core/src/client_common.rs:226` `impl Stream for ResponseStream {`
- `type` `codex-rs/core/src/client_common.rs:227` `type Item = Result<ResponseEvent>;`
- `fn` `codex-rs/core/src/client_common.rs:229` `fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {`
- `use` `codex-rs/core/src/client_common.rs:236` `use codex_api::ResponsesApiRequest;`
- `use` `codex-rs/core/src/client_common.rs:237` `use codex_api::common::OpenAiVerbosity;`
- `use` `codex-rs/core/src/client_common.rs:238` `use codex_api::common::TextControls;`
- `use` `codex-rs/core/src/client_common.rs:239` `use codex_api::create_text_param_for_request;`
- `use` `codex-rs/core/src/client_common.rs:240` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/client_common.rs:242` `use super::*;`
- `fn` `codex-rs/core/src/client_common.rs:245` `fn serializes_text_verbosity_when_set() {`
- `fn` `codex-rs/core/src/client_common.rs:276` `fn serializes_text_schema_with_strict_format() {`
- `fn` `codex-rs/core/src/client_common.rs:322` `fn omits_text_when_not_set() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::client_common::tools::ToolSpec;`
- `use crate::config::types::Personality;`
- `use crate::error::Result;`
- `use codex_protocol::models::BaseInstructions;`
- `use codex_protocol::models::ResponseItem;`
- `use futures::Stream;`
- `use serde::Deserialize;`
- `use serde_json::Value;`
- `use std::collections::HashSet;`
- `use std::pin::Pin;`
- `use std::task::Context;`
- `use std::task::Poll;`
- `use tokio::sync::mpsc;`
- `use crate::tools::spec::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use codex_api::ResponsesApiRequest;`
- `use codex_api::common::OpenAiVerbosity;`
- `use codex_api::common::TextControls;`
- `use codex_api::create_text_param_for_request;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
