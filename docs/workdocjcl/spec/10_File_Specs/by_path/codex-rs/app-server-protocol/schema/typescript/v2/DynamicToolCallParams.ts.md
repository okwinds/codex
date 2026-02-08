# `codex-rs/app-server-protocol/schema/typescript/v2/DynamicToolCallParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `338`
- sha256: `41097193de017ad12ceb6a4b182f01e1093ac7b5a268338710bdc62ca1d09563`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/DynamicToolCallParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type DynamicToolCallParams = { threadId: string, turnId: string, callId: string, tool: string, arguments: JsonValue, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/DynamicToolCallParams.ts:4` `import type { JsonValue } from "../serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/DynamicToolCallParams.ts:6` `export type DynamicToolCallParams = { threadId: string, turnId: string, callId: string, tool: string, arguments: JsonValue, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `export type DynamicToolCallParams = { threadId: string, turnId: string, callId: string, tool: string, arguments: JsonValue, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
