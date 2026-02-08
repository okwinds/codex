# `codex-rs/app-server-protocol/schema/typescript/ResourceTemplate.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `436`
- sha256: `f9da8918d1cad3998ee31a01c719f3cecf17ae20eac49910e77b4a7954b472a5`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ResourceTemplate.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ResourceTemplate = { annotations?: JsonValue, uriTemplate: string, name: string, title?: string, description?: string, mimeType?: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ResourceTemplate.ts:4` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ResourceTemplate.ts:9` `export type ResourceTemplate = { annotations?: JsonValue, uriTemplate: string, name: string, title?: string, description?: string, mimeType?: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type ResourceTemplate = { annotations?: JsonValue, uriTemplate: string, name: string, title?: string, description?: string, mimeType?: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
