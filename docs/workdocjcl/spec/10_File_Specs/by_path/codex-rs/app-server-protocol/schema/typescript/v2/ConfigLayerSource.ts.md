# `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayerSource.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `795`
- sha256: `dec237f4a0d93eae36cc04f1ed333babf8451c0416e96dd697c8ed0fcada6280`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayerSource.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConfigLayerSource = { "type": "mdm", domain: string, key: string, } | { "type": "system",`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayerSource.ts:4` `import type { AbsolutePathBuf } from "../AbsolutePathBuf";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayerSource.ts:6` `export type ConfigLayerSource = { "type": "mdm", domain: string, key: string, } | { "type": "system",`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AbsolutePathBuf } from "../AbsolutePathBuf";`
- `export type ConfigLayerSource = { "type": "mdm", domain: string, key: string, } | { "type": "system",`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
