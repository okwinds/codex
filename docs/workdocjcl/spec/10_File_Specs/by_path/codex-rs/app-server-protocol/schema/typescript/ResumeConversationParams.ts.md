# `codex-rs/app-server-protocol/schema/typescript/ResumeConversationParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `495`
- sha256: `c32d3ed8787567b4f444fabb716e181df0728874586abbd2847af5e14a2e83e8`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ResumeConversationParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ResumeConversationParams = { path: string | null, conversationId: ThreadId | null, history: Array<ResponseItem> | null, overrides: NewConversationParams | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationParams.ts:4` `import type { NewConversationParams } from "./NewConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationParams.ts:5` `import type { ResponseItem } from "./ResponseItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationParams.ts:6` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationParams.ts:8` `export type ResumeConversationParams = { path: string | null, conversationId: ThreadId | null, history: Array<ResponseItem> | null, overrides: NewConversationParams | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { NewConversationParams } from "./NewConversationParams";`
- `import type { ResponseItem } from "./ResponseItem";`
- `import type { ThreadId } from "./ThreadId";`
- `export type ResumeConversationParams = { path: string | null, conversationId: ThreadId | null, history: Array<ResponseItem> | null, overrides: NewConversationParams | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
