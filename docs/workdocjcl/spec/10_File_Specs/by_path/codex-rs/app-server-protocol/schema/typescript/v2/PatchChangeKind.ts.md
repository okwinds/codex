# `codex-rs/app-server-protocol/schema/typescript/v2/PatchChangeKind.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `275`
- sha256: `20e95907d698efbef2fa9d9ab00392b10caf127dfc5e0df1ba9878ad6f42531d`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/PatchChangeKind.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type PatchChangeKind = { "type": "add" } | { "type": "delete" } | { "type": "update", move_path: string | null, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/PatchChangeKind.ts:5` `export type PatchChangeKind = { "type": "add" } | { "type": "delete" } | { "type": "update", move_path: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type PatchChangeKind = { "type": "add" } | { "type": "delete" } | { "type": "update", move_path: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
