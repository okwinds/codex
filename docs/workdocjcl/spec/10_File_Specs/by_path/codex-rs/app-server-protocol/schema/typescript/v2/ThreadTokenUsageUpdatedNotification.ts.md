# `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsageUpdatedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `332`
- sha256: `53ce4421d686b8a7f9a86c5ad54de2a7dceecfb95df74fa5f441947e136f063d`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsageUpdatedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ThreadTokenUsageUpdatedNotification = { threadId: string, turnId: string, tokenUsage: ThreadTokenUsage, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsageUpdatedNotification.ts:4` `import type { ThreadTokenUsage } from "./ThreadTokenUsage";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsageUpdatedNotification.ts:6` `export type ThreadTokenUsageUpdatedNotification = { threadId: string, turnId: string, tokenUsage: ThreadTokenUsage, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadTokenUsage } from "./ThreadTokenUsage";`
- `export type ThreadTokenUsageUpdatedNotification = { threadId: string, turnId: string, tokenUsage: ThreadTokenUsage, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
