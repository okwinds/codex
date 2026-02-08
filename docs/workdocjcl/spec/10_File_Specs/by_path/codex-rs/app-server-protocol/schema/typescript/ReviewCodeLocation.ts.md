# `codex-rs/app-server-protocol/schema/typescript/ReviewCodeLocation.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `367`
- sha256: `47b669e5387f06d287d8e7eb47a4d4b6233a8218e9ac8e2ac30298ba59da4d80`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ReviewCodeLocation.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewCodeLocation = { absolute_file_path: string, line_range: ReviewLineRange, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ReviewCodeLocation.ts:4` `import type { ReviewLineRange } from "./ReviewLineRange";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ReviewCodeLocation.ts:9` `export type ReviewCodeLocation = { absolute_file_path: string, line_range: ReviewLineRange, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReviewLineRange } from "./ReviewLineRange";`
- `export type ReviewCodeLocation = { absolute_file_path: string, line_range: ReviewLineRange, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
