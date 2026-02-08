# `codex-rs/app-server-protocol/schema/typescript/v2/ReviewTarget.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `437`
- sha256: `fd0578ec697150df7ab5d7967cc6b2c5e4b87375579b8af2fe0f156a1888251c`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ReviewTarget.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewTarget = { "type": "uncommittedChanges" } | { "type": "baseBranch", branch: string, } | { "type": "commit", sha: string,`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ReviewTarget.ts:5` `export type ReviewTarget = { "type": "uncommittedChanges" } | { "type": "baseBranch", branch: string, } | { "type": "commit", sha: string,`

## Dependencies (auto sample)
### Imports / Includes
- `export type ReviewTarget = { "type": "uncommittedChanges" } | { "type": "baseBranch", branch: string, } | { "type": "commit", sha: string,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
