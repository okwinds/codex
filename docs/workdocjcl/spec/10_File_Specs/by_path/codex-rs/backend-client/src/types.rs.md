# `codex-rs/backend-client/src/types.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10904`
- sha256: `fb85b3eb58fb2d429aa31e4eba023ce21421f1e6ed570cea80a43a567854a4c9`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/backend-client/src/types.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CodeTaskDetailsResponse {`
- `pub struct Turn {`
- `pub struct TurnItem {`
- `pub enum ContentFragment {`
- `pub struct StructuredContent {`
- `pub struct DiffPayload {`
- `pub struct Worklog {`
- `pub struct WorklogMessage {`
- `pub struct Author {`
- `pub struct WorklogContent {`
- `pub struct TurnError {`
- `pub trait CodeTaskDetailsResponseExt {`
- `pub struct TurnAttemptsSiblingTurnsResponse {`

## Definitions (auto, per-file)
- `use` `codex-rs/backend-client/src/types.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/backend-client/src/types.rs:11` `use serde::de::Deserializer;`
- `use` `codex-rs/backend-client/src/types.rs:12` `use serde_json::Value;`
- `use` `codex-rs/backend-client/src/types.rs:13` `use std::collections::HashMap;`
- `struct` `codex-rs/backend-client/src/types.rs:19` `pub struct CodeTaskDetailsResponse {`
- `struct` `codex-rs/backend-client/src/types.rs:29` `pub struct Turn {`
- `struct` `codex-rs/backend-client/src/types.rs:49` `pub struct TurnItem {`
- `enum` `codex-rs/backend-client/src/types.rs:64` `pub enum ContentFragment {`
- `struct` `codex-rs/backend-client/src/types.rs:70` `pub struct StructuredContent {`
- `struct` `codex-rs/backend-client/src/types.rs:78` `pub struct DiffPayload {`
- `struct` `codex-rs/backend-client/src/types.rs:84` `pub struct Worklog {`
- `struct` `codex-rs/backend-client/src/types.rs:90` `pub struct WorklogMessage {`
- `struct` `codex-rs/backend-client/src/types.rs:98` `pub struct Author {`
- `struct` `codex-rs/backend-client/src/types.rs:104` `pub struct WorklogContent {`
- `struct` `codex-rs/backend-client/src/types.rs:110` `pub struct TurnError {`
- `impl` `codex-rs/backend-client/src/types.rs:117` `impl ContentFragment {`
- `fn` `codex-rs/backend-client/src/types.rs:118` `fn text(&self) -> Option<&str> {`
- `impl` `codex-rs/backend-client/src/types.rs:143` `impl TurnItem {`
- `fn` `codex-rs/backend-client/src/types.rs:144` `fn text_values(&self) -> Vec<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:151` `fn diff_text(&self) -> Option<String> {`
- `impl` `codex-rs/backend-client/src/types.rs:169` `impl Turn {`
- `fn` `codex-rs/backend-client/src/types.rs:170` `fn unified_diff(&self) -> Option<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:174` `fn message_texts(&self) -> Vec<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:193` `fn user_prompt(&self) -> Option<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:218` `fn error_summary(&self) -> Option<String> {`
- `impl` `codex-rs/backend-client/src/types.rs:223` `impl WorklogMessage {`
- `fn` `codex-rs/backend-client/src/types.rs:224` `fn is_assistant(&self) -> bool {`
- `fn` `codex-rs/backend-client/src/types.rs:232` `fn text_values(&self) -> Vec<String> {`
- `impl` `codex-rs/backend-client/src/types.rs:246` `impl TurnError {`
- `fn` `codex-rs/backend-client/src/types.rs:247` `fn summary(&self) -> Option<String> {`
- `trait` `codex-rs/backend-client/src/types.rs:259` `pub trait CodeTaskDetailsResponseExt {`
- `fn` `codex-rs/backend-client/src/types.rs:261` `fn unified_diff(&self) -> Option<String>;`
- `fn` `codex-rs/backend-client/src/types.rs:263` `fn assistant_text_messages(&self) -> Vec<String>;`
- `fn` `codex-rs/backend-client/src/types.rs:265` `fn user_text_prompt(&self) -> Option<String>;`
- `fn` `codex-rs/backend-client/src/types.rs:267` `fn assistant_error_message(&self) -> Option<String>;`
- `impl` `codex-rs/backend-client/src/types.rs:270` `impl CodeTaskDetailsResponseExt for CodeTaskDetailsResponse {`
- `fn` `codex-rs/backend-client/src/types.rs:271` `fn unified_diff(&self) -> Option<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:281` `fn assistant_text_messages(&self) -> Vec<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:295` `fn user_text_prompt(&self) -> Option<String> {`
- `fn` `codex-rs/backend-client/src/types.rs:299` `fn assistant_error_message(&self) -> Option<String> {`
- `struct` `codex-rs/backend-client/src/types.rs:315` `pub struct TurnAttemptsSiblingTurnsResponse {`
- `use` `codex-rs/backend-client/src/types.rs:322` `use super::*;`
- `use` `codex-rs/backend-client/src/types.rs:323` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/backend-client/src/types.rs:325` `fn fixture(name: &str) -> CodeTaskDetailsResponse {`
- `fn` `codex-rs/backend-client/src/types.rs:335` `fn unified_diff_prefers_current_diff_task_turn() {`
- `fn` `codex-rs/backend-client/src/types.rs:342` `fn unified_diff_falls_back_to_pr_output_diff() {`
- `fn` `codex-rs/backend-client/src/types.rs:349` `fn assistant_text_messages_extracts_text_content() {`
- `fn` `codex-rs/backend-client/src/types.rs:356` `fn user_text_prompt_joins_parts_with_spacing() {`
- `fn` `codex-rs/backend-client/src/types.rs:368` `fn assistant_error_message_combines_code_and_message() {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use serde::de::Deserializer;`
- `use serde_json::Value;`
- `use std::collections::HashMap;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
