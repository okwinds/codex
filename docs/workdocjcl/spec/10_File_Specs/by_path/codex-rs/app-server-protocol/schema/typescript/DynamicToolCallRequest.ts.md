# `codex-rs/app-server-protocol/schema/typescript/DynamicToolCallRequest.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `320`
- sha256: `34699526fffa604773d4461ac170391cf5f409cc737391ea0d03b38bbbf954ec`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/DynamicToolCallRequest.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type DynamicToolCallRequest = { callId: string, turnId: string, tool: string, arguments: JsonValue, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/DynamicToolCallRequest.ts:4` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/DynamicToolCallRequest.ts:6` `export type DynamicToolCallRequest = { callId: string, turnId: string, tool: string, arguments: JsonValue, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type DynamicToolCallRequest = { callId: string, turnId: string, tool: string, arguments: JsonValue, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
