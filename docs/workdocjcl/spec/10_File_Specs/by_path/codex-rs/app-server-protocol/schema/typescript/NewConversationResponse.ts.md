# `codex-rs/app-server-protocol/schema/typescript/NewConversationResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `401`
- sha256: `97a91e23b000d71d7b842fa2934bff94fa3d196e928aefdaf047dc9a8fbf95e0`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/NewConversationResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type NewConversationResponse = { conversationId: ThreadId, model: string, reasoningEffort: ReasoningEffort | null, rolloutPath: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/NewConversationResponse.ts:4` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/NewConversationResponse.ts:5` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/NewConversationResponse.ts:7` `export type NewConversationResponse = { conversationId: ThreadId, model: string, reasoningEffort: ReasoningEffort | null, rolloutPath: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import type { ThreadId } from "./ThreadId";`
- `export type NewConversationResponse = { conversationId: ThreadId, model: string, reasoningEffort: ReasoningEffort | null, rolloutPath: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
