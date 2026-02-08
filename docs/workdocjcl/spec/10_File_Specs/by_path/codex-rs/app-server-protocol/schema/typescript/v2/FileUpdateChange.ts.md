# `codex-rs/app-server-protocol/schema/typescript/v2/FileUpdateChange.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `298`
- sha256: `71acccec19639609d9a2a7f42de4bc53e540692afcbd29de0735826541dbe5a0`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/FileUpdateChange.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type FileUpdateChange = { path: string, kind: PatchChangeKind, diff: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/FileUpdateChange.ts:4` `import type { PatchChangeKind } from "./PatchChangeKind";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/FileUpdateChange.ts:6` `export type FileUpdateChange = { path: string, kind: PatchChangeKind, diff: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { PatchChangeKind } from "./PatchChangeKind";`
- `export type FileUpdateChange = { path: string, kind: PatchChangeKind, diff: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
