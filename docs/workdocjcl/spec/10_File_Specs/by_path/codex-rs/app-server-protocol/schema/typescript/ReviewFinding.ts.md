# `codex-rs/app-server-protocol/schema/typescript/ReviewFinding.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `441`
- sha256: `24585d39f23fc3e9a2d2853741fb7764c345a3ecb43b114b85a80549a2f5ca9c`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ReviewFinding.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewFinding = { title: string, body: string, confidence_score: number, priority: number, code_location: ReviewCodeLocation, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ReviewFinding.ts:4` `import type { ReviewCodeLocation } from "./ReviewCodeLocation";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ReviewFinding.ts:9` `export type ReviewFinding = { title: string, body: string, confidence_score: number, priority: number, code_location: ReviewCodeLocation, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReviewCodeLocation } from "./ReviewCodeLocation";`
- `export type ReviewFinding = { title: string, body: string, confidence_score: number, priority: number, code_location: ReviewCodeLocation, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
