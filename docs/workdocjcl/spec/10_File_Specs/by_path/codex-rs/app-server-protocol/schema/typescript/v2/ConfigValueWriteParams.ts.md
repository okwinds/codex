# `codex-rs/app-server-protocol/schema/typescript/v2/ConfigValueWriteParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `528`
- sha256: `e99e256fa03e7dabc36f2bbf7a696e00bf76d49ed9e12d14b6aa055d13b3ff61`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ConfigValueWriteParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConfigValueWriteParams = { keyPath: string, value: JsonValue, mergeStrategy: MergeStrategy,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigValueWriteParams.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigValueWriteParams.ts:5` `import type { MergeStrategy } from "./MergeStrategy";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigValueWriteParams.ts:7` `export type ConfigValueWriteParams = { keyPath: string, value: JsonValue, mergeStrategy: MergeStrategy,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { MergeStrategy } from "./MergeStrategy";`
- `export type ConfigValueWriteParams = { keyPath: string, value: JsonValue, mergeStrategy: MergeStrategy,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
