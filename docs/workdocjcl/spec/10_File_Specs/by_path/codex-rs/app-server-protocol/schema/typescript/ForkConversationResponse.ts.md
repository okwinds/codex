# `codex-rs/app-server-protocol/schema/typescript/ForkConversationResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `388`
- sha256: `505c873e477b60d6bcead578a7db0a41eacf9f6cf0b827cef38b0ce53488fa8c`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ForkConversationResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ForkConversationResponse = { conversationId: ThreadId, model: string, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ForkConversationResponse.ts:4` `import type { EventMsg } from "./EventMsg";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ForkConversationResponse.ts:5` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ForkConversationResponse.ts:7` `export type ForkConversationResponse = { conversationId: ThreadId, model: string, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { EventMsg } from "./EventMsg";`
- `import type { ThreadId } from "./ThreadId";`
- `export type ForkConversationResponse = { conversationId: ThreadId, model: string, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
