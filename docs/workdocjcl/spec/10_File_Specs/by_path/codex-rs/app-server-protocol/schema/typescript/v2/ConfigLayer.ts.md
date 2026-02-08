# `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayer.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `396`
- sha256: `24d1d2c7e0c774e0df55d767bb6d1874f92776daa96f2856f184a296de203161`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayer.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConfigLayer = { name: ConfigLayerSource, version: string, config: JsonValue, disabledReason: string | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayer.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayer.ts:5` `import type { ConfigLayerSource } from "./ConfigLayerSource";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigLayer.ts:7` `export type ConfigLayer = { name: ConfigLayerSource, version: string, config: JsonValue, disabledReason: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { ConfigLayerSource } from "./ConfigLayerSource";`
- `export type ConfigLayer = { name: ConfigLayerSource, version: string, config: JsonValue, disabledReason: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
