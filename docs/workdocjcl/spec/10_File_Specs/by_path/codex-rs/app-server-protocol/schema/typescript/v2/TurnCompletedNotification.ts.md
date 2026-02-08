# `codex-rs/app-server-protocol/schema/typescript/v2/TurnCompletedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `264`
- sha256: `1f56d73cb06876533fb224cd285634d3e090b21b647009be0e7c622937e40d3e`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/TurnCompletedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnCompletedNotification = { threadId: string, turn: Turn, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnCompletedNotification.ts:4` `import type { Turn } from "./Turn";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/TurnCompletedNotification.ts:6` `export type TurnCompletedNotification = { threadId: string, turn: Turn, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { Turn } from "./Turn";`
- `export type TurnCompletedNotification = { threadId: string, turn: Turn, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
