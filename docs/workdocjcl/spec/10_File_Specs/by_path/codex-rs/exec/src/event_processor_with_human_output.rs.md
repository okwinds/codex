# `codex-rs/exec/src/event_processor_with_human_output.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36344`
- sha256: `be681bce5ebc38b88c0b3974a141f43a1c8435008ec4235ef977385ec772ed7d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/event_processor_with_human_output.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:1` `use codex_common::elapsed::format_duration;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:2` `use codex_common::elapsed::format_elapsed;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:3` `use codex_core::config::Config;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:4` `use codex_core::protocol::AgentMessageEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:5` `use codex_core::protocol::AgentReasoningRawContentEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:6` `use codex_core::protocol::AgentStatus;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:7` `use codex_core::protocol::BackgroundEventEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:8` `use codex_core::protocol::CollabAgentInteractionBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:9` `use codex_core::protocol::CollabAgentInteractionEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:10` `use codex_core::protocol::CollabAgentSpawnBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:11` `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:12` `use codex_core::protocol::CollabCloseBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:13` `use codex_core::protocol::CollabCloseEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:14` `use codex_core::protocol::CollabWaitingBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:15` `use codex_core::protocol::CollabWaitingEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:16` `use codex_core::protocol::DeprecationNoticeEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:17` `use codex_core::protocol::ErrorEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:18` `use codex_core::protocol::Event;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:19` `use codex_core::protocol::EventMsg;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:20` `use codex_core::protocol::ExecCommandBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:21` `use codex_core::protocol::ExecCommandEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:22` `use codex_core::protocol::FileChange;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:23` `use codex_core::protocol::ItemCompletedEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:24` `use codex_core::protocol::McpInvocation;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:25` `use codex_core::protocol::McpToolCallBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:26` `use codex_core::protocol::McpToolCallEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:27` `use codex_core::protocol::PatchApplyBeginEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:28` `use codex_core::protocol::PatchApplyEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:29` `use codex_core::protocol::SessionConfiguredEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:30` `use codex_core::protocol::StreamErrorEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:31` `use codex_core::protocol::TurnAbortReason;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:32` `use codex_core::protocol::TurnCompleteEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:33` `use codex_core::protocol::TurnDiffEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:34` `use codex_core::protocol::WarningEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:35` `use codex_core::protocol::WebSearchEndEvent;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:36` `use codex_core::web_search::web_search_detail;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:37` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:38` `use codex_protocol::num_format::format_with_separators;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:39` `use owo_colors::OwoColorize;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:40` `use owo_colors::Style;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:41` `use shlex::try_join;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:42` `use std::collections::HashMap;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:43` `use std::path::PathBuf;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:44` `use std::time::Instant;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:46` `use crate::event_processor::CodexStatus;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:47` `use crate::event_processor::EventProcessor;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:48` `use crate::event_processor::handle_last_message;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:49` `use codex_common::create_config_summary_entries;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:50` `use codex_protocol::plan_tool::StepStatus;`
- `use` `codex-rs/exec/src/event_processor_with_human_output.rs:51` `use codex_protocol::plan_tool::UpdatePlanArgs;`
- `const` `codex-rs/exec/src/event_processor_with_human_output.rs:55` `const MAX_OUTPUT_LINES_FOR_EXEC_TOOL_CALL: usize = 20;`
- `impl` `codex-rs/exec/src/event_processor_with_human_output.rs:81` `impl EventProcessorWithHumanOutput {`
- `struct` `codex-rs/exec/src/event_processor_with_human_output.rs:129` `struct PatchApplyBegin {`
- `impl` `codex-rs/exec/src/event_processor_with_human_output.rs:141` `impl EventProcessor for EventProcessorWithHumanOutput {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:145` `fn print_config_summary(`
- `const` `codex-rs/exec/src/event_processor_with_human_output.rs:151` `const VERSION: &str = env!("CARGO_PKG_VERSION");`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:177` `fn process_event(&mut self, event: Event) -> CodexStatus {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:799` `fn print_final_output(&mut self) {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:823` `fn escape_command(command: &[String]) -> String {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:827` `fn format_file_change(change: &FileChange) -> &'static str {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:840` `fn format_collab_invocation(tool: &str, call_id: &str, prompt: Option<&str>) -> String {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:851` `fn format_collab_status(status: &AgentStatus) -> String {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:877` `fn style_for_agent_status(`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:889` `fn is_collab_status_failure(status: &AgentStatus) -> bool {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:893` `fn format_receiver_list(ids: &[codex_protocol::ThreadId]) -> String {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:903` `fn truncate_preview(text: &str, max_chars: usize) -> String {`
- `fn` `codex-rs/exec/src/event_processor_with_human_output.rs:912` `fn format_mcp_invocation(invocation: &McpInvocation) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_common::elapsed::format_duration;`
- `use codex_common::elapsed::format_elapsed;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::AgentMessageEvent;`
- `use codex_core::protocol::AgentReasoningRawContentEvent;`
- `use codex_core::protocol::AgentStatus;`
- `use codex_core::protocol::BackgroundEventEvent;`
- `use codex_core::protocol::CollabAgentInteractionBeginEvent;`
- `use codex_core::protocol::CollabAgentInteractionEndEvent;`
- `use codex_core::protocol::CollabAgentSpawnBeginEvent;`
- `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use codex_core::protocol::CollabCloseBeginEvent;`
- `use codex_core::protocol::CollabCloseEndEvent;`
- `use codex_core::protocol::CollabWaitingBeginEvent;`
- `use codex_core::protocol::CollabWaitingEndEvent;`
- `use codex_core::protocol::DeprecationNoticeEvent;`
- `use codex_core::protocol::ErrorEvent;`
- `use codex_core::protocol::Event;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecCommandBeginEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
