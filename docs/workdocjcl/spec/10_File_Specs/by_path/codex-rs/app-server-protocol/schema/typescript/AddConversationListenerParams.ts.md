# `codex-rs/app-server-protocol/schema/typescript/AddConversationListenerParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `304`
- sha256: `98f0454e648aab5a35af6497f0f4a07beeb650db5d2b9d8ed09a168c7788b302`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/AddConversationListenerParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AddConversationListenerParams = { conversationId: ThreadId, experimentalRawEvents: boolean, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/AddConversationListenerParams.ts:4` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/AddConversationListenerParams.ts:6` `export type AddConversationListenerParams = { conversationId: ThreadId, experimentalRawEvents: boolean, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadId } from "./ThreadId";`
- `export type AddConversationListenerParams = { conversationId: ThreadId, experimentalRawEvents: boolean, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
