# `codex-rs/core/src/rollout/truncation.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8155`
- sha256: `926131e4b11d883a47c9a492af363c7a57416011ef738d83f774c52afc894953`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/truncation.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/truncation.rs:6` `use crate::event_mapping;`
- `use` `codex-rs/core/src/rollout/truncation.rs:7` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/rollout/truncation.rs:8` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/rollout/truncation.rs:9` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/rollout/truncation.rs:10` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/truncation.rs:73` `use super::*;`
- `use` `codex-rs/core/src/rollout/truncation.rs:74` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/rollout/truncation.rs:75` `use assert_matches::assert_matches;`
- `use` `codex-rs/core/src/rollout/truncation.rs:76` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/rollout/truncation.rs:77` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/rollout/truncation.rs:78` `use codex_protocol::protocol::ThreadRolledBackEvent;`
- `use` `codex-rs/core/src/rollout/truncation.rs:79` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/rollout/truncation.rs:81` `fn user_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/rollout/truncation.rs:93` `fn assistant_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/rollout/truncation.rs:106` `fn truncates_rollout_from_start_before_nth_user_only() {`
- `fn` `codex-rs/core/src/rollout/truncation.rs:152` `fn truncation_max_keeps_full_rollout() {`
- `fn` `codex-rs/core/src/rollout/truncation.rs:168` `fn truncates_rollout_from_start_applies_thread_rollback_markers() {`
- `fn` `codex-rs/core/src/rollout/truncation.rs:194` `async fn ignores_session_prefix_messages_when_truncating_rollout_from_start() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::event_mapping;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use super::*;`
- `use crate::codex::make_session_and_context;`
- `use assert_matches::assert_matches;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use codex_protocol::protocol::ThreadRolledBackEvent;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
