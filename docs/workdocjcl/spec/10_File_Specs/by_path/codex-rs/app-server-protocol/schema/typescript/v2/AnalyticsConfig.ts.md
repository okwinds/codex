# `codex-rs/app-server-protocol/schema/typescript/v2/AnalyticsConfig.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `383`
- sha256: `3273d6b13fe0a7af66a315c499d0d89393ea7ae440af980004c5382504d5aa4a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/AnalyticsConfig.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AnalyticsConfig = { enabled: boolean | null, } & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/AnalyticsConfig.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/AnalyticsConfig.ts:6` `export type AnalyticsConfig = { enabled: boolean | null, } & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `export type AnalyticsConfig = { enabled: boolean | null, } & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
