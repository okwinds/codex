# `codex-rs/app-server-protocol/schema/typescript/v2/OverriddenMetadata.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `397`
- sha256: `5fd0c4e3191494dd262616335858b44fb635ae9d2a02e39632cdcf02acca0d68`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/OverriddenMetadata.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type OverriddenMetadata = { message: string, overridingLayer: ConfigLayerMetadata, effectiveValue: JsonValue, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/OverriddenMetadata.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/OverriddenMetadata.ts:5` `import type { ConfigLayerMetadata } from "./ConfigLayerMetadata";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/OverriddenMetadata.ts:7` `export type OverriddenMetadata = { message: string, overridingLayer: ConfigLayerMetadata, effectiveValue: JsonValue, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { ConfigLayerMetadata } from "./ConfigLayerMetadata";`
- `export type OverriddenMetadata = { message: string, overridingLayer: ConfigLayerMetadata, effectiveValue: JsonValue, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
