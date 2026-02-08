# `codex-rs/app-server-protocol/schema/typescript/v2/ConfigEdit.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `360`
- sha256: `67ee51dde287fc9587981fa1da666fd8ff5eedc5123fc72025807d1812e31543`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ConfigEdit.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConfigEdit = { keyPath: string, value: JsonValue, mergeStrategy: MergeStrategy, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigEdit.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigEdit.ts:5` `import type { MergeStrategy } from "./MergeStrategy";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigEdit.ts:7` `export type ConfigEdit = { keyPath: string, value: JsonValue, mergeStrategy: MergeStrategy, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { MergeStrategy } from "./MergeStrategy";`
- `export type ConfigEdit = { keyPath: string, value: JsonValue, mergeStrategy: MergeStrategy, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
