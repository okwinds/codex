# `codex-rs/exec/src/event_processor_with_jsonl_output.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `31386`
- sha256: `8e8d3d163272ad5cacb8cdef7a62b3436882280cfdd48e3cc5578177d08b478e`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/event_processor_with_jsonl_output.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct EventProcessorWithJsonOutput {`
- `pub fn new(last_message_path: Option<PathBuf>) -> Self {`
- `pub fn collect_thread_events(&mut self, event: &protocol::Event) -> Vec<ThreadEvent> {`

## Definitions (auto, per-file)
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:3` `use std::sync::atomic::AtomicU64;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:5` `use crate::event_processor::CodexStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:6` `use crate::event_processor::EventProcessor;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:7` `use crate::event_processor::handle_last_message;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:8` `use crate::exec_events::AgentMessageItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:9` `use crate::exec_events::CollabAgentState;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:10` `use crate::exec_events::CollabAgentStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:11` `use crate::exec_events::CollabTool;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:12` `use crate::exec_events::CollabToolCallItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:13` `use crate::exec_events::CollabToolCallStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:14` `use crate::exec_events::CommandExecutionItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:15` `use crate::exec_events::CommandExecutionStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:16` `use crate::exec_events::ErrorItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:17` `use crate::exec_events::FileChangeItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:18` `use crate::exec_events::FileUpdateChange;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:19` `use crate::exec_events::ItemCompletedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:20` `use crate::exec_events::ItemStartedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:21` `use crate::exec_events::ItemUpdatedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:22` `use crate::exec_events::McpToolCallItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:23` `use crate::exec_events::McpToolCallItemError;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:24` `use crate::exec_events::McpToolCallItemResult;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:25` `use crate::exec_events::McpToolCallStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:26` `use crate::exec_events::PatchApplyStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:27` `use crate::exec_events::PatchChangeKind;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:28` `use crate::exec_events::ReasoningItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:29` `use crate::exec_events::ThreadErrorEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:30` `use crate::exec_events::ThreadEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:31` `use crate::exec_events::ThreadItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:32` `use crate::exec_events::ThreadItemDetails;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:33` `use crate::exec_events::ThreadStartedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:34` `use crate::exec_events::TodoItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:35` `use crate::exec_events::TodoListItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:36` `use crate::exec_events::TurnCompletedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:37` `use crate::exec_events::TurnFailedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:38` `use crate::exec_events::TurnStartedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:39` `use crate::exec_events::Usage;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:40` `use crate::exec_events::WebSearchItem;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:41` `use codex_core::config::Config;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:42` `use codex_core::protocol;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:43` `use codex_core::protocol::AgentStatus as CoreAgentStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:44` `use codex_core::protocol::CollabAgentInteractionBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:45` `use codex_core::protocol::CollabAgentInteractionEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:46` `use codex_core::protocol::CollabAgentSpawnBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:47` `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:48` `use codex_core::protocol::CollabCloseBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:49` `use codex_core::protocol::CollabCloseEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:50` `use codex_core::protocol::CollabWaitingBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:51` `use codex_core::protocol::CollabWaitingEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:52` `use codex_protocol::models::WebSearchAction;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:53` `use codex_protocol::plan_tool::StepStatus;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:54` `use codex_protocol::plan_tool::UpdatePlanArgs;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:55` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:56` `use tracing::error;`
- `use` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:57` `use tracing::warn;`
- `struct` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:59` `pub struct EventProcessorWithJsonOutput {`
- `struct` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:76` `struct RunningCommand {`
- `struct` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:83` `struct RunningTodoList {`
- `struct` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:89` `struct RunningMcpToolCall {`
- `struct` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:97` `struct RunningCollabToolCall {`
- `impl` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:102` `impl EventProcessorWithJsonOutput {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:103` `pub fn new(last_message_path: Option<PathBuf>) -> Self {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:119` `pub fn collect_thread_events(&mut self, event: &protocol::Event) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:194` `fn get_next_item_id(&self) -> String {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:202` `fn handle_session_configured(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:211` `fn handle_web_search_begin(&mut self, ev: &protocol::WebSearchBeginEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:230` `fn handle_web_search_end(&mut self, ev: &protocol::WebSearchEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:247` `fn handle_output_chunk(&mut self, _call_id: &str, _chunk: &[u8]) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:252` `fn handle_terminal_interaction(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:260` `fn handle_agent_message(&self, payload: &protocol::AgentMessageEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:272` `fn handle_reasoning_event(&self, ev: &protocol::AgentReasoningEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:283` `fn handle_exec_command_begin(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:322` `fn handle_mcp_tool_call_begin(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:356` `fn handle_mcp_tool_call_end(&mut self, ev: &protocol::McpToolCallEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:416` `fn handle_collab_spawn_begin(&mut self, ev: &CollabAgentSpawnBeginEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:426` `fn handle_collab_spawn_end(&mut self, ev: &CollabAgentSpawnEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:454` `fn handle_collab_interaction_begin(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:467` `fn handle_collab_interaction_end(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:489` `fn handle_collab_wait_begin(&mut self, ev: &CollabWaitingBeginEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:502` `fn handle_collab_wait_end(&mut self, ev: &CollabWaitingEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:535` `fn handle_collab_close_begin(&mut self, ev: &CollabCloseBeginEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:545` `fn handle_collab_close_end(&mut self, ev: &CollabCloseEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:564` `fn start_collab_tool_call(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:595` `fn finish_collab_tool_call(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:629` `fn handle_patch_apply_begin(`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:639` `fn map_change_kind(&self, kind: &protocol::FileChange) -> PatchChangeKind {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:647` `fn handle_patch_apply_end(&mut self, ev: &protocol::PatchApplyEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:676` `fn handle_exec_command_end(&mut self, ev: &protocol::ExecCommandEndEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:713` `fn todo_items_from_plan(&self, args: &UpdatePlanArgs) -> Vec<TodoItem> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:723` `fn handle_plan_update(&mut self, args: &UpdatePlanArgs) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:747` `fn handle_task_started(&mut self, _: &protocol::TurnStartedEvent) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:752` `fn handle_task_complete(&mut self) -> Vec<ThreadEvent> {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:800` `fn is_collab_failure(status: &CoreAgentStatus) -> bool {`
- `impl` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:807` `impl From<CoreAgentStatus> for CollabAgentState {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:808` `fn from(value: CoreAgentStatus) -> Self {`
- `impl` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:838` `impl EventProcessor for EventProcessorWithJsonOutput {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:839` `fn print_config_summary(&mut self, _: &Config, _: &str, ev: &protocol::SessionConfiguredEvent) {`
- `fn` `codex-rs/exec/src/event_processor_with_jsonl_output.rs:847` `fn process_event(&mut self, event: protocol::Event) -> CodexStatus {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use std::sync::atomic::AtomicU64;`
- `use crate::event_processor::CodexStatus;`
- `use crate::event_processor::EventProcessor;`
- `use crate::event_processor::handle_last_message;`
- `use crate::exec_events::AgentMessageItem;`
- `use crate::exec_events::CollabAgentState;`
- `use crate::exec_events::CollabAgentStatus;`
- `use crate::exec_events::CollabTool;`
- `use crate::exec_events::CollabToolCallItem;`
- `use crate::exec_events::CollabToolCallStatus;`
- `use crate::exec_events::CommandExecutionItem;`
- `use crate::exec_events::CommandExecutionStatus;`
- `use crate::exec_events::ErrorItem;`
- `use crate::exec_events::FileChangeItem;`
- `use crate::exec_events::FileUpdateChange;`
- `use crate::exec_events::ItemCompletedEvent;`
- `use crate::exec_events::ItemStartedEvent;`
- `use crate::exec_events::ItemUpdatedEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
