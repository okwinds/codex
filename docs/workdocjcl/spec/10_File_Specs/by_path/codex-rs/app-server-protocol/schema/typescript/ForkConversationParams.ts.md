# `codex-rs/app-server-protocol/schema/typescript/ForkConversationParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `404`
- sha256: `25575fab1feb9a159f8ba59717ab937d7fad958cd87fa4a6b3e6fc78b4f84214`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ForkConversationParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ForkConversationParams = { path: string | null, conversationId: ThreadId | null, overrides: NewConversationParams | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ForkConversationParams.ts:4` `import type { NewConversationParams } from "./NewConversationParams";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ForkConversationParams.ts:5` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ForkConversationParams.ts:7` `export type ForkConversationParams = { path: string | null, conversationId: ThreadId | null, overrides: NewConversationParams | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { NewConversationParams } from "./NewConversationParams";`
- `import type { ThreadId } from "./ThreadId";`
- `export type ForkConversationParams = { path: string | null, conversationId: ThreadId | null, overrides: NewConversationParams | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
