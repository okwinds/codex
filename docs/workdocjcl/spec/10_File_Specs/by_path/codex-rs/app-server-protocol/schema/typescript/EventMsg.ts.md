# `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `8731`
- sha256: `5ab7da9ba3ef8b56965f67d733309ca029da16fe710856435c0ccf54c4d3d4a5`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type EventMsg = { "type": "error" } & ErrorEvent | { "type": "warning" } & WarningEvent | { "type": "context_compacted" } & ContextCompactedEvent | { "type": "thread_rolled_back" } & ThreadRolledBackEvent | { "type": "task_started" } & TurnStartedEvent | { "type": "task_complete" } & TurnCompleteEvent | { "type": "token_count" } & TokenCountEvent | { "type": "agent_message" } & AgentMessageEvent | { "type": "user_message" } & UserMessageEvent | { "type": "agent_message_delta" } & AgentMessageDeltaEvent | { "type": "agent_reasoning" } & AgentReasoningEvent | { "type": "agent_reasoning_delta" } & AgentReasoningDeltaEvent | { "type": "agent_reasoning_raw_content" } & AgentReasoningRawContentEvent | { "type": "agent_reasoning_raw_content_delta" } & AgentReasoningRawContentDeltaEvent | { "type": "agent_reasoning_section_break" } & AgentReasoningSectionBreakEvent | { "type": "session_configured" } & SessionConfiguredEvent | { "type": "thread_name_updated" } & ThreadNameUpdatedEvent | { "type": "mcp_startup_update" } & McpStartupUpdateEvent | { "type": "mcp_startup_complete" } & McpStartupCompleteEvent | { "type": "mcp_tool_call_begin" } & McpToolCallBeginEvent | { "type": "mcp_tool_call_end" } & McpToolCallEndEvent | { "type": "web_search_begin" } & WebSearchBeginEvent | { "type": "web_search_end" } & WebSearchEndEvent | { "type": "exec_command_begin" } & ExecCommandBeginEvent | { "type": "exec_command_output_delta" } & ExecCommandOutputDeltaEvent | { "type": "terminal_interaction" } & TerminalInteractionEvent | { "type": "exec_command_end" } & ExecCommandEndEvent | { "type": "view_image_tool_call" } & ViewImageToolCallEvent | { "type": "exec_approval_request" } & ExecApprovalRequestEvent | { "type": "request_user_input" } & RequestUserInputEvent | { "type": "dynamic_tool_call_request" } & DynamicToolCallRequest | { "type": "elicitation_request" } & ElicitationRequestEvent | { "type": "apply_patch_approval_request" } & ApplyPatchApprovalRequestEvent | { "type": "deprecation_notice" } & DeprecationNoticeEvent | { "type": "background_event" } & BackgroundEventEvent | { "type": "undo_started" } & UndoStartedEvent | { "type": "undo_completed" } & UndoCompletedEvent | { "type": "stream_error" } & StreamErrorEvent | { "type": "patch_apply_begin" } & PatchApplyBeginEvent | { "type": "patch_apply_end" } & PatchApplyEndEvent | { "type": "turn_diff" } & TurnDiffEvent | { "type": "get_history_entry_response" } & GetHistoryEntryResponseEvent | { "type": "mcp_list_tools_response" } & McpListToolsResponseEvent | { "type": "list_custom_prompts_response" } & ListCustomPromptsResponseEvent | { "type": "list_skills_response" } & ListSkillsResponseEvent | { "type": "skills_update_available" } | { "type": "plan_update" } & UpdatePlanArgs | { "type": "turn_aborted" } & TurnAbortedEvent | { "type": "shutdown_complete" } | { "type": "entered_review_mode" } & ReviewRequest | { "type": "exited_review_mode" } & ExitedReviewModeEvent | { "type": "raw_response_item" } & RawResponseItemEvent | { "type": "item_started" } & ItemStartedEvent | { "type": "item_completed" } & ItemCompletedEvent | { "type": "agent_message_content_delta" } & AgentMessageContentDeltaEvent | { "type": "plan_delta" } & PlanDeltaEvent | { "type": "reasoning_content_delta" } & ReasoningContentDeltaEvent | { "type": "reasoning_raw_content_delta" } & ReasoningRawContentDeltaEvent | { "type": "collab_agent_spawn_begin" } & CollabAgentSpawnBeginEvent | { "type": "collab_agent_spawn_end" } & CollabAgentSpawnEndEvent | { "type": "collab_agent_interaction_begin" } & CollabAgentInteractionBeginEvent | { "type": "collab_agent_interaction_end" } & CollabAgentInteractionEndEvent | { "type": "collab_waiting_begin" } & CollabWaitingBeginEvent | { "type": "collab_waiting_end" } & CollabWaitingEndEvent | { "type": "collab_close_begin" } & CollabCloseBeginEvent | { "type": "collab_close_end" } & CollabCloseEndEvent;`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:4` `import type { AgentMessageContentDeltaEvent } from "./AgentMessageContentDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:5` `import type { AgentMessageDeltaEvent } from "./AgentMessageDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:6` `import type { AgentMessageEvent } from "./AgentMessageEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:7` `import type { AgentReasoningDeltaEvent } from "./AgentReasoningDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:8` `import type { AgentReasoningEvent } from "./AgentReasoningEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:9` `import type { AgentReasoningRawContentDeltaEvent } from "./AgentReasoningRawContentDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:10` `import type { AgentReasoningRawContentEvent } from "./AgentReasoningRawContentEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:11` `import type { AgentReasoningSectionBreakEvent } from "./AgentReasoningSectionBreakEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:12` `import type { ApplyPatchApprovalRequestEvent } from "./ApplyPatchApprovalRequestEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:13` `import type { BackgroundEventEvent } from "./BackgroundEventEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:14` `import type { CollabAgentInteractionBeginEvent } from "./CollabAgentInteractionBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:15` `import type { CollabAgentInteractionEndEvent } from "./CollabAgentInteractionEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:16` `import type { CollabAgentSpawnBeginEvent } from "./CollabAgentSpawnBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:17` `import type { CollabAgentSpawnEndEvent } from "./CollabAgentSpawnEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:18` `import type { CollabCloseBeginEvent } from "./CollabCloseBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:19` `import type { CollabCloseEndEvent } from "./CollabCloseEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:20` `import type { CollabWaitingBeginEvent } from "./CollabWaitingBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:21` `import type { CollabWaitingEndEvent } from "./CollabWaitingEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:22` `import type { ContextCompactedEvent } from "./ContextCompactedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:23` `import type { DeprecationNoticeEvent } from "./DeprecationNoticeEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:24` `import type { DynamicToolCallRequest } from "./DynamicToolCallRequest";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:25` `import type { ElicitationRequestEvent } from "./ElicitationRequestEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:26` `import type { ErrorEvent } from "./ErrorEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:27` `import type { ExecApprovalRequestEvent } from "./ExecApprovalRequestEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:28` `import type { ExecCommandBeginEvent } from "./ExecCommandBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:29` `import type { ExecCommandEndEvent } from "./ExecCommandEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:30` `import type { ExecCommandOutputDeltaEvent } from "./ExecCommandOutputDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:31` `import type { ExitedReviewModeEvent } from "./ExitedReviewModeEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:32` `import type { GetHistoryEntryResponseEvent } from "./GetHistoryEntryResponseEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:33` `import type { ItemCompletedEvent } from "./ItemCompletedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:34` `import type { ItemStartedEvent } from "./ItemStartedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:35` `import type { ListCustomPromptsResponseEvent } from "./ListCustomPromptsResponseEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:36` `import type { ListSkillsResponseEvent } from "./ListSkillsResponseEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:37` `import type { McpListToolsResponseEvent } from "./McpListToolsResponseEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:38` `import type { McpStartupCompleteEvent } from "./McpStartupCompleteEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:39` `import type { McpStartupUpdateEvent } from "./McpStartupUpdateEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:40` `import type { McpToolCallBeginEvent } from "./McpToolCallBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:41` `import type { McpToolCallEndEvent } from "./McpToolCallEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:42` `import type { PatchApplyBeginEvent } from "./PatchApplyBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:43` `import type { PatchApplyEndEvent } from "./PatchApplyEndEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:44` `import type { PlanDeltaEvent } from "./PlanDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:45` `import type { RawResponseItemEvent } from "./RawResponseItemEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:46` `import type { ReasoningContentDeltaEvent } from "./ReasoningContentDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:47` `import type { ReasoningRawContentDeltaEvent } from "./ReasoningRawContentDeltaEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:48` `import type { RequestUserInputEvent } from "./RequestUserInputEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:49` `import type { ReviewRequest } from "./ReviewRequest";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:50` `import type { SessionConfiguredEvent } from "./SessionConfiguredEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:51` `import type { StreamErrorEvent } from "./StreamErrorEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:52` `import type { TerminalInteractionEvent } from "./TerminalInteractionEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:53` `import type { ThreadNameUpdatedEvent } from "./ThreadNameUpdatedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:54` `import type { ThreadRolledBackEvent } from "./ThreadRolledBackEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:55` `import type { TokenCountEvent } from "./TokenCountEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:56` `import type { TurnAbortedEvent } from "./TurnAbortedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:57` `import type { TurnCompleteEvent } from "./TurnCompleteEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:58` `import type { TurnDiffEvent } from "./TurnDiffEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:59` `import type { TurnStartedEvent } from "./TurnStartedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:60` `import type { UndoCompletedEvent } from "./UndoCompletedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:61` `import type { UndoStartedEvent } from "./UndoStartedEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:62` `import type { UpdatePlanArgs } from "./UpdatePlanArgs";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:63` `import type { UserMessageEvent } from "./UserMessageEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:64` `import type { ViewImageToolCallEvent } from "./ViewImageToolCallEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:65` `import type { WarningEvent } from "./WarningEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:66` `import type { WebSearchBeginEvent } from "./WebSearchBeginEvent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:67` `import type { WebSearchEndEvent } from "./WebSearchEndEvent";`
- `export` `codex-rs/app-server-protocol/schema/typescript/EventMsg.ts:73` `export type EventMsg = { "type": "error" } & ErrorEvent | { "type": "warning" } & WarningEvent | { "type": "context_compacted" } & ContextCompactedEvent | { "type": "thread_rolled_back" } & ThreadRolledBackEvent | { "type": "task_started" } & TurnStartedEvent | { "type": "task_complete" } & TurnCompleteEvent | { "type": "token_count" } & TokenCountEvent | { "type": "agent_message" } & AgentMessageEvent | { "type": "user_message" } & UserMessageEvent | { "type": "agent_message_delta" } & AgentMessageDeltaEvent | { "type": "agent_reasoning" } & AgentReasoningEvent | { "type": "agent_reasoning_delta" } & AgentReasoningDeltaEvent | { "type": "agent_reasoning_raw_content" } & AgentReasoningRawContentEvent | { "type": "agent_reasoning_raw_content_delta" } & AgentReasoningRawContentDeltaEvent | { "type": "agent_reasoning_section_break" } & AgentReasoningSectionBreakEvent | { "type": "session_configured" } & SessionConfiguredEvent | { "type": "thread_name_updated" } & ThreadNameUpdatedEvent | { "type": "mcp_startup_update" } & McpStartupUpdateEvent | { "type": "mcp_startup_complete" } & McpStartupCompleteEvent | { "type": "mcp_tool_call_begin" } & McpToolCallBeginEvent | { "type": "mcp_tool_call_end" } & McpToolCallEndEvent | { "type": "web_search_begin" } & WebSearchBeginEvent | { "type": "web_search_end" } & WebSearchEndEvent | { "type": "exec_command_begin" } & ExecCommandBeginEvent | { "type": "exec_command_output_delta" } & ExecCommandOutputDeltaEvent | { "type": "terminal_interaction" } & TerminalInteractionEvent | { "type": "exec_command_end" } & ExecCommandEndEvent | { "type": "view_image_tool_call" } & ViewImageToolCallEvent | { "type": "exec_approval_request" } & ExecApprovalRequestEvent | { "type": "request_user_input" } & RequestUserInputEvent | { "type": "dynamic_tool_call_request" } & DynamicToolCallRequest | { "type": "elicitation_request" } & ElicitationRequestEvent | { "type": "apply_patch_approval_request" } & ApplyPatchApprovalRequestEvent | { "type": "deprecation_notice" } & DeprecationNoticeEvent | { "type": "background_event" } & BackgroundEventEvent | { "type": "undo_started" } & UndoStartedEvent | { "type": "undo_completed" } & UndoCompletedEvent | { "type": "stream_error" } & StreamErrorEvent | { "type": "patch_apply_begin" } & PatchApplyBeginEvent | { "type": "patch_apply_end" } & PatchApplyEndEvent | { "type": "turn_diff" } & TurnDiffEvent | { "type": "get_history_entry_response" } & GetHistoryEntryResponseEvent | { "type": "mcp_list_tools_response" } & McpListToolsResponseEvent | { "type": "list_custom_prompts_response" } & ListCustomPromptsResponseEvent | { "type": "list_skills_response" } & ListSkillsResponseEvent | { "type": "skills_update_available" } | { "type": "plan_update" } & UpdatePlanArgs | { "type": "turn_aborted" } & TurnAbortedEvent | { "type": "shutdown_complete" } | { "type": "entered_review_mode" } & ReviewRequest | { "type": "exited_review_mode" } & ExitedReviewModeEvent | { "type": "raw_response_item" } & RawResponseItemEvent | { "type": "item_started" } & ItemStartedEvent | { "type": "item_completed" } & ItemCompletedEvent | { "type": "agent_message_content_delta" } & AgentMessageContentDeltaEvent | { "type": "plan_delta" } & PlanDeltaEvent | { "type": "reasoning_content_delta" } & ReasoningContentDeltaEvent | { "type": "reasoning_raw_content_delta" } & ReasoningRawContentDeltaEvent | { "type": "collab_agent_spawn_begin" } & CollabAgentSpawnBeginEvent | { "type": "collab_agent_spawn_end" } & CollabAgentSpawnEndEvent | { "type": "collab_agent_interaction_begin" } & CollabAgentInteractionBeginEvent | { "type": "collab_agent_interaction_end" } & CollabAgentInteractionEndEvent | { "type": "collab_waiting_begin" } & CollabWaitingBeginEvent | { "type": "collab_waiting_end" } & CollabWaitingEndEvent | { "type": "collab_close_begin" } & CollabCloseBeginEvent | { "type": "collab_close_end" } & CollabCloseEndEvent;`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AgentMessageContentDeltaEvent } from "./AgentMessageContentDeltaEvent";`
- `import type { AgentMessageDeltaEvent } from "./AgentMessageDeltaEvent";`
- `import type { AgentMessageEvent } from "./AgentMessageEvent";`
- `import type { AgentReasoningDeltaEvent } from "./AgentReasoningDeltaEvent";`
- `import type { AgentReasoningEvent } from "./AgentReasoningEvent";`
- `import type { AgentReasoningRawContentDeltaEvent } from "./AgentReasoningRawContentDeltaEvent";`
- `import type { AgentReasoningRawContentEvent } from "./AgentReasoningRawContentEvent";`
- `import type { AgentReasoningSectionBreakEvent } from "./AgentReasoningSectionBreakEvent";`
- `import type { ApplyPatchApprovalRequestEvent } from "./ApplyPatchApprovalRequestEvent";`
- `import type { BackgroundEventEvent } from "./BackgroundEventEvent";`
- `import type { CollabAgentInteractionBeginEvent } from "./CollabAgentInteractionBeginEvent";`
- `import type { CollabAgentInteractionEndEvent } from "./CollabAgentInteractionEndEvent";`
- `import type { CollabAgentSpawnBeginEvent } from "./CollabAgentSpawnBeginEvent";`
- `import type { CollabAgentSpawnEndEvent } from "./CollabAgentSpawnEndEvent";`
- `import type { CollabCloseBeginEvent } from "./CollabCloseBeginEvent";`
- `import type { CollabCloseEndEvent } from "./CollabCloseEndEvent";`
- `import type { CollabWaitingBeginEvent } from "./CollabWaitingBeginEvent";`
- `import type { CollabWaitingEndEvent } from "./CollabWaitingEndEvent";`
- `import type { ContextCompactedEvent } from "./ContextCompactedEvent";`
- `import type { DeprecationNoticeEvent } from "./DeprecationNoticeEvent";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
