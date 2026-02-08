# `codex-rs/app-server-protocol/schema/typescript/ExitedReviewModeEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `297`
- sha256: `8c7741d08f88d9af90a7dc7982f1e62e586b8e145a3ceb6a4c0924decbe913f7`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ExitedReviewModeEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ExitedReviewModeEvent = { review_output: ReviewOutputEvent | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ExitedReviewModeEvent.ts:4` `import type { ReviewOutputEvent } from "./ReviewOutputEvent";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ExitedReviewModeEvent.ts:6` `export type ExitedReviewModeEvent = { review_output: ReviewOutputEvent | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReviewOutputEvent } from "./ReviewOutputEvent";`
- `export type ExitedReviewModeEvent = { review_output: ReviewOutputEvent | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
