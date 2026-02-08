# `codex-rs/app-server-protocol/schema/typescript/v2/ItemCompletedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `298`
- sha256: `ba347219616a9ff497f84622af5ff337ba13b6dfbfd4e6722a2438c03a038065`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ItemCompletedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ItemCompletedNotification = { item: ThreadItem, threadId: string, turnId: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ItemCompletedNotification.ts:4` `import type { ThreadItem } from "./ThreadItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ItemCompletedNotification.ts:6` `export type ItemCompletedNotification = { item: ThreadItem, threadId: string, turnId: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadItem } from "./ThreadItem";`
- `export type ItemCompletedNotification = { item: ThreadItem, threadId: string, turnId: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
