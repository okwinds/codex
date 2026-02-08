# `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1581`
- sha256: `8805e40b9bfc5528f8ce4399fd09103ccffa78f7ff6a64f3a012c9db8298fcdf`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ServerRequest = { "method": "item/commandExecution/requestApproval", id: RequestId, params: CommandExecutionRequestApprovalParams, } | { "method": "item/fileChange/requestApproval", id: RequestId, params: FileChangeRequestApprovalParams, } | { "method": "item/tool/requestUserInput", id: RequestId, params: ToolRequestUserInputParams, } | { "method": "item/tool/call", id: RequestId, params: DynamicToolCallParams, } | { "method": "account/chatgptAuthTokens/refresh", id: RequestId, params: ChatgptAuthTokensRefreshParams, } | { "method": "applyPatchApproval", id: RequestId, params: ApplyPatchApprovalParams, } | { "method": "execCommandApproval", id: RequestId, params: ExecCommandApprovalParams, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:4` `import type { ApplyPatchApprovalParams } from "./ApplyPatchApprovalParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:5` `import type { ExecCommandApprovalParams } from "./ExecCommandApprovalParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:6` `import type { RequestId } from "./RequestId";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:7` `import type { ChatgptAuthTokensRefreshParams } from "./v2/ChatgptAuthTokensRefreshParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:8` `import type { CommandExecutionRequestApprovalParams } from "./v2/CommandExecutionRequestApprovalParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:9` `import type { DynamicToolCallParams } from "./v2/DynamicToolCallParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:10` `import type { FileChangeRequestApprovalParams } from "./v2/FileChangeRequestApprovalParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:11` `import type { ToolRequestUserInputParams } from "./v2/ToolRequestUserInputParams";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ServerRequest.ts:16` `export type ServerRequest = { "method": "item/commandExecution/requestApproval", id: RequestId, params: CommandExecutionRequestApprovalParams, } | { "method": "item/fileChange/requestApproval", id: RequestId, params: FileChangeRequestApprovalParams, } | { "method": "item/tool/requestUserInput", id: RequestId, params: ToolRequestUserInputParams, } | { "method": "item/tool/call", id: RequestId, params: DynamicToolCallParams, } | { "method": "account/chatgptAuthTokens/refresh", id: RequestId, params: ChatgptAuthTokensRefreshParams, } | { "method": "applyPatchApproval", id: RequestId, params: ApplyPatchApprovalParams, } | { "method": "execCommandApproval", id: RequestId, params: ExecCommandApprovalParams, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ApplyPatchApprovalParams } from "./ApplyPatchApprovalParams";`
- `import type { ExecCommandApprovalParams } from "./ExecCommandApprovalParams";`
- `import type { RequestId } from "./RequestId";`
- `import type { ChatgptAuthTokensRefreshParams } from "./v2/ChatgptAuthTokensRefreshParams";`
- `import type { CommandExecutionRequestApprovalParams } from "./v2/CommandExecutionRequestApprovalParams";`
- `import type { DynamicToolCallParams } from "./v2/DynamicToolCallParams";`
- `import type { FileChangeRequestApprovalParams } from "./v2/FileChangeRequestApprovalParams";`
- `import type { ToolRequestUserInputParams } from "./v2/ToolRequestUserInputParams";`
- `export type ServerRequest = { "method": "item/commandExecution/requestApproval", id: RequestId, params: CommandExecutionRequestApprovalParams, } | { "method": "item/fileChange/requestApproval", id: RequestId, params: FileChangeRequestApprovalParams, } | { "method": "item/tool/requestUserInput", id: RequestId, params: ToolRequestUserInputParams, } | { "method": "item/tool/call", id: RequestId, params: DynamicToolCallParams, } | { "method": "account/chatgptAuthTokens/refresh", id: RequestId, params: ChatgptAuthTokensRefreshParams, } | { "method": "applyPatchApproval", id: RequestId, params: ApplyPatchApprovalParams, } | { "method": "execCommandApproval", id: RequestId, params: ExecCommandApprovalParams, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
