# `codex-rs/app-server-protocol/schema/typescript/FileChange.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `328`
- sha256: `831feada4d69f7049a174ff7abdd49797b4a2a28ba2a2167f44f1aa17b6f3520`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/FileChange.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type FileChange = { "type": "add", content: string, } | { "type": "delete", content: string, } | { "type": "update", unified_diff: string, move_path: string | null, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/FileChange.ts:5` `export type FileChange = { "type": "add", content: string, } | { "type": "delete", content: string, } | { "type": "update", unified_diff: string, move_path: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type FileChange = { "type": "add", content: string, } | { "type": "delete", content: string, } | { "type": "update", unified_diff: string, move_path: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
