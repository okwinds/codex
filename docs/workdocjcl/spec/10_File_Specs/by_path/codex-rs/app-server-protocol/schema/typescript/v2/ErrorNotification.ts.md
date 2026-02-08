# `codex-rs/app-server-protocol/schema/typescript/v2/ErrorNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `308`
- sha256: `f30701035a45042495c0cbf41d4002f9e1a2c2b8c41bd4762ed6588338c6d5e1`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ErrorNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ErrorNotification = { error: TurnError, willRetry: boolean, threadId: string, turnId: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ErrorNotification.ts:4` `import type { TurnError } from "./TurnError";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ErrorNotification.ts:6` `export type ErrorNotification = { error: TurnError, willRetry: boolean, threadId: string, turnId: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { TurnError } from "./TurnError";`
- `export type ErrorNotification = { error: TurnError, willRetry: boolean, threadId: string, turnId: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
