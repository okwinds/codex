# `codex-rs/app-server-protocol/schema/typescript/ResumeConversationResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `390`
- sha256: `697f040b539a5d5cc13077781a91b14088676468104b7e4cd7e25f6887dfbf1e`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ResumeConversationResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ResumeConversationResponse = { conversationId: ThreadId, model: string, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationResponse.ts:4` `import type { EventMsg } from "./EventMsg";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationResponse.ts:5` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ResumeConversationResponse.ts:7` `export type ResumeConversationResponse = { conversationId: ThreadId, model: string, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { EventMsg } from "./EventMsg";`
- `import type { ThreadId } from "./ThreadId";`
- `export type ResumeConversationResponse = { conversationId: ThreadId, model: string, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
