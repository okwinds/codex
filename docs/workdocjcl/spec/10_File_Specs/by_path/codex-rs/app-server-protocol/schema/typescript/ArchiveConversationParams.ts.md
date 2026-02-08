# `codex-rs/app-server-protocol/schema/typescript/ArchiveConversationParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `289`
- sha256: `5240782dddb096db19899f05bcb647fcf26de22454790d90e2f7e833facaf328`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ArchiveConversationParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ArchiveConversationParams = { conversationId: ThreadId, rolloutPath: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ArchiveConversationParams.ts:4` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ArchiveConversationParams.ts:6` `export type ArchiveConversationParams = { conversationId: ThreadId, rolloutPath: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadId } from "./ThreadId";`
- `export type ArchiveConversationParams = { conversationId: ThreadId, rolloutPath: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
