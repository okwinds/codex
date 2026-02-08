# `codex-rs/app-server-protocol/src/protocol/thread_history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19158`
- sha256: `221bcc3bc61e9124f405cc9eb0e64dcc0ecb50571e01f4b89e6dfb3036b29d6a`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/protocol/thread_history.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn build_turns_from_event_msgs(events: &[EventMsg]) -> Vec<Turn> {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:1` `use crate::protocol::v2::ThreadItem;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:2` `use crate::protocol::v2::Turn;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:3` `use crate::protocol::v2::TurnError;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:4` `use crate::protocol::v2::TurnStatus;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:5` `use crate::protocol::v2::UserInput;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:6` `use codex_protocol::protocol::AgentReasoningEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:7` `use codex_protocol::protocol::AgentReasoningRawContentEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:8` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:9` `use codex_protocol::protocol::ItemCompletedEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:10` `use codex_protocol::protocol::ThreadRolledBackEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:11` `use codex_protocol::protocol::TurnAbortedEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:12` `use codex_protocol::protocol::UserMessageEvent;`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:19` `pub fn build_turns_from_event_msgs(events: &[EventMsg]) -> Vec<Turn> {`
- `struct` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:27` `struct ThreadHistoryBuilder {`
- `impl` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:34` `impl ThreadHistoryBuilder {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:35` `fn new() -> Self {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:44` `fn finish(mut self) -> Vec<Turn> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:51` `fn handle_event(&mut self, event: &EventMsg) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:70` `fn handle_user_message(&mut self, payload: &UserMessageEvent) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:79` `fn handle_agent_message(&mut self, text: String) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:90` `fn handle_agent_reasoning(&mut self, payload: &AgentReasoningEvent) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:110` `fn handle_agent_reasoning_raw_content(&mut self, payload: &AgentReasoningRawContentEvent) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:130` `fn handle_item_completed(&mut self, payload: &ItemCompletedEvent) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:143` `fn handle_turn_aborted(&mut self, _payload: &TurnAbortedEvent) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:150` `fn handle_thread_rollback(&mut self, payload: &ThreadRolledBackEvent) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:167` `fn finish_current_turn(&mut self) {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:176` `fn new_turn(&mut self) -> PendingTurn {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:185` `fn ensure_turn(&mut self) -> &mut PendingTurn {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:198` `fn next_turn_id(&mut self) -> String {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:204` `fn next_item_id(&mut self) -> String {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:210` `fn build_user_inputs(&self, payload: &UserMessageEvent) -> Vec<UserInput> {`
- `struct` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:235` `struct PendingTurn {`
- `impl` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:242` `impl From<PendingTurn> for Turn {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:243` `fn from(value: PendingTurn) -> Self {`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:255` `use super::*;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:256` `use codex_protocol::protocol::AgentMessageEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:257` `use codex_protocol::protocol::AgentReasoningEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:258` `use codex_protocol::protocol::AgentReasoningRawContentEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:259` `use codex_protocol::protocol::ThreadRolledBackEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:260` `use codex_protocol::protocol::TurnAbortReason;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:261` `use codex_protocol::protocol::TurnAbortedEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:262` `use codex_protocol::protocol::UserMessageEvent;`
- `use` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:263` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:266` `fn builds_multiple_turns_with_reasoning_items() {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:355` `fn splits_reasoning_when_interleaved() {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:401` `fn marks_turn_as_interrupted_when_aborted() {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:473` `fn drops_last_turns_on_thread_rollback() {`
- `fn` `codex-rs/app-server-protocol/src/protocol/thread_history.rs:548` `fn thread_rollback_clears_all_turns_when_num_turns_exceeds_history() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::protocol::v2::ThreadItem;`
- `use crate::protocol::v2::Turn;`
- `use crate::protocol::v2::TurnError;`
- `use crate::protocol::v2::TurnStatus;`
- `use crate::protocol::v2::UserInput;`
- `use codex_protocol::protocol::AgentReasoningEvent;`
- `use codex_protocol::protocol::AgentReasoningRawContentEvent;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::ItemCompletedEvent;`
- `use codex_protocol::protocol::ThreadRolledBackEvent;`
- `use codex_protocol::protocol::TurnAbortedEvent;`
- `use codex_protocol::protocol::UserMessageEvent;`
- `use super::*;`
- `use codex_protocol::protocol::AgentMessageEvent;`
- `use codex_protocol::protocol::AgentReasoningEvent;`
- `use codex_protocol::protocol::AgentReasoningRawContentEvent;`
- `use codex_protocol::protocol::ThreadRolledBackEvent;`
- `use codex_protocol::protocol::TurnAbortReason;`
- `use codex_protocol::protocol::TurnAbortedEvent;`
- `use codex_protocol::protocol::UserMessageEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
