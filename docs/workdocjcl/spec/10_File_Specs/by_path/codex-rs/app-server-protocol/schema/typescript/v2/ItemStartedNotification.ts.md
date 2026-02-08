# `codex-rs/app-server-protocol/schema/typescript/v2/ItemStartedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `296`
- sha256: `adc1ff5954da47cb28fe823a0b842d285266f346b65fe1b211a74136975c5be3`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ItemStartedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ItemStartedNotification = { item: ThreadItem, threadId: string, turnId: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ItemStartedNotification.ts:4` `import type { ThreadItem } from "./ThreadItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ItemStartedNotification.ts:6` `export type ItemStartedNotification = { item: ThreadItem, threadId: string, turnId: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadItem } from "./ThreadItem";`
- `export type ItemStartedNotification = { item: ThreadItem, threadId: string, turnId: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
