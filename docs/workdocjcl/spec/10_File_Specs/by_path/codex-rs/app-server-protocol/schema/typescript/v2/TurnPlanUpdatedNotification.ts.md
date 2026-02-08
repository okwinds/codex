# `codex-rs/app-server-protocol/schema/typescript/v2/TurnPlanUpdatedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `341`
- sha256: `9f7505555f199125bc2774878d488a3dcbc4d7304a54967993e68053d9915d01`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/TurnPlanUpdatedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnPlanUpdatedNotification = { threadId: string, turnId: string, explanation: string | null, plan: Array<TurnPlanStep>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnPlanUpdatedNotification.ts:4` `import type { TurnPlanStep } from "./TurnPlanStep";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/TurnPlanUpdatedNotification.ts:6` `export type TurnPlanUpdatedNotification = { threadId: string, turnId: string, explanation: string | null, plan: Array<TurnPlanStep>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { TurnPlanStep } from "./TurnPlanStep";`
- `export type TurnPlanUpdatedNotification = { threadId: string, turnId: string, explanation: string | null, plan: Array<TurnPlanStep>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
