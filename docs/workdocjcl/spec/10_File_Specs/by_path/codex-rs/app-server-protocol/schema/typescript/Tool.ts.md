# `codex-rs/app-server-protocol/schema/typescript/Tool.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `460`
- sha256: `d5e9e622156040df012f8a0769258093132854b64e30b6ec45c8831c11231d92`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/Tool.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Tool = { name: string, title?: string, description?: string, inputSchema: JsonValue, outputSchema?: JsonValue, annotations?: JsonValue, icons?: Array<JsonValue>, _meta?: JsonValue, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/Tool.ts:4` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/Tool.ts:9` `export type Tool = { name: string, title?: string, description?: string, inputSchema: JsonValue, outputSchema?: JsonValue, annotations?: JsonValue, icons?: Array<JsonValue>, _meta?: JsonValue, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type Tool = { name: string, title?: string, description?: string, inputSchema: JsonValue, outputSchema?: JsonValue, annotations?: JsonValue, icons?: Array<JsonValue>, _meta?: JsonValue, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
