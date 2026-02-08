# `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `5578`
- sha256: `6850d41c49c9c1ca9301feaa0ebc66b8ae50401261bd0dca5388c034485021cf`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ServerNotification = { "method": "error", "params": ErrorNotification } | { "method": "thread/started", "params": ThreadStartedNotification } | { "method": "thread/name/updated", "params": ThreadNameUpdatedNotification } | { "method": "thread/tokenUsage/updated", "params": ThreadTokenUsageUpdatedNotification } | { "method": "turn/started", "params": TurnStartedNotification } | { "method": "turn/completed", "params": TurnCompletedNotification } | { "method": "turn/diff/updated", "params": TurnDiffUpdatedNotification } | { "method": "turn/plan/updated", "params": TurnPlanUpdatedNotification } | { "method": "item/started", "params": ItemStartedNotification } | { "method": "item/completed", "params": ItemCompletedNotification } | { "method": "rawResponseItem/completed", "params": RawResponseItemCompletedNotification } | { "method": "item/agentMessage/delta", "params": AgentMessageDeltaNotification } | { "method": "item/plan/delta", "params": PlanDeltaNotification } | { "method": "item/commandExecution/outputDelta", "params": CommandExecutionOutputDeltaNotification } | { "method": "item/commandExecution/terminalInteraction", "params": TerminalInteractionNotification } | { "method": "item/fileChange/outputDelta", "params": FileChangeOutputDeltaNotification } | { "method": "item/mcpToolCall/progress", "params": McpToolCallProgressNotification } | { "method": "mcpServer/oauthLogin/completed", "params": McpServerOauthLoginCompletedNotification } | { "method": "account/updated", "params": AccountUpdatedNotification } | { "method": "account/rateLimits/updated", "params": AccountRateLimitsUpdatedNotification } | { "method": "item/reasoning/summaryTextDelta", "params": ReasoningSummaryTextDeltaNotification } | { "method": "item/reasoning/summaryPartAdded", "params": ReasoningSummaryPartAddedNotification } | { "method": "item/reasoning/textDelta", "params": ReasoningTextDeltaNotification } | { "method": "thread/compacted", "params": ContextCompactedNotification } | { "method": "deprecationNotice", "params": DeprecationNoticeNotification } | { "method": "configWarning", "params": ConfigWarningNotification } | { "method": "windows/worldWritableWarning", "params": WindowsWorldWritableWarningNotification } | { "method": "account/login/completed", "params": AccountLoginCompletedNotification } | { "method": "authStatusChange", "params": AuthStatusChangeNotification } | { "method": "loginChatGptComplete", "params": LoginChatGptCompleteNotification } | { "method": "sessionConfigured", "params": SessionConfiguredNotification };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:4` `import type { AuthStatusChangeNotification } from "./AuthStatusChangeNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:5` `import type { LoginChatGptCompleteNotification } from "./LoginChatGptCompleteNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:6` `import type { SessionConfiguredNotification } from "./SessionConfiguredNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:7` `import type { AccountLoginCompletedNotification } from "./v2/AccountLoginCompletedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:8` `import type { AccountRateLimitsUpdatedNotification } from "./v2/AccountRateLimitsUpdatedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:9` `import type { AccountUpdatedNotification } from "./v2/AccountUpdatedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:10` `import type { AgentMessageDeltaNotification } from "./v2/AgentMessageDeltaNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:11` `import type { CommandExecutionOutputDeltaNotification } from "./v2/CommandExecutionOutputDeltaNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:12` `import type { ConfigWarningNotification } from "./v2/ConfigWarningNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:13` `import type { ContextCompactedNotification } from "./v2/ContextCompactedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:14` `import type { DeprecationNoticeNotification } from "./v2/DeprecationNoticeNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:15` `import type { ErrorNotification } from "./v2/ErrorNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:16` `import type { FileChangeOutputDeltaNotification } from "./v2/FileChangeOutputDeltaNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:17` `import type { ItemCompletedNotification } from "./v2/ItemCompletedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:18` `import type { ItemStartedNotification } from "./v2/ItemStartedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:19` `import type { McpServerOauthLoginCompletedNotification } from "./v2/McpServerOauthLoginCompletedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:20` `import type { McpToolCallProgressNotification } from "./v2/McpToolCallProgressNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:21` `import type { PlanDeltaNotification } from "./v2/PlanDeltaNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:22` `import type { RawResponseItemCompletedNotification } from "./v2/RawResponseItemCompletedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:23` `import type { ReasoningSummaryPartAddedNotification } from "./v2/ReasoningSummaryPartAddedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:24` `import type { ReasoningSummaryTextDeltaNotification } from "./v2/ReasoningSummaryTextDeltaNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:25` `import type { ReasoningTextDeltaNotification } from "./v2/ReasoningTextDeltaNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:26` `import type { TerminalInteractionNotification } from "./v2/TerminalInteractionNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:27` `import type { ThreadNameUpdatedNotification } from "./v2/ThreadNameUpdatedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:28` `import type { ThreadStartedNotification } from "./v2/ThreadStartedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:29` `import type { ThreadTokenUsageUpdatedNotification } from "./v2/ThreadTokenUsageUpdatedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:30` `import type { TurnCompletedNotification } from "./v2/TurnCompletedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:31` `import type { TurnDiffUpdatedNotification } from "./v2/TurnDiffUpdatedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:32` `import type { TurnPlanUpdatedNotification } from "./v2/TurnPlanUpdatedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:33` `import type { TurnStartedNotification } from "./v2/TurnStartedNotification";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:34` `import type { WindowsWorldWritableWarningNotification } from "./v2/WindowsWorldWritableWarningNotification";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ServerNotification.ts:39` `export type ServerNotification = { "method": "error", "params": ErrorNotification } | { "method": "thread/started", "params": ThreadStartedNotification } | { "method": "thread/name/updated", "params": ThreadNameUpdatedNotification } | { "method": "thread/tokenUsage/updated", "params": ThreadTokenUsageUpdatedNotification } | { "method": "turn/started", "params": TurnStartedNotification } | { "method": "turn/completed", "params": TurnCompletedNotification } | { "method": "turn/diff/updated", "params": TurnDiffUpdatedNotification } | { "method": "turn/plan/updated", "params": TurnPlanUpdatedNotification } | { "method": "item/started", "params": ItemStartedNotification } | { "method": "item/completed", "params": ItemCompletedNotification } | { "method": "rawResponseItem/completed", "params": RawResponseItemCompletedNotification } | { "method": "item/agentMessage/delta", "params": AgentMessageDeltaNotification } | { "method": "item/plan/delta", "params": PlanDeltaNotification } | { "method": "item/commandExecution/outputDelta", "params": CommandExecutionOutputDeltaNotification } | { "method": "item/commandExecution/terminalInteraction", "params": TerminalInteractionNotification } | { "method": "item/fileChange/outputDelta", "params": FileChangeOutputDeltaNotification } | { "method": "item/mcpToolCall/progress", "params": McpToolCallProgressNotification } | { "method": "mcpServer/oauthLogin/completed", "params": McpServerOauthLoginCompletedNotification } | { "method": "account/updated", "params": AccountUpdatedNotification } | { "method": "account/rateLimits/updated", "params": AccountRateLimitsUpdatedNotification } | { "method": "item/reasoning/summaryTextDelta", "params": ReasoningSummaryTextDeltaNotification } | { "method": "item/reasoning/summaryPartAdded", "params": ReasoningSummaryPartAddedNotification } | { "method": "item/reasoning/textDelta", "params": ReasoningTextDeltaNotification } | { "method": "thread/compacted", "params": ContextCompactedNotification } | { "method": "deprecationNotice", "params": DeprecationNoticeNotification } | { "method": "configWarning", "params": ConfigWarningNotification } | { "method": "windows/worldWritableWarning", "params": WindowsWorldWritableWarningNotification } | { "method": "account/login/completed", "params": AccountLoginCompletedNotification } | { "method": "authStatusChange", "params": AuthStatusChangeNotification } | { "method": "loginChatGptComplete", "params": LoginChatGptCompleteNotification } | { "method": "sessionConfigured", "params": SessionConfiguredNotification };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AuthStatusChangeNotification } from "./AuthStatusChangeNotification";`
- `import type { LoginChatGptCompleteNotification } from "./LoginChatGptCompleteNotification";`
- `import type { SessionConfiguredNotification } from "./SessionConfiguredNotification";`
- `import type { AccountLoginCompletedNotification } from "./v2/AccountLoginCompletedNotification";`
- `import type { AccountRateLimitsUpdatedNotification } from "./v2/AccountRateLimitsUpdatedNotification";`
- `import type { AccountUpdatedNotification } from "./v2/AccountUpdatedNotification";`
- `import type { AgentMessageDeltaNotification } from "./v2/AgentMessageDeltaNotification";`
- `import type { CommandExecutionOutputDeltaNotification } from "./v2/CommandExecutionOutputDeltaNotification";`
- `import type { ConfigWarningNotification } from "./v2/ConfigWarningNotification";`
- `import type { ContextCompactedNotification } from "./v2/ContextCompactedNotification";`
- `import type { DeprecationNoticeNotification } from "./v2/DeprecationNoticeNotification";`
- `import type { ErrorNotification } from "./v2/ErrorNotification";`
- `import type { FileChangeOutputDeltaNotification } from "./v2/FileChangeOutputDeltaNotification";`
- `import type { ItemCompletedNotification } from "./v2/ItemCompletedNotification";`
- `import type { ItemStartedNotification } from "./v2/ItemStartedNotification";`
- `import type { McpServerOauthLoginCompletedNotification } from "./v2/McpServerOauthLoginCompletedNotification";`
- `import type { McpToolCallProgressNotification } from "./v2/McpToolCallProgressNotification";`
- `import type { PlanDeltaNotification } from "./v2/PlanDeltaNotification";`
- `import type { RawResponseItemCompletedNotification } from "./v2/RawResponseItemCompletedNotification";`
- `import type { ReasoningSummaryPartAddedNotification } from "./v2/ReasoningSummaryPartAddedNotification";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
