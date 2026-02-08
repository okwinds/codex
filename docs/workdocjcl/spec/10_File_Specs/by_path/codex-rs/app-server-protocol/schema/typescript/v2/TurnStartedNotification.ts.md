# `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `262`
- sha256: `95135229129526d7d9e1db077962210ca5b564adc5fe414ff07e9a65ba43adcf`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnStartedNotification = { threadId: string, turn: Turn, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartedNotification.ts:4` `import type { Turn } from "./Turn";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartedNotification.ts:6` `export type TurnStartedNotification = { threadId: string, turn: Turn, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { Turn } from "./Turn";`
- `export type TurnStartedNotification = { threadId: string, turn: Turn, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
