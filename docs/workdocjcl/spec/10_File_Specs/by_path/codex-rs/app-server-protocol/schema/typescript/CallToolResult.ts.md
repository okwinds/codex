# `codex-rs/app-server-protocol/schema/typescript/CallToolResult.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `389`
- sha256: `6c097e5c19fce49daf3a54e06556d3186a78640e651aae2b9aedfce2d4769d66`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/CallToolResult.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CallToolResult = { content: Array<JsonValue>, structuredContent?: JsonValue, isError?: boolean, _meta?: JsonValue, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/CallToolResult.ts:4` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/CallToolResult.ts:9` `export type CallToolResult = { content: Array<JsonValue>, structuredContent?: JsonValue, isError?: boolean, _meta?: JsonValue, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type CallToolResult = { content: Array<JsonValue>, structuredContent?: JsonValue, isError?: boolean, _meta?: JsonValue, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
