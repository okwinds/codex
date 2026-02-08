# `codex-rs/app-server-protocol/schema/typescript/GetConversationSummaryParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `298`
- sha256: `1e419864686b73b516ae209cefe0f5efc15cb9055183ea0451fbbaef42afa81f`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/GetConversationSummaryParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type GetConversationSummaryParams = { rolloutPath: string, } | { conversationId: ThreadId, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/GetConversationSummaryParams.ts:4` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/GetConversationSummaryParams.ts:6` `export type GetConversationSummaryParams = { rolloutPath: string, } | { conversationId: ThreadId, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadId } from "./ThreadId";`
- `export type GetConversationSummaryParams = { rolloutPath: string, } | { conversationId: ThreadId, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
