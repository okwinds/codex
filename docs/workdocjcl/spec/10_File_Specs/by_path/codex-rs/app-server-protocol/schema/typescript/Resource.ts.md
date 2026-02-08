# `codex-rs/app-server-protocol/schema/typescript/Resource.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `474`
- sha256: `d5b8c1e68332e96ac9281075a30bc231810ceafea795c0a388d8fe0d54596bf1`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/Resource.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Resource = { annotations?: JsonValue, description?: string, mimeType?: string, name: string, size?: number, title?: string, uri: string, icons?: Array<JsonValue>, _meta?: JsonValue, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/Resource.ts:4` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/Resource.ts:9` `export type Resource = { annotations?: JsonValue, description?: string, mimeType?: string, name: string, size?: number, title?: string, uri: string, icons?: Array<JsonValue>, _meta?: JsonValue, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type Resource = { annotations?: JsonValue, description?: string, mimeType?: string, name: string, size?: number, title?: string, uri: string, icons?: Array<JsonValue>, _meta?: JsonValue, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
