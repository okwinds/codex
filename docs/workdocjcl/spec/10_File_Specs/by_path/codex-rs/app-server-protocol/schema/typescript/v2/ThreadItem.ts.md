# `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `3476`
- sha256: `60c524a0789c8cf98e595b442d495ec375472fb0edf1be4cafa1097893ccb6ff`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ThreadItem = { "type": "userMessage", id: string, content: Array<UserInput>, } | { "type": "agentMessage", id: string, text: string, } | { "type": "plan", id: string, text: string, } | { "type": "reasoning", id: string, summary: Array<string>, content: Array<string>, } | { "type": "commandExecution", id: string,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:5` `import type { CollabAgentState } from "./CollabAgentState";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:6` `import type { CollabAgentTool } from "./CollabAgentTool";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:7` `import type { CollabAgentToolCallStatus } from "./CollabAgentToolCallStatus";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:8` `import type { CommandAction } from "./CommandAction";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:9` `import type { CommandExecutionStatus } from "./CommandExecutionStatus";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:10` `import type { FileUpdateChange } from "./FileUpdateChange";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:11` `import type { McpToolCallError } from "./McpToolCallError";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:12` `import type { McpToolCallResult } from "./McpToolCallResult";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:13` `import type { McpToolCallStatus } from "./McpToolCallStatus";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:14` `import type { PatchApplyStatus } from "./PatchApplyStatus";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:15` `import type { UserInput } from "./UserInput";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:16` `import type { WebSearchAction } from "./WebSearchAction";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadItem.ts:18` `export type ThreadItem = { "type": "userMessage", id: string, content: Array<UserInput>, } | { "type": "agentMessage", id: string, text: string, } | { "type": "plan", id: string, text: string, } | { "type": "reasoning", id: string, summary: Array<string>, content: Array<string>, } | { "type": "commandExecution", id: string,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { CollabAgentState } from "./CollabAgentState";`
- `import type { CollabAgentTool } from "./CollabAgentTool";`
- `import type { CollabAgentToolCallStatus } from "./CollabAgentToolCallStatus";`
- `import type { CommandAction } from "./CommandAction";`
- `import type { CommandExecutionStatus } from "./CommandExecutionStatus";`
- `import type { FileUpdateChange } from "./FileUpdateChange";`
- `import type { McpToolCallError } from "./McpToolCallError";`
- `import type { McpToolCallResult } from "./McpToolCallResult";`
- `import type { McpToolCallStatus } from "./McpToolCallStatus";`
- `import type { PatchApplyStatus } from "./PatchApplyStatus";`
- `import type { UserInput } from "./UserInput";`
- `import type { WebSearchAction } from "./WebSearchAction";`
- `export type ThreadItem = { "type": "userMessage", id: string, content: Array<UserInput>, } | { "type": "agentMessage", id: string, text: string, } | { "type": "plan", id: string, text: string, } | { "type": "reasoning", id: string, summary: Array<string>, content: Array<string>, } | { "type": "commandExecution", id: string,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
