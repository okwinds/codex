# `codex-rs/app-server-protocol/schema/typescript/v2/ConfigReadResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `450`
- sha256: `9efa2d02c6ccb42cf509010727c9d27b4ac3783ac8b47e41f92eb6556848cb15`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ConfigReadResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConfigReadResponse = { config: Config, origins: { [key in string]?: ConfigLayerMetadata }, layers: Array<ConfigLayer> | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigReadResponse.ts:4` `import type { Config } from "./Config";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigReadResponse.ts:5` `import type { ConfigLayer } from "./ConfigLayer";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigReadResponse.ts:6` `import type { ConfigLayerMetadata } from "./ConfigLayerMetadata";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigReadResponse.ts:8` `export type ConfigReadResponse = { config: Config, origins: { [key in string]?: ConfigLayerMetadata }, layers: Array<ConfigLayer> | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { Config } from "./Config";`
- `import type { ConfigLayer } from "./ConfigLayer";`
- `import type { ConfigLayerMetadata } from "./ConfigLayerMetadata";`
- `export type ConfigReadResponse = { config: Config, origins: { [key in string]?: ConfigLayerMetadata }, layers: Array<ConfigLayer> | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
