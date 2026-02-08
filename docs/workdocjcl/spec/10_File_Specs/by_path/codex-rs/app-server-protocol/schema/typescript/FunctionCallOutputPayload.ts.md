# `codex-rs/app-server-protocol/schema/typescript/FunctionCallOutputPayload.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `792`
- sha256: `63789e2ae1a801c103f8606385c1dbfd23c5e6e85894f3ceb94c42cc45081237`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/FunctionCallOutputPayload.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type FunctionCallOutputPayload = { content: string, content_items: Array<FunctionCallOutputContentItem> | null, success: boolean | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/FunctionCallOutputPayload.ts:4` `import type { FunctionCallOutputContentItem } from "./FunctionCallOutputContentItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/FunctionCallOutputPayload.ts:15` `export type FunctionCallOutputPayload = { content: string, content_items: Array<FunctionCallOutputContentItem> | null, success: boolean | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { FunctionCallOutputContentItem } from "./FunctionCallOutputContentItem";`
- `export type FunctionCallOutputPayload = { content: string, content_items: Array<FunctionCallOutputContentItem> | null, success: boolean | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
