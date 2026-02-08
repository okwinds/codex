# `codex-rs/exec/src/exec_events.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10133`
- sha256: `2a53405ad178ecfd2ce9a3e4997a92c7584d0c1a719e01394b37090e84196583`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/exec_events.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ThreadEvent {`
- `pub struct ThreadStartedEvent {`
- `pub struct TurnStartedEvent {}`
- `pub struct TurnCompletedEvent {`
- `pub struct TurnFailedEvent {`
- `pub struct Usage {`
- `pub struct ItemStartedEvent {`
- `pub struct ItemCompletedEvent {`
- `pub struct ItemUpdatedEvent {`
- `pub struct ThreadErrorEvent {`
- `pub struct ThreadItem {`
- `pub enum ThreadItemDetails {`
- `pub struct AgentMessageItem {`
- `pub struct ReasoningItem {`
- `pub enum CommandExecutionStatus {`
- `pub struct CommandExecutionItem {`
- `pub struct FileUpdateChange {`
- `pub enum PatchApplyStatus {`
- `pub struct FileChangeItem {`
- `pub enum PatchChangeKind {`
- `pub enum McpToolCallStatus {`
- `pub enum CollabToolCallStatus {`
- `pub enum CollabTool {`
- `pub enum CollabAgentStatus {`
- `pub struct CollabAgentState {`
- `pub struct CollabToolCallItem {`
- `pub struct McpToolCallItemResult {`
- `pub struct McpToolCallItemError {`
- `pub struct McpToolCallItem {`
- `pub struct WebSearchItem {`
- `pub struct ErrorItem {`
- `pub struct TodoItem {`
- `pub struct TodoListItem {`

## Definitions (auto, per-file)
- `use` `codex-rs/exec/src/exec_events.rs:1` `use codex_protocol::models::WebSearchAction;`
- `use` `codex-rs/exec/src/exec_events.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/exec/src/exec_events.rs:3` `use serde::Serialize;`
- `use` `codex-rs/exec/src/exec_events.rs:4` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/exec/src/exec_events.rs:5` `use std::collections::HashMap;`
- `use` `codex-rs/exec/src/exec_events.rs:6` `use ts_rs::TS;`
- `enum` `codex-rs/exec/src/exec_events.rs:11` `pub enum ThreadEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:40` `pub struct ThreadStartedEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:47` `pub struct TurnStartedEvent {}`
- `struct` `codex-rs/exec/src/exec_events.rs:50` `pub struct TurnCompletedEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:55` `pub struct TurnFailedEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:61` `pub struct Usage {`
- `struct` `codex-rs/exec/src/exec_events.rs:71` `pub struct ItemStartedEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:76` `pub struct ItemCompletedEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:81` `pub struct ItemUpdatedEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:87` `pub struct ThreadErrorEvent {`
- `struct` `codex-rs/exec/src/exec_events.rs:93` `pub struct ThreadItem {`
- `enum` `codex-rs/exec/src/exec_events.rs:102` `pub enum ThreadItemDetails {`
- `struct` `codex-rs/exec/src/exec_events.rs:133` `pub struct AgentMessageItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:139` `pub struct ReasoningItem {`
- `enum` `codex-rs/exec/src/exec_events.rs:146` `pub enum CommandExecutionStatus {`
- `struct` `codex-rs/exec/src/exec_events.rs:156` `pub struct CommandExecutionItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:165` `pub struct FileUpdateChange {`
- `enum` `codex-rs/exec/src/exec_events.rs:173` `pub enum PatchApplyStatus {`
- `struct` `codex-rs/exec/src/exec_events.rs:181` `pub struct FileChangeItem {`
- `enum` `codex-rs/exec/src/exec_events.rs:189` `pub enum PatchChangeKind {`
- `enum` `codex-rs/exec/src/exec_events.rs:198` `pub enum McpToolCallStatus {`
- `enum` `codex-rs/exec/src/exec_events.rs:208` `pub enum CollabToolCallStatus {`
- `enum` `codex-rs/exec/src/exec_events.rs:218` `pub enum CollabTool {`
- `enum` `codex-rs/exec/src/exec_events.rs:228` `pub enum CollabAgentStatus {`
- `struct` `codex-rs/exec/src/exec_events.rs:239` `pub struct CollabAgentState {`
- `struct` `codex-rs/exec/src/exec_events.rs:246` `pub struct CollabToolCallItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:257` `pub struct McpToolCallItemResult {`
- `struct` `codex-rs/exec/src/exec_events.rs:271` `pub struct McpToolCallItemError {`
- `struct` `codex-rs/exec/src/exec_events.rs:277` `pub struct McpToolCallItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:289` `pub struct WebSearchItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:297` `pub struct ErrorItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:303` `pub struct TodoItem {`
- `struct` `codex-rs/exec/src/exec_events.rs:309` `pub struct TodoListItem {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::WebSearchAction;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde_json::Value as JsonValue;`
- `use std::collections::HashMap;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
