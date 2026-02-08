# `codex-rs/app-server-protocol/schema/typescript/WebSearchEndEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `305`
- sha256: `d0eef575a2afff21f8799e22b5f5de4f45ff4597d4e6528c0edc016d1180e826`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/WebSearchEndEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type WebSearchEndEvent = { call_id: string, query: string, action: WebSearchAction, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/WebSearchEndEvent.ts:4` `import type { WebSearchAction } from "./WebSearchAction";`
- `export` `codex-rs/app-server-protocol/schema/typescript/WebSearchEndEvent.ts:6` `export type WebSearchEndEvent = { call_id: string, query: string, action: WebSearchAction, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { WebSearchAction } from "./WebSearchAction";`
- `export type WebSearchEndEvent = { call_id: string, query: string, action: WebSearchAction, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
