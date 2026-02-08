# `codex-rs/app-server-protocol/schema/typescript/v2/ReviewStartParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `510`
- sha256: `7ae5a410902a9bc37ad8dc2576ad07bb083710add6a72bb7591d5d3f964a049e`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ReviewStartParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewStartParams = { threadId: string, target: ReviewTarget,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ReviewStartParams.ts:4` `import type { ReviewDelivery } from "./ReviewDelivery";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ReviewStartParams.ts:5` `import type { ReviewTarget } from "./ReviewTarget";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ReviewStartParams.ts:7` `export type ReviewStartParams = { threadId: string, target: ReviewTarget,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReviewDelivery } from "./ReviewDelivery";`
- `import type { ReviewTarget } from "./ReviewTarget";`
- `export type ReviewStartParams = { threadId: string, target: ReviewTarget,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
