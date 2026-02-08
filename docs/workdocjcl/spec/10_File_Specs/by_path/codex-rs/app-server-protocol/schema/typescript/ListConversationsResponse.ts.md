# `codex-rs/app-server-protocol/schema/typescript/ListConversationsResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `326`
- sha256: `1415d9f797b967ec1604e553eb9a80b82187bfd43e595995d71746d472830ae0`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ListConversationsResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ListConversationsResponse = { items: Array<ConversationSummary>, nextCursor: string | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ListConversationsResponse.ts:4` `import type { ConversationSummary } from "./ConversationSummary";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ListConversationsResponse.ts:6` `export type ListConversationsResponse = { items: Array<ConversationSummary>, nextCursor: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ConversationSummary } from "./ConversationSummary";`
- `export type ListConversationsResponse = { items: Array<ConversationSummary>, nextCursor: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
