# `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `7869`
- sha256: `54b2ca100ead1e401764305dccf874dae097206487b500b023bd42b5bc170460`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ClientRequest ={ "method": "initialize", id: RequestId, params: InitializeParams, } | { "method": "thread/start", id: RequestId, params: ThreadStartParams, } | { "method": "thread/resume", id: RequestId, params: ThreadResumeParams, } | { "method": "thread/fork", id: RequestId, params: ThreadForkParams, } | { "method": "thread/archive", id: RequestId, params: ThreadArchiveParams, } | { "method": "thread/name/set", id: RequestId, params: ThreadSetNameParams, } | { "method": "thread/unarchive", id: RequestId, params: ThreadUnarchiveParams, } | { "method": "thread/rollback", id: RequestId, params: ThreadRollbackParams, } | { "method": "thread/list", id: RequestId, params: ThreadListParams, } | { "method": "thread/loaded/list", id: RequestId, params: ThreadLoadedListParams, } | { "method": "thread/read", id: RequestId, params: ThreadReadParams, } | { "method": "skills/list", id: RequestId, params: SkillsListParams, } | { "method": "app/list", id: RequestId, params: AppsListParams, } | { "method": "skills/config/write", id: RequestId, params: SkillsConfigWriteParams, } | { "method": "turn/start", id: RequestId, params: TurnStartParams, } | { "method": "turn/interrupt", id: RequestId, params: TurnInterruptParams, } | { "method": "review/start", id: RequestId, params: ReviewStartParams, } | { "method": "model/list", id: RequestId, params: ModelListParams, } | { "method": "mcpServer/oauth/login", id: RequestId, params: McpServerOauthLoginParams, } | { "method": "config/mcpServer/reload", id: RequestId, params: undefined, } | { "method": "mcpServerStatus/list", id: RequestId, params: ListMcpServerStatusParams, } | { "method": "account/login/start", id: RequestId, params: LoginAccountParams, } | { "method": "account/login/cancel", id: RequestId, params: CancelLoginAccountParams, } | { "method": "account/logout", id: RequestId, params: undefined, } | { "method": "account/rateLimits/read", id: RequestId, params: undefined, } | { "method": "feedback/upload", id: RequestId, params: FeedbackUploadParams, } | { "method": "command/exec", id: RequestId, params: CommandExecParams, } | { "method": "config/read", id: RequestId, params: ConfigReadParams, } | { "method": "config/value/write", id: RequestId, params: ConfigValueWriteParams, } | { "method": "config/batchWrite", id: RequestId, params: ConfigBatchWriteParams, } | { "method": "configRequirements/read", id: RequestId, params: undefined, } | { "method": "account/read", id: RequestId, params: GetAccountParams, } | { "method": "newConversation", id: RequestId, params: NewConversationParams, } | { "method": "getConversationSummary", id: RequestId, params: GetConversationSummaryParams, } | { "method": "listConversations", id: RequestId, params: ListConversationsParams, } | { "method": "resumeConversation", id: RequestId, params: ResumeConversationParams, } | { "method": "forkConversation", id: RequestId, params: ForkConversationParams, } | { "method": "archiveConversation", id: RequestId, params: ArchiveConversationParams, } | { "method": "sendUserMessage", id: RequestId, params: SendUserMessageParams, } | { "method": "sendUserTurn", id: RequestId, params: SendUserTurnParams, } | { "method": "interruptConversation", id: RequestId, params: InterruptConversationParams, } | { "method": "addConversationListener", id: RequestId, params: AddConversationListenerParams, } | { "method": "removeConversationListener", id: RequestId, params: RemoveConversationListenerParams, } | { "method": "gitDiffToRemote", id: RequestId, params: GitDiffToRemoteParams, } | { "method": "loginApiKey", id: RequestId, params: LoginApiKeyParams, } | { "method": "loginChatGpt", id: RequestId, params: undefined, } | { "method": "cancelLoginChatGpt", id: RequestId, params: CancelLoginChatGptParams, } | { "method": "logoutChatGpt", id: RequestId, params: undefined, } | { "method": "getAuthStatus", id: RequestId, params: GetAuthStatusParams, } | { "method": "getUserSavedConfig", id: RequestId, params: undefined, } | { "method": "setDefaultModel", id: RequestId, params: SetDefaultModelParams, } | { "method": "getUserAgent", id: RequestId, params: undefined, } | { "method": "userInfo", id: RequestId, params: undefined, } | { "method": "fuzzyFileSearch", id: RequestId, params: FuzzyFileSearchParams, } | { "method": "execOneOffCommand", id: RequestId, params: ExecOneOffCommandParams, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:4` `import type { AddConversationListenerParams } from "./AddConversationListenerParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:5` `import type { ArchiveConversationParams } from "./ArchiveConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:6` `import type { CancelLoginChatGptParams } from "./CancelLoginChatGptParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:7` `import type { ExecOneOffCommandParams } from "./ExecOneOffCommandParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:8` `import type { ForkConversationParams } from "./ForkConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:9` `import type { FuzzyFileSearchParams } from "./FuzzyFileSearchParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:10` `import type { GetAuthStatusParams } from "./GetAuthStatusParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:11` `import type { GetConversationSummaryParams } from "./GetConversationSummaryParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:12` `import type { GitDiffToRemoteParams } from "./GitDiffToRemoteParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:13` `import type { InitializeParams } from "./InitializeParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:14` `import type { InterruptConversationParams } from "./InterruptConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:15` `import type { ListConversationsParams } from "./ListConversationsParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:16` `import type { LoginApiKeyParams } from "./LoginApiKeyParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:17` `import type { NewConversationParams } from "./NewConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:18` `import type { RemoveConversationListenerParams } from "./RemoveConversationListenerParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:19` `import type { RequestId } from "./RequestId";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:20` `import type { ResumeConversationParams } from "./ResumeConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:21` `import type { SendUserMessageParams } from "./SendUserMessageParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:22` `import type { SendUserTurnParams } from "./SendUserTurnParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:23` `import type { SetDefaultModelParams } from "./SetDefaultModelParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:24` `import type { AppsListParams } from "./v2/AppsListParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:25` `import type { CancelLoginAccountParams } from "./v2/CancelLoginAccountParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:26` `import type { CommandExecParams } from "./v2/CommandExecParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:27` `import type { ConfigBatchWriteParams } from "./v2/ConfigBatchWriteParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:28` `import type { ConfigReadParams } from "./v2/ConfigReadParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:29` `import type { ConfigValueWriteParams } from "./v2/ConfigValueWriteParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:30` `import type { FeedbackUploadParams } from "./v2/FeedbackUploadParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:31` `import type { GetAccountParams } from "./v2/GetAccountParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:32` `import type { ListMcpServerStatusParams } from "./v2/ListMcpServerStatusParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:33` `import type { LoginAccountParams } from "./v2/LoginAccountParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:34` `import type { McpServerOauthLoginParams } from "./v2/McpServerOauthLoginParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:35` `import type { ModelListParams } from "./v2/ModelListParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:36` `import type { ReviewStartParams } from "./v2/ReviewStartParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:37` `import type { SkillsConfigWriteParams } from "./v2/SkillsConfigWriteParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:38` `import type { SkillsListParams } from "./v2/SkillsListParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:39` `import type { ThreadArchiveParams } from "./v2/ThreadArchiveParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:40` `import type { ThreadForkParams } from "./v2/ThreadForkParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:41` `import type { ThreadListParams } from "./v2/ThreadListParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:42` `import type { ThreadLoadedListParams } from "./v2/ThreadLoadedListParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:43` `import type { ThreadReadParams } from "./v2/ThreadReadParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:44` `import type { ThreadResumeParams } from "./v2/ThreadResumeParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:45` `import type { ThreadRollbackParams } from "./v2/ThreadRollbackParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:46` `import type { ThreadSetNameParams } from "./v2/ThreadSetNameParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:47` `import type { ThreadStartParams } from "./v2/ThreadStartParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:48` `import type { ThreadUnarchiveParams } from "./v2/ThreadUnarchiveParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:49` `import type { TurnInterruptParams } from "./v2/TurnInterruptParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:50` `import type { TurnStartParams } from "./v2/TurnStartParams";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ClientRequest.ts:55` `export type ClientRequest ={ "method": "initialize", id: RequestId, params: InitializeParams, } | { "method": "thread/start", id: RequestId, params: ThreadStartParams, } | { "method": "thread/resume", id: RequestId, params: ThreadResumeParams, } | { "method": "thread/fork", id: RequestId, params: ThreadForkParams, } | { "method": "thread/archive", id: RequestId, params: ThreadArchiveParams, } | { "method": "thread/name/set", id: RequestId, params: ThreadSetNameParams, } | { "method": "thread/unarchive", id: RequestId, params: ThreadUnarchiveParams, } | { "method": "thread/rollback", id: RequestId, params: ThreadRollbackParams, } | { "method": "thread/list", id: RequestId, params: ThreadListParams, } | { "method": "thread/loaded/list", id: RequestId, params: ThreadLoadedListParams, } | { "method": "thread/read", id: RequestId, params: ThreadReadParams, } | { "method": "skills/list", id: RequestId, params: SkillsListParams, } | { "method": "app/list", id: RequestId, params: AppsListParams, } | { "method": "skills/config/write", id: RequestId, params: SkillsConfigWriteParams, } | { "method": "turn/start", id: RequestId, params: TurnStartParams, } | { "method": "turn/interrupt", id: RequestId, params: TurnInterruptParams, } | { "method": "review/start", id: RequestId, params: ReviewStartParams, } | { "method": "model/list", id: RequestId, params: ModelListParams, } | { "method": "mcpServer/oauth/login", id: RequestId, params: McpServerOauthLoginParams, } | { "method": "config/mcpServer/reload", id: RequestId, params: undefined, } | { "method": "mcpServerStatus/list", id: RequestId, params: ListMcpServerStatusParams, } | { "method": "account/login/start", id: RequestId, params: LoginAccountParams, } | { "method": "account/login/cancel", id: RequestId, params: CancelLoginAccountParams, } | { "method": "account/logout", id: RequestId, params: undefined, } | { "method": "account/rateLimits/read", id: RequestId, params: undefined, } | { "method": "feedback/upload", id: RequestId, params: FeedbackUploadParams, } | { "method": "command/exec", id: RequestId, params: CommandExecParams, } | { "method": "config/read", id: RequestId, params: ConfigReadParams, } | { "method": "config/value/write", id: RequestId, params: ConfigValueWriteParams, } | { "method": "config/batchWrite", id: RequestId, params: ConfigBatchWriteParams, } | { "method": "configRequirements/read", id: RequestId, params: undefined, } | { "method": "account/read", id: RequestId, params: GetAccountParams, } | { "method": "newConversation", id: RequestId, params: NewConversationParams, } | { "method": "getConversationSummary", id: RequestId, params: GetConversationSummaryParams, } | { "method": "listConversations", id: RequestId, params: ListConversationsParams, } | { "method": "resumeConversation", id: RequestId, params: ResumeConversationParams, } | { "method": "forkConversation", id: RequestId, params: ForkConversationParams, } | { "method": "archiveConversation", id: RequestId, params: ArchiveConversationParams, } | { "method": "sendUserMessage", id: RequestId, params: SendUserMessageParams, } | { "method": "sendUserTurn", id: RequestId, params: SendUserTurnParams, } | { "method": "interruptConversation", id: RequestId, params: InterruptConversationParams, } | { "method": "addConversationListener", id: RequestId, params: AddConversationListenerParams, } | { "method": "removeConversationListener", id: RequestId, params: RemoveConversationListenerParams, } | { "method": "gitDiffToRemote", id: RequestId, params: GitDiffToRemoteParams, } | { "method": "loginApiKey", id: RequestId, params: LoginApiKeyParams, } | { "method": "loginChatGpt", id: RequestId, params: undefined, } | { "method": "cancelLoginChatGpt", id: RequestId, params: CancelLoginChatGptParams, } | { "method": "logoutChatGpt", id: RequestId, params: undefined, } | { "method": "getAuthStatus", id: RequestId, params: GetAuthStatusParams, } | { "method": "getUserSavedConfig", id: RequestId, params: undefined, } | { "method": "setDefaultModel", id: RequestId, params: SetDefaultModelParams, } | { "method": "getUserAgent", id: RequestId, params: undefined, } | { "method": "userInfo", id: RequestId, params: undefined, } | { "method": "fuzzyFileSearch", id: RequestId, params: FuzzyFileSearchParams, } | { "method": "execOneOffCommand", id: RequestId, params: ExecOneOffCommandParams, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AddConversationListenerParams } from "./AddConversationListenerParams";`
- `import type { ArchiveConversationParams } from "./ArchiveConversationParams";`
- `import type { CancelLoginChatGptParams } from "./CancelLoginChatGptParams";`
- `import type { ExecOneOffCommandParams } from "./ExecOneOffCommandParams";`
- `import type { ForkConversationParams } from "./ForkConversationParams";`
- `import type { FuzzyFileSearchParams } from "./FuzzyFileSearchParams";`
- `import type { GetAuthStatusParams } from "./GetAuthStatusParams";`
- `import type { GetConversationSummaryParams } from "./GetConversationSummaryParams";`
- `import type { GitDiffToRemoteParams } from "./GitDiffToRemoteParams";`
- `import type { InitializeParams } from "./InitializeParams";`
- `import type { InterruptConversationParams } from "./InterruptConversationParams";`
- `import type { ListConversationsParams } from "./ListConversationsParams";`
- `import type { LoginApiKeyParams } from "./LoginApiKeyParams";`
- `import type { NewConversationParams } from "./NewConversationParams";`
- `import type { RemoveConversationListenerParams } from "./RemoveConversationListenerParams";`
- `import type { RequestId } from "./RequestId";`
- `import type { ResumeConversationParams } from "./ResumeConversationParams";`
- `import type { SendUserMessageParams } from "./SendUserMessageParams";`
- `import type { SendUserTurnParams } from "./SendUserTurnParams";`
- `import type { SetDefaultModelParams } from "./SetDefaultModelParams";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
