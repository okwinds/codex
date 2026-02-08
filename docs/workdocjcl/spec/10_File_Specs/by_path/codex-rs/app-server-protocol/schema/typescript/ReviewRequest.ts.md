# `codex-rs/app-server-protocol/schema/typescript/ReviewRequest.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `341`
- sha256: `e899ad360ad94175e016f68d957757a490408f1d770bbf5269df4cc27f73cfe0`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ReviewRequest.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewRequest = { target: ReviewTarget, user_facing_hint?: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ReviewRequest.ts:4` `import type { ReviewTarget } from "./ReviewTarget";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ReviewRequest.ts:9` `export type ReviewRequest = { target: ReviewTarget, user_facing_hint?: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReviewTarget } from "./ReviewTarget";`
- `export type ReviewRequest = { target: ReviewTarget, user_facing_hint?: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
