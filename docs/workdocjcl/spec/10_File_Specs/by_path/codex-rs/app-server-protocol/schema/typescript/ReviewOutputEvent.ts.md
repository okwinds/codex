# `codex-rs/app-server-protocol/schema/typescript/ReviewOutputEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `440`
- sha256: `aa43245e4156fc21613cb2a0b01481371f963735e6f5b03e58b06e5e3312734b`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ReviewOutputEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewOutputEvent = { findings: Array<ReviewFinding>, overall_correctness: string, overall_explanation: string, overall_confidence_score: number, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ReviewOutputEvent.ts:4` `import type { ReviewFinding } from "./ReviewFinding";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ReviewOutputEvent.ts:9` `export type ReviewOutputEvent = { findings: Array<ReviewFinding>, overall_correctness: string, overall_explanation: string, overall_confidence_score: number, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReviewFinding } from "./ReviewFinding";`
- `export type ReviewOutputEvent = { findings: Array<ReviewFinding>, overall_correctness: string, overall_explanation: string, overall_confidence_score: number, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
