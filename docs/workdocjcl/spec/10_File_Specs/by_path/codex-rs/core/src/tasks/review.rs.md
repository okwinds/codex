# `codex-rs/core/src/tasks/review.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9505`
- sha256: `1d334bb486a8053bd1f6cb651b0d543df325d4daa7097da72f88021d61e2b7ca`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/review.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tasks/review.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/review.rs:3` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/review.rs:4` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/tasks/review.rs:5` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/tasks/review.rs:6` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/tasks/review.rs:7` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tasks/review.rs:8` `use codex_protocol::protocol::AgentMessageContentDeltaEvent;`
- `use` `codex-rs/core/src/tasks/review.rs:9` `use codex_protocol::protocol::AgentMessageDeltaEvent;`
- `use` `codex-rs/core/src/tasks/review.rs:10` `use codex_protocol::protocol::Event;`
- `use` `codex-rs/core/src/tasks/review.rs:11` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/tasks/review.rs:12` `use codex_protocol::protocol::ExitedReviewModeEvent;`
- `use` `codex-rs/core/src/tasks/review.rs:13` `use codex_protocol::protocol::ItemCompletedEvent;`
- `use` `codex-rs/core/src/tasks/review.rs:14` `use codex_protocol::protocol::ReviewOutputEvent;`
- `use` `codex-rs/core/src/tasks/review.rs:15` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tasks/review.rs:17` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tasks/review.rs:18` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/review.rs:19` `use crate::codex_delegate::run_codex_thread_one_shot;`
- `use` `codex-rs/core/src/tasks/review.rs:20` `use crate::config::Constrained;`
- `use` `codex-rs/core/src/tasks/review.rs:21` `use crate::review_format::format_review_findings_block;`
- `use` `codex-rs/core/src/tasks/review.rs:22` `use crate::review_format::render_review_output_text;`
- `use` `codex-rs/core/src/tasks/review.rs:23` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/review.rs:24` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/tasks/review.rs:26` `use super::SessionTask;`
- `use` `codex-rs/core/src/tasks/review.rs:27` `use super::SessionTaskContext;`
- `impl` `codex-rs/core/src/tasks/review.rs:32` `impl ReviewTask {`
- `impl` `codex-rs/core/src/tasks/review.rs:39` `impl SessionTask for ReviewTask {`
- `fn` `codex-rs/core/src/tasks/review.rs:40` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/review.rs:44` `async fn run(`
- `fn` `codex-rs/core/src/tasks/review.rs:75` `async fn abort(&self, session: Arc<SessionTaskContext>, ctx: Arc<TurnContext>) {`
- `fn` `codex-rs/core/src/tasks/review.rs:80` `async fn start_review_conversation(`
- `fn` `codex-rs/core/src/tasks/review.rs:128` `async fn process_review_events(`
- `fn` `codex-rs/core/src/tasks/review.rs:183` `fn parse_review_output_event(text: &str) -> ReviewOutputEvent {`
- `const` `codex-rs/core/src/tasks/review.rs:207` `const REVIEW_USER_MESSAGE_ID: &str = "review_rollout_user";`
- `const` `codex-rs/core/src/tasks/review.rs:208` `const REVIEW_ASSISTANT_MESSAGE_ID: &str = "review_rollout_assistant";`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use async_trait::async_trait;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::AgentMessageContentDeltaEvent;`
- `use codex_protocol::protocol::AgentMessageDeltaEvent;`
- `use codex_protocol::protocol::Event;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::ExitedReviewModeEvent;`
- `use codex_protocol::protocol::ItemCompletedEvent;`
- `use codex_protocol::protocol::ReviewOutputEvent;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::codex_delegate::run_codex_thread_one_shot;`
- `use crate::config::Constrained;`
- `use crate::review_format::format_review_findings_block;`
- `use crate::review_format::render_review_output_text;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
