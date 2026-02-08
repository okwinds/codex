# `codex-rs/app-server-protocol/schema/typescript/v2/RawResponseItemCompletedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `316`
- sha256: `b5b6a62552ff5441a7fe2a1e762fef812b8bdbcad403adc59fdd4a5b90faf0c7`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/RawResponseItemCompletedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type RawResponseItemCompletedNotification = { threadId: string, turnId: string, item: ResponseItem, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/RawResponseItemCompletedNotification.ts:4` `import type { ResponseItem } from "../ResponseItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/RawResponseItemCompletedNotification.ts:6` `export type RawResponseItemCompletedNotification = { threadId: string, turnId: string, item: ResponseItem, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ResponseItem } from "../ResponseItem";`
- `export type RawResponseItemCompletedNotification = { threadId: string, turnId: string, item: ResponseItem, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
